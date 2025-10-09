# n8n-nodes-lerty

A custom n8n community node package for seamless integration with the Lerty AI platform. This package provides two specialized nodes that enable communication between n8n workflows and Lerty agents through HTTP webhooks.

## Features

- **HTTP Webhook Integration**: Reliable message exchange through webhook endpoints
- **File Attachments**: Full support for file uploads and downloads via S3 presigned URLs
- **Dynamic Agent Selection**: Automatically populated agent dropdown from Lerty API
- **Message Filtering**: Filter incoming messages by event type
- **Conversation Context**: Maintains conversation context across message exchanges
- **Secure Authentication**: Bearer token authentication for API access

## Nodes Included

### 1. Lerty Node
A regular node for sending messages to Lerty agents with support for:
- Message sending with file attachments
- Reply to existing conversations
- Agent information retrieval
- File upload capabilities

### 2. Lerty Trigger Node
A trigger node for receiving messages from Lerty users with:
- HTTP webhook message reception
- File attachment handling
- Conversation context preservation
- Message filtering by event type
- Automatic agent ID inclusion in output

## Installation

### Prerequisites
- Node.js >= 20.15
- n8n >= 1.0.0
- Lerty AI platform account with API access

### Via npm (Recommended)
```bash
npm install n8n-nodes-lerty
```

### Via n8n GUI (For verified community nodes)
1. Go to **Settings** → **Community Nodes**
2. Click **Install a Community Node**
3. Enter: `n8n-nodes-lerty`
4. Click **Install**

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/CloudBedrock/n8n-nodes-lerty.git
cd n8n-nodes-lerty

# Install dependencies
npm install

# Build the package
npm run build

# Link globally for testing
npm link
```

## Configuration

### 1. Lerty API Credentials
Create a new credential in n8n:
- **Credential Type**: Lerty API
- **Server URL**: Your Lerty instance URL (e.g., `https://lerty.ai`)
- **Bearer Token**: Your Lerty API token
- **Organization ID**: (Optional) Your organization ID
- **Tenant ID**: (Optional) Your tenant ID

### 2. Agent Selection
The nodes automatically populate available agents from your Lerty instance. Select the appropriate agent from the dropdown when configuring each node.

## Usage Examples

### Basic Message Flow
```
[Lerty Trigger] → [Process Message] → [Lerty Response]
```

### File Attachment Workflow
```
[Lerty Trigger] → [Download File] → [Process] → [Lerty Response with File]
```

### Multi-Step Processing
```
[Lerty Trigger] → [Data Processing] → [Database] → [Lerty Response]
```

## API Integration

### Lerty Platform Endpoints
- `GET /api/v1/agents` - Agent selection
- `POST /webhooks/agents/{agent_id}/message` - HTTP webhook endpoint
- `POST /api/v1/agents/{agent_id}/files` - File uploads
- Response webhook URL provided in incoming messages for replies

### Message Formats

#### Incoming User Message
```json
{
  "conversation_id": "uuid-v4",
  "content": "Hello, I need help with...",
  "message_id": "uuid-v4",
  "user_id": "uuid-v4",
  "timestamp": "2025-01-10T16:00:00Z",
  "attachments": [
    {
      "type": "image",
      "url": "https://s3.amazonaws.com/...",
      "filename": "screenshot.png",
      "size": 1024000,
      "mime_type": "image/png"
    }
  ]
}
```

#### Outgoing Agent Response
```json
{
  "conversation_id": "uuid-v4",
  "content": "I can help you with that...",
  "message_id": "external-id-123",
  "timestamp": "2025-01-10T16:01:00Z",
  "attachments": [
    {
      "type": "file",
      "url": "https://s3.amazonaws.com/...",
      "filename": "report.pdf",
      "size": 2048000,
      "mime_type": "application/pdf"
    }
  ]
}
```

## Development

### Setup
```bash
# Clone repository
git clone https://github.com/CloudBedrock/n8n-nodes-lerty.git
cd n8n-nodes-lerty

# Install dependencies
npm install

# Start development mode
npm run dev
```

### Building
```bash
# Build TypeScript and icons
npm run build

# Lint code
npm run lint

# Format code
npm run format
```

### Testing
```bash
# Run tests
npm run test

# Test with local n8n instance
npm link
npm link n8n-nodes-lerty
N8N_CUSTOM_EXTENSIONS=n8n-nodes-lerty n8n start
```

## Configuration Examples

### Environment Variables
```bash
# For local development
export LERTY_API_URL=http://localhost:4000

# For n8n configuration
export N8N_CUSTOM_EXTENSIONS=n8n-nodes-lerty
export N8N_NODES_INCLUDE=n8n-nodes-lerty
```

### Docker Configuration
```dockerfile
FROM n8nio/n8n:latest

# Install the community node
RUN npm install -g n8n-nodes-lerty

# Set environment variables
ENV N8N_CUSTOM_EXTENSIONS=n8n-nodes-lerty
```

## Troubleshooting

### Common Issues

#### Node Not Appearing in n8n
1. Ensure the package is properly installed
2. Check that `N8N_CUSTOM_EXTENSIONS` is set correctly
3. Restart n8n after installation

#### Webhook Connection Issues
1. Verify webhook URL is correctly configured
2. Check bearer token authentication
3. Ensure Lerty platform can reach your n8n instance

#### File Upload Problems
1. Verify S3 configuration in Lerty platform
2. Check file size limits
3. Ensure proper MIME type handling

### Debug Mode
Enable debug logging in n8n:
```bash
export N8N_LOG_LEVEL=debug
n8n start
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow TypeScript best practices
- Add tests for new functionality
- Update documentation as needed
- Follow n8n community node guidelines

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [Lerty Platform Docs](https://docs.lerty.ai)
- **Issues**: [GitHub Issues](https://github.com/CloudBedrock/n8n-nodes-lerty/issues)
- **Community**: [n8n Community](https://community.n8n.io)

## Changelog

### Version 0.1.0
- Initial release
- HTTP webhook support for sending and receiving messages
- File attachment handling
- Dynamic agent selection
- Reply to conversation functionality

## Related Projects

- [n8n](https://github.com/n8n-io/n8n) - Workflow automation platform
- [Lerty AI](https://lerty.ai) - AI agent platform

---

**Note**: This is a community-maintained package. For official support, please contact the Lerty AI team.