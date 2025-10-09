# n8n-nodes-signwell

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node package that provides integration with the [SignWell API](https://www.signwell.com/api/) for electronic document signing and template management.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## 🆕 What's New in v1.4.0

### 🎣 **NEW: Webhook Triggers**
Real-time event notifications for document activities! Get instant updates when:
- 📄 **Documents** are created, sent, viewed, signed, or completed
- 📋 **Templates** are created or encounter errors
- ⚠️ **Issues** occur (declined, bounced, expired, canceled)

### ✨ Attachment Requests Support
Request file uploads from recipients during the signing process! Perfect for:
- **Driver's License** verification
- **Insurance Certificates**
- **Credit Card Authorization** forms
- **Identity Documents** and more

### 🎯 Complete SignWell Integration
Now supports **all major SignWell features**:
- ✅ **Recipients** - Multiple signers with role assignment
- ✅ **Template Variables** - Dynamic text replacement
- ✅ **Template Fields** - Pre-fill form fields
- ✅ **Attachment Requests** - File upload requirements
- ✅ **Webhook Triggers** - Real-time event notifications
- ✅ **Webhook Management** - Create, list, and delete webhooks

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install**
3. Enter `n8n-nodes-signwell` as the npm package name
4. Agree to the risks of using community nodes
5. Select **Install**

### Manual Installation

To install the node locally for development:

```bash
# Clone the repository
git clone https://github.com/davidstillson/n8n-nodes-signwell.git
cd n8n-nodes-signwell

# Install dependencies
pnpm install

# Build the package
pnpm build

# Link to your n8n installation
npm link
cd ~/.n8n/nodes
npm link n8n-nodes-signwell
```

## Prerequisites

You need a SignWell account and API key to use this node. You can get your API key from your SignWell account under **Settings > API**.

## Credentials

This package includes a **SignWell API** credential type. Configure it with:

- **API Key**: Your SignWell API key
- **Test Mode**: Enable for testing (optional)
- **Base URL**: SignWell API base URL (default: `https://www.signwell.com/api/v1`)

## Nodes

### SignWell

A unified node for interacting with the SignWell API, supporting:
- **Document Operations** - Create, manage, and track documents
- **Template Operations** - Create and manage document templates
- **Webhook Management** - Create, list, and delete webhooks
- **Webhook Triggers** - Listen for real-time SignWell events and automatically start workflows

#### Resources

The SignWell node provides two main resources:

##### Documents

Interact with SignWell documents for electronic signing.

**Operations:**
- **Create From Template**: Create a new document from an existing template (supports recipients, template variables, template fields, and attachment requests)
- **Get**: Retrieve document information
- **Delete**: Delete a document
- **Get Completed PDF**: Download the completed signed PDF
- **Send Reminder**: Send a signing reminder to recipients

**Create From Template Example:**

```json
{
  "template_id": "template_123",
  "draft": false,
  "test_mode": false,
  "recipients": [
    {
      "id": "recipient_1",
      "name": "John Doe",
      "email": "john@example.com",
      "role": "signer",
      "placeholder_names": ["renter", "customer"]
    }
  ],
  "template_variables": {
    "customer_name": "John Doe",
    "rental_dates": "2024-01-15 to 2024-01-22",
    "total_amount": "$1,250.00"
  },
  "template_fields": [
    {
      "api_id": "start_date",
      "value": "2024-01-15"
    },
    {
      "api_id": "end_date",
      "value": "2024-01-22"
    }
  ],
  "attachment_requests": [
    {
      "name": "Driver's License",
      "recipient_id": "recipient_1",
      "required": true
    },
    {
      "name": "Insurance Certificate",
      "recipient_id": "recipient_1",
      "required": false
    }
  ]
}
```

**Template Variables vs Template Fields vs Attachment Requests:**

| Feature | Purpose | Example Use Case |
|---------|---------|------------------|
| **Template Variables** | Text replacement in document content | Replace `{{customer_name}}` with "John Doe" |
| **Template Fields** | Pre-fill form fields | Set date field values, checkbox states |
| **Attachment Requests** | Request file uploads from recipients | Require driver's license, insurance docs |

**Detailed Explanations:**
- **Template Variables**: Used for text replacement in the document content (e.g., replacing `{{customer_name}}` placeholders in the document text)
- **Template Fields**: Used to pre-fill form fields in the document (e.g., setting values for date fields, text inputs, checkboxes, etc.)
- **Attachment Requests**: Used to request file uploads from recipients during the signing process (e.g., driver's license, insurance certificates, etc.)

##### Webhooks

Manage SignWell webhooks and listen for real-time event notifications.

**Operations:**
- **Listen for Events**: Set up webhook trigger to listen for SignWell events (trigger mode)
- **List**: List all registered webhooks
- **Create**: Register a new webhook URL
- **Delete**: Remove a webhook registration

#### Webhook Events

The SignWell node supports the following webhook events when in trigger mode:

| Event | Description | When Triggered |
|-------|-------------|----------------|
| `document_created` | Document created | When a new document is created |
| `document_sent` | Document sent | When a document is sent to recipients |
| `document_viewed` | Document viewed | Each time a signer views the document |
| `document_in_progress` | Document in progress | When signing has started (status: pending) |
| `document_signed` | Document signed | Each time a recipient signs the document |
| `document_completed` | Document completed | When all recipients have signed |
| `document_expired` | Document expired | When a document has expired |
| `document_canceled` | Document canceled | When sender cancels the document |
| `document_declined` | Document declined | When a signer declines the document |
| `document_bounced` | Email bounced | When email delivery fails |
| `document_error` | Document error | When there's an error with the document |
| `template_created` | Template created | When a new template is created |
| `template_error` | Template error | When there's an error with a template |

**Webhook Security:**
- ✅ **Hash Verification**: Automatic HMAC-SHA256 signature verification
- ✅ **Event Filtering**: Only process selected event types
- ✅ **Secure Headers**: Proper authentication and content-type handling

##### Templates

Manage SignWell document templates.

**Operations:**
- **Get**: Retrieve template information
- **Create**: Create a new template
- **Update**: Update an existing template
- **Delete**: Delete a template

**Create Template Example:**

```json
{
  "name": "RV Rental Agreement",
  "file": "base64_encoded_pdf_data",
  "filename": "rv-rental-agreement.pdf",
  "test_mode": false
}
```

## Usage Examples

### RV Rental Management Workflow

This package is designed to integrate with RV rental management systems. Here's a typical workflow:

1. **Customer Books RV** → Triggers n8n workflow
2. **Admin Approves Booking** → Triggers document creation
3. **Create Document From Template** → Uses SignWell Documents node
4. **Send for Signing** → Document automatically sent to customer
5. **Monitor Completion** → SignWell Trigger automatically detects completion

### Webhook-Driven Automation Workflow

With the new webhook trigger functionality, you can create fully automated workflows:

1. **Document Created** → SignWell node (trigger mode) detects creation
2. **Document Sent** → SignWell node (trigger mode) detects sending
3. **Document Signed** → SignWell node (trigger mode) detects each signature
4. **Document Completed** → SignWell node (trigger mode) starts completion workflow
5. **Automatic Actions** → Update database, send notifications, generate invoices

### Example: Document Completion Trigger

```json
{
  "nodes": [
    {
      "name": "Document Completed Trigger",
      "type": "n8n-nodes-signwell.signWell",
      "parameters": {
        "resource": "webhook",
        "operation": "trigger",
        "events": ["document_completed", "document_signed"],
        "verifyHash": true
      }
    }
  ]
}
```

### Example Workflow: Create Rental Agreement

```json
{
  "nodes": [
    {
      "name": "Create Rental Agreement",
      "type": "n8n-nodes-signwell.signWell",
      "parameters": {
        "resource": "document",
        "operation": "createFromTemplate",
        "templateId": "{{ $json.template_id }}",
        "draft": false,
        "recipients": {
          "recipient": [
            {
              "id": "recipient_1",
              "name": "{{ $json.customer_name }}",
              "email": "{{ $json.customer_email }}",
              "role": "signer",
              "placeholder_names": "renter, customer"
            }
          ]
        },
        "templateVariables": "{{ JSON.stringify($json.rental_details) }}",
        "templateFields": {
          "field": [
            {
              "api_id": "start_date",
              "value": "{{ $json.start_date }}"
            },
            {
              "api_id": "end_date",
              "value": "{{ $json.end_date }}"
            }
          ]
        },
        "attachmentRequests": {
          "attachmentRequest": [
            {
              "name": "Driver's License",
              "recipient_id": "recipient_1",
              "required": true
            },
            {
              "name": "Insurance Certificate",
              "recipient_id": "recipient_1",
              "required": false
            }
          ]
        }
      }
    }
  ]
}
```

## API Reference

This package implements the following SignWell API endpoints:

### Documents
- `POST /document_templates/documents` - Create document from template
- `GET /documents/{id}` - Get document
- `DELETE /documents/{id}` - Delete document
- `GET /documents/{id}/completed_pdf` - Get completed PDF
- `POST /documents/{id}/remind` - Send reminder

### Templates
- `GET /document_templates/{id}` - Get template
- `POST /template` - Create template
- `PUT /document_templates/{id}` - Update template
- `DELETE /document_templates/{id}` - Delete template

### Webhooks
- `GET /hooks` - List webhooks
- `POST /hooks` - Create webhook
- `DELETE /hooks/{id}` - Delete webhook

## Error Handling

The nodes include comprehensive error handling:

- **API Errors**: Properly formatted error messages from SignWell API
- **Validation Errors**: Input validation with helpful error messages
- **Network Errors**: Retry logic and timeout handling
- **Continue on Fail**: Option to continue workflow execution on errors

## Test Mode

SignWell provides a test mode for development and testing:

- Test mode requests don't count against your quota
- Documents created in test mode are not actually sent
- Perfect for workflow development and testing

Enable test mode in the credential configuration or per-operation.

## Rate Limits

SignWell API has the following rate limits:

- **General requests**: 100 requests per 60 seconds
- **Test mode**: 20 requests per minute
- **Document/template creation**: 30 requests per minute

The nodes automatically handle rate limiting with appropriate error messages.

## Support

- [SignWell API Documentation](https://developers.signwell.com/)
- [n8n Community Forum](https://community.n8n.io/)
- [GitHub Issues](https://github.com/davidstillson/n8n-nodes-signwell/issues)

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests to the GitHub repository.

## License

[MIT](LICENSE.md)

## Changelog

### 1.4.0 - 2024-07-23
- 🎣 **NEW FEATURE**: Added **Webhook Triggers** integrated into the main SignWell node
  - Listen for real-time SignWell events (document created, sent, signed, completed, etc.)
  - Automatic workflow triggering when document activities occur
  - HMAC-SHA256 hash verification for security
  - Event filtering to only process selected event types
  - Unified interface - no separate trigger node needed
- 🔧 **NEW FEATURE**: Added **Webhook Management** operations
  - List all registered webhooks
  - Create new webhook registrations
  - Delete webhook registrations
- 📚 **Documentation**: Comprehensive webhook documentation and examples
- 🏗️ **Architecture**: Unified node design combining regular operations and webhook triggers

### 1.3.1 - 2024-07-23
- 📚 **Documentation**: Comprehensive README and changelog updates
- 📚 **Documentation**: Added "What's New" section highlighting latest features
- 📚 **Documentation**: Enhanced feature comparison table and examples
- 📚 **Documentation**: Improved version history and migration guidance

### 1.3.0 - 2024-07-23
- ✨ **NEW FEATURE**: Added **Attachment Requests** support for document creation
  - Recipients can now be required to upload files during the signing process
  - Configurable attachment names (e.g., "Driver's License", "Insurance Certificate")
  - Per-recipient attachment assignment via `recipient_id` matching
  - Optional/required attachment settings with `required` boolean flag
  - Attachments shown after all document fields are completed
- 📚 **Documentation**: Updated README with attachment requests examples and usage
- 📚 **Documentation**: Enhanced API structure examples with all supported features
- 🧪 **Testing**: Updated test files to include attachment requests validation
- 📦 **Examples**: Updated workflow examples to demonstrate attachment requests usage

### 1.2.0 - 2024-07-22
- ✨ **NEW FEATURE**: Added **Template Fields** support for pre-filling form fields
  - Pre-fill date fields, text inputs, checkboxes, and other form elements
  - Separate from template variables - used for actual form field values
  - Support for `api_id` and `value` field mapping
  - Full n8n variable expression support for dynamic field values
- 🔧 **API Compatibility**: Fixed recipients structure to use `placeholder_name` (singular) instead of `placeholder_names` (plural)
  - Aligns with SignWell API specification
  - Each recipient now has single placeholder assignment
- 📚 **Documentation**: Added clear distinction between Template Variables vs Template Fields vs Attachment Requests
- 📚 **Documentation**: Updated examples to show proper usage of all features
- 🧪 **Testing**: Added template fields testing and validation

### 1.1.1 - 2024-07-20
- 🐛 **Bug Fix**: Fixed recipients API compatibility issue with SignWell template placeholders
- ✨ **Enhancement**: Added required `id` field for recipients for proper API compliance
- ✨ **Enhancement**: Added optional `placeholder_name` field for mapping recipients to template placeholders
- 📚 **Documentation**: Updated documentation and examples with correct recipient structure
- 🧹 **Code Quality**: Cleaned up unused imports and variables

### 1.1.0 - 2024-07-15
- 🔄 **BREAKING CHANGE**: Combined SignWell Documents and Templates into a single unified SignWell node
- 🔄 **BREAKING CHANGE**: Updated recipients structure to include required `id` field and optional `placeholder_name` field
- ✨ **Enhancement**: Improved user experience with resource-based operation selection (Document/Template)
- 🐛 **Bug Fix**: Fixed recipients API compatibility issues with SignWell template placeholders
- ✅ **Compatibility**: Maintained all existing functionality from both previous nodes
- 📚 **Documentation**: Updated documentation to reflect new combined node structure and recipient format
- 🏗️ **Architecture**: Cleaner package structure with single node registration

### 1.0.0 - 2024-07-01
- 🎉 **Initial Release**: Complete SignWell API integration for n8n
- 📄 **Documents**: Full document lifecycle management (create, get, delete, PDF download, reminders)
- 📋 **Templates**: Complete template CRUD operations (create, read, update, delete)
- 🔐 **Authentication**: SignWell API credentials with API key authentication
- 🛡️ **Error Handling**: Comprehensive error handling and validation
- 🧪 **Test Mode**: Full test mode support for development and testing
- ⚡ **Rate Limiting**: Rate limiting awareness with proper error messages
- 📚 **Documentation**: Complete documentation with examples and API reference
