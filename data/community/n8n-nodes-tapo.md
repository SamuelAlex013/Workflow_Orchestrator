# n8n-nodes-tapo

[![npm version](https://img.shields.io/npm/v/n8n-nodes-tapo)](https://www.npmjs.com/package/n8n-nodes-tapo)
[![license](https://img.shields.io/npm/l/n8n-nodes-tapo)](LICENSE)

A custom node for [n8n](https://n8n.io) that allows you to control **TP-Link Tapo smart devices** like bulbs and plugs using either **local IP** or **cloud-based login**.

## Features

- 🌐 Cloud login and discovery.
- 📡 Local IP login for faster control.
- 💡 Control actions: Turn On, Turn Off, Toggle.
- 🔐 Secure credential handling.
- 🧩 Easy integration into n8n workflows.

## Installation

> This node is intended to be installed in a custom [n8n community node environment](https://docs.n8n.io/integrations/community-nodes/).

```bash
# Clone the repository
git clone https://github.com/javier8340/n8n-nodes-tapo.git

# Go into the folder
cd n8n-nodes-tapo

# Install dependencies
npm install

# Build the node
npm run build

# Link the node globally (for development)
npm link

# Then in your n8n custom install:
npm link n8n-nodes-tapo
