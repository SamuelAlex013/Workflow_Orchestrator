# n8n-nodes-zep-v3

[![npm version](https://badge.fury.io/js/n8n-nodes-zep-v3.svg)](https://www.npmjs.com/package/n8n-nodes-zep-v3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Community node package that **replicates 100%** of the deprecated Zep nodes using **Zep API v3 semantics** (threads & user context) while preserving the **same UX** in n8n.

> 🔄 **Drop-in replacement** for the deprecated `@n8n/n8n-nodes-langchain.memoryZep` that stopped working with Zep Cloud.

## ✨ Features

- **🧠 Zep Memory (v3)** — Sub-node that plugs into AI Agent/Chat nodes via the `ai_memory` port
- **🔍 Zep Vector Store (v3)** — Root node with Insert, Search, and Get Many operations  
- **☁️ Zep Cloud compatible** — Works seamlessly with https://api.getzep.com
- **🔄 Sessions → Threads mapping** — Automatic conversion for v2 compatibility
- **🚀 Auto-thread creation** — Creates threads automatically when needed
- **📊 User context support** — Advanced context retrieval (basic/summary modes)

## 🎯 Why This Package?

The original n8n Zep nodes stopped working when Zep migrated from v2 to v3 API:
- ❌ `@n8n/n8n-nodes-langchain.memoryZep` throws "resource not found" errors
- ❌ Incompatible with Zep Cloud (uses v3 API)
- ❌ Community workflows broken for months

This package solves these issues:
- ✅ **Same interface** — No workflow changes needed
- ✅ **Zep v3 API** — Compatible with latest Zep Cloud
- ✅ **Enhanced features** — Additional context modes and auto-creation

## 📋 Requirements

- **n8n**: >= 1.82.0
- **Zep**: Cloud account or self-hosted v3
- **Installation**: Self-hosted n8n only (community packages not supported on n8n Cloud)

## 🚀 Installation

### Method 1: NPM (Recommended)
```bash
# Navigate to your n8n custom nodes directory
cd ~/.n8n/custom

# Install the package
npm install n8n-nodes-zep-v3

# Restart n8n
```

### Method 2: Git Clone
```bash
# Navigate to your n8n custom nodes directory  
cd ~/.n8n/custom

# Clone the repository
git clone https://github.com/fabiohsan/n8n-nodes-zep-v3.git

# Install dependencies and build
cd n8n-nodes-zep-v3
npm install
npm run build

# Restart n8n
```

### Docker Installation
```bash
# Connect to your n8n container
docker exec -it your_n8n_container bash

# Navigate to custom directory
cd /home/node/.n8n/custom

# Install package
npm install n8n-nodes-zep-v3

# Exit and restart container
exit
docker restart your_n8n_container
```

## ⚙️ Configuration

### 1. Set up Zep API v3 Credentials

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for **"Zep API (v3)"**
3. Configure:
   - **API Key**: Your Zep API key from [Zep Cloud](https://app.getzep.com)
   - **Base URL**: `https://api.getzep.com` (default for Zep Cloud)

### 2. Test Connection
Click **Test** to verify your credentials work with Zep v3 API.

## 📖 Usage

### Zep Memory (v3) Node

The memory node acts as a **sub-node** that connects to AI Agent/Chat nodes via the special `ai_memory` port.

#### Basic Setup
1. Add **"Zep Memory (v3)"** node to your workflow
2. Connect it to your **AI Agent** node via the **memory port**
3. Configure the **Session ID** parameter
4. Run your workflow

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **Session ID** | string | *required* | Unique identifier for the conversation thread |
| **Mode** | options | `basic` | Context retrieval mode (`basic` or `summary`) |
| **Auto-create Thread** | boolean | `true` | Automatically create thread if it doesn't exist |
| **Return Context on Add** | boolean | `false` | Return context when adding messages |
| **User ID** | string | `""` | Optional user ID for cross-thread graph building |

#### Example Configuration
```javascript
// Session ID examples
"user_123_session"           // User-specific session
"chat_{{ $json.conversation_id }}"  // Dynamic from input data  
"support_ticket_456"         // Support conversation
```

### Zep Vector Store (v3) Node

The vector store node provides document storage and semantic search capabilities.

#### Operations

##### Insert Documents
```javascript
// Input data structure
{
  "content": "Your document content here",
  "metadata": {
    "category": "support", 
    "language": "en",
    "timestamp": "2025-01-01T00:00:00Z"
  }
}
```

##### Search Documents  
```javascript
// Search configuration
{
  "query": "How do I reset my password?",
  "limit": 10,
  "searchType": "similarity"  // or "mmr"
}
```

##### Get Many Documents
```javascript
// Retrieve by UUIDs or document IDs
{
  "uuids": "uuid1,uuid2,uuid3",
  "documentIds": "doc1,doc2,doc3" 
}
```

## 🔄 Migration from Legacy Zep Nodes

### Before (Broken)
```json
{
  "nodes": [
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.memoryZep",
      "credentials": {
        "zepApi": "your_old_credentials"
      }
    }
  ]
}
```

### After (Working)
```json
{
  "nodes": [
    {
      "parameters": {
        "sessionId": "{{ $json.user_id }}"
      },
      "type": "zepMemoryV3", 
      "credentials": {
        "zepApiV3": "your_new_credentials"
      }
    }
  ]
}
```

### Migration Steps
1. ✅ Install `n8n-nodes-zep-v3`
2. ✅ Create new **Zep API (v3)** credentials  
3. ✅ Replace old **Zep Memory** nodes with **Zep Memory (v3)**
4. ✅ Update node parameters (add explicit `sessionId`)
5. ✅ Test your workflows

## 🎭 Example Workflows

### Basic AI Chatbot with Memory
```javascript
[Manual Trigger] 
    ↓
[Zep Memory (v3)]  →  [AI Agent (OpenAI)]
    ↓                      ↓  
[Return Response]  ←  [Format Output]
```

### Customer Support with Vector Search
```javascript
[Webhook Trigger]
    ↓
[Zep Vector Store (v3) - Search]  →  [AI Agent with Context]
    ↓                                     ↓
[Zep Memory (v3)]  ←  [Format Support Response]
```

### Document Ingestion Pipeline
```javascript
[Schedule Trigger]
    ↓
[Read Files]  →  [Zep Vector Store (v3) - Insert]
    ↓                ↓
[Process Text]   [Confirm Upload]
```

## 🛠️ API Compatibility

### Zep v2 → v3 Mapping

| Zep v2 Concept | Zep v3 Equivalent | This Package |
|----------------|-------------------|--------------|
| `sessions` | `threads` | ✅ Auto-mapped |
| `memory.get` | `thread.get_user_context` | ✅ Supported |
| `memory.add` | `thread.add_messages` | ✅ Supported |
| `memory.delete` | `thread.delete` | ✅ Supported |
| Collections | Collections | ✅ Unchanged |

### API Endpoints Used
- `GET /api/v2/threads/{id}/messages` - Retrieve conversation history
- `POST /api/v2/threads/{id}/messages` - Add new messages  
- `GET /api/v2/threads/{id}/context` - Get user context
- `DELETE /api/v2/threads/{id}` - Clear thread
- `POST /api/v2/collections/{name}/search` - Vector search
- `POST /api/v2/collections/{name}/documents` - Insert documents

## 🔧 Troubleshooting

### Common Issues

#### "Couldn't connect with these settings"
- ✅ Check API key is correct
- ✅ Verify Base URL is `https://api.getzep.com` (not `app.getzep.com`)
- ✅ Ensure you have Zep Cloud access

#### "Thread not found" 
- ✅ Enable **Auto-create Thread** option
- ✅ Check Session ID is not empty
- ✅ Verify thread exists in Zep Cloud dashboard

#### "Node not appearing in n8n"
- ✅ Restart n8n after installation
- ✅ Check package installed in correct directory
- ✅ Verify n8n version >= 1.82

#### Memory not persisting
- ✅ Ensure Session ID is consistent across workflow runs
- ✅ Check Zep Memory node is connected to AI Agent memory port
- ✅ Verify credentials are valid

### Debug Mode
Enable verbose logging by setting:
```bash
export N8N_LOG_LEVEL=debug
```

### Getting Help
1. 🐛 **GitHub Issues**: [Report bugs](https://github.com/fabiohsan/n8n-nodes-zep-v3/issues)
2. 💬 **n8n Community**: [Discuss usage](https://community.n8n.io)
3. 📖 **Zep Docs**: [API Reference](https://docs.getzep.com)

## 🧪 Testing

### Manual Testing
```bash
# Run type checking
npm run lint

# Build package
npm run build

# Test in development n8n instance
npm run watch  # for development
```

### Integration Testing
1. Create test workflow with Zep Memory node
2. Send test messages through AI Agent
3. Verify memory persistence across conversations
4. Test vector search with sample documents

## 🤝 Contributing

We welcome contributions! Please:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch
3. ✅ Add tests for new functionality  
4. 📝 Update documentation
5. 🔄 Submit a pull request

### Development Setup
```bash
git clone https://github.com/fabiohsan/n8n-nodes-zep-v3.git
cd n8n-nodes-zep-v3
npm install
npm run watch  # Development mode
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **n8n Team** - For the amazing workflow automation platform
- **Zep Team** - For the powerful memory management service  
- **Community** - For feedback and feature requests

## 🔗 Links

- 📦 [NPM Package](https://www.npmjs.com/package/n8n-nodes-zep-v3)
- 💻 [GitHub Repository](https://github.com/fabiohsan/n8n-nodes-zep-v3)
- 🌐 [Zep Cloud](https://app.getzep.com)
- 📚 [Zep Documentation](https://docs.getzep.com)
- 🤖 [n8n Documentation](https://docs.n8n.io)

---

**⭐ If this package helped you, please give it a star on GitHub!**