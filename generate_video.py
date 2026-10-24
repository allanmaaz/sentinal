#!/usr/bin/env python3
"""
Generate a beautiful 1080p Pitch Deck Video for SentinelFlow using Pillow & ffmpeg.
Creates 8 high-res slides (1920x1080) and compiles them into SentinelFlow_Pitch_Deck.mp4.
"""

import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

FONT_HELVETICA = "/System/Library/Fonts/Helvetica.ttc"
FONT_MENLO = "/System/Library/Fonts/Menlo.ttc"

BG_COLOR = (7, 11, 20)       # #070B14
CARD_BG = (15, 23, 42)       # #0F172A
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (148, 163, 184) # #94A3B8
CYAN = (0, 240, 255)         # #00F0FF
GREEN = (16, 185, 129)       # #10B981
RED = (239, 68, 68)          # #EF4444
YELLOW = (245, 158, 11)      # #F59E0B
BORDER_SUBTLE = (30, 41, 59)

def get_font(size, is_mono=False, is_bold=False):
    fp = FONT_MENLO if is_mono else FONT_HELVETICA
    try:
        index = 1 if is_bold and not is_mono else 0
        return ImageFont.truetype(fp, size, index=index)
    except Exception:
        return ImageFont.load_default()

def draw_rounded_card(draw, x, y, w, h, border_color=BORDER_SUBTLE, bg=CARD_BG, r=16):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=bg, outline=border_color, width=2)

