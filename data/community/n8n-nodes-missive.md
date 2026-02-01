# n8n-nodes-missive

This package contains n8n nodes for the Missive API, allowing you to automate your Missive workflows.

## Features

- Create and manage drafts
- Create posts in conversations
- Manage contacts and contact books
- Access conversation data
- List organizations

## Installation

### In n8n
1. Go to **Settings** > **Community Nodes**
2. Click on **Install**
3. Enter `n8n-nodes-missive` in **Name**
4. Click **Install**

### In your own n8n installation
1. Go to your n8n installation directory
2. Run `npm install n8n-nodes-missive`
3. Start n8n

## Usage

### Authentication

To use the Missive nodes, you'll need an API token from Missive:
1. Open your Missive preferences
2. Click on the API tab
3. Create a new token
4. Use this token when setting up your Missive credentials in n8n

### Available Resources and Operations

- **Drafts**
  - Create a new draft

- **Posts**
  - Create a new post in a conversation

- **Contacts**
  - Create a new contact
  - Get a specific contact
  - Get all contacts
  - Update a contact
  - Delete a contact

- **Contact Books**
  - Get all contact books

- **Conversations**
  - Get a specific conversation
  - Get all conversations

- **Organizations**
  - Get all organizations

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Missive API documentation](https://learn.missiveapp.com/api-documentation/rest-endpoints)