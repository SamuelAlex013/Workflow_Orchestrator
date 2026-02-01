# n8n-nodes-qwen-embedding

[![NPM Version](https://img.shields.io/npm/v/n8n-nodes-qwen-embedding)](https://www.npmjs.com/package/n8n-nodes-qwen-embedding)
[![License](https://img.shields.io/npm/l/n8n-nodes-qwen-embedding)](https://github.com/theseedship/deposium_n8n_embeddings_integration/blob/master/LICENSE)
[![n8n Community](https://img.shields.io/badge/n8n-community_node-orange)](https://n8n.io/integrations)

n8n community nodes for integrating Qwen embeddings via Ollama with your n8n workflows. Generate high-quality text embeddings using Ollama-hosted Qwen models for vector stores, similarity search, and AI applications.

## 🌟 Features

- **Two Specialized Nodes**:
  - **Qwen Embedding**: For vector store integration (Supabase, Qdrant, PGVector, etc.)
  - **Qwen Embedding Tool**: For direct embedding generation in workflows
- **LangChain Compatible**: Seamlessly integrates with n8n's AI ecosystem
- **Flexible Dimensions**: Support for 32-1024 dimensions via MRL (Matryoshka Representation Learning)
- **Instruction-Aware**: Optimized embeddings for queries vs documents
- **Batch Processing**: Efficient bulk embedding generation
- **Ollama Integration**: Direct connection to Ollama for embedding generation
- **No Middleware Required**: Works directly with Ollama's API endpoints

## 📦 Installation

### In n8n

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-qwen-embedding`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-qwen-embedding
```

## 🚀 Prerequisites

You need to have Ollama installed and running with a Qwen model:

1. **Install Ollama**: Visit [https://ollama.com](https://ollama.com) for installation instructions

2. **Pull a Qwen embedding model**:
```bash
# Qwen3-Embedding models (specialized for embeddings):
ollama pull qwen3-embedding:0.6b  # Recommended - 1024 dimensions
ollama pull qwen3-embedding:latest

# Note: Use qwen3-embedding models for best embedding quality
# Generic qwen2.5 models can also generate embeddings but are optimized for chat
```

3. **Verify Ollama is running**:
```bash
ollama list  # Should show your pulled models
```

Ollama will be available at `http://localhost:11434` by default

## 🔧 Setup

### ⚠️ CRITICAL: Ollama URL Configuration

**ALWAYS remove trailing slashes from your Ollama URL!**

```
✅ CORRECT:   http://localhost:11434
❌ WRONG:     http://localhost:11434/
```

**Why this matters:** A trailing slash creates a double-slash in the API path (`http://host:11434//api/embed`), which causes HTTP parsers to silently transform POST requests to GET requests, resulting in HTTP 405 "Method Not Allowed" errors.

This is the #1 cause of 405 errors with this node. Always verify your Ollama URL format first.

### 1. Configure Credentials (Optional)

**For self-hosted Ollama without authentication:** You can skip credential configuration. The node will connect directly to your Ollama instance.

**For authenticated Ollama instances:**

1. In n8n, go to **Credentials** > **New**
2. Select **Qwen Embedding API (Ollama)**
3. Enter:
   - **Ollama URL**: `http://localhost:11434` (**NO trailing slash!**)
   - **Model Name**: `qwen3-embedding:0.6b` (or your chosen model)
   - **API Key**: Your authentication token (if required)
4. **IMPORTANT:** Verify your URL has NO trailing slash before saving
5. Click **Test Connection** to verify

### 2. Using the Nodes

#### Qwen Embedding (Vector Store Integration)

Connect to any vector store node:

```
[Vector Store] ← [Qwen Embedding]
   (Stores)        (Provides embeddings)
```

**Use Cases:**
- RAG applications
- Semantic search
- Document indexing
- Knowledge bases

#### Qwen Embedding Tool (Direct Usage)

Use in any workflow for direct embedding generation:

```
[Trigger] → [Qwen Embedding Tool] → [Process/Store]
```

**Use Cases:**
- Similarity calculations
- Text clustering
- Anomaly detection
- Content deduplication

## ⚙️ Configuration Options

### Performance Mode

Controls timeout and retry behavior based on your hardware:

- **Auto-Detect** (default): Automatically detects GPU/CPU on first request
  - GPU detected (<1s response): 10s timeout, 2 retries
  - CPU detected (>5s response): 60s timeout, 3 retries
  - Works great for dynamic environments

- **GPU Optimized**: Manual setting for GPU hardware
  - 10 second timeout
  - 2 retry attempts
  - Best for NVIDIA GPU setups

- **CPU Optimized**: Manual setting for CPU hardware
  - 60 second timeout
  - 3 retry attempts
  - Prevents timeout errors on CPU-only systems

- **Custom**: User-defined timeout and retry settings
  - Set your own timeout (in milliseconds)
  - Configure max retry attempts (0-5)

**How Auto-Detection Works:**
```
First request measures actual response time:
- Response < 1s → GPU detected → timeout = 10s
- Response > 5s → CPU detected → timeout = 60s
- 1s ≤ response ≤ 5s → keep default 30s
```

### Dimensions

Adjust embedding vector size (32-1024 dimensions):

- **Default**: 1024 (full model dimensions)
- **Recommended ranges**:
  - 128-256: Smaller databases, faster similarity search
  - 512: Balanced performance/quality
  - 1024: Maximum quality (default)

**Implementation:** Uses Matryoshka Representation Learning (MRL) - dimensions are truncated or padded to match your target size without retraining the model.

### Instruction Type

Optimize embeddings for specific use cases:

- **None** (default): Standard embeddings without special instructions
- **Query**: Optimized for search queries
  - Prefix: `"Instruct: Retrieve semantically similar text.\nQuery: "`
  - Use for: User questions, search inputs
- **Document**: Optimized for document storage
  - Prefix: `"Instruct: Represent this document for retrieval.\nDocument: "`
  - Use for: Indexing documents, knowledge base entries

**Performance Impact:** 1-5% better semantic matching when query/document types match their use case.

### Context Prefix

Add custom context to all texts before embedding:

**Example:**
```
Context Prefix: "Medical context:"
Input text: "patient symptoms include fever"
Embedded as: "Medical context: patient symptoms include fever"
```

**Use Cases:**
- Domain-specific context (legal, medical, technical)
- Language hints
- Task-specific framing

### Return Format (Tool Only)

Controls output structure:

- **Full** (default):
  ```json
  {
    "embedding": [0.123, 0.456, ...],
    "dimensions": 1024,
    "text": "original text",
    "model": "qwen3-embedding:0.6b",
    "metadata": { ... }  // if includeMetadata enabled
  }
  ```

- **Simplified**:
  ```json
  {
    "text": "original text",
    "vector": [0.123, 0.456, ...],
    "dimensions": 1024
  }
  ```

- **Embedding Only**:
  ```json
  {
    "embedding": [0.123, 0.456, ...]
  }
  ```

### Include Metadata (Tool Only)

When enabled, adds processing metadata to output:

```json
{
  "metadata": {
    "prefix": "Medical context:",      // Context prefix used
    "instruction": "query",            // Instruction type applied
    "timestamp": "2025-10-07T19:44:23Z",  // Processing time
    "batchSize": 5                     // Number of texts (batch mode only)
  }
}
```

**Use Cases:**
- Debugging embedding configurations
- Tracking when embeddings were generated
- Auditing processing parameters

### Custom Timeout & Max Retries (Custom Mode Only)

Fine-tune request behavior:

- **Custom Timeout**: Milliseconds to wait before timeout (default: 30000)
- **Max Retries**: Number of retry attempts on failure (0-5, default: 2)

**Retry Logic:**
- Exponential backoff: 1s → 2s → 4s → 5s (capped)
- Clear console logging for debugging
- Automatic retry on transient failures

### Operation (Tool Only)

- **Generate Embedding**: Single text embedding
- **Generate Batch Embeddings**: Multiple texts in one request

## 📝 Examples

### Example 1: Vector Store with RAG

```
1. Add "Supabase Vector Store" node
2. Add "Qwen Embedding" node
3. Connect Qwen to Vector Store's embedding input
4. Configure your collection and start indexing
```

### Example 2: Semantic Search

```
1. Add "Manual Trigger" node
2. Add "Qwen Embedding Tool" node (set to "Generate Embedding")
3. Add another "Qwen Embedding Tool" for documents
4. Add "Code" node to calculate similarities
```

### Example 3: Batch Processing

```javascript
// Input: Array of texts
{
  "texts": [
    "First document",
    "Second document",
    "Third document"
  ]
}

// Qwen Embedding Tool (Batch mode) output:
{
  "embeddings": [[...], [...], [...]],
  "count": 3,
  "dimensions": 1024
}
```

## 🔬 Technical Details

### Model Information

- **Recommended Model**: `qwen3-embedding:0.6b`
  - 1024 native dimensions
  - MRL support (Matryoshka Representation Learning)
  - Adjustable dimensions: 32-1024
  - Multilingual support (100+ languages)
- **Alternative Models**: Any Ollama-compatible embedding model
- **Provider**: Ollama (local inference, no external API calls)

### Performance Characteristics

- **GPU Mode**: ~200-270ms per embedding (NVIDIA GPU)
- **CPU Mode**: 5-10 seconds per embedding
- **Auto-Detection**: Automatically adjusts timeouts based on hardware
- **Query Optimization**: 1-5% performance boost with instruction type
- **Batch Processing**: Processes texts sequentially (Ollama API limitation)
- **Timeout**: Adaptive (10s GPU, 60s CPU, or 30s default)

### API Compatibility

- **Ollama API**: `/api/embed` endpoint (POST method)
- **Request Format**: `{model: string, input: string}`
- **Response Format**: `{embeddings: number[][]}`
- **Authentication**: Optional (credentials not required for self-hosted)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Qwen Team](https://github.com/QwenLM) for the amazing embedding models
- [n8n Community](https://community.n8n.io/) for support and feedback
- [LangChain](https://github.com/langchain-ai/langchainjs) for the embedding interface

## 🐛 Troubleshooting

### HTTP 405 "Method Not Allowed" Errors

**Most Common Cause (90% of cases):** Trailing slash in Ollama URL configuration.

```bash
# Check your credential configuration:
✅ Correct: http://localhost:11434
❌ Wrong:   http://localhost:11434/
```

**Quick Fix:**
1. Go to N8N Credentials
2. Edit your Ollama credential
3. Remove the trailing slash from the URL
4. Save and test again

For other 405 error causes, see the comprehensive [HTTP 405 Troubleshooting Guide](docs/HTTP_405_TROUBLESHOOTING.md) which covers:
- URL formatting issues (trailing slashes)
- N8N authentication system issues
- Working patterns vs anti-patterns
- Step-by-step verification

### Model Not Found Errors

```bash
# Pull the correct model first:
ollama pull qwen3-embedding:0.6b

# Verify it's available:
ollama list
```

### Performance Issues

- **CPU mode timing out:** Use Performance Mode "CPU Optimized" or "Auto-Detect"
- **GPU not detected:** Ensure NVIDIA drivers and Docker GPU runtime are configured
- **Slow responses:** Check Ollama is running with `ollama list`

## 🔗 Links

- [NPM Package](https://www.npmjs.com/package/n8n-nodes-qwen-embedding)
- [GitHub Repository](https://github.com/theseedship/deposium_n8n_embeddings_integration)
- [Troubleshooting Guide](docs/HTTP_405_TROUBLESHOOTING.md)
- [n8n Community Nodes](https://n8n.io/integrations)
- [Qwen3-Embedding Paper](https://arxiv.org/abs/2411.00156)
- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings)

## 📮 Support

For issues and questions:
- [GitHub Issues](https://github.com/theseedship/deposium_n8n_embeddings_integration/issues)
- [n8n Community Forum](https://community.n8n.io/)

---

Made with ❤️ for the n8n community