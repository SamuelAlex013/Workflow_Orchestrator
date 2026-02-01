# n8n-nodes-respondio

This is an n8n community node. It lets you use Respond.io in your n8n workflows.

Respond.io is a customer conversation management platform that helps businesses manage customer conversations across multiple channels like WhatsApp, Facebook Messenger, Instagram, and more. This node provides comprehensive integration with the Respond.io API to automate customer communication workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

- [Installation](#installation)
- [Operations](#operations)
- [Triggers](#triggers)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Respond.io Actions Node

The Respond.io Actions node supports the following operations:

#### Channels

- **Get All Channels** - Retrieve all channels connected to your workspace

#### Closing Notes

- **Get All Closing Notes** - Retrieve all closing notes templates

#### Comments

- **Add Comment** - Add a comment to a conversation

#### Contacts

- **Create Contact** - Create a new contact
- **Create or Update Contact** - Create or update an existing contact
- **Update Contact** - Update an existing contact's information
- **Find Contact** - Find a specific contact by identifier
- **Get Many Contacts** - Retrieve multiple contacts with search filtering
- **Add Tags** - Add tags to a contact
- **Remove Tags** - Remove tags from a contact
- **Add Space Tag** - Add a space tag to a contact
- **Delete Space Tag** - Delete a space tag
- **Update Space Tag** - Update a space tag
- **Delete Contact** - Delete a contact
- **Find Contact Channels** - Find channels associated with a contact

#### Contact Fields

- **Get All Custom Fields** - Retrieve all custom fields
- **Find Custom Field** - Find a specific custom field
- **Create Custom Field** - Create a new custom field

#### Conversations

- **Assign or Unassign Conversation** - Assign or unassign a conversation to/from a user
- **Open or Close Conversation** - Open or close a conversation

#### Lifecycle

- **Update Contact Lifecycle** - Update a contact's lifecycle stage
- **Remove Contact Lifecycle** - Remove a contact's lifecycle stage

#### Messages

- **Send Message** - Send a message to a contact (supports text, email, attachments, quick replies, WhatsApp templates, and custom payloads)
- **Find Message** - Find a specific message by ID

#### Users

- **Find User** - Find a specific user by ID
- **Get All Users** - Retrieve all users in the workspace

## Triggers

### Respond.io Trigger Node

The Respond.io Trigger node can listen for the following events:

- **New Incoming Message** - Triggered when a new message is received
- **New Outgoing Message** - Triggered when a new outgoing message is sent
- **New Comment** - Triggered when a new comment is added to a conversation
- **Conversation Opened** - Triggered when a conversation is opened
- **Conversation Closed** - Triggered when a conversation is closed
- **New Contact** - Triggered when a new contact is created
- **Contact Updated** - Triggered when a contact is updated
- **Contact Assignee Updated** - Triggered when a contact's assignee is changed
- **Contact Tag Updated** - Triggered when a contact's tags are modified
- **Contact Lifecycle Updated** - Triggered when a contact's lifecycle stage changes

## Credentials

To use this node, you need to authenticate with Respond.io. You'll need:

1. **API Key** - Your Respond.io API key

### How to get your API Key

1. Log in to your Respond.io account
2. Go to **Settings** → **Integrations** → **N8N**
3. Generate a new API key
4. Copy the API key and use it in the credentials

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with n8n versions**: 1.0.0+
- **Node.js version**: >=18.0.0

## Usage

### Basic Workflow Example

1. **Set up a trigger** - Use the Respond.io Trigger node to listen for new incoming messages
2. **Process the message** - Use the Respond.io Actions node to find the contact and send a response
3. **Add automation** - Create workflows that automatically assign conversations, update contact information, or send follow-up messages

### Advanced Workflow Example

1. **New message trigger** → **Find contact** → **Check contact tags** → **Send automated response** → **Assign to team member**

### Message Types Supported

The Send Message operation supports multiple message types:

- **Text messages** - Simple text messages
- **Email messages** - Rich email content with subject and body
- **Attachments** - Send files and media
- **Quick replies** - Interactive quick reply buttons
- **WhatsApp templates** - Pre-approved WhatsApp message templates
- **Custom payloads** - Custom message formats for specific channels

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Respond.io API Documentation](https://developers.respond.io/)
- [Respond.io Platform](https://respond.io/)

## Version history

### Version 1.0.0

- Initial release
- Support for all major Respond.io API operations
- Webhook triggers for real-time events
- Comprehensive contact and conversation management
- Multi-channel message sending capabilities
