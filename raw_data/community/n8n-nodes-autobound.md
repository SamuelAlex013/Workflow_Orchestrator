# n8n-nodes-autobound

<img src="https://github.com/jasonhowie/n8n-nodes-autobound/raw/main/nodes/Autobound/autobound-logo.svg" alt="Autobound Logo" width="300" />

An n8n community node for Autobound's AI-powered sales content generation and insights API.

[![npm version](https://badge.fury.io/js/n8n-nodes-autobound.svg)](https://www.npmjs.com/package/n8n-nodes-autobound)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **AI-Powered Content Generation**: Create personalized emails, LinkedIn messages, and cold call scripts
- **Insights Retrieval**: Access detailed prospect and company insights
- **Multi-Language Support**: Generate content in 10+ languages
- **Advanced Personalization**: Leverage 350+ insight types for hyper-targeted content
- **Email Sequences**: Generate multi-step email campaigns
- **Content Rewriting**: Improve existing content with AI

## 📦 Installation

### Prerequisites

- An [Autobound](https://autobound.ai) API key

### Self-hosted n8n

In a self-hosted n8n instance, you can install community nodes directly:

1. Navigate to **Settings** → **Community Nodes**
2. Click **Install**
3. Enter `n8n-nodes-autobound` and click **Install**
4. The node will be available immediately

Alternatively, you can install via npm:

```bash
# Install globally for global n8n installations
npm install -g n8n-nodes-autobound

# Or install locally in your n8n project
npm install n8n-nodes-autobound
```

After npm installation, restart your n8n instance to load the new node.

### n8n Cloud

For n8n cloud users:

1. Go to **Settings** → **Community Nodes**
2. Click **Install**
3. Enter `n8n-nodes-autobound` and click **Install**
4. The node will be installed automatically

> **Note**: Community nodes are available on n8n cloud for Pro and Enterprise plans.

## 🔧 Configuration

1. **Add Credentials**:
   - In n8n, go to **Settings → Credentials**
   - Click **Add Credential**
   - Search for "Autobound API"
   - Enter your Autobound API key

2. **Get Your API Key**:
   - Sign up at [Autobound](https://autobound.ai)
   - Navigate to Settings → API Keys
   - Generate a new API key

## 🎯 Usage

### Content Generation

The Autobound node supports three types of content generation:

#### 1. Email Generation

```json
{
	"resource": "content",
	"operation": "generateEmail",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"additionalContext": "Prospect showed interest in cybersecurity solutions",
	"tone": "professional",
	"writingStyle": "consultative",
	"wordCount": 150
}
```

#### 2. LinkedIn Messages

```json
{
	"resource": "content",
	"operation": "generateLinkedIn",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"messageType": "connection_request",
	"tone": "friendly",
	"wordCount": 100
}
```

#### 3. Cold Call Scripts

```json
{
	"resource": "content",
	"operation": "generateColdCall",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"callDuration": "60_seconds",
	"tone": "professional"
}
```

### Insights Retrieval (v1.4)

Get detailed insights about prospects and companies:

```json
{
	"resource": "insights",
	"contactEmail": "prospect@company.com",
	"insightSubtype": "companyMarketTrends, financialEarningsCall"
}
```

## 🔥 Advanced Features

### Email Sequences

Generate multi-step email campaigns:

```json
{
	"resource": "content",
	"operation": "generateEmail",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"sequenceNumberOfEmails": 3,
	"writingStyle": "challenger_sale"
}
```

### Content Rewriting

Improve existing content:

```json
{
	"resource": "content",
	"operation": "generateEmail",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"contentToRewrite": "Your existing email content here..."
}
```

### Multiple Variations

Generate multiple content variations:

```json
{
	"resource": "content",
	"operation": "generateEmail",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"n": 3
}
```

### Insight Control

Fine-tune which insights to include or exclude:

```json
{
	"resource": "content",
	"operation": "generateEmail",
	"contactEmail": "prospect@company.com",
	"userEmail": "you@company.com",
	"enabledInsights": "companyMarketTrends, newsEvents, jobOpenings",
	"disabledInsights": "personalInterests, schoolMascot"
}
```

## 📋 Available Parameters

### Required Fields

- `contactEmail` or `contactLinkedinUrl`: Prospect identifier
- `userEmail` or `userLinkedinUrl`: Seller identifier (for content generation)

### Optional Fields

- `additionalContext`: Custom context or intent signals
- `tone`: Content tone (professional, casual, friendly, etc.)
- `language`: Content language (10+ supported)
- `wordCount`: Target word count
- `n`: Number of variations to generate
- `enabledInsights`: Comma-separated insight types to include
- `disabledInsights`: Comma-separated insight types to exclude
- `valueProposition`: Your company's value proposition
- `salesAsset`: Sales collateral to reference

## 🎨 Writing Styles (Email)

- **Challenger Sale**: Challenge prospect's thinking with insights
- **Consultative**: Advisory approach with expert positioning
- **CXO Pitch**: Direct, strategic communication for executives
- **Data-Driven**: Focus on metrics and ROI
- **Problem-Solver**: Identify and solve specific challenges
- **Storyteller**: Use narratives and case studies
- **Value-Based**: Emphasize business value and outcomes

## 🌍 Supported Languages

- English, Spanish, French, German, Italian
- Portuguese, Dutch, Russian, Chinese, Japanese

## 💡 Example Workflows

### Lead Qualification + Content Generation

1. **HTTP Request** → Get prospect data from CRM
2. **Autobound** → Generate personalized email
3. **Send Email** → Deliver via your email service
4. **CRM Update** → Log the outreach

### Multi-Channel Outreach

1. **Autobound** → Generate email content
2. **Autobound** → Generate LinkedIn message
3. **Autobound** → Generate call script
4. **Parallel execution** → Send via multiple channels

### Content A/B Testing

1. **Autobound** → Generate 3 email variations (`n: 3`)
2. **Function** → Randomly select version
3. **Send Email** → Deliver selected variation
4. **Track** → Monitor response rates

## 🔧 Troubleshooting

### Common Issues

1. **Node not appearing**: Restart n8n after installation
2. **Credential errors**: Verify API key in Autobound dashboard
3. **Rate limits**: Implement delays between requests
4. **Large responses**: Consider using pagination for insights

### Debug Mode

Enable debug logging to see request/response details:

```json
{
	"debug": true
}
```

## 📊 API Limits

- **Rate Limits**: Respect Autobound's API rate limits
- **Content Length**: Max 500 words for generated content
- **Variations**: Max 5 variations per request
- **Sequences**: Max 10 emails per sequence

## 🤝 Contributing

This is a community node. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Autobound Website](https://autobound.ai)
- [Autobound API Documentation](https://autobound-api.readme.io/)
- [n8n Documentation](https://docs.n8n.io/)
- [Community Nodes Guide](https://docs.n8n.io/integrations/community-nodes/)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/jasonhowie/n8n-nodes-autobound/issues)
- **Autobound Help Center**: [https://help.autobound.ai/en](https://help.autobound.ai/en)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io/)

## 📋 Changelog

### v2.3.2 (Latest)

- **Fixed**: Email sequences now properly parse and return individual emails as separate items
  - When generating an email sequence, each email is now returned as its own item with proper structure
  - Each item includes the email subject, body, and metadata (insights used, value props, etc.)
  - Items are numbered (1 of 3, 2 of 3, etc.) for easy identification

### v2.3.1

- Fixed credential test configuration
- Updated Insights API from v1.2 to v1.4
- Updated installation documentation for cloud users

### v2.2.1

- Fixed npm package logo display

### v2.0.0

- Renamed package from `n8n-node-autobound` to `n8n-nodes-autobound`
- Added Generate Insights API support (v1.2)
- Multi-resource node structure
- 350+ insight types support

---

Made with ❤️ by the n8n community and [Autobound](https://autobound.ai)
