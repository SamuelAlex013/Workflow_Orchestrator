# n8n-nodes-shlink

This is an n8n community node. It lets you use Shlink in your n8n workflows.

**What is Shlink?**  
Shlink is an open source, self-host application which allow you to create and track your short links.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

There is only one node in this package capable of interacting with below resources and respective operations:

- Short Links  
  - Create short url *(v0.0.1)*
  - List short urls *(v0.0.2)*
  - more options coming soon ...

## Credentials

Shlink uses api key based authentication in the header x-api-key for each request. You can generate the key as per the shlink documentation [here](https://shlink.io/documentation/api-docs/authentication/).

## Compatibility

This node is tested to run on a minimum version of n8n `v1.46.0`.

## Resources

* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Shlink API Documentation](https://shlink.io/documentation/api-docs/)


