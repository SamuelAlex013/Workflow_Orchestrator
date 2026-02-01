# n8n-nodes-businessmap

This is the official n8n community node working with the [Businessmap API](https://demo.businessmap.io/openapi/). 

**Businessmap** is the most flexible software platform for outcomes-driven enterprise agility. The unmatched functionality consolidates multiple tools into one, enabling affordable deployment at scale, visibility across all projects/portfolios, and alignment on goals, to deliver quality work faster. 


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

### Supported Triggers
The **Businessmap n8n community node** supports the following triggers:
* `All Events`
* `Card Created`
* `Card Details Changed`
* `Card Discarded`
* `Card Restored`
* `Card Moved`
* `Card Archived`
* `Card Is Unarchived`
* `Comment Created`
* `Comment Updated`
* `Comment Deleted`
* `Subtask Created`
* `Subtask Updated`
* `Subtask Deleted`
* `Board Renamed`
* `Board Archived`
* `Board Unarchived`
* `Board Deleted`
* `Board Structure Changed`

### Supported Actions
The **Businessmap n8n community node** supports the following actions:
* `Create Card`: Create a card in a board of your choice. Set card details including custom fields, stickers and tags.
* `Update Card`: Update the properties of a card (Title, Description, Priority, Size, Deadline, etc.).
* `Move Card`: Move a card to a new column, lane or board.
* `Get Card by ID`: Get the details of a card by its internal ID.
* `Get Card by Custom Card ID`: Find card by custom card ID. If multiple cards are found, all will be returned. Use "Board" parameter to filter search by boards.
* `Get All Cards Per Board`: Get all cards from a selected board. The response contains up to 200 cards. To retrieve more than 200 cards, please use pagination.
* `Link Card`: Link a card to an existing card.
* `Unlink Card`: Remove a link between two cards.
* `Set Custom Fields`: Sets values of custom fields.
* `Block Card`: Block a card.
* `Unblock Card`: Unblock a card.
* `Archive Card`: Add card to archive.
* `Unarchive Card`: Extract card from archive.
* `Discard Card`: Discard a card.
* `Restore Card`: Restore a previously discarded card.
* `Add Comment`: Add a comment to a card.
* `Create Subtask`: Create a new subtask of a card.
* `Log Time`: Log time to a card.
* `Upload Attachment`: Upload an attachment to a card.
* `Download Attachment`: Download an attachment from a card.
* `Get Card Attachments`: Get a list with all attachments for a specified card.
* `Create Workspace`: Create a workspace.
* `Update Workspace`: Update a workspace.
* `Get Workspace`: Get a workspace.
* `Get All Workspaces`: Get a list with all workspaces in the account.
* `Create Board`: Create a board.
* `Update Board`: Update a board.
* `Get Board`: Get a board.
* `Get All Boards`: Get a list with all boards.
* `Get Board Structure`: Get board structure which includes all workflows, lanes and columns.
* `Create Tag`: Create a tag.
* `Update Tag`: Update a tag.
* `Delete Tag`: Delete a tag.
* `Get Tag`: Get a tag.
* `Get All Tags`: Get a list with all tags.
* `Assign Tag`: Assign a tag to a board.
* `Create Sticker`: Create a sticker.
* `Update Sticker`: Update a sticker.
* `Delete Sticker`: Delete a sticker.
* `Get Sticker`: Get a sticker.
* `Get All Stickers`: Get a list with all stickers.
* `Assign Sticker`: Assign a sticker to a board.


## Credentials

* To use this **n8n community node**, you'll need a **Businessmap** account and a user with permissions to access the API. If you don’t have an account yet, [sign up here](https://businessmap.io/sign-up) to get started.

To authenticate with the Businessmap API, you'll need to provide your domain name and API key when setting up your credentials. Follow the instructions provided on the [Businessmap API page](https://businessmap.io/api) to obtain your API key.

## Compatibility

Requires n8n version 1.0.0 or later
Requires Node.js 20.15.0 or later

## Usage

* Visit our [Knowledge Base](https://knowledgebase.businessmap.io/hc/en-us) to find answers to all your questions regarding Businessmap.
* Contact our [customer support](https://businessmap.io/customer-support) with any specific request.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/builtin/app-nodes/)
* [Create Businessmap Account](https://businessmap.io/sign-up)
* [Knowledge Base](https://knowledgebase.businessmap.io/hc/en-us)
* [Businessmap API documentation](https://demo.businessmap.io/openapi/#/)
