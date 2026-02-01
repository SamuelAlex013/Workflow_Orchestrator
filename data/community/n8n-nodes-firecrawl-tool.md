# n8n-nodes-firecrawl-tool

[![npm version](https://badge.fury.io/js/n8n-nodes-firecrawl-tool.svg)](https://badge.fury.io/js/n8n-nodes-firecrawl-tool)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An n8n community node for [Firecrawl](https://firecrawl.dev) v2 API - a powerful web scraping, crawling, and data extraction tool. This node works both as a standard workflow node and as an AI tool for use with n8n's AI Agent and MCP Trigger nodes.

## Features

- 🔍 **Scrape**: Extract content from single webpages in multiple formats (markdown, HTML, summary, screenshots)
- 🕷️ **Crawl**: Recursively scrape entire websites with intelligent navigation
- 🗺️ **Map**: Quickly discover all URLs on a website
- 🔎 **Search**: Search the web and optionally scrape results
- 🤖 **Extract**: Use AI to extract structured data from webpages
- 🤝 **AI Tool Compatible**: Full support for use as an AI agent tool with comprehensive descriptions
- ⚡ **Caching**: Built-in caching support for improved performance
- 🎯 **Actions**: Perform clicks, scrolls, and other interactions before scraping

## Installation

### Community Nodes (Recommended)

1. In n8n, go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-firecrawl-tool`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-firecrawl-tool
```

Then restart your n8n instance.

### Local Development

```bash
# Clone the repository
git clone https://github.com/jezweb/n8n-nodes-firecrawl-tool.git
cd n8n-nodes-firecrawl-tool

# Install dependencies
npm install

# Build the node
npm run build

# Link to n8n
npm link
cd ~/.n8n/custom
npm link n8n-nodes-firecrawl-tool

# Restart n8n
```

## Setup

### Getting a Firecrawl API Key

1. Visit [firecrawl.dev](https://firecrawl.dev)
2. Sign up for an account
3. Navigate to your dashboard to get your API key

### Configuring Credentials in n8n

1. In n8n, go to **Credentials** > **New**
2. Search for "Firecrawl API"
3. Enter your API key
4. (Optional) Change the API host if using a self-hosted instance
5. Save the credentials

## Usage

### As a Regular Workflow Node

1. Add the "Firecrawl Tool" node to your workflow
2. Select your Firecrawl API credentials
3. Choose an operation (Scrape, Crawl, Map, Search, or Extract)
4. Configure the operation parameters
5. Execute the workflow

### As an AI Tool

1. Add an "AI Agent" or "MCP Trigger" node to your workflow
2. Add the "Firecrawl Tool" node
3. Connect the Firecrawl Tool to the AI Agent's tool input
4. The AI will automatically use the tool based on the descriptions provided

## Operations

### Scrape

Extract content from a single webpage.

**Parameters:**
- `URL`: The webpage to scrape
- `Formats`: Output formats (markdown, HTML, summary, screenshot, links)
- `Options`: Cache duration, wait time, content filtering, actions, and more

**Example Use Cases:**
- Extract article content for analysis
- Capture screenshots for monitoring
- Get structured data from product pages

### Crawl

Recursively scrape an entire website or subdomain.

**Parameters:**
- `URL`: Starting point for the crawl
- `Limit`: Maximum pages to crawl
- `Max Depth`: How deep to crawl from the starting URL
- `Smart Crawl Prompt`: Natural language guidance for the crawler
- `Wait for Completion`: Whether to wait for results or get a job ID

**Example Use Cases:**
- Index an entire documentation site
- Extract all blog posts from a website
- Create a knowledge base from a company website

### Map

Quickly discover all URLs on a website.

**Parameters:**
- `URL`: The website to map
- `Limit`: Maximum URLs to return
- `Search`: Filter URLs by term
- `Include Subdomains`: Whether to include subdomain URLs

**Example Use Cases:**
- Site structure analysis
- Finding specific page types
- SEO audits

### Search

Search the web and optionally scrape the results.

**Parameters:**
- `Query`: Search terms
- `Sources`: Web, news, and/or images
- `Scrape Results`: Whether to extract content from results
- `Location`: Geographic location for results

**Example Use Cases:**
- Market research
- Competitive analysis
- Content aggregation

### Extract

Extract structured data from webpages using AI.

**Parameters:**
- `URLs`: Pages to extract from
- `Extraction Prompt`: Natural language description of what to extract
- `Schema`: Optional JSON schema for structured output

**Example Use Cases:**
- Product data extraction
- Contact information gathering
- Automated form filling

## AI Tool Usage

This node is designed to work seamlessly with AI agents. Each operation and parameter includes detailed descriptions that help AI models understand when and how to use the tool.

**Example AI Prompts:**
- "Get the content from docs.firecrawl.dev"
- "Find all URLs on example.com"
- "Search for recent news about n8n automation"
- "Extract product prices from these e-commerce pages"

## Advanced Features

### Caching

All scrape operations support caching with the `maxAge` parameter. Cached results are returned instantly if they're younger than the specified age, reducing API calls and improving performance.

### Actions

Perform interactions before scraping:
```json
[
  {"type": "wait", "milliseconds": 1000},
  {"type": "click", "selector": "button.load-more"},
  {"type": "scroll", "direction": "down"},
  {"type": "screenshot", "fullPage": true}
]
```

### Smart Crawling

Use natural language prompts to guide crawling:
- "Only crawl blog posts from 2024"
- "Focus on product pages under /shop"
- "Avoid PDF files and image galleries"

## Rate Limits

Please refer to [Firecrawl's rate limit documentation](https://docs.firecrawl.dev/rate-limits) for current limits based on your plan.

## Troubleshooting

### Common Issues

1. **API Key Invalid**: Ensure your API key is correctly entered in the credentials
2. **Rate Limit Exceeded**: Upgrade your Firecrawl plan or add delays between requests
3. **Timeout Errors**: Increase the wait time for dynamic content or use actions
4. **Empty Results**: Check if the site requires authentication or has anti-bot measures

### Debug Mode

Enable n8n's execution details to see the full API requests and responses for debugging.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-firecrawl-tool/issues)
- **Discussions**: [n8n Community Forum](https://community.n8n.io)
- **Firecrawl Docs**: [docs.firecrawl.dev](https://docs.firecrawl.dev)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## Author

Jeremy Dawes - [Jezweb](https://www.jezweb.com.au)

## Acknowledgments

- [Firecrawl](https://firecrawl.dev) for the excellent API
- [n8n](https://n8n.io) for the workflow automation platform
- The n8n community for inspiration and support