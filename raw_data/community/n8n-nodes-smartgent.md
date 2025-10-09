# 🤖 n8n-nodes-smartgent

**SmartGent Custom Nodes for n8n** - AI-powered automation and intelligent workflow integrations including LiteLLM chat completions and S3/MinIO file storage.

[![npm version](https://badge.fury.io/js/n8n-nodes-smartgent.svg)](https://badge.fury.io/js/n8n-nodes-smartgent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

SmartGent brings intelligent enterprise search capabilities, AI chat completions, and cloud storage integration to your n8n workflows. Search through your organization's knowledge base using AI-powered chatbots, interact with LLM models, and manage file storage seamlessly.

## ✨ Features

- 🧠 **AI-Powered Enterprise Search** - Intelligent search through enterprise knowledge bases
- 🤖 **Dynamic Chatbot Selection** - Choose from available enterprise chatbots
- 💬 **LiteLLM Chat Completions** - Interact with various LLM models through LiteLLM API
- 📁 **SmartGent MinIO File Storage** - Upload files and generate presigned URLs for S3/MinIO
- 🔧 **Multiple Node Types** - Regular workflow nodes and AI Agent tool versions
- 🛡️ **Secure Authentication** - API key-based authentication with configurable base URLs
- 📊 **Rich Response Data** - Structured results with source attribution and metadata
- 🎯 **AI Agent Compatible** - Tool versions work seamlessly with n8n AI Agent nodes

## 📦 Installation

### Via n8n Community Nodes (Recommended)
1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Click **Install** and enter: `n8n-nodes-smartgent`
3. Click **Install** and restart n8n

### Via npm
```bash
npm install n8n-nodes-smartgent
```

## 🔧 Available Nodes

### SmartGent Enterprise Search
Main workflow node for manual enterprise search operations.

**Operations:**
- **Get Chatbots** - Retrieve list of available enterprise chatbots
- **Search** - Perform intelligent search using selected chatbot

### SmartGent Enterprise Search Tool  
AI Agent tool version for automated searches initiated by AI agents.

**Features:**
- Automatically called by AI Agent nodes
- Returns formatted text optimized for AI consumption
- Same search capabilities as the main node

### LiteLLM Chat
Interact with various LLM models through the LiteLLM API.

**Features:**
- Support for multiple LLM providers
- Text and mixed content (text + files) support
- Dynamic model selection
- Streaming and non-streaming responses

### SmartGent MinIO
Comprehensive file storage solution for S3 and MinIO-compatible services.

**Operations:**
- **Upload File** - Upload binary or text files to buckets
- **Generate Presigned URL** - Create time-limited access URLs
- **Upload and Get Presigned URL** - Combined operation for efficiency

**Features:**
- Support for AWS S3 and MinIO
- Binary and text file uploads
- Custom metadata and headers
- Configurable expiration times
- Path-style and virtual-hosted-style URLs

## ⚙️ Configuration

### Credentials Setup
1. Create **SmartGent API** credentials in n8n
2. Configure the following:
   - **API Key**: Your SmartGent API key
   - **Base URL**: SmartGent API base URL (e.g., `https://smartgendev.w3btest.com`)

### Node Configuration
- **Chatbot Selection**: Choose from dynamically loaded enterprise chatbots
- **Search Query**: Enter your search query or use expressions
- **Max Results**: Limit the number of results returned (default: 10)

## 🎯 Usage Examples

### Basic Enterprise Search
1. Add **SmartGent Enterprise Search** node to your workflow
2. Configure your SmartGent API credentials
3. Select **Search** operation
4. Choose a chatbot (e.g., "Toyota - all about toyota")
5. Enter your search query: "What's the price of RAV4?"
6. Execute the workflow

### AI Agent Integration
1. Add **AI Agent** node to your workflow
2. Connect **SmartGent Enterprise Search Tool** to the AI Agent
3. Configure the chatbot selection
4. The AI will automatically use the tool when users ask relevant questions

Example AI conversation:
```
User: "What are the latest Toyota car prices?"
AI Agent: *automatically calls SmartGent tool*
AI Agent: "Based on the latest information, here are the Toyota car prices..."
```

### Workflow Automation
```javascript
// Example: Auto-search when new support ticket arrives
{
  "nodes": [
    {"type": "Webhook Trigger"},
    {"type": "SmartGent Enterprise Search", "operation": "search"},
    {"type": "Send Email"}
  ]
}
```

## 📋 API Response Format

The search operation returns structured data:

```json
{
  "operation": "search",
  "chatbotGuid": "07929b5a-a298-4df1-8cbf-d5fef990c120",
  "query": "rav4 price",
  "results": {
    "success": true,
    "docs": [
      {
        "content": "2025 Toyota RAV4 pricing information...",
        "filename": "toyota_price_list.pdf",
        "page_number": 1
      }
    ]
  },
  "timestamp": "2025-01-27T08:15:30Z",
  "resultCount": 3
}
```

## 🔍 Supported Operations

| Operation | Description | Use Case |
|-----------|-------------|----------|
| Get Chatbots | List available enterprise chatbots | Discovery, configuration |
| Search | Execute search query using selected chatbot | Information retrieval |

## 🛠️ Development

### Prerequisites
- Node.js >= 20.15
- n8n installed

### Local Development
```bash
# Clone the repository
git clone https://github.com/chassis-app/n8n-nodes-smartgent.git
cd n8n-nodes-smartgent

# Install dependencies
npm install

# Build the project
npm run build

# Link for local testing
npm link
```

### Testing
```bash
# Run linting
npm run lint

# Format code
npm run format

# Build and test
npm run build
```

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run `npm run lint` and `npm run format`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [SmartGent API Documentation](https://docs.smartgent.ai)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [Issue Tracker](https://github.com/chassis-app/n8n-nodes-smartgent/issues)

## 📞 Support

- 📧 Email: max.cheung@jarvisnsam.ai
- 🐛 Issues: [GitHub Issues](https://github.com/chassis-app/n8n-nodes-smartgent/issues)
- 💬 Community: [n8n Community Forum](https://community.n8n.io)

---

Made with ❤️ for the n8n community
