# Enhanced Claude Code - n8n Community Node

[![npm version](https://badge.fury.io/js/n8n-nodes-claudecode-enhanced.svg)](https://badge.fury.io/js/n8n-nodes-claudecode-enhanced)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **An enhanced version of the Claude Code n8n community node with enterprise features!**

This project extends the original [@holtweb/n8n-nodes-claudecode](https://github.com/holt-web-ai/n8n-nodes-claudecode) with powerful enhancements for production use.

## ✨ Key Features

- ✅ **Native Authentication** - Built-in credential management without CLI dependency
- ✅ **Direct API Access** - Bypass Claude Code CLI when needed
- ✅ **Latest Models** - Access to Claude 3.5 Sonnet, Haiku, and Opus
- ✅ **Enterprise Ready** - Advanced error handling, debugging, and monitoring
- ✅ **Backward Compatible** - Works with existing workflows
- 🔄 **Future MCP Support** - Native MCP protocol integration (planned)

## 🔥 What's Enhanced

| Feature | Original | Enhanced |
|---------|----------|----------|
| **Authentication** | CLI-only | Built-in credentials + CLI |
| **API Access** | CLI wrapper only | Direct API + CLI fallback |
| **Model Support** | Legacy names | Latest model identifiers |
| **Error Handling** | Basic | Enterprise-grade recovery |
| **Configuration** | Static | Dynamic with validation |
| **Debugging** | Limited | Comprehensive logging |

## 🚀 Quick Start

### Docker (Recommended)

```bash
docker run -it --rm \
  -p 5678:5678 \
  -e N8N_COMMUNITY_NODE_PACKAGES="n8n-nodes-claudecode-enhanced" \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### npm

```bash
npm install n8n-nodes-claudecode-enhanced
```

## 📖 Documentation

- 📚 **[Complete Documentation](README-ENHANCED.md)** - Detailed setup and usage guide
- 🎯 **[Migration Guide](#migration)** - Upgrade from the original node
- 🔧 **[API Reference](#configuration)** - All parameters and options
- ❓ **[Troubleshooting](#troubleshooting)** - Common issues and solutions

## 🎯 Migration from Original

The enhanced node is **100% backward compatible**. Simply:

1. Install the enhanced package
2. Replace "Claude Code" nodes with "Claude Code Enhanced"
3. Optionally configure new authentication method
4. Enjoy the new features!

## 🔧 Configuration

### Authentication Options

#### Option 1: API Key (Recommended)
```javascript
// In n8n Credentials
{
  "authMethod": "credentials",
  "apiKey": "sk-ant-your-api-key",
  "organizationId": "optional-org-id"
}
```

#### Option 2: CLI Authentication  
```javascript
// Uses existing Claude Code CLI setup
{
  "authMethod": "cli"
}
```

### Operation Modes

#### Query Mode
Start fresh conversations with full tool access:
```javascript
{
  "operation": "query",
  "prompt": "Create a Python web scraper",
  "model": "claude-3-5-sonnet-20241022"
}
```

#### Continue Mode  
Maintain conversation context:
```javascript
{
  "operation": "continue", 
  "prompt": "Now add error handling"
}
```

#### Direct API Mode
Fast text generation without tools:
```javascript
{
  "operation": "direct",
  "prompt": "Explain async/await in JavaScript",
  "model": "claude-3-5-sonnet-20241022",
  "maxTokens": 2000,
  "temperature": 0.3
}
```

## 🏗️ Development

### Building from Source

```bash
git clone https://github.com/shaike1/n8n-claudecode.git
cd n8n-claudecode
npm install
npm run build
```

### Testing Locally

```bash
npm link
n8n start
```

### Project Structure

```
├── nodes/
│   └── ClaudeCode/
│       ├── ClaudeCode.node.ts          # Original node (maintained)
│       └── ClaudeCodeEnhanced.node.ts  # Enhanced node
├── credentials/
│   ├── ClaudeCodeApi.credentials.ts    # API credential type
│   └── MCPServer.credentials.ts        # MCP server credential (future)
├── examples/                           # Usage examples
├── workflow-templates/                 # Pre-built workflows
└── docs/                              # Additional documentation
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

### v1.0.0 ✅ (Current)
- Native authentication support
- Direct API access capability  
- Latest Claude model support
- Enhanced error handling and debugging

### v1.1.0 🔄 (In Progress)
- Native MCP protocol support
- Advanced MCP server management
- Streaming response support
- Workflow templates

### v1.2.0 📅 (Planned)
- OAuth2 authentication
- Team/organization management
- Usage analytics and monitoring
- Custom tool development SDK

## 🐛 Troubleshooting

### Common Issues

**"Invalid API key" Error**
- Verify your Anthropic API key is correct
- Ensure sufficient API credits
- Check base URL if using custom endpoint

**"Claude Code CLI not found"**  
- Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
- Authenticate: `claude auth login`
- Verify: `claude --version`

**Timeout Errors**
- Increase timeout in Additional Options
- Break complex tasks into smaller steps
- Use Continue operation for multi-step workflows

**Node Not Appearing**
- Restart n8n after installation
- Check community packages are enabled
- Verify package name: `@shaike1/n8n-nodes-claudecode-enhanced`

### Debug Mode

Enable detailed logging:
```javascript
{
  "additionalOptions": {
    "debug": true
  }
}
```

## 📄 License

MIT License - see [LICENSE.md](LICENSE.md) for details.

## 🙏 Acknowledgments

- Built on the excellent work by [Adam Holt](https://github.com/holt-web-ai/n8n-nodes-claudecode)
- Powered by [Anthropic's Claude](https://www.anthropic.com/claude) AI models
- Integrated with [n8n](https://n8n.io) workflow automation platform

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/shaike1/n8n-claudecode/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/shaike1/n8n-claudecode/discussions)
- 📖 **Documentation**: [Enhanced Guide](README-ENHANCED.md)
- 🌟 **Community**: [n8n Community Forum](https://community.n8n.io/)

---

⭐ **If this project helps you, please give it a star!** ⭐