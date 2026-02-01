# n8n-nodes-softr

This is an n8n community node. It lets you use Softr in your n8n workflows.

Softr is a no-code platform that allows you to build web applications and websites. It provides a user-friendly interface for creating and managing applications without needing to write code.

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

### Softr Databases

Triggers

* `On New Record`: Triggered when a new record is created in a Softr database.
* `On Updated Record`: Triggered when an existing record in a Softr database is updated.

Actions:

* `Create Record`: Creates a new record in a specified Softr database.
* `Update Record`: Updates an existing record in a specified Softr database.
* `Delete Record`: Deletes a record from a specified Softr database.
* `Get Record`: Retrieves a specific record from a specified Softr database.
* `Get All Records`: Retrieves all records from a specified Softr database.
* `Search Records`: Searches for records in a specified Softr database based on a search query.

### Softr Application Users

* `Create Application User`: Creates a new user in a specified Softr application.
* `Delete Application User`: Deletes a user from a specified Softr application.

## Credentials

To use Softr, you must authenticate with your API Key. You can find your API Key in your [Softr account settings](https://studio.softr.io/user/apisettings).

More details on how to find your API Key can be found in the [Softr documentation](https://docs.softr.io/softr-api/tTFQ5vSAUozj5MsKixMH8C/api-setup-and-endpoints/j1PrTZxt7pv3iZCnZ5Fp19).

## Compatibility

Implemented and tested against n8n version 1.103.2.

## Usage

Softr node uses Softr Public API under the hood. You can find more information about the API in the [Softr API documentation](https://docs.softr.io/softr-api/tTFQ5vSAUozj5MsKixMH8C/softr-database-api/5aZs45abxPkQ4dURKFwRGF).

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Softr API documentation](https://docs.softr.io/softr-api/tTFQ5vSAUozj5MsKixMH8C/softr-database-api/5aZs45abxPkQ4dURKFwRGF)
