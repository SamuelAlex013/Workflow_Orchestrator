# ScrapingDog Node for n8n

This is a custom n8n node that integrates with the ScrapingDog API, providing web scraping and search capabilities. The node has been converted to use n8n's declarative style for better maintainability and reliability.

## Key Highlights

- ✅ **6 Different APIs**: URL Scraping, Google Search, Google Images, Google News, Bing Search, and Amazon Search
- ✅ **Declarative Style**: Modern n8n node implementation for better performance
- ✅ **Comprehensive Filtering**: Advanced search options for all supported APIs
- ✅ **Multi-language Support**: Support for multiple languages and regions
- ✅ **Rate Limit Handling**: Built-in error handling for API limitations
- ✅ **TypeScript**: Fully typed for better development experience

## Features

- 🌐 **URL Scraping**: Extract content from any webpage
- 🔍 **Google Search**: Perform Google searches with advanced options
- 🖼️ **Google Images**: Search Google Images with advanced filtering options
- 📰 **Google News**: Search Google News with time-based and geographic filtering
- 🔎 **Bing Search**: Search Bing with customizable filters
- 🛍️ **Amazon Search**: Search products on Amazon

## Directory Structure

```
nodes/ScrapingDog/
├── ScrapingDog.node.ts      # Main node implementation (Declarative Style)
├── ScrapingDog.node.json    # Node metadata
├── scrappingDog.svg         # Node icon
├── types/
│   └── index.ts             # TypeScript interfaces and types
├── resources/
│   ├── index.ts             # Resource exports
│   ├── scrapeUrl.ts         # Scrape URL resource
│   ├── googleSearch.ts      # Google Search resource
│   ├── googleImages.ts      # Google Images resource
│   ├── googleNews.ts        # Google News resource
│   ├── bingSearch.ts        # Bing Search resource
│   ├── amazonSearch.ts      # Amazon Search resource
│   └── staticResource.ts    # Static data (countries, etc.)
```

## Recent Updates

### Version 0.4.2 - LinkedIn API Removal & Documentation Updates
- 🗑️ **REMOVED: LinkedIn Profile and Jobs APIs** - Removed LinkedIn Profile and LinkedIn Jobs functionality
- **Simplified Interface**: Streamlined resource options for better focus on core web scraping features
- **Reduced Dependencies**: Cleaner codebase with fewer external integrations
- **Enhanced Documentation**: Added comprehensive parameter documentation for all remaining APIs
- **Updated Examples**: Improved usage examples and API response documentation

### Version 0.4.1 - Google News API Integration
- 📰 **NEW: Google News Search** - Added comprehensive Google News API support
- **Time-Based Filtering**: Filter news by hour, day, week, month, or year
- **Geographic Targeting**: Country-specific news results with custom domain support
- **Language Support**: 18 different languages for news results
- **Advanced Filtering**: Geographic location (UULE), language restrictions, safe search
- **Auto-Correct Control**: Option to exclude auto-corrected query results

### Version 0.4.0 - Google Images API Integration
- 🖼️ **NEW: Google Images Search** - Added comprehensive Google Images API support
- **Advanced Image Filtering**: Size, type, color, usage rights, time period filters
- **Multi-language Support**: 13 different languages for search results
- **Safe Search Controls**: Strict, moderate, or off filtering options
- **Geographic Targeting**: Country-specific image search results

### Previous Updates
1. **Converted to Declarative Style**
   - Removed manual HTTP request handling
   - Added routing configuration for each resource
   - Improved error handling
   - Better parameter validation

2. **Resource Improvements**
   - Added proper parameter descriptions
   - Fixed boolean parameter descriptions to start with "Whether"
   - Sorted option lists alphabetically
   - Improved type safety

3. **API Integration**
   - Fixed API key handling in requests
   - Proper HTML content handling for scraping
   - Improved response processing

## Usage Examples

### 1. Scrape URL
```javascript
{
    "resource": "scrapeUrl",
    "operation": "get",
    "parameters": {
        "url": "https://example.com",
        "dynamic": false,
        "markdown": false,
        "premium": false,
        "superProxy": false,
        "additionalFields": {
            "aiQuery": "Extract all product names",
            "aiExtractRules": "Find prices and descriptions"
        }
    }
}
```

### 2. Google Search
```javascript
{
    "resource": "googleSearch",
    "operation": "search",
    "parameters": {
        "query": "n8n automation",
        "advance": true,
        "page": "1",
        "location": "US",
        "results": "10"
    }
}
```

### 3. Google Images
```javascript
{
    "resource": "googleImages",
    "operation": "search",
    "parameters": {
        "query": "sunset landscape",
        "results": "20",
        "country": "US",
        "language": "en",
        "imgsz": "l",
        "imageType": "photo",
        "imageColor": "bw",
        "licenses": "f",
        "tbs": "qdr:d",
        "safe": "1"
    }
}
```

### 4. Google News
```javascript
{
    "resource": "googleNews",
    "operation": "search",
    "parameters": {
        "query": "artificial intelligence technology",
        "results": "50",
        "additionalFields": {
            "country": "us",
            "page": 0,
            "domain": "google.com",
            "language": "en",
            "tbs": "qdr:d",
            "safe": "active",
            "nfpr": false
        }
    }
}
```

### 5. Bing Search
```javascript
{
    "resource": "bingSearch",
    "operation": "search",
    "parameters": {
        "query": "web scraping tools",
        "page": 1,
        "country": "US",
        "results": 20,
        "filters": "ex1:'answerType:CalculatorPageType'"
    }
}
```

