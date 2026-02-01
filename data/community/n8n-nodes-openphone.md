# n8n-nodes-openphone

This is an n8n community node that provides OpenPhone integration for n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[OpenPhone](https://www.openphone.com) is a business phone system built for teams.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### In n8n

1. Go to **Settings > Community Nodes**
2. Select **Install a community node**
3. Enter `n8n-nodes-openphone`
4. Select **Install**

### Manual installation

To install this node manually in a local n8n instance:

```bash
npm install n8n-nodes-openphone
```

## Operations

### OpenPhone Node

The OpenPhone node supports the following operations:

#### Messages
- **Send** - Send SMS/MMS messages
- **Get** - Retrieve a specific message
- **List** - List all messages

#### Contacts
- **Create** - Create a new contact
- **Get** - Retrieve a contact
- **Update** - Update contact information
- **List** - List all contacts

#### Webhooks
- **Create** - Create a webhook subscription
- **Delete** - Remove a webhook
- **List** - List all webhooks

### OpenPhone Trigger Node

The OpenPhone Trigger node listens for real-time events:

- Message received
- Message delivered
- Message updated
- Call started
- Call completed
- Call recording ready
- Contact created
- Contact updated

## Credentials

You'll need an OpenPhone API key to use this node:

1. Log into your OpenPhone account
2. Go to Workspace Settings → API
3. Click "Generate API Key"
4. Enter a label for your key
5. Copy the API key and save it securely

In n8n:
1. Go to Credentials
2. Create new "OpenPhone API" credential
3. Paste your API key

## Usage Example

### Send SMS Workflow

1. Add an OpenPhone node to your workflow
2. Select "Message" resource and "Send" operation
3. Configure:
   - **To**: Recipient phone number
   - **From**: Your OpenPhone number
   - **Message**: Your message text
4. Connect your OpenPhone credentials

### Webhook Trigger Example

1. Add an OpenPhone Trigger node
2. Select events to listen for (e.g., "Message Received")
3. Configure optional filters
4. The webhook URL will be automatically registered with OpenPhone

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [OpenPhone API documentation](https://www.openphone.com/docs/mdx/api-reference/introduction)
- [OpenPhone Developer Portal](https://www.openphone.com/product/api)

## License

[MIT](https://github.com/treymcmeans/n8n-nodes-openphone/blob/master/LICENSE.md)