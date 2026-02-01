# n8n Cloudflare D1 Node

[![npm version](https://badge.fury.io/js/n8n-nodes-cloudflare-d1.svg)](https://badge.fury.io/js/n8n-nodes-cloudflare-d1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive n8n community node for integrating with Cloudflare D1, a serverless SQLite-compatible database. This node provides complete database management, visual query builders, AI-friendly operations, structured CRUD operations, and advanced chat memory capabilities for AI Agent workflows.

![Cloudflare D1 Node](https://raw.githubusercontent.com/jezweb/n8n-nodes-cloudflare-d1/main/docs/images/node-preview.png)

## Features

### Core Database Operations
- ➕ **Insert**: Add new records with column mapping
- 🔍 **Select**: Query records with conditions and sorting
- ✏️ **Update**: Modify existing records
- ❌ **Delete**: Remove records with conditions
- 🎯 **Find Record** (v0.5.6): AI-friendly simple search operation with intelligent operators

### Table Management
- 📋 **Create Tables**: Visual table builder without SQL knowledge
- 🔍 **List Tables**: View all tables and views in your database
- 📊 **Schema Inspection**: View table structure and column definitions
- 🗑️ **Drop Tables**: Safe table deletion with IF EXISTS support
- 🔧 **Alter Tables**: Add/drop columns, rename tables, manage indexes

### Query Builder Tools
- 🎨 **Visual Query Builder**: Build complex SELECT queries without SQL
- 📈 **Aggregate Queries**: COUNT, SUM, AVG, MIN, MAX, GROUP_CONCAT
- 🔎 **Search Records**: Full-text search across multiple columns
- 🎯 **Distinct Values**: Extract unique values from columns
- 📊 **Table Statistics**: Row counts and database analytics

### Database Management
- 💾 **Export Database**: Backup databases to SQL files
- 📂 **Import Database**: Restore from SQL dumps
- ℹ️ **Database Info**: View metadata, size, and creation date
- 📝 **List Databases**: View all D1 databases in your account

### Memory Resource Operations (v0.5.0)
- 📚 **Get Chat History**: Retrieve conversation messages by session
- 🔍 **Search Messages**: Full-text search across all chat sessions with fuzzy matching
- ⏱️ **Get Recent Messages**: Fetch the most recent messages from a session
- 📋 **Get Session List**: List all available chat sessions with message counts
- 🗑️ **Clear Session**: Delete all messages from a specific session

### AI & Chat Capabilities
- 🤖 **AI Agent Compatible**: Optimized for use with n8n AI Agents and MCP Trigger nodes
- 💬 **Chat Memory Storage**: LangChain-compatible chat message storage and retrieval
- 🧠 **Session Management**: Automatic conversation context and session handling
- 🔄 **Auto-Cleanup**: Message expiration and memory management
- 🔎 **Fuzzy Search** (v0.5.2): Advanced message search with fuzzy matching capabilities

### Security & Reliability
- 🔐 **Secure Authentication**: Cloudflare API token-based authentication with credential encryption
- 🛡️ **SQL Injection Protection**: Parameterized queries prevent SQL injection attacks
- 🔍 **Error Handling**: Comprehensive error reporting and debugging support
- ⚡ **High Performance**: Batch operations and optimized query execution
- 🔧 **Developer Experience**: Rich TypeScript types and comprehensive documentation

## Quick Start

### Installation

#### Via n8n Community Nodes (Recommended)
1. Go to **Settings > Community Nodes** in your n8n instance
2. Enter `n8n-nodes-cloudflare-d1` and click Install
3. Restart n8n - both **Cloudflare D1** and **Cloudflare D1 Chat Memory** nodes will appear in your nodes panel

#### Via npm
```bash
npm install n8n-nodes-cloudflare-d1
```

### Prerequisites
- n8n instance (local or cloud)
- Cloudflare account with D1 database access
- Cloudflare API token with D1 permissions

### Setup Cloudflare Credentials

1. **Get your Cloudflare Account ID**:
   - Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
   - Copy your Account ID from the right sidebar

2. **Create an API Token**:
   - Go to **My Profile > API Tokens**
   - Click **Create Token** → **Custom Token**
   - Add permissions: `D1:Read` and `D1:Write`
   - Include your account in the Account Resources
   - Click **Continue to Summary** → **Create Token**

3. **Configure in n8n**:
   - Create a new **Cloudflare D1 API** credential
   - Enter your Account ID and API Token

### Create a D1 Database

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Create a new D1 database
wrangler d1 create my-database

# Create a table (optional)
wrangler d1 execute my-database --command="CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);"
```

## Usage Examples

### Basic Query Execution

```sql
-- Select all users
SELECT * FROM users;

-- Insert a new user with parameters
INSERT INTO users (name, email) VALUES (?, ?);
-- Parameters: ["John Doe", "john@example.com"]
```

### Batch Operations

Execute multiple queries in a single transaction:

```sql
-- Query 1: Insert user
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Query 2: Create user profile
INSERT INTO profiles (user_id, bio) VALUES (last_insert_rowid(), 'Software Developer');
```

### JSON Operations

```sql
-- Query JSON data stored in D1
SELECT json_extract(metadata, '$.preferences.theme') as theme
FROM users 
WHERE json_extract(metadata, '$.active') = 1;

-- Update JSON field
UPDATE users 
SET metadata = json_set(metadata, '$.last_login', datetime('now'))
WHERE id = ?;
```

## Node Operations

### Main Node: Cloudflare D1

#### Structured Operations

##### Find Record (v0.5.6)
AI-friendly operation for finding records with simple search criteria. Automatically handles operator selection based on value type.

##### Insert
Add new records to a table with column mapping and value specification.

##### Select
Query records with conditions, sorting, and column selection.

##### Update
Modify existing records with WHERE conditions.

##### Delete
Remove records from a table based on conditions.

#### Table Management Operations

##### Create Table
Create a new table visually without writing SQL. Use the column builder to add columns with types and constraints.

**Features:**
- Visual column definition with types (TEXT, INTEGER, REAL, BLOB, BOOLEAN, DATETIME, JSON)
- Constraint configuration (PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT, AUTO INCREMENT)
- IF NOT EXISTS option for safe table creation

##### List Tables
Get a list of all tables and views in your database.

##### Get Table Schema
View the structure of a table including column names, types, and constraints.

##### Drop Table
Safely delete a table with optional IF EXISTS clause.

##### Alter Table
Modify table structure (add/drop columns, rename, manage indexes).

#### Query Builder Operations

##### Query Builder
Build complex SELECT queries visually without SQL knowledge.

**Features:**
- Column selection
- WHERE conditions with multiple operators (=, !=, >, <, LIKE, IN, BETWEEN, etc.)
- JOIN support (INNER, LEFT, RIGHT, FULL)
- GROUP BY and HAVING clauses
- ORDER BY with multiple columns
- LIMIT and OFFSET for pagination

##### Aggregate Query
Perform statistical operations on your data.

**Functions:**
- COUNT, SUM, AVG, MIN, MAX, GROUP_CONCAT
- WHERE filtering
- GROUP BY support

##### Search Records
Search across multiple columns with pattern matching.

##### Get Distinct Values
Extract unique values from one or more columns.

##### Table Statistics
Get row counts and database analytics.

#### Memory Resource Operations

##### Get Chat History
Retrieve conversation messages from a specific session with filtering options.

##### Search Messages
Search across all chat sessions with full-text and fuzzy search capabilities.

##### Get Recent Messages
Fetch the most recent messages from a session for context.

##### Get Session List
List all available chat sessions with message counts and metadata.

##### Clear Session
Delete all messages from a specific session for cleanup.

#### Database Management Operations

##### Export Database
Export your entire database to a SQL dump file with a signed URL.

##### Import Database
Import data from a SQL file to restore or migrate databases.

##### Get Database Info
View database metadata including UUID, table count, size, and creation date.

##### List Databases
List all D1 databases in your Cloudflare account.

#### Core Query Operations

##### Execute Query
Execute a single parameterized SQL query with optional parameter binding.

**Parameters:**
- **Database ID**: Your D1 database identifier
- **SQL Query**: The SQL statement to execute  
- **Parameters**: Optional array of parameters for binding (prevents SQL injection)

##### Batch Queries  
Execute multiple SQL queries in a single transaction for better performance and atomicity.

**Parameters:**
- **Database ID**: Your D1 database identifier
- **Queries**: Array of SQL statements with optional parameters

##### Execute Raw SQL
Execute raw SQL commands without parameter binding (use with caution).

**Parameters:**
- **Database ID**: Your D1 database identifier  
- **SQL Commands**: Raw SQL to execute

### Chat Memory Node: Cloudflare D1 Chat Memory

#### Purpose
LangChain-compatible chat message storage for AI Agent workflows. This sub-node provides persistent conversation memory using your D1 database.

#### Key Features
- **Session-based Storage**: Organize messages by conversation sessions
- **Message Types**: Support for human, AI, and system messages  
- **Auto-Management**: Automatic table creation and message cleanup
- **Configurable Limits**: Set maximum messages per session and expiration periods
- **Metadata Support**: Store additional context with each message

#### Configuration
- **Database ID**: Your D1 database identifier
- **Session ID**: Unique identifier for the conversation (supports expressions)
- **Table Name**: Custom table name for message storage (default: `chat_memory`)
- **Max Messages**: Maximum messages to keep per session (default: 100)
- **Expiration Days**: Auto-delete messages older than specified days (default: 30)

#### Integration with AI Agents
Connect this node to your AI Agent as a memory source for persistent conversation context. The node handles all chat history management automatically.

## AI Agent Integration

Both nodes are optimized for AI Agent workflows and can be used as tools by AI Agents:

### Database Operations Workflow

1. **MCP Trigger Node**: Receives AI Agent requests for data operations
2. **Cloudflare D1 Node**: Executes database queries and operations  
3. **Return results**: Structured data formatted for AI consumption

### Chat Memory Workflow

1. **AI Agent**: Generates responses and needs conversation context
2. **Cloudflare D1 Chat Memory**: Automatically stores and retrieves chat history
3. **Persistent Context**: Maintains conversation continuity across sessions

### Example Workflow: AI Chatbot with Memory
```
User Input → AI Agent → Chat Memory (retrieve context) → AI Processing → 
Response Generation → Chat Memory (store messages) → User Response
```

### AI-Friendly Features

- **Tool Compatibility**: Both nodes set `usableAsTool: true` for AI Agent discovery
- **Rich Descriptions**: All operations include AI-friendly descriptions and examples
- **Context Awareness**: Chat memory node provides conversation context for AI responses
- **Session Management**: Automatic handling of conversation sessions and message cleanup

## Error Handling

Both nodes provide comprehensive error handling with detailed error messages:

### Database Operation Errors
- **Authentication Errors**: Invalid API tokens or account IDs
- **Database Errors**: Database not found or access denied
- **SQL Errors**: Syntax errors with line numbers and context
- **Rate Limiting**: Automatic retry logic for rate-limited requests
- **Network Errors**: Connection timeouts and network issues

### Chat Memory Specific Errors
- **Table Creation**: Automatic handling of missing chat memory tables
- **Session Management**: Validation of session IDs and configuration
- **Message Cleanup**: Graceful handling of cleanup operation failures
- **Storage Limits**: Warnings for approaching storage or message limits

## Advanced Features

### Session Management
```sql
-- Use sessions for consistency across queries
-- Automatically handled by the node for batch operations
```

### Performance Optimization
- Parameterized queries for repeated operations
- Batch operations for bulk data processing
- Connection pooling handled by Cloudflare
- Automatic query optimization

### Security Features
- API token-based authentication
- Encrypted credential storage
- SQL injection prevention via parameterized queries
- Audit logging support

## Configuration

### Environment Variables
```env
# Optional: Custom Cloudflare API endpoint
CLOUDFLARE_API_ENDPOINT=https://api.cloudflare.com/client/v4

# Optional: Request timeout (milliseconds)
D1_REQUEST_TIMEOUT=30000
```

### Workflow Settings
- **Timeout**: Customize query timeout periods
- **Retry Logic**: Configure retry attempts for failed requests
- **Error Handling**: Choose between stopping workflow or continuing on errors

## Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/jezweb/n8n-nodes-cloudflare-d1.git
cd n8n-nodes-cloudflare-d1

# Install dependencies
npm install

# Build the project
npm run build

# Link for local n8n development
npm link
cd ~/.n8n/custom
npm link n8n-nodes-cloudflare-d1

# Start n8n
n8n start
```

### Testing

```bash
# Run linting
npm run lint

# Run tests
npm test

# Format code
npm run format
```

## API Reference

### Cloudflare D1 REST API
This node uses the [Cloudflare D1 REST API](https://developers.cloudflare.com/d1/api/):

- **Base URL**: `https://api.cloudflare.com/client/v4`
- **Endpoint**: `/accounts/{account_id}/d1/database/{database_id}/query`
- **Authentication**: Bearer token

### Response Format
```json
{
  "success": true,
  "result": [
    {
      "results": [...],
      "success": true,
      "meta": {
        "duration": 0.123,
        "rows_read": 1,
        "rows_written": 0
      }
    }
  ]
}
```

## Troubleshooting

### Common Issues

**Node not appearing in n8n:**
- Restart n8n after installation
- Check n8n logs for errors
- Verify package installation: `npm list n8n-nodes-cloudflare-d1`

**Authentication errors:**
- Verify Account ID and API Token
- Check token permissions include D1:Read and D1:Write  
- Ensure token hasn't expired

**Query execution failures:**
- Verify database ID is correct
- Check SQL syntax
- Review D1 database permissions

### Debug Mode

Enable debug logging:
```bash
N8N_LOG_LEVEL=debug n8n start
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE.md) for details.

## Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-cloudflare-d1/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/jezweb/n8n-nodes-cloudflare-d1/discussions)  
- 📖 **Documentation**: [Wiki](https://github.com/jezweb/n8n-nodes-cloudflare-d1/wiki)
- 🌐 **Community**: [n8n Community Forum](https://community.n8n.io)

## Related Links

- [n8n Documentation](https://docs.n8n.io/)
- [Cloudflare D1 Documentation](https://developers.cloudflare.com/d1/)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [Cloudflare API Documentation](https://developers.cloudflare.com/api/)

---

Made with ❤️ by [Jez (Jeremy Dawes)](https://www.jezweb.com.au) - [Jezweb](https://www.jezweb.com.au)