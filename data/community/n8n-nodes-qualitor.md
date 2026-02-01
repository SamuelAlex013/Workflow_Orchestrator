# n8n-nodes-qualitor

This is an n8n community node. It lets you use Qualitor SOAP API in your n8n workflows.

Qualitor is a Brazilian service management platform that provides ITSM (IT Service Management) solutions for businesses. This node allows you to integrate with Qualitor's SOAP webservices to manage tickets, services, and general operations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Manual Installation

1. Install the package in your n8n installation:
   ```bash
   npm install n8n-nodes-qualitor
   ```

2. Restart your n8n instance to load the new node.

## Operations

The Qualitor node supports three main service types:

### General Services (`wsgeneral.wsdl`)
- Access to general Qualitor operations
- Used for system-wide functions and configurations

### Ticket Services (`wsticket.wsdl`)
- Ticket creation, retrieval, and updates
- Ticket status management
- Ticket field operations

### Service Management (`wsservice.wsdl`)
- Service catalog operations
- Service request management
- Service configuration

### Available Operations

For each service type, you can specify any operation name (e.g., `getTicket`, `createTicket`, `updateTicket`) and provide the required fields as key-value pairs.

## Credentials

To use this node, you need to configure the Qualitor API credentials:

### Required Fields

- **Qualitor Base URL**: The base URL of your Qualitor instance (e.g., `https://qualitor.example.com/qualitor`)
- **Company ID**: The ID of the company to which the user belongs (numeric value)
- **Username**: Your Qualitor username for authentication
- **Password**: Your Qualitor password for authentication

### Setting up Credentials

1. In n8n, go to **Credentials** → **Create New**
2. Search for "Qualitor API" and select it
3. Fill in all required fields
4. Test the connection to ensure it works
5. Save the credentials

## Compatibility

- **n8n version**: 1.0.0 or higher
- **Node.js version**: 20.15 or higher
- **Qualitor API**: Compatible with Qualitor SOAP webservices

## Usage

### Basic Example: Get Ticket Information

1. Add the Qualitor node to your workflow
2. Select your Qualitor API credentials
3. Choose the service: "Ticket" (`wsticket.wsdl`)
4. Set the operation: `getTicket`
5. Add fields:
   - Field Name: `cdchamado`
   - Field Value: `123456` (your ticket ID)
6. Enable "Parse Response" to get JSON output

### Example: Create a New Ticket

1. Add the Qualitor node to your workflow
2. Select your Qualitor API credentials
3. Choose the service: "Ticket" (`wsticket.wsdl`)
4. Set the operation: `createTicket`
5. Add required fields for ticket creation:
   - `titulo`: "Issue title"
   - `descricao`: "Issue description"
   - `prioridade`: "2"
   - And other required fields according to your Qualitor configuration

### Configuration Options

- **Parse Response**: When enabled, the node will parse the SOAP XML response into JSON format for easier processing in subsequent nodes. When disabled, returns raw XML.
- **Fields**: Add multiple key-value pairs to send as parameters to the SOAP operation.

## Features

- ✅ Support for all three Qualitor SOAP services (General, Ticket, Service)
- ✅ Flexible operation specification
- ✅ Dynamic field configuration
- ✅ XML to JSON response parsing
- ✅ Raw XML response option
- ✅ Secure credential management
- ✅ TypeScript implementation

## Resources

- [Qualitor Official Documentation](https://www.qualitor.com.br/docs/8.10.08.20170713/integracao/index.html)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [n8n Workflow Automation Platform](https://n8n.io/)

## Development

If you want to contribute to this node or modify it for your needs:

```bash
# Clone the repository
git clone https://github.com/juniorfontenele/n8n-qualitor.git

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint

# Auto-fix linting issues
npm run lintfix
```

## License

[MIT](LICENSE.md)

## Author

**Junior Fontenele**
- Email: n8n@juniorfontenele.com.br
- GitHub: [@juniorfontenele](https://github.com/juniorfontenele)

## Support

If you encounter any issues or have questions:

1. Check the [Qualitor documentation](https://www.qualitor.com.br/docs/8.10.08.20170713/integracao/index.html)
2. Review the [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
3. Open an issue on the [GitHub repository](https://github.com/juniorfontenele/n8n-qualitor/issues)
