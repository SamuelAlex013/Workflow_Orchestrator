# n8n-nodes-docugenerate

This is an n8n community node. It lets you use [DocuGenerate](https://www.docugenerate.com/) in your n8n workflows.

DocuGenerate is a powerful document generation service that creates high-quality PDF documents from Word templates using
merge tags. Automatically populate templates with dynamic data to generate invoices, contracts, reports, and other
business documents.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community
nodes documentation.

## Operations

**Document Operations:**
- **Generate Document** - Create a document from a template with your data
- **List Documents** - Get all documents generated from a specific template
- **Get Document** - Retrieve details of a specific generated document
- **Update Document** - Change the name of a generated document
- **Delete Document** - Remove a generated document

**Template Operations:**
- **List Templates** - Retrieve all available templates
- **Get Template** - Fetch details of a specific template including merge tags
- **Delete Template** - Remove a template from your account

## Credentials

You need a DocuGenerate API Key to use this node.

### Prerequisites
1. Sign up for a [DocuGenerate account](https://app.docugenerate.com/signup)
2. Get your unique API Key from the Developers tab in the [Settings](https://app.docugenerate.com/settings/developers) page.

### Authentication Setup
1. In n8n, go to **Credentials** → **Create New**
2. Search for **DocuGenerate API** 
3. Enter your API Key
4. Test the connection
5. Save the credential

## Compatibility

- **Minimum n8n version:** 0.198.0
- **Tested with:** n8n 1.0+
- **Node API version:** 1

## Usage

### Generating Documents

The most common workflow is generating documents from templates:

```
HTTP Request (get data) → DocuGenerate (Generate Document)
```

**Data Field:** By default, the data field uses `{{ $json }}` to automatically populate with data from the previous
node. You can also manually customize the JSON structure to match your template's merge tags.

**Supported Output Formats:**
- Microsoft Word (.docx, .doc)
- PDF (.pdf) 
- OpenDocument (.odt)
- Plain Text (.txt)
- PNG (.png)

### Template Data Structure

DocuGenerate templates use merge tags like `[Name]`, `[Address]`, etc. Your data should be structured as JSON arrays:

```json
[{
  "Name": "John Doe",
  "Address": "123 Main St",
  "Items": [
    {"Product": "Widget", "Price": "$10.00"},
    {"Product": "Gadget", "Price": "$15.00"}
  ]
}]
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [DocuGenerate API Reference](https://api.docugenerate.com/)
* [DocuGenerate Website](https://www.docugenerate.com/)
* [Template Creation Guide](https://www.docugenerate.com/help/templates/)

## Version History

### 1.0.0 (2025-07-21)
- Initial release
- Template and document operations
- Dynamic template dropdown loading
- Populate data field with previous node data by default
