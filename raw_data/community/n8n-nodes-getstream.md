![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# N8N GetStream Chat Node

An N8N community node for integrating with GetStream Chat server-side SDK.

## Features

This node provides comprehensive server-side operations for GetStream Chat:

### User Operations
- **Generate Token**: Create authentication tokens for users
- **Upsert**: Create or update a single user
- **Upsert Multiple**: Bulk create or update multiple users
- **Query Users**: Search users with filters and pagination
- **Deactivate**: Deactivate a user account

### Channel Operations
- **Create**: Create new channels with optional members
- **Update**: Update channel information and settings
- **Add Members**: Add users to existing channels
- **Remove Members**: Remove users from channels
- **Add Moderators**: Grant moderator permissions to users
- **Demote Moderators**: Remove moderator permissions
- **Query Channels**: Search channels with filters and pagination

### Message Operations
- **Send**: Send messages to channels on behalf of users
- **Update**: Modify existing messages
- **Delete**: Remove messages from channels
- **Search**: Search for messages within channels

### Moderation Operations
- **Ban User**: Ban users with optional reason and timeout
- **Unban User**: Remove user bans

## Installation

1. Install the package in your N8N instance:
```bash
npm install n8n-nodes-getstream
```

2. Restart your N8N instance to load the new node.

## Configuration

### Credentials Setup

1. In N8N, create new credentials of type "Stream Chat API"
2. Add your GetStream Chat credentials:
   - **API Key**: Your GetStream Chat API key
   - **API Secret**: Your GetStream Chat API secret (server-side only)

⚠️ **Security Note**: The API secret should only be used server-side and never exposed to client applications.

## Usage Examples

### Generate User Token
- **Resource**: User
- **Operation**: Generate Token
- **User ID**: `user123`

### Send Message
- **Resource**: Message
- **Operation**: Send
- **Channel CID**: `messaging:general` (format: type:id)
- **Message Text**: `Hello, world!`
- **User ID (Sender)**: `user123`

### Create Channel
- **Resource**: Channel
- **Operation**: Create
- **Channel Type**: `messaging`
- **Channel ID**: `general`
- **Members**: `user1,user2,user3` (comma-separated)

### Query Users
- **Resource**: User
- **Operation**: Query Users
- **Query Filter**: `{"name": {"$autocomplete": "john"}}`
- **Limit**: `50`

## API Documentation

For detailed information about GetStream Chat API and available operations, visit:
- [GetStream Chat Documentation](https://getstream.io/chat/docs/node/)
- [Server-side SDK Reference](https://getstream.io/chat/docs/node/backend/)

## Development

To build the node locally:

```bash
# Install dependencies
pnpm install

# Build the project
pnpm run build

# Run in development mode
pnpm run dev
```

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
1. Check the [GetStream Chat documentation](https://getstream.io/chat/docs/node/)
2. Open an issue on this repository
3. Contact GetStream support for API-related questions

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature requests.
