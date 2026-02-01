# n8n-nodes-datocms

This is an n8n community node that provides a simplified interface for DatoCMS operations. It lets you automate content management tasks in DatoCMS using n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[DatoCMS](https://www.datocms.com/) is a headless CMS for modern web and mobile applications.

## ⚠️ Early Development Notice

**This integration is in early development stages.** 
- Expect bugs and issues
- Production use is not recommended without thorough testing
- Breaking changes may occur in future updates
- Please report issues on [GitHub](https://github.com/philippherzig/n8n-nodes-datocms/issues)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### npm

```bash
npm install n8n-nodes-datocms
```

### n8n Community Nodes GUI

1. Go to **Settings** > **Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-datocms` in **Enter npm package name**
4. Select **Install**

## Operations

### Records

- **Create** - Create a new content record
- **Create or Update** - Create or update a record based on matching fields (upsert)
- **Delete** - Delete a record
- **Get** - Retrieve a single record
- **Get Many** - List records with advanced filtering
- **Update** - Update an existing record
- **Publish** - Publish a draft record
- **Unpublish** - Unpublish a live record

### Uploads

- **Create** - Upload a file from binary data or URL
- **Bulk Create** - Upload multiple files from URLs with automatic asset reference replacement
- **Delete** - Delete an uploaded file
- **Get** - Get upload information
- **Get Many** - List uploads with optional collection filtering

### Item Types

- **Get** - Get details of a specific content model
- **Get Many** - List all available content models

### Blocks

- **Create** - Create modular content blocks for use in modular content fields

## Features

### Dynamic Field Loading
- Content types and fields are automatically loaded from your DatoCMS project
- No need to manually enter IDs or field names

### ResourceMapper Integration
- Visual field mapping interface for easy configuration
- Support for required, unique, and localized fields
- Automatic field validation based on DatoCMS schema

### Advanced Filtering
- Filter records by any field value
- Support for multiple operators (equals, greater than, in, exists, etc.)
- Works with both system fields and custom fields

### Bulk Operations
- Upload multiple files at once from URLs
- Automatic URL extraction from data structures
- Replace URLs with DatoCMS asset references for seamless integration

### Error Handling
- Comprehensive error messages
- Continue on fail support for batch operations
- Detailed operation statistics for bulk uploads

## Credentials

To use this node, you need to create DatoCMS API credentials:

1. Log in to your DatoCMS project
2. Go to **Settings** > **API Tokens**
3. Create a new API token with appropriate permissions
4. In n8n, create new DatoCMS credentials using this token

### Credential Fields

- **API Token** - Your DatoCMS management API token
- **Environment** - The environment to use (default: main)
- **Base URL** - The DatoCMS API endpoint (default: https://site-api.datocms.com)

## Usage Examples

### Creating a Record

1. Select **Resource**: Record
2. Select **Operation**: Create
3. Choose your **Item Type** from the dropdown
4. Map fields using the visual ResourceMapper
5. Enable **Auto Publish** if needed

### Filtering Records

1. Select **Resource**: Record
2. Select **Operation**: Get Many
3. Choose your **Item Type**
4. Add filters to search for specific records:
   - Select field (e.g., "status", "created_at")
   - Choose operator (e.g., "equals", "greater than")
   - Enter value

### Bulk Upload Images

1. Select **Resource**: Upload
2. Select **Operation**: Bulk Create
3. Configure source (input data or URL list)
4. Enable **Replace URLs in Data** to get asset references
5. The output will include DatoCMS asset references ready for record creation

### Upsert Records (Sync External Data)

1. Select **Resource**: Record
2. Select **Operation**: Create or Update
3. Choose your **Item Type**
4. In ResourceMapper, select matching fields (e.g., external_id, SKU)
5. Map all other fields
6. Enable **Create If Not Found** to create new records when no match exists

### Creating Modular Content Blocks

1. Select **Resource**: Block
2. Select **Operation**: Create
3. Choose your **Block Type** from available modular blocks
4. Map fields using the visual ResourceMapper
5. Use the complete returned block object (including ID) in modular content fields

## Compatibility

- Requires n8n version 0.193.0 or later
- Works with DatoCMS Content Management API v3
- Supports all DatoCMS field types including localized content

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [DatoCMS API documentation](https://www.datocms.com/docs/content-management-api)
* [GitHub repository](https://github.com/philippherzig/n8n-nodes-datocms)

## License

[MIT](https://github.com/philippherzig/n8n-nodes-datocms/blob/master/LICENSE.md)