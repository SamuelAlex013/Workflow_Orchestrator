# n8n-nodes-SmsManager

This is an n8n community node. It lets you use [SmsManager](https://smsmanager.com/) in your n8n workflows.

SmsManager is a service that allows you to send and receive SMS and WhatsApp messages.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The node supports the following operations:
*   **Send WhatsApp Text**: Sends a text message via WhatsApp.
*   **Send WhatsApp Template**: Sends a message based on a WhatsApp template.
*   **Send SMS**: Sends a standard SMS message.
*   **Trigger**: The trigger node receives webhook callbacks from smsmanager.com, handling batched webhooks.

## Credentials

To use this node, you need to authenticate with the SmsManager API.
1.  Sign up and get an API Key from [smsmanager.com](https://smsmanager.com/).
2.  In n8n, create new credentials for 'SmsManager API (Header)'.
3.  Enter your API Key in the 'API Key' field.

## Compatibility

This node is tested on n8n node API v1 and n8n version 1.91.3 without any errors

## Usage

This node provides both an action and a trigger.

### Action Node
The action node is used to send messages. It has a 'Callback Strategy' option:
*   **Manual URL**: Specify a URL where SmsManager should send the status of the message.
*   **Use "SmsManager Trigger"**: Use a trigger node in the same workflow to receive the status. Just enter the name of the trigger node.

### Trigger Node
The trigger node receives status updates for sent messages. It receives batched webhooks (as an array of 1-100 records) from SmsManager and emits one n8n item for each record in the batch.

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
*   [SmsManager API documentation](https://smsmanager.cz/api-json-v2/)
