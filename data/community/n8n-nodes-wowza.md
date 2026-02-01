# n8n-nodes-wowza

An n8n community node for interacting with Wowza Streaming Engine API.

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**
2. Select **Install a community node**
3. Enter `n8n-nodes-wowza`
4. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-wowza
```

## Operations

### Stream Targets (Push Publish)

- **Enable**: Enable a stream target for push publishing
- **Disable**: Disable a stream target 
- **Get Status**: Get the current status of a stream target
- **List All**: List all stream targets in an application

## Credentials

The node uses **Wowza API** credentials:

- **Server URL**: Your Wowza server URL (e.g., `http://your-server.com:8087`)
- **Username**: Wowza REST API username
- **Password**: Wowza REST API password

## Usage Example

1. **Add Wowza node** to your workflow
2. **Configure credentials** with your Wowza server details
3. **Set operation** to "Stream Target"
4. **Choose action**: Enable, Disable, Get Status, or List All
5. **Enter application name** (e.g., "live")
6. **Enter stream target name** (for specific actions)

## Compatibility

- Tested with Wowza Streaming Engine 4.6+
- Requires n8n version 0.87.0+

## Development

```bash
git clone https://github.com/yourusername/n8n-nodes-wowza.git
cd n8n-nodes-wowza
npm install
npm run build
```

## License

MIT

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Wowza REST API documentation](https://www.wowza.com/docs/wowza-streaming-engine-rest-api)

## Keywords

n8n, wowza, streaming, rtmp, live-streaming, push-publish, stream-targets