![PDFMonkey for n8n](./images/n8n-nodes-pdfmonkey.webp)

# n8n-nodes-pdfmonkey

This is an n8n community node. It lets you use PDFMonkey in your n8n workflows.

[PDFMonkey](https://www.pdfmonkey.io/) is a service that allows you to generate PDFs from HTML templates with dynamic data.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### PDFMonkey Node

The PDFMonkey node provides the following operations:

- **Generate Document**: Create a new PDF document using a template and dynamic data
  - Supports custom metadata and filename customization
  - Optional auto-polling for document completion (controlled by "Wait For Completion" option)
  - Uses a simple 2-second interval between status checks when polling
  - Downloads the PDF automatically if generation is successful and auto-polling is enabled
- **Get Document**: Get document details and check its generation status
- **Download File**: Download a generated PDF or image document and save it as a binary file
- **Delete Document**: Delete a previously generated PDF document from PDFMonkey

### PDFMonkey Trigger Node

The PDFMonkey Trigger node listens for webhooks from PDFMonkey and processes them:

- **Webhook Receiver**: Triggers when PDFMonkey sends a webhook notification
- **Automatic File Download**: Automatically downloads the PDF or image when the document generation is successful
- **Intelligent Filename Handling**: Extracts the filename from metadata
- **Complete Response Data**: Returns all document properties from the PDFMonkey API in the JSON output

## Credentials

To use the PDFMonkey nodes, you need to have a PDFMonkey account and API key.

1. Sign up for PDFMonkey at [https://www.pdfmonkey.io/](https://www.pdfmonkey.io/)
2. In your PDFMonkey dashboard, navigate to the API section
3. Copy your API key
4. In n8n, create new credentials of type 'PDFMonkey API' and paste your API key

## Compatibility

This node has been tested with n8n version 1.0.0 and later.

## Usage

### Flexible Payload Input

The Generate Document operation supports two methods for providing template data:

1. **JSON Format**:

   - Enter your entire payload as a JSON object
   - Ideal for complex data structures or when copying from another source
   - Example:
     ```json
     {
     	"invoiceNumber": "INV-2023-001",
     	"customerName": "Acme Inc.",
     	"items": [
     		{ "name": "Widget", "quantity": 5, "price": 10.99 },
     		{ "name": "Gadget", "quantity": 2, "price": 24.99 }
     	],
     	"total": 104.93
     }
     ```

2. **Key-Value Pairs**:
   - Add fields individually with key-value pairs
   - More visual and easier to manage for simple templates
   - Supports complex data structures:
     - JSON objects/arrays: Values starting with `{` or `[` are automatically parsed as JSON
     - Arrays from other nodes: The node automatically handles n8n's special array format `[Array: [...]]`
     - Direct objects: When passing data from other nodes that return objects, they are used directly

### Enhanced Object Handling

The node intelligently processes different value types in key-value pairs:

- **Direct Objects**: Objects passed directly from other nodes are preserved intact
- **JSON Strings**: Strings that look like JSON (starting with `{` or `[`) are parsed automatically
- **Special Array Format**: The n8n array format `[Array: [...]]` is detected and parsed
- **Regular Values**: Simple strings, numbers, and booleans are handled appropriately

This makes it easy to pass complex data from other nodes to PDFMonkey without manual conversion.

#### Example: Processing Arrays from n8n

When you map data from other nodes (like Function or HTTP Request nodes), arrays often come in this special format:

```
[Array: [{"name":"Mouse","quantity":3,"price":88.92},{"name":"Headphones","quantity":5,"price":14.99},{"name":"Keyboard","quantity":3,"price":48.28}]]
```

The PDFMonkey node will automatically detect this format, extract the array content, and properly parse it as a JSON array. This is especially useful for templating tables or lists in your PDFs where you need to pass complex structured data.

### Generate Document with Auto-Polling

The Generate Document operation includes a "Wait For Completion" option that controls whether the node waits for the document to finish generating before continuing the workflow:

1. When **enabled** (default):

   - The node checks the document status every 2 seconds until it reaches a final state (success or failure)
   - If successful, it automatically downloads the PDF or image and returns it as a binary file
   - Simple, straightforward polling mechanism with minimal overhead
   - Progress is logged with status updates during polling

2. When **disabled**:
   - The node returns immediately after creating the document
   - The response includes the document ID and initial pending status
   - You can later use the Get Document or Download File operations to check status and retrieve the document

This feature is especially useful for smaller documents that generate quickly, providing a simpler workflow without needing separate Get Document and Download File steps. For larger documents that take longer to generate, you may want to disable this option and use a separate Get Document or Download File operation later.

### Custom Filenames

You can set a custom filename for your generated PDF or image using the dedicated `Custom Filename` field in the Generate Document operation

If the field is left empty, the node will use the default generated filename.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [PDFMonkey API Documentation](https://docs.pdfmonkey.io/)
