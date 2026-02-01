# n8n-nodes-cloudflare-autorag

This is an n8n community node that lets you use [Cloudflare AutoRAG](https://developers.cloudflare.com/autorag/) in your n8n workflows.

Cloudflare AutoRAG is a managed service for creating Retrieval-Augmented Generation (RAG) applications. It allows you to query your knowledge bases with AI-powered search, retrieving relevant information from your indexed data and generating context-aware responses.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

### Community Node (Recommended)

1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Select **Install**
3. Enter `n8n-nodes-cloudflare-autorag` in the npm Package Name field
4. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-cloudflare-autorag
```

## Operations

This node supports two operations:

- **AI Search**: Search your knowledge base and generate an AI response with retrieved context
- **Search**: Perform semantic search to retrieve raw document chunks without AI generation

## Authentication

You'll need to create credentials in n8n using:

1. **Account ID**: Your Cloudflare Account ID (found in dashboard URL or sidebar)
2. **API Token**: A Cloudflare API token with AutoRAG Read and Edit permissions

### Creating an API Token

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com)
2. Navigate to **AI > AutoRAG**
3. Select your AutoRAG instance
4. Click **Use AutoRAG** > **API**
5. Select **Create an API Token**
6. Copy and save the token securely

## Node Reference

### Input Fields

- **Operation**: Choose between AI Search or Search
- **AutoRAG Name**: The unique name of your AutoRAG instance
- **Query**: The question or search query for your knowledge base

### Additional Options

- **Model** (AI Search only): Override the default text generation model
- **Rewrite Query**: Optimize the query for better semantic search
- **Result Limit**: Maximum number of document chunks (1-50)
- **Minimum Score**: Minimum similarity score for results (0.0-1.0)

## AI Agent Tool Usage

This node is **AI Agent compatible** (`usableAsTool: true`). You can connect it to AI Agent nodes in n8n, allowing the AI to autonomously query your knowledge bases when needed to answer user questions.

### Example AI Agent Setup

1. Add an AI Agent node to your workflow
2. Connect the Cloudflare AutoRAG node to the Agent's tool input
3. The AI will automatically use your knowledge base when relevant

## Example Usage

### Simple Query Workflow

```json
{
  "nodes": [
    {
      "name": "Cloudflare AutoRAG",
      "type": "n8n-nodes-cloudflare-autorag.cloudflareAutoRag",
      "parameters": {
        "operation": "aiSearch",
        "autoRagName": "my-knowledge-base",
        "query": "How do I configure authentication?",
        "additionalOptions": {
          "limit": 5,
          "rewriteQuery": true
        }
      }
    }
  ]
}
```

### Output Structure

The node returns:

```json
{
  "answer": "The generated AI response...",
  "sources": [
    {
      "id": "doc-chunk-id",
      "score": 0.89,
      "text": "The relevant text content...",
      "metadata": {
        "source": "r2://bucket/document.pdf"
      }
    }
  ],
  "query": "Your original query",
  "rewritten_query": "The optimized query (if enabled)"
}
```

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Cloudflare AutoRAG documentation](https://developers.cloudflare.com/autorag/)
- [AutoRAG API Reference](https://developers.cloudflare.com/autorag/usage/rest-api/)

## License

[MIT](https://github.com/jezweb/n8n-nodes-cloudflare-autorag/blob/master/LICENSE.md)

## Support

For issues and feature requests, please use the [GitHub issues page](https://github.com/jezweb/n8n-nodes-cloudflare-autorag/issues).

## Author

Jeremy Dawes - [Jezweb](https://www.jezweb.com.au)