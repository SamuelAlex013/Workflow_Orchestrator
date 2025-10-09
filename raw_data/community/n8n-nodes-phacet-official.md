# n8n-nodes-phacet

![Phacet Logo](https://raw.githubusercontent.com/spx-software/n8n-phacet-official/main/nodes/Phacet/phacet.svg)

This is an n8n community node for [Phacet](https://phacetlabs.com), a powerful AI-driven spreadsheet platform. It allows you to upload files and manage spreadsheet data directly from your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (n8n Cloud & Self-hosted)

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-phacet-official`
4. Select **Install**

Once installed, the Phacet node will be available in your node palette.

## Operations

### File Operations
- **Upload**: Upload PDF files to Phacet for processing

### Row Operations
- **Create**: Create new rows in Phacet spreadsheets with dynamic column mapping

## Credentials

You need a Phacet API key to use this node.

### Getting your Phacet API Key

1. Log in to your [Phacet dashboard](https://app.phacetlabs.com)
2. Go to **Settings** or **API Settings**
3. Generate a new API key
4. Copy the API key

### Setting up the credential in n8n

1. In n8n, create a new **Phacet API** credential
2. Enter your API key in the **API Key** field
3. Save the credential

## Compatibility

- **n8n version**: 1.0.0 or later
- **Node version**: 18.0.0 or later

## Usage

### Upload Files

Use the **Upload** operation to send PDF files to Phacet:

1. Add the Phacet node to your workflow
2. Select **File** as the resource
3. Select **Upload** as the operation
4. Configure your file input (usually from a previous node)
5. The node returns the uploaded file information including the file ID

### Create Rows

Use the **Create** operation to add new rows to your Phacet spreadsheets:

1. Add the Phacet node to your workflow
2. Select **Row** as the resource
3. Select **Create** as the operation
4. Choose your **Phacet** from the dynamic dropdown
5. Choose your **Session** from the dynamic dropdown (based on selected phacet)
6. Map your data to **Columns** using the dynamic column selector
7. The node returns the created row information

### Dynamic Dropdowns

This node features intelligent dynamic dropdowns that:
- Load your available phacets automatically
- Show sessions based on your selected phacet
- Display column names (not just IDs) for easy mapping
- Update in real-time as you make selections

## Example Workflows

### PDF Processing Pipeline
```
Email Trigger → Extract Attachments → Phacet Upload → Create Row with File ID
```

### Data Import Workflow
```
HTTP Request → JSON Processing → Phacet Create Row → Notification
```

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Phacet API Documentation](https://docs.phacetlabs.com/reference/authentication-1)
- [Phacet Platform](https://phacetlabs.com)

## License

[MIT](LICENSE.md)

---

**Developed by [Phacet Labs](https://phacetlabs.com)**