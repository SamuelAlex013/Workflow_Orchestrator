# n8n-nodes-kylas

This is an n8n community node that lets you use Kylas CRM in your n8n workflows.

Kylas is a comprehensive sales CRM platform designed for growing businesses. It provides lead management, sales automation, contact management, and pipeline tracking capabilities to help sales teams streamline their processes and increase productivity.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Advanced Features](#advanced-features)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [Version History](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Manual Installation

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-kylas`
4. Agree to the risks of using community nodes
5. Select **Install**

After installation restart n8n to register the community node.

## Operations

The Kylas node supports the following operations:

### User
- **Get**: Retrieve user information by ID

### Company
- **Get All**: Retrieve all companies with advanced filtering options
  - Support for field-based filtering
  - JSON rule-based filtering with operators (equal, contains, etc.)
  - Pagination support

### Lead
- **Create**: Create a new lead with custom fields support
- **Get**: Retrieve lead information by ID
- **Update**: Update existing lead information
- **Search**: Search for leads using various criteria
- **Custom Fields**: Full support for dynamic custom fields with type validation

## Credentials

To use this node, you need to authenticate with Kylas using an API key.

### Prerequisites

1. You must have a Kylas CRM account
2. You need to generate an API key from your Kylas account

### Setting up Authentication

1. Log in to your Kylas CRM account
2. Navigate to your account settings or API section
3. Generate a new API key
4. In n8n, create new credentials for "Kylas API"
5. Enter your API key in the credentials configuration

### Authentication Method

The node uses API key authentication via the `api-key` header. The credentials are automatically applied to all requests to the Kylas API.

## Compatibility

- **Minimum n8n version**: 0.198.0
- **Node API version**: 1
- **Tested with n8n versions**: 0.198.0+

This node follows n8n's latest development standards and should be compatible with all recent versions of n8n.

## Usage

### Basic Lead Creation

1. Add the Kylas node to your workflow
2. Select "Lead" as the resource
3. Choose "Create" as the operation
4. Fill in the required lead information
5. Optionally configure custom fields

### Company Filtering

The company "Get All" operation supports advanced filtering:

- **Simple filtering**: Use the fields array to specify which fields to return
- **Advanced filtering**: Use JSON rules with conditions like:
  - `equal`: Exact match
  - `contains`: Partial match
  - Support for multiple field types (text, number, date, etc.)

### Custom Fields

The node provides dynamic custom field support for leads:

- Custom fields are automatically loaded from your Kylas instance
- Field types are validated (TEXT_FIELD, NUMBER, DATE, etc.)
- Required fields are clearly marked
- Supports various field types including text, numbers, dates, and more

## Advanced Features

### Dynamic Custom Fields Loading

The Kylas node automatically fetches and validates custom fields from your Kylas instance:

- **Real-time field loading**: Custom fields are loaded directly from the Kylas API
- **Type validation**: Each field type is validated according to Kylas specifications
- **Required field handling**: Required fields are clearly marked and validated
- **Supported field types**:
  - TEXT_FIELD: Single-line text input
  - NUMBER: Numeric values
  - DATE: Date fields with proper formatting
  - EMAIL: Email address validation
  - PHONE: Phone number fields
  - URL: Website URL fields
  - And more...

### Company Filtering System

Advanced filtering capabilities for company data retrieval:

```json
{
  "fields": ["name", "email", "phone"],
  "jsonRule": {
    "condition": "AND",
    "rules": [
      {
        "field": "name",
        "operator": "contains",
        "value": "Tech"
      },
      {
        "field": "status",
        "operator": "equal",
        "value": "Active"
      }
    ]
  }
}
```

### Error Handling and Validation

- Comprehensive error handling for API responses
- Field type validation before submission
- Duplicate field prevention
- Clear error messages for troubleshooting

## Examples

### Example 1: Create a Lead with Custom Fields

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "customFields": {
    "companyName": "Tech Corp",
    "leadSource": "Website",
    "budget": 50000
  }
}
```

### Example 2: Filter Companies

```json
{
  "fields": ["name", "email", "industry"],
  "jsonRule": {
    "condition": "OR",
    "rules": [
      {
        "field": "industry",
        "operator": "equal",
        "value": "Technology"
      },
      {
        "field": "revenue",
        "operator": "greaterThan",
        "value": 1000000
      }
    ]
  }
}
```

### Example 3: Search Leads

```json
{
  "searchTerm": "john@example.com",
  "filters": {
    "status": "New",
    "source": "Website"
  }
}
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify your API key is correct
   - Check that your Kylas account has API access enabled
   - Ensure the API key hasn't expired

2. **Custom Fields Not Loading**
   - Verify you have permission to access custom fields
   - Check that custom fields are active in your Kylas instance
   - Try refreshing the node configuration

3. **Validation Errors**
   - Ensure required fields are provided
   - Check field types match expected formats
   - Verify field names are correct

4. **Rate Limiting**
   - Kylas API has rate limits; implement delays between requests if needed
   - Use pagination for large data sets

### Debug Tips

- Enable debug mode in n8n to see detailed API requests and responses
- Check the Kylas API documentation for field requirements
- Use the test functionality to verify credentials before running workflows

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Kylas CRM Official Website](https://kylas.io/)
- [Kylas API Documentation](https://www.postman.com/ss0225/test/collection/yikzmca/kylas-apis-public)
- [Kylas Help Center](https://support.kylas.io/portal/en/home)
- [n8n Documentation](https://docs.n8n.io/)

## Version History

### v0.1.0 (Current)

**Initial Release**
- User operations: Get
- Company operations: Get All with advanced filtering
- Lead operations: Create, Get, Update, Search
- Dynamic custom fields support for leads
- Comprehensive error handling and validation
- Support for JSON-based filtering rules
- Field type validation and required field handling

**Features:**
- API key authentication
- Real-time custom field loading
- Advanced company filtering with JSON rules
- Lead management with custom fields
- User management operations
- Comprehensive error handling

**Compatibility:**
- n8n version 0.198.0+
- Kylas API v1

---

## Contributing

This is a community-maintained node. If you encounter issues or have suggestions for improvements, please feel free to contribute or report issues.

## License

MIT License - see the LICENSE file for details.
