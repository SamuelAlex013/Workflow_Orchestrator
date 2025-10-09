![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-sandbox

This package provides a single custom node: **Sandbox Code**.

Sandbox Code executes user-supplied code remotely through a sandbox API (`/v1/sandbox/run`) and returns `stdout` and `error` output. It supports Python 3 currently.

## Prerequisites

You need the following installed on your development machine:

- [git](https://git-scm.com/downloads)
- Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
- Install n8n with:

  ```bash
  npm install n8n -g
  ```

- Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Node Overview

Sandbox Code Node parameters:

- Language: `python3` or `javascript`. Python code is auto-wrapped in an async function; JavaScript code is auto-wrapped in an async IIFE for top-level `await`.
- Enable Network: toggles outbound network (mapped to `enable_network`).
- Code: multi-line code string to execute.

Execution response shape:

```json
{
	"code": 0,
	"message": "success",
	"data": { "stdout": "...", "error": "" }
}
```

The node outputs an item JSON containing: `success`, `language`, `stdout`, `error`.

## Credentials

Create credentials of type `Sandbox API` providing:

- Base URL (default: <https://sandbox.0x2a.top>)
- API Key (sent as `X-Api-Key` header)

## Development

Install deps and build:

```bash
npm install
npm run build
```

Link or copy the built package into your n8n instance, then add the Sandbox Code node.

## License

MIT
