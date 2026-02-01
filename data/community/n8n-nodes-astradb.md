# n8n-nodes-astradb

[![npm version](https://badge.fury.io/js/n8n-nodes-astradb.svg)](https://badge.fury.io/js/n8n-nodes-astradb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/node/v/n8n-nodes-astradb.svg)](https://nodejs.org/)

A comprehensive community node for n8n that provides seamless integration with DataStax Astra DB, a serverless NoSQL database with advanced vector capabilities for AI/ML applications.

## 🚀 Features

- **Full CRUD Operations**: Complete document lifecycle management
- **Vector Search**: Advanced AI/ML vector similarity search capabilities
- **Batch Operations**: Efficient bulk operations for large datasets
- **Atomic Operations**: ACID-compliant find and update/replace/delete operations
- **Advanced Querying**: Support for complex filters, projections, and sorting
- **Connection Testing**: Built-in credential validation and connection testing
- **Error Handling**: Comprehensive error handling with retry mechanisms
- **Type Safety**: Full TypeScript support with comprehensive type definitions
- **Performance Optimized**: Connection pooling and query optimization

## 📦 Installation

### Method 1: npm (Recommended)
```bash
npm install n8n-nodes-astradb
```

### Method 2: Community Nodes Installation
1. In your n8n instance, go to **Settings** → **Community Nodes**
2. Click **Install a community node**
3. Enter `n8n-nodes-astradb`
4. Click **Install**

### Method 3: [Manual Installation](https://docs.n8n.io/integrations/community-nodes/installation)
1. Download the latest release from [GitHub](https://github.com/msmygit/n8n-nodes-astradb/releases)
2. Extract to your n8n community nodes directory
3. Run `npm install` in the extracted directory

## ⚙️ Configuration

### Credentials Setup

Create an Astra DB API credential with the following fields:

- **Endpoint**: Your Astra DB endpoint URL
  - Format: `https://your-database-id-your-region.apps.astra.datastax.com`
  - Example: `https://abc123-def456-us-east1.apps.astra.datastax.com`
- **Token**: Your Astra DB application token

### Getting Your Credentials

1. [**Create Astra DB Database**](https://docs.datastax.com/en/astra-db-serverless/databases/create-database.html):
   - Go to [DataStax Astra](https://astra.datastax.com?utm_source=MadhavanS)
   - Sign up or log in to your account
   - Create a new database or select an existing one

2. [**Get Connection Details**](https://docs.datastax.com/en/astra-db-serverless/administration/manage-application-tokens.html):
   - Navigate to your database dashboard
   - Go to the **Connect** tab
   - Copy your **Endpoint URL**
   - Generate an **Application Token** (with appropriate permissions)

3. **Configure in n8n**:
   - In n8n, go to **Credentials** → **Add Credential**
   - Search for "Astra DB API"
   - Enter your endpoint and token
   - Test the connection

## 🔧 Operations

### 📝 Insert Operations

#### Insert One
Insert a single document into a collection.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name  
- **Document**: JSON document to insert

**Example:**
```json
{
  "name": "Ni2 Maddy",
  "email": "ni2maddy@bits.com",
  "age": 30,
  "createdAt": "2024-01-01T00:00:00Z"
}
```

#### Insert Many
Insert multiple documents in a single operation.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Documents**: Array of JSON documents
- **Options**: Additional options (limit, skip, etc.)

**Example:**
```json
[
  {
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "name": "Jane Smith", 
    "email": "jane@example.com"
  }
]
```

### 🔍 Find Operations

#### Find Many
Find multiple documents matching filter criteria.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Options**: Query options (limit, skip, sort, projection)

#### Find One
Find a single document matching filter criteria.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Options**: Query options

### ✏️ Update Operations

#### Update Many
Update multiple documents matching filter criteria.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Update**: JSON update operations
- **Options**: Update options (upsert, etc.)

**Update Example:**
```json
{
  "$set": {
    "lastLogin": "2024-01-01T12:00:00Z",
    "status": "active"
  },
  "$inc": {
    "loginCount": 1
  }
}
```

#### Find and Update
Atomically find and update a single document.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Update**: JSON update operations
- **Options**: Update options (upsert, returnDocument)

#### Find and Replace
Atomically find and replace a single document.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Replacement**: Complete replacement document
- **Options**: Update options

### 🗑️ Delete Operations

#### Delete
Delete documents matching filter criteria.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria

#### Find and Delete
Atomically find and delete a single document.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Filter**: JSON filter criteria
- **Options**: Query options

### 📊 Utility Operations

#### Estimated Document Count
Get an estimated count of documents in the collection.

**Parameters:**
- **Keyspace**: The keyspace name
- **Collection**: The collection name
- **Options**: Query options

## 🔍 Query Examples

### Basic Filters
```json
// Exact match
{
  "name": "John Doe"
}

// Range queries
{
  "age": { "$gte": 18, "$lt": 65 }
}

// Array operations
{
  "tags": { "$in": ["premium", "vip"] }
}
```

### Complex Filters
```json
{
  "$and": [
    { "status": "active" },
    { "$or": [
      { "role": "admin" },
      { "role": "user" }
    ]},
    { "createdAt": { "$gte": "2024-01-01T00:00:00Z" } }
  ]
}
```

### Sort Options
```json
{
  "name": 1,        // Ascending
  "createdAt": -1   // Descending
}
```

### Projection
```json
{
  "name": 1,        // Include
  "email": 1,       // Include
  "_id": 0          // Exclude
}
```

## 🤖 Vector Operations

Astra DB provides powerful vector search capabilities for AI/ML applications:

### Insert Vector Document
```json
{
  "text": "Sample document content",
  "embedding": [0.1, 0.2, 0.3, 0.4, 0.5],
  "metadata": {
    "source": "document.pdf",
    "page": 1,
    "category": "technical"
  }
}
```

### Vector Search
```json
{
  "embedding": [0.1, 0.2, 0.3, 0.4, 0.5],
  "similarity": 0.8,
  "vectorFilter": {
    "category": "technical"
  }
}
```

### Vector Search Options
- **Embedding**: Vector array for similarity search
- **Similarity Threshold**: Minimum similarity score (0-1)
- **Vector Filter**: Additional filter criteria
- **Limit**: Maximum number of results

## ⚡ Advanced Options

### Query Options
- **Limit**: Maximum documents to return (1-1000)
- **Skip**: Number of documents to skip (pagination)
- **Sort**: Sort criteria with field and direction
- **Projection**: Fields to include/exclude
- **Upsert**: Create document if not found (update operations)
- **Return Document**: Return before/after version (atomic operations)

### Additional Options
- **Continue on Fail**: Continue processing other items on failure
- **Timeout**: Operation timeout in seconds (1-300)
- **Retry Attempts**: Number of retry attempts (0-10)

## 🛡️ Error Handling

The node includes comprehensive error handling:

- **Connection Errors**: Automatic retry with exponential backoff
- **Validation Errors**: Clear error messages for invalid inputs
- **Query Errors**: Detailed error information for failed operations
- **Continue on Fail**: Option to continue processing other items on individual failures
- **Input Sanitization**: Protection against injection attacks
- **Type Safety**: Runtime type checking and validation

## 🧪 Testing

### Unit Tests
```bash
npm test
```

### Test Coverage
```bash
npm run test:coverage
```

### Watch Mode
```bash
npm run test:watch
```

## 🚀 Development

### Prerequisites
- Node.js 18.17.0 or higher
- npm or yarn
- Astra DB account and database

### Setup
```bash
git clone https://github.com/msmygit/n8n-nodes-astradb.git
cd n8n-nodes-astradb
npm install
```

### Build
```bash
npm run build
```

### Development Mode
```bash
npm run dev
```

### Linting
```bash
npm run lint
npm run lint:fix
```

## 📚 Examples

### Basic CRUD Workflow
1. **Trigger**: Schedule or webhook
2. **Astra DB - Find**: Query existing data
3. **Astra DB - Update**: Modify documents
4. **Astra DB - Insert**: Add new documents

### Vector Search Workflow
1. **Trigger**: Document upload
2. **AI Embedding**: Generate vector embeddings
3. **Astra DB - Insert**: Store document with embeddings
4. **Astra DB - Vector Search**: Find similar documents

### Data Migration Workflow
1. **Trigger**: Manual or scheduled
2. **Astra DB - Find Many**: Query source data
3. **Transform**: Process and clean data
4. **Astra DB - Insert Many**: Bulk insert to target

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow TypeScript best practices
- Add tests for new functionality
- Update documentation
- Follow the existing code style
- Ensure all tests pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Documentation
- [Astra DB Documentation](https://docs.datastax.com/en/astra-db-serverless/)
- [n8n Community Nodes Guide](https://docs.n8n.io/integrations/community-nodes/)

### Community Support
- [GitHub Issues](https://github.com/msmygit/n8n-nodes-astradb/issues)
- [n8n Community Forum](https://community.n8n.io/)
- [DataStax Community](https://dtsx.io/discord)

### Professional Support
- [DataStax Support](https://www.datastax.com/support)
- [n8n Enterprise Support](https://n8n.io/enterprise/)

## 🏆 Acknowledgments

- DataStax for providing Astra DB, an excellent knowledge layer
- n8n team for the platform
- Community contributors and testers

## 📈 Roadmap

### Version 1.1 (Planned)
- [ ] Advanced aggregation operations
- [ ] Real-time change streams
- [ ] Enhanced vector search features
- [ ] Performance monitoring

### Version 1.2 (Planned)
- [ ] Multi-region support
- [ ] Advanced security features
- [ ] Custom authentication methods
- [ ] Enhanced error reporting

---

**Made with ❤️ for the n8n and IBM DataStax communities**