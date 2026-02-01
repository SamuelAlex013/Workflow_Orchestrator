![Banner image](https://github.com/binalyze/n8n-nodes-binalyze-air/blob/main/assets/header-image.jpg)

# n8n-nodes-binalyze-air

This is an n8n community node that integrates with Binalyze AIR (Automated Incident Response) platform.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Supported Resources](#supported-resources)
  - [Acquisitions](#acquisitions)
  - [Assets](#assets)
  - [Baselines](#baselines)
  - [Cases](#cases)
  - [InterACT](#interact)
  - [Organizations](#organizations)
  - [Repositories](#repositories)
  - [Tasks](#tasks)
  - [Triage Rules](#triage-rules)
  - [Users](#users)
- [Trigger Node](#trigger-node)
  - [How to Use](#how-to-use)
  - [Supported Event Types](#supported-event-types)
  - [Event Data Structure](#event-data-structure)
- [Development](#development)
- [Testing](#testing)
- [TODO](#todo)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/) in the n8n community nodes documentation.

## Configuration

Before using this node, you need to configure your Binalyze AIR credentials:

### Step 1: Create AIR API Key

1. Go to AIR > Integrations > API Tokens > Add New
	* Provide a Token Name
	* Select an Organization
	* Select a Role
	* Define Expiration time
2. Click Save button, and copy the token as you will not be able to see it again
3. Click 'I got the token' button

### Step 2: Create AIR Credentials on your n8n instance

1. In n8n, go to Settings → Credentials
2. Add a new credential for "Binalyze AIR API"
3. Enter your AIR instance URL and API token

## Supported Resources

This node provides comprehensive coverage of Binalyze AIR's features listed below:

### Acquisitions
Manage evidence acquisition profiles and tasks.

**Operations:**
- `get` - Retrieve a specific acquisition profile
- `assignEvidenceTask` - Assign an evidence acquisition task by filter
- `assignImageTask` - Assign an image acquisition task by filter
- `createOffNetworkTask` - Create an off-network acquisition task

### Assets
Manage endpoints and their associated tasks, tags, and status.

**Operations:**
- `addTags` - Add tags to assets by filter
- `get` - Retrieve a specific asset
- `getAssetTasks` - Get tasks for a specific asset
- `getAll` - Retrieve many assets
- `reboot` - Assign reboot task to a specific asset (returns standardized response with success status, message, asset details, task, and error information)
- `removeTags` - Remove tags from assets by filter
- `setIsolation` - Assign isolation task to a specific asset (checks for existing tasks and current isolation status, returns standardized response)
- `shutdown` - Assign shutdown task to a specific asset (returns standardized response with success status, message, asset details, task, and error information)

### Baselines
Acquire and compare system baselines.

**Operations:**
- `acquireBaseline` - Acquire baseline for endpoints
- `compareBaseline` - Compare two baseline acquisition results from the same endpoint
- `getComparisonReport` - Get baseline comparison report

### Cases
Manage incident response cases, notes, and activities.

**Operations:**
- `changeOwner` - Change the owner of a case
- `checkName` - Check if a case name is available
- `closeCase` - Close a specific case
- `create` - Create a new case
- `get` - Retrieve a specific case
- `getActivities` - Get activities for a specific case
- `getEndpoints` - Get endpoints for a specific case
- `getAll` - Retrieve many cases
- `getTasks` - Get tasks for a specific case
- `getUsers` - Get users for a specific case

### InterACT
Execute commands and interact with endpoints remotely.

**Operations:**
- `createSession` - Create a new InterACT shell session for an asset
- `waitForSession` - Wait for an InterACT session to become live by monitoring task status (supports indefinite wait with timeout=0)
- `closeSession` - Close an InterACT session
- `executeCommand` - Execute a command in an InterACT session
- `executeAsyncCommand` - Execute an asynchronous command in an InterACT session
- `getCommandMessage` - Get the result of a command execution
- `interruptCommand` - Interrupt a running command

### Organizations
Manage organizations and their users.

**Operations:**
- `addTags` - Add tags to an organization
- `assignUser` - Assign a user to an organization
- `checkNameExists` - Check if an organization name already exists
- `create` - Create a new organization
- `get` - Retrieve a specific organization
- `getAll` - Retrieve many organizations
- `getUsers` - Retrieve users assigned to an organization
- `removeTags` - Remove tags from an organization
- `removeUser` - Remove a user from an organization
- `update` - Update an organization
- `updateShareableDeployment` - Update organization shareable deployment status

### Repositories
Manage evidence repositories.

**Operations:**
- `get` - Get a repository by name, ID, or from list selection
- `getAll` - Get many repositories with filtering options

### Tasks
Manage and monitor tasks and assignments.

**Operations:**
- `cancelTask` - Cancel a specific task
- `cancelTaskAssignment` - Cancel a specific task assignment
- `deleteTask` - Delete a specific task
- `deleteTaskAssignment` - Delete a specific task assignment
- `get` - Retrieve a specific task
- `getAll` - Retrieve many tasks
- `getTaskAssignments` - Retrieve assignments for a specific task
- `waitForCompletion` - Wait for a task to complete with polling

### Triage Rules
Create and manage triage rules for automated analysis.

**Operations:**
- `assignTask` - Assign a triage task
- `create` - Create a new triage rule
- `delete` - Delete a triage rule
- `get` - Retrieve a specific triage rule
- `getAll` - Retrieve many triage rules
- `update` - Update a triage rule
- `validate` - Validate a triage rule

### Users
Manage user accounts and permissions.

**Operations:**
- `getAll` - Retrieve many users
- `get` - Retrieve a specific user

## Trigger Node

The On AIR Event-Trigger node allows you to trigger workflows based on AIR events.

### How to Use

1. Add the On new AIR Trigger node to your workflow
2. Configure your AIR API credentials
3. Select the event types you want to listen for from the dynamically loaded list
4. Configure the Bearer token that AIR will use for webhook authentication
5. Copy the webhook URL from the node
6. Create an event subscription in AIR:
   - Go to AIR > Integrations > Event Subscriptions
   - Add a new subscription with the webhook URL
   - Select the same event types
   - Provide the same Bearer token you configured in the trigger node

### Supported Event Types

The trigger node dynamically loads available [event types](https://kb.binalyze.com/air/features/event-subscription) from your AIR instance, which may include:
- TaskProcessingCompletedEvent
- TaskProcessingFailedEvent
- TaskCompletedEvent
- TaskFailedEvent
- CaseClosedEvent
- EndpointRegisteredEvent
- ...  

### Event Data Structure

When an event is triggered, the node outputs data in the following format:
```json
{
  "eventName": "TaskCompletedEvent",
  "organizationId": 0,
  "data": {
    "id": "task-id",
    "name": "Task Name",
    "type": "Task Type",
    "organizationId": "org-id",
    "totalAssignedEndpoints": 5,
    "totalCompletedEndpoints": 4
  }
}
```

## Development

To set up the development environment:

1. Clone this repository
2. Install dependencies: `yarn install`
3. Build the project: `yarn build`
4. Link the project using: 
   - `npm link`
   - `npm link n8n-nodes-binalyze-air`
5. Start the development environment:
   - `yarn dev` - Start n8n in watch mode with automatic rebuilds
   - `yarn debug` - Start n8n in debug mode with verbose logging

### Development Scripts

- `yarn build` - Build the project
- `yarn dev` - Start development environment with file watching
- `yarn debug` - Start development environment with debug logging enabled
- `yarn restart:n8n` - Restart n8n without rebuilding

### Debug Mode

The `yarn debug` command enables comprehensive debug logging to help troubleshoot issues:

**Features:**
- **Verbose Logging**: Sets `N8N_LOG_LEVEL=debug` for detailed n8n logs
- **Console Output**: Direct log output to console (`N8N_LOG_OUTPUT=console`)
- **Debug Patterns**: Enables debug output for n8n core and community nodes (`DEBUG=n8n*,n8n-nodes-*`)
- **Error Details**: Shows detailed error information (`N8N_DETAILED_ERROR_OUTPUT=true`)
- **Development Mode**: Sets `NODE_ENV=development` for enhanced debugging

**Usage:**
```bash
# Start development with debug logging
yarn debug

# Or manually start debug mode
./scripts/dev-watch.sh --debug
./scripts/restart-n8n.sh --debug
```

**Debug Output Examples:**
```
16:38:21.490   debug   Loaded all credentials and nodes from n8n-nodes-binalyze-air { "credentials": 1, "nodes": 1 }
16:38:21.662   info    n8n ready on ::, port 5678
16:38:23.607   info    Version: 1.103.2
```

When debug mode is active, you'll see detailed information about:
- Node and credential loading
- API requests and responses
- Workflow execution steps
- Error stack traces
- Internal n8n operations

## Testing

The project includes an end-to-end testing workflow that can be managed using the e2e.js script.

### Prerequisites

1. Create a `.env.local.yml` file in the project root with your credentials:
   ```yaml
   # n8n instance configuration
   N8N:
     INSTANCE_URL: http://127.0.0.1:5678
     API_TOKEN: your_n8n_api_token_here
   ```

2. Ensure your n8n instance is running and you have a valid API token.

### Download Test Workflow

To download the test workflow from your n8n instance:
```bash
npm run test:download
# or
yarn test:download
```
Or using the Node.js script directly:
```bash
node test/e2e.js download
```

This will download the `n8n-nodes-binalyze-air-e2e` workflow and save it to `test/n8n-nodes-binalyze-air-e2e.json`.

### Command Options

Both commands support additional options:

```bash
# Use a custom n8n instance URL
node test/e2e.js download --url http://n8n.example.com:5678

# Use a custom workflow name
node test/e2e.js download --name my-custom-workflow

# Use a custom output file
node test/e2e.js download --file my-workflow.json
```


## TODO
- Add interACT Library related operations
- https://docs.google.com/document/d/1zK9XXgfZIB45i4bMrxWRmG5t8FaxwlQZIhDh8-qVmmc/edit?tab=t.0
