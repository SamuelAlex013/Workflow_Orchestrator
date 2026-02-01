# n8n-nodes-convex

n8n node for Convex database integration. This package provides a comprehensive n8n node that allows you to interact with Convex databases through queries, mutations, and actions.

## Features

- **Query Operations**: Read data from your Convex database
  - Get single documents by ID
  - List documents from tables
  - Execute custom query functions
- **Mutation Operations**: Write and modify data in your Convex database
  - Insert new documents
  - Update existing documents
  - Delete documents
  - Execute custom mutation functions
- **Action Operations**: Call external APIs and services through Convex actions
  - Execute custom action functions
- **Authentication**: Support for both public and authenticated functions using JWT tokens
- **Error Handling**: Built-in retry logic and comprehensive error handling
- **Type Safety**: Full TypeScript support with proper type definitions

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Installation

To use this node in your n8n instance:

1. Install via npm:
   ```bash
   npm install n8n-nodes-convex
   ```

2. Restart your n8n instance to load the new node.

## Configuration

### Credentials Setup

1. In n8n, go to **Credentials** and create new **Convex API** credentials
2. Enter your Convex deployment URL (e.g., `https://your-deployment.convex.cloud`)
3. Optionally, add an auth token (JWT) if you need to access authenticated functions

### Node Usage

1. Add the **Convex** node to your workflow
2. Select your credentials
3. Choose the resource type:
   - **Query**: For reading data
   - **Mutation**: For writing/modifying data
   - **Action**: For calling external APIs
4. Configure the specific operation and parameters

## Examples

### Query Examples

**Get Document by ID:**
- Resource: Query
- Operation: Get Document
- Table Name: `tasks`
- Document ID: `j97d2hx9x6s8nz9v4x5m6w7y8z`

**Custom Query:**
- Resource: Query  
- Operation: Custom Query
- Function Name: `api.tasks.listByUser`
- Arguments: `{"userId": "user123"}`

### Mutation Examples

**Insert Document:**
- Resource: Mutation
- Operation: Insert
- Table Name: `tasks`
- Document Data: `{"title": "New Task", "completed": false}`

**Custom Mutation:**
- Resource: Mutation
- Operation: Custom Mutation
- Function Name: `api.tasks.markComplete`
- Arguments: `{"taskId": "j97d2hx9x6s8nz9v4x5m6w7y8z"}`

### Action Examples

**Custom Action:**
- Resource: Action
- Operation: Custom Action
- Function Name: `api.notifications.sendEmail`
- Arguments: `{"to": "user@example.com", "subject": "Hello", "body": "Message"}`

## Advanced Options

The node includes several advanced configuration options:

- **Timeout**: Configure request timeout (default: 30 seconds)
- **Retry Count**: Set number of retry attempts on failure (default: 3)
- **Continue on Fail**: Handle errors gracefully without stopping the workflow

## Requirements

- Convex deployment with accessible functions
- n8n version 1.0.0 or higher
- Node.js 20+ (for development)

## Development

To contribute to this node:

1. Clone the repository
2. Install dependencies: `npm install`
3. Build the project: `npm run build`
4. Run linting: `npm run lint`

## Support

For issues and questions:
- [GitHub Issues](https://github.com/siddhardha99/n8n-nodes-convex/issues)
- [Convex Documentation](https://docs.convex.dev)
- [n8n Community](https://community.n8n.io)

## License

[MIT](LICENSE)
