# n8n-nodes-applyboard

This is a custom n8n node that enables seamless integration with ApplyBoard's API services. The node provides a streamlined interface for making authenticated HTTP requests to ApplyBoard's endpoints while automatically handling necessary headers and authentication.

## Features

- **OAuth2 Authentication**: Secure API access using standard OAuth2 flow
- **Automatic Header Management**: 
  - Adds `traceparent` header for request tracking
  - Sets `User-Agent` with workflow name (e.g., `n8n - My Workflow`)
  - Automatically includes noCaptcha headers if configured in n8n variables
- **Full HTTP Support**: Supports all standard HTTP methods (GET, POST, PUT, DELETE, etc.)
- **Error Handling**: Proper error output handling similar to n8n's HTTP node
- **Response Formatting**: Support for both JSON and string response formats
- **Environment Variables**: Automatically picks up `noCaptcha_headerName` and `noCaptcha_headerValue` from n8n instance variables if available

## Installation

### n8n Community Node Installation

For n8n instance owners:

1. Open your n8n instance
2. Go to **Settings** > **Community Nodes**
3. Select **Install**
4. Enter `n8n-nodes-applyboard` in **Enter npm package name**
5. Agree to the risks of using community nodes
6. Select **Install**

For more details, see the [n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/).

### Manual Installation

For manual installation in your n8n instance:

```bash
cd YOUR_N8N_ROOT_DIRECTORY
npm install n8n-nodes-applyboard
```

For more details about manual installation, especially for Docker-based setups, see the [n8n manual installation guide](https://docs.n8n.io/integrations/community-nodes/installation/manual-install/).

## Usage

1. Add your OAuth2 credentials in n8n's credentials manager
2. Add the ApplyBoard node to your workflow
3. Configure:
   - HTTP method
   - Endpoint URL
   - Headers (optional)
   - Query parameters (optional)
   - Request body (for POST/PUT/PATCH)
   - Response format (JSON/String)

### Environment Variables

The node will automatically use these variables if configured in your n8n instance:
- `noCaptcha_headerName`: Name of the noCaptcha header
- `noCaptcha_headerValue`: Value of the noCaptcha header

### Headers

The node automatically adds:
- `traceparent` header with a unique trace ID
- `User-Agent` header with your workflow name
- Any custom headers you configure
- noCaptcha headers (if environment variables are set)

## ⚠️ Limited Beta

This node is currently in limited beta. API access and documentation are available only to select integration partners. Please contact your ApplyBoard representative for access details.

## Support

For technical support or questions about API access, please contact your ApplyBoard integration specialist.

## Contributing

This is a community node. Feel free to contribute by:
1. Creating issues for bug reports or feature requests
2. Submitting pull requests for improvements

This node was built following n8n's community node development guidelines:
- [Creating nodes overview](https://docs.n8n.io/integrations/creating-nodes/overview/)
- [Node development documentation](https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/)
- [Node architecture guidelines](https://docs.n8n.io/integrations/creating-nodes/build/reference/)

## License

[MIT](LICENSE.md) 