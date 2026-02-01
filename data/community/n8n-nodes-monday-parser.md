# n8n-nodes-monday-parser

Custom n8n node for parsing and structuring Monday.com data with advanced column type handling.

## Description

This node provides comprehensive parsing of Monday.com data, transforming complex column values into structured, easily accessible formats. It supports all major Monday.com column types and provides both detailed and simplified data representations.

## Installation

### Via npm (Recommended)

`ash
npm install n8n-nodes-monday-parser
`

### Via n8n Community Nodes

1. Go to **Settings  Community Nodes** in n8n
2. Click **"Install a community node"**
3. Enter: 
8n-nodes-monday-parser
4. Click **Install**

### Via Environment Variable (for self-hosted)

`ash
N8N_COMMUNITY_PACKAGES=n8n-nodes-monday-parser
`

## Usage

1. Add the **"Monday Parser"** node to your workflow
2. In the **Input JSON** field, provide your Monday.com data in JSON format
3. The node will automatically parse and structure the data

## Supported Column Types

The node supports parsing of all Monday.com column types:

- **Basic Types**: text, numbers, checkbox, status
- **People & Teams**: people assignments with counts
- **Dates & Time**: date, timeline, time tracking, world clock
- **Files & Media**: file attachments, images
- **Relations**: board relations, dependencies, mirror columns
- **Communication**: email, phone, link columns
- **Advanced**: location, country, rating, vote, formula
- **Custom**: tags, dropdown, color, button
- And many more...

## Input Format

The node expects Monday.com data in JSON format. Example:

`json
{
  "id": "123456789",
  "name": "Sample Item",
  "created_at": "2023-01-01T00:00:00Z",
  "state": "active",
  "column_values": [
    {
      "id": "status",
      "type": "status",
      "value": "{\"index\": 1, \"label\": \"Working on it\"}",
      "text": "Working on it",
      "column": {"title": "Status"}
    }
  ]
}
`

## Output Format

The node returns structured data with:

- **Parsed column values** with type-specific formatting
- **Mappable values** for easy workflow integration
- **Metadata** including board, group, and timing information

`json
{
  "id": "123456789",
  "name": "Sample Item",
  "column_values": [...],
  "mappable_column_values": {
    "status": "Working on it",
    "checkbox": {"checked": true, "text": "Done"}
  }
}
`

## Features

-  **Complete column type support** - Handles all Monday.com column types
-  **Smart JSON parsing** - Automatically handles string and object values
-  **Error handling** - Graceful fallbacks for malformed data
-  **Type safety** - TypeScript implementation with proper typing
-  **Performance optimized** - Efficient parsing algorithms
-  **Easy integration** - Clean, structured output for workflow use

## Development

`ash
# Install dependencies
npm install

# Build the project
npm run build

# Development mode
npm run dev

# Lint code
npm run lint
`

## License

MIT

## Support

For issues and feature requests, please visit the [GitHub repository](https://github.com/retailbox-automation/n8n-monday-parser).
