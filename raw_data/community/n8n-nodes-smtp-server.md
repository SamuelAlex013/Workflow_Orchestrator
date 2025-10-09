# n8n SMTP Server Node

A custom n8n node that starts an SMTP server and triggers workflows when emails are received. This node allows you to receive emails directly into your n8n workflows, enabling powerful email automation scenarios.

## Features

- 🚀 **SMTP Server**: Starts a lightweight SMTP server to receive emails
- 📧 **Email Parsing**: Automatically parses incoming emails with full metadata
- 🔐 **Authentication**: Optional SMTP authentication support
- 📎 **Attachment Support**: Handles email attachments with metadata
- 🔄 **Workflow Triggers**: Triggers n8n workflows with parsed email data
- 🛡️ **Security**: Configurable security options for production use

## Installation

### From npm (Recommended)

```bash
npm install n8n-nodes-smtp-server
```

### From Source

```bash
git clone https://github.com/alexrster/n8n-nodes-smtp-server.git
cd n8n-nodes-smtp-server
npm install
npm run build
```

## Usage

### Basic Setup

1. **Add the node to your n8n instance:**
   - If installed via npm: The node will appear automatically in the trigger nodes list
   - If built from source: Copy the `dist` folder to your n8n custom nodes directory

2. **Configure the SMTP Server:**
   - Set the port (default: 2525)
   - Set the host (default: 0.0.0.0)
   - Configure authentication if needed
   - Set security options

3. **Connect to your workflow:**
   - The node will trigger your workflow whenever an email is received
   - Email data is available in the workflow execution

### Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **Port** | Number | 2525 | Port to listen on for SMTP connections |
| **Host** | String | 0.0.0.0 | Host to bind the SMTP server to |
| **Enable Authentication** | Boolean | false | Whether to enable SMTP authentication |
| **Username** | String | - | Username for SMTP authentication |
| **Password** | String | - | Password for SMTP authentication |
| **Allow Insecure** | Boolean | true | Whether to allow insecure connections (no TLS) |

### Email Data Structure

When an email is received, the workflow is triggered with the following data structure:

```json
{
  "subject": "Email Subject",
  "to": "recipient@example.com",
  "from": "sender@example.com",
  "body": "Email body text",
  "html": "<html>Email HTML content</html>",
  "text": "Plain text email content",
  "date": "2024-01-15T10:30:00.000Z",
  "messageId": "<message-id@example.com>",
  "attachments": [
    {
      "filename": "document.pdf",
      "contentType": "application/pdf",
      "size": 1024
    }
  ],
  "headers": {
    "received": "...",
    "date": "...",
    "from": "...",
    "to": "...",
    "subject": "..."
  },
  "raw": "Raw email content"
}
```

## Use Cases

### 1. Email Support Automation
- Receive support emails and automatically create tickets
- Route emails to different teams based on content
- Auto-respond with confirmation messages

### 2. Form Submissions
- Receive form submissions via email
- Process and store form data
- Send confirmation emails

### 3. Email Monitoring
- Monitor specific email addresses for keywords
- Trigger alerts based on email content
- Archive important emails automatically

### 4. Integration Workflows
- Bridge email systems with other services
- Convert emails to tasks, events, or notifications
- Sync email data with databases or CRMs

## Example Workflows

### Basic Email Processing
```
SMTP Server → Email Parser → Database → Notification
```

### Support Ticket Creation
```
SMTP Server → Extract Email Data → Create Ticket → Send Confirmation
```

### Email Filtering
```
SMTP Server → Filter by Subject → Route to Different Teams → Archive
```

## Security Considerations

### Production Deployment

1. **Use Authentication**: Enable SMTP authentication in production
2. **Configure Firewall**: Only allow connections from trusted sources
3. **Use TLS**: Consider implementing TLS for encrypted connections
4. **Monitor Logs**: Keep an eye on server logs for suspicious activity
5. **Regular Updates**: Keep the node and dependencies updated

### Network Configuration

- **Internal Use**: Bind to localhost (127.0.0.1) for internal use only
- **External Access**: Use proper firewall rules when exposing to the internet
- **Port Selection**: Choose non-standard ports to avoid conflicts

## Development

### Prerequisites

- Node.js 20.x or higher
- npm or yarn
- n8n instance for testing

### Local Development

```bash
# Clone the repository
git clone https://github.com/alexrster/n8n-nodes-smtp-server.git
cd n8n-nodes-smtp-server

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint

# Format code
npm run format
```

### Testing

```bash
# Test the build
npm run build

# Test with n8n (requires n8n to be installed)
npm install -g n8n
npx n8n --help
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run linting and build
6. Submit a pull request

## Troubleshooting

### Common Issues

**Node not appearing in n8n:**
- Ensure the node is properly built (`npm run build`)
- Check that the `dist` folder is in the correct location
- Restart n8n after adding the node

**SMTP Server not starting:**
- Check if the port is already in use
- Verify firewall settings
- Ensure proper permissions

**Authentication issues:**
- Verify username and password are correct
- Check that authentication is enabled
- Test with a simple SMTP client

**Email parsing errors:**
- Check the email format
- Verify the email content is valid
- Review server logs for details

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Dependencies

This node uses external dependencies (`smtp-server` and `mailparser`) that are essential for its core functionality. These dependencies are:

- **Well-maintained** by the Nodemailer team
- **Widely used** in production environments
- **Security audited** with no known critical vulnerabilities
- **Industry standard** for SMTP and email parsing

For detailed information about these dependencies and why they are necessary, see [DEPENDENCIES.md](DEPENDENCIES.md).

## Support

- **Issues**: [GitHub Issues](https://github.com/alexrster/n8n-nodes-smtp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/alexrster/n8n-nodes-smtp-server/discussions)
- **Email**: a@qx.zone

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## Acknowledgments

- Built for the n8n community
- Uses [smtp-server](https://github.com/nodemailer/smtp-server) for SMTP functionality
- Uses [mailparser](https://github.com/nodemailer/mailparser) for email parsing
