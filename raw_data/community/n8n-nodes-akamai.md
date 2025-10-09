# n8n-nodes-akamai

[![npm version](https://img.shields.io/npm/v/n8n-nodes-akamai.svg)](https://www.npmjs.com/package/n8n-nodes-akamai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Community Node](https://img.shields.io/badge/n8n-Community%20Node-FF6D5A.svg)](https://n8n.io)

Professional Akamai API integration for n8n workflows with automatic EdgeGrid authentication.

## Features

- Automatic EdgeGrid authentication handling
- Complete REST API support (GET, POST, PUT, PATCH, DELETE)
- PAPI-Use-Prefixes header management
- Custom headers and query parameters
- Comprehensive error handling
- Configurable response format: body-only or full `{ meta, data }` with status code and headers

## Prerequisites

- n8n v1.104.2+ (self-hosted installation required)
- Active Akamai account with API access

## Installation

### Step 1: Enable Community Nodes

Configure your n8n instance to support Community Nodes:

```yaml
# docker-compose.yml
services:
  n8n:
    image: n8nio/n8n:latest
    environment:
      - N8N_COMMUNITY_PACKAGES_ENABLED=true
      - N8N_REINSTALL_MISSING_PACKAGES=true
```

### Step 2: Install Package

1. Navigate to **Settings → Community Nodes** in your n8n instance
2. Click **Install** and enter: `n8n-nodes-akamai`
3. Restart n8n to complete installation

## Quickstart

### Example: GET user profile

1. Create credentials: `Akamai API`
2. Add the `Akamai API` node to the workflow
3. Select `Operation: GET`
4. Set `API Path: /identity-management/v3/user-profile`
5. Run

### Example: POST with JSON body

1. `Operation: POST`
2. `API Path: /some/api/path`
3. `Request Body`:

```json
{
  "example": true
}
```

4. Run

## Authentication

### API Credentials Setup

1. Access **Identity & Access Management → API clients** in Akamai Control Center
2. Create or configure API client with required permissions
3. Note your credentials for n8n configuration

### n8n Credentials Configuration

Create **Akamai API** credentials with:

| Field         | Description                                           |
| ------------- | ----------------------------------------------------- |
| Client Token  | API client token                                      |
| Client Secret | API client secret                                     |
| Access Token  | API access token                                      |
| Host          | API hostname (e.g., `akab-xxxxx.luna.akamaiapis.net`) |

## Configuration

### PAPI Use Prefixes

| Option                  | Behavior                                     |
| ----------------------- | -------------------------------------------- |
| Don't Send Header       | Use client default                           |
| Include Prefixes (True) | Include ID prefixes (`prp_`, `ctr_`, `grp_`) |
| Remove Prefixes (False) | Return clean IDs                             |

### Response Format

There are two response modes:

- Body-only (default): returns only the response body

```json
{ "propertyId": "prp_123", "name": "Site" }
```

- Full response (enable "Return Full Response (Meta/Data)"): returns `{ meta, data }`

```json
{
  "meta": {
    "statusCode": 200,
    "endpoint": "GET /identity-management/v3/user-profile",
    "headers": { "...": "..." }
  },
  "data": { "...": "..." }
}
```

Notes:

- `headers` are included in `meta` only in full response mode
- For `204 No Content`, `data` may be `null` or an empty object depending on the API

### Query parameters and headers

- Add multiple query parameters via `Options → Query Parameters`
- Add custom headers via `Options → Headers`

### Tips for Akamai

- `PAPI-Use-Prefixes`: control ID prefixes in responses (`prp_`, `ctr_`, `grp_`). Leave empty to use client default
- Account Switch Key: if needed, add as query parameter `accountSwitchKey=...` in `Options → Query Parameters`

## Troubleshooting

- 401/403 Unauthorized/Forbidden: verify tokens/permissions in Akamai Control Center (API client scopes)
- Invalid host: use only the hostname (e.g., `akab-xxxxx.luna.akamaiapis.net`), without path or protocol
- Clock skew: ensure server time is synchronized (NTP) to satisfy EdgeGrid auth
- 4xx/5xx with JSON body: the node returns the parsed error body; enable full response to inspect headers and endpoint

## Support

- [GitHub Issues](https://github.com/simpsss/n8n-nodes-akamai/issues)
- [Akamai Developer Documentation](https://techdocs.akamai.com/developer/docs)
- [n8n Community Forum](https://community.n8n.io)

## License

MIT License - see [LICENSE.md](LICENSE.md) for details.

## About

Community node providing integration between n8n automation workflows and Akamai's API ecosystem.
