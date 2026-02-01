# n8n-nodes-gh-models

This is an n8n community node. It lets you use GitHub Models in your n8n workflows.

GitHub Models provides free access to popular AI models including OpenAI's GPT-4.1, GPT-4o, O1, O3, O4, and Text Embedding models through GitHub's API. This node simplifies the integration process, replacing complex HTTP request configurations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

**Chat Completions**

- Send messages to AI models and receive responses
- Support for conversation history with multiple roles (user, assistant, system)
- Configurable model parameters (temperature, top_p, max_tokens)
- Option to return full JSON response or simplified content

## Credentials

This node uses GitHub Personal Access Token for authentication. You need:

1. **GitHub Account**: Sign up at [github.com](https://github.com) if you don't have an account
2. **GitHub Models Access**: Ensure you have access to GitHub Models (currently in beta)
3. **Personal Access Token**: Generate a token with appropriate permissions

### Setting up GitHub Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select appropriate scopes for GitHub Models API access
4. Copy the generated token
5. In n8n, create new credentials using the "Github Models Credentials API" type
6. Paste your token in the "Github Token" field

## Compatibility

- **Minimum n8n version**: 0.187.0
- **Node.js**: 20.15.0 or higher
- **Tested with**: n8n 1.0.0+

## Usage

### Supported Models

The node supports these AI models from GitHub Models:

**OpenAI GPT Models:**

- `openai/gpt-4.1` - Latest GPT-4.1 with major improvements in coding and instruction following
- `openai/gpt-4.1-mini` - Efficient version outperforming GPT-4o-mini
- `openai/gpt-4.1-nano` - Lightweight version with lower latency and cost
- `openai/gpt-4o` - Advanced multimodal model supporting text and image inputs
- `openai/gpt-4o-mini` - Affordable and efficient model for diverse tasks

**Reasoning Models:**

- `openai/o1` - Advanced reasoning for complex problems including math and science
- `openai/o1-mini` - Smaller, faster, 80% cheaper than o1-preview
- `openai/o1-preview` - Preview version focused on advanced reasoning
- `openai/o3` - Improved quality and safety with o1 features
- `openai/o3-mini` - Cost-efficient version with high performance
- `openai/o4-mini` - Latest improvements with o3-mini features

**Embedding Models:**

- `openai/text-embedding-3-large` - Most capable large embedding model
- `openai/text-embedding-3-small` - Efficient small embedding model

### Basic Configuration

1. **Model Selection**: Choose from the dropdown list of available models
2. **Messages**: Configure conversation with:
   - **Prompt**: Your message content
   - **Role**: Select user, assistant, or system
3. **Options** (optional): Fine-tune model behavior:
   - **Temperature**: Controls randomness (0.0-2.0, default: 1.0)
   - **Top P**: Controls diversity (0.0-1.0, default: 1.0)
   - **Max Tokens**: Maximum response length (default: 1024)
4. **Output Format**: Choose between full JSON response or simplified content

### Configurations

**Simple Chat:**

```bash
Model: openai/gpt-4o
Messages:
  - Prompt: "Hello, can you help me with n8n workflows?"
  - Role: user
Output as JSON: false
```

**System Instructions:**

```bash
Model: openai/gpt-4.1
Messages:
  - Prompt: "You are a helpful assistant specialized in workflow automation."
  - Role: system
  - Prompt: "How can I automate email processing?"
  - Role: user
Options:
  - Temperature: 0.7
  - Max Tokens: 500
```

**Complex Reasoning:**

```bash
Model: openai/o1
Messages:
  - Prompt: "Solve this step by step: [complex problem]"
  - Role: user
Options:
  - Temperature: 0.3
  - Max Tokens: 2048
Output as JSON: true
```

### Response Formats

**Simplified Output** (Output as JSON: false):

```json
{
	"result": "The AI response content here..."
}
```

**Full JSON Output** (Output as JSON: true):

```json
{
	"id": "chatcmpl-...",
	"object": "chat.completion",
	"created": 1234567890,
	"model": "openai/gpt-4o",
	"choices": [
		{
			"index": 0,
			"message": {
				"role": "assistant",
				"content": "The AI response content here..."
			},
			"finish_reason": "stop"
		}
	],
	"usage": {
		"prompt_tokens": 10,
		"completion_tokens": 20,
		"total_tokens": 30
	}
}
```

### Best Practices

1. **Model Selection**:
   - Use GPT-4o for general tasks requiring multimodal capabilities
   - Use O1 models for complex reasoning and problem-solving
   - Use mini/nano variants for cost-effective operations

2. **Temperature Settings**:
   - Lower values (0.1-0.3) for factual, consistent responses
   - Higher values (0.7-1.0) for creative, varied responses

3. **Token Management**:
   - Monitor token usage to optimize costs
   - Set appropriate max_tokens limits

4. **Error Handling**:
   - Enable "Continue on Fail" for robust workflows
   - Handle rate limiting and authentication errors gracefully

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [GitHub Models documentation](https://docs.github.com/en/github-models)
- [Author's website](https://truonghaidang.com)
