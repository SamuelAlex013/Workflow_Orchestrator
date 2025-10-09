# n8n-nodes-opnsense-gateway-status

This is an n8n community node. It lets you use OPNSense gateway monitoring in your n8n workflows.

OPNSense is an open-source firewall and routing platform. This node integrates with OPNSense API to fetch gateway statuses and trigger workflows on status changes.

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

- Fetch gateway statuses from OPNSense router via API.
- Trigger workflows when gateway status changes.
- Handle connection timeouts as gateway down.

## Credentials

This node requires OPNSense API credentials. You need to generate an API key and secret on your OPNSense router and configure them in n8n credentials for this node.

## Compatibility

Minimum n8n version: 0.241.0  
Tested with n8n Docker latest image (2025-09).  

## Usage

1. Add the OPNSense Gateway Status node to your workflow.
2. Fill in the Router IP field with your OPNSense router address (including protocol).
3. Select or enter your OPNSense API credentials.
4. Select the gateway to monitor from the dropdown.
5. The node will trigger when the gateway status changes, outputting the old and new status.

For new users, refer to the n8n [Try it out](https://docs.n8n.io/try-it-out/) documentation to learn the basics of n8n workflows.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)  
* [OPNSense API documentation](https://docs.opnsense.org/development/how-tos/api.html)  
* [n8n node starter template](https://github.com/n8n-io/n8n-nodes-starter)

## Version history

- 1.0.0 - Initial release supporting OPNSense gateway monitoring and status change triggering.
