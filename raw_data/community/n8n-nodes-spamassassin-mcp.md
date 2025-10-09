# n8n-nodes-spamassassin-mcp

An n8n community node that integrates with the [SpamAssassin MCP server](https://github.com/btafoya/spamassassin-mcp) to provide powerful email spam analysis capabilities within your n8n workflows.

[![Publish to npm](https://github.com/btafoya/spamassassin-mcp-n8n-community-node/actions/workflows/publish.yml/badge.svg)](https://github.com/btafoya/spamassassin-mcp-n8n-community-node/actions/workflows/publish.yml)
[![npm version](https://img.shields.io/npm/v/n8n-nodes-spamassassin-mcp.svg)](https://www.npmjs.com/package/n8n-nodes-spamassassin-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n](https://img.shields.io/badge/n8n-community%20node-blue)](https://n8n.io)
[![SpamAssassin](https://img.shields.io/badge/SpamAssassin-MCP-orange)](https://spamassassin.apache.org/)

## Features

This node provides four main operations for email security analysis:

### 🔍 Scan Email
- Analyze email content for spam probability
- Configurable analysis levels (Basic, Detailed, Full)
- Include/exclude header analysis
- Returns spam score, confidence, and triggered rules

### 🛡️ Check Reputation
- Check sender email reputation
- Verify IP address reputation (optional)
- Domain reputation analysis (optional)
- Blacklist checking across multiple sources

### 🧪 Test Rules
- Test custom SpamAssassin rules
- Validate rule syntax and effectiveness
- Score individual rule contributions
- Detailed test result breakdown

### 📊 Explain Score
- Detailed spam score breakdown
- Rule-by-rule explanation
- Categorized analysis
- Actionable recommendations

## Installation

### Prerequisites

1. **SpamAssassin MCP Server**: Install the SpamAssassin MCP server first:
   ```bash
   npm install -g @btafoya/spamassassin-mcp
   ```

2. **n8n**: This is a community node for n8n. You need n8n installed:
   ```bash
   npm install n8n -g
   ```

### Install the Community Node

1. **Via npm** (recommended):
   ```bash
   npm install n8n-nodes-spamassassin-mcp
   ```

2. **Via n8n Community Nodes UI**:
   - Go to Settings → Community Nodes
   - Click "Install a community node"
   - Enter: `n8n-nodes-spamassassin-mcp`
   - Click Install

3. **For Development**:
   ```bash
   git clone https://github.com/btafoya/spamassassin-mcp-n8n-community-node.git
   cd spamassassin-mcp-n8n-community-node
   npm install
   npm run build
   npm link
   cd ~/.n8n/nodes
   npm link n8n-nodes-spamassassin-mcp
   ```

## Configuration

### Credentials Setup

The node requires SpamAssassin MCP API credentials. You can connect in two ways:

#### 1. Command Line Connection (Recommended)
- **Connection Type**: Command Line
- **Command**: `npx @btafoya/spamassassin-mcp` (default)
- **Arguments**: Additional command line arguments (optional)
- **Timeout**: Connection timeout in seconds (default: 30)

#### 2. HTTP/SSE Connection
- **Connection Type**: HTTP/SSE
- **Base URL**: `http://localhost:3000` (default)
- **API Key**: Authentication key (if required)
- **Timeout**: Connection timeout in seconds (default: 30)

### Enable Community Node Tool Usage

If you want to use this node as a tool in n8n AI Agents, enable the community node tool usage:

```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
n8n start
```

Or in your `.env` file:
```env
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

## Usage Examples

### Basic Email Spam Scanning

1. Add the SpamAssassin MCP node to your workflow
2. Set operation to "Scan Email"
3. Provide email content in the "Email Content" field
4. Configure analysis level (Basic/Detailed/Full)
5. Execute the workflow

**Example Input**:
```
Subject: Amazing Deal - Limited Time Offer!
From: winner@suspicious-domain.com

Congratulations! You've won $1,000,000! 
Click here to claim your prize now!
```

**Example Output**:
```json
{
  "operation": "scan_email",
  "scanResult": {
    "is_spam": true,
    "spam_score": 15.2,
    "threshold": 5.0,
    "confidence": 0.95,
    "rules_triggered": [
      "LOTS_OF_MONEY",
      "SUSPICIOUS_DOMAIN",
      "URGENT_ACTION"
    ],
    "analysis_time_ms": 245,
    "headers_analyzed": true
  },
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### Reputation Checking

Perfect for validating sender trustworthiness:

1. Set operation to "Check Reputation"
2. Enter the email address to check
3. Optionally add IP address and domain
4. Execute to get reputation scores

### Custom Rule Testing

Test your own SpamAssassin rules:

1. Set operation to "Test Rules"
2. Enter your custom rules in "Rules Content"
3. Provide test email content
4. Get detailed test results and rule effectiveness

### Score Explanation

Understand why an email was marked as spam:

1. Set operation to "Explain Score"
2. Provide the email content
3. Enable detailed explanation if needed
4. Get rule-by-rule breakdown

## Workflow Integration

### Email Processing Pipeline

```
Email Trigger → SpamAssassin MCP (Scan) → Router → [Clean Email Path / Quarantine Path]
```

### Reputation-Based Filtering

```
New Contact → SpamAssassin MCP (Check Reputation) → Decision → [Allow / Block / Monitor]
```

### Rule Development Workflow

```
Rule Editor → SpamAssassin MCP (Test Rules) → Validation → [Deploy / Refine]
```

## Advanced Configuration

### Performance Tuning

- **Timeout**: Adjust based on your email size and analysis complexity
- **Analysis Level**: Use "Basic" for high-volume processing, "Full" for detailed analysis
- **Connection Type**: Command line is generally faster for local setups

### Security Considerations

- **Defensive Operations Only**: This node performs only defensive email analysis
- **No Email Storage**: Emails are not persistently stored by the MCP server
- **Rate Limiting**: The MCP server includes built-in rate limiting
- **Input Validation**: All inputs are validated before processing

### Docker Integration

If using n8n in Docker, ensure the SpamAssassin MCP server is accessible:

```yaml
version: '3'
services:
  n8n:
    image: n8nio/n8n
    environment:
      - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
    volumes:
      - ~/.n8n:/home/node/.n8n
    depends_on:
      - spamassassin-mcp

  spamassassin-mcp:
    image: btafoya/spamassassin-mcp
    ports:
      - "3000:3000"
```

## Error Handling

The node includes comprehensive error handling:

- **Connection Errors**: Automatic retry with exponential backoff
- **Timeout Handling**: Configurable timeouts with graceful degradation
- **Validation Errors**: Clear error messages for invalid inputs
- **Continue on Fail**: Optional continue-on-fail for batch processing

## Troubleshooting

### Common Issues

1. **"Connection Failed"**
   - Verify SpamAssassin MCP server is running
   - Check connection credentials
   - Ensure network connectivity

2. **"Command Not Found"**
   - Install SpamAssassin MCP server: `npm install -g @btafoya/spamassassin-mcp`
   - Verify PATH includes npm global binaries

3. **"Permission Denied"**
   - Check file permissions
   - Ensure n8n has access to execute commands

4. **"Timeout Error"**
   - Increase timeout in credentials
   - Check system resources
   - Reduce analysis complexity

### Debug Mode

Enable debug logging in credentials to get detailed connection information.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/btafoya/spamassassin-mcp-n8n-community-node.git
cd spamassassin-mcp-n8n-community-node
npm install
npm run build
npm run lint
npm test
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Related Projects

- [SpamAssassin MCP Server](https://github.com/btafoya/spamassassin-mcp) - The underlying MCP server
- [n8n](https://n8n.io/) - Workflow automation platform
- [Model Context Protocol](https://modelcontextprotocol.io/) - Protocol for AI-tool integration

## Support

- 📚 [Documentation](https://github.com/btafoya/spamassassin-mcp-n8n-community-node/docs)
- 🐛 [Bug Reports](https://github.com/btafoya/spamassassin-mcp-n8n-community-node/issues)
- 💬 [Discussions](https://github.com/btafoya/spamassassin-mcp-n8n-community-node/discussions)
- 📧 Email: btafoya@briantafoya.com