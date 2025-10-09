# Wolt n8n Node

This n8n node allows you to interact with the Wolt API, enabling you to manage your venue's menu items and inventory directly from your n8n workflows.

## Features

This node provides two main operations for interacting with the Wolt API:

- **Update Items**: Allows for bulk updates of item data, such as price and visibility. This is useful for syncing your menu from a point-of-sale (POS) or menu management system with the Wolt app.
- **Update Inventory**: Enables bulk updates of inventory quantities for items. This helps prevent orders for out-of-stock items.

These operations are performed by making authenticated `PATCH` requests to the Wolt API using n8n's built-in `httpRequest` helper, which is a wrapper around the standard [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

## Technology Stack

This project is built with [TypeScript](https://www.typescriptlang.org/) and is designed to integrate with [n8n](https://n8n.io/), a workflow automation tool. It uses the `n8n-workflow` library to define the node's properties, credentials, and execution logic.

## Project Structure

```
.
├── credentials/
│   └── WoltClientApi.credentials.ts
├── dist/
├── nodes/
│   └── WoltClient/WoltClient.node.ts
├── package.json
└── tsconfig.json
```

- [**credentials/**](./credentials/): This directory contains the definition for the Wolt API credentials, allowing you to securely store and use your API username and password within n8n.
- [**nodes/WoltClient/**](./nodes/WoltClient/): This directory holds the core logic for the Wolt Client node, including the node's properties, operations, and the execution flow for interacting with the Wolt API.
