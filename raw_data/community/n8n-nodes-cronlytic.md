# n8n-nodes-cronlytic

An n8n community node for integrating with [Cronlytic](https://cronlytic.com), providing advanced cron scheduling capabilities for n8n workflows through webhook triggers.

![n8n](https://img.shields.io/badge/n8n-community%20node-FF6D5A)
![npm](https://img.shields.io/npm/v/n8n-nodes-cronlytic)
![License](https://img.shields.io/npm/l/n8n-nodes-cronlytic)

## What is Cronlytic?

Cronlytic is an advanced cron scheduling service that provides:
- Robust, reliable cron job execution
- Detailed execution logs and monitoring
- Advanced scheduling features beyond basic cron
- API-based job management
- Webhook-based triggers for external systems

## Features

This n8n node provides:

- **Cronlytic Trigger**: Create scheduled workflows using Cronlytic's advanced cron scheduler
- **Webhook Integration**: Automatically sets up webhooks between Cronlytic and n8n
- **Advanced Scheduling**: Support for complex cron expressions
- **Automatic Job Management**: Creates, updates, and deletes Cronlytic jobs as needed
- **Custom Headers & Payloads**: Configure webhook requests with custom data

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install**
3. Enter `n8n-nodes-cronlytic`
4. Click **Install**

### Manual Installation

```bash
# In your n8n installation directory
npm install n8n-nodes-cronlytic

# Restart your n8n instance
```

## Setup

### 1. Get Cronlytic API Credentials

1. Sign up for a [Cronlytic account](https://cronlytic.com)
2. Navigate to **API Keys** in your dashboard
3. Click **Generate New API Key**
4. Copy your **API Key** and **User ID**

### 2. Configure Credentials in n8n

1. In n8n, go to **Credentials**
2. Click **Create New Credential**
3. Search for and select **Cronlytic API**
4. Enter your **API Key** and **User ID**
5. Test the connection and save

## Usage

### Cronlytic Trigger Node

The Cronlytic Trigger node creates scheduled jobs on Cronlytic that trigger your n8n workflows via webhooks.

#### Configuration Options:

- **Job Name**: Unique identifier for the cron job (alphanumeric, hyphens, underscores only)
- **Cron Expression**: 5-field cron expression (minute hour day month day-of-week)
- **Webhook Body**: Optional JSON payload to send with the webhook
- **Additional Headers**: Custom headers for webhook requests

#### Example Cron Expressions:

- `*/5 * * * *` - Every 5 minutes
- `0 9 * * 1-5` - 9 AM on weekdays
- `0 0 1 * *` - First day of every month
- `30 14 * * 0` - 2:30 PM every Sunday

### Example Workflow

1. Add a **Cronlytic Trigger** node to your workflow
2. Configure credentials
3. Set job name: `daily-report-generator`
4. Set cron expression: `0 9 * * *` (daily at 9 AM)
5. Add webhook body: `{"source": "cronlytic", "type": "daily_report"}`
6. Connect to your processing nodes
7. Activate the workflow

When activated, this creates a job on Cronlytic that will trigger your workflow daily at 9 AM.

## Advanced Features

### Custom Webhook Payloads

Include dynamic data in your webhook triggers:

```json
{
  "trigger_time": "{{timestamp}}",
  "source": "cronlytic",
  "workflow_id": "daily-backup",
  "environment": "production"
}
```

### Error Handling

The node includes built-in error handling:
- API connection retries with exponential backoff
- Automatic lambda warming for reliable execution
- Detailed error messages for troubleshooting

### Job Management

Jobs are automatically managed by n8n:
- **Created** when workflow is activated
- **Updated** when node configuration changes
- **Deleted** when workflow is deactivated or node is removed

## API Reference

This node uses the [Cronlytic Programmatic API](https://api.cronlytic.com/prog/). For advanced usage, refer to the complete API documentation.

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify API Key and User ID are correct
   - Check that credentials are properly configured in n8n

2. **Invalid Cron Expression**
   - Use 5-field format: `minute hour day month day-of-week`

3. **Webhook Not Triggering**
   - Ensure workflow is activated
   - Check Cronlytic dashboard for job status and logs
   - Verify webhook URL is accessible

4. **Job Limit Exceeded**
   - Check your Cronlytic plan limits
   - Delete unused jobs or upgrade your plan

### Support

- **Node Issues**: [GitHub Issues](https://github.com/Cronlytic/n8n-nodes-cronlytic)
- **Cronlytic API**: saleh@cronlytic.com
- **n8n Community**: [n8n Community Forum](https://community.n8n.io/)

## Development

### Requirements

- Node.js ≥ 20.15
- n8n development environment

### Setup

```bash
# Clone the repository
git clone https://github.com/Cronlytic/n8n-nodes-cronlytic.git
cd n8n-nodes-cronlytic

# Install dependencies
npm install

# Build the node
npm run build

# Link for local testing
npm link
n8n start
```

### Scripts

- `npm run build` - Build the node
- `npm run dev` - Build in watch mode
- `npm run lint` - Run linter
- `npm run format` - Format code

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run linting and formatting
6. Submit a pull request

## License

[MIT](LICENSE.md)

## Author

**Saleh Alsaihati**
- GitHub: [@Cronlytic](https://github.com/Cronlytic/n8n-nodes-cronlytic)
- Email: saleh@cronlytic.com

---

*Built with ❤️ for the n8n community*
