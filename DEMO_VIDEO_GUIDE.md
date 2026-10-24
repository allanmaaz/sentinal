# SentinelFlow — Demo Video Recording Guide & Script
**Fetch.ai & ASI:One Innovation Hackathon 2026**

This guide provides everything needed to record and submit a winning **2 to 3-minute demo video** for SentinelFlow.

---

## 1. Ready-Made Assets Available

| Asset | Location / URL | Purpose |
| :--- | :--- | :--- |
| **Pre-Rendered Slide Video (1080p MP4)** | [SentinelFlow_Pitch_Deck.mp4](file:///Users/apple/Desktop/Fetch%20ai/SentinelFlow_Pitch_Deck.mp4) | High-definition 1080p slide video generated via `ffmpeg`. Use as b-roll or intro/outro. |
| **Interactive Live Console + Auto-Demo** | `http://localhost:3000` | Click **"Play Auto-Demo"** (or press `D`). The page navigates and runs the entire live demo automatically! |
| **Interactive Web Presentation Deck** | `http://localhost:3000/slides.html` | Browser-based slide deck with keyboard arrows (`←`/`→`) and fullscreen (`F`). |
| **Native PowerPoint Presentation** | [SentinelFlow_Presentation.pptx](file:///Users/apple/Desktop/Fetch%20ai/SentinelFlow_Presentation.pptx) | 16:9 Widescreen presentation deck for Keynote, PowerPoint, or Google Slides. |
| **Passing Test Suite Verification** | `pytest -v` (Terminal) | 26/26 automated unit and security tests passing. |

---

## 2. Quick Recording Instructions on macOS (QuickTime)

You do **not** need any third-party recording software installed:
1. Make sure the local web server is running: `http://localhost:3000`.
2. Press **`Cmd + Shift + 5`** on your Mac keyboard.
3. In the toolbar at the bottom:
   - Select **"Record Selected Portion"** and drag the box to cover your browser window (or choose **"Record Entire Screen"**).
   - Click **Options** -> Select your **Microphone** (Built-in Microphone or Headset).
   - Set Timer to **None** or **5 seconds** to get ready.
4. Click **Record**.
5. When finished, click the **Stop** icon in the Mac menu bar at the top right (or press `Cmd + Control + Esc`).

---

## 3. Timestamped Storyboard & Word-for-Word Script (Target: 2 min 20 sec)

### Scene 1: The Problem — The "Panic Window" (0:00 – 0:25)
* **Visual:** Show Slide 2 ("The Panic Window") or the hero section of `http://localhost:3000`.
* **Voiceover:**
  > *"Imagine waking up at 2 AM to an alert on your phone: 'New login from Lagos, Nigeria on your primary email and crypto exchange.'*
  > 
  > *You panic. You frantically open a customer support ticket. But human support takes 24 to 48 hours to answer. Within 4 minutes, an intruder forwards your emails, bypasses two-factor authentication, and drains your assets.*
  > 
  > *Enterprise security tools like Splunk or CrowdStrike cost over $50,000 a year, while consumer antivirus is completely blind to cloud account takeovers. Everyday people are left completely defenseless."*

---

### Scene 2: The Solution — SentinelFlow Autonomous Swarm (0:25 – 0:45)
* **Visual:** Transition to `http://localhost:3000` Console or Slide 3.
* **Voiceover:**
  > *"Meet **SentinelFlow**: the 24/7 autonomous AI bodyguard for everyday accounts, built natively on Fetch.ai uAgents.*
  > 
  > *Instead of waiting 48 hours, SentinelFlow detects account takeovers in milliseconds, kicks the intruder out of every laptop and phone in 1 second for a 10-cent micropayment (0.1 FET), and issues an immutable cryptographic SHA-256 safety certificate."*

---

### Scene 3: Live SecOps Console & Sub-Second Containment (0:45 – 1:30)
* **Visual:** On `http://localhost:3000`, click **"Play Auto-Demo"** (or press key **`D`**). Watch the UI automatically scroll, scan, sever, and verify!
* **Voiceover:**
  > *"Let’s see SentinelFlow in action on our live SecOps console.*
  > 
  > *Here, our Investigator Agent correlates SIEM authentication logs in real-time. Notice how it immediately flags an intrusion on alex@gmail.com: 5 failed passwords in 50 seconds, followed by an impossible travel anomaly from Lagos, Nigeria.*
  > 
  > *Our Threat Analyst Agent maps this directly against MITRE ATT&CK techniques T1110 and T1078, assigning a Critical Risk score of 94 out of 100.*
  > 
  > *With one tap, the user triggers emergency containment for just 0.1 FET. Watch what happens: in just 1.05 seconds, our Containment Agent revokes all active OAuth sessions across all devices and firewalls the attacker IP.*
  > 
  > *Instantly, our Auditor Agent independently verifies that active sessions have dropped to zero, issuing a tamper-proof SHA-256 cryptographic certificate that victims can present directly to banks and insurance providers."*

---

### Scene 4: ASI:One Agent Chat & Adaptive Cards (1:30 – 2:05)
* **Visual:** Scroll to the **Agent Chat** playground on `http://localhost:3000` or show the Agent Chat interface. (Auto-Demo automatically types `"Investigate alex@gmail.com"` and sends it).
* **Voiceover:**
  > *"Users don’t need to know complex cybersecurity jargon. They can interact in plain English through ASI:One chat via the Agent Chat Protocol (ACP).*
  > 
  > *When a user asks 'Investigate alex@gmail.com', our Coordinator Agent parses the intent and returns structured Adaptive Cards with threat evidence and 1-tap containment actions.*
  > 
  > *Even if an attacker attempts an indirect prompt injection inside user-agent headers—trying to tell the AI to ignore the alert—our typed schema validation isolates untrusted data, preventing any compromise."*

---

### Scene 5: Swarm Architecture, Reliability & Wrap-Up (2:05 – 2:30)
* **Visual:** Show Slide 8 (Status & Verification) or switch to Terminal showing `pytest -v` with all 26 tests green.
* **Voiceover:**
  > *"Under the hood, SentinelFlow is a 5-agent collaborative swarm running on the Fetch.ai uAgents Bureau, live and connected to the Agentverse Mailbox.*
  > 
  > *The entire system is battle-tested with 26 automated reliability tests covering brute-force detection, token revocation, prompt injection resistance, and payment escrow.*
  > 
  > *With our 0.1 FET pay-as-you-save model, SentinelFlow brings enterprise-grade SOC defense to billions of everyday people.*
  > 
  > *Thank you!"*

---

## 4. Submission Checklist for Hackathon Judges

- [ ] **Video Length:** Between 2:00 and 2:45 minutes.
- [ ] **Resolution:** 1080p (1920x1080).
- [ ] **Audio Quality:** Clear voice with no background hum.
- [ ] **Live Features Highlighted:**
  - Problem statement (The 2 AM Panic Window).
  - Fetch.ai multi-agent swarm (Coordinator, Investigator, Analyst, Containment, Auditor).
  - 1-Tap Session Severance (0.1 FET micropayment).
  - SHA-256 cryptographic proof of containment.
  - ASI:One chat with interactive adaptive cards.
  - 26/26 automated tests passing.
- [ ] **Recommended Platforms for Video Link:**
  - **YouTube:** Upload as "Unlisted" or "Public" with title `SentinelFlow — Autonomous Account Defense on Fetch.ai (ASI:One Hackathon)`.
  - **Loom:** Share link with public view permissions.
  - **Google Drive:** Ensure "Anyone with the link can view" is enabled.
