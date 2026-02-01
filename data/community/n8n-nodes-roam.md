# n8n-nodes-roam

This is an n8n community node. It lets you use Roam in your n8n workflows.

Roam is a video conferencing and messaging platform that enables teams to connect, collaborate, and communicate effectively through video meetings, messaging, and integrations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Roam Node
- **Send Message**: Send messages to Roam groups
- **Create Meeting Link**: Create new video meeting links

### Roam Trigger Node
- **Webhook Events**: Trigger workflows when webhook events are received from Roam

## Credentials

To use this node, you need to authenticate with Roam's API using OAuth2.

1. Go to your Roam developer account at [developer.ro.am](https://developer.ro.am)
2. Create an OAuth2 application
3. Configure the redirect URI for n8n (usually `https://your-n8n-instance.com/rest/oauth2-credential/callback`)
4. Copy the Client ID and Client Secret
5. In n8n, create a new credential of type "Roam OAuth2 API"
6. Fill in your Client ID, Client Secret, and configure the OAuth2 flow

## Compatibility

- n8n version: 1.0.0+
- Node.js version: 18.0.0+
- Tested with n8n versions: 1.0.x, 1.1.x

## Usage

### Basic Setup
1. Install the community node
2. Set up your Roam OAuth2 credentials
3. Use the Roam node to send messages or create meetings
4. Use the Roam Trigger node to respond to webhook events

### Example Workflow
1. **Trigger**: HTTP Request (when a form is submitted)
2. **Action**: Roam - Send Message (notify team about the submission)
3. **Action**: Roam - Create Meeting Link (schedule a follow-up meeting)

## Development

To run n8n locally: 

- Run `ngrok http 5678` to support incoming webhooks. Set `WEBHOOK_URL` to the ngrok URL.
- Run `npm run dev`

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Roam API Documentation](https://developer.ro.am/)
* [Roam Developer Portal](https://developer.ro.am)

## Version history

### 0.1.1
- Initial release
- Roam node with meeting and messaging operations
- Roam Trigger node for webhook events
- Basic transport layer for API communication
- OAuth2 authentication
