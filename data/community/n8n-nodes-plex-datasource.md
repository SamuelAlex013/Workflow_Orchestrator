# n8n Plex ERP Data Source Node

An n8n community node for calling Plex ERP Data Sources via REST API. This node enables seamless integration with Plex ERP systems by executing data source queries with configurable parameters, authentication, and retry mechanisms.

## Features

- 🌐 **Multi-Environment Support**: Production and test environments
- 🏢 **Flexible Deployment**: Support for both cloud and on-premise (colo) Plex deployments
- 🔐 **Secure Authentication**: Basic Auth credentials with secure storage
- 🛠️ **Configurable Body Parameters**: Form-based key-value pairs or raw JSON input
- 🔄 **Retry Mechanism**: Configurable retry logic with exponential backoff
- 📊 **Data Type Conversion**: Automatic conversion for strings, numbers, booleans, and dates
- ⚙️ **Advanced Settings**: Timeout configuration, redirect handling
- 🚫 **Null Handling**: Optional null value filtering

## Installation

To install this community node in n8n:

### Option 1: n8n Community Nodes (Recommended)

1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter: `n8n-nodes-plex-datasource`
4. Click **Install**

### Option 2: Manual Installation

```bash
# For n8n installed via npm
npm install n8n-nodes-plex-datasource

# For n8n installed via Docker
# Add the package to your Docker setup
```

### Option 3: Local Development

```bash
# Clone this repository
git clone https://github.com/your-username/n8n-nodes-plex-datasource.git
cd n8n-nodes-plex-datasource

# Install dependencies
pnpm install

# Build the project
pnpm run build

# Link to your n8n installation
npm link
```

## Configuration

### 1. Credentials Setup

Before using the node, set up your Plex API credentials:

1. Go to **Credentials** in n8n
2. Click **Add Credential**
3. Select **Plex Basic Auth API**
4. Enter your Plex username and password
5. Test the connection
6. Save the credential

### 2. Node Configuration

#### Basic Settings

- **Description**: Free text description of what this data source call does
- **Environment**: Choose between Production or Test
- **Colo Name**: Enter colo name for on-premise deployments (leave blank for cloud)
- **Data Source ID**: The unique identifier for your Plex data source

#### URL Generation

The node automatically generates the correct API URL based on your configuration:

- **Cloud Production**: `https://cloud.plex.com/api/datasources/{ID}/execute?format=2`
- **Cloud Test**: `https://test.cloud.plex.com/api/datasources/{ID}/execute?format=2`
- **Colo Production**: `https://{colo}.on.plex.com/api/datasources/{ID}/execute?format=2`
- **Colo Test**: `https://{colo}.test.on.plex.com/api/datasources/{ID}/execute?format=2`

#### Body Configuration

Choose between two input methods:

##### Key-Value Form
- **Key**: Parameter name
- **Value**: Parameter value
- **Data Type**: string, number, boolean, or date
- **Skip if Null**: Skip parameter if value is null/empty
- **Data Format**: Format specification for dates (e.g., YYYY-MM-DD)

##### Raw JSON
Direct JSON input for complex request bodies.

#### Advanced Settings

- **Retry on Failure**: Enable automatic retry
- **Max Retry Attempts**: 1-10 attempts
- **Retry Wait Time**: 100-30000ms between retries
- **Request Timeout**: 1000-300000ms timeout
- **Follow Redirects**: Enable/disable redirect following

## Usage Examples

### Simple Data Source Query

```json
{
  "environment": "production",
  "dataSourceId": "12345",
  "bodyInputMethod": "form",
  "bodyParameters": {
    "parameter": [
      {
        "key": "startDate",
        "value": "2024-01-01",
        "dataType": "date",
        "format": "YYYY-MM-DD"
      },
      {
        "key": "limit",
        "value": "100",
        "dataType": "number"
      }
    ]
  }
}
```

### Complex JSON Query

```json
{
  "environment": "test",
  "coloName": "mycompany",
  "dataSourceId": "67890",
  "bodyInputMethod": "json",
  "jsonBody": {
    "filters": {
      "dateRange": {
        "start": "2024-01-01",
        "end": "2024-12-31"
      },
      "departments": ["manufacturing", "quality"]
    },
    "groupBy": ["department", "shift"],
    "metrics": ["count", "average"]
  }
}
```

## Response Format

The node returns a structured response:

```json
{
  "statusCode": 200,
  "headers": {
    "content-type": "application/json",
    "content-length": "1234"
  },
  "body": {
    // Plex API response data
  },
  "requestUrl": "https://cloud.plex.com/api/datasources/12345/execute?format=2",
  "executionTime": 1500
}
```

## Error Handling

The node provides comprehensive error handling:

- **Connection Errors**: Network connectivity issues
- **Authentication Errors**: Invalid credentials
- **API Errors**: Plex-specific error responses
- **Timeout Errors**: Request timeout exceeded
- **Validation Errors**: Invalid parameters

### Retry Logic

When retry is enabled:
- Exponential backoff between attempts
- Configurable max attempts (1-10)
- Configurable wait time (100-30000ms)

## Troubleshooting

### Common Issues

#### Authentication Failed
- Verify your credentials are correct
- Test the credential connection
- Check if your account has API access

#### Timeout Errors
- Increase the timeout setting
- Check network connectivity
- Verify the data source exists

#### Invalid Data Source ID
- Ensure the ID is numeric
- Verify the data source exists in your Plex environment
- Check environment (production vs test)

#### Invalid JSON Body
- Validate your JSON syntax
- Use the form-based input for simpler parameters
- Check for special characters or encoding issues

### Debug Mode

Enable debug mode in n8n to see detailed request/response information:

1. Set `N8N_LOG_LEVEL=debug` in your environment
2. Check n8n logs for detailed HTTP request information
3. Verify the generated URL is correct

## Development

### Requirements

- Node.js 18+
- pnpm 7+
- TypeScript 5+

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/n8n-nodes-plex-datasource.git
cd n8n-nodes-plex-datasource

# Install dependencies
pnpm install

# Development build with watch
pnpm run dev

# Production build
pnpm run build

# Run tests
pnpm test

# Lint code
pnpm run lint

# Format code
pnpm run format
```

### Project Structure

```
├── credentials/           # Credential type definitions
├── nodes/                # Node implementations
│   └── PlexDataSource/   # Main node
├── icons/                # Node icons
├── test/                 # Test files
├── dist/                 # Compiled output
└── docs/                 # Additional documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run `pnpm run lint` and `pnpm test`
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

- 📖 [Documentation](./docs/)
- 🐛 [Issues](https://github.com/your-username/n8n-nodes-plex-datasource/issues)
- 💬 [Discussions](https://github.com/your-username/n8n-nodes-plex-datasource/discussions)
- 📧 [Email Support](mailto:support@example.com)

## Changelog

### Version 1.0.0

- Initial release
- Basic Auth support
- Multi-environment support (production/test)
- Cloud and on-premise deployment support
- Configurable retry mechanism
- Form-based and JSON body input
- Comprehensive error handling
- Data type conversion
- Null value filtering
