# n8n-nodes-outline

![Banner](https://img.shields.io/badge/n8n-nodes-outline-blue.svg)

A community node for n8n that allows you to interact with your Outline knowledge base through its API.

## Features

- ✅ **Complete API Coverage**: Access all 10 Outline resources with 70+ operations
- ✅ **AI Agent Compatible**: All operations structured for proper AI tool calling interface
- ✅ **Advanced Operations**: Full CRUD plus specialized operations (archive, restore, export, user management)
- ✅ **Webhook Support**: Receive real-time events from Outline
- ✅ **Authentication**: Secure API key authentication with built-in credential testing
- ✅ **TypeScript**: Fully typed for better development experience

## Prerequisites

- n8n installed and running
- An Outline instance (hosted or self-hosted)
- An Outline API key (generate one in Settings → API & Apps)

## Installation

```bash
npm install n8n-nodes-outline
```

## Configuration

### Credentials

1. In n8n, go to **Credentials** in the left sidebar
2. Click **New Credential** and search for "Outline API"
3. Configure the credential with:
    - **Base URL**: Your Outline instance URL (e.g., `https://app.getoutline.com` or your self-hosted domain)
    - **API Key**: Your API key from Outline's Settings → API & Apps

### Testing Connection

The credential includes an automatic test to verify your API key and connection. Make sure the test passes before using the nodes.

## Nodes

### Outline Node

The main node for interacting with Outline's API.

#### Supported Resources

##### Documents (15 operations)

- **Create**: Create new documents
- **Get**: Retrieve document information
- **List**: List documents (with optional collection filtering)
- **Search**: Search for documents
- **Update**: Update document content and metadata
- **Delete**: Delete documents
- **Answer Question**: AI-powered question answering for documents
- **Archive**: Archive documents
- **Restore**: Restore archived documents or specific revisions
- **Duplicate**: Create copies of documents
- **Move**: Move documents between collections
- **Import**: Import documents from files
- **Export**: Export documents to various formats
- **Templatize**: Convert documents to templates
- **Unpublish**: Unpublish documents
- **Memberships**: List document memberships
- **Add User**: Add user permissions to documents
- **Remove User**: Remove user permissions from documents

##### Collections (12 operations)

- **Create**: Create new collections
- **Get**: Retrieve collection information
- **List**: List all collections
- **Update**: Update collection details
- **Delete**: Delete collections
- **Documents**: List documents in a collection
- **Add User**: Add user to collection with permissions
- **Remove User**: Remove user from collection
- **Memberships**: List collection memberships
- **Add Group**: Add group to collection with permissions
- **Remove Group**: Remove group from collection
- **Group Memberships**: List group memberships
- **Export**: Export collection contents
- **Export All**: Export all collections

##### Users (2 operations)

- **Get**: Get user information
- **List**: List team users

##### Teams (1 operation)

- **Get**: Get team information

##### Attachments (3 operations)

- **Create**: Upload file attachments
- **Delete**: Remove attachments
- **Redirect**: Get attachment download URLs

##### Comments (5 operations)

- **Create**: Add comments to documents
- **Get**: Retrieve comment information
- **List**: List comments for documents
- **Update**: Update comment content
- **Delete**: Remove comments

##### Events (1 operation)

- **List**: Retrieve audit trail and activity logs

##### File Operations (4 operations)

- **Get**: Retrieve file information
- **List**: List uploaded files
- **Delete**: Remove files
- **Redirect**: Get file download URLs

##### Groups (7 operations)

- **Create**: Create user groups
- **Get**: Retrieve group information
- **List**: List all groups
- **Update**: Update group details
- **Delete**: Remove groups
- **Add User**: Add users to groups
- **Remove User**: Remove users from groups
- **Memberships**: List group memberships

##### Auth (2 operations)

- **Info**: Get authentication information and validate API key
- **Config**: Get authentication configuration

#### Example Workflows

##### Create a Document

```json
{
	"resource": "document",
	"operation": "create",
	"title": "My New Document",
	"text": "# Welcome\n\nThis is the content of my document in markdown.",
	"collectionId": "your-collection-id",
	"publish": true
}
```

##### Search Documents

```json
{
	"resource": "document",
	"operation": "search",
	"query": "meeting notes",
	"additionalFields": {
		"limit": 10
	}
}
```

##### Archive a Document

```json
{
	"resource": "document",
	"operation": "archive",
	"documentId": "document-id-to-archive"
}
```

##### Add User to Collection

```json
{
	"resource": "collection",
	"operation": "addUser",
	"collectionId": "collection-id",
	"userId": "user-id",
	"permission": "read_write"
}
```

##### Create Comment on Document

```json
{
	"resource": "comment",
	"operation": "create",
	"documentId": "document-id",
	"data": {
		"body": "This is a helpful comment on the document."
	}
}
```

##### Export Collection

```json
{
	"resource": "collection",
	"operation": "export",
	"collectionId": "collection-id"
}
```

### Outline Webhook Node

Trigger workflows based on Outline events.

#### Supported Events

- **documents.create**: Document created
- **documents.update**: Document updated
- **documents.delete**: Document deleted
- **documents.archive**: Document archived
- **documents.restore**: Document restored
- **documents.move**: Document moved
- **documents.duplicate**: Document duplicated
- **collections.create**: Collection created
- **collections.update**: Collection updated
- **collections.delete**: Collection deleted
- **collections.move**: Collection moved
- **users.create**: User created
- **users.update**: User updated
- **users.delete**: User deleted
- **comments.create**: Comment added
- **comments.update**: Comment updated
- **comments.delete**: Comment deleted
- **groups.create**: Group created
- **groups.update**: Group updated
- **groups.delete**: Group deleted

#### Configuration

1. Add the **Outline Webhook** node to your workflow.
2. Select the events you want to listen for.
3. n8n will automatically create a webhook in your Outline instance when you activate the workflow, and delete it when you deactivate it.

## Local Development

To test this node locally with your n8n instance:

1. **Clone and build:**

    ```bash
    git clone <repository-url>
    cd n8n-nodes-outline
    bun install
    bun run build
    ```

2. **Link to n8n:**

    ```bash
    # Remove existing custom nodes
    rm -rf ~/.n8n/custom/*

    # Create symbolic link
    ln -s $(pwd) ~/.n8n/custom/n8n-nodes-outline
    ```

3. **Restart n8n** to pick up the new custom node.

## API Reference

This node implements the [Outline API](https://getoutline.com/developers) endpoints. Refer to the official documentation for detailed information about request/response formats and additional parameters.

The webhook creation and deletion is handled automatically by the node.

### Rate Limits

Outline has rate limits in place. The node will respect these limits and return appropriate error messages when limits are exceeded.

### Error Handling

- All API errors are properly handled and returned as structured error objects
- Use the "Continue on Fail" option to handle errors gracefully in your workflows
- Check the `ok` field in responses to determine success/failure

## Examples

### Document Management Workflow

```json
{
	"nodes": [
		{
			"name": "Create Document",
			"type": "n8n-nodes-outline.outline",
			"parameters": {
				"resource": "document",
				"operation": "create",
				"title": "Weekly Report",
				"text": "# Weekly Report\n\n## Achievements\n- Item 1\n- Item 2",
				"collectionId": "collection-id",
				"publish": true
			}
		},
		{
			"name": "Update Document",
			"type": "n8n-nodes-outline.outline",
			"parameters": {
				"resource": "document",
				"operation": "update",
				"documentId": "{{ $node['Create Document'].json.data.id }}",
				"text": "# Updated Weekly Report\n\nContent updated!"
			}
		}
	]
}
```

### Webhook Integration

```json
{
	"nodes": [
		{
			"name": "Document Created Webhook",
			"type": "n8n-nodes-outline.outlineWebhook",
			"parameters": {
				"events": ["documents.create"]
			}
		},
		{
			"name": "Process New Document",
			"type": "n8n-nodes-base.set",
			"parameters": {
				"values": {
					"title": "{{ $node['Document Created Webhook'].json.data.title }}",
					"author": "{{ $node['Document Created Webhook'].json.data.createdBy.name }}"
				}
			}
		}
	]
}
```

## Troubleshooting

### Common Issues

1. **"Cannot find module 'n8n-workflow'"**
    - Ensure n8n is properly installed
    - Restart n8n after installing the node

2. **"401 Unauthorized"**
    - Check your API key is correct
    - Ensure the API key has sufficient permissions
    - Verify the base URL is correct

3. **"Rate limited"**
    - Wait for the rate limit to reset
    - Implement retry logic in your workflows

### Getting Help

- Check the [Outline API documentation](https://getoutline.com/developers)
- Review n8n's [community node documentation](https://docs.n8n.io/integrations/community-nodes/)
- Open an issue in the repository

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Links

- [Outline](https://getoutline.com/)
- [n8n](https://n8n.io/)
- [API Documentation](https://getoutline.com/developers)
- [Repository](https://github.com/j-shelfwood/n8n-nodes-outline)
