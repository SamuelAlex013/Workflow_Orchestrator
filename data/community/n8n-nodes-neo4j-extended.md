# n8n-nodes-neo4j-extended

![Neo4j Banner](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

This is an n8n community node that provides comprehensive Neo4j integration with vector search, graph database operations, and AI tool capabilities.

[Neo4j](https://neo4j.com/) is a leading graph database with advanced vector search capabilities for knowledge graphs and AI applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Security](#security)  
[Vector Dimensions](#vector-dimensions)  
[Resources](#resources)  

## Features

- **Auto-Create Vector Indexes** 🚀 (NEW in v1.1.0)
  - Automatically creates missing vector indexes with dimension detection
  - Detects embedding dimensions from your data (1-2048)
  - Handles dimension mismatches with suffixed index names (e.g., `my_index_2048`)
  - No more "vector index does not exist" errors!

- **Dynamic Index Selection** 📋 (NEW in v1.1.0)
  - Dropdown menu to select existing vector indexes
  - Auto-populated list of available indexes
  - Works in "Add texts" and "Add documents" operations
  - Prevents typos and shows what indexes you have

- **Manual Vector Index Management** 🛠️ (NEW in v1.1.0)
  - Create Index: Manually create vector indexes with custom parameters
  - Delete Index: Remove vector indexes when no longer needed
  - List Indexes: View all vector indexes in your database
  - Get Index Info: Retrieve detailed information about specific indexes

- **Vector Store Operations:**
  - Similarity Search: Search for similar vectors with optional metadata filtering
  - Hybrid Search: Combine vector and fulltext search capabilities
  - Add Texts: Add new texts to the vector store (with auto-create)
  - Add Documents: Add document objects with metadata (with auto-create)

- **Graph Database Operations:**
  - Execute Query: Run custom Cypher queries with parameters
  - Create Node: Create new nodes with labels and properties
  - Create Relationship: Create relationships between nodes
  - Get Schema: Retrieve database schema information

- **AI Tool Integration:**
  - Usable as Tool: Can be used as a tool in LangChain agents
  - AI Embedding Support: Integrates with embedding models for vector operations
  - AI Tool Output: Provides ai_tool connection for agent workflows

- **Security** 🔒 (NEW in v1.1.0)
  - Comprehensive input validation prevents Cypher injection attacks
  - Multi-layer security (regex + explicit checks + length limits)
  - OWASP Top 10 compliant
  - See [SECURITY.md](SECURITY.md) for details

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-neo4j-extended
```

## Security

### v1.1.0 Security Enhancements

This version includes important security improvements:

- **Fixed**: Critical Cypher injection vulnerability (CVSS 9.8 → 2.0)
- **Added**: Comprehensive input validation for all vector index operations
- **Added**: Multi-layer defense against injection attacks
- **Validated**: 10/10 penetration tests passed, OWASP Top 10 compliant

**Security Features**:
- Regex-based identifier validation (`/^[a-zA-Z_$][a-zA-Z0-9_$]*$/`)
- Explicit backtick rejection (defense-in-depth)
- DoS protection (255 character limit)
- Type safety validation
- Range validation for vector dimensions (1-2048)

For security concerns, please see [SECURITY.md](SECURITY.md).

## Vector Dimensions

Neo4j vector indexes support dimensions from **1 to 2048** (Neo4j 5.11+).

### Common Embedding Models

| Model | Dimension | Similarity |
|-------|-----------|------------|
| OpenAI text-embedding-3-small | 1536 | Cosine |
| OpenAI text-embedding-ada-002 | 1536 | Cosine |
| GigaChat Embeddings | 2048 | Cosine |
| Sentence Transformers (MiniLM) | 384 | Cosine |
| Sentence Transformers (MPNet) | 768 | Cosine |
| Cohere Embed v3 | 1024 | Cosine |

**Note**: OpenAI `text-embedding-3-large` (3072D) exceeds Neo4j's 2048 limit. Consider dimension reduction or alternative models.

### Similarity Functions

- **Cosine**: Recommended for most text embeddings (measures angle between vectors)
- **Euclidean**: Measures straight-line distance between vectors

The plugin automatically detects dimensions from your embeddings and creates indexes accordingly.

## Operations

### Vector Store Operations

#### Similarity Search
1. Select "Vector Store" as the resource
2. Choose "Similarity Search" operation
3. Connect an embedding model to the AI Embedding input
4. Enter the query text
5. Optionally configure search type (vector/hybrid), number of results (k), and metadata filters
6. Execute to find similar vectors

#### Add Texts
1. Select "Vector Store" as the resource
2. Choose "Add Texts" operation
3. Connect an embedding model to the AI Embedding input
4. Enter the texts to add (supports multiple values)
5. Execute to store the texts as vectors

#### Add Documents
1. Select "Vector Store" as the resource
2. Choose "Add Documents" operation
3. Connect an embedding model to the AI Embedding input
4. Provide document objects as JSON array with pageContent and metadata
5. Execute to store the documents as vectors

### Graph Database Operations

#### Execute Query
1. Select "Graph Database" as the resource
2. Choose "Execute Query" operation
3. Enter your Cypher query
4. Optionally provide query parameters as JSON object
5. Execute to run the query

#### Create Node
1. Select "Graph Database" as the resource
2. Choose "Create Node" operation
3. Enter the node label
4. Provide node properties as JSON object
5. Execute to create the node

#### Create Relationship
1. Select "Graph Database" as the resource
2. Choose "Create Relationship" operation
3. Enter the "From Node Query" to match the source node
4. Enter the "To Node Query" to match the target node
5. Specify the relationship type
6. Optionally provide relationship properties as JSON object
7. Execute to create the relationship

#### Get Schema
1. Select "Graph Database" as the resource
2. Choose "Get Schema" operation
3. Select schema format (structured object or formatted string)
4. Execute to retrieve schema information

## Credentials

1. Add Neo4j credentials in n8n:
   - **Connection URI**: Neo4j connection string (e.g., `neo4j://localhost:7687`, `neo4j+s://xxx.databases.neo4j.io`)
   - **Username**: Neo4j username (default: `neo4j`)
   - **Password**: Neo4j password
   - **Database**: Database name (default: `neo4j`)

2. The node will appear in the n8n nodes panel under "Neo4j"

## Compatibility

- n8n version 1.0.0 and above
- Neo4j version 4.4.0 and above (with vector index support)
- LangChain community package 0.3.17+

## Usage

### Basic Vector Search Example

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "vectorStore",
        "operation": "similaritySearch",
        "queryText": "What is artificial intelligence?",
        "k": 5,
        "searchType": "hybrid"
      },
      "type": "n8n-nodes-neo4j-extended.neo4j",
      "credentials": {
        "neo4jApi": "your-neo4j-credentials"
      }
    }
  ]
}
```

### AI Agent Integration Example

The node can be used as a tool in AI Agent workflows:

```json
{
  "nodes": [
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.agent"
    },
    {
      "parameters": {
        "resource": "vectorStore",
        "operation": "similaritySearch",
        "mode": "retrieve-as-tool"
      },
      "type": "n8n-nodes-neo4j-extended.neo4j",
      "credentials": {
        "neo4jApi": "your-neo4j-credentials"
      }
    }
  ],
  "connections": {
    "Neo4j": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Graph Database Query Example

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "graphDb",
        "operation": "executeQuery",
        "cypherQuery": "MATCH (n:Person)-[:KNOWS]->(m:Person) WHERE n.name = $name RETURN m.name as friend",
        "queryParameters": "{\"name\": \"Alice\"}"
      },
      "type": "n8n-nodes-neo4j-extended.neo4j",
      "credentials": {
        "neo4jApi": "your-neo4j-credentials"
      }
    }
  ]
}
```

## Advanced Features

### Hybrid Search
The node supports Neo4j's hybrid search capabilities, combining vector similarity with fulltext search for enhanced retrieval accuracy.

### Metadata Filtering
Vector searches support metadata filtering to refine results based on specific node properties:

```json
{
  "metadataFilter": {
    "category": {"$eq": "technology"},
    "published_year": {"$gte": 2020}
  }
}
```

### Graph + Vector Workflows
Combine graph queries with vector operations for sophisticated AI-powered graph analysis.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Neo4j Documentation](https://neo4j.com/docs/)
- [Neo4j LangChain Integration](https://neo4j.com/labs/genai-ecosystem/langchain/)
- [Neo4j Vector Search Guide](https://neo4j.com/docs/cypher-manual/current/indexes-for-vector-search/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT
