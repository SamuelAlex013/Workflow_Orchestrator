![Banner image](https://go.alive5.com/images/alive5-banner-1584x396.png)

# n8n-nodes-alive5

This is an n8n community node for sending SMS messages via the Alive5 API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow these steps to install this community node in your n8n instance:

1. Open n8n.
2. Go to **Settings** > **Community Nodes**.
3. Click **Install Community Node**.
4. Enter the name of this package: `n8n-nodes-raia`
5. Click **Install**.

For more details, see the [official n8n documentation](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/).

## Operations

- **Send SMS**
  - Send SMS messages via Alive5 API
  - Dynamically select a Channel with a valid phone number
  - Dynamically select a User (Admin or Agent) from the selected Channel

## Credentials

The node requires the following credentials:

- **Alive5 API**
  - API Key: Your Alive5 API key
  - API Base URL: The base URL for the Alive5 API (default: https://api.alive5.com/public/1.1)
  - To obtain an Alive5 SMS account and API key, please contact us at support@alive5.com, view our website at https://www.alive5.com, or book a demo at https://demo.alive5.com

## Compatibility

This node has been tested with n8n version 1.0.0 and above.

## Usage

### Send SMS

This operation allows you to send SMS messages using the Alive5 API.

#### Parameters

- **From phone Number**
  - The phone number to send the SMS from (e.g., +1234567890)
- **To phone number**
  - The phone number to send the SMS to (e.g., +1234567890)
- **Message**
  - The text message to send
- **Channel**
  - Dynamically select a Channel with a valid phone number
- **User**
  - Dynamically select a User (Admin or Agent) from the selected Channel

#### Example

```json
{
	"nodes": [
		{
			"parameters": {
				"fromPhoneNumber": "+1234567890",
				"toPhoneNumber": "+1234567890",
				"message": "Hello from n8n!",
				"channel": "Channel Name",
				"agent": "Agent Name"
			},
			"name": "Send SMS",
			"type": "n8n-nodes-alive5.SendSMS",
			"typeVersion": 1,
			"position": [300, 300]
		}
	],
	"connections": {}
}
```

1. Add the Alive5 node to your workflow.
2. Configure the Alive5 API credentials with your API key.
3. Set the required parameters:
   - **From phone number**: Your sender phone number.
   - **To phone number**: Recipient's phone number.
   - **Message**: Your SMS message.
   - **Channel**: Select a Channel with a valid phone number.
   - **User**: Select a User (Admin or Agent) from the selected Channel.
4. Execute the workflow to send the SMS.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Alive5 API Documentation](https://support.alive5.com/public-api-overview)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
