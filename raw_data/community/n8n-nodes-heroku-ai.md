# n8n-nodes-heroku-ai

This is an n8n community node. It lets you use Heroku AI (Managed Inference and Agents) in your n8n workflows.

Heroku AI provides managed AI inference services with support for leading language models including Claude and other state-of-the-art models through a simple API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install via the n8n community nodes installation:

```bash
n8n-nodes-heroku-ai
```

## Operations

This node provides a **Heroku AI Chat Model** that can be used as a language model in n8n AI workflows:

- **Chat completions** with configurable parameters (temperature, max tokens, top-p, frequency penalty, presence penalty)
- **Model selection** from available Heroku AI models or custom model ID input
- **Streaming support** for real-time responses
- **Extended thinking mode** for more thorough analysis
- **Configurable timeouts** for API requests

## Credentials

To use this node, you need:

1. **Heroku AI API Key**: Your Heroku Managed Inference API key (INFERENCE_KEY)
2. **Base URL**: The Heroku AI API endpoint (defaults to `https://us.inference.heroku.com`)

### Setting up credentials

1. Sign up for Heroku AI services
2. Generate an Inference API key from your Heroku dashboard
3. In n8n, create new credentials for "Heroku AI API"
4. Enter your API key and base URL

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: >= 20.15
- **Tested with**: n8n 1.x

This node is compatible with all n8n AI workflow components including AI Agents, AI Chains, and other AI nodes.

## Usage

### Basic Setup

1. Add the **Heroku AI Chat Model** node to your workflow
2. Configure your Heroku AI API credentials
3. Select a model either:
   - **From List**: Choose from available models fetched from the API
   - **By ID**: Enter a custom model identifier (e.g., `claude-3-5-sonnet-latest`)
4. Adjust parameters like temperature, max tokens, etc. as needed
5. Connect to AI Agent, AI Chain, or other AI workflow nodes

### Model Selection

The node supports two ways to select models:

- **From List**: Automatically fetches and displays available chat models from Heroku AI
- **By ID**: Allows manual input of any model identifier

### Available Models

Commonly available models include:

- `claude-3-5-sonnet-latest`
- `claude-3-5-haiku`
- `claude-3-7-sonnet`
- `claude-4-sonnet`
- `gpt-oss-12b`
- `nova-lite`
- `nova-pro`

For a list of all available models, see the [Heroku AI Model Cards](https://devcenter.heroku.com/articles/heroku-inference-api-model-cards).

### Parameters

- **Temperature** (0-1): Controls randomness in responses
- **Maximum Tokens** (1-8192): Limits response length
- **Top P** (0-1): Nucleus sampling parameter
- **Frequency Penalty** (-2 to 2): Reduces repetition
- **Presence Penalty** (-2 to 2): Encourages new topics
- **Streaming**: Enable real-time response streaming
- **Extended Thinking**: Enable enhanced reasoning mode
- **Timeout**: Request timeout in milliseconds

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Heroku AI Documentation](https://devcenter.heroku.com/articles/heroku-inference-api-v1-chat-completions)
- [LangChain Integration](https://www.npmjs.com/package/heroku-langchain)
