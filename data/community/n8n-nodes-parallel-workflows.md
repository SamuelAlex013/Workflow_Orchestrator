# n8n-nodes-parallel-workflows

⚡ **Version 0.4.3** - Expression support with improved UI!

This is an n8n community node that lets you execute multiple webhook URLs in parallel, perfect for orchestrating complex workflow patterns and dramatically improving performance.

## Features

- 🚀 **True Parallel Execution**: Execute unlimited webhooks simultaneously  
- 🔗 **Simple Webhook URLs**: Just paste URLs, one per line
- 🎯 **Flexible Modes**: Simple mode or detailed manual configuration
- 💪 **Error Resilience**: Continue processing even if some webhooks fail
- 📊 **Multiple Aggregation Modes**: Array, object, merged, or individual items
- ⚡ **Performance Optimized**: Optional concurrency limits and retry logic
- 📈 **Execution Tracking**: Monitor progress with metadata and timing info

## Prerequisites

### Webhook Setup (Required)

Each workflow you want to execute in parallel must have a **Webhook trigger node**:

1. **Add a Webhook trigger** to each sub-workflow
2. **Activate the workflows** to generate webhook URLs  
3. **Copy the webhook URLs** (use production URLs for live execution)
4. **Paste the URLs** into the Parallel Workflow Orchestrator

## Installation

### Via n8n UI

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-parallel-workflows`
3. Click **Install**
4. The node is ready to use - no credentials needed!

### Manual Installation

```bash
# Navigate to your n8n custom nodes folder
cd ~/.n8n/custom

# Install the package
npm install n8n-nodes-parallel-workflows

