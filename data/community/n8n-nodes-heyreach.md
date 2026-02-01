# n8n-nodes-heyreach

This is an n8n community node that lets you use [HeyReach](https://heyreach.io) in your n8n workflows.

HeyReach is a LinkedIn automation platform that helps you scale your outreach campaigns, manage leads, and track performance metrics.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-heyreach` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in your n8n workflows.

## Configuration

You'll need to configure your HeyReach API credentials:

1. In n8n, go to **Settings > Credentials**.
2. Select **Create New** and choose **HeyReach API**.
3. Enter your HeyReach API key (found in your HeyReach account settings).
4. Save the credentials.

## Nodes

This package contains two nodes:

### HeyReach
The main operations node that allows you to:
- **Campaigns**: Get, pause, resume campaigns, add/get leads
- **Leads**: Get lead details, manage tags
- **Lists**: Manage lead lists
- **Inbox**: Send messages, get conversations
- **LinkedIn Accounts**: Manage connected accounts
- **Stats**: Get campaign statistics
- **Webhooks**: Manage webhook subscriptions

### HeyReach Trigger
A trigger node that listens for webhook events from HeyReach:
- Connection requests sent/accepted
- Messages sent/replies received
- InMail sent/replies received
- Profile views and post likes
- Campaign completions
- Lead tag updates

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [HeyReach API Documentation](https://docs.heyreach.io)

## Development

To set up the development environment:

```bash
npm install
npm run dev
```

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
