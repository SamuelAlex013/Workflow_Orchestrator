# AI Token Tracking Node for N8N

## 🚀 Overview

A powerful N8N custom node that provides comprehensive AI token usage tracking and monitoring capabilities with sub-workflow execution support. This middleware node sits between your workflow and AI language models to provide detailed insights into token consumption, costs, and usage patterns.

## ✨ Features

### 🔍 Token Tracking
- **Real-time Token Monitoring**: Track input and output tokens for all AI model calls
- **Cost Calculation**: Automatic cost calculation based on configurable pricing per token
- **Multi-Model Support**: Compatible with GPT, Claude, Gemini, and other LangChain models
- **Usage Analytics**: Session-based tracking with historical data

### 🔄 Sub-Workflow Execution
- **Flexible Triggers**: Execute workflows on every call, token thresholds, or time intervals
- **Data Passing**: Complete tracking data passed to sub-workflows
- **Execution Modes**: Run once with all data or individually per item
- **Async/Sync Options**: Choose to wait for completion or continue immediately

### ⚙️ Configuration Options
- **Pricing Configuration**: Set custom prices per input/output token
- **Storage Options**: Memory or workflow data persistence
- **Threshold Alerts**: Execute actions when token limits are reached
- **Currency Support**: Multi-currency cost calculations

## 📦 Installation

### NPM Package
```bash
npm install @custom/n8n-nodes-ai-token-tracking
```

### Manual Installation
1. Clone this repository
2. Run `npm install` to install dependencies
3. Run `npm run build` to compile the TypeScript code
4. Install the package in your N8N instance

## 🏗️ Architecture

```
Input Data → AI Token Tracking Node → AI Model → Output Data + Tracking Metadata
                    ↓
            Sub-Workflow (Optional)
```

## 🔧 Usage

### Basic Setup

1. **Add the Node**: Drag the "AI Token Tracking" node into your workflow
2. **Connect Inputs**: 
   - Connect your data to the "Main Input"
   - Connect an AI Language Model to the "AI Model" input
3. **Configure Tracking**: Set up token tracking preferences
4. **Connect Outputs**: Use both outputs - main data flow and AI model passthrough

### Configuration Example

```typescript
// Tracking Configuration
{
  enableInputTokens: true,
  enableOutputTokens: true,
}

// Sub-Workflow Configuration  
{
  enabled: true,
  workflowId: "workflow-123",
  trigger: "always", // always/threshold/interval
  mode: "once",      // once/each
  waitForCompletion: true
}
```

## 📊 Output Data

The node adds comprehensive tracking metadata:

```json
{
  "originalData": "...",
  "_aiTokenTracking": {
    "sessionId": "workflow-node-123456-abc",
    "trackingEnabled": true,
    "timestamp": "2025-08-20T10:47:00.000Z",
    "usage": {
      "inputTokens": 150,
      "outputTokens": 75,
      "totalTokens": 225,
      "estimatedCost": 0.000375,
      "modelName": "gpt-4"
    }
  }
}
```

## 🔬 Testing

```bash
npm test                 # Run all tests
npm run test:watch      # Run tests in watch mode
npm run test:coverage   # Run tests with coverage
```

## 🛠️ Development

```bash
npm install     # Install dependencies
npm run dev     # Development mode with auto-reload
npm run build   # Build for production
npm run lint    # Run linting
```

## 📈 Performance

- **Overhead**: < 50ms per AI model call
- **Memory**: Efficient with configurable history limits
- **Scalability**: Handles concurrent executions
- **Reliability**: Robust error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE.md](LICENSE.md) for details

## 🆘 Support

- [GitHub Issues](https://github.com/custom/n8n-nodes-ai-token-tracking/issues)
- [Documentation](docs/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/n8n-ai-token-tracking)

---

**Made with ❤️ for the N8N community**
