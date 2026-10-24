#!/usr/bin/env python3
"""Generate a beautiful, professional 16:9 PowerPoint presentation for SentinelFlow.

Design:
- 16:9 Widescreen (13.333 x 7.5 inches)
- Deep Cyber Dark Aesthetic: Dark Navy/Obsidian (#080C16), Electric Cyan (#00F0FF), Pure White (#FFFFFF), Tech Gray (#94A3B8)
- Structured Workflow:
  1. Title & Overview
  2. The Problem Statement (The Panic Window)
  3. The Proposed Solution (SentinelFlow Swarm)
  4. 5-Agent Multi-Agent Architecture
  5. Overview of Existing Tools
  6. Competitive Differentiation (Why We Win)
  7. Real-World Business Models
  8. Live Deployment, Agentverse & Verification
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SentinelFlow_Presentation.pptx")

# Palette
BG_COLOR = RGBColor(8, 12, 22)        # #080C16
CARD_BG = RGBColor(17, 26, 46)        # #111A2E
CARD_BORDER = RGBColor(0, 240, 255)   # #00F0FF
TEXT_WHITE = RGBColor(255, 255, 255)
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
TEXT_CYAN = RGBColor(0, 240, 255)     # #00F0FF
TEXT_GREEN = RGBColor(16, 185, 129)   # #10B981
TEXT_RED = RGBColor(239, 68, 68)      # #EF4444
TEXT_YELLOW = RGBColor(245, 158, 11)  # #F59E0B


def create_deck():
    prs = Presentation()
    # 16:9 Widescreen Dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, category: str, title: str):
        # Category tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = TEXT_CYAN
        p_cat.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.font.name = "Arial"

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Accent glow rectangle
    glow = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(0.1), Inches(3.6))
    glow.fill.solid()
    glow.fill.fore_color.rgb = TEXT_CYAN
    glow.line.fill.background()

    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11), Inches(4.5))
    tf = tbox.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "FETCH.AI & ASI:ONE INNOVATION HACKATHON 2026"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_CYAN
    p0.font.name = "Arial"
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = "SentinelFlow"
    p1.font.size = Pt(48)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.font.name = "Arial"
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "The Autonomous 24/7 AI Bodyguard for Everyday Accounts"
    p2.font.size = Pt(22)
    p2.font.color.rgb = TEXT_CYAN
    p2.font.name = "Arial"
    p2.space_after = Pt(18)

    p3 = tf.add_paragraph()
    p3.text = "Sub-Second Account Takeover Defense • 0.1 FET Micropayments • Verifiable SHA-256 Proof"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED
    p3.font.name = "Arial"
    p3.space_after = Pt(36)

    p4 = tf.add_paragraph()
    p4.text = "Team F-ups: Meer Mohammed Shoaib • Mohammed Maaz • Prithvi S"
    p4.font.size = Pt(13)
    p4.font.color.rgb = TEXT_WHITE
    p4.font.name = "Arial"

    # =========================================================================
    # SLIDE 2: Problem Statement (The Panic Window)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "1. Problem Statement", "The 'Panic Window' — Why Account Takeovers Are Devastating")

    cards2 = [
        {
            "num": "01",
            "title": "The 2:00 AM Crisis",
            "subtitle": "Immediate Shock & Panic",
            "body": "An everyday user receives an alert: 'Unauthorized login from Lagos, Nigeria'. The attacker is actively guessing passwords and bypassing MFA while the victim sleeps.",
            "color": TEXT_RED,
        },
        {
            "num": "02",
            "title": "The 48-Hour Black Hole",
            "subtitle": "Customer Support Latency",
            "body": "Victims send an urgent ticket to support. Industry average response time is 24 to 48 hours. By the time human support reads the email, the damage is irreversible.",
            "color": TEXT_YELLOW,
        },
        {
            "num": "03",
            "title": "The Irreversible Damage",
            "subtitle": "Total Identity & Asset Loss",
            "body": "Within 4 minutes, attackers forward emails, change recovery phones, drain crypto wallets, and execute fraudulent credit card transactions.",
            "color": TEXT_RED,
        },
        {
            "num": "04",
            "title": "The Enterprise Cost Gap",
            "subtitle": "$50,000+ Enterprise Barrier",
            "body": "Enterprise automated SOAR tools (CrowdStrike, Palo Alto) cost over $50k/year and require a Tier-3 SOC team. Everyday people and small teams have zero real-time defense.",
            "color": TEXT_CYAN,
        },
    ]

    card_w = Inches(2.7)
    gap = Inches(0.28)
    left_start = Inches(0.8)
    top_pos = Inches(2.2)

    for i, c in enumerate(cards2):
        pos_left = left_start + i * (card_w + gap)
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_left, top_pos, card_w, Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = c["color"]
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = c["num"]
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = c["color"]
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = c["title"]
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(4)

        p = tf.add_paragraph()
        p.text = c["subtitle"]
        p.font.size = Pt(11)
        p.font.color.rgb = c["color"]
        p.space_after = Pt(14)

        p = tf.add_paragraph()
        p.text = c["body"]
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: Proposed Solution (SentinelFlow)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "2. Proposed Solution", "SentinelFlow: Autonomous Multi-Agent SecOps on Fetch.ai")

    sol_cards = [
        {
            "step": "Step 1",
            "title": "Instant Detection (Free)",
            "desc": "Investigator Agent correlates SIEM authentication logs in milliseconds. Spots brute-force bursts, impossible travel, and unauthorized MFA bypass attempts.",
            "stat": "< 500 ms",
            "stat_label": "Detection Latency",
            "color": TEXT_CYAN,
        },
        {
            "step": "Step 2",
            "title": "1-Tap Severance (0.1 FET)",
            "desc": "Victim taps 'Kick them out' or confirms via ACP chat. Containment Agent instantly invalidates OAuth tokens, revokes sessions everywhere, and firewalls the attacker IP.",
            "stat": "1 Second",
            "stat_label": "Response Time (~$0.10)",
            "color": TEXT_YELLOW,
        },
        {
            "step": "Step 3",
            "title": "Cryptographic Proof (Free)",
            "desc": "Auditor Agent independently inspects post-action state to verify 0 active sessions remain, computing an immutable SHA-256 certificate for bank & insurance records.",
            "stat": "SHA-256",
            "stat_label": "Verifiable Proof",
            "color": TEXT_GREEN,
        },
    ]

    card_w3 = Inches(3.7)
    gap3 = Inches(0.35)
    for i, c in enumerate(sol_cards):
        pos_left = Inches(0.8) + i * (card_w3 + gap3)
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_left, Inches(2.2), card_w3, Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = c["color"]
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = c["step"].upper()
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = c["color"]
        p.space_after = Pt(10)

        p = tf.add_paragraph()
        p.text = c["title"]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(14)

        p = tf.add_paragraph()
        p.text = c["desc"]
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(24)

        # Highlight Stat
        p = tf.add_paragraph()
        p.text = c["stat"]
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = c["color"]

        p = tf.add_paragraph()
        p.text = c["stat_label"]
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: Swarm Architecture (5 Specialized Fetch.ai Agents)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "3. System Architecture", "Collaborative 5-Agent Swarm (Fetch.ai uAgents Bureau)")

    agents = [
        ("Coordinator Agent", "Frontline Chat & Orchestrator", "Interfaces with ASI:One via Agent Chat Protocol (ACP). Parses natural language, presents adaptive cards, and coordinates swarm response."),
        ("Investigator Agent", "SIEM Telemetry & Log Ingestion", "Queries authentication tables, tracks geographic IP deltas, and neutralizes indirect prompt injections hidden in user-agent strings."),
        ("Threat Analyst Agent", "MITRE ATT&CK Scoring (0-100)", "Applies deterministic rule engine against T1110 (Brute Force), T1078 (Compromised Credentials), and T1556 (MFA Bypass)."),
        ("Containment Agent", "HITL Policy Gate & Severance", "Enforces Human-in-the-Loop policy gate. With user approval, executes zero-trust OAuth revocation and IP firewall quarantine."),
        ("Auditor Agent", "Closed-Loop Verification & Receipts", "Queries session table post-remediation to confirm active_sessions == 0, then computes a cryptographic SHA-256 state certificate."),
    ]

    card_h = Inches(0.85)
    gap_y = Inches(0.18)
    for i, (name, role, desc) in enumerate(agents):
        y_pos = Inches(2.1) + i * (card_h + gap_y)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.733), card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(0, 240, 255) if i == 0 else RGBColor(40, 60, 95)
        card.line.width = Pt(1)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = f"{i+1}. {name}  —  "
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        run_role = p.add_run()
        run_role.text = f"[{role}]"
        run_role.font.size = Pt(12)
        run_role.font.color.rgb = TEXT_CYAN
        run_role.font.bold = True

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 5: Overview of Existing Tools (The Landscape)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "4. Market Overview", "Existing Tools & Why They Fail Everyday Users")

    existing_tools = [
        {
            "category": "Enterprise SOAR & SIEM",
            "examples": "Splunk, CrowdStrike Falcon, Palo Alto Cortex",
            "strengths": "Powerful automated playbooks, advanced telemetry correlation.",
            "fatal_flaw": "Prohibitive cost ($50k - $200k/year), requires dedicated Tier-3 SOC engineers, impossible for consumers or small businesses.",
            "color": TEXT_RED,
        },
        {
            "category": "Consumer Antivirus / EDR",
            "examples": "Norton 360, McAfee, Bitdefender",
            "strengths": "Scans local filesystem for malware, trojans, and phishing URLs.",
            "fatal_flaw": "Completely blind to cloud account takeovers! If an attacker logs into your webmail or crypto account remotely, antivirus does nothing.",
            "color": TEXT_YELLOW,
        },
        {
            "category": "Traditional Customer Support",
            "examples": "Zendesk, Email Ticketing, Help Desks",
            "strengths": "Familiar human point of contact.",
            "fatal_flaw": "24 to 48-hour response latency. By the time a support rep reviews the ticket, credentials and assets are long gone.",
            "color": TEXT_RED,
        },
    ]

    for i, t in enumerate(existing_tools):
        pos_left = Inches(0.8) + i * (card_w3 + gap3)
        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_left, Inches(2.2), card_w3, Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = t["color"]
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = t["category"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = f"e.g. {t['examples']}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_CYAN
        p.space_after = Pt(16)

        p = tf.add_paragraph()
        p.text = "STRENGTHS:"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = TEXT_GREEN
        p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = t["strengths"]
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(18)

        p = tf.add_paragraph()
        p.text = "THE FATAL FLAW:"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = t["color"]
        p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = t["fatal_flaw"]
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 6: How Our Approach Differentiates (Why We Win)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "5. Competitive Differentiation", "Why SentinelFlow Wins — Direct Comparison Matrix")

    # Table
    rows, cols = 5, 5
    table_shape = slide6.shapes.add_table(rows, cols, Inches(0.8), Inches(2.1), Inches(11.733), Inches(4.6))
    table = table_shape.table

    table.columns[0].width = Inches(2.733)
    table.columns[1].width = Inches(2.25)
    table.columns[2].width = Inches(2.25)
    table.columns[3].width = Inches(2.25)
    table.columns[4].width = Inches(2.25)

    headers = ["Capability / Metric", "SentinelFlow (Fetch.ai)", "Enterprise SOAR", "Consumer Antivirus", "Customer Support"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(13, 20, 36)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_CYAN if j == 1 else TEXT_WHITE

    data = [
        ("Response Latency", "Sub-Second (~1.0s)", "Seconds (Scripted)", "N/A (No Cloud Action)", "24 to 48 Hours"),
        ("Pricing Model", "0.1 FET ($0.10) / action", "$50,000+ / year", "$50 - $100 / year", "Bundled (Slow)"),
        ("Interface / UX", "Plain English ASI:One Chat", "Complex SIEM Queries", "Desktop Tray App", "Email Ticket Form"),
        ("Proof of Containment", "Cryptographic SHA-256 Proof", "Internal Server Logs", "None", "'We have resolved it'"),
    ]

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(12)
            if j == 1:
                p.font.bold = True
                p.font.color.rgb = TEXT_CYAN
            elif j == 0:
                p.font.bold = True
                p.font.color.rgb = TEXT_WHITE
            else:
                p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 7: Business Models & Real-World Viability
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "6. Business Model", "Sustainable Economics Powered by Fetch.ai Micropayments")

    models = [
        {
            "tag": "MODEL A",
            "name": "B2C Roadside Rescue",
            "target": "Everyday crypto & web users",
            "bullets": [
                "Scans & Threat Reports: 100% Free",
                "Emergency 1-Tap Lockdown: 0.1 FET (~$0.10)",
                "No subscription lock-in or recurring fees",
                "Settled on-chain via Fetch.ai escrow protocol",
            ],
            "price": "0.1 FET / rescue",
            "color": TEXT_CYAN,
        },
        {
            "tag": "MODEL B",
            "name": "B2B Startup Slack Bot",
            "target": "10-50 person engineering teams",
            "bullets": [
                "Autonomous SecOps bot in Slack / Discord",
                "Replaces $120k/yr junior SOC analyst",
                "Automated triage, credential hygiene & audit trail",
                "Paid via monthly FET subscription",
            ],
            "price": "$99 - $299 / month",
            "color": TEXT_YELLOW,
        },
        {
            "tag": "MODEL C",
            "name": "Agent-to-Agent API",
            "target": "Autonomous agents on Fetch.ai",
            "bullets": [
                "DeFi bots, assistants, and trading agents",
                "Query SentinelFlow to verify partner identities",
                "Machine-to-machine micro-fee settlement",
                "Fully decentralized trust primitive",
            ],
            "price": "0.05 FET / audit call",
            "color": TEXT_GREEN,
        },
    ]

    for i, m in enumerate(models):
        pos_left = Inches(0.8) + i * (card_w3 + gap3)
        card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pos_left, Inches(2.2), card_w3, Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = m["color"]
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = m["tag"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = m["color"]
        p.space_after = Pt(4)

        p = tf.add_paragraph()
        p.text = m["name"]
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = f"Target: {m['target']}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(14)

        for b in m["bullets"]:
            p = tf.add_paragraph()
            p.text = f"• {b}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_WHITE
            p.space_after = Pt(4)

        p = tf.add_paragraph()
        p.space_before = Pt(16)
        p.text = m["price"]
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = m["color"]

    # =========================================================================
    # SLIDE 8: Live Deployment & Verification
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "7. Live Status & Verification", "Production Readiness on Fetch.ai Mainnet & Agentverse")

    stats = [
        ("Agentverse Mailbox", "CONNECTED", "Live on agentverse.ai with ACP 0.1.0 published", TEXT_GREEN),
        ("Coordinator Address", "agent1qwstka...", "Fully discoverable in ASI:One chat directory", TEXT_CYAN),
        ("Automated Tests", "26 / 26 PASSING", "100% test coverage across multi-agent workflow", TEXT_GREEN),
        ("Interactive Console", "LIVE (PORT 3000)", "Real working Python REST API + deterministic scoring", TEXT_CYAN),
    ]

    grid_w = Inches(5.6)
    grid_h = Inches(2.0)
    for idx, (title, highlight, note, color) in enumerate(stats):
        col = idx % 2
        row = idx // 2
        x = Inches(0.8) + col * (grid_w + Inches(0.533))
        y = Inches(2.2) + row * (grid_h + Inches(0.4))

        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, grid_w, grid_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = highlight
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(6)

        p = tf.add_paragraph()
        p.text = note
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE

    prs.save(OUTPUT_FILE)
    print(f"Presentation saved successfully to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_deck()
