# PDF Tools Node for n8n

A powerful n8n node for PDF manipulation that provides a comprehensive set of tools for working with PDF files.

## Features

### PDF Operations

- **Add Image**: Add images to PDF pages with customizable positioning and scaling
- **Add Watermark**: Add text watermarks with customizable font size, color, and opacity
- **Delete Pages**: Remove specific pages from a PDF
- **Extract Pages**: Extract specific pages into a new PDF
- **Extract Text**: Extract text content from PDF files
- **Merge PDFs**: Combine multiple PDFs into a single document
- **Read Metadata**: Extract PDF metadata (title, author, subject, etc.)
- **Reorder Pages**: Change the order of pages in a PDF
- **Rotate Pages**: Rotate specific pages by 90, 180, or 270 degrees
- **Split PDF**: Split a PDF into multiple files

## Installation

1. Install the node in your n8n instance:
```bash
npm install n8n-nodes-pdf-tools
```

2. Restart your n8n server

## Usage

### Add Image to PDF

Add an image to specific pages of a PDF with customizable positioning:

```javascript
// Example workflow
{
  "operation": "addImage",
  "pdfBinaryName": "input.pdf",
  "imageBinaryName": "logo.png",
  "pageTarget": "1,3-5",
  "imageOptions": {
    "x": 50,
    "y": 400,
    "scale": 0.5
  }
}
```

### Add Watermark

Add a text watermark to PDF pages:

```javascript
// Example workflow
{
  "operation": "watermark",
  "pdfBinaryName": "input.pdf",
  "watermarkText": "CONFIDENTIAL",
  "pageTarget": "all",
  "watermarkOptions": {
    "fontSize": 72,
    "color": "#FF0000",
    "opacity": 0.5
  }
}
```

### Merge PDFs

Combine multiple PDFs into a single document:

```javascript
// Example workflow
{
  "operation": "merge",
  "pdfBinaryNames": "pdf1.pdf,pdf2.pdf,pdf3.pdf"
}
```

### Page Management

Various operations for managing PDF pages:

```javascript
// Delete pages
{
  "operation": "delete",
  "pdfBinaryName": "input.pdf",
  "pages": "1,3-5"
}

// Extract pages
{
  "operation": "extractPages",
  "pdfBinaryName": "input.pdf",
  "pages": "1-3"
}

// Reorder pages
{
  "operation": "reorder",
  "pdfBinaryName": "input.pdf",
  "newPageOrder": "3,1,2"
}

// Rotate pages
{
  "operation": "rotate",
  "pdfBinaryName": "input.pdf",
  "pages": "1-3",
  "rotationAngle": 90
}
```

## Supported Formats

- **PDF**: application/pdf
- **Images**: 
  - PNG (image/png)
  - JPEG (image/jpeg)

## Page Selection Format

The node supports various page selection formats:
- Single page: "1"
- Multiple pages: "1,3,5"
- Page ranges: "1-5"
- All pages: "all"

## Error Handling

The node includes comprehensive error handling for:
- Invalid file formats
- Invalid page numbers
- Missing required parameters
- File processing errors

## Dependencies

- pdf-lib: For PDF manipulation
- pdf-parse: For text extraction

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please:
1. Check the [documentation](https://docs.n8n.io)
2. Open an issue on GitHub
3. Join the [n8n community](https://community.n8n.io)

