# n8n-nodes-unleashed

This is an n8n community node for integrating with the [Unleashed](https://www.unleashedsoftware.com/) inventory management system. It allows you to automate workflows with Unleashed using n8n.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Features

This node integrates with the Unleashed API and provides functionality to:

- Query and retrieve sales orders, invoices, and other Unleashed resources
- Create new sales orders with detailed line items
- Update existing sales orders including delivery instructions
- Complete sales orders in the Unleashed system
- Access multiple API endpoints with authentication handling built-in

## Installation

Follow these steps to install this node in your n8n instance:

### Community Nodes (Recommended)

For users on n8n Cloud:

1. Go to **Settings > Community Nodes**
2. Select **Install Community Node**
3. Enter `n8n-nodes-unleashed` in the **Enter npm package name** field
4. Click **Install**

For self-hosted n8n users:

```bash
npm install n8n-nodes-unleashed
```

### Manual Installation

1. Clone the repository into your custom nodes directory:
```bash
git clone https://github.com/neilcayton/n8n-nodes-unleashed.git
```

2. Install dependencies:
```bash
cd n8n-nodes-unleashed
npm install
```

3. Build the code:
```bash
npm run build
```

4. Restart n8n

## Usage

After installing the node, it will appear in the nodes panel under "Unleashed" category.

### Credentials

To use the node, you need to create an Unleashed API credential:

1. Get your API ID and API Key from the Unleashed Developer Portal
2. Create a new "Unleashed API" credential in n8n
3. Enter your API ID and API Key

### Operations

The node currently supports the following operations:

#### Sales Orders
- **Get**: Retrieve a specific sales order by ID
- **Get All**: List all sales orders with optional filtering
- **Create**: Create a new sales order with customer details, line items, and delivery instructions
- **Update**: Update an existing sales order
- **Complete**: Mark a sales order as complete

### Example Workflow

Here's an example of how to use this node to create a new sales order in Unleashed:

1. Add the **Unleashed** node to your workflow
2. Select the **Sales Order** resource
3. Choose the **Create** operation
4. Configure the node with customer code, order details, and line items
5. Connect to other nodes in your workflow to process the response

## Resources & Links

* [Unleashed API Documentation](https://apidocs.unleashedsoftware.com/)
* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](LICENSE.md)
