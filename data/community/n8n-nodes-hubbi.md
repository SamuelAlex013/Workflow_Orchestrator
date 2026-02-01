# n8n-nodes-hubbi

This is an n8n community node. It lets you use Hubbi services in your n8n workflows.

Hubbi is a B2B marketplace platform that connects corporate consumers with auto parts suppliers. Using BigData technologies, it enables an agile and assertive quotation, purchase and sale process.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Vehicle Operations: get detailed information about a vehicle by it's license plate.
- Stock Operations: List, create, update and delete your stock at Hubbi.
- Part Operations: Get detailed technical speficiation for an autopart, search for parts in Hubbi's catalog and see the lowest quotation for auto parts.

## Credentials

To use this node, you need to have a Hubbi account and valid API keys.

1. **Create a Hubbi Account:**  
   Sign up at [Hubbi](https://hubbi.app) if you don't already have an account.

2. **Generate API Keys:**  
   After logging in, navigate to your account settings to generate your API keys.

3. **Configure Credentials in n8n:**  
   In n8n, add a new set of credentials for the Hubbi node and enter your API keys.

These credentials will allow the node to authenticate and interact with Hubbi services securely.

## Compatibility

This node is compatible with n8n version 1.93.0 and onwards.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Hubbi](https://hubbi.app)
