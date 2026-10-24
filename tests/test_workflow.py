"""End-to-end workflow, resilience, idempotency, and card schema tests (T07, T08, T09, T10)."""

import json
import pytest
from controller import SentinelFlowController
from tools.simulated_response import reset_state_store, verify_containment_state, execute_simulated_action
from cards import build_risk_assessment_card, build_verification_receipt_card
from chat_proto import parse_card_selection, extract_target_from_text


@pytest.fixture(autouse=True)
def clean_state():
    reset_state_store()


def test_t07_tool_failure_resilience():
    """T07: When log search or backend tools fail, report clean failure instead of hallucinating success."""
    controller = SentinelFlowController()
    res = controller.process_investigation_request(
        intent="investigate_suspicious_logins",
        target="demo-user-104",
        simulate_tool_failure=True,
    )
    assert res["status"] == "failed"
    assert res["error_stage"] == "log_search"
    assert "timeout" in res["message"].lower() or "failed" in res["message"].lower()


def test_t08_verification_mismatch_detection():
    """T08: When a simulated action claims success but target state didn't change, verifier reports failure."""
    controller = SentinelFlowController()
    # Authorize action but simulate verification mismatch
    res = controller.process_investigation_request(
        intent="request_containment",
        target="demo-user-104",
        requested_action="revoke_user_sessions",
        approval_token="APPROVED_BY_ANALYST",
        simulate_verify_mismatch=True,
    )
    assert res["status"] == "failed"
    assert res["verification"] is not None
    assert res["verification"]["verified"] is False
    assert "FAILED" in res["verification"]["details"]


def test_t09_idempotency_duplicate_containment():
    """T09: Repeated containment requests on the same target return existing record without duplicate actions."""
    # First action
    res1 = execute_simulated_action("revoke_user_sessions", "demo-user-104")
    assert res1["status"] == "executed"
    act_id1 = res1["action_id"]

    # Duplicate action
    res2 = execute_simulated_action("revoke_user_sessions", "demo-user-104")
    assert res2["status"] == "duplicate_prevented"
    assert res2["action_id"] == act_id1


def test_t10_asi_one_interactive_cards_and_parsing():
    """T10: Validate ASI:One dynamic card schema structure and selection parsing."""
    from cards import (
        build_response_approval_card,
        build_verification_receipt_card,
        build_forensic_details_card,
        build_welcome_card,
    )

    # 1. Card A (Risk Assessment)
    card_a = build_risk_assessment_card(
        target="demo-user-104",
        risk_level="high",
        risk_score=85,
        evidence=["Multiple failed logins", "Anomalous location"],
        mitre_tactics=["T1110 - Brute Force"],
        summary="Suspicious burst detected.",
    )
    assert "root" in card_a
    assert card_a["root"]["type"] == "section"
    assert len(card_a["root"]["children"]) > 0

    # 2. Card B (Response Approval)
    card_b = build_response_approval_card(
        target="demo-user-104",
        risk_level="critical",
        proposed_action="revoke_user_sessions",
        fee="0.1 FET",
    )
    assert "root" in card_b
    assert card_b["root"]["type"] == "section"
    # Verify presence of interactive decision buttons
    buttons = [
        child for child in card_b["root"]["children"]
        if child.get("type") == "group" and any(c.get("type") == "button" for c in child.get("children", []))
    ]
    assert len(buttons) > 0

    # 3. Card C (Verification Receipt)
    card_c = build_verification_receipt_card(
        action_id="act-test-01",
        target="demo-user-104",
        action_type="revoke_user_sessions",
        actual_state="sessions_revoked",
        audit_hash="a"*64,
        timestamp="2026-10-24T12:00:00Z",
    )
    assert "root" in card_c

    # 4. Card D (Forensics) & Card E (Welcome)
    card_d = build_forensic_details_card(target="demo-user-104", risk_score=85, evidence=["Signal 1"])
    assert "root" in card_d
    card_e = build_welcome_card()
    assert "root" in card_e

    # 5. Format 1: Structured JSON button click parsing
    raw_button_click = json.dumps({
        "selection": {
            "action": "approve_containment",
            "target": "demo-user-104",
            "action_type": "revoke_user_sessions",
            "token": "CARD_ACTION_APPROVE",
            "fee": "0.1 FET",
        }
    })
    parsed_json = parse_card_selection(raw_button_click)
    assert parsed_json is not None
    assert parsed_json["action"] == "approve_containment"
    assert parsed_json["target"] == "demo-user-104"
    assert parsed_json["action_type"] == "revoke_user_sessions"

    # 6. Format 2: Natural Language text parsing
    p_approve = parse_card_selection("Approve session revocation")
    assert p_approve is not None and p_approve["action"] == "approve_containment"

    p_reject = parse_card_selection("Reject the action")
    assert p_reject is not None and p_reject["action"] == "dismiss_incident"

    p_info = parse_card_selection("Request more information")
    assert p_info is not None and p_info["action"] == "request_more_info"

    p_block = parse_card_selection("Block attacker IP")
    assert p_block is not None and p_block["action_type"] == "block_ip_address"

    # 7. Target regex extractor
    extracted = extract_target_from_text("Please investigate suspicious events on demo-user-104 immediately")
    assert extracted == "demo-user-104"


