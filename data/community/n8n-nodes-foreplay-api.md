# n8n-nodes-foreplay-api

This is an n8n community node that lets you interact with the Foreplay API in your n8n workflows.

[Foreplay](https://foreplay.co/) is a creative intelligence platform that helps marketing teams discover, analyze, and organize winning ad creative from top brands across Facebook, Instagram, TikTok, and other platforms. With Foreplay, you can build comprehensive creative databases, track competitor strategies, and accelerate your creative development process.

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

This node supports the following operations:

### Library & Swipefile
- **Get Library Ads** - Retrieve ads from your personal swipefile collection

### Boards Management
- **Get All Boards** - Retrieve all boards associated with your account
- **Get All Brands by Board ID** - Retrieve all brands associated with a specific board
- **Get Ads by Board ID** - Retrieve ads from a specific board with filtering options

### Spyder (Brand Tracking)
- **Get Tracked Brands** - Retrieve all brands you have access to in Spyder
- **Get Spyder Brand** - Get detailed information for a specific tracked brand
- **Get Ads by Spyder Brand ID** - Retrieve all ads for a specific brand in Spyder

### Ad Discovery & Search
- **Search for Ads** - Search and filter ads by various criteria including:
  - Keywords and text content
  - Ad formats and placements
  - Date ranges and performance metrics
  - Brand and industry filters
- **Get Ad Details** - Retrieve detailed information for a specific ad by ID

### Brand Discovery
- **Search for Brands by Name** - Search and filter brands by name
- **Get Brands by Domain** - Retrieve brands associated with a specific domain
- **Get Ads by Brand ID** - Retrieve all ads for specific brand IDs with comprehensive filtering
- **Get Ads by Page ID** - Retrieve ads associated with a specific page ID

## Credentials

To use this node, you need to authenticate with the Foreplay API:

### Prerequisites
1. Sign up for a [Foreplay account](https://foreplay.co/)

### Getting Your API Key
1. Log into your Foreplay account
2. Navigate to your [API settings](https://app.foreplay.co/api-overview)
3. Unlock the API for free, and copy your API key
4. For detailed instructions, refer to the [API onboarding documentation](https://help.foreplay.co/articles/0374062-getting-started-with-the-foreplay-api)

### Authentication Setup
1. In n8n, create new credentials of type "Foreplay API"
2. Enter your API key in the "API Key" field
3. The base URL is pre-configured to `https://public.api.foreplay.co/api`


## Compatibility

- **Minimum n8n version:** 1.0.0
- **Tested with n8n versions:** 1.0.0+
- **Node.js version:** 20.15+

## Usage

### Basic Examples

**Search for Ads by Keyword:**
1. Select "Search for Ads" operation
2. Configure search parameters (keywords, date range, etc.)
3. The node returns matching ads with metadata

**Get Your Library Ads:**
1. Select "Get Library Ads" operation
2. The node returns all ads from your personal swipefile

**Track Competitor Ads:**
1. Use "Get Tracked Brands" to see available brands
2. Use "Get Ads by Spyder Brand ID" to retrieve competitor ads
3. Filter by date ranges, ad formats, or performance metrics

### Common Use Cases
- **Competitive Intelligence:** Automate collection of competitor ad data
- **Creative Research:** Build automated creative research workflows
- **Performance Monitoring:** Track ad performance across different brands
- **Content Curation:** Automatically organize and categorize creative assets
- **Reporting:** Generate automated reports on creative trends and performance

### Tips
- Use filtering parameters to narrow down results and improve performance
- Combine multiple operations to create comprehensive creative intelligence workflows
- Set up scheduled workflows to automatically track competitor activities
- Use the search operations with specific criteria to find exactly what you need

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Foreplay API Documentation](https://docs.foreplay.co/)
* [Foreplay Platform](https://foreplay.co/)
* [Foreplay Help Center](https://help.foreplay.co/)
