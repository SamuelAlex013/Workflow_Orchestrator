# n8n-nodes-solar

Solar LLM and Embeddings nodes for n8n, powered by Upstage Solar models.

![Solar Node](https://img.shields.io/npm/v/n8n-nodes-solar)
![License](https://img.shields.io/npm/l/n8n-nodes-solar)

## Description

This package provides n8n community nodes for integrating with Upstage's Solar LLM and embedding models. Solar is a series of large language models that deliver exceptional performance with efficiency.

## Features

- **Solar Chat Model**: Use Solar LLM for chat completions with support for multiple models (solar-mini, solar-pro, solar-pro2)
- **Solar Embeddings**: Generate high-quality embeddings using Solar embedding models
- **Easy Authentication**: Simple API key-based authentication
- **Multiple Input Types**: Support for single text or batch processing
- **Comprehensive Options**: Temperature, max tokens, top-p, and more

## Installation

### Prerequisites

- n8n version 1.0.0 or later
- Node.js 18.0.0 or later

### Install via n8n Community Nodes

1. **Enable Community Nodes** (if not already enabled):
   ```bash
   export N8N_COMMUNITY_NODES_ENABLED=true
   n8n start
   ```

2. **Install via n8n UI**:
   - Go to **Settings** → **Community Nodes**
   - Click **Install a community node**
   - Enter: `n8n-nodes-solar`
   - Click **Install**

3. **Install via npm** (alternative):
   ```bash
   npm install n8n-nodes-solar
   ```

## Setup

### 1. Get API Key

1. Sign up at [Upstage Console](https://console.upstage.ai/)
2. Navigate to API Keys section
3. Create a new API key

### 2. Configure Credentials

1. In n8n, go to **Credentials** → **Create New**
2. Search for **"Upstage API"**
3. Enter your API key
4. Test and save

## Available Nodes

### Solar Chat Model

Use Solar LLM models for chat completions.

**Supported Models:**
- `solar-mini` - Fast and efficient for basic tasks
- `solar-pro` - Powerful model for complex tasks
- `solar-pro2` - Latest and most advanced Solar model

**Key Features:**
- Message-based conversation format
- Configurable temperature, max tokens, top-p
- Support for system, user, and assistant roles
- Streaming response option

### Embeddings Upstage

Generate high-quality embeddings using Solar embedding models.

**Supported Models:**
- `embedding-query` - Optimized for search queries and questions
- `embedding-passage` - Optimized for documents and passages

**Key Features:**
- Single text or batch processing
- Input from node parameters or previous node data
- High-dimensional vector outputs

## Usage Examples

### Simple Chat Completion

1. Add **Solar Chat Model** node
2. Configure with your Upstage API credentials
3. Set model to `solar-mini`
4. Add a message with role "user" and your prompt
5. Execute to get AI response

### Text Embeddings

1. Add **Embeddings Upstage** node
2. Configure credentials
3. Choose appropriate model (query vs passage)
4. Input your text
5. Get embedding vectors for similarity search, clustering, etc.

### Batch Processing

Use the **Embeddings Upstage** node with "Array of Texts" input type to process multiple texts efficiently in a single API call.

## API Reference

### Solar Chat API
- Endpoint: `https://api.upstage.ai/v1/solar/chat/completions`
- Documentation: [Upstage Chat API](https://developers.upstage.ai/docs/apis/chat)

### Solar Embeddings API
- Endpoint: `https://api.upstage.ai/v1/embeddings`
- Documentation: [Upstage Embeddings API](https://console.upstage.ai/docs/capabilities/embeddings)

## Troubleshooting

### Node Not Visible
1. Check if community nodes are enabled
2. Restart n8n completely
3. Clear browser cache
4. Check n8n logs for installation errors

### API Errors
1. Verify API key is correct and active
2. Check network connectivity
3. Review Upstage API documentation for rate limits
4. Check model availability

### Build Errors (for developers)
1. Ensure TypeScript is installed: `npm install -g typescript`
2. Check Node.js version compatibility
3. Clear node_modules and reinstall: `rm -rf node_modules && npm install`

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

MIT License - see LICENSE file for details.

## Links

- [Upstage Console](https://console.upstage.ai/)
- [Solar LLM Documentation](https://developers.upstage.ai/docs/apis/chat)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [GitHub Repository](https://github.com/UpstageAI/n8n-nodes-solar)
