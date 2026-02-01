![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# <img src="nodes/Tulip/tulip.svg"  height="40"> n8n-nodes-tulip

This is an n8n community node. It lets you use [Tulip](https://tulip.co) in your n8n workflows.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Use `n8n-nodes-tulip` in n8n settings to install the stable version.

## Operations

* Table
  * List all tables
  * Create a table
  * Look up a table
  * Update a table
  * List records
  * Create a records
  * Delete all records
  * Count records
  * Look up a record
  * Update a record
  * Delete a record
  * Increment or decrement a field in a Tulip Table record
* Machine
  * Set machine attribute value
  * List all machines

## Credentials

Tulip nodes uses Tulip API with basic authentication. You can find how to setup API authentication from the [Tulip](https://support.tulip.co/docs/setting-up-a-tulip-api) website.

- **Name**: Display name for the node instance in the editor.
- **Factory URL**: For example, `your-factory-instance.tulip.co`
- **API Key**: The API key for the API token. Should start with `apikey.2_`.
- **API Secret**: The API secret for the API token.

## Compatibility

n8n-nodes-tulip is tested against the `r319.1` Tulip version and the `1.92.2` n8n version.

## Usage

### Tulip Machine Attribute Node

#### Prerequisites
Before using a `machine` node, make sure that you have completed the following steps:

1. Have machine monitoring enabled on your factory instance. This is required to use the Machine Attributes API.

2. Follow the steps in [this support article](https://support.tulip.co/en/articles/5007794-how-to-use-the-machine-attributes-api) to:

  - Configure an API token with `attributes:write` permissions
  - Create a machine that uses the Tulip API as a datasource
  - Define machine attributes for the machine

#### Node Configuration

- **Name**: Display name for the node instance in the editor
- **Tulip Api Authentication**: A configuration node with authentication details for an API token on your Tulip account. The API token must have `attributes:write` permissions. See more details in the [Tulip API Auth Node](#tulip-api-auth-node) section.

### Tulip Tables Node

#### Overview

The Tulip Tables API node supports sending data to and reading data from Tulip Tables, as well as reading Tulip Table metadata, using the Tulip Tables API.

Each `tables` node is configured to send data to a single Tulip Tables API endpoint. On an input message, the node will send the configured request and output the HTTP response along with any returned data. The **Query Type** field determines the type of request, relevant parameters, and the response data type. See the Tulip Tables API documentation at `your-factory-instance.tulip.co/apiDocs` for more information on the different types of requests.

#### Node Configuration

- **Name**: Display name for the node instance in the editor
- **Tulip Api Authentication**: A configuration node with authentication details for an API token on your Tulip account. The API token must have `tables:read` and `tables:write` permissions for read and write operations respectively. See more details in the [Tulip API Auth Node](#tulip-api-auth-node) section.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Tulip API documentation](https://support.tulip.co/docs/setting-up-a-tulip-api)
