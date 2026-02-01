# n8n-nodes-hcaptcha

[![npm version](https://badge.fury.io/js/n8n-nodes-hcaptcha.svg)](https://www.npmjs.com/package/n8n-nodes-hcaptcha)

This is an [n8n](https://n8n.io/) community node that enables verification of hCaptcha responses within your workflows.

The node acts as a proxy to the hCaptcha verification API, allowing you to securely validate user captcha tokens server-side as part of your automation.

- 📦 [View on npm](https://www.npmjs.com/package/n8n-nodes-hcaptcha)
- 🧩 Works with n8n self-hosted and n8n cloud
- 🔒 Securely handles hCaptcha verification with secret keys

---

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

---

## Installation

Follow the [n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to add this node to your n8n instance.

---

## Operations

- **Verify hCaptcha token**: Send a user’s hCaptcha response token and your secret key to the official hCaptcha verification endpoint to confirm validity.

---

## Credentials

This node requires an **hCaptcha secret key** to authenticate with the hCaptcha API.

### Prerequisites

- Sign up for an hCaptcha account at [https://www.hcaptcha.com/](https://www.hcaptcha.com/).
- Register your site to get your **Secret Key** from the hCaptcha dashboard.

### Authentication

- The node uses this secret key as a credential.
- In n8n, create an **hCaptcha API credential** and securely store your secret key.
- Link this credential in the node’s settings when configuring workflows.

---

## Compatibility

- Minimum tested n8n version: **v0.230.0**
- Compatible with n8n cloud and self-hosted setups.
- No known incompatibilities as of this version.

---

## Usage

1. Add the **hCaptcha Proxy** node to your workflow.
2. Select or create your hCaptcha API credential with your secret key.
3. Pass the user’s hCaptcha response token to the node’s `response` parameter.
4. Execute the node to verify the token with hCaptcha servers.
5. Use the verification result (`success` boolean and additional data) in your workflow logic.

If you're new to n8n, check out the [Try it out](https://docs.n8n.io/try-it-out/) guide for basics.

---

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [hCaptcha official documentation](https://docs.hcaptcha.com/)

---

## Version history

- **v0.1.3**: Initial release supporting hCaptcha response verification via secret key and token.
