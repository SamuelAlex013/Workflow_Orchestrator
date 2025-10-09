# n8n-nodes-bitbucket-data-center

![Bitbucket Data Center](https://img.shields.io/badge/Bitbucket-Data%20Center-0052CC?style=flat&logo=bitbucket)
![n8n](https://img.shields.io/badge/n8n-community-FF6D5A?style=flat&logo=n8n)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

This is an n8n community node that allows you to interact with Bitbucket Data Center (Server) instances. It provides comprehensive operations for projects, repositories, pull requests (with full comment and review management), branches, commits, users, tags, files, and webhooks, as well as webhook triggers for real-time automation.

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
3. Enter `n8n-nodes-bitbucket-data-center`
4. Click **Install**

> **Note**: After publication to npm, it may take some time to appear in the n8n community registry.

### Option 2: Install via npm (self-hosted n8n)
```bash
npm install n8n-nodes-bitbucket-data-center
```

### Option 3: Docker Installation (Local Development)
```bash
# Install in a running n8n Docker container
docker exec -i your-n8n-container npm install n8n-nodes-bitbucket-data-center
docker restart your-n8n-container
```

### Option 4: Manual Installation
1. Navigate to your n8n installation directory
2. Run: `npm install n8n-nodes-bitbucket-data-center`
3. Restart n8n

## Features

### 🔐 Multiple Authentication Methods
- **Personal Access Tokens** (recommended)
- **Basic Authentication** (username/password)

### 📦 Comprehensive Operations
- **Projects**: Create, read, update, delete, and list projects
- **Repositories**: Full repository management including forking
- **Pull Requests**: Complete PR lifecycle management
- **Branches**: Branch creation and deletion
- **Commits**: Access commit information and history
- **Users**: User information and management

### 🎯 Smart UI Features
- **Dynamic Dropdowns**: Project and repository fields auto-populate from your Bitbucket instance
- **Real-time Validation**: Credential testing with proper authentication verification
- **Visual Icons**: Custom Bitbucket icons for all credentials and nodes

### ⚡ Real-time Triggers
- **25+ Webhook Events**: Comprehensive coverage of all Bitbucket Data Center events
- **Repository Events**: Push, create, delete, fork, modify, comment events  
- **Pull Request Events**: Complete PR lifecycle, reviews, comments
- **Branch & Tag Events**: Creation and deletion tracking
- **Mirror Events**: Data Center specific synchronization events
- **Smart Event Filtering**: Clean, categorized event selection

### 🌐 Data Center Specific Features
- **Configurable Server URLs**: Works with any Bitbucket Data Center instance
- **Project Key Support**: Uses Data Center's project-based structure
- **REST API v1.0**: Native Data Center API support

## Authentication

### Personal Access Token (Recommended)

1. In your Bitbucket Data Center instance:
   - Go to **Profile picture** → **Manage account** → **Personal access tokens**
   - Click **Create token**
   - Set appropriate permissions based on your needs
   - Copy the generated token

2. In n8n:
   - Create a new credential of type "Bitbucket Data Center API"
   - Enter your server URL (e.g., `https://bitbucket.example.com`)
   - Paste your Personal Access Token

### Basic Authentication

1. In n8n:
   - Create a new credential of type "Bitbucket Data Center Basic Auth"
   - Enter your server URL (e.g., `https://bitbucket.example.com`)
   - Enter your Bitbucket username
   - Enter your password or Personal Access Token

## Operations

All operations now feature **smart dropdowns** that automatically populate with data from your Bitbucket Data Center instance, making configuration faster and error-free. With **45+ operations** across 10 resource types, this node provides complete Bitbucket Data Center API coverage.

### Projects

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List all projects | - |
| **Get** | Get a specific project | Project (dropdown) |
| **Create** | Create a new project | Project Key, Name |
| **Update** | Update project details | Project (dropdown), Name |
| **Delete** | Delete a project | Project (dropdown) |

### Repositories

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List repositories in a project | Project (dropdown) |
| **Get** | Get a specific repository | Project (dropdown), Repository (dropdown) |
| **Create** | Create a new repository | Project (dropdown), Name |
| **Update** | Update repository details | Project (dropdown), Repository (dropdown), Name |
| **Delete** | Delete a repository | Project (dropdown), Repository (dropdown) |
| **Fork** | Fork a repository | Project (dropdown), Repository (dropdown) |

### Pull Requests

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List pull requests | Project (dropdown), Repository (dropdown) |
| **Get** | Get a specific pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Create** | Create a new pull request | Project (dropdown), Repository (dropdown), Title, From Branch, To Branch |
| **Update** | Update pull request | Project (dropdown), Repository (dropdown), PR ID, Title |
| **Merge** | Merge a pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Decline** | Decline a pull request | Project (dropdown), Repository (dropdown), PR ID |

#### Pull Request Comments
| **Add Comment** | Add a comment to a pull request | Project (dropdown), Repository (dropdown), PR ID, Comment Text |
| **Get All Comments** | Get all comments for a pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Update Comment** | Update a pull request comment | Project (dropdown), Repository (dropdown), PR ID, Comment ID, Comment Text |
| **Delete Comment** | Delete a pull request comment | Project (dropdown), Repository (dropdown), PR ID, Comment ID |

#### Pull Request Reviews
| **Approve** | Approve a pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Unapprove** | Remove approval from a pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Needs Work** | Mark a pull request as needing work | Project (dropdown), Repository (dropdown), PR ID |
| **Add Reviewer** | Add a reviewer to a pull request | Project (dropdown), Repository (dropdown), PR ID, Username |
| **Remove Reviewer** | Remove a reviewer from a pull request | Project (dropdown), Repository (dropdown), PR ID, Username |

#### Pull Request Information
| **Get Activities** | Get all activities for a pull request | Project (dropdown), Repository (dropdown), PR ID |
| **Get Participants** | Get all participants for a pull request | Project (dropdown), Repository (dropdown), PR ID |

### Branches

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List all branches | Project (dropdown), Repository (dropdown) |
| **Create** | Create a new branch | Project (dropdown), Repository (dropdown), Name, Start Point |
| **Delete** | Delete a branch | Project (dropdown), Repository (dropdown), Name |

### Commits

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List commits | Project (dropdown), Repository (dropdown) |
| **Get** | Get a specific commit | Project (dropdown), Repository (dropdown), Commit ID |

### Users

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get** | Get user information | Username (optional - defaults to current user) |
| **Get All** | List all users | - |

### Tags

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List all tags | Project (dropdown), Repository (dropdown) |
| **Create** | Create a new tag | Project (dropdown), Repository (dropdown), Tag Name, Start Point |
| **Delete** | Delete a tag | Project (dropdown), Repository (dropdown), Tag Name |

### Files

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get** | Get file content | Project (dropdown), Repository (dropdown), File Path |
| **Get All** | List files in a directory | Project (dropdown), Repository (dropdown), Directory Path (optional) |
| **Create** | Create or update a file | Project (dropdown), Repository (dropdown), File Path, File Content, Commit Message |

### Webhooks

| Operation | Description | Required Parameters |
|-----------|-------------|-------------------|
| **Get All** | List all webhooks | Project (dropdown), Repository (dropdown) |
| **Create** | Create a new webhook | Project (dropdown), Repository (dropdown), Webhook URL, Events |
| **Update** | Update an existing webhook | Project (dropdown), Repository (dropdown), Webhook ID, Webhook URL, Events |
| **Delete** | Delete a webhook | Project (dropdown), Repository (dropdown), Webhook ID |

## Triggers

The Bitbucket Data Center Trigger node supports **25+ webhook events** with smart dropdowns for project and repository selection. The trigger automatically registers and manages webhooks in your Bitbucket Data Center instance.

### Repository Events
- `repo:refs_changed` - Repository Push (Code Changes) - *Most common*
- `repo:created` - Repository Created
- `repo:deleted` - Repository Deleted  
- `repo:forked` - Repository Forked
- `repo:modified` - Repository Modified (settings changed)

### Pull Request Lifecycle Events
- `pr:opened` - Pull Request Opened
- `pr:modified` - Pull Request Modified (title/description)
- `pr:merged` - Pull Request Merged
- `pr:declined` - Pull Request Declined
- `pr:deleted` - Pull Request Deleted
- `pr:from_ref_updated` - Pull Request Source Branch Updated

### Pull Request Review Events  
- `pr:reviewer:approved` - Pull Request Approved
- `pr:reviewer:unapproved` - Pull Request Approval Removed
- `pr:reviewer:needs_work` - Pull Request Marked as Needs Work
- `pr:reviewer:added` - Pull Request Reviewer Added
- `pr:reviewer:removed` - Pull Request Reviewer Removed

### Comment Events
- `pr:comment:added` - Pull Request Comment Added
- `pr:comment:edited` - Pull Request Comment Edited
- `pr:comment:deleted` - Pull Request Comment Deleted
- `repo:comment:added` - Commit Comment Added
- `repo:comment:edited` - Commit Comment Edited
- `repo:comment:deleted` - Commit Comment Deleted

### Branch Events
- `repo:branch:created` - Branch Created
- `repo:branch:deleted` - Branch Deleted

### Tag Events
- `repo:tag:created` - Tag Created
- `repo:tag:deleted` - Tag Deleted

### Mirror Events (Data Center Specific)
- `mirror:repo_synchronization_started` - Mirror Synchronization Started
- `mirror:repo_synchronization_finished` - Mirror Synchronization Finished
- `mirror:repo_synchronization_failed` - Mirror Synchronization Failed

## Configuration

### Server URL Format
Your Bitbucket Data Center server URL should be in the format:
```
https://your-bitbucket-server.com
```

Do not include API paths like `/rest/api/1.0/` - the node handles this automatically.

### Smart Dropdowns
The node features intelligent dropdowns that automatically fetch and populate:
- **Projects**: Shows all projects you have access to
- **Repositories**: Dynamically loads repositories based on selected project
- **Real-time Loading**: Updates instantly when you change project selection

No more manual typing of project keys or repository slugs!

### Permissions Required

For Personal Access Tokens, ensure the following permissions are granted based on your use case:

- **Project Read/Write**: For project operations
- **Repository Read/Write**: For repository operations
- **Pull Request Read/Write**: For PR operations
- **Repository Admin**: For branch operations and webhook management

## Examples

### Example 1: Get All Repositories in a Project

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "repository", 
        "operation": "getAll",
        "projectKey": "MYPROJ",
        "returnAll": true
      },
      "type": "n8n-nodes-bitbucket-data-center.bitbucketDataCenter",
      "typeVersion": 1,
      "position": [300, 300],
      "name": "Get All Repos"
    }
  ]
}
```

> **Note**: When using the UI, the `projectKey` parameter becomes a smart dropdown that shows all available projects.

### Example 2: Create a Pull Request

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "pullRequest",
        "operation": "create",
        "projectKey": "MYPROJ",
        "repositorySlug": "my-repo",
        "title": "Feature: Add new functionality",
        "fromRef": "feature/new-functionality",
        "toRef": "main"
      },
      "type": "n8n-nodes-bitbucket-data-center.bitbucketDataCenter",
      "typeVersion": 1,
      "position": [500, 300],
      "name": "Create Pull Request"
    }
  ]
}
```

