# n8n-hlautomate

This repository provides custom nodes and credentials for the [n8n](https://n8n.io/) workflow automation platform, enabling integration with HL Automate.

## Features
- **HL Automate Node:** Interact with the HL Automate API for contacts, locations, and users, with dynamic options and credential-based authentication.

## Project Structure
- `nodes/` — Node implementations, grouped by integration
- `credentials/` — Custom credential types for API authentication
- `dist/` — Build output (ignored in git)
- `gulpfile.js` — Copies icons to `dist/` during build

## Installation
Follow the [n8n community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/).

## Development
- **Build:** `npm run build` (cleans, compiles, copies icons)
- **Watch:** `npm run dev` (TypeScript watch mode)
- **Lint:** `npm run lint` (n8n custom ESLint rules)
- **Format:** `npm run format` (Prettier)
- **Prepublish:** `npm run prepublishOnly` (build + lint with stricter rules)

## Usage
After installation, the custom nodes will appear in the n8n editor. Configure credentials as required for each node.

## Resources
- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [HL Automate API docs](https://hlautomate.com/docs)



