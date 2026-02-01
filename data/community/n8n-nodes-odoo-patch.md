# n8n-nodes-odoo-patch

This node is a patched copy of [n8n](https://github.com/n8n-io/n8n) original Odoo node.
It fixes multiple issues such as:

- Fetching models names
- Fetching model fields
- Add the ability to perform an action on a model

## Usage

In order to install this node in your development setup, follow these steps:

1. Clone this repository

1. Install dependencies

```bash
npm install
```

1. Once you are done with your modifications, build the code

```bash
npm run build
```

1. Link the node

```bash
npm link
```

1. Add the node to your setup

```bash
cd .. && mkdir -p n8n_install && cd n8n_install && \
npm link n8n-nodes-odoo-patch
```

1. Start your instance

```bash
npx n8n
```
