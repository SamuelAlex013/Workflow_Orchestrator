# n8n-nodes-smart-web-scraper

Smart Web Scraper node for [n8n](https://n8n.io/) with automatic failover and intelligent content extraction. This node attempts multiple scraping methods to ensure you get the content you need, even when sites block traditional HTTP requests.

## Features

- **🚀 Automatic Failover**: Tries multiple scraping methods until one succeeds
- **📄 Smart Content Extraction**: Automatically extracts main article content, removing ads, navigation, and other clutter
- **🎯 Multiple Strategies**: Choose between cost-effective, speed-first, or quality-first approaches
- **🔄 Multiple Backends**: Supports HTTP GET, Jina AI Reader, and Firecrawl API
- **🌐 Proxy Support**: Route requests through proxy servers when needed
- **📝 Multiple Output Formats**: Markdown, plain text, HTML, or structured JSON
- **🤖 AI-Ready**: Enabled as a tool for AI agents with `usableAsTool` flag

## Installation

### Community Nodes (Recommended)

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-smart-web-scraper`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-smart-web-scraper
```

## Scraping Methods

### 1. HTTP GET with Content Extraction (Free)
- Standard HTTP request with intelligent content extraction
- Uses Mozilla's Readability algorithm to extract main content
- Removes ads, navigation, sidebars automatically
- Converts to clean markdown format

### 2. Jina AI Reader (Free Tier Available)
- Specialized reader API that returns clean markdown
- No API key required for basic usage
- Handles JavaScript-rendered content better than HTTP GET

### 3. Firecrawl API (Premium)
- Professional web scraping API
- Best extraction quality
- Handles complex sites and anti-scraping measures

## Configuration

### Scraping Strategies

- **Cost Effective**: Tries free methods first (HTTP → Jina → Firecrawl)
- **Speed First**: Uses fastest available method
- **Quality First**: Starts with premium APIs for best extraction

### Credentials Setup

#### Firecrawl API (Optional)
1. Sign up at [Firecrawl.dev](https://firecrawl.dev)
2. Get your API key
3. Add to n8n credentials

#### Jina AI API (Optional)
1. Visit [Jina AI Reader](https://jina.ai/reader/)
2. API key is optional for basic usage
3. Add to n8n credentials for higher limits

#### Proxy Server (Optional)
1. Configure your proxy details
2. Supports HTTP, HTTPS, and SOCKS5 protocols
3. Optional authentication support

## Usage Examples

### Basic Web Scraping
```json
{
  "url": "https://example.com/article",
  "strategy": "cost_effective",
  "outputOptions": {
    "format": "markdown",
    "extractMainContent": true
  }
}
```

### With Failover Options
```json
{
  "url": "https://example.com/article",
  "strategy": "cost_effective",
  "failoverOptions": {
    "enableJina": true,
    "enableFirecrawl": true,
    "enableProxy": false
  },
  "outputOptions": {
    "format": "markdown",
    "maxLength": 5000,
    "includeMetadata": true
  }
}
```

### For AI Processing
```json
{
  "url": "https://example.com/article",
  "strategy": "quality_first",
  "outputOptions": {
    "format": "markdown",
    "extractMainContent": true,
    "maxLength": 3000
  }
}
```

## Output Structure

The node returns:
- `content`: The extracted content in your chosen format
- `metadata`: Title, author, excerpt, site name (when available)
- `scrapingMethod`: Which method successfully retrieved the content
- `url`: The scraped URL
- `timestamp`: When the scraping occurred

## Use with AI Agents

This node is AI-tool enabled with `usableAsTool: true`. You can:
1. Connect it to an AI Agent node
2. The AI will automatically use it to fetch web content
3. Clean, extracted content is perfect for AI context windows

## Error Handling

The node includes comprehensive error handling:
- Automatic retry with exponential backoff
- Detailed error messages for each failed method
- Option to continue workflow on errors
- Clear indication of which method succeeded

## Tips

1. **Start with Cost Effective strategy** - It's free and works for most sites
2. **Enable Jina for JavaScript sites** - Better than plain HTTP for SPAs
3. **Use Firecrawl for critical content** - When you absolutely need the data
4. **Set max length for AI use** - Prevent token limit issues
5. **Extract main content by default** - Cleaner data for processing

## Development

```bash
# Install dependencies
pnpm install

# Build the node
pnpm run build

# Test in development
pnpm run dev

# Lint code
pnpm run lint
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

## Support

For issues and feature requests, please use the [GitHub Issues](https://github.com/jezweb/n8n-nodes-smart-web-scraper/issues) page.

## Changelog

### v0.1.0
- Initial release
- HTTP GET with Readability extraction
- Jina AI Reader integration
- Firecrawl API support
- Proxy server support
- Multiple output formats
- AI tool compatibility