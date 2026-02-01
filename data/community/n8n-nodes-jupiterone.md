# n8n-nodes-jupiterone

This is an n8n community node. It lets you use JupiterOne in your n8n workflows.

JupiterOne is a cloud-native security and compliance platform that enables you to query, visualize, and automate insights about your cloud resources and security posture.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **JupiterOne Query**: Run J1QL queries against your JupiterOne account with automatic LIMIT handling
- **JupiterOne Webhook**: Listen for JupiterOne rule alerts and security events

## Credentials

This node requires JupiterOne API credentials:
- **Account ID**: Your JupiterOne account ID
- **API Token**: Your JupiterOne API access token
- **API Base URL**: (Optional) The base URL for your JupiterOne instance (defaults to `https://api.us.jupiterone.io`)

To obtain your API token, log in to JupiterOne and generate an access token from your account settings.

## Compatibility

- Minimum n8n version: 1.0.0
- Tested with n8n 1.x and JupiterOne client 2.x

## Usage

### JupiterOne Query Node

1. Add the JupiterOne Query node to your workflow.
2. Create and select your JupiterOne credentials.
3. Enter your J1QL query (e.g., `FIND jupiterone_account`).
4. Set the limit for maximum results (optional, min: 1, max: 10,000, leave empty for all results).
5. Execute the workflow to retrieve results from JupiterOne.

**Note**: The LIMIT clause is automatically appended to your query. If your query already contains a LIMIT, it will be replaced with the specified limit value. If no limit is specified, any existing LIMIT clause will be removed to return all results.

### JupiterOne Webhook Node

1. Add the JupiterOne Webhook node to your workflow as a trigger.
2. Configure authentication (optional):
   - Select "Header Token" for authentication
   - Set a webhook secret and header name
3. Copy the webhook URL provided by n8n.
4. Configure your JupiterOne rule to send webhooks to this URL.
5. The node will automatically trigger when JupiterOne sends webhook events.

**Note**: The webhook node processes incoming webhook payloads and structures the data for use in downstream nodes. It supports both authenticated and unauthenticated webhooks.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [JupiterOne n8n documentation](https://docs.jupiterone.io/integrations/outbound-directory/n8n-community-node)
* [J1QL query language reference](https://docs.jupiterone.io/jupiterone-query-language/)

## Version history

- 0.1.6
  - Fixed Test Credential Logic, Added copilot-instructions.md

- 0.1.5
  - Removed Credential Test for J1 API

- 0.1.4
  - Added Credential Test for J1 API

- 0.1.3
  - Added JupiterOne Webhook node for receiving rule alerts and security events

- 0.1.2
  - Internal update - no customer impacting changes. 

- 0.1.1
  - Initial release: JupiterOne Query node for running J1QL queries
