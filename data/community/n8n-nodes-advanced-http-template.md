# n8n-nodes-advanced-http

This is an n8n community node that provides an Advanced HTTP Request node with dynamic type conversion and enhanced security features.

## Features

- **Dynamic Type Conversion**: Automatically converts typed values from your data sources
- **Enhanced Security**: Built-in URL validation and secure header handling
- **Flexible Configuration**: Use static configuration or dynamic data from previous nodes
- **Type Safety**: Supports string, integer, number, boolean, array, and object types
- **Error Handling**: Comprehensive error handling with continue-on-fail support
- **Full Response**: Option to return complete HTTP response including headers

## Installation

### Using n8n Community Nodes

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-advanced-http`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-advanced-http
```

## Usage

### Basic HTTP Request

1. Add the **Advanced HTTP Request** node to your workflow
2. Configure:
   - **Method**: GET, POST, PUT, PATCH, DELETE, etc.
   - **URL**: The endpoint URL
   - **Headers**: Any required headers
   - **Body**: Request body for POST/PUT/PATCH

### Dynamic Data with Type Conversion

Enable **Use Dynamic Data** to process incoming data with type annotations:

```json
{
  "query": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "name": {
        "type": "string",
        "value": "John Doe"
      },
      "age": {
        "type": "integer",
        "value": "30"
      },
      "active": {
        "type": "boolean",
        "value": "true"
      },
      "tags": {
        "type": "array",
        "value": "[\"admin\", \"user\"]"
      }
    }
  }
}
```

### Type Conversion

The node supports the following type conversions:

| Type | Input | Output |
|------|-------|--------|
| string | Any value | String representation |
| integer | "123" | 123 |
| number | "123.45" | 123.45 |
| boolean | "true"/"false" | true/false |
| array | "[1,2,3]" | [1,2,3] |
| object | '{"key":"value"}' | {key:"value"} |

### Options

- **Timeout**: Request timeout in milliseconds (default: 30000)
- **Validate SSL Certificate**: Whether to validate SSL certificates
- **Follow Redirects**: Automatically follow HTTP redirects
- **Max Redirects**: Maximum number of redirects to follow
- **Return Full Response**: Include headers and status in response

## Example Workflows

### API Integration with Credential Management

```json
{
  "nodes": [
    {
      "name": "Get API Credentials",
      "type": "n8n-nodes-base.supabase",
      "parameters": {
        "operation": "get",
        "table": "credentials"
      }
    },
    {
      "name": "Advanced HTTP Request",
      "type": "n8n-nodes-advanced-http.advancedHttp",
      "parameters": {
        "useDynamicData": true
      }
    }
  ]
}
```

## Security Features

### Authentication Header Protection

This node includes built-in security features to protect sensitive authentication data:

1. **Automatic Header Masking**: When returning full responses, sensitive headers are automatically masked:
   - `Authorization`, `X-API-Key`, `Token`, etc. are partially redacted
   - Shows only first and last 3 characters for debugging (e.g., `Bea...xyz`)
   - Completely redacts short tokens as `[REDACTED]`

2. **Credential Integration**: The node integrates with n8n's credential system:
   - Supports `httpBasicAuth` and `httpHeaderAuth` credentials
   - Credentials are never exposed in logs or outputs
   - n8n handles credential encryption and storage

3. **No Logging of Sensitive Data**: Unlike curl commands, this node:
   - Never logs full authentication headers
   - Doesn't expose credentials in error messages
   - Keeps sensitive data within n8n's secure credential system

### Additional Security Best Practices

1. **URL Validation** - Automatically validates URLs to prevent SSRF attacks
2. **SSL/TLS Verification** - Validates SSL certificates by default
3. **Timeout Protection** - Default 30-second timeout prevents hanging requests
4. **Error Handling** - Errors never expose full request details with credentials
5. **Type Safety** - Strong type validation prevents injection attacks

## Development

```bash
# Install dependencies
npm install

# Run tests
npm test

# Build
npm run build

# Lint
npm run lint
```

## Why Use This Over Curl?

1. **Security**: Authentication headers are protected and never exposed
2. **Integration**: Native n8n node with proper error handling
3. **Type Safety**: Automatic type conversion with validation
4. **No Shell Risk**: No command injection vulnerabilities
5. **Better Performance**: Direct HTTP calls without shell overhead

## License

MIT

## Author

dwillitzer

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and feature requests, please use the [GitHub issues page](https://github.com/dwillitzer/n8n-nodes-advanced-http/issues).