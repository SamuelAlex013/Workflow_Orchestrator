![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-dumplingai

This is an n8n community node that provides integration with [Dumpling AI](https://dumplingai.com) APIs for data extraction, web scraping, document conversion, and AI-powered operations.

[Dumpling AI](https://dumplingai.com) is a comprehensive API platform that provides various data extraction and AI services including YouTube transcript extraction, TikTok data scraping, web scraping, document conversion, and more.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Credentials

You must have a Dumpling AI API key to use this node. You can register for a free account to get an API key here:

https://app.dumplingai.com/register

Once registered, you can find your API key here:

https://app.dumplingai.com/api-keys

Then you'll need to create a credential in n8n for Dumpling AI.

## Usage

Add Dumpling AI to a workflow and configure your operation.

### Available Operations

This node currently supports:

#### Data API Operations
- **Get YouTube Transcript** - Extract transcripts from YouTube videos with timestamps and language options
- **Get TikTok Transcript** - Extract transcripts/captions from TikTok videos
- **Search (Google Web)** - Perform Google web searches with optional content scraping
- **Search Places** - Search Google Places for businesses and locations
- **Search News** - Search Google News for articles
- **Get Google Reviews** - Extract Google Reviews for businesses using keywords, CID, or Place ID

#### Web Scraping Operations
- **Scrape URL** - Extract content from web pages with formatting options

Additional operations will be added in future releases.

#### Get YouTube Transcript

Extract transcripts from YouTube videos with optional timestamps and language preferences.

```json
{
  "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "includeTimestamps": true,
  "timestampsToCombine": 5,
  "preferredLanguage": "en"
}
```

#### Get TikTok Transcript

Extract transcripts/captions from TikTok videos with language preferences.

```json
{
  "videoUrl": "https://www.tiktok.com/@username/video/1234567890",
  "preferredLanguage": "en"
}
```

#### Search (Google Web)

Perform Google web searches with optional content scraping of results.

```json
{
  "query": "artificial intelligence trends 2024",
  "country": "US",
  "language": "en",
  "scrapeResults": true,
  "numResultsToScrape": 3,
  "scrapeFormat": "markdown"
}
```

#### Search Places

Search Google Places for businesses and locations.

```json
{
  "query": "coffee shops near me",
  "location": "New York, NY",
  "language": "en"
}
```

#### Search News

Search Google News for articles and news content.

```json
{
  "query": "climate change",
  "dateRange": "past_week",
  "language": "en"
}
```

#### Get Google Reviews

Extract Google Reviews for businesses using different identification methods.

```json
{
  "inputType": "keyword",
  "keyword": "Starbucks Times Square",
  "reviews": 20,
  "sortBy": "newest"
}
```

#### Scrape URL

Extract content from web pages with customizable formatting and processing options.

```json
{
  "url": "https://example.com",
  "format": "markdown",
  "cleaned": true,
  "renderJs": true
}
```

**Output Formats:**
- **HTML** - Raw HTML content
- **Markdown** - Clean markdown format  
- **Screenshot** - Screenshot of the page

## API Resources

This node currently supports the most popular Dumpling AI APIs. If there's an API missing that you would like to use, please let us know at admin@dumplingai.com

In the meantime, you can also use the [generic HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to construct your requests.

### Coming Soon

- Document Conversion (PDF, Word, Excel, etc.)
- AI Operations (Agent completions, Knowledge base search, Image generation)
- Developer Tools (JavaScript/Python code execution)
- Additional Data APIs (Social media profiles, advanced scraping)

## Related Resources

Dumpling AI's complete API documentation is available here:

https://docs.dumplingai.com/api-reference/introduction

You can also find additional tutorials and resources here:

https://docs.dumplingai.com/guides

## Development

### Release Flow

After merging PRs into master, follow these steps to publish a new version:

```bash
# Switch to master branch and ensure it's up to date
git checkout master
git pull origin master

# Bump version (patch, minor, or major)
npm version patch         # or minor / major

# Push changes and tags
git push origin master
git push origin v$(node -p "require('./package.json').version")
```

The tag push will automatically trigger the GitHub Actions workflow, which will:
1. Build the package
2. Check if the version already exists on npm
3. Publish to npm if it's a new version

You'll see a ✅ job in the Actions tab and the new version will appear on npm within a minute.

## License

[MIT](https://github.com/dumplingai/n8n-nodes-dumplingai/blob/master/LICENSE.md)
