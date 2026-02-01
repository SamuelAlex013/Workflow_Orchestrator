# n8n-nodes-sap-hana-vector-store

This is an n8n community node for integrating SAP HANA Vector Store with n8n workflows using LangChain.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Features

- **Vector Store Operations**: Store, retrieve, and manage vector embeddings in SAP HANA
- **LangChain Integration**: Seamlessly works with LangChain for AI/ML workflows
- **Document Management**: Load, insert, update, and retrieve documents with embeddings
- **Similarity Search**: Find similar documents based on vector similarity
- **Metadata Support**: Store and query documents with custom metadata

## Installation

**⚠️ Important**: This node is designed for **self-hosted n8n** installations only. It cannot be used with n8n Cloud due to dependency requirements.

### Option 1: npm Installation (Recommended)

1. Navigate to your n8n installation directory
2. Install the package:
   ```bash
   npm install n8n-nodes-sap-hana-vector-store
   ```
3. Restart your n8n instance

### Option 2: Development Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/pondev1/n8n-nodes-sap-hana-vector-store.git
   cd n8n-nodes-sap-hana-vector-store
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the node:
   ```bash
   npm run build
   ```

4. Link the package locally:
   ```bash
   npm pack
   cd ~/.n8n
   npm install "C:\path\to\n8n-nodes-sap-ai-core\n8n-nodes-sap-hana-vector-store-1.0.0.tgz"
   ```

5. Restart your n8n instance

## Operations

### Available Operations

1. **Load**: Load documents from the vector store
2. **Insert Documents**: Add new documents with embeddings to the store
3. **Get Documents**: Retrieve specific documents by ID or metadata
4. **Update Documents**: Update existing documents in the store
5. **Retrieve (As Tool)**: Use the vector store as a tool for AI agents

## Credentials

You'll need to configure SAP HANA credentials with the following information:

- **Host**: Database hostname (from service key "host" field)
- **Port**: Database port (from service key "port" field, typically 443 for HANA Cloud)
- **Username**: Database username (from service key "user" field)
  - Use **_DT** suffix user for design-time operations (creating/modifying database objects) - **Recommended for this node**
  - Use **_RT** suffix user for runtime operations (reading data, SELECT queries)
- **Password**: Database password (from service key "password" field)
- **Database**: Database name (from service key "database" field, optional)
- **Schema**: Schema name (from service key "schema" field or your specific schema)

### Additional Options
- **SSL/TLS**: Enable encryption for secure connections
- **Validate Certificate**: Certificate validation for production environments
- **Connection Timeout**: Customize connection timeout
- **Auto Commit**: Transaction auto-commit setting

## Prerequisites

- SAP HANA Cloud instance or on-premise SAP HANA database
- Database user with appropriate permissions
- Vector tables configured in your HANA instance

## SAP HANA Vector Table Structure

The default vector table structure expected:
- `VEC_TEXT` (NCLOB) - Document content
- `VEC_META` (NVARCHAR) - JSON metadata
- `VEC_VECTOR` (REAL_VECTOR) - Vector embeddings

## Usage Example

### Basic Document Storage

1. Connect an Embeddings node (e.g., OpenAI Embeddings)
2. Configure your SAP HANA credentials
3. Set the table name for your vector store
4. Choose operation (Insert/Load/Update)
5. Connect to your workflow

### Similarity Search

Use the "Load" operation with:
- **Mode**: Load
- **Prompt**: Your search query
- **Top K**: Number of similar documents to retrieve

## Compatibility

- Requires n8n version 1.82.0 or later
- Node.js 18.0.0 or higher
- Compatible with SAP HANA Cloud and on-premise installations

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [SAP HANA Cloud Documentation](https://help.sap.com/docs/HANA_CLOUD)
- [LangChain Documentation](https://js.langchain.com/docs/)

## Sample Workflows

Ready-to-use n8n workflow examples are available in the `workflows/` directory:

### 1. Document Ingestion Workflow
**File**: [`workflows/Document Ingestion.json`](./workflows/Document%20Ingestion.json)

Comprehensive workflow for ingesting documents into SAP HANA Vector Store with embeddings generation and storage.

**Features**:
- Document processing and chunking
- Embedding generation using SAP AI Core
- Vector storage in HANA database
- Metadata extraction and storage
- Batch processing capabilities

### 2. RAG (Retrieval-Augmented Generation) Workflow
**File**: [`workflows/RAG.json`](./workflows/RAG.json)

Advanced RAG workflow that combines SAP AI Core embeddings, HANA Vector Store, and chat models for intelligent document retrieval and generation.

**Features**:
- Chat trigger for interactive conversations
- SAP AI Core embeddings integration
- Vector store retrieval capabilities
- AI agent with RAG functionality
- Context-aware responses

### How to Use Sample Workflows

1. Download the desired workflow JSON file
2. In n8n, go to **Workflows** > **Import from File**
3. Select the downloaded JSON file
4. Configure your SAP HANA credentials
5. Update the `tableName` with your vector table name
6. Configure embedding function settings
7. Activate and test the workflow

## Support

For issues and feature requests, please use the [GitHub issues](https://github.com/pondev1/n8n-nodes-sap-hana-vector-store/issues) page.

## License

[MIT](https://github.com/pondev1/n8n-nodes-sap-hana-vector-store/blob/master/LICENSE)

## Author

**Pon Murugesh Devendren**  
Email: pon.murugesan.d@gmail.com  
GitHub: [@pondev1](https://github.com/pondev1)