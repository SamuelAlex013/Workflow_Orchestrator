# n8n-nodes-pearch

[![npm version](https://img.shields.io/npm/v/n8n-nodes-pearch.svg)](https://www.npmjs.com/package/n8n-nodes-pearch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Community](https://img.shields.io/badge/n8n-Community%20Node-green.svg)](https://n8n.io)

A powerful n8n community node for integrating with the [Pearch AI](https://pearch.ai) recruitment platform. This node enables automated candidate search operations with intelligent result waiting and comprehensive search options.

## 🚀 Features

- **🔍 Smart Search**: Execute candidate searches with natural language queries
- **⏱️ Automatic Waiting**: Built-in result polling with configurable timeouts
- **🎯 Search Types**: Choose between Fast (quick results) and Pro (comprehensive analysis)
- **📊 Advanced Options**: Configure insights, freshness, contact details, and profile scoring
- **🔐 Secure Authentication**: Bearer token-based API security
- **⚡ Efficient**: Single node operation for complete search workflows

## 📋 Prerequisites

- [n8n](https://n8n.io) (self-hosted or cloud)
- [Pearch AI](https://pearch.ai) account with API access
- Node.js 20.15+ (for development)

## 🛠️ Installation

### For n8n Cloud Users

1. In your n8n workflow, click the **+** button to add a new node
2. Search for "Pearch" in the node library
3. Select the Pearch node and configure your credentials

### For Self-Hosted n8n

1. Install the package globally:
   ```bash
   npm install -g n8n-nodes-pearch
   ```

2. Restart your n8n instance

3. The Pearch node will be available in your node library

### Local Development

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/n8n-nodes-pearch.git
   cd n8n-nodes-pearch
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the project:
   ```bash
   npm run build
   ```

4. Link to your n8n installation:
   ```bash
   npm link
   npm link n8n-nodes-pearch
   ```

## 🔑 Setup

### 1. Create Pearch API Credentials

1. In n8n, go to **Settings** → **Credentials**
2. Click **Add Credential**
3. Search for "Pearch API" and select it
4. Fill in your credentials:
   - **Base URL**: `https://api.pearch.ai`
   - **API Key**: Your Pearch API key
5. Click **Save**

### 2. Add the Pearch Node

1. In your workflow, click the **+** button
2. Search for "Pearch" and select it
3. Connect your Pearch API credentials
4. Configure the search parameters

## 📖 Usage

### Basic Search

Configure the node with:
- **Query**: "senior python developer with Django experience"
- **Limit**: 25
- **Search Type**: Fast
- **Max Wait Time**: 300 seconds (5 minutes)

### Advanced Search

For comprehensive candidate analysis:
- **Query**: "data scientist with machine learning and AWS experience"
- **Limit**: 100
- **Search Type**: Pro
- **Insights**: ✅ Enabled
- **Profile Scoring**: ✅ Enabled
- **Show Emails**: ✅ Enabled
- **Max Wait Time**: 600 seconds (10 minutes)

### Search Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| **Query** | String | ✅ Yes | - | Search query (e.g., "python developer with Django") |
| **Limit** | Number | ❌ No | 50 | Max results (1-100) |
| **Search Type** | Options | ❌ No | Fast | Fast (quick) or Pro (comprehensive) |
| **Insights** | Boolean | ❌ No | false | Include AI-powered candidate insights |
| **High Freshness** | Boolean | ❌ No | false | Prioritize recently updated profiles |
| **Show Emails** | Boolean | ❌ No | false | Include candidate email addresses |
| **Show Phone Numbers** | Boolean | ❌ No | false | Include candidate phone numbers |
| **Profile Scoring** | Boolean | ❌ No | false | Include AI matching scores |
| **Max Wait Time** | Number | ❌ No | 300 | Max wait time in seconds (10-3600) |
| **Polling Interval** | Number | ❌ No | 5 | Status check interval in seconds (2-60) |

## 🔄 How It Works

1. **Submit Search**: Sends your query to Pearch API
2. **Get Task ID**: Receives a unique task identifier
3. **Poll Status**: Automatically checks completion status
4. **Wait for Results**: Continues until search is complete
5. **Return Data**: Provides final candidate results


## 🎯 Use Cases

### Recruitment Automation
- **Automated Candidate Sourcing**: Set up workflows to regularly search for specific skill sets
- **Lead Generation**: Automatically collect candidate contact information
- **Skill Gap Analysis**: Monitor available talent for specific technologies

### Integration Workflows
- **CRM Integration**: Add candidates directly to your recruitment CRM
- **Email Campaigns**: Automatically send outreach emails to qualified candidates
- **Data Analysis**: Export search results for further analysis

### Time-Saving Automation
- **Batch Processing**: Search multiple skill combinations in parallel
- **Scheduled Searches**: Run searches at optimal times
- **Result Filtering**: Process and filter results automatically

## 🚨 Error Handling

The node includes comprehensive error handling for:
- **Invalid Queries**: Empty or malformed search terms
- **Authentication Errors**: Invalid API keys or base URLs
- **API Failures**: Network issues or service unavailability
- **Timeout Errors**: Searches exceeding maximum wait time
- **Rate Limiting**: API usage limits and quotas

## 🔧 Configuration Tips

### Performance Optimization
- **Fast searches** typically complete within 1-2 minutes
- **Pro searches** may take 3-5 minutes for comprehensive results
- **Increase polling interval** for high-traffic periods
- **Use appropriate limits** - higher limits increase processing time

### Best Practices
- **Be specific** in your search queries for better results
- **Use Pro search** for critical hiring decisions
- **Enable insights** for AI-powered candidate analysis
- **Set reasonable timeouts** based on your search complexity

## 📚 API Reference

### Endpoints Used
- **POST** `/v2/search/submit` - Submit search request
- **GET** `/v2/search/status/{task_id}` - Check search status

### Authentication
Uses Bearer token authentication with your Pearch API key.

### Rate Limits
Respects Pearch API rate limits with configurable polling intervals.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## 🙏 Acknowledgments

- [n8n](https://n8n.io) for the amazing workflow automation platform
- [Pearch AI](https://pearch.ai) for providing the recruitment API
- The n8n community for support and feedback

## 📞 Support

- **Documentation**: [Pearch API Docs](https://apidocs.pearch.ai)
- **Issues**: [GitHub Issues](https://github.com/yourusername/n8n-nodes-pearch/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/n8n-nodes-pearch/discussions)
- **Email**: mz@pearch.ai

## 🔗 Links

- [n8n Community Nodes](https://n8n.io/integrations/)
- [Pearch AI Platform](https://pearch.ai)
- [n8n Documentation](https://docs.n8n.io)
- [npm Package](https://www.npmjs.com/package/n8n-nodes-pearch)

---

**Made with ❤️ by the Pearch AI team**