def create_slide_1():
    """Title Slide"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Event Tag
    f_tag = get_font(20, is_mono=True)
    draw_rounded_card(draw, 140, 160, 460, 44, border_color=(0, 240, 255, 100), bg=(10, 25, 45), r=8)
    draw.text((160, 172), "FETCH.AI & ASI:ONE HACKATHON 2026", font=f_tag, fill=CYAN)

    # Big Title
    f_title = get_font(92, is_bold=True)
    draw.text((140, 240), "Sentinel", font=f_title, fill=TEXT_WHITE)
    w_sent = draw.textlength("Sentinel", font=f_title)
    draw.text((140 + w_sent, 240), "Flow", font=f_title, fill=CYAN)

    # Subtitle
    f_sub = get_font(38)
    draw.text((140, 360), "The 24/7 Autonomous AI Bodyguard for Everyday Accounts.", font=f_sub, fill=TEXT_WHITE)

    f_desc = get_font(24)
    desc_lines = [
        "Detects unauthorized logins in <500ms, severs intruder sessions across all devices in 1 second",
        "for a 0.1 FET micropayment, and issues an immutable SHA-256 cryptographic proof."
    ]
    for i, line in enumerate(desc_lines):
        draw.text((140, 440 + i * 36), line, font=f_desc, fill=TEXT_MUTED)

    # 3 Highlight Cards
    highlights = [
        ("Sub-Second Severance", "Instant OAuth & session token invalidation", CYAN),
        ("0.1 FET Micropayments", "No monthly lock-in. Pay-as-you-save model", YELLOW),
        ("SHA-256 Receipt", "Cryptographic proof for bank/insurance disputes", GREEN)
    ]
    for i, (h_title, h_desc, color) in enumerate(highlights):
        cx = 140 + i * 545
        draw_rounded_card(draw, cx, 580, 520, 180, border_color=color, r=14)
        draw.text((cx + 30, 615), h_title, font=get_font(26, is_bold=True), fill=color)
        draw.text((cx + 30, 665), h_desc, font=get_font(18), fill=TEXT_MUTED)

    # Footer
    f_foot = get_font(20)
    draw.text((140, 940), "Team F-ups: Meer Mohammed Shoaib  •  Mohammed Maaz  •  Prithvi S", font=f_foot, fill=TEXT_MUTED)
    draw.text((1400, 940), "Native Fetch.ai uAgents Bureau", font=get_font(20, is_mono=True), fill=CYAN)

    return img

def create_slide_2():
    """Slide 2: Problem Statement"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "1. PROBLEM STATEMENT", font=get_font(20, is_mono=True), fill=RED)
    draw.text((140, 130), "The 'Panic Window' — Why Account Takeovers Are Devastating", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    cards = [
        ("01", "2:00 AM Crisis", "Immediate Panic", "A user gets an alert: 'Login from Lagos, Nigeria'. The victim is asleep or helpless while attackers guess passwords and bypass 2FA.", RED),
        ("02", "48-Hour Delay", "Support Black Hole", "Customer support takes 24–48 hours to answer an urgent ticket. By the time humans reply, the account is completely drained.", YELLOW),
        ("03", "Irreversible Loss", "Within 4 Minutes", "Attackers immediately forward emails, swap phone numbers, transfer funds, and lock the real owner out permanently.", RED),
        ("04", "$50k Cost Gap", "Enterprise Barrier", "Automated SOAR tools cost over $50,000/year and require Tier-3 SOC teams. Everyday people and small teams have zero real-time defense.", CYAN)
    ]

    for i, (num, title, sub, desc, color) in enumerate(cards):
        cx = 140 + i * 410
        draw_rounded_card(draw, cx, 240, 390, 620, border_color=color, r=14)
        draw.text((cx + 30, 275), num, font=get_font(44, is_mono=True, is_bold=True), fill=color)
        draw.text((cx + 30, 345), title, font=get_font(24, is_bold=True), fill=TEXT_WHITE)
        draw.text((cx + 30, 385), sub, font=get_font(18, is_bold=True), fill=color)
        
        # Word wrap desc
        words = desc.split(" ")
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 28:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        
        for li, line in enumerate(lines):
            draw.text((cx + 30, 440 + li * 28), line, font=get_font(18), fill=TEXT_MUTED)

    draw.text((140, 960), "Result: Consumers and startups lose identity and funds within the first 15 minutes of an intrusion.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_3():
    """Slide 3: Proposed Solution"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "2. PROPOSED SOLUTION", font=get_font(20, is_mono=True), fill=CYAN)
    draw.text((140, 130), "SentinelFlow: Autonomous Multi-Agent SecOps on Fetch.ai", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    pillars = [
        ("1. Spot Password Thieves", "100% Free Telemetry Scans", "Investigator Agent correlates SIEM authentication logs in milliseconds. Spots brute-force bursts, impossible travel, and MFA bypass attempts with zero false alarms.", "< 500 ms", "Correlation Latency", CYAN),
        ("2. 1-Tap Severance", "0.1 FET (~$0.10 / 10 Cents)", "Victim taps 'Kick them out' or confirms via chat. Containment Agent instantly invalidates OAuth tokens, revokes sessions across all devices, and firewalls the attacker IP.", "1 Second", "Response Time", YELLOW),
        ("3. Cryptographic Proof", "Immutable SHA-256 Receipt", "Auditor Agent independently inspects post-action state to confirm 0 active sessions remain, computing a tamper-proof SHA-256 certificate for bank & insurance dispute records.", "SHA-256", "Verified On-Chain", GREEN)
    ]

    for i, (title, sub, desc, stat_val, stat_lbl, color) in enumerate(pillars):
        cx = 140 + i * 545
        draw_rounded_card(draw, cx, 240, 525, 620, border_color=color, r=16)
        draw.text((cx + 35, 280), title, font=get_font(26, is_bold=True), fill=color)
        draw.text((cx + 35, 320), sub, font=get_font(18, is_bold=True), fill=TEXT_WHITE)

        words = desc.split(" ")
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 36:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)

        for li, line in enumerate(lines):
            draw.text((cx + 35, 380 + li * 28), line, font=get_font(18), fill=TEXT_MUTED)

        # Big Stat at Bottom
        draw.line([cx + 35, 680, cx + 490, 680], fill=BORDER_SUBTLE, width=1)
        draw.text((cx + 35, 710), stat_val, font=get_font(44, is_bold=True), fill=color)
        draw.text((cx + 35, 765), stat_lbl, font=get_font(16), fill=TEXT_MUTED)

    draw.text((140, 960), "Empowers everyday account owners with enterprise-grade defense at sub-second velocity.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_4():
    """Slide 4: Swarm Architecture"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "3. SYSTEM ARCHITECTURE", font=get_font(20, is_mono=True), fill=CYAN)
    draw.text((140, 130), "Collaborative 5-Agent Swarm (Fetch.ai uAgents Bureau)", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    agents = [
        ("1. Coordinator Agent", "Interfaces with ASI:One via Agent Chat Protocol (ACP 0.1.0). Parses natural language, presents adaptive cards, and coordinates the swarm pipeline.", "ACP & UI Interface", CYAN),
        ("2. Investigator Agent", "Ingests authentication tables, correlates geographic IP deltas, and neutralizes indirect prompt injections hidden in user-agent strings.", "SIEM & Log Retrieval", CYAN),
        ("3. Threat Analyst Agent", "Applies deterministic rule engine against MITRE ATT&CK: T1110 (Brute Force), T1078 (Compromised Credentials), T1556 (MFA Bypass).", "MITRE Scoring (0-100)", YELLOW),
        ("4. Containment Agent", "Enforces strict Human-in-the-Loop policy gate. With user approval, executes zero-trust OAuth revocation and IP firewall quarantine.", "Zero-Trust Severance", RED),
        ("5. Auditor Agent", "Queries session table post-remediation to confirm active_sessions == 0, then computes an immutable SHA-256 cryptographic certificate.", "Closed-Loop Verification", GREEN)
    ]

    for i, (name, role_desc, tag, color) in enumerate(agents):
        cy = 230 + i * 135
        draw_rounded_card(draw, 140, cy, 1640, 115, border_color=color, r=12)
        draw.text((170, cy + 22), name, font=get_font(22, is_bold=True), fill=TEXT_WHITE)
        draw.text((170, cy + 58), role_desc, font=get_font(17), fill=TEXT_MUTED)
        
        # Badge on right
        draw_rounded_card(draw, 1480, cy + 32, 260, 44, border_color=color, bg=(10, 20, 35), r=8)
        draw.text((1500, cy + 44), tag, font=get_font(16, is_mono=True), fill=color)

    draw.text((140, 960), "Bureau Architecture: Agents communicate through local asynchronous IPC and Agentverse Mailbox.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_5():
    """Slide 5: Existing Tools vs SentinelFlow"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "4. MARKET OVERVIEW", font=get_font(20, is_mono=True), fill=YELLOW)
    draw.text((140, 130), "Existing Tools & Why They Fail Everyday Users", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    tools = [
        ("Enterprise SOAR", "Splunk, CrowdStrike, Palo Alto", "Powerful automated playbooks, advanced telemetry correlation across corporate networks.", "Costs $50,000 to $200,000/year. Requires dedicated Tier-3 SOC engineers. Totally inaccessible for consumers or small startups.", RED),
        ("Consumer Antivirus", "Norton 360, McAfee, Bitdefender", "Scans local filesystem for malware, trojans, viruses, and phishing URLs.", "Completely blind to cloud account takeovers! If a hacker breaks into your email or crypto exchange remotely, antivirus does nothing.", YELLOW),
        ("Customer Support", "Email Tickets, Help Desks", "Familiar human point of contact with manual review processes.", "24 to 48-hour response latency. By the time a support rep reads the ticket, credentials and assets are long gone.", RED)
    ]

    for i, (t_name, t_sub, t_str, t_flaw, color) in enumerate(tools):
        cx = 140 + i * 545
        draw_rounded_card(draw, cx, 240, 525, 620, border_color=color, r=16)
        draw.text((cx + 35, 280), t_name, font=get_font(28, is_bold=True), fill=TEXT_WHITE)
        draw.text((cx + 35, 325), t_sub, font=get_font(18, is_bold=True), fill=CYAN)

        draw.text((cx + 35, 390), "STRENGTHS:", font=get_font(16, is_bold=True), fill=GREEN)
        draw.text((cx + 35, 420), t_str, font=get_font(18), fill=TEXT_MUTED)

        draw.line([cx + 35, 520, cx + 490, 520], fill=BORDER_SUBTLE, width=1)

        draw.text((cx + 35, 550), "THE FATAL FLAW:", font=get_font(16, is_bold=True), fill=color)
        
        words = t_flaw.split(" ")
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) < 34:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        for li, line in enumerate(lines):
            draw.text((cx + 35, 585 + li * 28), line, font=get_font(18), fill=TEXT_MUTED)

    draw.text((140, 960), "Conclusion: A massive gap exists between expensive enterprise tools and helpless consumer antivirus.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_6():
    """Slide 6: Differentiation Matrix"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "5. COMPETITIVE DIFFERENTIATION", font=get_font(20, is_mono=True), fill=GREEN)
    draw.text((140, 130), "Why SentinelFlow Wins — Direct Comparison Matrix", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    # Table layout
    headers = ["Capability / Metric", "SentinelFlow (Fetch.ai)", "Enterprise SOAR", "Consumer Antivirus", "Customer Support"]
    cols_x = [140, 540, 920, 1260, 1560]

    # Draw header row
    draw_rounded_card(draw, 140, 230, 1640, 60, border_color=BORDER_SUBTLE, bg=(13, 20, 36), r=8)
    for i, h in enumerate(headers):
        color = CYAN if i == 1 else TEXT_WHITE
        draw.text((cols_x[i] + 15, 248), h, font=get_font(18, is_bold=True), fill=color)

    rows = [
        ("Response Latency", "Sub-Second (~1.0s)", "Seconds (Scripted)", "N/A (No Cloud Action)", "24 to 48 Hours"),
        ("Pricing Model", "0.1 FET ($0.10) / rescue", "$50,000+ / year", "$50 - $100 / year", "Bundled (Slow)"),
        ("Interface / UX", "Plain English ASI:One Chat", "Complex SIEM Queries", "Desktop Tray App", "Email Ticket Form"),
        ("Proof of Containment", "Cryptographic SHA-256 Proof", "Internal Server Logs", "None", "'We have resolved it'"),
        ("Autonomous Swarm", "5 Fetch.ai uAgents", "Central Orchestrator", "Single Daemon", "Human Reps"),
        ("Zero-Trust Severance", "Instant OAuth & IP Block", "Firewall Rules", "Local File Quarantine", "Manual Password Reset")
    ]

    for ri, row in enumerate(rows):
        cy = 310 + ri * 90
        bg = (18, 28, 48) if ri % 2 == 0 else (12, 18, 32)
        draw_rounded_card(draw, 140, cy, 1640, 75, border_color=BORDER_SUBTLE, bg=bg, r=8)
        for ci, val in enumerate(row):
            f_style = get_font(18, is_bold=(ci <= 1))
            color = CYAN if ci == 1 else (TEXT_WHITE if ci == 0 else TEXT_MUTED)
            draw.text((cols_x[ci] + 15, cy + 25), val, font=f_style, fill=color)

    draw.text((140, 960), "Summary: SentinelFlow delivers enterprise-tier speed at consumer micro-pricing with cryptographic assurance.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_7():
    """Slide 7: Business Model"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "6. BUSINESS MODEL & MARKET VIABILITY", font=get_font(20, is_mono=True), fill=CYAN)
    draw.text((140, 130), "Sustainable Economics via Fetch.ai Micropayments", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    models = [
        ("MODEL A", "B2C Roadside Rescue", "For everyday crypto & web users", [
            "• Scans & Threat Reports: 100% Free",
            "• Emergency Lockdown: 0.1 FET (~$0.10)",
            "• Zero subscription lock-in or recurring fees",
            "• Settled on-chain via Fetch.ai escrow",
            "• Solves the 2:00 AM panic window instantly"
        ], "0.1 FET", "Per Automated Rescue", CYAN),

        ("MODEL B", "B2B Startup Slack Bot", "For 10–50 person companies", [
            "• Autonomous SecOps in Slack & Discord",
            "• Replaces $120k/yr junior SOC analyst",
            "• Automated credential hygiene & audit trail",
            "• Instant employee session revocation",
            "• Paid via monthly FET subscription"
        ], "$99 - $299", "Per Month", YELLOW),

        ("MODEL C", "Agent-to-Agent API", "For autonomous agents on Fetch.ai", [
            "• Machine-to-machine trust protocol",
            "• DeFi bots query SentinelFlow before trades",
            "• Verifies partner identities & session state",
            "• Micro-fee settlement per verification",
            "• Decentralized security primitive"
        ], "0.05 FET", "Per Machine Audit Call", GREEN)
    ]

    for i, (tag, title, target, points, stat_val, stat_lbl, color) in enumerate(models):
        cx = 140 + i * 545
        draw_rounded_card(draw, cx, 240, 525, 620, border_color=color, r=16)
        draw.text((cx + 35, 275), tag, font=get_font(16, is_mono=True), fill=color)
        draw.text((cx + 35, 305), title, font=get_font(26, is_bold=True), fill=TEXT_WHITE)
        draw.text((cx + 35, 345), target, font=get_font(17), fill=TEXT_MUTED)

        draw.line([cx + 35, 385, cx + 490, 385], fill=BORDER_SUBTLE, width=1)

        for pi, pt in enumerate(points):
            draw.text((cx + 35, 410 + pi * 36), pt, font=get_font(17), fill=TEXT_WHITE)

        draw.line([cx + 35, 640, cx + 490, 640], fill=BORDER_SUBTLE, width=1)
        draw.text((cx + 35, 670), stat_val, font=get_font(44, is_bold=True), fill=color)
        draw.text((cx + 35, 725), stat_lbl, font=get_font(16), fill=TEXT_MUTED)

    draw.text((140, 960), "Economics: Pure utility-driven token demand powered by real-world security containment actions.", font=get_font(20), fill=TEXT_MUTED)
    return img

def create_slide_8():
    """Slide 8: Status & Verification"""
    img = Image.new("RGB", (1920, 1080), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw.text((140, 90), "7. LIVE STATUS & VERIFICATION", font=get_font(20, is_mono=True), fill=GREEN)
    draw.text((140, 130), "Production Readiness on Fetch.ai Mainnet & Agentverse", font=get_font(44, is_bold=True), fill=TEXT_WHITE)

    # 4 Status Boxes
    boxes = [
        ("AGENTVERSE MAILBOX", "CONNECTED & ACTIVE", "Live on agentverse.ai with Agent Chat Protocol (ACP 0.1.0) published and discoverable in ASI:One chat.", "agent1qwstka0f...dfy", GREEN),
        ("RELIABILITY GAUNTLET", "26 / 26 TESTS PASSING", "100% pass rate across automated pytest suite covering brute force, token validation, and multi-agent IPC.", "100% Automated", GREEN),
        ("CONTAINMENT VELOCITY", "< 1.05 SECONDS", "Average response latency from user tap to complete OAuth severance and IP firewall rule enforcement.", "100x Faster than SOAR", CYAN),
        ("PROMPT INJECTION DEFENSE", "ZERO COMPROMISE", "Simulated adversarial user-agent strings neutralized by strictly typed schema validation and sanitized logs.", "Tamper-Proof SIEM", GREEN)
    ]

    for i, (subtitle, title, desc, tag, color) in enumerate(boxes):
        col = i % 2
        row = i // 2
        cx = 140 + col * 840
        cy = 240 + row * 310
        draw_rounded_card(draw, cx, cy, 800, 280, border_color=color, r=16)
        draw.text((cx + 35, cy + 30), subtitle, font=get_font(16, is_mono=True), fill=TEXT_MUTED)
        draw.text((cx + 35, cy + 65), title, font=get_font(30, is_bold=True), fill=color)
        draw.text((cx + 35, cy + 120), desc, font=get_font(18), fill=TEXT_WHITE)
        
        # Tag at bottom
        draw_rounded_card(draw, cx + 35, cy + 205, 300, 42, border_color=color, bg=(10, 25, 45), r=8)
        draw.text((cx + 50, cy + 217), tag, font=get_font(16, is_mono=True), fill=color)

    draw.text((140, 960), "Ready for live demo and hackathon evaluation across all ASI:One & Fetch.ai criteria.", font=get_font(20), fill=TEXT_MUTED)
    return img

def main():
    slides_dir = "/tmp/sentinelflow_slides"
    os.makedirs(slides_dir, exist_ok=True)

    slide_funcs = [
        create_slide_1,
        create_slide_2,
        create_slide_3,
        create_slide_4,
        create_slide_5,
        create_slide_6,
        create_slide_7,
        create_slide_8
    ]

    print("Rendering 8 slide frames in 1080p...")
    for idx, func in enumerate(slide_funcs):
        img = func()
        path = os.path.join(slides_dir, f"slide_{idx+1:02d}.png")
        img.save(path)
        print(f"  Slide {idx+1} saved to {path}")

    # Generate MP4 Video with ffmpeg
    output_mp4 = "/Users/apple/Desktop/Fetch ai/SentinelFlow_Pitch_Deck.mp4"
    web_mp4 = "/Users/apple/Desktop/Fetch ai/web/SentinelFlow_Pitch_Deck.mp4"

    # Use ffmpeg concat with 8 seconds per slide = 64 seconds total duration
    concat_txt = os.path.join(slides_dir, "concat.txt")
    with open(concat_txt, "w") as f:
        for idx in range(1, 9):
            f.write(f"file '{slides_dir}/slide_{idx:02d}.png'\n")
            f.write("duration 8\n")
        # ffmpeg requires the last file to be specified again without duration
        f.write(f"file '{slides_dir}/slide_08.png'\n")

    print("\nCompiling MP4 video with ffmpeg...")
    cmd = [
        "/usr/local/bin/ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt,
        "-pix_fmt", "yuv420p",
        "-c:v", "libx264",
        "-r", "30",
        output_mp4
    ]
    subprocess.run(cmd, check=True)
    print(f"Video created successfully at: {output_mp4}")

    # Copy to web folder
    import shutil
    shutil.copy(output_mp4, web_mp4)
    print(f"Copied video to: {web_mp4}")

if __name__ == "__main__":
    main()