def test_t13_consumer_emergency_lock_and_email_flow():
    """T13: Validate Real-World Consumer 'Emergency Lock' Mode with arbitrary email and 0.1 FET."""
    from cards import (
        build_consumer_alert_card,
        build_consumer_lockdown_card,
        build_consumer_safety_certificate_card,
    )
    from tools.log_search import search_logs

    # 1. Arbitrary consumer email query parsing
    consumer_input = "Someone hacked my account alex@gmail.com please help"
    parsed = parse_card_selection(consumer_input)
    assert parsed is not None
    assert parsed["action"] == "investigate_target"
    assert parsed["target"] == "alex@gmail.com"
    assert parsed["mode"] == "consumer"

    # 2. Dynamic consumer log telemetry lookup
    telemetry = search_logs(account_id="alex@gmail.com")
    assert telemetry["matches_found"] > 0
    assert any("Lagos, Nigeria" in str(evt.get("location")) for evt in telemetry["events"])

    # 3. Consumer Card builders
    alert_card = build_consumer_alert_card(target="alex@gmail.com", risk_score=85)
    assert "root" in alert_card
    assert alert_card["root"]["title"] == "🚨 Account Security Alert"

    lockdown_card = build_consumer_lockdown_card(target="alex@gmail.com", fee="0.1 FET (~$0.12)")
    assert "root" in lockdown_card
    assert lockdown_card["root"]["title"] == "🛡️ 1-Tap Emergency Account Lockdown"

    cert_card = build_consumer_safety_certificate_card(
        target="alex@gmail.com",
        action_id="act-consumer-01",
        audit_hash="f"*64,
        timestamp="2026-10-24T12:00:00Z",
    )
    assert "root" in cert_card
    assert cert_card["root"]["title"] == "✅ Account Successfully Secured!"

    # 4. Consumer 1-tap lock input parsing
    lock_click = parse_card_selection("Lock my account now")
    assert lock_click is not None
    assert lock_click["action"] == "approve_containment"
    assert lock_click["mode"] == "consumer"

    # 5. Consumer "It was me" parsing
    safe_click = parse_card_selection("It was me")
    assert safe_click is not None
    assert safe_click["action"] == "it_was_me"

    # 6. Informational Summary Report Card builder
    from cards import build_summary_report_card, build_summary_report_message
    summary_card = build_summary_report_card()
    assert "root" in summary_card
    assert any("High-Risk" in str(ch.get("value", "")) for ch in summary_card["root"]["children"])

    summary_msg = build_summary_report_message("Incident summary")
    assert summary_msg.content[1].metadata["card_kind"] == "custom"



