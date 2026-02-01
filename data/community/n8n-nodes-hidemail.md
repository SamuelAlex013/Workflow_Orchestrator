# n8n-nodes-hidemail

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node for the [HideMail](https://hidemail.app) API. It lets you create and manage email aliases in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-hidemail` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in n8n.

## Credentials

You'll need to create credentials for the HideMail API:

1. Go to your [HideMail dashboard](https://hidemail.app/dashboard)
2. Navigate to **API Tokens** in the menu
3. Create a new API token
4. In n8n, create new credentials of type "HideMail API"
5. Enter your API token and the base URL (https://hidemail.app)

## Operations

The HideMail node supports the following operations:

### Aliases
- **Create**: Create a new email alias
- **Get All**: Retrieve all your aliases
- **Update**: Update an alias note
- **Activate**: Activate an alias
- **Deactivate**: Deactivate an alias

### Authentication
- **Create Token**: Create a new API token
- **Delete Token**: Delete an API token

### User
- **Get User**: Get current user information

### Domain Options
- **Get Domain Options**: Get available domain options

### Webhooks
- **Subscribe**: Set a webhook URL for email notifications
- **Unsubscribe**: Remove a webhook URL

## Compatibility

This node was built and tested with n8n version 1.0+.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [HideMail API documentation](https://hidemail.app/docs)
- [HideMail website](https://hidemail.app)
# Testing HideMail n8n Node Locally

This guide helps you set up and test the HideMail n8n node on your local macOS machine.

## Prerequisites

- macOS
- Node.js >=18.10
- npm >=7
- n8n installed globally or locally

## Setup Instructions

### 1. Install n8n (if not already installed)

```bash
npm install n8n -g
```

### 2. Install Node Dependencies

In the HideMail node directory:

```bash
npm install
```

### 3. Build the Node

```bash
npm run build
```

### 4. Link the Node to Local n8n

Run the provided setup script:

```bash
./scripts/setup-local-n8n.sh
```

### 5. Start n8n with Custom Node

```bash
n8n start --tunnel
```

## Testing the Node

1. Open n8n in your browser (typically at http://localhost:5678)
2. Create a new workflow
3. Search for "HideMail" in the node sidebar
4. Add the HideMail node to your workflow
5. Configure the node with your API credentials
6. Connect it to other nodes as needed
7. Execute the workflow to test

## Troubleshooting

- If the node doesn't appear in n8n, check the console logs for errors
- Ensure the node is properly built with `npm run build`
- Check that the node is correctly linked to your local n8n installation
- Verify your API credentials in the HideMail node settings

## Development

For development with auto-reloading:

```bash
npm run dev
```

This will watch for changes and rebuild automatically.

## Documentation

For more information about the HideMail API, visit [HideMail API Documentation](https://hidemail.app/developers).
## License

[MIT](https://github.com/georgedaneke/n8n-nodes-hidemail/blob/main/LICENSE.md)
