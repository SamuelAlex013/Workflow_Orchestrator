# n8n-nodes-hedera

This is an n8n community node that enables seamless integration with the Hedera network in your n8n workflows.

Hedera is a decentralized public network that enables individuals and businesses to create powerful decentralized applications (dApps). It is designed to be a fast, fair, and secure platform for the decentralized economy. 

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following Hedera operations:

- **Create Account**: Create a new Hedera account with optional initial HBAR balance
  - Generates new ED25519 key pair
  - Returns new account ID and keys
- **Transfer HBAR**: Send HBAR to another account
  - Specify recipient account ID
  - Set transfer amount in HBAR
  - Returns transaction status and ID

### Transaction Operations
- **Sign Transaction**: Sign a transaction payload
  - Accepts base64-encoded transaction
  - Returns signed transaction in base64 format

## Credentials

To use this node, you'll need:
1. A Hedera account (a Testnet account can be created on [Hedera Portal](https://portal.hedera.com/))
2. Your account ID (in format 0.0.x)
3. Your private key (ED25519 or SECP256K1)
4. Choose the appropriate network (Mainnet, Testnet, or Previewnet)

## Compatibility

- Minimum n8n version: (no idea)
- Tested with n8n version: 1.91.3

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Hedera Documentation](https://docs.hedera.com/)
* [Hedera Portal](https://portal.hedera.com/)
* [Hedera SDK](https://docs.hedera.com/hedera/sdks-and-apis)




