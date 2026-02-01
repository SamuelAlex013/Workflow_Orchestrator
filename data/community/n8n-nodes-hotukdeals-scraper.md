# HotUKDeals Scraper Node for n8n

A custom n8n node that scrapes deal information from the HotUKDeals website, allowing you to automate deal monitoring and integrate deal data into your workflows.

## Features

- **Deal Scraping**: Extracts deals from HotUKDeals website pages
- **Comprehensive Data**: Retrieves title, description, price, image URL, and deal link
- **Pagination Support**: Scrape multiple pages with configurable start and end pages
- **Rate Limiting**: Built-in delay between requests to respect the website
- **Error Handling**: Graceful handling of network errors and parsing issues
- **Declarative Style**: Built using n8n's modern declarative node architecture

## Installation

### From npm (when published)
```bash
npm install n8n-nodes-hotukdeals-scraper
```

### Local Development
1. Clone this repository
2. Run `npm install` to install dependencies
3. Run `npm run build` to compile the node
4. Link the node locally:
   ```bash
   npm link
   cd ~/.n8n/nodes
   npm link n8n-nodes-hotukdeals-scraper
   ```
5. Restart your n8n instance

## Configuration

The node accepts the following parameters:

### Required Parameters

- **Start Page**: The first page to scrape (0-based indexing)
- **End Page**: The last page to scrape (inclusive)
- **Delay Between Requests**: Delay in milliseconds between page requests (recommended: 1000ms or higher)

### Operation

- **Scrape Deals**: The main operation that fetches and processes deal data

## Output Data Structure

Each deal item in the output contains:

```json
{
  "title": "Deal Title",
  "link": "https://www.hotukdeals.com/deals/...",
  "description": "Deal description text",
  "price": "£29.99",
  "imageUrl": "https://images.hotukdeals.com/..."
}
```

## Example Usage

### Basic Deal Scraping
1. Add the HotUKDeals Scraper node to your workflow
2. Set Start Page to `0` and End Page to `2` to scrape the first 3 pages
3. Set Delay to `1000` milliseconds
4. Execute the workflow

### Advanced Workflow Ideas

- **Deal Monitoring**: Use with a Schedule Trigger to check for new deals periodically
- **Price Alerts**: Filter deals by price and send notifications via email/Slack
- **Deal Database**: Store scraped deals in Airtable, Google Sheets, or a database
- **Social Media**: Post hot deals to Twitter or Discord channels
- **Email Newsletters**: Compile daily/weekly deal roundups

## Technical Details

### Architecture
- Built using n8n's declarative node style
- Uses Cheerio for HTML parsing
- Handles Vue.js embedded data extraction for enhanced deal information
- Implements proper error handling and rate limiting

### Data Sources
The node extracts data from:
- HTML content for basic deal information (title, description, links)
- Vue.js component data for pricing and image information
- HotUKDeals AJAX API endpoints for paginated content

### Rate Limiting
The node includes configurable delays between requests to:
- Respect HotUKDeals server resources
- Avoid potential rate limiting or blocking
- Ensure reliable data extraction

## Best Practices

1. **Respectful Scraping**: Always use appropriate delays (1000ms+) between requests
2. **Error Handling**: Enable "Continue on Fail" in production workflows
3. **Data Validation**: Check for empty results and handle gracefully
4. **Monitoring**: Set up alerts for workflow failures
5. **Compliance**: Ensure your use case complies with HotUKDeals terms of service

## Troubleshooting

### Common Issues

**No deals returned**: 
- Check if the website structure has changed
- Verify network connectivity
- Increase delay between requests

**Rate limiting errors**:
- Increase the delay between requests
- Reduce the number of pages scraped per execution

**Build errors**:
- Ensure Node.js version 20+ is installed
- Run `npm install` to update dependencies
- Check TypeScript compilation with `npm run build`

## Development

### Prerequisites
- Node.js 20+
- npm
- n8n installed globally

### Building
```bash
npm run build
```

### Linting
```bash
npm run lint
npm run lintfix  # Auto-fix issues
```

### Testing Locally
1. Build the node: `npm run build`
2. Link the package: `npm link`
3. Install in n8n: `cd ~/.n8n/nodes && npm link n8n-nodes-hotukdeals-scraper`
4. Restart n8n and test the node

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## Legal Notice

This node is for educational and personal use only. Users are responsible for:
- Complying with HotUKDeals terms of service
- Respecting website resources through appropriate rate limiting
- Ensuring their use case is legally compliant

The developers are not responsible for any misuse of this tool.

## License

MIT License - see [LICENSE.md](LICENSE.md) for details.

## Support

For issues and questions:
- Create an issue in this repository
- Check the [n8n community forum](https://community.n8n.io/)
- Review the [n8n documentation](https://docs.n8n.io/)

## Changelog

### v1.1.1
- Converted to declarative node architecture
- Added proper TypeScript support
- Implemented Vue.js data extraction
- Added comprehensive error handling
- Fixed linting issues

---

**Note**: This is an unofficial tool and is not affiliated with HotUKDeals. Use responsibly and in accordance with the website's terms of service.
