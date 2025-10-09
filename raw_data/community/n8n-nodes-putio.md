# n8n-nodes-putio

[![npm version](https://badge.fury.io/js/n8n-nodes-putio.svg)](https://badge.fury.io/js/n8n-nodes-putio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Community Node](https://img.shields.io/badge/n8n-Community%20Node-green)](https://n8n.io)

This is an n8n community node for Put.io.

[Put.io](https://put.io/) is a cloud storage service that allows you to download and manage files.

## Authentication

To use this node, you need to have a Put.io account and an API key. You can find your API key in your Put.io account settings under "API Settings".

## Endpoints

The node supports the following operations:

### List Files
- Lists files in a specified folder
- Endpoint: `GET /files/list`
- Parameters:
  - `parent_id`: ID of the folder to list (default: 0 for root)

### Get File
- Retrieves details of a specific file
- Endpoint: `GET /files/{file_id}`

### Download File
- Downloads a specific file
- Endpoint: `GET /files/{file_id}/download`

### Create Folder
- Creates a new folder
- Endpoint: `POST /files/create-folder`
- Parameters:
  - `name`: Name of the new folder
  - `parent_id`: ID of the parent folder (default: 0 for root)

### Upload File
- Uploads a file to Put.io
- Endpoint: `POST /files/upload`
- Parameters:
  - `file`: The file to upload
  - `parent_id`: ID of the parent folder (default: 0 for root)

## Example API Request

Here's a sample curl request to check your account status:

```bash
curl -X GET "https://api.put.io/v2/account/info" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Resources

* [Put.io API Documentation](https://api.put.io/v2/docs/)
* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](https://github.com/webthingee/n8n-nodes-putio/blob/master/LICENSE.md) 