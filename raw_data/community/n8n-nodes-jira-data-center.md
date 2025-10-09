# n8n-nodes-jira-data-center

![Jira Data Center](https://img.shields.io/badge/Jira-Data%20Center-0052CC?style=flat&logo=jira)
![n8n](https://img.shields.io/badge/n8n-community-FF6D5A?style=flat&logo=n8n)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This is an n8n community node that allows you to interact with Jira Data Center (Server) instances. It provides comprehensive operations for projects, issues, users, and more, as well as webhook triggers for real-time automation.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Authentication](#authentication)
- [Operations](#operations)
- [Triggers](#triggers)
- [Configuration](#configuration)
- [Examples](#examples)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow the [n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) for installing community nodes.

### Option 1: Install via n8n Editor UI
1. Go to **Settings > Community Nodes**
2. Select **Install a community node**
3. Enter `n8n-nodes-jira-data-center`
4. Click **Install**

### Option 2: Install via npm (self-hosted n8n)
```bash
npm install n8n-nodes-jira-data-center
```

### Option 3: Docker Installation
```bash
# Install in a running n8n Docker container
docker exec -i your-n8n-container npm install n8n-nodes-jira-data-center
docker restart your-n8n-container
```

### Option 4: Manual Installation
1. Navigate to your n8n installation directory
2. Run: `npm install n8n-nodes-jira-data-center`
3. Restart n8n

## Features

### 🔐 Multiple Authentication Methods
- **Personal Access Tokens** (recommended)
- **Basic Authentication** (username/password)

### 📦 Comprehensive Operations
- **Projects**: Create, read, update, and list projects
- **Issues**: Full issue lifecycle management
- **Comments**: Issue comment management
- **Users**: User information and management
- **Workflows**: Workflow and status management

### 🎯 Smart UI Features
- **Dynamic Dropdowns**: Project and issue type fields auto-populate from your Jira instance
- **Real-time Validation**: Credential testing with proper authentication verification
- **Visual Icons**: Custom Jira icons for all credentials and nodes

### ⚡ Real-time Triggers
- **Issue Events**: Created, updated, deleted, assigned
- **Comment Events**: Added, updated, deleted
- **Project Events**: Created, updated, deleted
- **Workflow Events**: Status transitions and workflow changes

### 🌐 Data Center Specific Features
- **Configurable Server URLs**: Works with any Jira Data Center instance
- **Project Key Support**: Uses Data Center's project-based structure
- **REST API v2**: Native Data Center API support

## Authentication

### Personal Access Token (Recommended)

1. In your Jira Data Center instance:
   - Go to **Profile picture** → **Personal Settings** → **Personal Access Tokens**
   - Click **Create token**
   - Set appropriate permissions based on your needs
   - Copy the generated token

2. In n8n:
   - Create a new credential of type "Jira Data Center API"
   - Enter your server URL (e.g., `https://jira.example.com`)
   - Paste your Personal Access Token

### Basic Authentication

1. In n8n:
   - Create a new credential of type "Jira Data Center Basic Auth"
   - Enter your server URL (e.g., `https://jira.example.com`)
   - Enter your Jira username
   - Enter your password or Personal Access Token

## Operations

All operations feature **smart dropdowns** that automatically populate with data from your Jira Data Center instance.

### Projects

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List all projects | - |
| **Get** | Get a specific project | Project (dropdown) |
| **Create** | Create a new project | Project Key, Name, Lead |
| **Update** | Update project details | Project (dropdown), Name |

### Issues

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List issues in a project | Project (dropdown) |
| **Get** | Get a specific issue | Issue Key |
| **Create** | Create a new issue | Project (dropdown), Issue Type, Summary |
| **Update** | Update issue details | Issue Key, Fields to Update |
| **Delete** | Delete an issue | Issue Key |
| **Assign** | Assign issue to user | Issue Key, Assignee |

### Comments

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List comments on an issue | Issue Key |
| **Add** | Add comment to issue | Issue Key, Comment Body |
| **Update** | Update a comment | Comment ID, New Body |
| **Delete** | Delete a comment | Comment ID |

### Users

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get** | Get user information | Username (optional - defaults to current user) |
| **Get All** | List all users | - |
| **Search** | Search for users | Query String |

## Triggers

The Jira Data Center Trigger node supports webhook events for real-time automation.

### Issue Events
- `jira:issue_created` - Issue Created
- `jira:issue_updated` - Issue Updated
- `jira:issue_deleted` - Issue Deleted

### Comment Events
- `comment_created` - Comment Added to Issue
- `comment_updated` - Comment Updated
- `comment_deleted` - Comment Deleted

### Project Events
- `project_created` - Project Created
- `project_updated` - Project Updated
- `project_deleted` - Project Deleted

## Configuration

### Server URL Format
Your Jira Data Center server URL should be in the format:
```
https://your-jira-server.com
```

Do not include API paths like `/rest/api/2/` - the node handles this automatically.

### Permissions Required

For Personal Access Tokens, ensure the following permissions are granted:
- **Browse Projects**: For project operations
- **Create Issues**: For issue creation
- **Edit Issues**: For issue updates
- **Add Comments**: For comment operations
- **System Admin**: For webhook management (triggers)

## Examples

### Example 1: Create an Issue

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "issue",
        "operation": "create",
        "projectKey": "TEST",
        "issueType": "Bug",
        "summary": "Sample bug report",
        "description": "This is a test issue created via n8n"
      },
      "type": "n8n-nodes-jira-data-center.jiraDataCenter",
      "typeVersion": 1,
      "position": [300, 300],
      "name": "Create Jira Issue"
    }
  ]
}
```

### Example 2: Get All Issues in Project

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "issue",
        "operation": "getAll",
        "projectKey": "TEST",
        "returnAll": true
      },
      "type": "n8n-nodes-jira-data-center.jiraDataCenter",
      "typeVersion": 1,
      "position": [500, 300],
      "name": "Get All Issues"
    }
  ]
}
```

### Example 3: Webhook Trigger for Issue Events

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "projectKey": "TEST",
        "events": ["jira:issue_created", "jira:issue_updated"]
      },
      "type": "n8n-nodes-jira-data-center.jiraDataCenterTrigger",
      "typeVersion": 1,
      "position": [100, 300],
      "name": "On Issue Events"
    }
  ]
}
```

## Development

### Prerequisites
- Node.js 18.10.0 or higher
- npm or pnpm
- n8n development environment

### Setup
```bash
# Clone the repository
git clone https://github.com/sine-ai/n8n-nodes-jira-data-center.git

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint
```

### Project Structure
```
n8n-nodes-jira-data-center/
├── credentials/
│   ├── JiraDataCenterApi.credentials.ts
│   └── JiraDataCenterBasicAuth.credentials.ts
├── nodes/
│   └── JiraDataCenter/
│       ├── JiraDataCenter.node.ts
│       ├── JiraDataCenterTrigger.node.ts
│       └── jira.svg
├── dist/                          # Compiled JavaScript
├── package.json
├── tsconfig.json
└── README.md
```

## Docker Management

For easy local development and testing, this project includes Docker Compose configuration:

### Quick Setup
1. **Copy management template:**
   ```bash
   cp n8n-management.template.md n8n-management.md
   ```
2. **Update paths in your local copy**
3. **Start n8n with both Jira and Bitbucket Data Center nodes:**
   ```bash
   docker-compose up -d
   ```

### Management Commands
- **Start:** `docker-compose up -d`
- **Stop:** `docker-compose down`  
- **Restart:** `docker-compose restart`
- **Logs:** `docker-compose logs -f n8n`
- **Access:** http://localhost

The `n8n-management.md` file is gitignored to keep personal paths private.

## API Differences from Jira Cloud

This node is specifically designed for Jira Data Center and differs from Jira Cloud:

| Feature | Jira Cloud | Jira Data Center |
|---------|------------|------------------|
| **API Version** | v3 | v2 |
| **Base URL** | `api.atlassian.com` | Configurable server |
| **Authentication** | OAuth2, API tokens | Personal Access Tokens, Basic Auth |
| **Projects** | Cloud-based | Server-based with keys |
| **Webhooks** | Different registration | Data Center webhook system |

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [n8n](https://n8n.io/) for the amazing automation platform
- [Atlassian](https://atlassian.com/) for Jira Data Center
- The n8n community for inspiration and support

---

**Note**: This is a community-maintained node and is not officially supported by n8n or Atlassian.