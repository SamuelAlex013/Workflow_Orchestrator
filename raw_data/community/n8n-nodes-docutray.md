# n8n-nodes-docutray

This is an n8n community node package that provides seamless integration with [Docutray](https://docutray.com/), a powerful document processing and OCR service. It includes a unified node with organized resource groups to automate document processing and knowledge base search workflows directly within your n8n automations.

## Features

- **Document OCR**: Extract text from images and PDFs using advanced OCR technology
- **Document Type Identification**: Automatically identify document types with confidence scores
- **Knowledge Base Search**: RAG-based semantic search in knowledge bases for intelligent information retrieval
- **Dynamic Knowledge Base Selector**: Dropdown selection from available knowledge bases with metadata
- **Multiple Input Methods**: Support for file uploads, Base64 encoded images, and image URLs
- **Wide Format Support**: JPEG, PNG, GIF, BMP, WebP, and PDF files (up to 100MB)

## Installation

Follow the [n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to install this package in your n8n instance.

## Credentials

To use this node, you'll need a Docutray API key:

1. Sign up for a [Docutray account](https://docutray.com/)
2. Navigate to your API settings in the dashboard
3. Generate an API key
4. Configure the "Docutray API" credentials in n8n with your API key

## Available Node

This package includes a unified Docutray node with organized resource groups:

### Docutray Node

A comprehensive node that provides access to all Docutray services through organized resource groups. Users first select a resource type, then choose from available operations for that resource.

#### Document Resource

Handles document OCR and type identification operations.

#### Convert Operation
Extract text from documents using OCR technology.

**Supported Methods:**
- Upload file directly
- Provide Base64 encoded image
- Specify image URL for automatic download

**Parameters:**
- Document type code (required)
- Image content type (optional)
- Document metadata (optional)

#### Identify Operation
Automatically identify document types from a list of options.

**Supported Methods:**
- Upload file directly
- Provide Base64 encoded image
- Specify image URL for automatic download

**Parameters:**
- Document type code options (array of possible document types)
- Document metadata (optional)

**Response includes:**
- Primary document type with confidence score
- Alternative document type suggestions

#### Knowledge Base Resource

Handles semantic search operations within knowledge bases using RAG technology.

##### Search Operation
Perform semantic search within knowledge bases using RAG technology.

**Parameters:**
- Knowledge Base Name or ID (required) - Select from dropdown or enter ID manually
- Query (required) - Search query text (max 1000 characters)
- Limit (optional) - Maximum number of results (1-50, default: 50)
- Similarity Threshold (optional) - Minimum similarity threshold (0-1, default: 0.7)
- Include Metadata (optional) - Whether to include metadata in results (default: true)

**Features:**
- Dynamic knowledge base selector with dropdown showing available bases
- Displays knowledge base name, description, and document count
- Fallback to manual ID entry if API is unavailable

**Response includes:**
- Semantic search results with relevance scores
- Document excerpts and content snippets
- Optional metadata for each result

## Compatibility

This node has been tested with n8n version 1.94.0 and newer.

## Resources

- [Docutray API Documentation](https://docs.docutray.com/)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Docutray Website](https://docutray.com/)

## License

[MIT](LICENSE.md)
