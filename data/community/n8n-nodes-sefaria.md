# n8n-nodes-sefaria

This package provides n8n nodes to interact with the [Sefaria API](https://www.sefaria.org/developers), allowing you to access Jewish texts and connections programmatically in your n8n workflows.

## Features

The Sefaria node allows you to:
- Access the complete Sefaria library of Jewish texts
- Search across all texts
- Retrieve specific texts by reference
- Get text metadata and structure
- Access links between texts
- Retrieve user public collections and notes

## Installation

To install this node in your n8n instance:

```bash
npm install n8n-nodes-sefaria
```

## Usage

1. Add the Sefaria node to your workflow
2. Configure the node with your desired operation:
   - Text Retrieval
   - Search
   - Index API
   - Links API
   - Collections API

No API key is required for most operations, as Sefaria's API is freely available. However, some operations may have rate limits.

## Example Usage

### Get a Text
Retrieve a specific text passage:
1. Select the "Text API" operation
2. Enter the text reference (e.g., "Genesis 1:1")
3. Choose optional parameters like language and version

### Search Texts
Search across Sefaria's library:
1. Select the "Search API" operation
2. Enter your search query
3. Configure filters like language and text types

## Development

To run this node locally for development:

```bash
# Install dependencies
npm install

# Build the node
npm run build

# Link to your local n8n instance
npm link

# Start n8n with your local node
n8n start
```

## Resources

- [Sefaria API Documentation](https://www.sefaria.org/developers)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](LICENSE.md)
