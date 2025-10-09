# n8n-nodes-wbiztool

N8n nodes for WbizTool WhatsApp Business Automation Platform integration.

## Overview

This package provides 10 production-ready n8n nodes to integrate with the WbizTool platform, enabling automated WhatsApp messaging workflows. WbizTool is a comprehensive WhatsApp Business Automation Platform that allows you to send messages, manage campaigns, check message status, and manage WhatsApp clients.

## Features

### 🚀 **Core Messaging Nodes**
- **WbizTool Send Message**: Send individual WhatsApp messages with text, images, documents, or videos
- **WbizTool Send Group Message**: Send messages to WhatsApp groups  
- **WbizTool Send Multi Message**: Send bulk messages to multiple recipients
- **WbizTool Schedule Message**: Schedule messages for future delivery with timezone support
- **WbizTool Cancel Message**: Cancel scheduled messages before they're sent

### 📊 **Status & Monitoring Nodes**
- **WbizTool Message Status**: Check delivery status and read receipts for sent messages
- **WbizTool Check Credentials**: Validate API credentials and account status

### 🔧 **WhatsApp Client Management Nodes**
- **WbizTool List WhatsApp Clients**: Get list of all connected WhatsApp clients
- **WbizTool Create WhatsApp Client**: Create new WhatsApp client connections
- **WbizTool WhatsApp Client Status**: Monitor WhatsApp client connection status

## Installation

### Method 1: Install from npm (Recommended)
```bash
npm install n8n-nodes-wbiztool
```

### Method 2: Install in n8n using the UI
1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Enter: `n8n-nodes-wbiztool`
3. Click **Install**

After installation, restart your n8n instance to load the new nodes.

## Configuration

### Prerequisites
1. Create a WbizTool account at [https://wbiztool.com](https://wbiztool.com)
2. Connect your WhatsApp account in [WhatsApp Settings](https://wbiztool.com/whatsapp-settings/)
3. Generate API credentials from [API Keys page](https://wbiztool.com/settings/#api-keys)

### Credentials Setup
1. In n8n, create new **WbizTool API** credentials
2. Enter your:
   - **Base URL**: `https://wbiztool.com/api/v1/` (default)
   - **Client ID**: Your unique client ID from API Keys page
   - **API Key**: Your API key from API Keys page
   - **WhatsApp Client ID**: Your WhatsApp client ID from WhatsApp Settings

## Quick Start Examples

### 📱 Send Your First Message
1. Add the **"WbizTool Send Message"** node to your workflow
2. Configure your WbizTool credentials  
3. Set the message parameters:
   - **Message Type**: Text (0), Image (1), Document (2), or Video (3)
   - **Message**: Your message content
   - **Phone Number**: Recipient's phone number with country code (e.g., `919876543210`)
   - **Country Code**: Recipient's country code (e.g., `91` for India)

### ⏰ Schedule a Message
1. Add the **"WbizTool Schedule Message"** node
2. Set scheduling parameters:
   - **Message**: Your scheduled message content
   - **Phone Number**: Recipient's number
   - **Schedule Date**: Date in `YYYY-MM-DD` format
   - **Schedule Time**: Time in `HH:MM` format
   - **Timezone**: Select appropriate timezone

### 📊 Check Message Status
1. Add the **"WbizTool Message Status"** node
2. Provide the **Message ID** from a previously sent message
3. Get delivery status, read receipts, and timestamps

### 👥 Send Group Messages
1. Add the **"WbizTool Send Group Message"** node
2. Provide the **Group ID** (get from WhatsApp group info)
3. Set your message content and type

## Supported Message Types

| Type | Value | Description | Supported Formats |
|------|-------|-------------|-------------------|
| Text | `0` | Plain text messages | UTF-8 text |
| Image | `1` | Image messages | JPG, PNG, GIF |
| Document | `2` | Document/File messages | PDF, DOC, XLS, etc. |
| Video | `3` | Video messages | MP4, AVI, MOV |

## API Endpoints Used

This package integrates with the following WbizTool REST API endpoints:
- `POST /api/v1/me/` - Credential validation
- `POST /api/v1/send_msg/` - Send individual messages
- `POST /api/v1/send_msg/group/` - Send group messages  
- `POST /api/v1/send_msg/multi/` - Send bulk messages
- `POST /api/v1/schedule_msg/` - Schedule messages
- `POST /api/v1/cancel_msg/` - Cancel scheduled messages
- `GET /api/v1/message/status/<id>/` - Get message status
- `GET /api/v1/whatsapp-client/list/` - List WhatsApp clients
- `POST /api/v1/whatsapp-client/create/` - Create WhatsApp client
- `GET /api/v1/whatsapp-client/status/` - Get client status

## Rate Limits

- **Free Plan**: 10 requests per minute
- **Paid Plans**: 100+ requests per minute  
- **Enterprise**: Custom limits available

## Error Handling

All nodes include comprehensive error handling with detailed error messages:
- **401 Unauthorized**: Invalid API credentials
- **400 Bad Request**: Invalid phone number format or missing required fields
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server-side issues

## Troubleshooting

### Common Issues
1. **Credential Test Fails**: Verify your Client ID and API Key from [API Keys page](https://wbiztool.com/settings/#api-keys)
2. **WhatsApp Not Connected**: Ensure your WhatsApp is connected in [WhatsApp Settings](https://wbiztool.com/whatsapp-settings/)
3. **Invalid Phone Format**: Use international format with country code (e.g., `919876543210`)

## Support & Documentation

- **WbizTool Dashboard**: [https://wbiztool.com/dashboard/](https://wbiztool.com/dashboard/)
- **API Keys Management**: [https://wbiztool.com/settings/#api-keys](https://wbiztool.com/settings/#api-keys)
- **WhatsApp Settings**: [https://wbiztool.com/whatsapp-settings/](https://wbiztool.com/whatsapp-settings/)
- **Platform Docs**: [https://wbiztool.com/docs/](https://wbiztool.com/docs/)

## Contributing

We welcome contributions! Please check our GitHub repository for development guidelines and current milestones.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Version History

### v0.1.0 (Current)
✅ **Complete n8n Integration Package**
- 10 production-ready nodes covering all core WbizTool APIs
- Secure credential management with connection testing
- Comprehensive error handling and validation
- Support for text, image, document, and video messages
- Message scheduling with timezone support
- WhatsApp client management capabilities
- Delivery status tracking and monitoring

---

**🚀 Ready for Production • Made with ❤️ for the n8n Community**

*Install now: `npm install n8n-nodes-wbiztool`* 