![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-aitable-unofficial

This is an n8n community node. It lets you use AITable in your n8n workflows.

AITable is a powerful collaborative database platform that combines the flexibility of spreadsheets with the power of databases, allowing users to create custom views, forms, and dashboards.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

You can install this node in two ways:

### Using npm

```bash
npm install n8n-nodes-aitable-unofficial
```

For more information, follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Manual Installation

1. Go to Settings > Community Nodes
2. Select "Install"
3. Enter `n8n-nodes-aitable-unofficial` in the "npm package name" field
4. Click "Install"

## Operations

This node supports the following operations with AITable:

- **Get Node Details**: Retrieve detailed information about a specific node (datasheet, folder, form, dashboard, etc.)
- **Get Node List**: Retrieve a list of nodes with filtering options
- **Search Nodes**: Search for nodes based on specific criteria

## Credentials

To use this node, you need an AITable API token.

### Prerequisites:
1. Have an AITable account
2. Generate an API token in your AITable account settings

### Setting up credentials:
1. In n8n, go to **Credentials** and select **AITable API**
2. Enter your API token
3. Save the credentials

## Compatibility

This node has been tested with n8n v1.0+ and AITable API v1.

## Usage

### Getting Node Details

To retrieve details about a specific node in AITable:
1. Add the AITable node to your workflow
2. Select the "Get Node Details" operation
3. Provide the Space ID and Node ID
4. The node will return details including type, name, icon, and permissions

### Working with Different Node Types

AITable supports various node types:
- **Datasheet**: Spreadsheet-like data
- **Folder**: Collection of other nodes
- **Form**: Data collection forms
- **Dashboard**: Visual data representations
- **Mirror**: Alternative views of data

When working with these different types, be sure to check the "type" property in responses to handle the data appropriately.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [AITable API documentation](https://developers.aitable.ai/api/)
* [AITable Help Center](https://help.aitable.ai/)

## Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/texonica/n8n-aitable.git
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Build the node:
   ```bash
   pnpm build
   ```

### Releasing New Versions

To release a new version:

1. Update the code and commit your changes
2. Run one of the following commands depending on the type of change:
   ```bash
   # For bug fixes
   pnpm version:patch
   
   # For new features
   pnpm version:minor
   
   # For breaking changes
   pnpm version:major
   ```
3. Update the CHANGELOG.md file
4. Commit the version changes
5. Create a new GitHub release
6. Publish to npm:
   ```bash
   pnpm release
   ```

## License

[MIT](https://github.com/texonica/n8n-aitable/blob/master/LICENSE.md)
