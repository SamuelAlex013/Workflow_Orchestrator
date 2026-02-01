# n8n-nodes-amazon-paapi

This is an n8n community node for Amazon's Product Advertising API (PA API 5.0). It provides functionality to search for products and retrieve detailed product information from Amazon's marketplace.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install @henkey/n8n-nodes-amazon-paapi
```

## Operations

### Amazon Product Search

This node provides two main operations:

1. **Search Products**
   - Search for products using keywords
   - Get product details including prices, titles, and URLs
   - Filter results based on various criteria

2. **Get Product Details**
   - Retrieve detailed information about specific products using their ASIN
   - Access comprehensive product data including descriptions and features

### Available Fields

Both operations support retrieving the following information:
- Title
- Features
- Price
- Images
- Rating
- Review Count
- Brand
- Product Description

## Credentials

To use this node, you need Amazon PA API credentials:

1. Access Key
2. Secret Key
3. Partner Tag (Amazon Associates tracking ID)
4. Marketplace selection

You can obtain these credentials by:
1. Joining the [Amazon Associates Program](https://affiliate-program.amazon.com/)
2. Registering for [Product Advertising API](https://webservices.amazon.com/paapi5/documentation/)

## Compatibility

- Requires n8n version 1.0.0 or later
- Supports all Amazon marketplaces
- Compatible with both workflow and agent usage

## Usage

1. **As a Workflow Node**
   - Add the "Amazon Product Search" node to your workflow
   - Configure the credentials
   - Select the operation (Search Products or Get Product Details)
   - Configure the operation parameters
   - Connect to other nodes as needed

2. **As an Agent Tool**
   - The node is automatically available as a tool for AI agents
   - Agents can use it to search for products or get product details
   - Results are formatted for easy consumption by other nodes

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Amazon PA API documentation](https://webservices.amazon.com/paapi5/documentation/)

## License

[MIT](LICENSE.md)
