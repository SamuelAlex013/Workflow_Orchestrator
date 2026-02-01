# n8n-nodes-nessus

This is an n8n community node for interacting with Tenable Nessus vulnerability scanners, bringing comprehensive vulnerability management capabilities to n8n workflows.

<div align="center">
  <img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" alt="n8n" width="200">
  <img src="https://raw.githubusercontent.com/arpit-patel1/n8n-nodes-nessus/refs/heads/master/nodes/Nessus/nessus-icon.svg" alt="Nessus Node" width="100">
</div>

## About

This node provides a comprehensive interface to Tenable Nessus vulnerability scanners within n8n, enabling security teams to automate vulnerability management workflows. Our goal is to make Nessus functionality seamlessly available in n8n, allowing users to integrate vulnerability scanning into their automation pipelines.

## Inspiration and Credits

This project is inspired by and references the excellent [pyTenable](https://github.com/tenable/pyTenable) Python library created by Tenable, Inc. The pyTenable library provides a pythonic interface into Tenable's platform APIs and serves as our primary reference for API interactions and functionality.

- **pyTenable Library**: https://github.com/tenable/pyTenable
- **pyTenable Documentation**: https://pytenable.readthedocs.io/
- **License**: MIT License (same as this project)

We've adapted the pyTenable library's approach and functionality to work within the n8n ecosystem, translating Python patterns to TypeScript and n8n's node architecture.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Supported Resources

### Scan Operations
- **List Scans**: Get all scans with optional filtering
- **Get Scan Details**: Retrieve detailed information about a specific scan
- **Create Scan**: Create new scans with policy and target configuration
- **Launch Scan**: Start configured scans
- **Stop Scan**: Halt running scans
- **Pause Scan**: Temporarily pause running scans
- **Resume Scan**: Resume paused scans
- **Delete Scan**: Remove scans from the system
- **Export Scan**: Download scan results in various formats (PDF, CSV, Nessus)
- **Copy Scan**: Duplicate existing scan configurations

### Policy Operations
- **List Policies**: Get all scan policies
- **Get Policy Details**: Retrieve detailed policy information
- **Create Policy**: Create new scan policies
- **Update Policy**: Modify existing policies
- **Delete Policy**: Remove policies
- **Copy Policy**: Duplicate existing policies

### Folder Operations
- **List Folders**: Get all scan folders
- **Create Folder**: Create new folders for organizing scans
- **Delete Folder**: Remove folders

### Plugin Operations
- **List Plugins**: Get available Nessus plugins
- **Get Plugin Details**: Retrieve detailed plugin information
- **List Plugin Families**: Get plugin families and categories

### Session Operations
- **Get Session Details**: Retrieve current session information
- **Logout**: End current session

## Credentials

This node requires Nessus API credentials. You can obtain these by:

1. Logging into your Nessus instance
2. Going to Settings > My Account > API Keys
3. Generating a new API key pair (Access Key and Secret Key)
4. Adding the credentials to your n8n credentials store

### Required Credential Fields
- **Nessus URL**: The base URL of your Nessus instance (e.g., https://your-nessus-server:8834)
- **Access Key**: Your Nessus API access key
- **Secret Key**: Your Nessus API secret key
- **Allow Self-Signed Certificates**: Enable if using self-signed certificates (optional)

## Configuration Examples

### List All Scans
- Resource: Scan
- Operation: List
- Additional Options: Configure pagination and filtering as needed

### Create and Launch a Scan
1. **Create Scan**:
   - Resource: Scan
   - Operation: Create
   - Policy: Select from available policies
   - Targets: Specify IP addresses or hostnames
   - Name: Give your scan a descriptive name

2. **Launch Scan**:
   - Resource: Scan
   - Operation: Launch
   - Scan ID: Use the ID from the created scan

### Export Scan Results
- Resource: Scan
- Operation: Export
- Scan ID: Specify the scan to export
- Format: Choose PDF, CSV, or Nessus format

## Advanced Features

- **Pagination Support**: Automatically handles large result sets
- **Retry Logic**: Built-in retry mechanism with exponential backoff
- **Input Validation**: Comprehensive parameter validation
- **Error Handling**: Detailed error messages with Nessus-specific error codes
- **Bulk Operations**: Support for managing multiple scans simultaneously

## Security Considerations

- Always use HTTPS when connecting to Nessus
- Store API credentials securely using n8n's credential management
- Regularly rotate API keys
- Use appropriate network security measures for Nessus communications

## Use Cases

- **Automated Vulnerability Scanning**: Schedule regular scans and process results
- **Incident Response**: Trigger scans based on security events
- **Compliance Reporting**: Generate and distribute compliance reports
- **Asset Management**: Track and organize scan targets
- **Integration with SIEM**: Send vulnerability data to security platforms
- **Notification Systems**: Alert teams about critical vulnerabilities

## Resources

- [Nessus API Documentation](https://docs.tenable.com/nessus/Content/NessusAPIReference.htm)
- [pyTenable Documentation](https://pytenable.readthedocs.io/)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Tenable Nessus](https://www.tenable.com/products/nessus)

## License

[MIT](LICENSE.md)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Disclaimer

This is an unofficial community node and is not affiliated with or endorsed by Tenable, Inc. Tenable and Nessus are trademarks of Tenable, Inc.
