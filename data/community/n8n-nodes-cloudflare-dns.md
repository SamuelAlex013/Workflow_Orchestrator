# n8n-nodes-cloudflare-dns

This is an n8n community node that allows you to interact with the Cloudflare DNS API to manage DNS records programmatically within your n8n workflows.

## Features

- **List DNS Records**: Retrieve all DNS records for a zone with optional filtering
- **Create DNS Record**: Add new DNS records to your zone  
- **Update DNS Record**: Modify existing DNS records
- **Delete DNS Record**: Remove DNS records from your zone

Supported DNS record types: A, AAAA, CNAME, MX, TXT, NS, SRV, PTR

## Prerequisites

You need:
1. A Cloudflare account
2. A domain managed by Cloudflare
3. A Cloudflare API Token with DNS permissions

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Community nodes are installed in n8n by adding the package name `n8n-nodes-cloudflare-dns` in n8n's community nodes settings.

## Credentials

This node uses the Cloudflare DNS API credentials. You need to configure:

- **API Token**: Your Cloudflare API Token with DNS permissions

### Getting a Cloudflare API Token

1. Go to the [Cloudflare dashboard](https://dash.cloudflare.com/profile/api-tokens)
2. Click "Create Token"
3. Use the "Custom token" template
4. Set the permissions:
   - Zone:Zone:Read
   - Zone:DNS:Edit
5. Choose the zones you want to manage
6. Copy the generated token

## Operations

### List DNS Records
- Retrieves all DNS records for a specified zone
- Optional filtering by record type, name, or content
- Supports pagination

### Create DNS Record
- Creates a new DNS record in the specified zone
- Supports all common DNS record types
- Optional fields: TTL, proxied status, comment, tags, priority

### Update DNS Record  
- Updates an existing DNS record
- Requires the DNS record ID
- Supports all fields available in create operation

### Delete DNS Record
- Removes a DNS record from the zone
- Requires the DNS record ID

## Usage Examples

### List all A records for a domain
1. Select "Get All" operation
2. Enter your Zone ID
3. In options, set Record Type to "A"

### Create a new A record
1. Select "Create" operation  
2. Enter Zone ID
3. Set Record Type to "A"
4. Set Record Name (e.g., "www")
5. Set Record Content (e.g., "192.0.2.1")

### Update an existing record
1. Select "Update" operation
2. Enter Zone ID and DNS Record ID
3. Modify the required fields

## Finding Zone and Record IDs

- **Zone ID**: Found in your Cloudflare dashboard under the domain overview
- **DNS Record ID**: Obtained from the "List DNS Records" operation

## Version history

### 0.1.0
- Initial release
- Support for basic DNS operations: list, create, update, delete
- Support for common DNS record types

## Resources

- [Cloudflare DNS API Documentation](https://developers.cloudflare.com/api/resources/dns/)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
