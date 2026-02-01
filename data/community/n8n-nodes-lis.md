# n8n-nodes-lis

This is an n8n community node. It lets you use Lis in your n8n workflows.

Lis is an AI assistant that supports dynamic chat-based workflows with advanced thread management, system instructions, and interaction with external tools such as calendars.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation or, for development, clone this repository and run the following commands:

```bash
export N8N_CUSTOM_EXTENSIONS=/path/to/n8n-nodes-lis
```

and install at `n8n`.

## Operations

- Send Chat Message
- Send System Instructions
- Get Thread State
- Get Thread History
- Delete Thread

## Credentials

This node requires a single credential:

- **Lis API**
  - `API URL`: Base URL of your Lis API (default: `http://localhost:8000`)

Make sure your Lis backend is running and accessible at the provided URL.

## Compatibility

- Requires **n8n v1.0.0+**
- Tested with **Node.js v18.10+**
- Uses **pnpm >= 9.1**

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Lis API documentation](https://github.com/Rfluid/n8n-nodes-lis.git) (your repo here)
