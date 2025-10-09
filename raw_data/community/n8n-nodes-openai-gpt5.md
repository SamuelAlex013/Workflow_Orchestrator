# n8n-nodes-openai-gpt5

This is an n8n community node that provides access to OpenAI's GPT-5 models and advanced features through the Responses API. It supports PDF processing, multiple file inputs, and all the latest GPT-5 capabilities including reasoning effort control, verbosity settings, and reasoning summaries. **Now with AI Agent Tool support!**

## Features

- 🚀 **Full GPT-5 Support**: Access GPT-5, GPT-5 Mini, GPT-5 Nano models
- 📄 **PDF Processing**: Upload and process PDF files directly
- 🎯 **Reasoning Control**: Fine-tune reasoning effort (minimal, low, medium, high)
- 📝 **Verbosity Control**: Adjust output length (low, medium, high)
- 🧠 **Reasoning Summaries**: Get insights into the model's thinking process
- 🔗 **Multiple File Support**: Process multiple PDFs and images in one request
- ⚡ **O-Series Models**: Support for O3, O3 Pro, O3 Mini, O4 Mini models
- 🤖 **AI Agent Tool**: Use as a tool with n8n AI Agent nodes

## Installation

### In n8n

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-openai-gpt5`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-openai-gpt5
```

Then restart your n8n instance.

## Setup

1. **Get OpenAI API Key**:
   - Sign up at [OpenAI Platform](https://platform.openai.com)
   - Generate an API key from your account settings

2. **Configure Credentials in n8n**:
   - Go to **Credentials** > **New**
   - Select **OpenAI GPT-5 API**
   - Enter your API key
   - (Optional) Add Organization ID if you have one
   - Save the credentials

## Usage

### Using as an AI Agent Tool

This node can be used as a tool with n8n's AI Agent nodes, allowing AI agents to leverage GPT-5's advanced reasoning capabilities:

1. **Enable Community Tools** (if needed):
   - Set environment variable: `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true`
   
2. **Connect to AI Agent**:
   - Add an AI Agent node to your workflow
   - Add this OpenAI GPT-5 node
   - Connect the GPT-5 node to the AI Agent's tool input
   
3. **AI Tool Mode**:
   - The node includes a special "AI Tool Mode" operation
   - Simplified interface optimized for AI agent usage
   - Automatically handles file processing if needed
   
4. **Example Use Cases**:
   - Document analysis and summarization
   - Complex reasoning tasks
   - PDF content extraction and Q&A
   - Multi-modal analysis (text + images)

### Basic PDF Processing

1. Add the **OpenAI GPT-5** node to your workflow
2. Select **Upload & Process PDF** operation
3. Choose input type:
   - **Binary Data**: Use files from previous nodes
   - **File URL**: Direct download from URL
   - **File Path**: Server file path
4. Enter your prompt
5. Configure additional options as needed

### Process with File ID

If you've already uploaded a file and have its ID:
1. Select **Process with File ID** operation
2. Enter the file ID
3. Provide your prompt

## Node Options

### Models
- **GPT-5**: Most capable model
- **GPT-5 Mini**: Smaller, faster variant
- **GPT-5 Nano**: Smallest, fastest variant
- **GPT-4.1**: Previous generation model
- **O3**: Advanced reasoning model
- **O3 Pro**: Enhanced O3 with better reasoning
- **O3 Mini**: Smaller O3 variant
- **O4 Mini**: Latest mini reasoning model

### Reasoning Effort (GPT-5 & O-Series)
- **Minimal**: Fastest responses with minimal reasoning (GPT-5 only)
- **Low**: Lower reasoning effort for faster responses
- **Medium**: Balanced reasoning and speed (default)
- **High**: Maximum reasoning capability

### Verbosity (GPT-5 only)
- **Low**: Most concise output
- **Medium**: Balanced verbosity
- **High**: More detailed output

### Reasoning Summary
- **None**: No reasoning summary
- **Auto**: Automatic summary generation
- **Detailed**: Detailed reasoning summary

Note: Reasoning summaries are not guaranteed for every request.

### Additional Options
- **Max Tokens**: Control output length (default: 4096)
- **Temperature**: Control randomness (0-2, default: 0.7)
- **Additional Files**: Include multiple files in the request
- **Purpose**: Specify file upload purpose (default: "user_data")

## Example Workflows

### 1. PDF Analysis
```
[Read Binary File] → [OpenAI GPT-5: Analyze PDF] → [Output]
```

### 2. Multiple Document Processing
```
[HTTP Request: Get PDFs] → [OpenAI GPT-5: Process with Additional Files] → [Save Results]
```

### 3. High-Reasoning Analysis
```
[Input Data] → [OpenAI GPT-5: High Reasoning + Low Verbosity] → [Slack Message]
```

## API Structure

The node uses OpenAI's Responses API (`/v1/responses`) with the following structure:

### GPT-5 Models
```json
{
  "model": "gpt-5",
  "input": [...],
  "reasoning": {
    "effort": "medium",
    "summary": "auto"
  },
  "text": {
    "verbosity": "medium"
  }
}
```

### O-Series Models
```json
{
  "model": "o3",
  "input": [...],
  "reasoning_effort": "medium"
}
```

## Performance Guidelines

| Reasoning Effort | Response Time | Use Case |
|-----------------|---------------|----------|
| Minimal | ~3-4s | Quick answers, simple queries |
| Low | ~3-5s | Standard queries with basic reasoning |
| Medium | ~5-10s | Balanced performance and quality |
| High | ~15-50s | Complex analysis, critical decisions |

## Limitations

- **Not Supported**: Temperature control for reasoning models, image generation with O3 Pro
- **Reasoning Summaries**: Not guaranteed for every request
- **Token Limits**: Subject to your OpenAI plan limits
- **File Size**: PDF uploads subject to OpenAI file size limits

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development

```bash
# Install dependencies
npm install

# Build the node
npm run build

# Run tests
OPENAI_API_KEY=your-key npm test

# Lint code
npm run lint
```

## Support

- **Issues**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-openai-gpt5/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jezweb/n8n-nodes-openai-gpt5/discussions)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io)

## License

MIT - See [LICENSE](LICENSE) file for details

## Author

**Jez** - [Jezweb](https://www.jezweb.com.au)

## Changelog

### v0.4.0 (2025-01-10)
- Added AI Agent Tool support with `usableAsTool` property
- New "AI Tool Mode" operation for simplified AI agent usage
- Added codex metadata for better tool discovery
- Enhanced documentation for AI agent integration
- Automatic file handling in AI Tool Mode

### v0.3.2 (2025-01-10)
- Temperature parameter now excluded for GPT-5 models (not supported by reasoning models)
- Updated temperature description to clarify it's not supported by GPT-5
- Reordered options alphabetically for better maintainability

### v0.3.1 (2025-01-10)
- Fixed response extraction for simplified output
- Improved input structure for text-only requests
- Enhanced error handling with detailed messages
- Fixed response parsing for GPT-5 output structure
- Removed preamble option (only for tool-calling scenarios)

### v0.3.0 (2025-01-10)
- Added verbosity control for GPT-5 models
- Added reasoning summary support
- Enhanced reasoning effort with all levels
- Initial error handling improvements

### v0.2.2 (2025-01-09)
- Initial public release
- PDF processing support
- Multiple file inputs
- Basic reasoning effort control

## Acknowledgments

- Built for the [n8n](https://n8n.io) workflow automation platform
- Uses [OpenAI API](https://platform.openai.com) for AI capabilities
- Community feedback and contributions