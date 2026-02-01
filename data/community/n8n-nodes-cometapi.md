# n8n-nodes-cometapi

This is an n8n community node. It lets you use CometAPI in your n8n workflows.

CometAPI is a powerful AI language model service that provides OpenAI-compatible API endpoints for various large language models, enabling developers to integrate advanced AI capabilities into their applications.

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

The CometAPI node supports chat completions using various AI language models:

### Chat Completions
- **Model Selection**: Choose from available models (default: gpt-4o-mini)
- **Message Management**: Support for multi-turn conversations with user, assistant, and system roles
- **Advanced Parameters**:
  - **Temperature**: Control randomness (0-2, default: 0.7)
  - **Max Tokens**: Set maximum response length (up to 32,768 tokens)
  - **Top P**: Control diversity via nucleus sampling (0-1, default: 1)
  - **Frequency Penalty**: Reduce repetition (-2 to 2, default: 0)
  - **Presence Penalty**: Encourage new topics (-2 to 2, default: 0)
  - **Stream**: Enable streaming responses (default: false)

## Credentials

To use this node, you need to authenticate with CometAPI:

1. Sign up for a CometAPI account at [CometAPI Console](https://api.cometapi.com/console/token)
2. Generate an API key from your console dashboard
3. In n8n, create new CometAPI credentials and enter your API key

### Authentication Method
- **API Key**: Bearer token authentication using your CometAPI API key

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: 20.15 or higher
- **Tested with**: Latest stable versions of n8n

This node is compatible with all n8n deployment methods including:
- Self-hosted n8n instances
- n8n Cloud
- Docker deployments

## Usage

### Basic Chat Completion

1. Add the CometAPI node to your workflow
2. Configure your CometAPI credentials
3. Set up your messages:
   - **System message**: Define the AI's behavior (optional)
   - **User message**: Your prompt or question
4. Choose your preferred model (e.g., gpt-4o-mini)
5. Execute the workflow

### Example Use Cases

- **Content Generation**: Create articles, summaries, or creative content
- **Data Analysis**: Analyze and interpret data with AI assistance
- **Customer Support**: Build intelligent chatbots and support systems
- **Code Review**: Get AI feedback on code quality and suggestions
- **Translation**: Translate text between different languages

### Advanced Configuration

For more control over the AI responses, you can adjust:
- **Temperature**: Lower values (0.1-0.3) for more focused responses, higher values (0.7-1.0) for more creative outputs
- **Max Tokens**: Limit response length to control costs and response time
- **Frequency/Presence Penalty**: Fine-tune repetition and topic diversity

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [CometAPI Documentation](https://api.cometapi.com/docs)
* [CometAPI Console](https://api.cometapi.com/console/token)

## License

[MIT](https://github.com/cometapi-dev/n8n-nodes-cometapi/blob/master/LICENSE.md)
