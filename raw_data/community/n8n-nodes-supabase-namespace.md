# n8n-nodes-supabase-namespace

This is an n8n community node that allows you to work with Supabase Vector Store with extended support for custom schemas and namespaces.

Supabase Vector Store is a vector database that allows you to store and search document embeddings efficiently, ideal for AI applications and semantic search.

[n8n](https://n8n.io/) is a workflow automation platform with [fair-code license](https://docs.n8n.io/reference/license/).

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version History](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following operations:

- **Load**: Load an existing vector store from Supabase
- **Insert**: Insert new documents into the vector store
- **Retrieve**: Retrieve similar documents based on queries
- **Update**: Update existing documents in the vector store
- **Retrieve as Tool**: Use retrieval as a tool in LangChain flows

## Main Features

### 🗄️ Custom Schema Support
- Use database schemas different from the default "public" schema
- Flexible configuration for multi-tenant environments

### 🏷️ Namespace System
- Logical partitioning of documents
- Efficient filtering by namespace
- Option to clear namespaces before inserting new data

### 🔍 Custom Queries
- Configuration of custom query names
- Support for advanced metadata filters
- Native integration with LangChain

## Credentials

To use this node, you need to configure Supabase credentials:

### Prerequisites
1. An account on [Supabase](https://supabase.com/)
2. A configured Supabase project
3. A PostgreSQL database with the `pgvector` extension enabled

### Credential Configuration
1. Go to your Supabase project
2. Navigate to Settings > API
3. Copy your **Project URL** (host)
4. Copy your **service_role** key (not the anon key)
5. In n8n, configure the credentials with:
   - **Host**: Your Project URL
   - **Service Role**: Your service_role key

### Required Table Structure
Your table must have the following minimum structure:
```sql
CREATE TABLE your_table_name (
  id BIGSERIAL PRIMARY KEY,
  content TEXT,
  metadata JSONB,
  embedding vector(1536), -- or the dimension of your embeddings
  namespace TEXT -- column for the namespace system
);
```

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Minimum Node.js version**: 20.15
- **Tested versions**: n8n 1.0.0+

## Usage

### Basic Configuration
1. **Table Name**: Select or write the name of your table
2. **Use Custom Schema**: Activate if you want to use a schema different from "public"
3. **Schema**: Specify the schema name (e.g., "ai_docs", "user_data")
4. **Namespace**: Define a namespace to organize your documents

### Common Use Cases

#### 📚 Client Document Management
```json
{
  "tableName": "documents",
  "schema": "client_data",
  "namespace": "client_123",
  "options": {
    "clearNamespace": true
  }
}
```

#### 🔍 Semantic Search
```json
{
  "tableName": "knowledge_base",
  "namespace": "product_docs",
  "options": {
    "queryName": "search_products",
    "metadataFilter": {
      "category": "electronics"
    }
  }
}
```

#### 🔄 Data Update
```json
{
  "tableName": "user_preferences",
  "schema": "user_profiles",
  "namespace": "user_456"
}
```

### LangChain Integration
This node integrates perfectly with LangChain flows in n8n, enabling:
- Complex reasoning chains
- Conversational agents
- Recommendation systems
- Document analysis

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Official Supabase documentation](https://supabase.com/docs)
* [pgvector guide](https://github.com/pgvector/pgvector)
* [LangChain documentation](https://python.langchain.com/docs/get_started/introduction)
* [Project repository](https://github.com/Nesticopng/n8n-nodes-supabase-namespace)

## Version History

### v0.1.0 (Current)
- ✅ Basic support for Supabase Vector Store
- ✅ Namespace system implemented
- ✅ Support for custom schemas
- ✅ Complete CRUD operations
- ✅ LangChain integration
- ✅ Advanced metadata filters

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

**Néstor Cano** - [nestor.cano.vielma@gmail.com](mailto:nestor.cano.vielma@gmail.com)

---

⭐ If this node is useful to you, consider giving the repository a star!