### Example 3: Webhook Trigger for Repository Push

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "accessToken",
        "projectKey": "MYPROJ",
        "repositorySlug": "my-repo", 
        "events": ["repo:refs_changed"]
      },
      "type": "n8n-nodes-bitbucket-data-center.bitbucketDataCenterTrigger",
      "typeVersion": 4,
      "position": [100, 300],
      "name": "On Repository Push"
    }
  ]
}
```

> **Note**: The trigger now uses separate `projectKey` and `repositorySlug` parameters with smart dropdowns instead of a single `repository` parameter.

## Development

### Prerequisites
- Node.js 18.10.0 or higher
- pnpm 9.1.0 or higher
- n8n development environment

### Setup
```bash
# Clone the repository
git clone https://github.com/sine-ai/n8n-nodes-bitbucket-data-center.git

# Install dependencies
pnpm install

# Build the project
pnpm build

# Run linting
pnpm lint

# Fix linting issues
pnpm lintfix
```

### Project Structure
```
n8n-nodes-bitbucket-data-center/
├── credentials/
│   ├── BitbucketDataCenterApi.credentials.ts
│   └── BitbucketDataCenterBasicAuth.credentials.ts
├── nodes/
│   └── BitbucketDataCenter/
│       ├── BitbucketDataCenter.node.ts
│       ├── BitbucketDataCenterTrigger.node.ts
│       └── bitbucket.svg
├── dist/                          # Compiled JavaScript
├── package.json
├── tsconfig.json
├── .eslintrc.js
└── README.md
```

### Testing
Test your node in a local n8n instance:

1. Install in development mode:
   ```bash
   npm link
   cd path/to/n8n
   npm link n8n-nodes-bitbucket-data-center
   ```

2. Restart n8n and test the nodes

## API Differences from Bitbucket Cloud

This node is specifically designed for Bitbucket Data Center and differs from Bitbucket Cloud in several ways:

| Feature | Bitbucket Cloud | Bitbucket Data Center |
|---------|----------------|----------------------|
| **API Version** | v2.0 | v1.0 |
| **Base URL** | `api.bitbucket.org` | Configurable server |
| **Authentication** | OAuth2, App Passwords | Personal Access Tokens, Basic Auth |
| **Organization** | Workspaces | Projects with Keys |
| **Repository URL** | `/repositories/{workspace}/{repo}` | `/projects/{key}/repos/{slug}` |
| **Issues** | Native support | External (Jira integration) |
| **Webhooks** | Different event names | Data Center specific events |

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify your server URL is correct and accessible (e.g., `https://bitbucket.company.com:7990`)
   - Ensure your Personal Access Token has sufficient permissions
   - Check that your Bitbucket Data Center instance allows API access
   - Test credentials using the built-in "Test" button in n8n credential configuration

