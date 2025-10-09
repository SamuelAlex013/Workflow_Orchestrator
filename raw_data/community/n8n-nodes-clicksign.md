# n8n-nodes-clicksign

This is an n8n community node. It lets you use Clisign API in your n8n workflows.

Clicksign is a Brazilian electronic signature platform that provides legally valid document signing capabilities with features like automation, WhatsApp integration, and AI-powered document processing. It offers a comprehensive API for creating documents, managing signers, and automating contract workflows while ensuring compliance with Brazilian legislation for document integrity, authenticity, and non-repudiation.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following Clicksign operations:

- **List Envelopes**: Retrieve all envelopes from your Clicksign account
- **List Documents in Envelope**: Get all documents within a specific envelope
- **Create Envelope**: Create a new envelope for document signing

## Credentials

To use this node, you need to create a Clicksign API credential. You can do this in the n8n credentials panel.

### Prerequisites

1. Create a Clicksign account at [clicksign.com](https://www.clicksign.com/)
2. Generate an API access token from your Clicksign dashboard

### Authentication Setup

1. In n8n, go to **Settings** → **Credentials**
2. Click **Add Credential** and select **Clicksign API**
3. Enter your **Access Token** from your Clicksign account
4. Select the appropriate **Environment**:
   - **Sandbox**: For testing and development
   - **Production**: For live applications
5. Click **Save** to store your credentials securely

For detailed instructions on obtaining your API access token, visit the [Clicksign API documentation](https://developers.clicksign.com/docs/primeiros-passos).

## Compatibility

- **Node.js**: Requires Node.js version 20.15 or higher
- **n8n**: Compatible with n8n versions that support community nodes
- **n8n Nodes API Version**: 1

This node is built using the n8n community node framework and should work with any n8n installation that supports community nodes. The node uses the latest n8n workflow API and follows current best practices for community node development.

## Usage

This node allows you to integrate Clicksign electronic signature workflows into your n8n automations. Here are some common use cases:

### Basic Workflow Examples

#### 1. Automated envelope Creation
- Use the **Create Envelope** operation to generate new envelopes
- Set up automatic reminders and deadlines for signers
- Configure custom messages and subjects for your documents

**Related Documentation:**
- [Envelope Overview](https://developers.clicksign.com/docs/envelope)
- [Create Envelope API Reference](https://developers.clicksign.com/reference/api-criar-envelope)
- [Envelope Fields and Business Rules](https://developers.clicksign.com/reference/envelope-campos-e-regras-de-negocio)

#### 2. Envelope Tracking
- Use **List Envelopes** to check your created envelopes
- Check the status of pending signatures
- Track completion rates and deadlines

#### 3. Document Management
- Use **List Documents in Envelope** to retrieve all documents within a specific envelope
- Process signed documents for further automation
- Extract metadata from completed signatures

### Best Practices

#### Environment Setup
- **Sandbox Environment**: Always test your workflows in the Sandbox environment before moving to Production
- **Production Environment**: Use for live applications and real document signing

#### Error Handling
- Use n8n's error handling nodes to manage API failures gracefully
- Implement retry logic for transient failures
- Monitor workflow execution for any authentication or permission issues

#### Data Management
- The node returns structured JSON data that can be easily mapped to other nodes
- Use n8n's data transformation nodes to format responses for your specific needs
- Store sensitive data securely using n8n's credential management

### Getting Started

For beginners, check out the [n8n Try it out](https://docs.n8n.io/try-it-out/) documentation to learn the basics of workflow automation.

## Resources

### n8n Documentation
* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [n8n workflow automation guide](https://docs.n8n.io/try-it-out/)
* [n8n credentials management](https://docs.n8n.io/integrations/credentials/)

### Clicksign Documentation
* [Clicksign API Documentation](https://developers.clicksign.com/)
* [Getting Started with Clicksign API](https://developers.clicksign.com/docs/primeiros-passos)

### Support & Community
* [n8n Community Forum](https://community.n8n.io/)
* [n8n GitHub Discussions](https://github.com/n8n-io/n8n/discussions)
* [Clicksign repository](https://github.com/clicksign/n8n-nodes-clicksign)
