# n8n-nodes-verifi-email

![Verifi.Email Logo](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

A powerful n8n node for seamless email validation using the [Verifi.Email](https://verifi.email) API. Validate email addresses with enterprise-grade accuracy while maintaining complete privacy and security.

## Features

- **Seamless Integration** - Easy-to-use n8n node for email validation workflows
- **High Accuracy** - Enterprise-grade email validation with detailed results
- **Privacy-First** - Secure and private API that doesn't store your data
- **Real-time Validation** - Instant email verification results
- **Bulk Processing** - Validate multiple emails efficiently in n8n workflows
- **Detailed Responses** - Comprehensive validation data including deliverability, syntax, and more

## Installation

### Install via n8n Community Nodes

1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Click **Install a Community Node**
3. Enter: `n8n-nodes-verifi-email`
4. Click **Install**

### Manual Installation

```bash
# In your n8n installation directory
npm install n8n-nodes-verifi-email
```

## Setup

### 1. Get Your API Key

1. Visit [Verifi.Email Registration](https://app.verifi.email/register)
2. Create your free account
3. Get your API key from the dashboard

### 2. Configure Credentials

1. In n8n, go to **Credentials**
2. Click **Add Credential** → **Verifi.Email API**
3. Enter your API key
4. Save the credential

## Usage

### Basic Email Validation

1. Add the **Verifi.Email** node to your workflow
2. Select your configured credentials
3. Choose operation: **Validate Email**
4. Enter the email address to validate
5. Execute the workflow

### Example Workflow

```json
{
  "email": "test@example.com",
  "validation_result": {
    "is_valid": true,
    "is_deliverable": true,
    "is_risky": false,
    "syntax_valid": true,
    "domain_exists": true,
    "mailbox_exists": true,
    "disposable": false,
    "role_account": false,
    "free_provider": false
  }
}
```

### Bulk Validation

Use n8n's **Split In Batches** node to process multiple emails:

1. **Read Data** → Email list
2. **Split In Batches** → Process in chunks
3. **Verifi.Email** → Validate each email
4. **Merge** → Combine results

## Node Operations

### Validate Email
Validates a single email address and returns comprehensive results.

**Parameters:**
- `email` (string, required): Email address to validate

**Output:**
- `is_valid` (boolean): Overall validation result
- `is_deliverable` (boolean): Whether email can receive messages
- `is_risky` (boolean): Risk assessment for the email
- `syntax_valid` (boolean): Email syntax validation
- `domain_exists` (boolean): Domain existence check
- `mailbox_exists` (boolean): Mailbox existence verification
- `disposable` (boolean): Whether it's a disposable email
- `role_account` (boolean): Whether it's a role-based email
- `free_provider` (boolean): Whether it's from a free email provider

## API Documentation

For detailed API documentation and advanced features, visit: [https://verifi.email/docs](https://verifi.email/docs)

## Use Cases

- **Lead Validation** - Clean your lead lists before marketing campaigns
- **User Registration** - Validate emails during sign-up processes
- **Data Cleaning** - Remove invalid emails from existing databases
- **Email Marketing** - Improve deliverability by validating subscriber lists
- **Form Validation** - Real-time email validation in web forms
- **CRM Integration** - Validate contacts automatically in your CRM workflows

## Example Workflows

### Marketing List Cleanup
```
Google Sheets → Split In Batches → Verifi.Email → Filter Valid → Update Sheet
```

### Real-time Form Validation
```
Webhook → Verifi.Email → Conditional Logic → Send Response
```

### CRM Contact Validation
```
CRM Trigger → Verifi.Email → Update Contact Status → Slack Notification
```

## Error Handling

The node includes comprehensive error handling for:
- Invalid API keys
- Rate limit exceeded
- Malformed email addresses
- Network connectivity issues
- API service unavailable

## Rate Limits

Please refer to your [Verifi.Email dashboard](https://app.verifi.email) for current rate limits and usage statistics.

## Support

- **Documentation**: [https://verifi.email/docs](https://verifi.email/docs)
- **Website**: [https://verifi.email](https://verifi.email)
- **Issues**: Report issues on this GitHub repository
- **API Support**: Contact us on **support@verifi.email**

## Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

### Development Setup

1. Clone this repository
2. Install dependencies: `npm install`
3. Build the node: `npm run build`
4. Link to your n8n installation: `npm link`
5. In your n8n directory: `npm link n8n-nodes-verifi-email`

### Testing

```bash
npm run test
npm run lint
```

## Changelog

### v1.0.0
- Initial release
- Email validation functionality
- Comprehensive validation results
- Error handling and rate limiting

## License

[MIT](LICENSE.md)

---

**Secure • Private • Accurate**

Transform your email workflows with reliable validation powered by Verifi.Email and n8n automation.