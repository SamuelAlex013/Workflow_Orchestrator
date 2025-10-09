# n8n-nodes-rag

Advanced RAG (Retrieval-Augmented Generation) knowledge base nodes for n8n.

## Features

This package provides two powerful nodes for building RAG applications:

### 🗄️ RAG Knowledge Base Node
- **Text Processing**: Clean and preprocess text data with customizable options
- **Intelligent Chunking**: Multiple strategies (fixed size, sentence-based, paragraph-based)
- **Vector Embeddings**: Support for OpenAI, Hugging Face, and custom embedding providers
- **Flexible Storage**: Plugin interface for various vector databases (Qdrant, Milvus)
- **Operations**: Store, delete, and count documents

### 🔍 RAG Retrieval Node
- **Multiple Search Types**: Vector search, full-text search, and hybrid search
- **Configurable Results**: Customizable limits, score thresholds, and filtering
- **Metadata Support**: Include or exclude metadata in search results
- **AI-Ready Output**: Formatted results perfect for AI agent workflows

## Installation

```bash
npm install n8n-nodes-rag
```

## Supported Vector Databases

- **Qdrant**: Cloud and self-hosted vector database
- **Milvus**: Open-source vector database
- **Extensible**: Easy to add new vector store adapters

## Supported Embedding Providers

- **OpenAI**: text-embedding-ada-002 and other models
- **Hugging Face**: Wide range of open-source models
- **Custom API**: Bring your own embedding service

## Quick Start

### 1. Setup Vector Database
Start with Qdrant (easiest option):
```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 2. Create Knowledge Base
1. Add **RAG Knowledge Base** node to your workflow
2. Connect your text data source
3. Configure chunking strategy and embedding provider
4. Set vector database connection details
5. Execute to process and store your documents

### 3. Retrieve Information
1. Add **RAG Retrieval** node to your workflow
2. Configure the same vector database settings
3. Set your search query and parameters
4. Choose search type (vector, full-text, or hybrid)
5. Execute to get relevant results

## Configuration Examples

### Basic Text Processing
```json
{
  "operation": "store",
  "chunkingStrategy": "sentence",
  "chunkSize": 1000,
  "overlap": 200,
  "generateEmbeddings": true,
  "embeddingProvider": "openai"
}
```

### Vector Search
```json
{
  "searchType": "vector",
  "limit": 10,
  "threshold": 0.7,
  "includeMetadata": true
}
```

### Hybrid Search
```json
{
  "searchType": "hybrid",
  "limit": 10,
  "alpha": 0.5,
  "threshold": 0.6
}
```

## Use Cases

### 📚 Document Q&A Systems
Build intelligent document search and question-answering systems.

### 🤖 AI Agent Knowledge Base
Provide contextual information to AI agents and chatbots.

### 🔍 Semantic Search
Create powerful semantic search experiences for your applications.

### 📊 Content Analytics
Analyze and categorize large collections of text documents.

## Architecture

### Text Processing Pipeline
1. **Input Validation**: Ensure text data is properly formatted
2. **Text Cleaning**: Remove extra whitespace, normalize line breaks
3. **Chunking**: Split text using configurable strategies
4. **Embedding Generation**: Create vector representations
5. **Storage**: Save to vector database with metadata

### Search Pipeline
1. **Query Processing**: Generate embeddings for search queries
2. **Vector Search**: Find semantically similar content
3. **Full-text Search**: Keyword-based matching
4. **Hybrid Search**: Combine vector and full-text results
5. **Result Ranking**: Score and filter results

## Advanced Features

### Custom Metadata Filtering
Filter search results based on document metadata:
```json
{
  "source": "documentation",
  "category": "technical",
  "date": { "$gte": "2024-01-01" }
}
```

### Chunking Strategies
- **Fixed Size**: Split by character count with overlap
- **Sentence**: Respect sentence boundaries
- **Paragraph**: Maintain paragraph structure
- **Semantic**: AI-powered semantic chunking (future)

### Vector Store Adapters
Easily extend support for additional vector databases by implementing the `VectorStoreAdapter` interface.

## API Reference

### RAG Knowledge Base Node Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `operation` | string | Operation to perform (store/delete/count) |
| `inputField` | string | Field containing text data |
| `chunkingStrategy` | string | How to split text (fixed/sentence/paragraph) |
| `chunkSize` | number | Maximum chunk size in characters |
| `overlap` | number | Character overlap between chunks |
| `generateEmbeddings` | boolean | Whether to create vector embeddings |
| `embeddingProvider` | string | Embedding service (openai/huggingface/custom) |

### RAG Retrieval Node Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | string | Search query text |
| `searchType` | string | Search method (vector/fulltext/hybrid) |
| `limit` | number | Maximum results to return |
| `threshold` | number | Minimum similarity score |
| `includeMetadata` | boolean | Include document metadata |
| `metadataFilter` | string | JSON filter for metadata |

## Troubleshooting

### Common Issues

**Empty results from vector search**
- Check that embeddings were generated during storage
- Verify embedding provider settings match between store and search
- Adjust similarity threshold (try lower values like 0.5)

**API rate limits**
- Use batch processing for large documents
- Implement delays between API calls
- Consider using local embedding models

**Vector database connection errors**
- Verify endpoint URL and API key
- Check network connectivity
- Ensure collection/index exists

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE.md) for details.

## Support

- 📖 [Documentation](https://github.com/QixYuanmeng/n8n-nodes-rag/wiki)
- 🐛 [Issue Tracker](https://github.com/QixYuanmeng/n8n-nodes-rag/issues)
- 💬 [Discussions](https://github.com/QixYuanmeng/n8n-nodes-rag/discussions)

---

Built with ❤️ for the n8n community