### 6. Amazon Search
```javascript
{
    "resource": "amazonSearch",
    "operation": "search",
    "parameters": {
        "query": "wireless headphones",
        "country": "US",
        "page": 1,
        "domain": "amazon.com",
        "postal_code": "10001"
    }
}
```

## Resource Parameters

### Scrape URL
- `url` (Required): Target webpage URL
- `dynamic`: Whether to enable JavaScript rendering
- `premium`: Whether to use premium proxy
- `superProxy`: Whether to enable super proxy
- `markdown`: Whether to get response in markdown format
- `wait`: Wait time for dynamic rendering (ms)
- `country`: Geolocation for the request
- `aiQuery`: AI-powered data extraction query
- `aiExtractRules`: Custom extraction rules

### Google Search
- `query` (Required): Search keyword
- `advance`: Whether to enable advanced features
- `page`: Result page number (1-10)
- `location`: Search location/country
- `results`: Number of results (10-100)

### Google Images
- `query` (Required): Search keyword for images
- `results`: Number of results (10-100)
- `country`: Country for geotargeting (US, UK, CA, etc.)
- `language`: Search language (en, es, fr, de, etc.)
- `imgsz`: Filter by size (any, large, medium, icon)
- `imageType`: Filter by type (any, face, photo, clipart, lineart, animated)
- `imageColor`: Filter by color (any, color, gray, trans, red, orange, yellow, green, teal, blue, purple, pink, white, black, brown)
- `licenses`: Filter by usage rights (any, labeled-for-reuse, labeled-for-reuse-with-modification, etc.)
- `tbs`: Filter by time (any, hour, day, week, month, year)
- `safe`: Safe search level (strict, moderate, off)

### Google News
- `query` (Required): Search keyword for news articles
- `results`: Number of results (1-100)
- `country`: Country for geotargeting (us, uk, in, ca, au, de, fr, jp, br, etc.)
- `page`: Page number (0 for first page, 1 for second page, etc.)
- `domain`: Google domain for local results (e.g., google.co.uk for UK)
- `language`: Search language (en, es, fr, de, it, pt, ru, ja, zh-cn, ko, ar, hi, etc.)
- `lr`: Language restriction in format lang_{language_code} (e.g., lang_en)
- `uule`: Geographic location parameter for tailored results
- `tbs`: Time-based search filter (qdr:h for past hour, qdr:d for past day, qdr:w for past week, qdr:m for past month, qdr:y for past year)
- `safe`: Safe search filter (active/off)
- `nfpr`: Exclude auto-corrected queries (true to exclude, false to include)

### Bing Search
- `query` (Required): Search keyword
- `page`: Page number for pagination
- `country`: Country for geotargeting
- `filters`: Custom search filters
- `results`: Number of results to return

### Amazon Search
- `query` (Required): Product search keyword
- `country`: Country for Amazon marketplace (e.g., US, UK, CA, DE, FR, etc.)
- `page`: Page number for pagination
- `domain`: Amazon domain (e.g., amazon.com, amazon.co.uk)
- `postal_code`: Postal code for location-based results

## API Response Examples

### Google Images Response
```json
{
  "time_taken": 685.692823,
  "ads": [],
  "images_results": [
    {
      "title": "Beautiful Sunset Landscape",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:...",
      "source": "example.com",
      "original": "https://example.com/images/sunset.jpg",
      "link": "https://example.com/sunset-photography",
      "original_height": 1080,
      "original_width": 1920,
      "original_size": "245KB",
      "know_more_link": "https://www.google.com/search/about-this-image?...",
      "is_product": false,
      "rank": 1
    }
  ]
}
```

### Google News Response
```json
{
  "time_taken": 542.123456,
  "ads": [],
  "news_results": [
    {
      "rank": 1,
      "title": "Breakthrough in Artificial Intelligence Technology",
      "link": "https://example-news.com/ai-breakthrough-2024",
      "source": "TechNews",
      "published_date": "3 hours ago",
      "snippet": "Researchers have developed a new AI system that can understand complex human emotions and respond appropriately, marking a significant milestone in artificial intelligence development.",
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:...",
      "rank_page": 1
    },
    {
      "rank": 2,
      "title": "AI Companies Announce Major Partnership",
      "link": "https://business-news.com/ai-partnership",
      "source": "Business Daily",
      "published_date": "5 hours ago",
      "snippet": "Leading technology companies have formed a strategic alliance to accelerate AI research and development, focusing on ethical AI implementation.",
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:...",
      "rank_page": 1
    }
  ]
}
```

## Installation

### For n8n Users

1. Install the package in your n8n instance:
```bash
npm install n8n-nodes-scraping-dog
```

2. Restart your n8n instance to load the new node.

3. The ScrapingDog node will appear in the node palette under the "Transform" category.

### Credentials Setup

1. Create a ScrapingDog API account at [ScrapingDog.com](https://scrapingdog.com)
2. Get your API key from the dashboard
3. In n8n, create new credentials of type "ScrapingDog API"
4. Enter your API key in the credentials configuration

## Development

1. Install dependencies:
```bash
npm install
```

2. Build the node:
```bash
npm run build
```

3. Run with Docker:
```bash
make rebuild-and-logs
```

## Testing

The node includes proper error handling for:
- Invalid API key
- Rate limiting
- Invalid parameters
- Network errors
- Blocked requests

## License

MIT License - see LICENSE file for details 