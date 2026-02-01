# n8n-nodes-docx-to-md

This is an n8n community node. It lets you convert Microsoft Word documents (.docx) to Markdown format in your n8n workflows.

This node provides seamless conversion of Word documents to clean, GitHub-flavored Markdown with automatic formatting correction and linting.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The Docx to Markdown node supports the following operation:

- **Convert**: Converts a Microsoft Word document (.docx) from binary data to clean Markdown format

### Features

- Converts Word documents to GitHub-flavored Markdown
- Automatically converts tables with proper headers
- Applies markdown linting and formatting corrections
- Preserves document structure and formatting
- Supports headings, lists, tables, and basic text formatting
- **Option to remove images** from the converted Markdown output

## Compatibility

- Minimum n8n version: 1.0.0
- Tested with n8n versions: 1.0.0+
- Compatible with all n8n deployment methods (self-hosted, cloud, desktop)

## Usage

### Basic Setup

1. Add the "Docx to Markdown" node to your workflow
2. Configure the **Input Binary Field** parameter with the name of the field containing your Word document binary data (default: "data")
3. Configure the **Destination Output Field** parameter with the name where you want the converted Markdown text to be stored (default: "text")
4. Optionally, enable **Remove Images** if you want to exclude all images from the converted Markdown (default: false)

### Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| Input Binary Field | String | "data" | Name of the field containing the Word document binary data |
| Destination Output Field | String | "text" | Name of the field where converted Markdown will be stored |
| Remove Images | Boolean | false | Whether to remove all images from the converted Markdown |

### Example Workflow

1. Use an HTTP Request node or file input to get a .docx file
2. Connect it to the Docx to Markdown node
3. The converted Markdown will be available in the specified output field
4. Use the Markdown output in subsequent nodes (e.g., save to file, send via email, etc.)

### Tips

- The node automatically handles table formatting by converting the first row to headers
- All markdown output is linted and formatted for consistency
- Binary data should be in proper .docx format for best results
- Use the "Remove Images" option when you need clean text-only output without image references
- Images in Word documents are typically converted to markdown image syntax (`![alt](src)`) unless the Remove Images option is enabled

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Mammoth.js documentation](https://github.com/mwilliamson/mammoth.js/) (underlying conversion library)
- [Turndown documentation](https://github.com/mixmark-io/turndown) (HTML to Markdown converter)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
