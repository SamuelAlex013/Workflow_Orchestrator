![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-hap

[![npm version](https://badge.fury.io/js/n8n-nodes-hap.svg)](https://badge.fury.io/js/n8n-nodes-hap)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An official n8n community node for integrating with **HAP (Hyper Application Platform)** - an innovative no-code platform that enables users to build enterprise applications without coding.

## 📋 Table of Contents

- [Installation](#installation)
- [Credentials](#credentials)
- [Operations](#operations)
- [Examples](#examples)
- [API Compatibility](#api-compatibility)
- [Development](#development)
- [License](#license)

## 🚀 Installation

### Community Nodes (Recommended)

Install directly from the n8n Community Nodes interface:

1. Go to **Settings** → **Community Nodes** in n8n
2. Select **Install** and enter: `n8n-nodes-hap`
3. Click **Install**

### Manual Installation

```bash
# For n8n installed globally
npm install -g n8n-nodes-hap

# For local n8n installation
npm install n8n-nodes-hap
```

### Docker

```dockerfile
FROM n8nio/n8n:latest
RUN npm install -g n8n-nodes-hap
```

## 🔐 Credentials

Configure HAP API credentials in n8n:

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| **API Domain** | HAP API endpoint URL | `https://api.mingdao.com` |
| **HAP App Key** | Your application key | `your-app-key` |
| **HAP Sign** | Your signature key | `your-sign-key` |

### Private Deployment

For private deployments, append `/api` to your service address:
- **Public**: `https://api.mingdao.com`
- **Private**: `https://your-domain.com/api`

## 📚 Operations

### 🏢 Application Operations
- **Get Information** - Retrieve application details and configuration

### 📊 Worksheet Operations
- **Create** - Create new worksheets with custom fields
- **Get Structure** - Retrieve worksheet configuration and field definitions
- **Update** - Modify worksheet properties and field structures
- **Delete** - Remove worksheets from application

### 📝 Record Operations
- **Create** - Add new records with field data
- **Get** - Retrieve individual records by ID
- **Update** - Modify existing record field values
- **Delete** - Remove records (soft or permanent deletion)
- **Get Many** - Query multiple records with filtering, sorting, and pagination
- **Batch Create** - Create multiple records in a single operation
- **Batch Update** - Update multiple records simultaneously
- **Batch Delete** - Delete multiple records at once
- **Get Related** - Retrieve records related through relationship fields
- **Get Pivot** - Generate pivot table data with aggregations
- **Get Share Link** - Create shareable links for records
- **Get Logs** - Retrieve operation history and audit trails
- **Get Discussions** - Access record comments and discussions

### ⚙️ Workflow Operations
- **Get Many** - List available workflows
- **Get** - Retrieve workflow details and configuration
- **Trigger** - Execute workflows with input parameters

### 🎯 Option Set Operations
- **Get Many** - List all option sets
- **Create** - Create new option sets with values, colors, and scores
- **Update** - Modify option set configurations
- **Delete** - Remove option sets

### 👥 Role Operations
- **Get Many** - List all roles
- **Create** - Create new roles with descriptions
- **Get** - Retrieve role details
- **Delete** - Remove roles
- **Add Member** - Add users, departments, or job positions to roles
- **Remove Member** - Remove members from roles
- **Leave All** - Remove user from all assigned roles

### 🔍 Public Query Operations
- **Find Member** - Search for users by name
- **Find Department** - Search for organizational departments
- **Get Region** - Retrieve geographical region information

## 💡 Examples

### Creating a Record

```json
{
  "worksheetId": "your-worksheet-id",
  "fields": [
    {
      "id": "title_field",
      "value": "My New Record"
    },
    {
      "id": "email_field", 
      "value": "user@example.com"
    }
  ],
  "triggerWorkflow": true
}
```

### Batch Record Operations

```json
{
  "worksheetId": "your-worksheet-id",
  "rows": [
    {
      "fields": [
        {"id": "name", "value": "John Doe"},
        {"id": "email", "value": "john@example.com"}
      ]
    },
    {
      "fields": [
        {"id": "name", "value": "Jane Smith"},
        {"id": "email", "value": "jane@example.com"}
      ]
    }
  ]
}
```

### Advanced Filtering

```json
{
  "filter": {
    "type": "group",
    "logic": "AND",
    "children": [
      {
        "type": "condition",
        "field": "status",
        "operator": "eq",
        "value": "active"
      },
      {
        "type": "condition",
        "field": "created_date",
        "operator": "between",
        "value": ["2024-01-01", "2024-12-31"]
      }
    ]
  }
}
```

### Creating Option Sets

```json
{
  "name": "Priority Levels",
  "options": [
    {
      "value": "High",
      "index": 1,
      "color": "#F52222",
      "score": 3
    },
    {
      "value": "Medium", 
      "index": 2,
      "color": "#FAD714",
      "score": 2
    },
    {
      "value": "Low",
      "index": 3,
      "color": "#00C345", 
      "score": 1
    }
  ],
  "enableColor": true,
  "enableScore": true
}
```

## 🔗 API Compatibility

This node is built against **HAP API v3** with full compatibility for all endpoints. The implementation includes:

- **Authentication**: HAP-AppKey and HAP-Sign header authentication
- **Complete Coverage**: All 35 HAP API operations supported
- **Type Safety**: Full TypeScript implementation with proper error handling
- **Performance**: Optimized batch operations and pagination support
- **Validation**: Input validation and sanitization for all parameters

### Supported API Categories

| Category | Operations | Description |
|----------|------------|-------------|
| **Application** | 1 operation | App information and configuration |
| **Worksheet** | 4 operations | Table structure management |
| **Record** | 13 operations | Data CRUD with advanced features |
| **Workflow** | 3 operations | Process automation and triggers |
| **OptionSet** | 4 operations | Dropdown and selection management |
| **Role** | 7 operations | User permission and access control |
| **PublicQuery** | 3 operations | Search and lookup functionality |

## 🛠️ Development

### Prerequisites

- Node.js >= 20.15
- npm or yarn
- TypeScript knowledge recommended

### Setup

```bash
# Clone the repository
git clone https://github.com/mingdaocloud/n8n-nodes-hap.git
cd n8n-nodes-hap

# Install dependencies  
npm install

# Build the project
npm run build

# Run linter
npm run lint

# Auto-fix linting issues
npm run lintfix

# Development mode (watch for changes)
npm run dev
```

### Project Structure

```
n8n-nodes-hap/
├── nodes/
│   └── Hap/
│       ├── Hap.node.ts          # Main node definition
│       ├── HapOperations.ts     # Parameter configurations
│       ├── HapExecute.ts        # API execution logic
│       └── hap.svg              # Node icon
├── credentials/
│   └── HapApi.credentials.ts    # Authentication configuration
├── .dev_helper/
│   └── original_apis/           # OpenAPI 3.1 specifications
├── dist/                        # Compiled output
└── package.json                 # Package configuration
```

### Testing Locally

```bash
# Link the package globally
npm link

# In your n8n installation
npm link n8n-nodes-hap

# Start n8n
n8n start
```

## 📋 API Documentation

For detailed API documentation, refer to:
- **Official HAP API Docs**: [https://apidoc.mingdao.com/application/en](https://apidoc.mingdao.com/application/en)
- **Chinese Documentation**: [https://apidoc.mingdao.com/application](https://apidoc.mingdao.com/application)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow the existing code style and linting rules
- Add tests for new functionality
- Update documentation as needed
- Ensure all operations match HAP API specifications exactly

## 🐛 Support

For issues and support:

- **GitHub Issues**: [Report bugs and request features](https://github.com/mingdaocloud/n8n-nodes-hap/issues)
- **n8n Community**: [Join the discussion](https://community.n8n.io)
- **HAP Documentation**: [Official API docs](https://apidoc.mingdao.com/application/en)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏷️ Keywords

`n8n`, `hap`, `mingdao`, `nocoly`, `no-code`, `workflow`, `automation`, `api`, `integration`, `enterprise`

---

**Made with ❤️ by the HAP Community**

*This is an official community node for n8n, providing seamless integration with HAP (Hyper Application Platform) for building powerful no-code automation workflows.*
