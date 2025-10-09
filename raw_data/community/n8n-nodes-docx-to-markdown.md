# n8n-nodes-docx-to-markdown

A professional n8n community node package that provides powerful document conversion capabilities for your workflows.

This package enables seamless conversion of DOCX documents and HTML content to clean, well-formatted Markdown within your n8n automation workflows. Perfect for content processing, documentation workflows, and data transformation pipelines.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[![npm version](https://badge.fury.io/js/n8n-nodes-docx-to-markdown.svg)](https://badge.fury.io/js/n8n-nodes-docx-to-markdown)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

✅ **DOCX to Markdown Conversion** - Convert Microsoft Word documents to clean Markdown  
✅ **HTML to Markdown Conversion** - Transform HTML content into well-formatted Markdown  
✅ **Multiple Output Modes** - JSON field output or binary file output  
✅ **Structure Preservation** - Maintains headings, lists, and table formatting  
✅ **Image Handling** - Converts embedded images to base64 data URIs  
✅ **Flexible Input Sources** - Support for binary files and text fields  
✅ **Content Sanitization** - Built-in HTML sanitization for security  
✅ **Professional Error Handling** - Comprehensive validation and error reporting

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Install

```bash
npm install n8n-nodes-docx-to-markdown
```

Or install directly in n8n:
1. Go to **Settings** → **Community Nodes**
2. Enter: `n8n-nodes-docx-to-markdown`
3. Click **Install**

## Nodes

### DOCX → Markdown

Convert Microsoft Word (.docx) documents to Markdown format.

**Key Features:**
- Support for complex document structures (headings, lists, tables)
- Image conversion with base64 encoding
- Flexible output options (JSON field or binary file)
- Document metadata preservation
- Conversion warnings and error reporting

**Configuration Options:**
- **Binary Property**: Source property containing the DOCX file
- **Output Mode**: Choose between JSON field or binary file output
- **Preserve Structure**: Maintain document formatting and structure
- **Include HTML**: Optionally include HTML version in output

### HTML → Markdown

Convert HTML content to clean, readable Markdown with flexible input and output options.

**Key Features:**
- **Dual Input Modes**: Support for binary HTML files or direct text input
- **Conversion Modes**: Default settings or fully customizable options
- **Advanced Sanitization**: Built-in HTML cleaning and security filtering
- **Flexible Output**: JSON field output or binary .md file generation
- **Content Control**: Length limits, domain filtering, and structure preservation

**Configuration Options:**
- **Input Mode**: Choose between text field or binary file input
- **Conversion Mode**: 
  - **Default Settings**: Optimized defaults for any HTML content
  - **Custom Options**: Full control over conversion parameters
- **Custom Options** (when enabled):
  - **Preserve Tables**: Maintain HTML table formatting in Markdown
  - **Include Image Alt Text**: Extract and include image alt attributes
  - **Preserve Line Breaks**: Keep original line break formatting
  - **Max Length**: Set content length limits (0 = no limit)
  - **Allowed Domains**: Whitelist trusted domains for links and images
- **Output Mode**: JSON field or binary .md file output
- **Include Original HTML**: Optionally preserve original HTML in JSON output

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: ≥20.15
- **Tested with**: n8n 1.112.1+

## Usage Examples

### Basic DOCX Conversion

1. Add a **DOCX → Markdown** node to your workflow
2. Connect it to a node that provides DOCX files (e.g., HTTP Request, Google Drive)
3. Configure the binary property name (default: "data")
4. Choose output mode (JSON field or binary file)
5. Execute the workflow

### HTML Processing Pipeline

**Text Input Example:**
1. Use **HTTP Request** to fetch HTML content
2. Add **HTML → Markdown** node
3. Set **Input Mode** to "Text (HTML String)"
4. Choose **Conversion Mode** (Default Settings or Custom Options)
5. Configure output mode (JSON field or binary file)
6. Process the converted Markdown in subsequent nodes

**Binary File Example:**
1. Use **HTTP Request** with `responseFormat: "file"` to download HTML file
2. Add **HTML → Markdown** node
3. Set **Input Mode** to "Binary (HTML File)"
4. Specify the binary property name (default: "data")
5. Configure conversion and output options as needed

### Advanced Document Processing

**DOCX to Markdown Example:**
```json
{
  "nodes": [
    {
      "name": "Get DOCX",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://example.com/document.docx",
        "responseFormat": "file"
      }
    },
    {
      "name": "Convert DOCX to Markdown",
      "type": "n8n-nodes-docx-to-markdown.docxToMarkdown",
      "parameters": {
        "outputMode": "json",
        "markdownField": "content",
        "includeHtml": true,
        "preserveStructure": true
      }
    }
  ]
}
```

**HTML to Markdown Example:**
```json
{
  "nodes": [
    {
      "name": "Get HTML",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://example.com/page.html",
        "responseFormat": "file"
      }
    },
    {
      "name": "Convert HTML to Markdown",
      "type": "n8n-nodes-docx-to-markdown.htmlToMarkdown",
      "parameters": {
        "inputMode": "binary",
        "binaryPropertyName": "data",
        "conversionMode": "custom",
        "preserveTables": true,
        "includeImageAlt": true,
        "maxLength": 5000,
        "outputMode": "json",
        "markdownField": "markdown"
      }
    }
  ]
}
```

## Development

### Prerequisites

- Node.js ≥20.15
- npm or yarn
- n8n installed globally

### Setup

```bash
# Clone the repository
git clone https://github.com/scoupleuxSG/n8n-node-docx-to-markdown-new.git

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint

# Auto-fix linting issues
npm run lintfix
```

### Testing Locally

1. Build the project: `npm run build`
2. Link the package: `npm link`
3. In your n8n installation: `npm link n8n-nodes-docx-to-markdown`
4. Restart n8n to load the nodes

## Dependencies

- **mammoth**: DOCX to HTML conversion
- **turndown**: HTML to Markdown conversion
- **jsdom**: HTML parsing and manipulation
- **sanitize-html**: HTML content sanitization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE.md) © 2025 Stephane Coupleux

## Support
- 🐛 Issues: [GitHub Issues](https://github.com/scoupleuxSG/n8n-node-docx-to-markdown-new/issues)
- 📖 n8n Community: [n8n Community Forum](https://community.n8n.io/)

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/#community-nodes)
- [n8n Node Development Guide](https://docs.n8n.io/integrations/creating-nodes/)
- [Mammoth.js Documentation](https://github.com/mwilliamson/mammoth.js)
- [Turndown Documentation](https://github.com/mixmark-io/turndown)
