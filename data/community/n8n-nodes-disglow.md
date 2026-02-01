# n8n-nodes-disglow

This is an n8n community node for integrating with the Disglow API, allowing you to manage Discord servers, roles, and users through n8n workflows.

## Installation

To use this node in your n8n instance, you have several options:

### Via npm
```bash
npm install n8n-nodes-disglow
```

### Via Community Nodes (n8n Cloud & Self-hosted)
1. Go to **Settings** > **Community Nodes**
2. Enter `n8n-nodes-disglow` as the package name
3. Install the node

## Prerequisites

Before using this node, you need:
1. A Disglow API key (get it from [Disglow Dashboard](https://disglow.app))
2. Discord server(s) where you are the owner
3. The Disglow Discord bot added to your server(s)

## Configuration

### Credentials
1. In n8n, create new credentials of type "Disglow API"
2. Enter your Disglow API key (format: `disglow-api-key`)

## Available Operations

### Connection
- **Test Connection**: Verify your API key is working

### Server Operations
- **Get Servers**: Retrieve all Discord servers you own
- **Get Server Roles**: Get all roles from a specific server
- **Generate Invite**: Create personalized Discord invite links
- **Validate Server**: Check server connectivity and bot permissions

### User Operations
- **Add User to Roles**: Assign Discord roles to users
- **Remove User from Roles**: Remove roles or kick users from server

### Monitoring
- **Get API Logs**: Retrieve API usage history with filtering
- **Get API Stats**: View usage statistics and metrics

## Usage Examples

### Basic Server Information
1. Add a Disglow node to your workflow
2. Select **Server** > **Get Servers**
3. Configure your Disglow API credentials
4. Execute to get your server list

### User Management
1. Use **User** > **Add User to Roles**
2. Specify server ID, user identifier (Discord ID or email)
3. List role IDs to assign (comma-separated)
4. Choose identifier type (Discord ID or Email)

### Invite Generation
1. Select **Server** > **Generate Invite**
2. Provide server ID and user email
3. Set expiration time and usage limits
4. Get personalized invite link

## API Endpoints Covered

This node implements all Disglow API endpoints:
- `GET /test` - Connection testing
- `GET /discord/servers` - Server listing  
- `GET /discord/servers/{id}/roles` - Role management
- `POST /discord/servers/{id}/invite` - Invite generation
- `POST /discord/servers/validate` - Server validation
- `POST /discord/servers/{id}/users/{id}/roles` - Add user roles
- `DELETE /discord/servers/{id}/users/{id}/roles` - Remove user roles
- `GET /logs` - API logging
- `GET /stats` - Usage statistics

## Support

For issues with this n8n node:
- [GitHub Issues](https://github.com/disglow/n8n-nodes-disglow/issues)

For Disglow API support:
- [Disglow Documentation](https://disglow.app/dashboard/api)
- [Disglow Support](https://disglow.app/dashboard/support)

## License

MIT