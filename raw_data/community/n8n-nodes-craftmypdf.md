# n8n-nodes-craftmypdf

This is an n8n community node. It lets you use [CraftMyPdf](https://craftmypdf.com) in your n8n workflows.

[CraftMyPdf](https://craftmypdf.com) offers PDF generation API and image generation API. CraftMyPDF's advanced drag & drop editor lets you design PDF templates in any browser and generate pixel-perfect PDF documents from reusable templates and data with no-code platforms such as N8n, Zapier, Make, Bubble.io or REST API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

The sections:
- [Installation](#installation)  
- [Operations](#operations)  
- [Credentials](#credentials) <!-- delete if no auth needed -->  
- [Compatibility](#compatibility)  
- [Usage](#usage) <!-- delete if not using this section -->  
- [Resources](#resources)
- [License](#license)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The following are the options:

| Name           | Operation         | Description                                                                                                                    | Action                         | Documentation Link                                                                                                           |
|----------------|---------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Create         | `create`      | Creates a PDF file with JSON data and your template.                                                                          | Create a PDF                   | [Link](https://craftmypdf.com/docs/index.html#tag/PDF-Generation-API/operation/create)                                       |
| Create Async   | `createAsync` | Creates a PDF file asynchronously with JSON data and your template. The API returns immediately, and will retry for 3 times.  | Create a PDF asynchronously    | [Link](https://craftmypdf.com/docs/index.html#tag/PDF-Generation-API/operation/create-async)                                |
| Merge          | `merge`       | Merges multiple PDF URLs.                                                                                                     | Merge multiple PDF files       | [Link](https://craftmypdf.com/docs/index.html#tag/PDF-Manipulation-API/operation/merge-pdfs)                                |
| Add Watermark  | `addWatermark`| Adds a watermark to a PDF.                                                                                                    | Add watermark                  | [Link](https://craftmypdf.com/docs/index.html#tag/PDF-Manipulation-API/operation/add-watermark)                             |


## Credentials

You only need a CraftMyPdf API Key for this, you can get it in the API Integration tab in the web portal.

## Compatibility

This package was developed & tested with n8n > 1.4.0.

## Usage

Please check out the [CraftMyPdf API Reference](https://craftmypdf.com/docs/index.html) for more information on how to use the integration.

Please check out the [N8n integration tutorial](https://craftmypdf.com/blog/automate-pdf-generation-with-n8n-and-craftmypdf/) for more information.

## License
CraftMyPDF/n8n-nodes-craftmypdf is licensed under the [MIT License](LICENSE.md).

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [CraftMyPdf API Reference](https://craftmypdf.com/docs/index.html)