# Restart n8n
```

## Usage

### Quick Start - Simple Mode

The easiest way to use the node:

1. **Add Webhook triggers** to your sub-workflows
2. **Activate** the sub-workflows to get webhook URLs
3. **Add Parallel Workflow Orchestrator** to your main workflow
4. **Paste webhook URLs** (one per line) in Simple mode
5. **Execute** - all webhooks run simultaneously!

Example webhook URLs:
```
https://your-n8n.com/webhook/abc-def-ghi
https://your-n8n.com/webhook/jkl-mno-pqr
https://your-n8n.com/webhook/stu-vwx-yz
```

### Manual Configuration Mode

For more control over each webhook:

1. Set **Execution Mode** to "Manual Configuration"
2. Click **Add Workflow** for each webhook
3. For each webhook configure:
   - **Webhook URL**: The full webhook URL
   - **Execution Name**: Optional friendly name for results
   - **Input Data**: Custom JSON data for this webhook
   - **Additional Settings**: Timeout and retry options

### Dynamic Mode - From Input Data

Pass webhook configurations through input data:

```json
{
  "workflows": [
    {
      "webhookUrl": "https://your-n8n.com/webhook/abc-123",
      "executionName": "Analysis Task",
      "inputData": {
        "prompt": "Analyze sales data",
        "region": "North America"
      },
      "timeout": 30,
      "retryCount": 2
    },
    {
      "webhookUrl": "https://your-n8n.com/webhook/def-456",
      "executionName": "Report Generation",
      "inputData": {
        "format": "PDF",
        "template": "executive"
      }
    }
  ]
}
```

## Real-World Use Cases

### 1. Multiple AI API Calls in Parallel

Perfect for calling multiple AI services simultaneously:

**Setup:**
1. Create workflows with Webhook triggers for each AI task
2. Paste all webhook URLs into Parallel Orchestrator
3. Execute - all AI calls happen simultaneously

**Time Savings Example:**
- Sequential: 6 workflows × 3 seconds each = 18 seconds
- Parallel: All 6 workflows = ~3 seconds total
- **6x faster!**

### 2. Batch Data Processing

Process different data sources simultaneously:
- Configure webhooks for CSV processor, API fetcher, and Database queries
- All data sources are processed in parallel
- Results automatically combined based on your aggregation setting

### 3. Multi-Service Health Checks

Check multiple services at once:
- Create webhook-triggered health check workflows
- Set Result Aggregation to "Object (Named)"
- Get instant status of all services

## Authentication (New in v0.4.0)

The node now supports authentication for secured webhook endpoints:

### Authentication Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **None** | No authentication | Public webhooks |
| **Header Auth** | Custom header with API key | Most REST APIs |
| **Bearer Token** | Authorization: Bearer token | OAuth2, JWT tokens |
| **Basic Auth** | Username and password | Legacy systems |

### Simple (Structured) Mode Features

#### Per-Webhook Authentication
Each webhook can have its own authentication settings:
1. Select authentication type for each webhook
2. Configure the required fields (token, username, etc.)
3. Different webhooks can use different authentication methods

#### Global Authentication
Use the same authentication for all webhooks:
1. Enable "Use Same Auth for All Webhooks"
2. Configure authentication once
3. All webhooks will use the same credentials

#### Dynamic Data with Expressions
Pass different data to each webhook using n8n expressions:
1. Use the "Additional Data" field for each webhook
2. Drag and drop fields from the input schema directly into the field
3. Use expressions like `{{ $json.objectKey }}` to reference input data
4. Enter JSON objects for multiple values: `{"key": "{{ $json.field }}", "custom": "value"}`
5. Additional data is merged with main input (overrides on conflict)

Example Additional Data:
- Single expression: `{{ $json.pdfKey }}`
- JSON with expressions: `{"documentId": "{{ $json.pdfKey }}", "timestamp": "{{ $now }}"}`
- Plain value: `custom-value-123`

### Example Configurations

**Header Authentication:**
- Authentication: Header Auth
- Header Name: `X-API-Key`
- Token/Key: `your-api-key-here`

**Bearer Token:**
- Authentication: Bearer Token
- Token/Key: `your-jwt-token-here`

**Basic Authentication:**
- Authentication: Basic Auth
- Username: `user@example.com`
- Password: `secure-password`

## Configuration Options

### Execution Modes

| Mode | Description | Best For |
|------|-------------|----------|
| **Simple** | Paste webhook URLs (one per line) | Quick parallel execution |
| **Manual** | Configure each webhook individually | Custom settings per webhook |
| **From Input** | Use webhook list from data | Dynamic/programmatic execution |

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| **Pass Input Data** | Boolean | true | Send input data to all webhooks |
| **Continue On Fail** | Boolean | true | Continue if a webhook fails |
| **Result Aggregation** | Select | array | How to combine results |

### Advanced Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| **Max Concurrent** | Number | 0 | Limit concurrent executions (0 = unlimited) |
| **Include Metadata** | Boolean | false | Add execution timing and status |
| **Global Timeout** | Number | 300 | Maximum seconds for all webhooks |

## Output Format Examples

### Array Aggregation (Default)
```json
{
  "results": [
    {
      "success": true,
      "webhookUrl": "https://your-n8n.com/webhook/abc-123",
      "name": "Webhook_1",
      "data": { /* webhook response */ }
    },
    {
      "success": true,
      "webhookUrl": "https://your-n8n.com/webhook/def-456",
      "name": "Webhook_2",
      "data": { /* webhook response */ }
    }
  ]
}
```

### Object Aggregation
```json
{
  "Webhook_1": {
    "success": true,
    "data": { /* webhook response */ }
  },
  "Webhook_2": {
    "success": true,
    "data": { /* webhook response */ }
  }
}
```

## Performance Tips

1. **Use Simple Mode** when all webhooks need the same input data
2. **Set Max Concurrent** if you have resource constraints
3. **Use appropriate timeouts** to prevent hanging executions
4. **Enable Continue on Fail** for non-critical webhooks
5. **Test webhook URLs** independently before adding to orchestrator

## Troubleshooting

### Common Issues

**Q: Webhooks aren't executing**
- Ensure sub-workflows are activated
- Check webhook URLs are correct (use production URLs)
- Verify webhooks are accessible from your n8n instance

**Q: Getting timeout errors**
- Increase timeout values in Additional Settings
- Check if sub-workflows are taking longer than expected
- Increase Global Timeout in Advanced options

**Q: Results are empty**
- Ensure webhook workflows have a Respond to Webhook node
- Check that webhooks are returning data properly

## Development

### Building from Source

```bash
npm run build        # Build the node
npm run dev         # Watch mode for development
npm run lint        # Check code style
npm run format      # Format code
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## License

MIT - See [LICENSE](LICENSE) file

## Support

- **Issues**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-parallel-workflows/issues)
- **Author**: Jez Dawes
- **Email**: jeremy@jezweb.net
- **Company**: [Jezweb](https://www.jezweb.com.au)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for full version history.

### Latest Version (0.4.3)
- Improved Additional Data field UI - clean single-line input
- Expression support with drag-and-drop from input schema  
- Supports both JSON objects and plain values
- Enhanced parsing for flexible data input

---

*Built with ❤️ for the n8n community*