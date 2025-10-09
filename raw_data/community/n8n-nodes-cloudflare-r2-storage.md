# n8n-nodes-cloudflare-r2

[![npm version](https://badge.fury.io/js/n8n-nodes-cloudflare-r2-storage.svg)](https://www.npmjs.com/package/n8n-nodes-cloudflare-r2-storage)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An n8n community node for seamless integration with **Cloudflare R2 Object Storage**. Upload, download, manage files and buckets with zero egress fees. Includes batch operations, CORS management, and full AI Agent compatibility.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Usage Examples](#usage-examples)
- [AI Agent Compatibility](#ai-agent-compatibility)
- [API Reference](#api-reference)
- [Development](#development)
- [Support](#support)

## Installation

### Via n8n Community Nodes (Recommended)

1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Enter `n8n-nodes-cloudflare-r2-storage` in the **Package** field  
3. Click **Install**
4. Restart your n8n instance

### Via npm

```bash
# Navigate to your n8n installation folder
cd ~/.n8n

# Install the package  
npm install n8n-nodes-cloudflare-r2-storage

# Restart n8n
```

## Operations

### 🪣 Bucket Operations
- **Create** - Create new R2 buckets with location hints
- **List** - List all buckets in your account
- **Get Info** - Get detailed bucket information
- **Delete** - Remove empty buckets
- **CORS Management** - Get, set, and delete CORS policies

### 📄 Object Operations  
- **Upload** - Upload files from binary data or text content
- **Download** - Download files with automatic binary data handling
- **Delete** - Remove objects from buckets
- **List** - List objects with prefix filtering and pagination
- **Copy** - Copy objects between buckets
- **Get Metadata** - Retrieve object metadata without downloading

### ⚡ Batch Operations
- **Upload Multiple** - Upload multiple files in one operation
- **Delete Multiple** - Delete up to 1,000 objects at once
- **Download Multiple** - Download multiple files efficiently

## Credentials

You'll need a Cloudflare account with R2 enabled. This node requires two sets of credentials:

### 1. API Token (for bucket management)

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/profile/api-tokens)
2. Click **"Create Token"** → **"Custom token"**
3. Configure permissions:
   - **Account**: `Cloudflare R2:Edit`
   - **Zone Resources**: `Include - All zones` (if using custom domains)
4. Copy the generated token

### 2. R2 Access Keys (for object operations)

1. Go to your [Cloudflare R2 Dashboard](https://dash.cloudflare.com/)
2. Select **R2** → **Manage R2 API Tokens**
3. Click **"Create API Token"**
4. Configure:
   - **Token Name**: Choose a descriptive name (e.g., "n8n-r2-access")
   - **Permissions**: Select **Object Read & Write** (or appropriate level)
   - **Bucket**: Select specific buckets or allow all
5. Click **"Create API Token"**
6. Copy the **Access Key ID** and **Secret Access Key** (you won't see the secret again!)

### Node Credentials Configuration

- **Account ID**: Your Cloudflare Account ID (found in dashboard sidebar)
- **API Token**: The token created in step 1 (for bucket operations)
- **Access Key ID**: The R2 Access Key ID from step 2 (for object operations)
- **Secret Access Key**: The R2 Secret Access Key from step 2 (for object operations)
- **API Endpoint**: `https://api.cloudflare.com/client/v4` (default)

## Usage Examples

### Basic File Upload

```json
{
  "resource": "object",
  "operation": "upload", 
  "bucketName": "my-storage-bucket",
  "objectKey": "documents/report.pdf",
  "dataSource": "binaryData",
  "binaryPropertyName": "data",
  "contentType": "application/pdf"
}
```

### List Objects with Filtering

```json
{
  "resource": "object",
  "operation": "list",
  "bucketName": "my-storage-bucket", 
  "listOptions": {
    "prefix": "images/",
    "maxKeys": 100
  }
}
```

### Batch Delete

```json
{
  "resource": "batch",
  "operation": "deleteMultiple",
  "bucketName": "my-storage-bucket",
  "objectKeys": "old/file1.txt\nold/file2.jpg\ntemp/cache.json"
}
```

### CORS Configuration

```json
{
  "resource": "bucket", 
  "operation": "setCORS",
  "bucketName": "my-web-assets",
  "corsRules": {
    "rules": [
      {
        "allowedOrigins": "https://mywebsite.com,https://app.mywebsite.com",
        "allowedMethods": ["GET", "POST", "PUT"],
        "allowedHeaders": "Content-Type,Authorization",
        "maxAge": 3600
      }
    ]
  }
}
```

## AI Agent Compatibility

This node is fully compatible with n8n's AI Agent nodes and can be used as a tool. The AI can:

- **Upload files** provided by users or generated content
- **Download and retrieve** files for processing  
- **Manage storage** by creating buckets and organizing files
- **Batch operations** for handling multiple files efficiently

### AI-Friendly Features

- **Clear operation descriptions** that help AI understand capabilities
- **Comprehensive error handling** with meaningful messages
- **Flexible input handling** for various data sources
- **Structured responses** for easy AI interpretation

## API Reference

### Supported Cloudflare R2 Features

- ✅ **Object Storage**: Full CRUD operations
- ✅ **Bucket Management**: Complete lifecycle management
- ✅ **CORS Policies**: Cross-origin resource sharing
- ✅ **Batch Operations**: Efficient bulk operations  
- ✅ **Custom Metadata**: Attach metadata to objects
- ⏳ **Multipart Uploads**: Large file support (coming soon)
- ⏳ **Lifecycle Policies**: Automated object management (coming soon)
- ⏳ **Event Notifications**: Webhook integrations (coming soon)

### Response Formats

All operations return structured JSON responses:

```json
{
  "success": true,
  "object": {
    "key": "path/to/file.txt",
    "size": 1024,
    "etag": "d41d8cd98f00b204e9800998ecf8427e", 
    "last_modified": "2023-12-01T10:30:00Z",
    "content_type": "text/plain"
  }
}
```

## Development

### Building from Source

```bash
# Clone repository
git clone https://github.com/jezweb/n8n-nodes-cloudflare-r2.git
cd n8n-nodes-cloudflare-r2

# Install dependencies
npm install

# Build the project
npm run build

# Link for local testing
npm link
cd ~/.n8n/custom
npm link n8n-nodes-cloudflare-r2-storage
```

### Testing

```bash
# Lint code
npm run lint

# Format code 
npm run format

# Build and test
npm run build
```

## Advanced Configuration

### Custom Endpoints

For enterprise or specialized deployments, you can configure custom API endpoints:

```json
{
  "accountId": "your-account-id",
  "apiToken": "your-api-token", 
  "apiEndpoint": "https://api.custom.cloudflare.com/client/v4"
}
```

### Location Hints

Optimize performance by specifying geographic location hints when creating buckets:

- **ENAM**: Eastern North America  
- **WNAM**: Western North America
- **EEUR**: Europe
- **APAC**: Asia-Pacific

### Error Handling

The node provides comprehensive error handling:

- **Validation errors**: Invalid bucket names, object keys
- **API errors**: Authentication, permissions, rate limits
- **Network errors**: Connection timeouts, DNS issues
- **Resource errors**: Bucket not found, object not found

## Troubleshooting

### Common Issues

**"Invalid bucket name"**
- Bucket names must be 3-63 characters
- Only lowercase letters, numbers, hyphens, periods
- Cannot be formatted as IP address

**"Authentication failed"**  
- Verify Account ID is correct
- Ensure API token has R2:Edit permissions
- Check token hasn't expired

**"Object not found"**
- Verify bucket name and object key are correct
- Ensure object exists in the specified bucket
- Check for case sensitivity in object keys

## Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-cloudflare-r2/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/jezweb/n8n-nodes-cloudflare-r2/discussions)
- 📖 **Documentation**: [Cloudflare R2 Docs](https://developers.cloudflare.com/r2/)
- 💬 **Community**: [n8n Community Forum](https://community.n8n.io/)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

---

**Built with ❤️ by [Jez (Jeremy Dawes)](https://www.jezweb.com.au)** | **Powered by [Cloudflare R2](https://cloudflare.com/r2/)**