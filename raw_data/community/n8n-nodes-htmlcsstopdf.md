# n8n-nodes-htmlcsstopdf

![HTML to PDF Banner](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

An n8n community node for converting HTML content to PDF documents and capturing website screenshots as PDFs using the PDFMunk API.

## Features

- **HTML to PDF**: Convert custom HTML/CSS content to PDF documents
- **Website to PDF**: Capture full-page website screenshots as PDF files
- **Flexible Output**: Support for URL, PNG, and Base64 response formats
- **Customizable Viewport**: Configure viewport dimensions for optimal rendering
- **Full Page Capture**: Option to capture entire web pages or specific viewport areas

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install via n8n's Community Nodes feature:
1. Go to Settings > Community Nodes in your n8n instance
2. Install `n8n-nodes-htmlcsstopdf`

Or install manually:
```bash
npm install n8n-nodes-htmlcsstopdf
```

## Installation

<<<<<<< HEAD
- n8n version 0.187.0 or higher
- PDFMunk API credentials (sign up at [PDFMunk](https://pdfmunk.com))

## Credentials

This node requires PDFMunk API credentials:

1. Create an account at [PDFMunk](https://pdfmunk.com)
2. Generate your API key from the dashboard
3. In n8n, create new credentials of type "HTMLCSStoPDF API"
4. Enter your PDFMunk API key

## Operations

### HTML to PDF
Convert custom HTML and CSS content into PDF documents.

**Parameters:**
- **HTML Content**: The HTML content to convert
- **CSS Content**: Optional CSS styling for the HTML
- **Viewport Width**: Viewport width in pixels (default: 1080)
- **Viewport Height**: Viewport height in pixels (default: 720)
- **Response Format**: Choose between URL, PNG, or Base64 output

**Example Use Cases:**
- Generate invoices from HTML templates
- Create reports with custom styling
- Convert rich text content to PDF documents

### URL to PDF
Capture website screenshots and save them as PDF documents.

**Parameters:**
- **URL**: The website URL to capture
- **Full Page**: Capture the entire page (default: true)
- **Wait Time**: Milliseconds to wait before capturing (default: 10000)
- **Viewport Width**: Viewport width in pixels (default: 1080)
- **Viewport Height**: Viewport height in pixels (default: 720)

**Example Use Cases:**
- Archive web pages as PDFs
- Generate website screenshots for documentation
- Create visual reports of web content

## Example Workflows

### Generate Invoice PDF
```javascript
// Previous node provides customer data
{
  "operation": "htmlToPdf",
  "html_content": `
    <html>
      <body>
        <h1>Invoice #{{$json.invoiceNumber}}</h1>
        <p>Customer: {{$json.customerName}}</p>
        <p>Amount: ${{$json.amount}}</p>
      </body>
    </html>
  `,
  "css_content": `
    body { font-family: Arial, sans-serif; }
    h1 { color: #333; }
  `,
  "response_format": "base64"
}
```

### Website Screenshot
```javascript
{
  "operation": "urlToPdf",
  "url": "https://example.com",
  "full_page": true,
  "wait_till": 5000,
  "viewPortWidth": 1920,
  "viewPortHeight": 1080
}
```

## Output

The node returns:
- **URL format**: Direct link to the generated PDF
- **PNG format**: PNG image data
- **Base64 format**: Base64 encoded PDF data

## Error Handling

The node includes comprehensive error handling:
- Invalid HTML/CSS content
- Network connectivity issues
- API rate limiting
- Invalid URLs or parameters

## Compatibility

- **n8n version**: 0.187.0+
- **Node.js**: 18.0.0+
- **Supported formats**: HTML, CSS, PDF, PNG, Base64

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [PDFMunk API Documentation](https://pdfmunk.com/api-docs)
- [n8n workflow examples](https://n8n.io/workflows)

## Support

- Report issues on [GitHub](https://github.com/yourusername/n8n-nodes-htmlcsstopdf)
- Join the [n8n community](https://community.n8n.io/)
- Check [PDFMunk support](https://pdfmunk.com/support)

## Version History

- **1.0.0**: Initial release with HTML to PDF and URL to PDF operations

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests for any improvements.

## License

[MIT](LICENSE.md)

---

Built with ❤️ for the n8n community
=======
### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter `n8n-nodes-htmlcsstopdf`
4. Click **Install**

### Manual Installation

```bash
# Navigate to your n8n installation directory
cd ~/.n8n/nodes

# Install the package
npm install n8n-nodes-htmlcsstopdf
```

### Docker

Add the package to your n8n Docker container:

```dockerfile
FROM n8nio/n8n:latest
USER root
RUN npm install -g n8n-nodes-htmlcsstopdf
USER node
```

## Getting Your PdfMunk API Key

1. **Sign Up**: Visit [PdfMunk.com](https://pdfmunk.com) and create an account
2. **Verify Email**: Check your email and verify your account
3. **Access Dashboard**: Log in to your PdfMunk dashboard
4. **Generate API Key**: 
   - Navigate to the "API Keys" section
   - Click "Generate New API Key"
   - Copy your API key securely
5. **Choose Plan**: Select a plan based on your usage needs:
   - **Free Tier**: 100 conversions/month
   - **Starter**: 1,000 conversions/month
   - **Professional**: 10,000 conversions/month
   - **Enterprise**: Custom limits

## Configuration

### Setting Up Credentials

1. In n8n, go to **Credentials**
2. Click **+ Add Credential**
3. Search for "HtmlCssToPdf API"
4. Enter your PdfMunk API key
5. Test the connection
6. Save the credential

## Usage

### Basic HTML to PDF Conversion

```json
{
  "html": "<h1>Hello World</h1><p>This is a test document.</p>",
  "css": "h1 { color: blue; } p { font-size: 14px; }",
  "options": {
    "format": "A4",
    "orientation": "portrait"
  }
}
```

### Advanced Usage Examples

#### 1. Invoice Generation
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .invoice { font-family: Arial, sans-serif; }
        .header { background-color: #f0f0f0; padding: 20px; }
        .total { font-weight: bold; font-size: 18px; }
    </style>
</head>
<body>
    <div class="invoice">
        <div class="header">
            <h1>Invoice #12345</h1>
        </div>
        <div class="total">Total: $299.99</div>
    </div>
</body>
</html>
```

#### 2. Report Generation
```html
<div class="report">
    <h1>Monthly Report</h1>
    <table border="1">
        <tr><th>Metric</th><th>Value</th></tr>
        <tr><td>Sales</td><td>$50,000</td></tr>
        <tr><td>Growth</td><td>15%</td></tr>
    </table>
</div>
```

#### 3. Certificate Generation
```html
<div class="certificate">
    <h1>Certificate of Completion</h1>
    <p>This certifies that <strong>John Doe</strong> has completed the course.</p>
    <div class="signature">Authorized Signature</div>
</div>
```

## Use Cases

### Business Applications
- **Invoice Generation**: Automatically generate invoices from order data
- **Report Creation**: Convert analytics data into professional PDF reports
- **Contract Generation**: Create contracts from templates with dynamic data
- **Certificate Issuance**: Generate certificates for course completions
- **Receipt Creation**: Convert transaction data into PDF receipts

### Content Management
- **Document Archival**: Convert web pages to PDF for archival purposes
- **Newsletter PDFs**: Transform HTML newsletters into PDF format
- **eBook Creation**: Generate PDF books from HTML content
- **Documentation**: Convert online docs to downloadable PDFs

### Marketing & Sales
- **Proposal Generation**: Create branded proposals from CRM data
- **Brochure Creation**: Generate marketing materials dynamically
- **Price Lists**: Convert product catalogs to PDF format
- **Quotation PDFs**: Transform quotes into professional PDFs

## Node Options

| Option | Type | Description | Default |
|--------|------|-------------|---------|
| HTML Content | string | The HTML content to convert | Required |
| CSS Styles | string | Custom CSS for styling | Optional |
| Page Format | select | Paper size (A4, Letter, Legal, etc.) | A4 |
| Orientation | select | Portrait or Landscape | Portrait |
| Margins | object | Page margins in pixels | {top: 20, right: 20, bottom: 20, left: 20} |
| Header HTML | string | Header content for each page | Optional |
| Footer HTML | string | Footer content for each page | Optional |
| Scale | number | Zoom level (0.1 to 2.0) | 1 |

## Error Handling

The node provides detailed error messages for common issues:

- **Invalid API Key**: Check your PdfMunk credentials
- **HTML Parse Error**: Validate your HTML syntax
- **CSS Error**: Check your CSS for syntax errors
- **Rate Limit**: Upgrade your PdfMunk plan or wait for reset
- **Network Error**: Check your internet connection

## Workflow Examples

### Example 1: E-commerce Invoice
```json
{
  "nodes": [
    {
      "name": "Order Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Generate Invoice HTML",
      "type": "n8n-nodes-base.function"
    },
    {
      "name": "Convert to PDF",
      "type": "n8n-nodes-htmlcsstopdf.htmlcsstopdf"
    },
    {
      "name": "Email PDF",
      "type": "n8n-nodes-base.emailSend"
    }
  ]
}
```

### Example 2: Scheduled Reports
```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.cron"
    },
    {
      "name": "Fetch Analytics Data",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "name": "Build Report HTML",
      "type": "n8n-nodes-base.function"
    },
    {
      "name": "Generate PDF Report",
      "type": "n8n-nodes-htmlcsstopdf.htmlcsstopdf"
    },
    {
      "name": "Save to Google Drive",
      "type": "n8n-nodes-base.googleDrive"
    }
  ]
}
```

## FAQ

**Q: Is there a free tier?**
A: Yes, PdfMunk offers 100 free conversions per month.

**Q: What HTML features are supported?**
A: Most modern HTML5 and CSS3 features are supported, including flexbox, grid, and media queries.

**Q: Can I use external images?**
A: Yes, images accessible via URL will be included in the PDF.

**Q: What's the maximum file size?**
A: PDFs can be up to 10MB on most plans. Check PdfMunk documentation for current limits.

**Q: Can I customize headers and footers?**
A: Yes, you can add custom HTML headers and footers to each page.

## Support

- **Issues**: [GitHub Issues](https://github.com/PdfMunk/n8n-nodes-htmltopdf/issues)
- **Documentation**: [PdfMunk API Docs](https://docs.pdfmunk.com)
- **Community**: [n8n Community Forum](https://community.n8n.io)

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

## License

MIT License - see LICENSE file for details.

## Changelog

### v2.0.2
- Improved error handling
- Added support for custom headers/footers
- Performance optimizations

### v2.0.1
- Bug fixes and stability improvements

### v2.0.0
- Complete rewrite with new PdfMunk API
- Enhanced CSS support
- Better error messages
>>>>>>> dc0ef71 (Update Doc)
