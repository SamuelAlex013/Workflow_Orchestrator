# n8n-nodes-url-to-html

This is an n8n community node. It lets you use **PDFMunk** in your n8n workflows.

PDFMunk is a powerful API service that converts URLs to clean HTML content or even converts URL to PDF or HTML to PDF, perfect for web scraping, content extraction, and data processing workflows.

**n8n** is a **fair-code licensed** workflow automation platform.

## Installation

Follow the **installation guide** in the n8n community nodes documentation.

1. **Go to Settings > Community Nodes.**
2. **Select Install.**
3. **Enter** `n8n-nodes-url-to-html` **in Enter npm package name**.
4. **Agree to the risks of using community nodes: select I understand the risks of installing unverified code from a public source.**
5. **Select Install.**

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

It supports these operations:

* Convert any URL to clean HTML content
* Extract web page content for data processing
* Scrape website content for analysis
* Generate HTML from dynamic web pages
* Process multiple URLs in batch workflows

## Credentials

Create a PDFMunk account **here**: http://pdfmunk.com to get your API key.

* Generate your API key at: http://pdfmunk.com
* Configure the PDFMunk API credential in n8n with your API key

## Compatibility

Tested against n8n version 0.225+.

## Usage

A typical workflow using this node would look like this:

```
Webhook → URL to HTML → HTML Extract → Database
```

**Example workflow for content extraction:**
1. **HTTP Request** - Get list of URLs to process
2. **URL to HTML** - Convert each URL to HTML content  
3. **HTML Extract** - Parse specific data from HTML
4. **Set** - Format the extracted data
5. **Database** - Store the processed content

**Input Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **URL** | String | Yes | The URL to convert to HTML |
| **Credentials** | PDFMunk API | Yes | Your PDFMunk API credentials |

**Output:**

The node returns clean HTML content that can be processed by other n8n nodes for data extraction, content analysis, or storage.

## Troubleshooting

**Common Issues:**

* **Authentication Error** - Verify your API key is correct and your PDFMunk account is active
* **URL Not Accessible** - Ensure the URL is publicly accessible and properly formatted
* **Rate Limiting** - Check your PDFMunk plan limits for high-volume workflows

## Resources

* **n8n community nodes documentation**
* **PDFMunk API Documentation**: https://pdfmunk.com/api-docs
* **PDFMunk Website**: http://pdfmunk.com
* **PDFMunk Support**: support@pdfmunk.com

## Version History

### v1.0.0
- Initial release
- Basic URL to HTML conversion functionality
- PDFMunk API integration

---

**Keywords**
* **n8n-community-node-package**
* **web-scraping**
* **html-conversion**
* **url-processing**