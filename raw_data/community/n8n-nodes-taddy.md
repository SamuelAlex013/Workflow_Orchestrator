# n8n-nodes-taddy

This is an n8n community node. It lets you use the Taddy Podcast API in your n8n workflows.

Taddy provides access to over 4 million podcasts and 180+ million episodes through a comprehensive GraphQL API. Search for podcast content, get detailed podcast and episode information, discover popular content, find latest episodes, and access transcripts.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Community package name: `n8n-nodes-taddy`

## Operations

### Search Content
- **Full-text search** across podcasts and episodes with advanced filtering
- **Field selection** - Choose which data fields to include in results
- **Content type filtering** - Search podcasts, episodes, or both
- **Advanced filters** - Language, country, genre, date ranges, duration, and more
- **Exclude terms** - Exclude specific terms from search results
- **Sorting options** - Sort by popularity or exactness
- **Match types** - Exact phrase, all terms, or most terms matching

### Podcast Details
- Get detailed podcast information by UUID, name, iTunes ID, or RSS URL
- Includes episode list, metadata, genres, and statistics

### Episode Details
- Get detailed episode information by UUID, GUID, or name
- Includes podcast series information, transcript data, and chapters

### Popular Content
- Discover trending podcasts with optional language and genre filtering
- Pagination support for browsing popular content

### Latest Episodes
- Get recent episodes from specific podcasts or RSS feeds
- Filter by podcast UUIDs or RSS URLs with pagination

### Transcript
- Retrieve episode transcripts in multiple formats (text, SRT, VTT, JSON)
- Support for on-demand transcript generation

### Top Charts
- Get Apple Podcasts top charts by country with filtering options
- Get top charts by genre with optional country filtering
- Support for both podcast series and episode content types

## Credentials

To use this node, you need to authenticate with the Taddy API:

### Prerequisites
1. Sign up for a Taddy API account at [taddy.org](https://taddy.org)
2. Obtain your API credentials from the Taddy dashboard

### Setting up credentials in n8n
1. In n8n, go to **Settings** > **Credentials**
2. Click **Create New** and search for "Taddy API"
3. Enter your credentials:
   - **X-USER-ID**: Your Taddy user identifier
   - **X-API-KEY**: Your Taddy API key
4. Test the connection and save

### Authentication Method
The node uses header-based authentication, automatically adding the required `X-USER-ID` and `X-API-KEY` headers to all API requests.

## Compatibility

- **Minimum n8n version**: 0.174.0
- **Tested with**: n8n 0.174.0 - 1.0.0+
- **Node.js version**: 16+ (matches n8n requirements)

This node follows n8n community node standards and should be compatible with all modern n8n versions.

## Usage

### Basic Search Example
1. Add the Taddy API node to your workflow
2. Select **Search Content** operation
3. Enter a search term (e.g., "technology podcasts")
4. Configure optional filters like language or date range
5. Choose which fields to include in the response
6. Execute to get search results with metadata

### Working with Results
- **Search results** include pagination metadata as the first item for easy access to `totalCount` and `pagesCount`
- **Episode results** automatically include podcast series information (name, UUID) by default
- **Field selection** is content-type aware - episode-only fields are filtered out for podcast searches

### Advanced Features
- **Exclude terms**: Use the dedicated "Exclude Terms" field to filter out unwanted content
- **Response fields**: Select only the data fields you need to optimize response size
- **Pagination**: Use the metadata from search results to implement pagination workflows
- **Date filtering**: Supports precise date ranges with automatic epoch timestamp conversion

### Common Workflows
- **Content Discovery**: Search → Filter → Extract podcast information for subscriptions
- **Content Analysis**: Search with transcripts → Get transcript → Analyze content
- **Monitoring**: Search for specific topics → Check for new episodes → Send notifications
- **Trend Analysis**: Get top charts by country/genre → Track popular podcast trends

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Taddy API Documentation](https://taddy.org) - Official API documentation and guides
* [GraphQL API Reference](https://taddy.org/developers/graphql) - Complete API schema and examples
* [Node Testing Guide](./docs/testing-guide.md) - Comprehensive testing procedures for this node

## Version History


### 0.1.2 (2025-07-29)
- Repository Url fixed

### 0.1.1 (2025-07-29)
- n8n guidelines checklist
### 0.1.0 (Initial Release)
- Full Taddy API integration with 7 resource types
- Advanced search with field selection and filtering
- Podcast and episode detail operations
- Popular content discovery
- Latest episodes retrieval
- Transcript access with multiple formats
- Top charts by country and genre
- Comprehensive error handling and validation
- Production-ready with extensive testing coverage
