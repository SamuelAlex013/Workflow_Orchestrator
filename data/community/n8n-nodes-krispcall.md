![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-krispcall

This repository contains the custom [n8n](https://n8n.io) node for Krispcall, designed to help you automate your telephony workflows directly within n8n. It includes the node linter and other necessary development dependencies.

**KrispCall** is an AI-powered modern telephony platform that helps businesses streamline communication with virtual numbers, advanced calling features, and seamless CRM integrations.

This **n8n community node** enables you to integrate KrispCall’s advanced telephony features into your n8n workflows. You can create and manage contacts, send SMS/MMS messages, retrieve voicemails, and manage webhooks directly from n8n.

---

## 🔧 Features

- 🔐 API key authentication
- 📇 Create and manage contacts
- 📤 Send SMS and MMS
- 📥 Retrieve voicemails and phone numbers
- 🌐 Create and delete webhooks for real-time event handling

---

## 📦 Installation

Install this community node in your n8n instance:

```bash
npm install n8n-nodes-krispcall
```

Or via the n8n Community Nodes UI (under Settings → Community Nodes → Install).

## 🔐 Authentication

To use this node, you must have a [KrispCall](https://krispcall.com) account and an API key.

### Get your API Key

1. Sign in to your [KrispCall](https://krispcall.com) account
2. Navigate to **Settings** → **Developer**
3. Click **Generate API Key**
4. Copy the key and use it when setting up **credentials** in n8n

### Credentials Setup in n8n

**Base URL:** `https://app.krispcall.com/api/v3/platform/n8n`

**API Key:** Paste your [KrispCall](https://krispcall.com) API key

## 🔁 Supported Resources & Operations Resource

| Resource    | Actions              |Triggers |
| ----------- | ----------------------- | -- |
| `Contact`   | Create, Delete | New Contact, Call Logs|
| `SMS` `MMS`  | Send              | New SMS or MMS, |
| `Voicemail` | Get| New Voicemail|

## 📘 Example Usage

### Create a Contact

1. Connect to KrispCall via `credentials`
2. Select resource: `Contact`
3. Choose operation: `Create`
4. Provide the contact details (`name`, `phone`, etc.)
5. Execute

### Send SMS

1. Select resource: `SMS`
2. Choose operation: `Send`
3. Set `phone number` and `message`
4. Execute

## License

[MIT](./LICENSE)
