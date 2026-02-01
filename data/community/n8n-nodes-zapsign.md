# n8n-nodes-zapsign

This is an n8n community node that lets you use ZapSign's digital signature API in your n8n workflows.

[ZapSign](https://zapsign.co) is a digital signature platform that enables you to create, send, and manage legally binding electronic signatures for your documents.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-zapsign` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes.
5. Select **Install**.

After installing the node, you can use it like any other node in n8n.

### Manual Installation

To get started install the package in your n8n root directory:

```bash
npm install n8n-nodes-zapsign
```

For Docker-based deployments add the following line before the font installation command in your n8n Dockerfile:

```dockerfile
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-zapsign
```

## Credentials

You'll need to set up ZapSign API credentials to use this node:

1. Sign up for a [ZapSign account](https://zapsign.co)
2. Go to your ZapSign dashboard
3. Navigate to API settings and generate an API key
4. In n8n, create new ZapSign API credentials with:
   - **API Key**: Your ZapSign API key
   - **Environment**: Choose between Production or Sandbox

## Environment Variables (optional)

You can override the default API base URLs using a `.env` file:

```bash
ZAPSIGN_API_BASE_URL=https://api.zapsign.com.br
ZAPSIGN_API_BASE_URL_SANDBOX=https://sandbox.api.zapsign.com.br
```

These are optional; by default the production and sandbox endpoints above are used.

## Operations

### ZapSign Node

The ZapSign node supports the following resources and operations:

#### Document
- **Create**: Upload and create a new document
  - **File Upload**: Upload a file from binary data
  - **Base64**: Provide file content as base64 string
  - **Public Link**: Provide a public URL to the file
- **Get**: Retrieve document details
- **Get All**: List all documents
- **Send**: Send document for signature
- **Cancel**: Cancel a document
- **Download**: Download a signed document

#### Signer
- **Add**: Add a signer to a document
- **Get All**: Get all signers of a document
- **Remove**: Remove a signer from a document
- **Update**: Update signer information

#### Template
- **Get All**: List all available templates
- **Create Document From Template**: Create a new document from a template

#### Webhook
- **Create**: Create a webhook for event notifications
- **Get All**: List all webhooks
- **Delete**: Delete a webhook

### ZapSign Trigger Node

The ZapSign Trigger node allows you to start workflows when ZapSign events occur:

#### Supported Events
- **Document Created**: When a document is created
- **Document Sent**: When a document is sent for signature
- **Document Viewed**: When a document is viewed by a signer
- **Document Signed**: When a document is signed by any signer
- **Document Completed**: When all signers have signed the document
- **Document Cancelled**: When a document is cancelled
- **Document Expired**: When a document expires
- **Signer Added**: When a signer is added to a document
- **Signer Signed**: When a specific signer signs
- **Signer Declined**: When a signer declines to sign

## Example Workflows

### Document Signature Workflow

1. **HTTP Request**: Receive document upload request
2. **ZapSign**: Create document with uploaded file
3. **ZapSign**: Add signers to the document
4. **ZapSign**: Send document for signature
5. **ZapSign Trigger**: Wait for document completion
6. **Email**: Send notification when document is signed

### Template-Based Document Creation

1. **Schedule Trigger**: Run daily
2. **Google Sheets**: Get contract data
3. **ZapSign**: Create document from template
4. **ZapSign**: Add signers from spreadsheet
5. **ZapSign**: Send for signature
6. **Slack**: Notify team

### Webhook Event Processing

1. **ZapSign Trigger**: Listen for document events
2. **Switch**: Route based on event type
3. **Database**: Update document status
4. **Email**: Send appropriate notifications

## File Input Types for Document Creation

The ZapSign node now supports multiple ways to provide files for document creation:

### File Upload (Binary Data)
- Use when you have a file uploaded through n8n's binary data system
- Supports any file type that ZapSign accepts
- Automatically detects filename and MIME type

### Base64 Encoding
- Use when you have file content as a base64 string
- Requires specifying the filename and MIME type manually
- Useful for files generated programmatically or stored as base64

### Public URL
- Use when the file is publicly accessible via a URL
- Automatically downloads the file from the URL
- Attempts to detect filename and MIME type from the URL
- Supports common file formats: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, RTF, images (JPG, PNG, GIF, BMP, TIFF), HTML, XML, JSON

## Authentication Methods

ZapSign supports multiple authentication methods for signers:

- **Email**: Simple email verification
- **SMS**: SMS code verification
- **WhatsApp**: WhatsApp code verification

Additional security features:
- **Document Authentication**: Require ID document upload
- **Facial Recognition**: Verify identity through facial recognition
- **Biometric GOV+**: Government database validation (Brazil)

## API Endpoints Structure

The node assumes the following ZapSign API structure:

```
Base URL: https://api.zapsign.com.br/ (Production)
         https://sandbox.api.zapsign.com.br/ (Sandbox)

Documents:
- POST /v1/documents - Create document
- GET /v1/documents - List documents
- GET /v1/documents/{id} - Get document
- POST /v1/documents/{id}/send - Send document
- POST /v1/documents/{id}/cancel - Cancel document
- GET /v1/documents/{id}/download - Download document

Signers:
- POST /v1/documents/{id}/signers - Add signer
- GET /v1/documents/{id}/signers - List signers
- PUT /v1/documents/{id}/signers/{email} - Update signer
- DELETE /v1/documents/{id}/signers/{email} - Remove signer

Templates:
- GET /v1/templates - List templates
- POST /v1/documents/from-template - Create from template

Webhooks:
- POST /v1/webhooks - Create webhook
- GET /v1/webhooks - List webhooks
- DELETE /v1/webhooks/{id} - Delete webhook
```

## Error Handling

The node includes comprehensive error handling:

- **Authentication errors**: Invalid API key or expired tokens
- **Rate limiting**: Automatic retry with exponential backoff
- **Validation errors**: Missing required fields or invalid data
- **Network errors**: Connection timeouts and retries

All errors are properly formatted and include helpful context for debugging.

## Compatibility

- n8n v0.187.0 and above
- Node.js v18.10 and above

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [ZapSign API Documentation](https://docs.zapsign.com.br/)
- [ZapSign Website](https://zapsign.co)

## Support

For support with this community node:

1. Check the [ZapSign API documentation](https://docs.zapsign.com.br/)
2. Review the [n8n community forum](https://community.n8n.io/)
3. Open an issue on this repository

For ZapSign-specific questions, contact ZapSign support at support@zapsign.co

## License

[MIT](https://github.com/zapsign/n8n-nodes-zapsign/blob/main/LICENSE.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog
### 1.0.22
- Updated "List Documents" operation to fully match ZapSign API specification
- Implements ZapSign API endpoint `GET /api/v1/docs/?page={page}`
- Added comprehensive filtering options:
  - **Page navigation**: Page-based pagination (25 documents per page)
  - **Folder filtering**: Filter by folder path (e.g., "/" for root, "/api/pasta2/" for specific folder)
  - **Deletion status**: Filter deleted vs non-deleted documents
  - **Document status**: Filter by pending, signed, or refused status
  - **Date range**: Filter by creation date (YYYY-MM-DD format)
  - **Sort order**: Ascending, descending, or default sorting
- API returns paginated response with count, next/previous links, and results array
- Response includes temporary file URLs (60-minute expiration) for original_file and signed_file
- Cache duration: 60 minutes as per API documentation
- Supports all query parameters: folder_path, deleted, status, created_from, created_to, sort_order
- **Fixed**: Resolved circular dependency issue with displayOptions that was causing "Max iterations reached" error in n8n
- **Fixed**: Removed displayOptions from child parameters in collections to prevent circular dependency issues
- **Fixed**: Corrected TypeScript formatting and indentation issues

### 1.0.16
- Added "Reorder Documents in Envelope" operation to Document resource
- Implements ZapSign API endpoint `PUT /api/v1/docs/{doc_token}/document-display-order/`
- Allows reordering documents within an envelope while it's still in progress
- Supports multiple document tokens in the desired display order
- Only works on envelope documents (documents that group multiple files)
- Requires document to be in "em andamento" (in progress) status
- Fixed API endpoint to match official documentation exactly

### 1.0.15
- Added "Update Document" operation to Document resource
- Implements ZapSign API endpoint `PUT /api/v1/docs/{doc_token}/`
- Allows updating document data while document is still in progress (not finalized or cancelled)
- Supports updating: document name, signature deadline, folder path, folder token
- Supports renaming extra documents via `extra_docs[]` array
- Only works on documents with "em andamento" (in progress) status
- Fixed API endpoint to match official documentation exactly

### 1.0.14
- Updated Get Document operation to match exact ZapSign API specification
- Changed endpoint from `/api/v1/docs/{id}` to `/api/v1/docs/{id}/` (with trailing slash)
- API now returns comprehensive document information including:
  - Basic document details (ID, status, name, timestamps)
  - File URLs (original_file, signed_file with 60-minute expiration)
  - Complete signer information with authentication and signature status
  - Extra documents array with metadata
  - Template variables (answers array for dynamic templates)
  - Branding settings and metadata (external_id, folder_path, lang, created_by)
- Fixed API endpoint to match official documentation exactly

### 1.0.13

### 1.0.12
- Added "Add Extra Document" operation to Document resource
- Implements ZapSign API endpoint `/api/v1/docs/{doc_principal_token}/upload-extra-doc/`
- Supports both URL and Base64 input methods for extra documents
- Extra documents inherit all settings from the main document
- Maximum of 14 extra documents per main document (API limitation)
- Only PDF files up to 10MB are supported for extra documents

### 1.0.11
- Updated Create Document From Template operation to match exact ZapSign API specification
- Changed endpoint from `/api/v1/docs/from-template` to `/api/v1/models/create-doc/`
- Added comprehensive template parameters: signer info, template variables, branding, WhatsApp automation
- Added support for template data replacement with `data[]` array format
- Added advanced options: folder management, signature ordering, signer permissions
- Fixed parameter names to match API documentation exactly

### 1.0.10
- Added OneClick (ClickWrap) document creation operation
- Added OneClick-specific settings (signature drawing, custom consent text, redirect)
- OneClick documents are simplified for consent capture with minimal configuration
- Maintains compatibility with all file input types (File Upload, Base64, Public Link)
- Added `oneclick: true` flag for OneClick document identification

### 1.0.9
- Fixed document creation to match exact ZapSign API specification
- Changed from form-data to JSON request format
- Updated API endpoints to use correct paths (/api/v1/docs/)
- Added proper parameter names (base64_pdf, url_pdf, base64_docx, url_docx)
- Added required signers array parameter
- Added comprehensive signer configuration options
- Added proper additional fields matching API documentation
- Fixed authentication and request structure issues

### 1.0.8
- Added support for multiple file input types in document creation:
  - Base64 encoding for file content
  - Public URL for file downloads
  - Enhanced file upload with better MIME type detection
- Improved error handling for file processing
- Added comprehensive MIME type support for common file formats

### 1.0.7
- Added support for multiple file input types in document creation:
  - Base64 encoding for file content
  - Public URL for file downloads
  - Enhanced file upload with better MIME type detection
- Improved error handling for file processing
- Added comprehensive MIME type support for common file formats

### 1.0.6
- Corrigido formato de autenticação: alterado de 'Authorization: Bearer' para 'apikey'


### 1.0.5
- Corrigido endpoint de teste para o caminho correto da API ZapSign: /api/v1/docs/?page=1


### 1.0.4
- Corrigido endpoint de teste para autenticação



### 1.0.0
- Initial release
- Support for Document, Signer, Template, and Webhook operations
- ZapSign Trigger node for webhook events
- Complete authentication and error handling
- Support for both Production and Sandbox environments
