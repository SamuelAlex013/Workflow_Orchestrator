# n8n-nodes-crowd-tt-explorer

A simple n8n node wrapper to interact with TapTools APIs. This node provides an easy way to query wallet token trades directly from your n8n workflows.

## Installation

### Community Nodes (Recommended)

1. Go to **Settings → Community Nodes** in your n8n instance
2. Enter `n8n-nodes-crowd-tt-explorer` in the npm package name field
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-crowd-tt-explorer
```

## Credentials Setup

1. Create a new credential of type **"Crowd TT API"**
2. Enter your TapTools API key in the **API Key** field
3. Save the credential

## Operations

### Get Wallet Token Trades

Retrieves token trades for a specific wallet address.

**Parameters:**
- **Wallet Address** (required): The Cardano wallet address to query
- **Page**: Page number for pagination (default: 1)
- **Per Page**: Number of results per page (default: 10)  
- **Unit**: Optional unit parameter


## API Documentation

This node interacts with the TapTools API. For more information about available endpoints and data formats, visit the https://www.taptools.io/openapi/subscription (https://openapi.taptools.io/).

## Support


## Changelog

### 1.0.1
- Initial release
- Support for wallet token trades endpoint
- TapTools API credential integration
- Pagination support