# n8n-nodes-shipentegra

<!-- Shields -->
![Build Status](https://img.shields.io/github/actions/workflow/status/se-public-repos/n8n-nodes-shipentegra/ci.yml?branch=main)
![npm Version](https://img.shields.io/npm/v/n8n-nodes-shipentegra)
![License](https://img.shields.io/github/license/se-public-repos/n8n-nodes-shipentegra)
![Coverage](https://img.shields.io/codecov/c/github/se-public-repos/n8n-nodes-shipentegra)
![Downloads](https://img.shields.io/npm/dt/n8n-nodes-shipentegra)
![Issues](https://img.shields.io/github/issues/se-public-repos/n8n-nodes-shipentegra)
![Last Commit](https://img.shields.io/github/last-commit/se-public-repos/n8n-nodes-shipentegra)

This is an n8n community node. It lets you use Shipentegra in your n8n workflows.

Shipentegra is a shipping and logistics platform that enables seamless integration for managing shipping rates, creating orders, generating shipping labels, tracking cargo activities, and more via its public API.

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

This node supports the following operations:

- **Calculate Price**: Calculate shipping price for a package.
- **Create Manual Order**: Create a manual order with detailed package and address information.
- **Create Post Orders**: Create one or more post orders by providing order IDs.
- **Create SE-DHL Ecommerce Label**: Generate DHL ecommerce shipping labels.
- **Create SE-Fedex Label**: Generate FedEx shipping labels.
- **Create SE-UPS Label**: Generate UPS shipping labels.
- **Create SE-USPS Label**: Generate USPS shipping labels.
- **Create Shipentegra Label**: Generate Shipentegra shipping labels.
- **Find Cargo Activities**: Track cargo activities by shipment number.
- **Find Order**: Retrieve detailed information about a specific order.
- **Find Orders**: Retrieve a list of orders associated with the user.
- **List Carriers**: List available carriers for the user.
- **Update Order Status**: Update the status of an order.

## Credentials

To use this node, you need to authenticate with Shipentegra:

1. Sign up for a Shipentegra account at [shipentegra.com](https://shipentegra.com).
2. Obtain your **Client ID** and **Client Secret** from your Shipentegra dashboard.
3. In n8n, add new credentials for "Shipentegra API" and enter your Client ID and Client Secret.
4. The node will automatically fetch and use an access token for API requests.

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with Node.js**: >=20.15
- **API Base URL**: `https://publicapi.shipentegra.com/v1`
- No known incompatibility issues at this time.

## Usage

- Add the Shipentegra node to your workflow.
- Select the desired operation.
- Fill in the required fields (e.g., package details, address, carrier).
- Connect your Shipentegra API credentials.
- Execute the workflow to interact with Shipentegra services.

For more details on each operation and field, refer to the [Shipentegra API documentation](https://docs.shipentegra.com).

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Shipentegra API documentation](https://docs.shipentegra.com)

## Version history

- **1.0.0**: Initial release with support for all major Shipentegra API operations.
