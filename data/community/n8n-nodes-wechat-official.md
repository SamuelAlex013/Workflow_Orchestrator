# n8n-nodes-wechat-official

[![npm version](https://badge.fury.io/js/%40xwang152%2Fn8n-nodes-wechat-official.svg)](https://badge.fury.io/js/%40xwang152%2Fn8n-nodes-wechat-official)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.15-brightgreen.svg)](https://nodejs.org/)
[![n8n Community Node](https://img.shields.io/badge/n8n-Community%20Node-FF6D5A.svg)](https://docs.n8n.io/integrations/community-nodes/)
[![GitHub Stars](https://img.shields.io/github/stars/xwang152-jack/n8n-nodes-wechat-official.svg)](https://github.com/xwang152-jack/n8n-nodes-wechat-official/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/xwang152-jack/n8n-nodes-wechat-official.svg)](https://github.com/xwang152-jack/n8n-nodes-wechat-official/issues)

> 🚀 **Professional WeChat Official Account integration for n8n workflows**

This is an n8n community node that provides comprehensive WeChat Official Account API integration, enabling you to automate WeChat content management, user interactions, and media operations within your n8n workflows.

[WeChat Official Account](https://mp.weixin.qq.com/) is China's leading social media platform for businesses, allowing organizations to create official accounts for customer engagement, content publishing, and service delivery.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## 📋 Table of Contents

- [✨ Key Features](#-key-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🔐 Authentication](#-authentication)
- [⚙️ Operations](#️-operations)
- [🤖 AI Tool Integration](#-ai-tool-integration)
- [🐳 Docker Deployment](#-docker-deployment)
- [📚 Usage Examples](#-usage-examples)
- [🔧 Development](#-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🆘 Support](#-support)

## ✨ Key Features

### 🎯 **Core Capabilities**
- 🔑 **Smart Token Management** - Automatic access token caching and refresh
- 📁 **Complete Material Management** - Upload images, voice, video, and thumbnails
- 📝 **Draft Management** - Create, edit, and publish article drafts
- 🛡️ **Robust Error Handling** - Comprehensive error codes mapping and retry mechanisms
- 🚀 **High Performance** - Batch processing and intelligent rate limiting
- 🔒 **Enterprise Security** - IP whitelist support and credential encryption

### 🤖 **Advanced Integration**
- 🔧 **Dual Usage Mode** - Works as both workflow node and AI tool (`usableAsTool: true`)
- 🔄 **Batch Operations** - Efficient bulk media uploads and content management
- 📊 **Real-time Monitoring** - Built-in logging and performance metrics
- 🌐 **Multi-environment Support** - Production and sandbox environments

### 🛠️ **Developer Experience**
- 📖 **Comprehensive Documentation** - Detailed guides and examples
- 🧪 **Full Test Coverage** - Jest-based testing suite
- 🎨 **TypeScript Support** - Full type safety and IntelliSense
- 🔍 **ESLint Integration** - Code quality and consistency

## 🚀 Quick Start

### Prerequisites
- n8n instance (version 1.0.0 or higher)
- WeChat Official Account with API access
- Node.js 20.15 or higher

### 1-Minute Setup

1. **Install the node**:
   ```bash
   npm install n8n-nodes-wechat-official
   ```

2. **Configure credentials** in n8n:
   - App ID: Your WeChat Official Account App ID
   - App Secret: Your WeChat Official Account App Secret
   - Environment: Choose 'production' or 'sandbox'

3. **Start automating** - Add the WeChat Official Account node to your workflow!

## 📦 Installation

### Method 1: npm Installation (Recommended)

```bash
# Install globally for n8n
npm install -g n8n-nodes-wechat-official

# Or install in your n8n project
npm install @xwang152/n8n-nodes-wechat-official
```

### Method 2: Community Node Installation

1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter: `@xwang152/n8n-nodes-wechat-official`
4. Click **Install**

For detailed instructions, follow the [n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/).

### Method 3: Manual Installation

```bash
# Clone the repository
git clone https://github.com/xwang152-jack/n8n-nodes-wechat-official.git
cd n8n-nodes-wechat-official

# Install dependencies and build
npm install
npm run build

# Link to your n8n installation
npm link
```

## 🔐 Authentication

### Setting Up Credentials

This node requires WeChat Official Account API credentials:

| Field | Description | Required | Example |
|-------|-------------|----------|----------|
| **App ID** | WeChat Official Account App ID | ✅ | `wx1234567890abcdef` |
| **App Secret** | WeChat Official Account App Secret | ✅ | `abcdef1234567890...` |
| **Environment** | API environment | ✅ | `production` or `sandbox` |
| **Server IP** | Your server IP for whitelist | ⚠️ | `192.168.1.100` |

### Getting Your Credentials

1. **Access WeChat Platform**
   - Visit [WeChat Official Account Platform](https://mp.weixin.qq.com/)
   - Login with your account credentials

2. **Navigate to Developer Settings**
   - Go to **Development** > **Basic Configuration**
   - Copy your **App ID** and **App Secret**

3. **Configure IP Whitelist** (Production Only)
   - Add your server IP to the whitelist
   - This is mandatory for production API access

### Security Best Practices

- ✅ Store credentials securely in n8n credential store
- ✅ Use environment variables for sensitive data
- ✅ Regularly rotate App Secret (recommended: every 90 days)
- ✅ Monitor API usage and access logs
- ✅ Enable IP whitelist for production environments

## ⚙️ Operations

### 🔑 Access Token Management
- **Get Access Token** - Retrieve and cache access tokens
  - ⚡ Automatic caching (2-hour validity)
  - 🔄 Smart refresh mechanism
  - 🛡️ Error handling for expired tokens

### 📁 Material Management
- **Upload Image** - Upload images for articles and media
  - 📸 Support for base64 encoded images
  - ✅ Automatic format validation (JPG, PNG)
  - 📏 Size limit validation (up to 10MB)
  - 🆔 Returns media_id for further use

- **Upload Media** - Upload permanent media files
  - 🎵 **Voice**: MP3, WMA, WAV, AMR (up to 60s, 2MB)
  - 🎬 **Video**: MP4 (up to 10MB)
  - 🖼️ **Thumbnail**: JPG, PNG (up to 64KB)
  - 📦 Batch upload capabilities
  - 🔍 File validation and error reporting

### 📝 Draft Management
- **Add Draft** - Create new article drafts
  - 📝 Rich text content support
  - 🖼️ Media attachment handling
  - 👀 Draft validation and preview
  - 📊 Content statistics

- **Publish Draft** - Publish draft articles
  - 🚀 Automatic publishing workflow
  - 📈 Status tracking and confirmation
  - 🔄 Error recovery mechanisms
  - 📅 Scheduled publishing support

## 🤖 AI Tool Integration

This node supports **AI Tool Calling Mode** (`usableAsTool: true`), enabling seamless integration with AI assistants and automated systems.

### Integration Methods

#### 1. Workflow Node
```
[Trigger] → [WeChat Official Account] → [Other Nodes]
```

#### 2. AI Tool Calling
```javascript
// AI assistants can directly invoke node functions
const result = await wechatNode.execute({
  resource: 'material',
  operation: 'uploadImage',
  image: 'base64_encoded_image'
});
```

#### 3. API Integration
```bash
# Direct API integration
curl -X POST /api/wechat/upload-image \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_encoded_image"}'
```

### Benefits of AI Integration
- 🤖 **AI Assistant Integration** - Let AI manage WeChat operations automatically
- 🔧 **Programmatic Access** - Use in custom scripts and applications
- 📦 **Batch Processing** - Efficient bulk operations
- ⚡ **Real-time Integration** - Immediate response for time-sensitive tasks
- 🔄 **Event-driven Automation** - Trigger actions based on external events

## 🐳 Docker Deployment

### Quick Start with Docker Compose

```yaml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n-wechat
    ports:
      - "5679:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=password
    volumes:
      - n8n_data:/home/node/.n8n
      - ./dist:/home/node/.n8n/custom  # Plugin files
    command: >
      sh -c "mkdir -p /home/node/.n8n/custom && 
             chown -R node:node /home/node/.n8n/custom && 
             n8n start"

volumes:
  n8n_data:
```

### Deployment Steps

1. **Build the plugin**:
   ```bash
   npm run build
   ```

2. **Start with Docker Compose**:
   ```bash
   docker-compose up -d
   ```

3. **Access n8n**:
   - URL: http://localhost:5679
   - Username: admin
   - Password: password

### Verification

```bash
# Check plugin installation
docker exec n8n-wechat ls -la /home/node/.n8n/custom

# Verify plugin files
docker exec n8n-wechat find /home/node/.n8n/custom -name '*.js' -type f
```

## 📚 Usage Examples

### Example 1: Automated Content Publishing

```json
{
  "workflow": {
    "nodes": [
      {
        "name": "Upload Thumbnail",
        "type": "n8n-nodes-wechat-official",
        "parameters": {
          "resource": "material",
          "operation": "uploadImage",
          "image": "{{ $binary.data.data }}"
        }
      },
      {
        "name": "Create Article Draft",
        "type": "n8n-nodes-wechat-official",
        "parameters": {
          "resource": "draft",
          "operation": "addDraft",
          "title": "{{ $json.title }}",
          "content": "{{ $json.content }}",
          "thumb_media_id": "{{ $node['Upload Thumbnail'].json.media_id }}"
        }
      },
      {
        "name": "Publish Article",
        "type": "n8n-nodes-wechat-official",
        "parameters": {
          "resource": "draft",
          "operation": "publishDraft",
          "media_id": "{{ $node['Create Article Draft'].json.media_id }}"
        }
      }
    ]
  }
}
```

### Example 2: Batch Media Upload

```json
{
  "resource": "material",
  "operation": "uploadMedia",
  "type": "image",
  "media": [
    {"name": "product1.jpg", "data": "base64_data_1"},
    {"name": "product2.jpg", "data": "base64_data_2"},
    {"name": "product3.jpg", "data": "base64_data_3"}
  ]
}
```

### Example 3: AI-Powered Content Management

```javascript
// AI assistant automatically manages WeChat content
const aiWorkflow = {
  trigger: 'schedule',
  actions: [
    {
      tool: 'wechat-official-account',
      operation: 'generateContent',
      parameters: {
        topic: 'daily news',
        style: 'professional',
        includeImages: true
      }
    },
    {
      tool: 'wechat-official-account', 
      operation: 'publishDraft',
      parameters: {
        scheduleTime: 'tomorrow 9:00 AM'
      }
    }
  ]
};
```

## 🔧 Development

### Requirements

- **Node.js**: >= 20.15.0
- **TypeScript**: >= 5.8.0
- **n8n**: >= 1.0.0

### Development Setup

```bash
# Clone repository
git clone https://github.com/xwang152-jack/n8n-nodes-wechat-official.git
cd n8n-nodes-wechat-official

# Install dependencies
npm install

# Start development mode
npm run dev
```

### Available Scripts

```bash
# Build project
npm run build

# Run tests
npm test

# Run tests with coverage
npm run test:coverage

# Watch mode for tests
npm run test:watch

# Code linting
npm run lint

# Fix linting issues
npm run lintfix

# Format code
npm run format
```

### Project Structure

```
n8n-nodes-wechat-official/
├── 📁 credentials/                 # Authentication credentials
│   └── WechatOfficialAccountApi.credentials.ts
├── 📁 nodes/
│   └── 📁 WechatOfficialAccount/  # Main node implementation
│       ├── 📁 types/              # TypeScript type definitions
│       ├── 📁 utils/              # Utility functions
│       ├── WechatOfficialAccount.node.ts
│       └── wechat.svg            # Node icon
├── 📁 test/                       # Test files
├── 📁 dist/                       # Built files
├── 📄 package.json
├── 📄 tsconfig.json
├── 📄 jest.config.js
└── 📄 README.md
```

### Testing

```bash
# Run all tests
npm test

# Run specific test file
npm test -- WechatOfficialAccount.test.ts

# Run tests with coverage report
npm run test:coverage
```

### Code Quality

This project maintains high code quality standards:

- ✅ **TypeScript** - Full type safety
- ✅ **ESLint** - Code linting and style enforcement
- ✅ **Prettier** - Code formatting
- ✅ **Jest** - Comprehensive testing
- ✅ **Husky** - Git hooks for quality checks

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow TypeScript best practices
- Write comprehensive tests for new features
- Update documentation for API changes
- Follow the existing code style
- Add meaningful commit messages

## 📄 License

[MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help

If you encounter issues or need assistance:

1. 📖 **Check Documentation** - Review this README and inline documentation
2. 🔍 **Search Issues** - Look through [existing GitHub issues](https://github.com/xwang152-jack/n8n-nodes-wechat-official/issues)
3. 🆕 **Create New Issue** - [Submit a detailed bug report or feature request](https://github.com/xwang152-jack/n8n-nodes-wechat-official/issues/new)
4. 💬 **Community Support** - Join the [n8n Community Forum](https://community.n8n.io/)
5. 📧 **Direct Contact** - Email: xwagn152@163.com

### Troubleshooting

#### Common Issues

**Q: "Access token invalid" error**
A: Check your App ID and App Secret, ensure IP whitelist is configured correctly.

**Q: "Media upload failed" error**  
A: Verify file format and size limits, check network connectivity.

**Q: "Draft publishing failed" error**
A: Ensure draft content is complete and complies with WeChat specifications.

#### API Limitations

- **Access Token**: Valid for 7200 seconds (2 hours) - automatically managed
- **Temporary Materials**: Valid for 3 days
- **API Call Frequency**: Follow WeChat Official Account Platform rate limits
- **File Size Limits**: Images (10MB), Voice (2MB), Video (10MB)

### Resources

- 📖 [WeChat Official Account API Documentation](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html)
- 🔗 [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- 🌐 [WeChat Official Account Platform](https://mp.weixin.qq.com/)
- 💬 [n8n Community Forum](https://community.n8n.io/)

---

<div align="center">

**🎉 Ready to automate your WeChat Official Account?**

[Install Now](#-installation) • [View Examples](#-usage-examples) • [Get Support](#-support)

**Made with ❤️ by [xwang152-jack](https://github.com/xwang152-jack)**

⭐ **Star this repo if it helped you!** ⭐

</div>
