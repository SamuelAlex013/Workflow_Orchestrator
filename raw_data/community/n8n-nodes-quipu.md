<div align="center">

# n8n-nodes-quipu

**Quipu integration for n8n - invoice and taxes software for freelancers and
companies**

<p>
<img alt="Static Badge" src="https://img.shields.io/badge/Status-experimental-orange" />
</p>

</div>

This is an n8n community node. It lets you use Quipu in your n8n workflows.

Quipu is an invoice and taxes software as a service for freelancers and
companies that helps you manage accounting, invoicing, and tax filing in one
place.

[n8n](https://n8n.io/) is a
[fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation
platform.

[Installation](#installation) [Operations](#operations)
[Credentials](#credentials) [Compatibility](#compatibility)
[Development](#development) [Resources](#resources)

## Installation

Follow the
[installation guide](https://docs.n8n.io/integrations/community-nodes/installation/)
in the n8n community nodes documentation.

```bash
npm install n8n-nodes-quipu
```

## Operations

This node supports the following Quipu API operations:

### Contacts

- Get all contacts
- Get a contact by ID
- Create a new contact
- Update a contact
- Delete a contact

### Invoices

- Get all invoices
- Get an invoice by ID
- Create a new invoice
- Update an invoice
- Delete an invoice

### Tickets

- Get all tickets
- Get a ticket by ID
- Create a new ticket
- Update a ticket
- Delete a ticket

### Paysheets

- Get all paysheets
- Get a paysheet by ID
- Create a new paysheet
- Update a paysheet
- Delete a paysheet

### Other Operations

- Get all book entries
- Get all accounting categories and subcategories
- Manage numbering series for invoices and tickets
- Upload and manage attachments

## Credentials

You need to obtain OAuth2 credentials from Quipu to authenticate with the API.

### Prerequisites

1. Sign up for a Quipu account at [getquipu.com](https://getquipu.com/)
2. [Enable API](https://getquipu.com/d/aldoborrero/integrations)
3. Generate the credentials

### Setting up credentials in n8n

1. Open your n8n workflow
2. Click on the Quipu node
3. Click on _Create new credential_
4. Enter your Client ID and Client Secret
5. Click _Save_

The node automatically handles token generation and renewal using the OAuth2
client credentials flow.

## Compatibility

This node has been tested with n8n version 1.0+ and Quipu API v1.

## Development

### Standard Development

If you want to contribute to this node, you can set up your development
environment as follows:

```bash
# Clone the repository
git clone https://github.com/aldoborrero/n8n-nodes-quipu.git
cd n8n-nodes-quipu

# Install dependencies
npm install

# Build the node
npm run build

# Run in development mode
npm run dev
```

### Development with Nix

This project provides a Nix flake for a reproducible development environment.

#### Prerequisites

- [Nix package manager](https://nixos.org/download.html) installed on your
  system
- [direnv](https://direnv.net/) (optional but recommended)

#### Setup with direnv

If you have direnv installed and configured, simply clone the repository and
enter the directory:

```bash
git clone https://github.com/aldoborrero/n8n-nodes-quipu.git
cd n8n-nodes-quipu
direnv allow
```

This will automatically set up your development environment based on the flake.

#### Manual Nix Shell

If you don't use direnv, you can manually enter the development environment:

```bash
nix develop
```

You can create a `.envrc.local` file for your personal environment
customizations. This file is gitignored and will be automatically loaded by
direnv.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Quipu API documentation](https://getquipu.com/en/integrations)
- [Quipu website](https://getquipu.com/)

## Support

If you have any questions or issues with this node, please:

1. Check the [n8n community forum](https://community.n8n.io/) for existing
   solutions
2. Open an issue on the
   [GitHub repository](https://github.com/aldoborrero/n8n-nodes-quipu)