def test_t14_conversational_human_parsing_and_agent_mention_stripping():
    """T14: Validate conversational human dialogue, agent address mention stripping, and 1-4 numeric shortcuts."""
    # 1. Bare agent address mention (user tagging agent without text)
    bare_mention = parse_card_selection("@agent1qwstka0f7sjyd0ux69zfv9pu66testhc807cdhx8yvav3u0eml7nwptkdfy")
    assert bare_mention is not None
    assert bare_mention["action"] == "welcome"

    # 2. Agent mention prefix with numeric shortcode 1
    tagged_1 = parse_card_selection("@agent1qwstka0f7sjyd0ux69zfv9pu66testhc807cdhx8yvav3u0eml7nwptkdfy 1")
    assert tagged_1 is not None
    assert tagged_1["action"] == "investigate_target"
    assert tagged_1["mode"] == "consumer"

    # 3. Numeric shortcuts 1, 2, 3, 4
    assert parse_card_selection("1")["action"] == "investigate_target"
    assert parse_card_selection("2")["action"] == "approve_containment"
    assert parse_card_selection("3")["action"] == "request_more_info"
    assert parse_card_selection("4")["action"] == "investigate_target"

    # 4. Human conversational phrases without jargon
    kick = parse_card_selection("kick them out")
    assert kick is not None
    assert kick["action"] == "approve_containment"
    assert kick["mode"] == "consumer"

    check = parse_card_selection("is my account safe")
    assert check is not None
    assert check["action"] == "investigate_target"
    assert check["mode"] == "consumer"

    who = parse_card_selection("who are you")
    assert who is not None
    assert who["action"] == "welcome"


def test_t15_agentverse_benchmark_evaluations():
    """T15: Validate exact handling of all 5 Agentverse benchmark evaluation prompts."""
    # Benchmark Prompt 1: Login history request
    p1 = "Can you show me the login history for my account so I can see who accessed it recently?"
    res1 = parse_card_selection(p1)
    assert res1 is not None
    assert res1["action"] == "request_more_info"
    assert res1["target"] == "demo-user-104"

    # Benchmark Prompt 2: Verification / Re-entry explanation
    p2 = "After you kick out the intruder, how do I know for sure they're actually gone and can't get back in?"
    res2 = parse_card_selection(p2)
    assert res2 is not None
    assert res2["action"] == "verification_explanation"

    # Benchmark Prompt 3: Pricing inquiry
    p3 = "Someone logged into my account from a device I don't recognize. How much will it cost to kick them out and lock my account right now?"
    res3 = parse_card_selection(p3)
    assert res3 is not None
    assert res3["action"] == "pricing_info"

    # Benchmark Prompt 4: Scan alex@gmail.com for suspicious logins
    p4 = "I think someone got into my email account — can you scan alex@gmail.com and tell me if there are any suspicious logins?"
    res4 = parse_card_selection(p4)
    assert res4 is not None
    assert res4["action"] == "investigate_target"
    assert res4["target"] == "alex@gmail.com"
    # Ensure controller detects breach on alex@gmail.com
    controller = SentinelFlowController()
    inv_res = controller.process_investigation_request(
        intent="investigate_suspicious_logins",
        target=res4["target"],
    )
    assert inv_res["status"] == "needs_confirmation"
    assert inv_res["risk_score"] >= 75
    assert inv_res["risk_level"] in ("high", "critical")
    assert any("Lagos, Nigeria" in ev or "unfamiliar location" in ev for ev in inv_res["evidence"])

    # Benchmark Prompt 5: SHA-256 safety certificate inquiry
    p5 = "What is the SHA-256 safety certificate and how can I use it as proof that my account is secure?"
    res5 = parse_card_selection(p5)
    assert res5 is not None
    assert res5["action"] == "sha256_explanation"

    # Benchmark Prompt 6: High-risk summary report request
    p6 = "Generate a summary report of all high-risk authentication events"
    res6 = parse_card_selection(p6)
    assert res6 is not None
    assert res6["action"] == "summary_report"





