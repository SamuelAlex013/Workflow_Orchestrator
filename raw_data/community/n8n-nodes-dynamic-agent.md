# N8N Dynamic AI Agent Node

A flexible and powerful Dynamic AI Agent node for n8n that provides **maximum flexibility** in message configuration with JSON5 support and seamless tool integration.

## Features

### 🎯 **Mixed Message Types Support**
- **System messages**: Configure AI behavior and personality  
- **User messages**: Simulate user inputs and conversation context
- **Assistant messages**: Provide AI response examples and context
- Support for unlimited messages of any type combination
- Reorder messages with drag & drop functionality
- Enable/disable individual messages
- Label messages for better organization

### 📝 **Dual Configuration Modes**
- **Individual Mode**: Configure messages one by one with role selection
- **JSON Array Mode**: Bulk configuration using JSON format
- Easy switching between configuration approaches
- Import/export message configurations

### 📊 **Enhanced Token Usage Tracking**
- Detailed token consumption metrics for all message types
- Prompt vs completion token breakdown
- Cost estimation for popular models (GPT-3.5, GPT-4, etc.)
- Real-time usage monitoring
- Message-type breakdown in metadata

### ⚙️ **Advanced Configuration**
- Configurable max iterations
- Temperature control
- Streaming support
- Intermediate steps logging
- Timeout management

### 🚀 **AI Sub-Node Integration**
- **Chat Model Connection**: Connect any compatible AI language model
- **Memory Support**: Add conversation history and context retention
- **Tools Integration**: Extend capabilities with search, API, and file tools  
- **Output Parsing**: Structure responses with JSON, XML, or custom parsers
- **Fallback Mode**: Graceful degradation to mock responses when no AI connected
- **Real AI Processing**: Full integration with N8N's AI ecosystem

### 🚀 **Simplified Architecture**
- **Modular Design**: Connect only the AI components you need
- **No forced dependencies**: Works standalone or with full AI stack
- Optional sub-node support for memory, tools, and parsing
- Clean, focused interface with intelligent defaults

## Installation

1. Install the package in your n8n instance:
   ```bash
   npm install n8n-nodes-dynamic-agent
   ```

2. Restart your n8n instance

3. The "Custom AI Agent" node will appear in the AI section of your node palette

## Quick Start

1. **Install the package** in your n8n instance
2. **Choose Message Mode**:
   - **Individual**: Configure messages one by one with role selection
   - **JSON Array**: Use JSON format for bulk message configuration

3. **Configure Messages**:
   
   **Individual Mode:**
   - Add messages and select role (system/user/assistant)
   - Reorder messages with drag & drop
   - Use the toggle to enable/disable specific messages
   - Add labels for organization

   **JSON Array Mode:**
   - Enter messages in JSON format:
   ```json
   [
     {"role": "system", "content": "You are a helpful assistant"},
     {"role": "user", "content": "Hello"},
     {"role": "assistant", "content": "Hi there! How can I help?"}
   ]
   ```

4. **Set User Input**:
   - Enter your prompt directly or use expressions like `{{ $json.input }}`

5. **Configure Options** (optional):
   - Adjust max iterations (1-50)
   - Set temperature (0-2)
   - Enable/disable streaming
   - Toggle token usage tracking
   - Set timeout limits

## Configuration Guide

### Mixed Message Types

The node supports three message types that can be mixed in any combination:

**System Messages** - Define AI behavior:
```
"You are a helpful customer service assistant. Always be polite and professional."
```

**User Messages** - Provide conversation context:
```
"I'm having trouble with my order #12345"
```

**Assistant Messages** - Give response examples:
```
"I understand your concern. Let me look up your order details right away."
```

**Configuration Examples:**
- **Pure System**: Multiple system messages for complex behavior setup
- **Conversation Context**: Mix user/assistant messages to provide conversation history  
- **Training Examples**: Use assistant messages to show desired response patterns
- **Complex Scenarios**: Combine all three types for sophisticated AI interactions

### Message Configuration Modes

#### Individual Mode
Perfect for step-by-step configuration:
- Visual interface for each message
- Role dropdown selection
- Drag-and-drop reordering
- Individual enable/disable toggles
- Message labeling for organization

#### JSON Array Mode  
Ideal for bulk configuration and programmatic setup:
- Import message arrays from external sources
- Copy/paste configurations between workflows
- Easy backup and version control
- Programmatic message generation

**Best Practices:**
- Start with system messages to establish AI personality
- Add conversation context with user/assistant message pairs
- Use clear, specific language in all message types
- Test different message combinations to optimize results
- Keep related messages grouped together

### Options

| Option | Description | Default | Range |
|--------|-------------|---------|-------|
| Max Iterations | Maximum number of agent iterations | 10 | 1-50 |
| Temperature | Response randomness (0=deterministic, 2=creative) | 0.7 | 0-2 |
| Enable Streaming | Stream responses in real-time | true | boolean |
| Include Token Usage | Track and return token consumption | true | boolean |
| Return Intermediate Steps | Include processing steps in output | false | boolean |
| Timeout | Maximum execution time in seconds | 60 | 10-300 |

## Output Format

The node returns a comprehensive response object:

```json
{
  "response": "AI agent response text",
  "tokenUsage": {
    "prompt": 150,
    "completion": 75,
    "total": 225,
    "estimatedCost": 0.001125
  },
  "metadata": {
    "executionTime": 1250,
    "model": "custom-agent-v1.0",
    "systemMessagesCount": 3,
    "timestamp": "2024-01-15T10:30:00.000Z",
    "nodeVersion": "1.0"
  },
  "intermediateSteps": [
    {
      "step": 1,
      "action": "Process system messages",
      "result": "Processed 3 system messages"
    }
  ]
}
```

## Examples

### Basic Chat Agent
```
System Message 1: "You are a friendly customer service agent."
User Input: "Hello, I need help with my order."
```

### Code Assistant
```
System Message 1: "You are an expert programmer."
System Message 2: "Always provide code examples when relevant."
System Message 3: "Explain your solutions step by step."
User Input: "How do I create a REST API in Node.js?"
```

### Creative Writing Helper
```
System Message 1: "You are a creative writing assistant."
System Message 2: "Focus on vivid descriptions and engaging narratives."
System Message 3: "Always ask follow-up questions to understand the writer's vision."
User Input: "Help me write a story about a time traveler."
```

## Use Cases

- **Customer Service Bots**: Multiple system messages for different service scenarios
- **Code Assistants**: Specialized system messages for different programming languages
- **Content Generation**: Context-specific guidelines for different content types
- **Educational Tools**: Adaptive system messages based on learning level
- **Creative Projects**: Dynamic personality and style adjustments

## Troubleshooting

### Common Issues

**Node doesn't appear in palette:**
- Ensure package is installed correctly
- Restart n8n after installation
- Check n8n logs for errors

**Token usage not showing:**
- Enable "Include Token Usage" in options
- Verify the model supports token tracking

**Responses are too short/long:**
- Adjust system messages to be more specific about response length
- Modify the temperature setting
- Check max iterations setting

**Performance issues:**
- Reduce max iterations for faster responses
- Set appropriate timeout values
- Consider disabling intermediate steps for production use

### Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/lauchacarro/n8n-nodes-dynamic-agent/issues)
- **Documentation**: [Full documentation and examples](https://github.com/lauchacarro/n8n-nodes-dynamic-agent)
- **Community**: Join the n8n community for discussions and help

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0
- Initial release
- Dynamic system messages with drag & drop reordering
- Comprehensive token usage tracking
- Advanced configuration options
- Simplified architecture without memory dependency
