# n8n-nodes-arivo

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/arivo-crm/n8n-nodes-arivo/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/arivo-crm/n8n-nodes-arivo/blob/main/README.pt-BR.md)

This is an n8n community node for Arivo CRM.

_Arivo CRM_ is a online CRM built for small to medium companies to keep track of contacts and deals.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)   
[Compatibility](#compatibility)   
[Usage](#usage)   
[Resources](#resources)  
[Version history](#version-history)   
[License](#license)

## Installation

To install the Arivo CRM node in a self-hosted n8n instance:
1. Open "Settings" (in the menu beside your user name)
2. Navigate to "Community nodes"
3. Click "Install"
4. Fill "npm Package Name" with "n8n-nodes-arivo"
5. Check "I understand the risks of installing unverified code from a public source."
6. Click "Install"

Or follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Action Node

- Contact (Person)
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Contact (Company)
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Deal
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Note
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Task
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Product
  - Create
  - Get
  - Get All
  - Update
  - Delete
- Product Category
  - Create
  - Get
  - Get All
  - Update
  - Delete
- File
  - Get
  - Get All
  - Delete
- Custom Record
  - Create
  - Get
  - Get All
  - Update
  - Delete

### Trigger Node

- Person Created
- Person Updated
- Person Deleted
- Company Created
- Company Updated
- Company Deleted
- Deal Created
- Deal Updated
- Deal Deleted
- Deal Won
- Deal Lost
- Deal Reopened
- Note Created
- Note Updated
- Note Deleted
- Task Created
- Task Updated
- Task Done
- Task Updated to Not Done
- Task Deleted
- Custom Record Created
- Custom Record Updated
- Custom Record Deleted

## Credentials

To use this node, you need to configure Arivo API credentials:

### Prerequisites
1. Sign up for an Arivo CRM account at [arivo.com.br](https://arivo.com.br)
2. Log in to your Arivo CRM account
3. Navigate to API Keys management at [arivo.com.br/api_keys](https://arivo.com.br/api_keys)
4. Generate a new API key for n8n integration

### Configuration
1. In n8n, create a new credential of type "Arivo API"
2. Enter your API key in the "API Key" field
3. Test the connection to verify the credentials work correctly

The API key will be used for authentication using the Token method as described in the [Arivo API documentation](https://arivo.docs.apiary.io).

## Compatibility

This package has been tested with recent n8n versions and requires Node.js >= 20.15.

## Usage

### Contact Management
- Create and manage person and company contacts
- Add phones, emails, and addresses
- Configure custom fields
- Associate contacts with deals and tasks

### Sales Opportunities
- Create and track sales deals
- Add products and services to deals
- Set up custom sales pipelines
- Monitor progress through pipeline stages

### Activities and Tasks
- Schedule and manage activities
- Configure recurring tasks
- Associate activities with contacts and deals
- Mark activities as completed

### Automation with Webhooks
- Set up triggers for CRM events
- Automate workflows based on data changes
- Receive real-time notifications
- Integrate with other systems

### AI Agent Integration
- Use Arivo nodes as tools for AI agents in n8n workflows
- Enable AI agents to autonomously manage CRM data
- Allow AI to create, update, and retrieve contacts, deals, tasks, and notes
- Integrate CRM operations into AI-powered automation workflows

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Arivo API Documentation](https://arivo.docs.apiary.io)

## Version history

### 1.3.0

- Add custom record trigger events with definition-aware webhooks and UI configuration

### 1.2.0

- Add trigger events for deal lifecycle: Deal Won, Deal Lost, and Deal Reopened

### 1.1.0

- Enable use of Arivo nodes as AI agent tools

### 1.0.0

- Initial release
- Complete CRUD operations for contacts (persons and companies), deals, notes, tasks, products, product categories, files, and custom records
- Comprehensive webhook triggers for all major events
- Support for phone, email, and address management
- Custom fields and load options support
- Extensive test coverage with 390+ tests 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
