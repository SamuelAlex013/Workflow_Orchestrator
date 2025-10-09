# n8n-nodes-trends

An n8n community node for accessing Google Trends data using the [@alkalisummer/google-trends-js](https://www.npmjs.com/package/@alkalisummer/google-trends-js) library.

## Features

This node provides access to all Google Trends API endpoints:

- **Daily Trends** - Get daily trending topics for a specific region
- **Real-Time Trends** - Get real-time trending topics
- **Trending Articles** - Get articles related to trending topics
- **Interest Over Time** - Get interest over time data for keywords
- **Autocomplete** - Get search suggestions for keywords
- **Explore** - Get widget data for keywords
- **Interest by Region** - Get interest data by geographic region

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Enter `n8n-nodes-trends` in the npm package name field
3. Click **Install**

### Manual Installation

1. Navigate to your n8n installation's root directory
2. Run: `npm install n8n-nodes-trends`
3. Restart n8n

## Usage

Once installed, you'll find the **Google Trends** node in the **Transform** category of your node palette.

### Operations

#### Daily Trends
Get daily trending topics for a specific geographic region.

**Parameters:**
- **Geo Location** (default: "US"): Geographic location code (e.g., US, GB, DE)
- **Language** (default: "en"): Language code (e.g., en, fr, de)

#### Real-Time Trends
Get currently trending topics in real-time.

**Parameters:**
- **Geo Location** (default: "US"): Geographic location code
- **Trending Hours** (default: 4): Number of hours to look back for trending topics

#### Trending Articles
Get articles related to specific trending topics.

**Parameters:**
- **Article Keys**: JSON array of article keys (obtained from Daily Trends)
- **Article Count** (default: 5): Number of articles to retrieve

#### Interest Over Time
Get interest over time data for a specific keyword.

**Parameters:**
- **Keyword**: Search keyword (required)
- **Geo Location** (default: "US"): Geographic location code

#### Autocomplete
Get search suggestions for a keyword.

**Parameters:**
- **Keyword**: Keyword to get suggestions for (required)
- **Language** (default: "en-US"): Language code

#### Explore
Get widget data for trend exploration.

**Parameters:**
- **Keyword**: Search keyword (required)
- **Geo Location** (default: "US"): Geographic location code
- **Time Range** (default: "now 1-d"): Time range for analysis
- **Category** (default: 0): Category number
- **Property**: Property filter
- **Language** (default: "en-US"): Language code

#### Interest by Region
Get interest data by geographic region.

**Parameters:**
- **Keywords**: Comma-separated list of keywords (required)
- **Start Date**: Start date for analysis
- **End Date**: End date for analysis  
- **Geo Locations** (default: "US"): Comma-separated list of geo codes
- **Resolution** (default: "REGION"): Geographic resolution (COUNTRY, REGION, CITY, DMA)
- **Language** (default: "en-US"): Language code
- **Timezone** (default: -240): Timezone offset in minutes
- **Category** (default: 0): Category number

## Example Workflows

### Basic Daily Trends
1. Add a **Manual Trigger** node
2. Add the **Google Trends** node
3. Set **Operation** to "Daily Trends"
4. Configure **Geo Location** (e.g., "US", "GB", "DE")
5. Execute to get trending topics

### Keyword Analysis Over Time
1. Add a **Manual Trigger** node
2. Add the **Google Trends** node
3. Set **Operation** to "Interest Over Time"
4. Enter your **Keyword** (e.g., "bitcoin", "climate change")
5. Execute to get historical interest data

### Multi-region Comparison
1. Add a **Manual Trigger** node
2. Add the **Google Trends** node
3. Set **Operation** to "Interest by Region"
4. Enter **Keywords**: "electric cars"
5. Set **Geo Locations**: "US,GB,DE,FR"
6. Execute to compare regional interest

## Output Format

All operations return data in the following format:

```json
{
  "operation": "operationName",
  "data": {
    // API response data specific to the operation
  }
}
```

In case of errors (when "Continue on Fail" is enabled):

```json
{
  "operation": "operationName", 
  "error": "Error message"
}
```

## Development

### Building the Node

```bash
npm install
npm run build
```

### Running Tests

```bash
npm test
npm run test:watch  # for watch mode
```

### Linting

```bash
npm run lint
npm run lintfix  # to auto-fix issues
```

## Dependencies

- **n8n-workflow**: Core n8n workflow functionality
- **@alkalisummer/google-trends-js**: Google Trends API wrapper

## License

MIT

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run tests and linting
6. Submit a pull request

## Support

If you encounter issues or have questions:

1. Check the [Issues](https://github.com/DirectorVector/n8n-nodes-trends/issues) page
2. Create a new issue with details about your problem
3. Include n8n version, node version, and error messages

## Changelog

### 1.0.0
- Initial release
- Support for all Google Trends API endpoints
- Comprehensive parameter configuration
- Error handling and validation
- TypeScript support
- Jest test suite
