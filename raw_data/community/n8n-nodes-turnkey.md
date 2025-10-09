[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/bd76f121-1c8f-4f5d-9c65-1eac5d81b6af)

# n8n-nodes-turnkey

This is an n8n community node that lets you interact with Turnkey services in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Credentials](#credentials)
[Operations](#operations)
[Compatibility](#compatibility)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Credentials

The Turnkey node requires API key credentials:

- **API Public Key**: Your Turnkey API public key
- **API Private Key**: Your Turnkey API private key

## Operations

The Turnkey node supports the following operations:

### Sign Transaction
Sign a blockchain transaction using your Turnkey wallet.

### Create Wallet 
Create a new wallet in your Turnkey organization.

### Create Wallet Accounts
Create new accounts within an existing wallet.

### List Wallets
Get a list of all wallets in your organization.

## Example Usage

To use the Turnkey node:

1. Add your API credentials
2. Select an operation (e.g. Sign Transaction)
3. Configure the required parameters:
   - Organization ID
   - Transaction type (Ethereum, Solana, or Tron)
   - Unsigned transaction data

The node will execute the operation and return the results.

## Error Handling

The node includes comprehensive error handling and will return clear error messages if:
- Invalid credentials are provided
- Required parameters are missing
- The API request fails
