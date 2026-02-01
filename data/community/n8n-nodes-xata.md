# n8n-nodes-xata

This is an n8n community node. It lets you use Xata in your n8n workflows.

Xata is a serverless database with built-in powerful search and analytics.

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

* Append a record to a table
* Create a record by ID
* Create or Update a record in a table by ID
* Delete a recoord from a table
* List records from a table
* Read a record from a table
* Update a record in a table

## Credentials

You will need to create an API key

## Compatibility

Tested against n8n@0.214.2

## Usage

if using the filter functionalities, avoid using the full dictionary as in the Xata code snippet. For example to filter records from a table containing the word "TECH" in the product_name column insert the following string in the filter parameter: {'product_name':{'$contains':'TECH'}}

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Xata docs](https://xata.io/docs/overview)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

## Version history

* 0.2.1 Added create record by id
* 0.1.3 Added upsert
