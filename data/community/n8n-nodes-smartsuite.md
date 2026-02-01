# n8n-nodes-smartsuite

This is an n8n community node for SmartSuite. It allows you to interact with SmartSuite's API to manage records, search data, and perform operations on your SmartSuite solutions. v0.12.5.

## Features

- Get records by ID
- List records from a table
- Search records with filters
- Update records
- Support for various field types and operators
- Comprehensive filtering options
- AI Agent tool integration
- Improved date field handling for due_date fields

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Usage

### As a Regular Node

#### Get Record
Retrieve a specific record by its ID.

#### List Records
Get all records from a selected table.

#### Search Records
Search records using filters:
- Select a field to filter on
- Choose a condition (equals, contains, greater than, etc.)
- Enter the value to filter by
- Use AND/OR operators to combine multiple filters

#### Update Record
Update an existing record's fields with new values.

### As an AI Agent Tool

This node is designed to work seamlessly with the n8n AI Agent node. When used as a tool, it provides a structured interface for AI to interact with SmartSuite data.

#### Using with AI Agent

1. Add the SmartSuite node to your workflow
2. Connect it to the "Tools" input of the AI Agent node
3. Configure your SmartSuite credentials in the node
4. The AI Agent will automatically recognize the SmartSuite tool and its capabilities

#### Tool Capabilities

1. **Get Records**
   - Retrieve specific records by ID
   - Returns structured data with success/error status

2. **List Records**
   - Get all records from a table
   - Option to return hydrated records with full field data

3. **Search Records**
   - Search records using multiple filters
   - Support for various field types and operators
   - AND/OR logic for combining filters

4. **Update Records**
   - Update existing records with new values
   - Support for updating multiple fields at once

#### Tool Response Format

The tool returns responses in a consistent format:

```json
{
  "success": true,
  "data": {
    // The actual record data
  },
  "operation": "get|list|search|update",
  "resource": "record",
  "tableId": "your-table-id"
}
```

In case of errors:
```json
{
  "success": false,
  "error": "Error message",
  "operation": "get|list|search|update",
  "resource": "record",
  "tableId": "your-table-id"
}
```

## Credentials

To use this node, you'll need to set up your SmartSuite API credentials:

1. Log in to your SmartSuite account
2. Go to Settings > API
3. Generate a new API key
4. In n8n, add your SmartSuite credentials:
   - API Key: Your SmartSuite API key
   - Base URL: https://api.smartsuite.com/v1

## Security

### Known Vulnerabilities

This node has some known security vulnerabilities in its dependencies:

1. **High Severity**: Axios SSRF and Credential Leakage Vulnerability
   - Affects: `axios` package (transitive dependency)
   - Impact: Potential Server-Side Request Forgery (SSRF) and credential leakage
   - Mitigation: This vulnerability only affects requests to untrusted URLs. The SmartSuite node only makes requests to the SmartSuite API (a trusted domain) and handles credentials securely through n8n's credential system.

### Security Best Practices

1. **API Key Management**
   - Never share your SmartSuite API key
   - Use n8n's credential system to store your API key securely
   - Rotate your API key if you suspect it has been compromised

2. **Data Access**
   - Only grant the minimum required permissions to your SmartSuite API key
   - Review your SmartSuite audit logs regularly for suspicious activity
   - Use the principle of least privilege when setting up API access

3. **Network Security**
   - Ensure your n8n instance is running behind a secure network
   - Use HTTPS for all API communications
   - Keep your n8n instance and its dependencies up to date

### Reporting Security Issues

If you discover a security vulnerability in this node, please report it responsibly:

1. Do not create public issues for security vulnerabilities
2. Email security details to: [jacobwoodward@gmail.com](mailto:jacobwoodward@gmail.com)
3. Include a detailed description of the vulnerability
4. Provide steps to reproduce the issue
5. Include any relevant logs or error messages

We will respond to security reports within 48 hours and work to resolve critical issues as quickly as possible.

## Resources

- [SmartSuite API Documentation](https://docs.smartsuite.com/api)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [n8n Community Forum](https://community.n8n.io/)
- [n8n AI Agent Documentation](https://docs.n8n.io/ai-agent/)

## License

MIT License - see the [LICENSE](LICENSE) file for details 
