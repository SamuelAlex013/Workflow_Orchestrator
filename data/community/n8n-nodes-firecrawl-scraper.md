# n8n-nodes-firecrawl-scraper

This package contains n8n nodes for working with the Firecrawl API, allowing you to scrape, crawl, and map websites directly within your n8n workflows. It serves as a wrapper around the [Firecrawl npm SDK](https://www.npmjs.com/package/@mendable/firecrawl-js), primarily focusing on the extract feature.

> **Note:** This project is still in development. Features and functionality may change.

## Support and Feedback

For support, feedback, or to contribute to this project:

- GitHub Repository: [n8n-nodes-firecrawl-scraper](https://github.com/leonardogrig/n8n-nodes-firecrawl-scraper)
- Tutorial Video: [Watch on YouTube](https://youtu.be/j19nN38cIXI)

## Prerequisites

- A Firecrawl API key (get one from [firecrawl.dev](https://firecrawl.dev))
- n8n instance (v1.0.0 or later)

## Installation

Follow these steps to install this custom node package in your n8n instance:

### In an existing n8n instance

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-firecrawl-scraper` in the **Name** field
4. Agree to the risks of using community nodes
5. Click **Install**

### Manually (Development)

1. Clone this repository
2. Navigate to the directory: `cd n8n-nodes-firecrawl-scraper`
3. Install dependencies: `npm install`
4. Build the code: `npm run build`
5. Link to your n8n installation: `npm link`
6. In your n8n installation directory, run: `npm link n8n-nodes-firecrawl-scraper`

## Nodes

This package includes a single Firecrawl node with multiple operations:

### Firecrawl

A unified node that provides various operations to interact with the Firecrawl API:

**Operations:**

- **Scrape**: Scrape content from a single URL in Markdown format
- **Crawl**: Crawl multiple pages of a website and retrieve content in Markdown format
- **Map**: Generate a list of URLs from a website
- **Extract**: Extract structured data from URLs using simple extraction or schema-based extraction

**Common Parameters:**

- **URL**: Required for all operations - specifies the target URL(s)
- **Enable Debug Logs**: Available for Scrape and Extract operations - enables detailed logging

**Operation-Specific Parameters:**

- **Crawl**:

  - Limit: Maximum number of pages to crawl (default: 50)

- **Extract**:
  - Extraction Method: Simple extraction or Schema-based extraction
  - Extraction Prompt: Guide the extraction process
  - Schema Definition Type (for schema-based extraction): Generate from JSON example or define manually
  - JSON Example or Schema Definition: Define the data structure

## Credentials

You'll need to set up your Firecrawl API key in the **Firecrawl API** credential type:

1. In your n8n workflow, add any Firecrawl node
2. Click the **Create new credential** button
3. Enter your Firecrawl API key
4. Save the credential

## Examples

### Basic Web Scraping

1. Add a **Firecrawl** node
2. Select the **Scrape** operation
3. Set the URL to the webpage you want to scrape
4. Connect to nodes like ChatGPT or Text processors to analyze the scraped content

### Website Crawling for Data Extraction

1. Add a **Firecrawl** node
2. Select the **Crawl** operation
3. Set the URL to the website you want to crawl
4. Set a limit (e.g., 10 pages)
5. Connect to database nodes to store the extracted data

### Website Mapping for SEO Analysis

1. Add a **Firecrawl** node
2. Select the **Map** operation
3. Set the URL to the website you want to map
4. Connect to spreadsheet or visualization nodes to analyze the site structure

### Structured Data Extraction

1. Add a **Firecrawl** node
2. Select the **Extract** operation
3. Set the URL(s) to extract data from
4. Choose the extraction method (Simple or Schema-based)
5. If using Schema-based extraction, define your schema or provide a JSON example
6. Use the extracted structured data in your workflow

## License

[MIT](LICENSE.md)
