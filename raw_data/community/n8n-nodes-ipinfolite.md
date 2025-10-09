# n8n-nodes-ipinfolite

A community n8n node for IPinfo LITE API - simple IP lookups with minimal data.

## Description

This node provides access to IPinfo's APIs (`https://api.ipinfo.io/lite/{ip}` and standard endpoints) for IP information lookups.  
It supports both the **Lite API** (minimal data, faster and free) and **Base API** (more detailed info for specific fields).

## Installation

### Via n8n Community Nodes (Recommended)

1. In your n8n instance, go to **Settings > Community Nodes**
2. Click **Install a community node**
3. Search for `n8n-nodes-ipinfolite`
4. Click **Install**

### Via npm (Self-hosted)

```bash
npm install n8n-nodes-ipinfolite
```

### Manual Installation (Docker)

If you're running n8n via Docker, you can mount the node:

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -v /path/to/n8n-nodes-ipinfolite:/home/node/.n8n/nodes/n8n-nodes-ipinfolite \
  n8nio/n8n
```

## Configuration

1. Add the "IPinfo Lite" node to your workflow
2. Create credentials for IPinfo API:
   - Go to Credentials > Add Credential
   - Search for "IPinfo API"
   - Enter your API token (get one at https://ipinfo.io/dashboard/token)

## Usage

### Operations


Lite API

- **Get Self IP (General)** → Get general info for your own IP (/lite/me)
- **Get Lookup IP (General)** → Get general info for a specific IP (/lite/{ip})
- **Get Self IPv4** → Get IPv4 info for your own IP (v4.api.ipinfo.io/lite/me)
- **Get IPv4** → Get IPv4 info for a specific IP (v4.api.ipinfo.io/lite/{ip})
- **Get Self IPv6** → Get IPv6 info for your own IP (v6.api.ipinfo.io/lite/me)
- **Get Lookup IPv6** → Get IPv6 info for a specific IP (v6.api.ipinfo.io/lite/{ip})

Base API

- **Base - JSON IP Lookup** → Get complete JSON info for a specific IP (ipinfo.io/{ip})
- **Base - IP Lookup Organization (Filtered)** → Get the organization (plaintext) for a specific IP (ipinfo.io/{ip}/org)
- **Base - IP Lookup City (Filtered)** → Get the city (plaintext) for a specific IP (ipinfo.io/{ip}/city)
- **Base - IP Lookup Country (Filtered)** → Get the country code (plaintext) for a specific IP (ipinfo.io/{ip}/country)


### Example

1. Add the "IPinfo Lite" node to your workflow
2. Select "Get Lookup IP (Lite)" operation
3. Enter an IP address (e.g., "8.8.8.8")
4. Configure your IPinfo API credentials
5. Execute the workflow

The node will return basic IP information in the format:
```json
{
  "ipinfo": {
    "ip": "8.8.8.8",
    "city": "Mountain View",
    "region": "California",
    "country": "US"
  },
  "operation": "getLookupGeneral"
}
```

## Requirements

- n8n instance (self-hosted or cloud)
- IPinfo API token (free tier available)

## License

MIT License - see LICENSE file for details.

## Support

For issues and feature requests, please visit the [GitHub repository](https://github.com/ilcomix/n8n-nodes-ipinfolite).
