# n8n-nodes-unipile

This is an n8n community node. It lets you use Unipile in your n8n workflows.

[n8n](https://n8n.io/) is a fair-code licensed workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the community nodes installation guide:
https://docs.n8n.io/integrations/community-nodes/installation/

After installation, search for "Unipile" in the Nodes panel.

## Operations

Supported resources and operations:

- Accounts
  - List accounts
  - Get account
  - Create account (native)
  - Hosted link (connect via hosted auth)
  - Reconnect account
  - Restart account
  - Resync account
  - Resend checkpoint
  - Solve checkpoint
  - Delete account

- Messaging
  - List chats, get chat, start chat, send message in chat, patch chat, sync chat history
  - List chat messages, get message, get message attachment, forward message
  - List attendees, get attendee, get attendee picture
  - List attendee chats, list attendee messages

- Emails
  - List emails, get email, delete email
  - Send email, update email
  - Create draft
  - List folders, get folder
  - Get email attachment

- Calendars
  - List calendars, get calendar
  - List events, get event
  - Create event, edit event, delete event

- LinkedIn
  - Get job postings, get job posting, create job posting, edit job posting, publish job posting, close job posting
  - Get job applicants, get job applicant, download applicant resume
  - Search, search parameters
  - Perform action on member
  - Get company profile
  - Get inmail balance
  - Solve job publishing checkpoint

- Users
  - Get me, edit me, get profile by identifier
  - List followers, following, relations
  - List invitations sent/received, send invitation, cancel invitation, handle invitation
  - List user posts, comments, reactions

- Posts
  - Create post, get post
  - Comment post, add reaction
  - List post comments, list post reactions

- Webhooks
  - List webhooks, create webhook, delete webhook

## Credentials

Add credentials "Unipile API" in n8n:

- Access Token: your Unipile access token (from the Unipile dashboard)
- DSN (Base URL): your Unipile DSN, including protocol and port.
  - Example: https://api1.unipile.com:13111

Authentication is handled by the node using an X-API-KEY header. The credentials test performs a GET to `/api/v1/accounts` against your DSN.

## Compatibility

- n8n Nodes API version: 1
- Node.js: >= 20.15 (per package engines)
- n8n: built for n8n 1.x

If you encounter issues on older n8n versions, please upgrade to a recent 1.x release.

## Usage

1) Create Unipile credentials (Access Token + DSN) in n8n.
2) Add the Unipile node to a workflow, pick a Resource and Operation.
3) For operations requiring a body, provide JSON as specified in the Unipile docs.

Tips:
- Prefer "Hosted link" to connect accounts when you want an OAuth-like flow. Use "Create account (native)" for direct JSON-based connections.
- The DSN varies by tenant/region; copy it from your Unipile dashboard.
- For LinkedIn advanced cases, "Get raw data" is intentionally not exposed here; use the dedicated operations.

## Resources

- n8n community nodes documentation: https://docs.n8n.io/integrations/#community-nodes
- Unipile developer docs: https://developer.unipile.com

