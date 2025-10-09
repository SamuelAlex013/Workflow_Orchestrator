# n8n-nodes-marketing-architects-node

[![npm](https://img.shields.io/npm/v/n8n-nodes-marketing-architects-node)](https://www.npmjs.com/package/n8n-nodes-marketing-architects-node)
[![license](https://img.shields.io/npm/l/n8n-nodes-marketing-architects-node)](https://en.wikipedia.org/wiki/MIT_license)
[![developed by](https://img.shields.io/badge/developed_by-MarketingArchitects-white)](https://marketingarchitects.com)

This is an n8n community node that allows you to integrate Marketing Architects API into your n8n workflows.

Marketing Architects is a platform for creating and managing marketing campaigns, providing AI-powered text completion, image generation, and project management capabilities.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [Version History](#version-history)
- [Development](#development)
- [Adding New Features](#adding-new-features)
- [Version Management](#version-management)
- [Publishing to npm](#publishing-to-npm)

## Version History

### v0.6.0 (Latest)

- **New Feature**: Added OpenAI Sora video generation integration with three new operations
- **Enhanced**: Create videos using OpenAI's Sora model (Sora 2 and Sora 2 Pro) with customizable size and duration options
- **New Operation**: Get Sora Video Status - Check the current status of video generation by ID
- **New Operation**: Get Sora Video URL - Retrieve download URLs for completed Sora videos
- **Improved**: Comprehensive video workflow support from creation to download

### v0.5.2

- **New Feature**: Added Image Analysis operation to analyze images with custom prompts and extract insights
- **Enhanced**: Image analysis supports both file uploads and URL-based analysis with customizable prompts
- **Improved**: Better error handling and retry mechanisms for image analysis operations

### v0.5.1

- **New Feature**: Added Image Resize operation with configurable settings for fit, position, background color, output format, and quality
- **Enhanced**: Collage creation now includes fit and letterbox color options for better image composition
- **Improved**: Enhanced video analysis with custom prompt and output schema support

### v0.5.0

- **New Feature**: Added comprehensive video analysis capabilities
- **Enhanced**: Video analysis now supports custom prompts and structured output schemas
- **Improved**: Better error handling and retry mechanisms across all operations

### v0.4.1

- **Enhanced**: Added configurable retry settings to all node fields
- **Fixed**: Capitalized 'Seconds' in 'Retry Delay' field labels for consistency
- **Improved**: Better error handling and user experience

### v0.4.0

- **New Feature**: Added Collage creation operation for combining multiple images
- **New Feature**: Added Brand information retrieval functionality
- **Enhanced**: Improved documentation and streamlined setup instructions

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node provides six main resource types with the following operations:

### Brand Resource

- **Get Brand Info**: Retrieve brand information and insights for a given domain

### Text Resource

- **Text Completion**: Generate AI-powered text completions for given prompts using the OpenRouter API

### Image Resource

- **Image Generation**: Create AI-generated images from text prompts using Replicate API
- **Image Resize**: Resize images with configurable fit, position, background color, output format, and quality settings
- **Analyze Image**: Analyze images with custom prompts to extract insights, metadata, and answer specific questions about image content

### Video Resource

- **Video Generation**: Create AI-generated videos from text prompts using advanced video generation APIs
- **Create Video with Sora**: Generate videos using OpenAI's Sora model with customizable parameters (model version, size, duration, and optional input reference)
- **Get Sora Video Status**: Retrieve the current status of a Sora video generation by video ID
- **Get Sora Video URL**: Retrieve the download URL for a completed Sora video by video ID
- **Analyze Video**: Analyze video content from a given URL to extract insights and metadata with custom prompts and output schemas

### Collage Resource

- **Create Collage**: Combine multiple images into a single collage with configurable layout, fit options, and letterbox color settings

### Project Resource

- **Log Event**: Log events to track project activities and workflow executions

## Credentials

The Marketing Architects API requires authentication using the following credentials:

- **Token**: Your Marketing Architects API bearer token for authentication
- **Domain**: The API endpoint URL (defaults to `https://pushbtn.api.misfitsandmachines.com`)

To obtain your API credentials, visit the [Marketing Architects API Documentation](https://pushbtn.api.misfitsandmachines.com).

## Compatibility

- n8n 1.110.1 and above
- Node.js 20.15 and above
- Current version: 0.6.0

## Usage

### Basic Setup

1. Install the node following the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/)
2. Configure your Marketing Architects API credentials
3. Add the Marketing Architects node to your workflow
4. Select the desired resource (Brand, Text, Image, Video, Collage, or Project) and operation
5. Configure the operation parameters and execute your workflow

### Using Sora Video Generation

The Sora video operations enable a complete workflow for AI-powered video creation:

#### 1. Create Video with Sora

Generate videos using OpenAI's Sora model with the following parameters:

- **Prompt** (required): Describe the video you want to generate
- **Model**: Choose between Sora 2 (default) or Sora 2 Pro
- **Size**: Select resolution - 1280x720 (720p), 1920x1080 (1080p), or 720x1280 (portrait)
- **Duration**: Choose video length - 4, 8 (default), 12, or 16 seconds
- **Options**: Optionally add input reference for additional control

#### 2. Get Sora Video Status

Check the generation status of your video by providing the video ID returned from the creation step.

#### 3. Get Sora Video URL

Once your video generation is complete, retrieve the download URL using the video ID.

**Example Workflow:**

1. Use "Create Video with Sora" to start generation → Returns video ID
2. Use "Get Sora Video Status" to monitor progress → Check if completed
3. Use "Get Sora Video URL" to download → Retrieve final video URL

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Marketing Architects API Documentation](https://pushbtn.api.misfitsandmachines.com)
- [Repository](https://github.com/marketingarchitects/n8n-nodes-marketing-architects-node)

## Development

### Prerequisites

- Node.js 20.15 or higher
- npm package manager

### Run an initial build and make it linkable to n8n

```bash
npm run build
npm link
```

### List nodes and credentials in package.json

```json
"n8n": {
  "n8nNodesApiVersion": 1,
  "credentials": [
    "dist/credentials/MarketingArchitectsApi.credentials.js"
  ],
  "nodes": [
    "dist/nodes/MarketingArchitects/MarketingArchitects.node.js"
  ]
}
```

### Link build to n8n

```bash
# In the nodes directory within your n8n installation
cd ~/.n8n/nodes

# node-package-name is the name from the package.json
npm link n8n-nodes-marketing-architects-node
```

### Start n8n and see your node

```bash
n8n start
```

### Development Commands

```bash
# Build the project
npm run build

# Watch for changes during development
npm run dev

# Format code
npm run format

# Lint code
npm run lint

# Fix linting issues
npm run lintfix
```

### Restart n8n to see your changes

```bash
n8n start
```

## Adding New Features

### 1. Create New Operation Files

When adding new operations, create corresponding files in the `nodes/MarketingArchitects/` directory:

```bash
# Example: Adding a new "Analytics" resource
touch nodes/MarketingArchitects/Analytics.ts
```

### 2. Update Main Node File

Add your new resource and operations to `MarketingArchitects.node.ts`:

```typescript
// Import your new operation fields
import { analyticsFields } from './Analytics';

// Add to properties array
properties: [
	// ... existing resources
	{
		displayName: 'Analytics',
		name: 'analytics',
		value: 'analytics',
	},
	// ... existing operations
	...analyticsFields,
];
```

### 3. Update Node Configuration

Modify `MarketingArchitects.node.json` if needed:

```json
{
	"node": "n8n-nodes-base.marketingArchitects",
	"nodeVersion": "1.1", // Increment when adding features
	"categories": ["Utility", "Marketing", "Analytics"] // Add new categories
}
```

### 4. Test Your Changes

```bash
# Build and test
npm run build
npm run lint
npm run format

# Link to n8n and test
npm link
cd ~/.n8n/nodes
npm link n8n-nodes-marketing-architects-node
n8n start
```

## Publishing to npm

### Automated GitHub Actions Workflow

This project includes an automated GitHub Actions workflow that handles the entire publishing process. This is the **recommended approach** for publishing new versions.

#### Setup (already done)

1. **Add NPM_TOKEN to GitHub Secrets**:
   - Generate a token at [npmjs.com/settings/tokens](https://www.npmjs.com/settings/tokens)
   - Add to GitHub: Settings → Secrets and variables → Actions → New repository secret
   - Name: `NPM_TOKEN`, Value: your npm publish token

#### Publishing a New Version

1. Commit your changes to main branch
1. Go to **Actions** → **Manual Release & Publish**
1. Click **"Run workflow"**
1. Choose version type (patch/minor/major)
1. Add optional release notes
1. Click **"Run workflow"**

The workflow automatically:

- ✅ Runs quality checks (linting, formatting, build)
- ✅ Bumps version in package.json
- ✅ Updates README version history
- ✅ Publishes to npm
- ✅ Creates GitHub release with installation instructions

#### Testing Before Publishing

Use the **"Skip npm publish"** option to test version bumping and GitHub releases without actually publishing to npm.

### Manual CLI Publishing (Alternative)

If you prefer manual publishing:

```bash
# Build and quality checks
npm run build
npm run lint
npm run format

# Bump version and publish
npm version patch  # or minor/major
npm publish

# Create GitHub release
git tag v$(node -p "require('./package.json').version")
git push origin --tags
```

**Note**: Manual publishing requires npm login and doesn't include automated quality checks or documentation updates.
