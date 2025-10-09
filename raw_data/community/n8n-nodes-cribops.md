# n8n-nodes-cribops

This is an n8n community node. It lets you use Cribops in your n8n workflows.

Cribops is the platform where teams build, deploy, and scale AI-powered automation agents for customer service, support, and business operations.

> **Note**: This integration requires an active subscription with [Cribops.com](https://cribops.com). Sign up for an account to obtain your API credentials.

## Features

- **Scalable Automation**: Build resilient workflows with AI agents that handle customer interactions at scale
- **AWS Service Integration**: Leverage AWS SQS queues and SNS topics for enterprise-grade message processing
- **Real-time Communication**: HTTP webhooks enable instant bidirectional messaging between n8n and Cribops agents
- **Smart Agent Routing**: Dynamic agent selection ensures messages reach the right automation specialist
- **Context Preservation**: Maintains full conversation history across complex multi-step workflows
- **Enterprise Security**: Dual authentication with API tokens and AWS credentials for secure cloud operations
- **File Processing**: Handle documents, images, and attachments through S3 presigned URLs
- **Event-Driven Triggers**: Filter and respond to specific event types for targeted automation

## Nodes Included

### 1. Cribops Node
Execute operations on Cribops automation agents:
- **Send Messages**: Dispatch requests to AI agents with file attachments and metadata
- **Manage Conversations**: Reply to ongoing conversations while maintaining full context
- **Agent Operations**: List available agents, retrieve agent details, and route dynamically
- **Real-time Status**: Send typing indicators to show processing activity
- **Custom Properties**: Attach metadata for workflow-specific data handling

### 2. Cribops Trigger Node
Receive and process events from Cribops automation platform:
- **Webhook Reception**: Instantly receive messages from users and agents
- **Smart Filtering**: Process only relevant events (user messages, agent responses, attachments)
- **Secure Validation**: Verify webhook authenticity with secret tokens
- **Data Enrichment**: Automatically include routing information for seamless replies
- **Queue Integration**: Future support for AWS SQS polling for guaranteed message delivery
- **Topic Subscriptions**: Future support for AWS SNS for event broadcasting

## Installation

### Prerequisites
- Node.js >= 20.15
- n8n >= 1.0.0
- Active Cribops subscription (visit [cribops.com](https://cribops.com) to sign up)
- Cribops API access token (available in your Cribops dashboard)

### Via npm (Recommended)
```bash
npm install n8n-nodes-cribops
```

### Via n8n GUI (For verified community nodes)
1. Go to **Settings** → **Community Nodes**
2. Click **Install a Community Node**
3. Enter: `n8n-nodes-cribops`
4. Click **Install**

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/CloudBedrock/n8n-nodes-cribops.git
cd n8n-nodes-cribops

# Install dependencies
npm install

# Build the package
npm run build

# Link globally for testing
npm link
```

## Configuration

### 1. Cribops API Credentials
Create a new credential in n8n:
- **Credential Type**: Cribops API
- **API Token**: Your Cribops API token (Required)
- **Base URL**: Your Cribops instance URL (e.g., `https://api.cribops.com`)
- **Account ID**: (Optional) Account ID for AWS service integration
- **Account Secret**: (Optional) Secret key for AWS service integration
- **Region**: (Optional) AWS region for cloud services (default: us-east-1)

### 2. Agent Selection
The nodes automatically populate available agents from your Cribops instance. Select the appropriate agent from the dropdown when configuring each node.

## Usage Examples

### Customer Support Automation
```
[Cribops Trigger] → [Sentiment Analysis] → [Route to Agent] → [Cribops Response]
```
Automatically analyze customer sentiment and route to specialized AI agents based on urgency and topic.

### Document Processing Pipeline
```
[Cribops Trigger] → [Extract Attachment] → [OCR/Parse] → [Database] → [Cribops Response]
```
Process incoming documents, extract data, store in database, and respond with confirmation.

### Multi-Channel Integration
```
[Slack] → [Format Message] → [Cribops Agent] → [Process] → [Email/SMS/Slack]
```
Receive requests from any channel, process with Cribops agents, and respond across multiple platforms.

### Escalation Workflow
```
[Cribops Trigger] → [Check Complexity] → [If Complex] → [Human Review] → [Cribops Response]
```
Automatically escalate complex requests while handling routine inquiries with AI agents.

## API Integration

### Cribops Platform Endpoints
- `GET /api/v1/agents` - Agent selection and retrieval
- `GET /api/v1/agents/{agent_id}` - Get specific agent details
- `POST /webhooks/agents/{agent_id}/message` - HTTP webhook endpoint
- `POST /api/v1/agents/{agent_id}/files` - File uploads
- `POST /api/v1/agents/{agent_id}/typing` - Send typing indicators
- Response webhook URL provided in incoming messages for replies
- AWS SQS queue endpoints (when configured with AWS credentials)
- AWS SNS topic endpoints (when configured with AWS credentials)

### Message Formats

#### Incoming User Message
```json
{
  "conversation_id": "uuid-v4",
  "content": "Hello, I need help with...",
  "message_id": "uuid-v4",
  "user_id": "uuid-v4",
  "organization_id": "uuid-v4",
  "timestamp": "2025-01-10T16:00:00Z",
  "response_webhook": "https://api.cribops.com/webhooks/response/uuid-v4",
  "type": "user_message",
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
git clone https://github.com/CloudBedrock/n8n-nodes-cribops.git
cd n8n-nodes-cribops

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
npm link n8n-nodes-cribops
N8N_CUSTOM_EXTENSIONS=n8n-nodes-cribops n8n start
```

## Configuration Examples

### Environment Variables
```bash
# For local development
export CRIBOPS_API_URL=http://localhost:4000

# AWS configuration (optional)
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key

# For n8n configuration
export N8N_CUSTOM_EXTENSIONS=n8n-nodes-cribops
export N8N_NODES_INCLUDE=n8n-nodes-cribops
```

### Docker Configuration
```dockerfile
FROM n8nio/n8n:latest

# Install the community node
RUN npm install -g n8n-nodes-cribops

# Set environment variables
ENV N8N_CUSTOM_EXTENSIONS=n8n-nodes-cribops
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
3. Ensure Cribops platform can reach your n8n instance

#### File Upload Problems
1. Verify S3 configuration in Cribops platform
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

This n8n community node is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Important License Clarification:**
- The MIT license applies **only** to this n8n node integration code
- Cribops platform, services, and AI agents are licensed separately by CloudBedrock
- Use of Cribops services requires an active subscription and acceptance of Cribops Terms of Service
- CloudBedrock proprietary components and APIs remain under CloudBedrock's commercial license
- This open-source node is a client interface and does not grant any license to use Cribops services beyond your subscription terms

## Support

- **Documentation**: [GitHub Wiki](https://github.com/CloudBedrock/n8n-nodes-cribops/wiki)
- **Issues**: [GitHub Issues](https://github.com/CloudBedrock/n8n-nodes-cribops/issues)
- **Community**: [n8n Community](https://community.n8n.io)
- **Cribops Platform**: [cribops.com](https://cribops.com)

## Changelog

### Version 0.1.5
- Initial release
- HTTP webhook support for sending and receiving messages
- File attachment handling with S3 presigned URLs
- Dynamic agent selection with search functionality
- Reply to conversation functionality with webhook context
- Typing indicator support
- Event type filtering for trigger node
- AWS credentials support for future SQS/SNS integration
- Secret token validation for webhooks
- Message metadata support

## Related Projects

- [n8n](https://github.com/n8n-io/n8n) - Workflow automation platform
- [Cribops AI](https://cribops.com) - AI agent platform

---

**Note**: This is a community-maintained package that requires an active Cribops subscription. For official support, please contact the Cribops AI team at [cribops.com](https://cribops.com).

## Disclaimer

This n8n node is provided as an open-source integration tool. CloudBedrock and Cribops are registered trademarks of CloudBedrock, Inc. The use of these trademarks in this project is for identification purposes only and does not imply endorsement.
