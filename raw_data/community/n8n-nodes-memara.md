# Memara n8n Community Node

![Memara Logo](https://raw.githubusercontent.com/memara-ai/brand/main/logos/light/memara_logo_256x256.png)

A powerful n8n community node that integrates Memara's semantic memory system into your workflows. Store, search, and retrieve memories with AI-powered semantic search capabilities.

## 🚀 Features

- **Semantic Memory Storage**: Store information with intelligent context understanding
- **AI-Powered Search**: Find relevant memories using natural language queries
- **Memory Spaces**: Organize memories in isolated spaces for different projects
- **CRUD Operations**: Complete create, read, update, delete functionality
- **API Integration**: Direct integration with Memara's production API
- **Easy Configuration**: Simple API key authentication setup

## 📦 Installation

### Option 1: n8n Community Node Installation (Recommended)

1. In your n8n instance, go to **Settings** → **Community Nodes**
2. Enter the package name: `n8n-nodes-memara`
3. Click **Install**

### Option 2: Manual Installation

```bash
# Using npm
npm install n8n-nodes-memara

# Using yarn
yarn add n8n-nodes-memara
```

### Option 3: Development Installation

```bash
# Clone and install locally
git clone https://github.com/memara-ai/n8n-nodes-memara.git
cd n8n-nodes-memara
npm install
npm run build
npm link

# Link to your n8n installation
cd ~/.n8n/nodes
npm link n8n-nodes-memara
```

## 🔧 Configuration

### 1. Get Your Memara API Key

1. Visit [Memara Dashboard](https://app.memara.io)
2. Go to **Settings** → **API Keys**
3. Create a new API key
4. Copy the key (format: `mk_live_...`)

### 2. Configure Credentials in n8n

1. In n8n, create a new **Memara API** credential
2. Enter your API key
3. (Optional) Set a default Space ID
4. Test the connection

### 3. Add Memara Node to Workflow

1. In your workflow, click **Add Node**
2. Search for "Memara"
3. Select the Memara node
4. Choose your configured credentials

## 📝 Usage Examples

### Basic Memory Creation

```json
{
  "resource": "memory",
  "operation": "create",
  "content": "Customer John Smith reported billing issue with invoice #12345. Resolved by applying 10% discount due to delayed delivery.",
  "title": "Customer Issue Resolution",
  "tags": "customer-service, billing, discount"
}
```

### Semantic Memory Search

```json
{
  "resource": "memory",
  "operation": "search",
  "query": "billing problems with customers",
  "limit": 5
}
```

### Memory Space Management

```json
{
  "resource": "space",
  "operation": "create",
  "name": "Customer Support",
  "description": "Knowledge base for customer support team"
}
```

## 🎯 Common Workflow Patterns

### 1. Customer Support Knowledge Base

```
1. HTTP Request → Fetch support ticket
2. Memara → Search for similar issues
3. Memara → Create memory of resolution
4. Email → Send response to customer
```

### 2. Content Creation Assistant

```
1. Webhook → Receive content request
2. Memara → Search for related content
3. Code → Generate new content using context
4. Memara → Store new content as memory
```

### 3. Lead Qualification System

```
1. Form → Capture lead information
2. Memara → Search for similar leads
3. Memara → Store lead profile
4. Slack → Alert sales team with context
```

## 🔍 Available Operations

### Memory Operations

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Create** | Store new memory | `content` |
| **Search** | Find relevant memories | `query` |
| **Update** | Modify existing memory | `memoryId`, `content` |
| **Delete** | Remove memory | `memoryId` |
| **List** | Get all memories | None |

### Space Operations

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **List** | Get all spaces | None |
| **Create** | Create new space | `name` |

## ⚙️ Parameters Reference

### Memory Parameters

- **Content** (required): The main content/information to store
- **Title** (optional): Short title for the memory
- **Tags** (optional): Comma-separated tags for organization
- **Space ID** (optional): Target space (uses default if not specified)
- **Memory ID** (required for update/delete): Unique memory identifier

### Search Parameters

- **Query** (required): Natural language search query
- **Limit** (optional): Maximum results to return (1-100, default: 10)
- **Space ID** (optional): Search within specific space

### Space Parameters

- **Name** (required): Space name
- **Description** (optional): Space description

## 🐛 Troubleshooting

### Common Issues

#### "Invalid API Key" Error
- Verify your API key is correct and starts with `mk_live_`
- Check that the key hasn't expired in your Memara dashboard
- Ensure you're using the production API URL: `https://api.memara.io`

#### "Space Not Found" Error
- Verify the Space ID exists in your Memara account
- Check if you have access to the specified space
- Use the List Spaces operation to see available spaces

#### Node Not Appearing in n8n
- Restart n8n after installation
- Check that the package installed correctly: `npm list n8n-nodes-memara`
- Verify n8n version compatibility (requires n8n 1.0+)

### Getting Help

- **Documentation**: [docs.memara.io](https://docs.memara.io)
- **API Reference**: [docs.memara.io/api](https://docs.memara.io/api)
- **Support**: [support@memara.io](mailto:support@memara.io)
- **Community**: [Join our Discord](https://discord.gg/memara)

## 🧪 Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/memara-ai/n8n-nodes-memara.git
cd n8n-nodes-memara

# Start development environment
./scripts/docker-n8n.sh start

# Access environments
# Development: http://localhost:5678 (admin/admin)
# Testing: http://localhost:5679 (admin/admin)
```

### Available Scripts

```bash
# Build the node
./scripts/docker-n8n.sh build

# Run linter
./scripts/docker-n8n.sh lint

# View logs
./scripts/docker-n8n.sh logs

# Execute commands in container
./scripts/docker-n8n.sh exec npm test
```

## 📄 License

MIT License - see [LICENSE.md](LICENSE.md) for details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

- **Website**: [memara.io](https://memara.io)
- **Documentation**: [docs.memara.io](https://docs.memara.io)
- **Email**: [support@memara.io](mailto:support@memara.io)
- **GitHub Issues**: [Report a bug](https://github.com/memara-ai/n8n-nodes-memara/issues)

---

Made with ❤️ by the [Memara Team](https://memara.io)
