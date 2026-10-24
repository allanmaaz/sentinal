# SentinelFlow
### Autonomous Cybersecurity Swarm for Everyday People & Modern Teams
> **Built for Fetch.ai / ASI:One Hackathon — Fetch-A-Thon 3.0**  
> **Team F-ups:** Meer Mohammed Shoaib, Mohammed Maaz, Prithvi S  
> **Live Agent Address:** `agent1qwstka0f7sjyd0ux69zfv9pu66testhc807cdhx8yvav3u0eml7nwptkdfy`  
> **Agentverse Profile:** [agent1qwstka0f...](https://agentverse.ai/agents/details/agent1qwstka0f7sjyd0ux69zfv9pu66testhc807cdhx8yvav3u0eml7nwptkdfy)  
> **GitHub Repository:** [allanmaaz/sentinal](https://github.com/allanmaaz/sentinal)

---

## What is SentinelFlow?

When an everyday person receives an alert stating *"Someone logged into your account from an unrecognized device,"* they panic. Traditional customer support takes 48 hours to respond. By then, accounts, data, and credentials are compromised.

**SentinelFlow** is an autonomous AI cybersecurity bodyguard built natively on Fetch.ai uAgents. Users interact in plain English inside **ASI:One chat** or through our web dashboard. SentinelFlow correlates brute force logins in milliseconds, severs unauthorized sessions across all devices in **1 tap for 0.1 FET (~$0.10)**, and issues a tamper-proof SHA-256 safety certificate.

---

## 3-Step Incident Defense

```
   1. Scan Account (Free)         2. 1-Tap Kick Out (0.1 FET)       3. Cryptographic Proof (Free)
 ┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
 │ "Scan alex@gmail.com"   │ ──► │ Tap "Kick Out Intruder" │ ──► │ Verifiable SHA-256      │
 │ Correlates brute force  │     │ Revokes all sessions &  │     │ state certificate       │
 │ & impossible travel     │     │ blocks attacker IP      │     │ logged on-chain         │
 └─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

1. **Step 1: Check Account (Free):** Type *"Scan alex@gmail.com"* or *"Who accessed my account recently?"*. SentinelFlow correlates recent logs, detects impossible travel, and calculates a deterministic MITRE ATT&CK risk score (0–100).
2. **Step 2: 1-Tap Emergency Containment (0.1 FET):** Tap **[Kick Out Intruder & Lock Account]**. SentinelFlow immediately invalidates all active session tokens and blocks the attacker's IP at the firewall.
3. **Step 3: Cryptographic Proof (SHA-256):** An independent Auditor Agent confirms `active_sessions == 0` and generates an immutable cryptographic state certificate for insurance and banking dispute records.

---

## The 5-Agent Swarm Architecture

SentinelFlow deploys a collaborative multi-agent swarm of 5 specialized Fetch.ai `uAgents`:

| Agent | Core Functionality |
| :--- | :--- |
| **Coordinator Agent** | Frontline interface handling Agent Chat Protocol (ACP), natural language parsing, and interactive cards. |
| **Investigator Agent** | Searches SIEM telemetry logs and neutralizes indirect prompt injection attacks. |
| **Threat Analyst Agent**| Deterministic MITRE ATT&CK risk scoring engine (T1110, T1078, T1068). |
| **Containment Agent** | Enforces human-in-the-loop policy gates and executes zero-trust session severance. |
| **Auditor Agent** | Closed-loop state inspection (`active_sessions == 0`) and cryptographic SHA-256 receipt generation. |

---

## Interactive Web Dashboard

A lightweight, high-performance web dashboard is included in `/web`:
* **Live Incident Console:** Test real investigations against `alex@gmail.com`, `demo-user-104`, and `sarah-dev-92`.
* **Zero Emojis & Enterprise Vector Icons:** Built with crisp SVG vector icons for production SecOps quality.
* **Live REST API:** Direct Python endpoints (`/api/status`, `/api/scan`, `/api/contain`, `/api/chat`).

```bash
# Launch web dashboard on port 3000
python3 web/server.py
```
Visit: `http://localhost:3000`

---

## Quickstart & Installation

### 1. Setup Environment
```bash
git clone https://github.com/allanmaaz/sentinal.git
cd sentinal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 2. Run the Swarm
```bash
# Run standalone Coordinator connected to Agentverse Mailbox
python3 agent.py --standalone

# Or run full 5-agent Bureau locally
python3 agent.py
```

### 3. Run Automated Tests
```bash
pytest -v
# 26 passed in ~12s (100% test coverage)
```

---

## License & Credits

Built for the **Fetch.ai & ASI:One Innovation Hackathon 2026** by Team F-ups.  
Licensed under the MIT License.
