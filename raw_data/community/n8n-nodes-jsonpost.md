# n8n-nodes-jsonpost

A custom n8n node for integrating with JSONPost.com webhooks. This node allows you to easily create, manage, and receive webhooks from JSONPost endpoints in your n8n workflows.

## Features

- **Easy Webhook Management**: Create and delete webhooks for JSONPost endpoints
- **Real-time Data Reception**: Receive webhook data in real-time within your n8n workflows
- **Secure Authentication**: Uses API key authentication for secure access to JSONPost services
- **Event Filtering**: Subscribe to specific event types from your JSONPost endpoints
- **Automatic Cleanup**: Properly handles webhook cleanup when workflows are deactivated

## Installation

### From npm (Recommended)

```bash
npm install n8n-nodes-jsonpost
```

### n8n Community Nodes

You can also install this node directly through n8n's community nodes feature:

1. Go to **Settings** > **Community Nodes**
2. Click **Install a community node**
3. Enter `n8n-nodes-jsonpost`
4. Click **Install**

## Quick Start

### 1. Set up Credentials

1. In n8n, go to **Credentials** and create a new **JSONPost API** credential
2. Enter your JSONPost API key (get it from your JSONPost dashboard)
3. Test the connection to ensure it's working properly

### 2. Add the Node

1. Add the **JSONPost Trigger** node to your workflow
2. Select your JSONPost API credential
3. Enter your **Endpoint ID** (from your JSONPost dashboard)
4. Choose the **Event Type** you want to listen for (POST, GET, PUT, DELETE)

### 3. Activate and Test

1. Activate the workflow
2. The node will automatically create a webhook subscription with JSONPost
3. Send data to your JSONPost endpoint to trigger your workflow

## Usage

### Accessing Webhook Data

The JSONPost Trigger node outputs the complete webhook payload. You can access this data in subsequent nodes using:

- `{{ $json.body }}` - The request body
- `{{ $json.headers }}` - Request headers  
- `{{ $json.query }}` - Query parameters
- `{{ $json.method }}` - HTTP method used
- `{{ $json.timestamp }}` - When the request was received

### Example Workflow

1. **JSONPost Trigger** - Receives webhook data
2. **Set Node** - Extract specific fields from the payload
3. **HTTP Request** - Send processed data to another service
4. **Email Node** - Send notification about the received data

## Configuration Options

### JSONPost Trigger Node

- **Credential**: Your JSONPost API credential
- **Endpoint ID**: The ID of your JSONPost endpoint (found in your JSONPost dashboard)
- **Event Type**: The HTTP method to listen for:
  - `POST` - Listen for POST requests (default)
  - `GET` - Listen for GET requests
  - `PUT` - Listen for PUT requests
  - `DELETE` - Listen for DELETE requests

## Support

- **Issues & Bug Reports**: [GitHub Issues](https://github.com/yourusername/n8n-nodes-jsonpost/issues)
- **Feature Requests**: [GitHub Issues](https://github.com/yourusername/n8n-nodes-jsonpost/issues)
- **General n8n Questions**: [n8n Community Forum](https://community.n8n.io/)
- **JSONPost API Questions**: [JSONPost.com](https://jsonpost.com)

## Documentation

- **User Guide**: This README
- **Developer Documentation**: See [DEVELOPER.md](./DEVELOPER.md) for technical details, development setup, and contribution guidelines
- **Changelog**: See [CHANGELOG.md](./CHANGELOG.md) for version history

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Note**: This is a community-maintained node and is not officially supported by n8n or JSONPost. Use at your own discretion and always test thoroughly in your environment before production use.
