## Try it in 60 seconds

1) Download the ready-to-import workflow:
   - **Raw JSON (direct import)**  
     https://raw.githubusercontent.com/gitadta/n8n-nodes-cyberpulse-compliance/dev/examples/cyberpulse-template.json
   - **Browse in GitHub (human-readable)**  
     https://github.com/gitadta/n8n-nodes-cyberpulse-compliance/blob/dev/examples/cyberpulse-template.json

2) In n8n: **Workflows → Import from file** and select the JSON.

3) When prompted, select/create the **Header Auth** credential (paste your CyberPulse API key as the `Authorization` header value, e.g. `Bearer <YOUR_KEY>`).

4) Click **Execute workflow**.


## Getting Started (3 steps)

1) Install node: **Community Nodes → n8n-nodes-cyberpulse-compliance-dev**
2) Create credentials: **HTTP Header Auth** → Header **x-api-key** → paste your CyberPulse API key → **Save**
3) Import and run: `examples/cyberpulse-template.json` (works with free tier)

## Pricing
- **Starter (Free):** 100 evaluations/month, community support
- **Pro ($29/mo):** 1,000/mo, 30-day retention, metrics, email support
- **Business ($99/mo):** 5,000/mo, 90-day retention, audit logs export, priority support
- **Enterprise (Custom):** SSO, custom retention, dedicated support

## Limits & Errors
- Over cap → `{"error":"quota_exceeded","upgrade_url":"https://cyberpulsesolutions.com/pricing"}`
- Burst too fast → `{"error":"rate_limited","retry_after_seconds":60}`
- Missing key → `{"error":"auth_required","message":"Add API key in node credentials"}`

# CyberPulse Compliance (n8n Community Node)

[![npm version](https://img.shields.io/npm/v/n8n-nodes-cyberpulse-compliance.svg)](https://www.npmjs.com/package/n8n-nodes-cyberpulse-compliance)
[![GitHub issues](https://img.shields.io/github/issues/gitadta/n8n-nodes-cyberpulse-compliance)](https://github.com/gitadta/n8n-nodes-cyberpulse-compliance/issues)
[![GitHub stars](https://img.shields.io/github/stars/gitadta/n8n-nodes-cyberpulse-compliance)](https://github.com/gitadta/n8n-nodes-cyberpulse-compliance/stargazers)
[![License](https://img.shields.io/npm/l/n8n-nodes-cyberpulse-compliance.svg)](./LICENSE)

Custom n8n node that evaluates compliance controls against major frameworks (ISO 27001, NIST CSF, PCI DSS, Essential Eight, GDPR, etc.).

---

## ✨ Features
- Classifies control text into categories: MFA, Encryption, Logging, Backups, Patching, Access Reviews  
- Validates evidence links  
- Returns compliance status: **Compliant / Partial / Non-Compliant**  
- Maps controls to frameworks via external `crosswalk.json`  

---

## 🚀 Installation
1. In n8n, go to **Settings → Community Nodes → Install**  
2. Enter:
   ```bash
   n8n-nodes-cyberpulse-compliance-dev
🔧 Usage

Example workflow:

Add CyberPulse Compliance Node in your workflow

Provide compliance control text or questionnaire input

The node validates and classifies the response

Outputs can be routed to Google Sheets, Email, or Dashboards

Example Input:

PCI DSS Control 1.2 – Is a firewall deployed?


Example Output:

Compliant | Partial | Non-Compliant (with notes and framework mapping)

### Links
- [npm package](https://www.npmjs.com/package/n8n-nodes-cyberpulse-compliance-dev)
- [GitHub repository](https://github.com/gitadta/cyberpulse-node-dev)
- [Report issues](https://github.com/gitadta/cyberpulse-node-dev/issues)


📜 License

This project is licensed under the MIT License
