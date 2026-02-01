# n8n-nodes-mistral-ocr

A powerful n8n community node for document OCR (Optical Character Recognition) using Mistral AI's OCR API. Extract text and structured data from documents with ease!

## Features

- 📄 **Basic OCR**: Extract text from documents (PDFs, images)
- 🎯 **Smart Templates**: Pre-configured templates for common document types (invoices, contracts, IDs, etc.)
- 🛠️ **Custom Fields**: Define your own data extraction fields
- 📊 **Element Analysis**: Extract data from charts, tables, and figures
- 🔧 **Advanced Mode**: Full JSON schema control for power users
- 📱 **User-Friendly UI**: No JSON knowledge required for basic use

## Supported Document Types

- **Invoices/Bills** - Extract amounts, dates, customer info
- **Letters/Correspondence** - Extract sender, recipient, dates, references  
- **Contracts** - Extract parties, dates, amounts, terms
- **Receipts** - Extract store info, amounts, items
- **ID Documents** - Extract names, birth dates, ID numbers
- **Research Papers** - Extract titles, authors, abstracts, keywords

## Installation

```bash
npm install n8n-nodes-mistral-ocr
```

## Configuration

1. Get your Mistral API key from [Mistral AI](https://console.mistral.ai/)
2. In n8n, create a new credential of type "Mistral API"
3. Enter your API key

## Project Structure

The project has been modularized for better maintainability:

```
nodes/MistralOcr/
├── MistralOcr.node.ts          # Main node implementation
├── types/
│   └── index.ts                # TypeScript type definitions
├── templates/
│   └── documentTemplates.ts    # Predefined document templates
├── utils/
│   ├── nodeProperties.ts       # UI property definitions
│   └── schemaUtils.ts          # Schema helper functions
├── constants/
│   └── defaults.ts             # Default values and constants
└── mistral.svg                 # Node icon
```

### Module Overview

- **types/**: Contains all TypeScript interfaces and type definitions
- **templates/**: Predefined schemas for common document types (invoices, contracts, etc.)
- **utils/**: Helper functions for schema building, parsing, and UI configuration
- **constants/**: Default values, API endpoints, and limits

## Usage Examples

### Basic OCR
Simply upload a document and extract all text content.

### Invoice Processing with Template
1. Select "OCR with Annotations"
2. Choose "Invoice/Bill" template
3. The node automatically extracts: total amount, customer number, invoice date, etc.

### Custom Field Extraction
1. Select "OCR with Annotations"
2. Choose "Custom Fields"
3. Define your fields in JSON format:

```json
{
  "contract_value": {
    "type": "number",
    "description": "Total contract value"
  },
  "client_name": {
    "type": "string", 
    "description": "Name of the client"
  },
  "due_date": {
    "type": "string",
    "description": "Payment due date"
  }
}
```

### Advanced Mode
For power users who need full control over JSON schemas:
1. Enable "Advanced: Custom JSON Schema"
2. Define complete JSON schemas for document and bbox annotations

## API Limits

- **Document Annotations**: Maximum 8 pages per request
- **File Size**: Up to 50MB per document
- **Total Pages**: Up to 1000 pages per document
- **File Expiry**: 1-168 hours (default: 24 hours)

## Rate Limiting & Error Handling

The node includes intelligent rate limiting and error handling:

- **Automatic Retry**: 429 errors (rate limits) are automatically retried with exponential backoff
- **Smart Backoff**: Delays increase exponentially (1s, 2s, 4s) with randomization to avoid thundering herd
- **Descriptive Errors**: Clear error messages when rate limits are exceeded
- **File Validation**: Pre-upload validation for file size and format
- **Graceful Degradation**: Continue-on-fail support for batch processing

### Rate Limit Error Handling
If you encounter "Service tier capacity exceeded" errors:
1. The node automatically retries up to 3 times
2. Wait times increase with each retry attempt
3. Consider upgrading your Mistral API plan for higher limits
4. For batch processing, add delays between workflow executions

## Development

### Building the Project

```bash
npm run build
```

### Linting

```bash
npm run lint
npm run lint:fix
```

### Code Style

The project follows n8n's coding standards:
- TypeScript for all implementations
- ESLint + Prettier for code formatting
- Comprehensive JSDoc documentation
- Modular architecture for maintainability

## Error Handling

The node includes comprehensive error handling:
- Invalid JSON schema detection
- API rate limiting awareness
- File upload validation
- Graceful degradation with continue-on-fail

## Contributing

Contributions are welcome! The modular structure makes it easy to:
- Add new document templates in `templates/documentTemplates.ts`
- Extend type definitions in `types/index.ts`
- Add utility functions in `utils/`
- Update constants in `constants/defaults.ts`

## Changelog

### v0.4.7 - Rate Limiting & Enhanced Error Handling
- **NEW**: Automatic retry logic for 429 rate limit errors
- **NEW**: Exponential backoff with randomization to prevent thundering herd
- **NEW**: File size validation (50MB limit) before upload
- **NEW**: Enhanced error messages for rate limiting issues
- **IMPROVED**: Better API compliance with Mistral documentation
- **FIXED**: Robust handling of "Service tier capacity exceeded" errors

### v0.3.0 - Modular Architecture
- **BREAKING**: Restructured project into modules for better maintainability
- **NEW**: Separated types, templates, utils, and constants into dedicated modules
- **IMPROVED**: Better code organization and TypeScript support
- **FIXED**: Various linting issues and type safety improvements

### v0.2.0 - User-Friendly UI
- **NEW**: Pre-configured document templates
- **NEW**: Simplified custom field definition
- **NEW**: Element analysis for charts and tables
- **IMPROVED**: No JSON knowledge required for basic use
- **FIXED**: n8n compatibility issues with displayOptions

### v0.1.0 - Initial Release
- Basic OCR functionality
- JSON schema-based annotations
- Mistral API integration

## License

MIT

## Support

- Documentation: [GitHub Repository](https://github.com/yourusername/n8n-nodes-mistral-ocr)
- Issues: [GitHub Issues](https://github.com/yourusername/n8n-nodes-mistral-ocr/issues)
- Mistral API: [Mistral Documentation](https://docs.mistral.ai/)
