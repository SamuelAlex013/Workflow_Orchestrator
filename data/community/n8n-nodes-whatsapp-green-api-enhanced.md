# Green API Enhanced - WhatsApp Automation Nodes for n8n

## ⚠️ **IMPORTANT NOTICE - גירסה בעבודה**

**🚧 Version 1.2.0-1.2.1 is currently UNSTABLE and under active development**

- **Icons may not display correctly**
- **Nodes may appear scattered (not grouped properly)**  
- **Some functionality is still being tested**
- **Not recommended for production use yet**

**Please be patient while we work on stabilizing the package. A stable version will be released soon.**

---

## Description

Enhanced n8n community nodes for WhatsApp automation using Green API with advanced filtering, file support, and comprehensive event handling.

## Features

- **Enhanced Main Node**: Send messages, manage groups, get chat history, manage contacts
- **Advanced Trigger**: 27 different Green API events with smart filtering
- **Media Nodes**: Dedicated nodes for Voice, Document, and Image processing
- **File Support**: Automatic download and processing of media files
- **Comprehensive Filtering**: Filter by keywords, chat types, message types, and more

## Installation

```bash
npm install n8n-nodes-whatsapp-green-api-enhanced
```

## Quick Start

1. **Add Green API Credentials**:
   - Instance ID from Green API dashboard
   - API Token from Green API dashboard

2. **Use the Nodes**:
   - **Green API Enhanced**: Main operations node
   - **Green API Trigger**: Webhook trigger for incoming events
   - **Green API Get Voice**: Download voice messages
   - **Green API Get Document**: Download documents
   - **Green API Get Image**: Download images

## Available Nodes

### 1. Green API Enhanced
Main operations node with support for:
- **Messages**: Send text, files, polls, locations, contacts
- **Groups**: Create, manage, add/remove participants
- **Chats**: Get chat history and information
- **Contacts**: Retrieve contact lists

### 2. Green API Trigger
Advanced webhook trigger supporting 27 different events:
- Message events (text, media, reactions)
- Group events (join, leave, updates)
- Presence updates
- Call events
- And many more...

### 3. Media Processing Nodes
- **Green API Get Voice**: Download and process voice messages
- **Green API Get Document**: Download documents and files
- **Green API Get Image**: Download images with caption support

## Configuration

### Credentials Setup
1. Go to [Green API](https://green-api.com)
2. Create an instance and get your credentials:
   - Instance ID
   - API Token Instance
3. Add these credentials to your n8n instance

### Basic Workflow Example
```
Green API Trigger → Green API Get Voice → Process Audio
```

## Advanced Features

### Event Filtering
The trigger supports advanced filtering options:
- **Event Types**: Choose from 27 different event types
- **Chat Filters**: Filter by specific chats or chat types
- **Keyword Filtering**: Filter messages by keywords
- **Bot Detection**: Exclude automated messages
- **File Type Filters**: Process only specific file types

### File Handling
- Automatic file download from WhatsApp
- Binary data support for n8n workflows
- Support for images, audio, documents, videos, and stickers
- Configurable file type filtering

## Event Types Supported

- `session.status` - Session status changes
- `message` - Any incoming message
- `message.reaction` - Message reactions
- `message.ack` - Message delivery status
- `group.join` - Group member additions
- `group.leave` - Group member removals
- `presence.update` - User presence changes
- `call.received` - Incoming calls
- And 19 more event types...

## Requirements

- n8n version 0.198.0 or higher
- Green API account with active instance
- Node.js 16.0.0 or higher

## Support

For issues and feature requests, please visit our [GitHub repository](https://github.com/dacho2025/n8n-nodes-whatsapp-green-api-enhanced).

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

---

**Note**: This package enhances WhatsApp automation capabilities. Please ensure compliance with WhatsApp's terms of service and applicable privacy laws when using these nodes.