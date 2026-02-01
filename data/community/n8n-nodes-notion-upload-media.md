# n8n-nodes-notion-upload-media

This is an n8n community node that allows you to upload media files (images, videos, audio, and documents) to Notion blocks using Notion's internal API.

> **Note**: This package uses Notion's internal API to enable media uploads. While functional, it may be subject to changes if Notion modifies their internal API structure.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

### Community Nodes Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-notion-upload-media` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

### NPM Installation (for development)

```bash
npm install n8n-nodes-notion-upload-media
```

## Operations

This node supports the following operations:

### Block

- **Upload Media**: Upload media files (images, videos, audio, and documents) to a Notion block with support for:
  - Auto-detection of media type based on MIME type
  - Manual selection of media type (image/video)
  - Custom file names
  - Binary data from previous nodes

## Credentials

This node requires Notion Upload Media API credentials. You need to provide:

- **Token V2**: Your Notion `token_v2` cookie value
- **Space ID**: Your Notion workspace space ID  
- **User ID**: Your Notion user ID

### How to get credentials

1. **Token V2**:
   - Open your browser's developer tools while logged into Notion
   - Go to Application/Storage > Cookies > <https://www.notion.so>
   - Find and copy the `token_v2` value

2. **Space ID & User ID**:
   - In the same cookies section, look for `notion-space-id` and `notion-user-id`
   - Or inspect network requests to find these values in API calls

## Compatibility

This node was developed and tested with n8n version 1.56.0+.

## Usage

### Basic Media Upload

1. Add the **Notion Upload Media** node to your workflow
2. Configure your credentials
3. Set the **Block ID** where you want to upload the media
4. Specify the **Input Binary Field** containing your media file
5. Choose the **Media Type** (Auto-Detect, Image, or Video)

### Block ID formats supported

The node accepts block IDs in multiple formats:

- Full UUID: `214c413b-2a68-800f-9f9a-d234e37d1380`
- Notion URL: `https://www.notion.so/workspace/page-title-214c413b2a68800f9f9ad234e37d1380`
- Raw hex: `214c413b2a68800f9f9ad234e37d1380`

## Development & Testing

### Local Testing Environment

This project includes a local n8n test environment for development and testing:

1. **Setup Environment Variables**:
   - Copy `.env.example` to `.env`: `cp .env.example .env`
   - Fill in your actual Notion credentials in the `.env` file

2. **Start Test Environment**:

   ```bash
   pnpm start
   # or
   ./start-n8n.sh
   ```

3. **Development Workflow**:
   - Make changes to the node code
   - Run `pnpm build` to rebuild the node
   - Restart n8n (Ctrl+C and run `pnpm start` again)
   - The changes will be automatically available in n8n

4. **Access n8n**: Open `http://localhost:5678` in your browser

### Getting Credentials for Testing

1. **Token V2**:
   - Open browser developer tools while logged into Notion
   - Go to Application/Storage > Cookies > <https://www.notion.so>
   - Find and copy the `token_v2` value

2. **Space ID & User ID**:
   - In the same cookies section, look for `notion-space-id` and `notion-user-id`
   - Or inspect network requests to find these values in API calls

## Resources

- [npm package](https://www.npmjs.com/package/n8n-nodes-notion-upload-media)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Notion API documentation](https://developers.notion.com/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](LICENSE.md)

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/oriolrius/n8n-nodes-notion-upload-media/issues) on GitHub.
