# n8n-nodes-romulus

**n8n-nodes-romulus** is an n8n community node that enables you to interact with the **Romulus API** within your n8n workflows.

[Romulus](https://romulus.live) is a tool integrated with Voxloud that delivers an automated phone call experience. It provides APIs to manage robocalls, AI agents, and messaging bots for seamless communication workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform that lets you connect services and automate tasks visually.

---

## Table of Contents

- [Installation](#installation)  
- [Operations](#operations)  
- [Credentials](#credentials)  
- [Compatibility](#compatibility)  
- [Usage](#usage)  
- [Resources](#resources)  
- [Version History](#version-history)  

---

## Installation

To install this community node, follow the [n8n community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/).

---

## Operations

This node currently supports the following Romulus operations:

- **Calls**
  - List or initiate robocalls.
  
- **Users / AI Agents**
  - Start AI agents or calls.
  - List available agents.
  
- **Messenger**
  - List WhatsApp bots.
  - Send WhatsApp templated messages via bots.
  
- **Triggers**
  - Start workflows on real-time Romulus events such as:
    - robocall started
    - agentcall completed
    - agent action completed

---

## Credentials

To use this node, you’ll need a **Romulus API key**.

1. Sign in to your [Voxloud](https://voxloud.com) account.
2. Go to **Integrations → Romulus** and set up the Romulus integration.
3. Once configured, you will be given a **Romulus API key**.
4. In **n8n**, navigate to **Credentials > Create New > Romulus API** and enter your API key.
5. n8n will automatically test the connection.

> ⚠️ Note: While the API key is obtained from Voxloud, it authenticates directly with the **Romulus API**. All requests in this node are sent to `https://api.romulus.live`.

---

## Compatibility

- Tested with **n8n v1.94.1**
- No known incompatibilities with other versions.

---

## Usage

- Use the **Romulus Trigger** node to initiate workflows based on real-time events (e.g., when a robocall starts or an agent completes a call).
- Use resource nodes (Calls, Agents, Messenger) to manage Romulus operations directly.
- For webhook-based triggers to work, ensure your n8n instance is accessible from the internet (e.g., use [ngrok](https://ngrok.com/) during development).

---

## Resources

- 📘 [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/#community-nodes)  
- 📚 [Romulus API Documentation](https://developer.romulus.live)

---

## Version History

- **1.0.0**: Initial release with support for:
  - Robocalls  
  - AI agents  
  - WhatsApp messaging  
  - Webhook-based event triggers
