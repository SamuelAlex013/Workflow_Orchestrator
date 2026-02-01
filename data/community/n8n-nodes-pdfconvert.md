# n8n-nodes-pdfconvert

This package contains the PDF Convert node for [n8n](https://n8n.io). It provides functionality to convert PDF files into individual page images (PNG/JPG format).

## Features

- ✅ Convert PDF files to images (PNG or JPG)
- ✅ Process all pages or specific page ranges
- ✅ Configurable image scale/resolution  
- ✅ Support for binary data and base64 input
- ✅ Lightweight implementation using pdf-img-convert
- ✅ Perfect for scanned PDFs and image extraction

## Installation

To install this community node, follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n docs.

### Manual Installation

```bash
npm install n8n-nodes-pdfconvert
```

## Usage

### Node Configuration

The PDF Convert node provides the following configuration options:

#### Input Type
- **Binary Data**: Use PDF data from file uploads or previous nodes
- **Base64**: Use base64-encoded PDF string

#### Output Options
- **Output Format**: Choose PNG or JPG for resulting images
- **Scale**: Control image resolution (0.5x to 5x, default 2x)
- **Pages**: Specify pages to convert (e.g., "1,2,3" or "1-5" or leave empty for all)

#### Input/Output Properties
- **Binary Property**: Name of input property containing PDF data (default: "data")
- **Output Property Name**: Name for output property containing converted images (default: "images")

### Examples

#### Example 1: Convert all PDF pages to PNG
```
Input: PDF file via HTTP Request or File node
Configuration:
- Input Type: Binary Data
- Output Format: PNG
- Scale: 2
- Pages: (empty - converts all pages)
```

#### Example 2: Convert specific pages to high-res JPG
```
Input: PDF file
Configuration:
- Input Type: Binary Data  
- Output Format: JPG
- Scale: 3
- Pages: 1,3-5,10
```

#### Example 3: Convert base64 PDF to images
```
Input: Base64 PDF string
Configuration:
- Input Type: Base64
- Base64 Data: {{$json.pdfBase64}}
- Output Format: PNG
- Scale: 2
```

### Output Format

The node outputs:
- **JSON Data**: Metadata about converted images
- **Binary Data**: Individual page images as binary data

JSON output structure:
```json
{
  "images": [
    {
      "data": Buffer,
      "mimeType": "image/png",
      "fileName": "page_1.png", 
      "fileExtension": "png",
      "pageNumber": 1
    }
  ],
  "totalPages": 3,
  "outputFormat": "png",
  "scale": 2
}
```

Binary output: Each page is also available as binary data with property names like `images_page_1`, `images_page_2`, etc.

## Use Cases

- Extract pages from scanned documents
- Convert PDF presentations to image slides
- Generate thumbnails from PDF files
- Process invoices/receipts for OCR workflows
- Archive PDF content as individual images

## Technical Details

- Built with TypeScript for n8n
- Uses pdf-img-convert library (lightweight, PDF.js-based)
- No external dependencies (GraphicsMagick, Ghostscript)
- Supports Node.js 20.15+

## Development

### Prerequisites

- Node.js >= 20.15
- n8n installed globally: `npm install n8n -g`

### Setup

1. Clone the repository
2. Install dependencies: `npm install`
3. Build the node: `npm run build`
4. Link for development: `npm link`

### Testing

```bash
npm run lint        # Check code quality
npm run build       # Build the project
npm run dev         # Watch mode for development
```

## License

[MIT](LICENSE.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions:
1. Check the [n8n documentation](https://docs.n8n.io/integrations/community-nodes/)
2. Open an issue on [GitHub](https://github.com/movalex/n8n-nodes-pdfconvert/issues)

---

Made with ❤️ for the n8n community