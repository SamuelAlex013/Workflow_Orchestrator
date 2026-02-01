# n8n-nodes-cloudflare-vectorize

A comprehensive n8n community node for [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/), enabling vector database operations for semantic search, embeddings management, and RAG (Retrieval-Augmented Generation) applications.

[![npm version](https://badge.fury.io/js/n8n-nodes-cloudflare-vectorize.svg)](https://badge.fury.io/js/n8n-nodes-cloudflare-vectorize)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🚀 **Complete Vector Operations**: Insert, upsert, query, delete vectors
- 🔍 **Advanced Search**: Semantic similarity search with configurable parameters
- 📊 **Index Management**: Create, configure, and manage vector indexes
- 🏷️ **Metadata Support**: Rich metadata filtering and indexing
- 🎯 **AI Agent Ready**: Optimized for use with n8n AI Agent and MCP Trigger
- 📝 **Namespace Support**: Organize vectors with namespace segmentation
- ⚡ **Batch Operations**: Efficient bulk vector processing
- 🛠️ **Developer Friendly**: Full TypeScript support with comprehensive types

## Installation

### From n8n Community Nodes (Recommended)

1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter: `n8n-nodes-cloudflare-vectorize`
4. Click **Install**

### Manual Installation

```bash
# In your n8n installation directory
npm install n8n-nodes-cloudflare-vectorize

# Restart n8n
```

## Quick Start

### 1. Set up Cloudflare Vectorize

1. Create a [Cloudflare account](https://www.cloudflare.com/)
2. Create a vector index using Wrangler CLI:
   ```bash
   npx wrangler vectorize create my-index --dimensions=1536 --metric=cosine
   ```
3. Get your Account ID from the Cloudflare dashboard
4. Create an API token with Vectorize permissions

### 2. Configure Credentials in n8n

1. Add new credentials: **Cloudflare Vectorize API**
2. Enter your:
   - **Account ID**: Found in your Cloudflare dashboard
   - **API Token**: Created with Vectorize read/write permissions
   - **API Endpoint**: Leave default unless using custom endpoint

### 3. Use in Workflows

Add the **Cloudflare Vectorize** node to your workflow and select from these resources:

- **Index**: Manage vector indexes
- **Vector**: Insert, query, and manage vectors
- **Metadata**: Configure metadata indexes for filtering
- **Utility**: List vectors and get index information

## Usage Examples

### Insert Vectors

```json
{
  "resource": "vector",
  "operation": "insert",
  "indexName": "my-embeddings",
  "vectors": [
    {
      "id": "doc1",
      "values": [0.1, 0.2, 0.3, ...],
      "metadata": {
        "title": "Document 1",
        "category": "tech"
      }
    }
  ]
}
```

### Query Similar Vectors

```json
{
  "resource": "vector",
  "operation": "query",
  "indexName": "my-embeddings",
  "queryVector": [0.1, 0.2, 0.3, ...],
  "topK": 5,
  "returnValues": true,
  "returnMetadata": "all"
}
```

### Create Index

```json
{
  "resource": "index",
  "operation": "create",
  "indexName": "new-index",
  "dimensions": 1536,
  "metric": "cosine",
  "description": "Embeddings for documents"
}
```

## AI Agent Integration

This node is optimized for use with n8n's AI Agent and MCP Trigger:

```json
{
  "tool": "cloudflare-vectorize",
  "operation": "query-similar-vectors",
  "parameters": {
    "query": "Find documents about machine learning",
    "index": "knowledge-base",
    "limit": 3
  }
}
```

## Operations Reference

### Index Resource

| Operation | Description |
|-----------|-------------|
| `create` | Create a new vector index |
| `list` | List all available indexes |
| `delete` | Delete an index |
| `get` | Get index details |
| `info` | Get index statistics |

### Vector Resource

| Operation | Description |
|-----------|-------------|
| `insert` | Insert new vectors (fails if ID exists) |
| `upsert` | Insert or update vectors |
| `query` | Search vectors by similarity |
| `queryById` | Query using existing vector |
| `getByIds` | Retrieve specific vectors |
| `deleteByIds` | Delete vectors by ID |

### Metadata Resource

| Operation | Description |
|-----------|-------------|
| `createIndex` | Enable metadata filtering |
| `deleteIndex` | Remove metadata index |
| `listIndexes` | List metadata indexes |

### Utility Resource

| Operation | Description |
|-----------|-------------|
| `listVectors` | List all vector IDs |
| `describe` | Get index configuration |

## Configuration

### Vector Formats

Vectors can be provided as:
- Array of numbers: `[1.0, 2.0, 3.0]`
- Float32Array or Float64Array
- n8n expressions: `{{ $json.embedding }}`

### Distance Metrics

- **cosine**: Cosine similarity (recommended for most use cases)
- **euclidean**: Euclidean distance
- **dot-product**: Dot product similarity

### Metadata Filtering

Create metadata indexes to enable filtering:

```json
{
  "resource": "metadata",
  "operation": "createIndex",
  "indexName": "my-index",
  "propertyName": "category",
  "type": "string"
}
```

Then use in queries:

```json
{
  "resource": "vector",
  "operation": "query",
  "filter": {
    "category": "technology"
  }
}
```

## Error Handling

The node provides detailed error messages for common issues:

- **Authentication errors**: Check API token permissions
- **Index not found**: Verify index name and existence
- **Dimension mismatches**: Ensure vector dimensions match index
- **Rate limiting**: Automatic retry with exponential backoff
- **Network errors**: Configurable retry logic

## Limits

Cloudflare Vectorize has the following limits:

- **Vectors per request**: Up to 1,000 for inserts/upserts
- **Query topK**: Up to 100 (20 with returnValues/returnMetadata)
- **Metadata indexes**: Up to 10 per index
- **Vector dimensions**: Up to 1536
- **Namespace length**: Up to 64 characters
- **Metadata size**: Up to 10KB per vector

## Development

### Building from Source

```bash
git clone https://github.com/jezweb/n8n-nodes-cloudflare-vectorize.git
cd n8n-nodes-cloudflare-vectorize
npm install
npm run build
```

### Testing Locally

```bash
# Link to local n8n
npm link
cd ~/.n8n/custom
npm link n8n-nodes-cloudflare-vectorize

# Restart n8n
```

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) and submit issues and pull requests on GitHub.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- 📖 [Cloudflare Vectorize Documentation](https://developers.cloudflare.com/vectorize/)
- 🐛 [Report Issues](https://github.com/jezweb/n8n-nodes-cloudflare-vectorize/issues)
- 💬 [n8n Community](https://community.n8n.io/)
- 📧 [Email Support](mailto:jeremy@jezweb.net)

## Related

- [n8n-nodes-cloudflare-d1](https://github.com/jezweb/n8n-nodes-cloudflare-d1) - Cloudflare D1 database integration
- [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/) - Official documentation
- [n8n](https://n8n.io/) - Workflow automation platform