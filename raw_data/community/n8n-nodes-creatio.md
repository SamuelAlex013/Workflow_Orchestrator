# Creatio Node

This node allows you connect N8N to Creatio, the popular Agentic Nocode Platform with an excellent CRM. 
## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Authentication](#authentication)
- [Resources](#resources)
---

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

---

### Features

- Connect n8n to your Creatio instance
- Create, read, update, and delete records in any Creatio entity
- Select entities and fields dynamically
- Execute custom methods on Creatio models
- Store and manage multiple Creatio credentials

### Usage

#### GET
- Choose your Creatio subPath and target fields from the dropdown menus or add manually using an Expression
- Use the optional Filter, Top and Expand filters

#### POST
- Choose your Creatio subPath from the dropdown menu or add manually using an Expression
- Enter JSON with the data you want to add

#### PATCH
- Choose your Creatio subPath from the dropdown menu or add manually using an Expression
- Enter ID of record to update
- Enter JSON with the data you want to update

#### DELETE
- Choose your Creatio subPath from the dropdown menu or add manually using an Expression
- Enter ID of record to delete


**Example use cases:**
- Add new leads or contacts automatically
- Sync data between Creatio and other platforms
- Update records based on external triggers
- Retrieve and process Creatio data for reporting or AI agents

### Authentication

Authentication is required. Store your Creatio API credentials securely in n8n before using the node.
It is possible that the selected user is not allowed to delete records.

### Input

The node accepts:
- Storing credentials
- Creatio Tenant selection
- Creatio Entity selection
- Creatio model method execution body parameters

### Output

- Output from Creatio

### Authentication

All fields required

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
