# n8n-nodes-templated

This is an n8n community node. It lets you use Templated in your n8n workflows.

Templated is a powerful image and PDF generation service that allows you to create dynamic visual content from templates. With it's drag-and-drop editor and robust API, you can automate the creation of marketing images, social media posts, banners, PDFs, and more.

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

With Templated you can create images or PDFs from dynamic templates. Here are the operations you can use:

| Name | Operation | Description | Documentation Link |
|------|-----------|-------------|-------------------|
| Create Render | render:create | Creates an image or PDF file with JSON data and your template. Supports JPEG, PNG, WebP, and PDF formats with customizable layers. | [Link](https://templated.io/docs/renders/create/) |
| Retrieve Render | render:retrieve | Retrieves a specific render by its ID to check status and get the generated file URL. | [Link](https://templated.io/docs/renders/retrieve/) |
| Merge Renders | render:merge | Merges multiple rendered PDFs into a single PDF document. Useful for combining multiple pages or documents. | [Link](https://templated.io/docs/renders/merge/) |
| Retrieve Template | template:retrieve | Retrieves details of a specific template by its ID including metadata and layer information. | [Link](https://templated.io/docs/templates/retrieve/) |
| List All Templates | template:list | Lists all templates in your account with pagination and filtering options. | [Link](https://templated.io/docs/templates/list/) |
| List Template Layers | template:layers | Lists all available layers of a specific template for customization and dynamic content mapping. | [Link](https://templated.io/docs/templates/layers/) |
| List Template Renders | template:renders | Lists all renders created from a specific template with pagination support. | [Link](https://templated.io/docs/templates/renders/) |


## Credentials

To use this node, you need to authenticate with Templated using an API key.

### Prerequisites
1. Sign up for a [Templated account](https://templated.io)
2. Create a template using the Templated Editor
3. Get your API key from your account dashboard

### Authentication Setup
1. In n8n, create new credentials for "Templated API"
2. Enter your API key obtained from Templated
3. Test the connection to ensure it's working properly

## Compatibility

- **Minimum n8n version**: 0.174.0
- **Current version**: 0.2.2
- **Node API version**: 1
- **Tested with n8n versions**: 0.174.0, 1.0.0+
- **Node.js requirement**: >=18.10
- **Package manager**: pnpm >=9.1

This node uses the Templated API and should remain compatible with future versions of the service. The node includes AI tool integration capabilities for enhanced workflow automation.

## Usage

This node is perfect for automating visual content creation in your workflows. Common use cases include:

- **Marketing Automation**: Generate personalized social media posts, banners, or ads with dynamic content
- **E-commerce**: Create product images with dynamic pricing, promotional text, or seasonal branding
- **Document Generation**: Generate certificates, invoices, reports, or contracts in PDF format
- **SaaS Applications**: Create user-specific images, dashboards, or documents
- **Social Media**: Automate the creation of branded posts with dynamic content and user data
- **Batch Processing**: Merge multiple PDFs or generate series of related documents

### Advanced Features

- **Dynamic Layer Customization**: Control text content, colors, fonts, images, borders, and visibility
- **Template Search**: Quickly find templates by name or description using the built-in search
- **Resource Locators**: Choose templates from dropdown lists or enter IDs directly
- **Conditional Logic**: Hide/show layers dynamically based on your workflow data
- **Error Handling**: Graceful handling of missing templates or invalid parameters

### Example Workflow
1. **Trigger**: New data event (e.g., new customer, product, or order)
2. **Process**: Transform and prepare data for template variables  
3. **Generate**: Use the Templated node to create personalized image or PDF
4. **Distribute**: Share via email, social media, file storage, or webhook

The node integrates seamlessly with other n8n nodes, allowing you to pull data from databases, APIs, webhooks, or forms to populate your templates dynamically.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Templated API documentation](https://templated.io/docs)
* [Template Gallery](https://templated.io/templates)
