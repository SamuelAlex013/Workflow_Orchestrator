# n8n-nodes-longcat

This is an n8n community node for [LongCat Chat](https://longcat.chat/) API integration with **AI Agent Compatibility**. It allows you to interact with LongCat's AI models directly from your n8n workflows and works seamlessly with AI agents and tools.

## 🤖 AI Agent Integration

This node is specifically designed to work with AI agents and provides:

- **AI Tool Mode**: Enhanced integration with AI agents and MCP servers
- **Structured Output**: JSON responses for better AI agent parsing
- **Thinking Capabilities**: Advanced reasoning with LongCat-Flash-Thinking model
- **Agent-Friendly Parameters**: Optimized for AI agent usage patterns
- **Metadata Enrichment**: Rich response data for AI processing

## Features

- **Chat Completions**: Send messages to LongCat AI models
- **Model Selection**: Choose between LongCat-Flash-Chat and LongCat-Flash-Thinking
- **Thinking Mode**: Enable thinking capabilities for the LongCat-Flash-Thinking model
- **AI Tool Mode**: Enhanced AI agent integration with structured responses
- **Response Format**: Support for both text and JSON output formats
- **Parameter Control**: Adjust temperature, max tokens, thinking budget, and other parameters
- **Error Handling**: Comprehensive error handling with meaningful messages
- **Usage Statistics**: Track token usage and costs
- **Agent Metadata**: Enhanced response data for AI processing

## Installation

### Community Node (Recommended)

1. Open your n8n instance
2. Go to "Settings" > "Community Nodes"
3. Select "Install"
4. Enter `n8n-nodes-longcat` in the "Enter npm package name" field
5. Agree to the risks of using community nodes (if prompted)
6. Click "Install"

### Manual Installation

1. Open your n8n installation directory
2. Navigate to the `nodes` subdirectory
3. Run: `npm install n8n-nodes-longcat`
4. Restart your n8n instance

## Usage

1. Add the LongCat node to your workflow
2. Configure your LongCat API credentials
3. Select the operation (Chat)
4. Choose the model (LongCat-Flash-Chat or LongCat-Flash-Thinking)
5. Set up your system prompt and messages
6. Configure optional parameters
7. Execute the node

## Configuration

### API Credentials

1. Sign up at [LongCat Chat](https://longcat.chat/)
2. Generate an API key
3. In n8n, create a new credential of type 'LongCat API'
4. Enter your API key

### Node Parameters

- **Model**: LongCat-Flash-Chat or LongCat-Flash-Thinking
- **System Prompt**: Optional system message to set AI behavior
- **User Message**: The message to send to LongCat
- **Temperature**: Controls randomness (0.0 to 2.0)
- **Max Tokens**: Maximum tokens to generate (1-8192)
- **Enable Thinking**: Enable thinking mode (LongCat-Flash-Thinking only)
- **Thinking Budget**: Maximum thinking length (1024-4096)
- **AI Tool Mode**: Enable enhanced AI agent integration
- **Response Format**: Text or JSON output format

### AI Agent Integration Parameters

#### AI Tool Mode

When enabled, provides enhanced integration for AI agents:

```json
{
	"aiToolMode": true,
	"responseFormat": "json"
}
```

#### Response Metadata

AI agents receive enriched response data:

```json
{
	"content": "AI response content",
	"model": "LongCat-Flash-Chat",
	"usage": { "prompt_tokens": 10, "completion_tokens": 50 },
	"aiToolMode": true,
	"metadata": {
		"provider": "LongCat",
		"modelType": "LongCat-Flash-Chat",
		"hasThinking": false
	}
}
```

## Testing

### Manual Testing

1. Install dependencies: `npm install`
2. Build the project: `npm run build`
3. Install globally: `npm link` (for local testing)
4. In n8n, the LongCat node should appear in the node palette

### Test Workflow

```json
{
	"name": "LongCat Test Workflow",
	"nodes": [
		{
			"parameters": {},
			"name": "Start",
			"type": "n8n-nodes-base.start",
			"typeVersion": 1,
			"position": [240, 300]
		},
		{
			"parameters": {
				"model": "LongCat-Flash-Chat",
				"systemPrompt": "You are a helpful assistant.",
				"userMessage": "Hello! Please introduce yourself.",
				"options": {}
			},
			"name": "LongCat",
			"type": "n8n-nodes-longcat.longCat",
			"typeVersion": 1,
			"position": [460, 300],
			"credentials": {
				"longCatApi": {
					"id": "your-credential-id",
					"name": "LongCat API account"
				}
			}
		}
	],
	"connections": {
		"Start": {
			"main": [
				[
					{
						"node": "LongCat",
						"type": "main",
						"index": 0
					}
				]
			]
		}
	},
	"active": false,
	"settings": {},
	"id": "test-workflow"
}
```

### API Testing

To test the API directly without n8n:

```bash
curl -X POST https://api.longcat.chat/openai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "LongCat-Flash-Chat",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 1000
  }'
```

## 🤖 AI Agent Examples

### AI Agent Chat Completion

```json
{
	"model": "LongCat-Flash-Chat",
	"systemPrompt": "You are a helpful AI assistant specializing in data analysis.",
	"userMessage": "Analyze this data and provide insights: {{$json.data}}",
	"options": {
		"aiToolMode": true,
		"responseFormat": "json",
		"temperature": 0.3,
		"maxTokens": 2048
	}
}
```

### AI Agent with Thinking Model

```json
{
	"model": "LongCat-Flash-Thinking",
	"userMessage": "Solve this complex problem step by step: {{$json.problem}}",
	"options": {
		"aiToolMode": true,
		"enableThinking": true,
		"thinkingBudget": 2048,
		"temperature": 0.1,
		"maxTokens": 4096
	}
}
```

### MCP Integration Example

```json
{
	"name": "get_node_essentials",
	"arguments": {
		"nodeType": "n8n-nodes-longcat.longCat"
	}
}
```

## 🤖 AI Agent Compatibility

This node is fully compatible with AI agents and provides enhanced features for AI integration:

### Key AI Features

- **AI Tool Mode**: Structured responses optimized for AI processing
- **Multiple Response Formats**: Text and JSON output options
- **Enhanced Metadata**: Rich response data for AI agents
- **Thinking Model Support**: Advanced reasoning capabilities
- **MCP Integration**: Seamless integration with Model Context Protocol servers

### AI Agent Benefits

- **Predictable Output**: Structured responses for reliable parsing
- **Rich Context**: Detailed metadata for better decision making
- **Error Handling**: Comprehensive error reporting for AI agents
- **Flexible Integration**: Works with various AI agent frameworks

### MCP Server Integration

The node works seamlessly with n8n-mcp servers:

```bash
# AI agents can discover and use this node through MCP
npx n8n-mcp-server --help
```

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/OfficialMoAdel/n8n-nodes-longcat).

## License

MIT License

---

<div align="center">
  <p><strong>🤖 AI Agent Compatible</strong></p>
  <p>This node is optimized for AI agent integration with enhanced metadata and structured responses.</p>
</div>
