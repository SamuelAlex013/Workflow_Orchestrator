# n8n-nodes-sqlite-memory

[![npm version](https://badge.fury.io/js/n8n-nodes-sqlite-memory.svg)](https://badge.fury.io/js/n8n-nodes-sqlite-memory)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful N8N community node for AI Chat Memory with SQLite3 backend. Provides persistent local storage for chat conversations without external dependencies.

## 🚀 Features

- **🗄️ Local SQLite Storage**: No external database required - works out of the box
- **🔑 Session Management**: Organize conversations by unique session keys
- **📊 Smart Context Window**: Token-aware message retrieval with configurable limits
- **🤖 AI Integration**: Auto-detect and store user inputs and AI responses
- **🧹 Auto-cleanup**: Automatically maintains last 50 messages per session
- **⚡ Zero Configuration**: Works immediately after installation
- **🔄 Legacy Support**: Backward compatible with existing message formats

## 📦 Installation

### Option 1: Install via npm (Recommended)
```bash
npm install n8n-nodes-sqlite-memory
```

### Option 2: Manual Installation
1. Download the latest release
2. Place in your N8N custom nodes directory
3. Restart N8N

## 🛠️ Operations

### 📥 Get Messages
Retrieves recent messages from a chat session.

**Parameters:**
- `Session Key`: Unique identifier for the chat session
- `Window Size`: Number of recent messages to retrieve (default: 10)

**Output:**
```json
{
  "messages": [
    { "id": "uuid", "role": "user", "content": "Hello", "timestamp": 1703123456789 },
    { "id": "uuid", "role": "assistant", "content": "Hi there!", "timestamp": 1703123456790 }
  ],
  "sessionKey": "chat-123",
  "count": 2
}
```

### ➕ Add Message
Manually stores a message in the chat session.

**Parameters:**
- `Session Key`: Unique identifier for the chat session
- `Role`: Message sender role (user/assistant/system)
- `Message Content`: The message text to store

**Output:**
```json
{
  "success": true,
  "sessionKey": "chat-123",
  "message": {
    "role": "user",
    "content": "Hello"
  }
}
```

### 🔄 Auto-Store User Input
Automatically detects and stores user input from the previous node.

**Detects input from:**
- `chatInput`
- `message`
- `content`
- `text`
- `query`

**Output:**
```json
{
  "success": true,
  "sessionKey": "chat-123",
  "message": { "role": "user", "content": "Hello" },
  "chatInput": "Hello"
}
```

### 🤖 Auto-Store AI Response
Automatically detects and stores AI responses with metadata.

**Supports formats:**
- OpenAI API responses
- LangChain outputs
- Simple text responses

**Output:**
```json
{
  "success": true,
  "sessionKey": "chat-123",
  "message": {
    "role": "assistant",
    "content": "Hi there!",
    "metadata": {
      "model": "gpt-3.5-turbo",
      "tokens": 150
    }
  }
}
```

### 🎯 Format for AI
Formats conversation history for AI consumption with token limits.

**Parameters:**
- `Session Key`: Chat session identifier
- `Token Limit`: Maximum tokens for context (default: 4000)
- `AI Model`: Model for token counting (GPT-3.5/GPT-4)

**Output:**
```json
{
  "messages": [
    { "role": "user", "content": "Hello" },
    { "role": "assistant", "content": "Hi there!" }
  ],
  "sessionKey": "chat-123",
  "tokenLimit": 4000,
  "model": "gpt-3.5-turbo"
}
```

### 🧠 Smart Context Window
Retrieves context-aware message window based on token limits.

**Output:**
```json
{
  "messages": [...],
  "sessionKey": "chat-123",
  "count": 5,
  "tokenLimit": 4000
}
```

### 🗑️ Clear Memory
Removes all messages for a specific session.

**Output:**
```json
{
  "success": true,
  "sessionKey": "chat-123",
  "cleared": true
}
```

## 📋 Usage Examples

### Basic Chat Memory Flow
```
[Chat Trigger] → [SQLite Memory: Auto-Store User] → [OpenAI] → [SQLite Memory: Auto-Store AI]
```

### Context-Aware AI Chat
```
[Webhook] → [SQLite Memory: Auto-Store User] → [SQLite Memory: Format for AI] → [OpenAI] → [SQLite Memory: Auto-Store AI]
```

### Manual Message Management
```
[Manual Trigger] → [SQLite Memory: Add Message] → [SQLite Memory: Get Messages]
```

### Smart Context Retrieval
```
[HTTP Request] → [SQLite Memory: Smart Context Window] → [Process Messages] → [Response]
```

## 🗃️ Database Schema

**File Location**: Database file created in N8N working directory

**Table Structure**:
```sql
CREATE TABLE memory (
  sessionKey TEXT PRIMARY KEY,
  messages TEXT,
  created INTEGER,
  lastAccessed INTEGER
)
```

**Message Format**:
```json
{
  "id": "uuid-v4",
  "role": "user|assistant|system",
  "content": "message text",
  "timestamp": 1703123456789,
  "metadata": {
    "model": "gpt-3.5-turbo",
    "tokens": 150
  }
}
```

## ⚙️ Configuration

### Session Keys
- **Auto-generated**: Leave empty for automatic UUID generation
- **Custom**: Use consistent keys across workflow nodes
- **Best Practice**: Use meaningful identifiers like `user-${userId}-chat`

### Token Limits
- **GPT-3.5 Turbo**: 4,096 tokens (recommended: 3,500)
- **GPT-4**: 8,192 tokens (recommended: 7,500)
- **GPT-4 Turbo**: 128,000 tokens (recommended: 120,000)

### Window Sizes
- **Small conversations**: 5-10 messages
- **Medium conversations**: 20-30 messages
- **Large conversations**: 50+ messages (auto-trimmed)

## 🔧 Advanced Usage

### Custom Session Management
- Use consistent session keys across workflow nodes
- Generate meaningful identifiers for better organization
- Implement user-specific session isolation

### Conditional Memory Storage
- Filter messages based on importance or content type
- Implement selective storage logic
- Skip memory operations when not needed

### Message Preprocessing
- Clean and validate message content before storage
- Add custom metadata for tracking
- Transform message format as needed

## 🚨 Troubleshooting

### Node Not Appearing
- Verify package installation
- Restart N8N service
- Check custom extensions configuration

### Database Issues
- **Permission errors**: Ensure N8N has write access to working directory
- **File not found**: Database auto-creates on first use
- **Corruption**: Reset database if needed (data will be lost)

### Memory Not Persisting
- **Check session keys**: Must be consistent across operations
- **Verify operations**: Ensure using correct operation types
- **Database location**: Check N8N working directory

### Performance Issues
- **Large sessions**: Use Smart Context Window instead of Get Messages
- **Token limits**: Reduce window size or token limits
- **Cleanup**: Regularly clear old sessions

## 📊 Performance Tips

1. **Use Smart Context Window** for large conversations
2. **Set appropriate token limits** based on your AI model
3. **Implement session cleanup** for old conversations
4. **Use consistent session keys** to avoid fragmentation
5. **Monitor database size** and clean up periodically

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Links

- [GitHub Repository](https://github.com/Promit-revar/N8n_node)
- [npm Package](https://www.npmjs.com/package/n8n-nodes-sqlite-memory)
- [N8N Community](https://community.n8n.io/)
- [Issue Tracker](https://github.com/Promit-revar/N8n_node/issues)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Promit-revar/N8n_node/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Promit-revar/N8n_node/discussions)
- **Community**: N8N Community Forums

---

Made with ❤️ for the N8N community