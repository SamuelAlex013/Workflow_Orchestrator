# n8n-nodes-connect-secure

This is an n8n community node for Connect Secure. It provides access to the Connect Secure API, allowing you to integrate Connect Secure services with your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Resources](#resources)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

* **Auth**
  * Authorize with Connect Secure
* **Company**
  * Get all companies
  * Get a specific company
  * Create a company
  * Update a company
  * Delete a company
  * Get company statistics
* **Agent**
  * Get all agents
  * Get a specific agent
* **Credentials**
  * Get all credentials
  * Get a specific credential
  * Create a credential
  * Update a credential
  * Delete a credential
* **Discovery Settings**
  * Get all discovery settings
  * Get a specific discovery setting
  * Create a discovery setting
  * Update a discovery setting
  * Delete a discovery setting
* **Asset**
  * Get all assets
  * Get a specific asset
  * Create an asset
  * Update an asset
  * Delete an asset
  * Get asset statistics
* **Asset Data**
  * Get asset firewall policy
  * Get asset installed drivers
  * Get asset interfaces
  * Get asset ports
  * Get asset security report data
  * Get asset shares
  * Get asset storages

## Credentials

To use the Connect Secure node, you need to create credentials with the following information:
* **Tenant**: Your Connect Secure tenant name
* **Client ID**: Your Connect Secure client ID
* **Client Secret**: Your Connect Secure client secret
* **Base URL**: The base URL of your Connect Secure API (e.g., https://api.connect-secure.com)

## Compatibility

This node has been tested with n8n version 0.214.0.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Connect Secure API documentation](https://connect-secure.com/docs) (replace with the actual URL)