2. **Webhook Not Triggering**
   - Verify n8n is accessible from your Bitbucket Data Center instance
   - Check webhook configuration in Bitbucket (webhooks are auto-created/deleted)
   - Ensure selected events match your trigger configuration
   - Use separate project and repository dropdowns (not the old combined format)
   - Check n8n logs for webhook registration errors

3. **API Rate Limiting**
   - Implement delays between requests for bulk operations
   - Use pagination parameters to limit result sets
   - Contact your Bitbucket administrator about rate limits

4. **SSL/TLS Issues**
   - Ensure your Bitbucket Data Center instance has valid SSL certificates
   - Check n8n's SSL configuration if using self-signed certificates

5. **Dropdowns Not Loading**
   - Verify your credentials are correctly configured and tested
   - Ensure your PAT has at least "Project Read" permissions
   - Check that your Bitbucket Data Center instance is accessible from n8n
   - Try refreshing the node or creating a new one

### Getting Help

- Check the [n8n community forum](https://community.n8n.io/)
- Review [Bitbucket Data Center REST API documentation](https://developer.atlassian.com/server/bitbucket/rest/v900/intro/)
- Open an issue on this repository's GitHub page

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed
- Ensure all linting checks pass

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [n8n](https://n8n.io/) for the amazing automation platform
- [Atlassian](https://atlassian.com/) for Bitbucket Data Center
- The n8n community for inspiration and support

---

**Note**: This is a community-maintained node and is not officially supported by n8n or Atlassian. For commercial support, please consider reaching out to the maintainers or the broader n8n community.
