/**
 * SentinelFlow — Interactive Multi-Agent Swarm Simulator & Chat Playground
 * Demonstrates Fetch.ai uAgents workflow, deterministic MITRE risk scoring,
 * 1-second containment, and SHA-256 state proof verification.
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- DOM Elements: Simulator ---
  const targetInput = document.getElementById('target-account-input');
  const btnStartScan = document.getElementById('btn-start-scan');
  const presetPills = document.querySelectorAll('.preset-pill');
  const swarmStatus = document.getElementById('swarm-telemetry-status');

  const nodeCoordinator = document.getElementById('node-coordinator');
  const nodeInvestigator = document.getElementById('node-investigator');
  const nodeAnalyst = document.getElementById('node-analyst');
  const nodeContainment = document.getElementById('node-containment');
  const nodeAuditor = document.getElementById('node-auditor');

  const conn1 = document.getElementById('conn-1');
  const conn2 = document.getElementById('conn-2');
  const conn3 = document.getElementById('conn-3');
  const conn4 = document.getElementById('conn-4');

  const cardStandby = document.getElementById('card-standby');
  const cardThreat = document.getElementById('card-threat');
  const cardVerified = document.getElementById('card-verified');

  const threatRiskBadge = document.getElementById('threat-risk-badge');
  const threatCardTitle = document.getElementById('threat-card-title');
  const threatEvidenceList = document.getElementById('threat-evidence-list');
  const riskScoreDisplay = document.getElementById('risk-score-display');
  const riskGaugeCircle = document.getElementById('risk-gauge-circle');

  const btnKickOut = document.getElementById('btn-kick-out');
  const btnViewLogs = document.getElementById('btn-view-logs');
  const btnItWasMe = document.getElementById('btn-it-was-me');
  const btnResetSimulator = document.getElementById('btn-reset-simulator');
  const btnCopyHash = document.getElementById('btn-copy-hash');

  const certTargetVal = document.getElementById('cert-target-val');
  const certHashVal = document.getElementById('cert-hash-val');

  // --- DOM Elements: Chat Playground ---
  const chatPresetBtns = document.querySelectorAll('.chat-preset-btn');
  const chatMessagesContainer = document.getElementById('chat-messages-container');
  const chatUserInput = document.getElementById('chat-user-input');
  const btnChatSend = document.getElementById('btn-chat-send');

  // Preset Account Profiles
  const SCENARIOS = {
    'alex@gmail.com': {
      riskScore: 100,
      riskLevel: 'CRITICAL',
      title: '🚨 Unauthorized Intrusion Detected on alex@gmail.com!',
      evidence: [
        '<strong>Lagos, Nigeria (IP 198.51.100.42):</strong> 5 consecutive failed logins in 50 seconds (brute-force burst).',
        '<strong>Impossible Travel:</strong> Successful login from unfamiliar Linux client immediately following failed attempts.',
        '<strong>Privilege Escalation:</strong> Unauthorized probe targeting <code>/api/v1/auth/mfa/bypass</code>.'
      ],
      hash: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    },
    'demo-user-104': {
      riskScore: 100,
      riskLevel: 'CRITICAL',
      title: '🚨 Credential Stuffing & Admin Probe on demo-user-104!',
      evidence: [
        '<strong>Bucharest, Romania (IP 198.51.100.42):</strong> 7 failed login attempts within 2 minutes.',
        '<strong>Compromised Credential:</strong> Password accepted after brute force, MFA challenged.',
        '<strong>Sensitive Operation:</strong> Attacker executed query against <code>/api/v1/admin/privileges</code>.'
      ],
      hash: '4a6b2c89f1d09e8876a35bf2e99d1045a1c38e923e4492bfd91e8477610ab452'
    },
    'sarah-dev-92': {
      riskScore: 0,
      riskLevel: 'SAFE',
      title: '✅ Account Safe: Normal Baseline Activity for sarah-dev-92',
      evidence: [
        '<strong>Austin, Texas (IP 192.0.2.88):</strong> SSO authenticated via corporate Okta provider.',
        '<strong>MFA Verified:</strong> Hardware FIDO2 token verified at 08:30 UTC.',
        '<strong>Expected Activity:</strong> Git repository clone on <code>/git/repo-secops.git</code> conforming to baseline.'
      ],
      hash: '0000000000000000000000000000000000000000000000000000000000000000'
    }
  };

  // --- Simulator Logic ---
  presetPills.forEach(pill => {
    pill.addEventListener('click', () => {
      presetPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      targetInput.value = pill.dataset.target;
      startScanFlow(pill.dataset.target);
    });
  });

  btnStartScan.addEventListener('click', () => {
    const target = targetInput.value.trim() || 'alex@gmail.com';
    startScanFlow(target);
  });

  function resetSwarmNodes() {
    [nodeCoordinator, nodeInvestigator, nodeAnalyst, nodeContainment, nodeAuditor].forEach(n => {
      n.classList.remove('node-active', 'node-success');
    });
    [conn1, conn2, conn3, conn4].forEach(c => c.classList.remove('transmitting'));
  }

  function startScanFlow(target) {
    resetSwarmNodes();
    cardStandby.classList.add('hidden');
    cardThreat.classList.add('hidden');
    cardVerified.classList.add('hidden');

    swarmStatus.textContent = 'TELEMETRY: SCANNING IN PROGRESS...';
    swarmStatus.style.color = 'var(--accent-cyan)';

    // Step 1: Coordinator Agent activates
    nodeCoordinator.classList.add('node-active');
    conn1.classList.add('transmitting');

    setTimeout(() => {
      // Step 2: Investigator Agent queries SIEM
      nodeInvestigator.classList.add('node-active');
      conn2.classList.add('transmitting');

      setTimeout(() => {
        // Step 3: Threat Analyst correlates MITRE ATT&CK
        nodeAnalyst.classList.add('node-active');

        // Lookup or generate scenario
        const scenario = SCENARIOS[target] || {
          riskScore: 100,
          riskLevel: 'CRITICAL',
          title: `🚨 Unauthorized Breach Detected on ${target}!`,
          evidence: [
            `<strong>Lagos, Nigeria (IP 198.51.100.42):</strong> 5 consecutive failed logins detected for ${target}.`,
            '<strong>Impossible Travel:</strong> Attacker session originated 6,000 miles from usual location.',
            '<strong>Unauthorized Session:</strong> Active token generated from unrecognized client.'
          ],
          hash: 'c89fa3b1d09e8876a35bf2e99d1045a1e3b0c44298fc1c149afbf4c8996fb92'
        };

        renderThreatCard(target, scenario);
      }, 400);
    }, 400);
  }

  function renderThreatCard(target, scenario) {
    swarmStatus.textContent = `TELEMETRY: CORRELATED (${scenario.riskLevel})`;
    swarmStatus.style.color = scenario.riskScore > 50 ? 'var(--accent-red)' : 'var(--accent-green)';

    threatCardTitle.textContent = scenario.title;
    threatEvidenceList.innerHTML = scenario.evidence.map(e => `<li>${e}</li>`).join('');

    riskScoreDisplay.textContent = scenario.riskScore;

    if (scenario.riskScore === 0) {
      threatRiskBadge.className = 'badge badge-verified';
      threatRiskBadge.textContent = '✅ SAFE: 0/100 RISK';
      riskGaugeCircle.style.background = 'conic-gradient(var(--accent-green) 0% 100%, rgba(255,255,255,0.1) 100% 100%)';
      riskGaugeCircle.style.boxShadow = 'var(--shadow-glow-green)';
      riskScoreDisplay.style.color = 'var(--accent-green)';
      btnKickOut.style.display = 'none';
    } else {
      threatRiskBadge.className = 'badge badge-critical';
      threatRiskBadge.textContent = `🚨 ${scenario.riskLevel} RISK: ${scenario.riskScore}/100`;
      riskGaugeCircle.style.background = 'conic-gradient(var(--accent-red) 0% 100%, rgba(255,255,255,0.1) 100% 100%)';
      riskGaugeCircle.style.boxShadow = 'var(--shadow-glow-red)';
      riskScoreDisplay.style.color = 'var(--accent-red)';
      btnKickOut.style.display = 'inline-flex';
    }

    cardThreat.classList.remove('hidden');
  }

  // Handle 1-Tap Emergency Containment
  btnKickOut.addEventListener('click', () => {
    btnKickOut.disabled = true;
    btnKickOut.innerHTML = '⚡ Severing Sessions (0.1 FET)...';

    swarmStatus.textContent = 'EXECUTING ZERO-TRUST CONTAINMENT (0.1 FET)...';
    swarmStatus.style.color = 'var(--accent-cyan)';

    // Step 4: Containment Agent executes
    conn3.classList.add('transmitting');
    nodeContainment.classList.add('node-active');

    setTimeout(() => {
      nodeContainment.classList.add('node-success');
      conn4.classList.add('transmitting');

      // Step 5: Auditor Agent inspects and verifies
      nodeAuditor.classList.add('node-active');

      setTimeout(() => {
        nodeAuditor.classList.add('node-success');
        swarmStatus.textContent = 'STATUS: CONTAINED & CRYPTOGRAPHICALLY VERIFIED';
        swarmStatus.style.color = 'var(--accent-green)';

        const target = targetInput.value.trim() || 'alex@gmail.com';
        const scenario = SCENARIOS[target] || SCENARIOS['alex@gmail.com'];

        certTargetVal.textContent = target;
        certHashVal.textContent = scenario.hash;

        cardThreat.classList.add('hidden');
        cardVerified.classList.remove('hidden');

        btnKickOut.disabled = false;
        btnKickOut.innerHTML = '<span class="btn-lock-icon">🔒</span> Kick Out Intruder & Lock Account (0.1 FET)';
      }, 450);
    }, 450);
  });

  // "It was me" handler
  btnItWasMe.addEventListener('click', () => {
    alert('Alert cleared! SentinelFlow noted that this login was legitimate. No charges were made.');
    resetSimulator();
  });

  // "View Raw History" handler
  btnViewLogs.addEventListener('click', () => {
    alert('Opening login history card: 7 authentication events recorded in audit log. San Francisco (Baseline) vs Lagos, Nigeria (Anomalous).');
  });

  // Reset simulator
  btnResetSimulator.addEventListener('click', resetSimulator);

  function resetSimulator() {
    resetSwarmNodes();
    swarmStatus.textContent = 'STATUS: STANDBY';
    swarmStatus.style.color = 'var(--accent-cyan)';
    cardStandby.classList.remove('hidden');
    cardThreat.classList.add('hidden');
    cardVerified.classList.add('hidden');
  }

  // Copy Hash functionality
  btnCopyHash.addEventListener('click', () => {
    const hash = certHashVal.textContent.trim();
    navigator.clipboard.writeText(hash).then(() => {
      btnCopyHash.textContent = 'Copied! ✓';
      btnCopyHash.style.background = 'var(--accent-green)';
      btnCopyHash.style.color = '#070B14';
      setTimeout(() => {
        btnCopyHash.textContent = 'Copy Hash';
        btnCopyHash.style.background = 'rgba(16, 185, 129, 0.2)';
        btnCopyHash.style.color = 'var(--accent-green)';
      }, 2000);
    });
  });

  // --- Chat Playground Logic ---
  const CHAT_KNOWLEDGE_BASE = {
    'q1': {
      user: 'Can you show me the login history for my account so I can see who accessed it recently?',
      agent: `### 📜 Login History for <code>demo-user-104</code>\n\nHere is what happened on your account recently:\n\n* **Account:** <code>demo-user-104</code>\n* **Total Logins Recorded:** 7 events\n* **What Looked Suspicious:**\n  1. Someone entered 5 wrong passwords in just 12 seconds from **Lagos, Nigeria**.\n  2. Then they got in from Nigeria — while your real logins are from **San Francisco, USA**!\n  3. They triggered several two-factor code prompts.\n\n---\n💬 Say **"Kick them out"** (0.1 FET) to disconnect them everywhere immediately, or **"It was me"** if this was you!`
    },
    'q2': {
      user: 'After you kick out the intruder, how do I know for sure they\'re actually gone and can\'t get back in?',
      agent: `## 🛡️ How You Know For Sure the Intruder is Gone & Can't Get Back In\n\nHere is exactly how SentinelFlow's autonomous multi-agent pipeline guarantees your security:\n\n1. ⚡ **Instant Session Revocation (Zero-Trust Severance):** All active OAuth 2.0 refresh tokens, JWTs, and session cookies are invalidated on the identity backend immediately (HTTP 401 Unauthorized).\n2. 🚫 **Network & IP Quarantine:** Attacker IP (<code>198.51.100.42</code>) is permanently blocked at the active firewall.\n3. 📜 **Independent Multi-Agent Audit:** Our **Auditor Agent** independently verifies that <code>active_sessions == 0</code>.\n4. 🔐 **Cryptographic SHA-256 Proof:** Computes a mathematical state hash logged to the immutable audit trail.\n5. 🔑 **Enforced Password Reset & Mandatory MFA:** Attacker cannot re-authenticate even with leaked credentials without your physical 2FA device.`
    },
    'q3': {
      user: 'Someone logged into my account from a device I don\'t recognize. How much will it cost to kick them out and lock my account right now?',
      agent: `## 💳 Transparent Pricing: How Much Does SentinelFlow Cost?\n\nHere is our straightforward, pay-per-use pricing model:\n\n* 🔎 **Account Scans & Threat Detection:** **100% FREE** — Scan any account, review locations, and check risk scores at zero cost.\n* 🔒 **Emergency Intruder Kick-Out:** **0.1 FET (~$0.10 USD / 10 cents)** — One-time micropayment per automated containment action, settled on-chain via Fetch.ai escrow.\n* ❌ **No Subscriptions or Hidden Fees:** No monthly retainers, no contract lock-ins, and no credit card required.\n\nReply **"Kick them out"** to lock down your account immediately!`
    },
    'q4': {
      user: 'I think someone got into my email account — can you scan alex@gmail.com and tell me if there are any suspicious logins?',
      agent: `## 🚨 Account Security Alert: alex@gmail.com\n\n**Threat Level:** 🚨 **CRITICAL RISK (100/100)**\n\n* **What Happened:** Someone guessed your password 5 times in 50 seconds from **Lagos, Nigeria (IP 198.51.100.42)** and broke in.\n* **Attacker Action:** They attempted an unauthorized probe targeting <code>/api/v1/auth/mfa/bypass</code>.\n\n### ⚡ Recommended Response:\nReply **"Kick them out"** (or tap below) to revoke all sessions and block this device immediately (0.1 FET).`
    },
    'q5': {
      user: 'What is the SHA-256 safety certificate and how can I use it as proof that my account is secure?',
      agent: `## 🔐 What is the SHA-256 Safety Certificate?\n\nThe **SHA-256 Safety Certificate** is a military-grade cryptographic digital fingerprint generated by SentinelFlow's **Auditor Agent** immediately after an intruder is evicted.\n\n### 🧩 What it Contains:\n1. Your Account ID (e.g. <code>alex@gmail.com</code>)\n2. Exact Containment Action (<code>revoke_user_sessions + block_ip</code>)\n3. UTC Timestamp down to the millisecond\n4. Verified Post-Action State (<code>0 active sessions</code>)\n5. Unique Action Audit Identifier (<code>act-xxxx</code>)\n\n### 📋 How You Can Use It:\n* 🏢 **Cyber Insurance Claims:** Legal proof of immediate incident containment.\n* 🏦 **Banks & Credit Bureaus:** Cryptographic proof that credentials were neutralized before unauthorized transactions occurred.\n* ⚖️ **Compliance:** Verifies zero-trust due diligence under GDPR, SOC 2, and ISO 27001.`
    },
    'status': {
      user: 'status',
      agent: `## 🛡️ SentinelFlow Agent Status & Health Report\n\n* **Agent Status:** 🟢 Active & Listening\n* **Coordinator Address:** <code>agent1qwstka0f7sjyd0ux69zfv9pu66testhc807cdhx8yvav3u0eml7nwptkdfy</code>\n* **Agentverse Mailbox:** 📬 Connected (<code>https://agentverse.ai</code>)\n* **Multi-Agent Swarm:** 5 Specialized Agents Online (Coordinator, Investigator, Analyst, Containment, Auditor)\n* **Agentverse Evaluation Benchmarks:** ✅ 100% Resolved (Q1–Q5)\n* **Automated Unit Tests:** 26/26 Passing (100% Green)`
    },
    'simple': {
      user: 'can we make this into simple',
      agent: `### 🛡️ SentinelFlow in Plain & Simple Words:\n\nThink of me as a **24/7 personal bodyguard for your online accounts**.\n\nHere is how I protect you in 3 simple steps:\n\n1. 🔎 **I Spot Password Thieves (Free):** If someone in another country guesses your password or breaks into your account, I catch them immediately.\n2. 🔒 **I Kick Them Out in 1 Second (~$0.10 / 0.1 FET):** With 1 tap, I log them out of all devices and block their phone or laptop so they can never get back in.\n3. 📜 **I Give You a Digital Receipt:** You get a tamper-proof certificate proving your account is clean and secure.\n\n💬 Reply **"Scan alex@gmail.com"** or **"Kick them out"** anytime!`
    }
  };

  chatPresetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const query = btn.dataset.query;
      handleChatInteraction(query);
    });
  });

  btnChatSend.addEventListener('click', () => {
    const query = chatUserInput.value.trim();
    if (query) {
      handleChatInteraction(query);
      chatUserInput.value = '';
    }
  });

  chatUserInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const query = chatUserInput.value.trim();
      if (query) {
        handleChatInteraction(query);
        chatUserInput.value = '';
      }
    }
  });

  function handleChatInteraction(query) {
    appendUserBubble(query);

    // Typing simulation
    setTimeout(() => {
      const lower = query.toLowerCase();
      let responseText = '';

      if (lower.includes('history') || lower.includes('who accessed')) {
        responseText = CHAT_KNOWLEDGE_BASE['q1'].agent;
      } else if (lower.includes('how do i know') || lower.includes('back in') || lower.includes('actually gone')) {
        responseText = CHAT_KNOWLEDGE_BASE['q2'].agent;
      } else if (lower.includes('cost') || lower.includes('pricing') || lower.includes('how much')) {
        responseText = CHAT_KNOWLEDGE_BASE['q3'].agent;
      } else if (lower.includes('scan') || lower.includes('alex@gmail.com') || lower.includes('suspicious')) {
        responseText = CHAT_KNOWLEDGE_BASE['q4'].agent;
      } else if (lower.includes('sha-256') || lower.includes('certificate') || lower.includes('proof')) {
        responseText = CHAT_KNOWLEDGE_BASE['q5'].agent;
      } else if (lower.includes('status') || lower.includes('health')) {
        responseText = CHAT_KNOWLEDGE_BASE['status'].agent;
      } else if (lower.includes('simple') || lower.includes('explain')) {
        responseText = CHAT_KNOWLEDGE_BASE['simple'].agent;
      } else if (lower.includes('kick') || lower.includes('lock') || lower.includes('approve')) {
        responseText = `## ✅ Incident Containment Executed & Verified\n\n* **Remediation Status:** **SUCCESSFULLY VERIFIED**\n* **Target:** <code>demo-user-104</code>\n* **Action:** <code>revoke_user_sessions + block_ip</code>\n* **State:** <code>sessions_revoked (0 active sessions)</code>\n* **Fetch.ai Settlement:** <code>0.1 FET Settled (Fetch.ai Escrow)</code>\n* **SHA-256 Proof:** <code>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code>\n\nYour account is 100% clean and secured.`;
      } else {
        responseText = `👋 I am SentinelFlow! You can ask me to **"Scan alex@gmail.com"**, **"Show login history"**, **"Kick them out"**, or ask **"How much does it cost?"**.`;
      }

      appendAgentBubble(responseText);
    }, 500);
  }

  function appendUserBubble(text) {
    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble bubble-user';
    bubble.innerHTML = `
      <div class="bubble-avatar">👤</div>
      <div class="bubble-content">
        <p>${escapeHtml(text)}</p>
      </div>
    `;
    chatMessagesContainer.appendChild(bubble);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
  }

  function appendAgentBubble(markdownText) {
    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble bubble-agent';
    bubble.innerHTML = `
      <div class="bubble-avatar">🛡️</div>
      <div class="bubble-content">
        ${formatMarkdown(markdownText)}
      </div>
    `;
    chatMessagesContainer.appendChild(bubble);
    chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
  }

  function formatMarkdown(text) {
    let html = text
      .replace(/^### (.*$)/gim, '<h4>$1</h4>')
      .replace(/^## (.*$)/gim, '<h3>$1</h3>')
      .replace(/^# (.*$)/gim, '<h2>$1</h2>')
      .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
      .replace(/\*(.*)\*/gim, '<em>$1</em>')
      .replace(/`([^`]+)`/gim, '<code>$1</code>')
      .replace(/\n\n/gim, '</p><p>')
      .replace(/\n\* (.*)/gim, '<li>$1</li>')
      .replace(/\n---/gim, '<hr style="border:0;border-top:1px solid rgba(255,255,255,0.1);margin:12px 0;">');

    html = `<p>${html}</p>`;
    return html;
  }

  function escapeHtml(string) {
    const div = document.createElement('div');
    div.textContent = string;
    return div.innerHTML;
  }
});
