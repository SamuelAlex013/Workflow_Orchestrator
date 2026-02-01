# n8n-nodes-pipefy

A community node that brings _(part of)_ the [Pipefy GraphQL API](https://developers.pipefy.com/graphql) to your n8n instance! With it you can create, update, delete, and get information about your Pipefy organizations, pipes, cards and webhooks.

![Banner image](https://i.imgur.com/LHBRQAi.png)

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  
[License](#license)

## Installation

Simply go to Settings > Community Nodes, click on the "Install" button, and paste the package name `@cardtunic/n8n-nodes-pipefy`. Mark the _"I understand the risks..."_ checkbox and click on "Install".

If you encounter any issues, please refer to the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

![Screenshot of the available operations in n8n UI](https://i.imgur.com/lL5g7a1.png)

### Attachments

- **Create Presigned URL**: Creates a presigned URL to upload a file to Pipefy
- **Upload File**: Sends a PUT request to upload a file to a created presigned URL

### Cards

- **Create**: Creates a card
- **Create Relation**: Creates a relation between one card and another
- **Delete**: Deletes a given card
- **Get**: Gets a card by ID
- **Get Many**: Lists all cards inside a given pipe
- **Move**: Moves a card to a given phase
- **Update**: Updates a given card
- **Update Fields**: Updates the fields of a given card

### Pipes

- **Get**: Gets a pipe by ID

### Users

- **Get Current**: Returns the authenticated user

### Webhooks

- **Create In Org**: Create a webhook to watch organization events
- **Create In Pipe**: Create a webhook to watch pipe events
- **Delete**: Deletes a given webhook
- **Get From Org**: Get all webhooks related to a given organization
- **Get From Pipe**: Get all webhooks related to a given pipe

## Credentials

There're two types of credentials that can be used to authenticate with the Pipefy API: **Service Accounts and Personal Access Tokens.**

![Screenshot of the credentials modal in n8n](https://i.imgur.com/ypRAD4z.png)

### Service Accounts (recommended)

Service Accounts are special accounts that you can create as a superuser in Pipefy dashboard. After creation, you will recieve the Client ID and Client secret that you need to paste into n8n. This is the recommended way to authenticate with the API for production environments, providing expiration time for tokens, permission control trough roles and separation from user accounts. For more details, refer to the [Pipefy service ccounts docs](https://developers.pipefy.com/reference/service-accounts).

### Personal Access Tokens

Personal Access Tokens are a simple way to authenticate with the API. You can simply generate a new token in the your profile settings in Pipefy and paste the token into n8n. For more details, refer to the [Pipefy personal access tokens docs](https://developers.pipefy.com/reference/personal-access-token).

## Compatibility

This node was only tested in 1.106.3 n8n version, but it should work in any version 1.x.x above.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Pipefy API reference](https://developers.pipefy.com/reference/why-graphql)
- [Pipefy API GraphQL explorer](https://developers.pipefy.com/graphql)

## License

[MIT](https://github.com/cardtunic/n8n-nodes-pipefy/blob/master/LICENSE.md)
