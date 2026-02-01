# n8n-nodes-viral-app

This is an n8n community node that lets you use ViralApp in your n8n workflows.

ViralApp is a comprehensive video analytics platform that provides insights and tracking for content across TikTok, Instagram, and YouTube. It helps creators and businesses monitor their social media performance, track competitors, and discover trending content.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents
- [Installation](#installation)  
- [Operations](#operations)  
- [Credentials](#credentials)  
- [Compatibility](#compatibility)  
- [Resources](#resources)  
- [Version History](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### npm Installation
```bash
npm install n8n-nodes-viral-app
```

### GUI Installation
1. Go to **Settings** > **Community Nodes**
2. Click **Install**
3. Enter `n8n-nodes-viral-app`
4. Click **Install**

## Operations

The ViralApp node supports the following resources and operations:

### Account Data
- **Get Top Videos** - Retrieve top performing videos for tracked accounts
- **Get Top Accounts** - Get top performing accounts from your tracked list
- **Get KPIs** - Fetch key performance indicators for accounts
- **Get Interaction Metrics** - Retrieve interaction metrics for accounts
- **Export Daily Gains** - Export daily gains data for accounts

### Video Data  
- **Get Top Videos** - Retrieve top performing videos
- **Get Top Accounts** - Get accounts with top performing videos
- **Get KPIs** - Fetch video performance KPIs
- **Get Interaction Metrics** - Retrieve video interaction metrics
- **Export Daily Gains** - Export daily video gains data

### Tracked Accounts
- **Create** - Add a new tracked account
- **Delete** - Remove a tracked account
- **Get** - Retrieve details of a specific tracked account
- **Get Many** - List multiple tracked accounts with filtering
- **Update** - Modify tracked account settings
- **Export Daily Gains** - Export daily gains for tracked accounts

### Tracked Individual Videos
- **Create** - Add a new tracked video
- **Delete** - Remove a tracked video
- **Get** - Retrieve details of a specific tracked video
- **Get Many** - List multiple tracked videos
- **Update** - Modify tracked video settings

### Projects
- **Create** - Create a new project
- **Delete** - Remove a project
- **Get** - Retrieve project details
- **Get Many** - List multiple projects
- **Update** - Modify project settings

### Integrations
- **Create** - Set up a new integration
- **Delete** - Remove an integration
- **Get** - Retrieve integration details
- **Get Many** - List integrations
- **Update** - Modify integration settings

### General Data
- **Get Categories** - Retrieve available content categories
- **Get Countries** - Get list of supported countries
- **Get Performance KPIs** - Fetch performance KPIs
- **Get Top Videos** - Retrieve overall top performing videos

## Credentials

To use this node, you need to authenticate with the ViralApp API.

### Prerequisites
1. Sign up for a ViralApp account at [viral.app](https://viral.app)
2. Navigate to your account settings
3. Generate an API key

### Setting up credentials in n8n
1. In n8n, go to **Credentials** > **New**
2. Select **ViralApp API** from the list
3. Enter your API key
4. Click **Save**

## Compatibility

- **Minimum n8n version:** 1.0.0
- **Tested with:** n8n 1.0.0 and above
- **Node.js:** 18.10.0 or higher

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [ViralApp API documentation](https://viral.app/api-docs)
* [ViralApp website](https://viral.app)
* [Support](mailto:support@viral.app)

## Development

To contribute to this node or run it locally for development:

```bash
# Install dependencies
pnpm install

# Build the node
pnpm build

# Run in development mode
pnpm dev

# Run linter
pnpm lint

# Run linter and auto-fix
pnpm lintfix
```

## License

[MIT](LICENSE.md)

## Version History

### 0.2.1
- **Simplified parameter handling for tracked accounts and videos**
- Replace resourceLocator with simple string fields:
  * Tracked Accounts refresh: Now uses simple account ID input instead of complex resourceLocator
  * Tracked Individual Videos add/refresh: Now uses simple video ID input instead of resourceLocator
- Fix validation errors: "expected string, received object" issues resolved
- Improve user experience with clearer field descriptions:
  * Account ID: "Native platform account id"
  * Video ID: "Platform-specific video ID"
  * Platform: "Social media platform (tiktok, instagram, youtube)"
- Streamline node usage by removing unnecessary UI complexity

### 0.2.0
- **Major improvements to API parameter coverage and data simplification**
- Add complete parameter coverage for all API endpoints:
  * Projects: Add name filter for searching projects
  * GeneralAnalytics: Add contentTypes filter to interaction-metrics and KPIs operations
  * Integrations: Add provider, search, sortCol, and sortDir parameters for comprehensive filtering
  * TrackedIndividualVideos: Add search parameter for finding specific videos
- Implement Simplify option across all data operations:
  * GeneralAnalytics: All 4 operations now support simplified output
  * Projects: getAll operation returns essential fields only when simplified
  * Integrations: getApps operation provides streamlined app information
- Fix critical date handling issues in General Analytics:
  * Properly format dates to YYYY-MM-DD for API compatibility
  * Remove conflicting routing configurations
  * Ensure consistent date processing across all operations
- Fix data structure issues in simplify operations:
  * Correct field mapping for getKpis (videoCount, viewCount, etc.)
  * Fix getInteractionMetrics to properly access nested dailyMetrics array
  * Remove non-existent fields and add missing ones (bookmarks)
- Improve overall node reliability and user experience

### 0.1.2
- Move @typescript-eslint/utils from devDependencies to dependencies to fix n8n package scanner compatibility

### 0.1.1
- Fix ESLint compatibility by adding @typescript-eslint/utils dependency
- Improve API request handling for POST requests
- Enhance VideoAnalytics functionality with regex extraction for video IDs
- Update parameter naming for better clarity (filters → activityFilters)
- Remove outdated API documentation and routing information
- Add @types/node dependency for better TypeScript support

### 0.1.0
- Initial release
- Support for all major ViralApp API endpoints
- Account Data operations
- Video Data operations  
- Tracked Accounts management
- Tracked Individual Videos management
- Projects management
- Integrations management
- General Data operations