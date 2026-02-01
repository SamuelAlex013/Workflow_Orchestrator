# n8n-nodes-nqdev

This is an n8n community node. It lets you use eSMS.vn in your n8n workflows.

eSMS.vn is a messaging service that allows you to send SMS, Zalo, or Viber messages for marketing campaigns, customer care, or OTP verification directly through its API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials) <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage) <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history) <!-- delete if not using this section -->

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The `n8n-nodes-nqdev` node supports the following operations:

- **Send SMS**: Send text messages to one or multiple recipients.
- **Send Zalo Message**: Send messages via Zalo for notifications or marketing.
- **Send Viber Message**: Send messages via Viber for promotional or customer care purposes.
- **Send OTP**: Generate and send one-time passwords (OTP) for verification.

Each operation allows customization such as recipient phone numbers, message content, and sender ID (if supported by eSMS.vn).

## Credentials

To use this node, you need to authenticate with eSMS.vn using an API key. Follow these steps to set up your credentials:

1. **Prerequisites:**
   - Sign up for an account at [eSMS.vn](https://esms.vn/).
   - Obtain your API key from the eSMS.vn developer dashboard (refer to the [eSMS.vn API documentation](http://developers.esms.vn/)).
2. **Setup in n8n:**
   - In n8n, go to the Credentials section and click "Add Credential."
   - Select "eSMS.vn API" (or the name you’ve defined for this node’s credential type).
   - Enter your API key in the provided field.
   - Save the credential and connect it to the `n8n-nodes-nqdev` node in your workflow.

No additional authentication methods are required beyond the API key.

## Compatibility

- **Minimum n8n version**: Tested with n8n version 0.200.0 and above.
- **Tested versions**: Compatible with n8n versions up to the latest release as of March 19, 2025.
- **Known issues**: No known version incompatibilities at this time.

## Usage

This node is straightforward to use once credentials are set up. Here’s a quick guide to get started:

1. Add the `eSMS.vn` node to your workflow.
   ![Adding eSMS.vn node](docs/images/image1.png)
   [Placeholder for Image 1: Screenshot of adding the eSMS.vn node to a workflow]
2. Select an operation (e.g., "Send SMS").
   [Placeholder for Image 2: Screenshot of selecting the "Send SMS" operation in the node settings]
3. Connect your eSMS.vn API credentials.
   [Placeholder for Image 3: Screenshot of the credential selection dropdown with eSMS.vn API highlighted]
4. Configure the node by entering the recipient’s phone number(s), message content, and any optional parameters (e.g., sender ID).
   [Placeholder for Image 4: Screenshot of the node configuration panel with sample inputs like phone number and message text]
5. Execute the workflow to send your message.
   [Placeholder for Image 5: Screenshot of a completed workflow with a success message or output log]

For new n8n users, check out the [Try it out](https://docs.n8n.io/try-it-out/) documentation to learn the basics of building workflows.

**Tip:** If you encounter errors, double-check your API key and ensure your eSMS.vn account has sufficient credits for sending messages.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [eSMS.vn API documentation](http://developers.esms.vn/)

## Version history

- **0.1.0** (_Initial Release_)
  - Released on March 19, 2025.
  - First version of `n8n-nodes-nqdev`.
  - Supports sending SMS, Zalo, and Viber messages, as well as OTP generation via the eSMS.vn API.
  - Basic integration with n8n workflows, including credential setup using an API key.
- **0.1.1**
  - Released on March 25, 2025 (placeholder date).
  - Fixed integration bugs to improve stability and reliability with the eSMS.vn API.
- **0.2.0**
  - Released on April 1, 2025 (placeholder date).
  - Added support for sending SMS messages with brandname (sender ID customization).
