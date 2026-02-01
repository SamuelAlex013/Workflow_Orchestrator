# **n8n-nodes-gmail-with-reply**

It's just a modified version of the original Gmail node that adds the option to control whether to reply only to the sender (replyToSenderOnly) or only to the recipient (replyToRecipientOnly).

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)  <!-- delete if no auth needed -->
[Compatibility](#compatibility)
[Usage](#usage)  <!-- delete if not using this section -->
[Resources](#resources)
<!-- delete if not using this section -->

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This modified Gmail node is just like the normal gmail node, with a new option:

- Reply to recipient only

This option allow users to customize the behavior of their email responses by selecting whether to reply to the original sender, only the recipient, or both.

## Credentials

Users need to authenticate with the Gmail API. Set up the credentials as follows:

- Follow the Gmail API setup guide to create your API keys.
- Add the credentials in n8n under the Gmail node settings._
## Compatibility

_No known incompatibility issues._

## Usage

_This is an optional section. Use it to help users with any difficult or confusing aspects of the node._

This modified Gmail node includes a new option:

* `replyToRecipientOnly`: If enabled, it will exclude the sender and only send replies to the recipients.

Make sure you configure these options correctly to control how the reply behavior works.

For more general usage instructions on how to set up Gmail in n8n, refer to the [Try it out documentation](https://docs.n8n.io/try-it-out/)


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
