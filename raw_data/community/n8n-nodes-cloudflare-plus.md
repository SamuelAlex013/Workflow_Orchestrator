# n8n-nodes-cloudflare-plus

This is an n8n community node. It lets you use Cloudflare in your n8n workflows.

Cloudflare is a global connectivity cloud providing CDN, DNS, security, serverless compute (Workers), and analytics for internet properties.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

Supported resources and operations:

- Zone: `list`, `get`, `delete`
- DNS Record: `list`, `get`, `create`, `update`, `delete`
- Firewall Rule: `list`, `create`, `delete`
- Cache: `purge` (purge everything)
- Workers: `deploy` (route pattern to script)
- Analytics: `stats` (zone dashboard summary)

Dynamic option loaders help you select Accounts, Zones, and DNS Records.

## Credentials

Create credentials of type `Cloudflare API`.

- Recommended: API Token (scoped to required resources) — sent as `Authorization: Bearer <token>`
- Legacy: API Key + Email — sent as `X-Auth-Key` and `X-Auth-Email`

The node defaults to `https://api.cloudflare.com/client/v4`. A built-in credential test verifies tokens at `/user/tokens/verify`.

## Compatibility

- Works with current n8n 1.x releases.
- Uses standard REST requests and should be OS/architecture agnostic. Please open an issue if you hit a version incompatibility.

## Usage

- Use the Resource and Operation selectors to choose what to perform.
- For list operations, use `Return All` or `Limit`; pagination is handled automatically.
- Respecting Cloudflare rate limits: requests honor `Retry-After` and use backoff on 429/503.
- Examples are provided in `examples/` for DNS, cache purge, firewall rule creation, and worker route deployment.

## Support / Contact

- 💬 Open an [issue on GitHub](https://github.com/Quales-N8N/n8n-nodes-cloudflare-plus/issues)
- 💬 Discord : @pepito9159
- 📧 Mail: contact-n8n@quales.me
- 🧑‍💻 Author: [Quales](https://github.com/Quales)

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Cloudflare API documentation](https://developers.cloudflare.com/api/)

## Version history

- v1.0.0: Initial release with Zone, DNS, Firewall, Cache purge, Workers deploy, and Analytics stats.
