# n8n-nodes-serpstat

This is an n8n community node. It lets you use Serpstat in your n8n workflows.

[Serpstat](https://serpstat.com/) is AI-based SEO platform used for competitive intelligence, keyword and backlinks research, tracking keyword rankings, SEO audits, and managing SEO tasks.

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

[Domain competitors](https://api-docs.serpstat.com/docs/serpstat-public-api/qzd94b49vdkyb-get-organic-competitors-page)

## Credentials

You need a Serpstat API token to use this node. You can test Serpstat API with a [free trial](https://serpstat.com/page/free-trial/). 
Consider purchasing Serpstat [subscription plans](https://serpstat.com/pay/) to increase data volume.
For heavy API usage, we offer special API plans. [Contact us](https://data.serpstat.com/#contact-us) for the details.
After you get access to the Serpstat API, create a new token in your [user profile](https://serpstat.com/users/profile/).

## Compatibility

Compatible with n8n version 1.105.3 or higher.

## Usage

Each user can have only one API token. There are no sandboxes, test endpoints, or any other test environment.
During the testing phase, limit the data size by using the Page and Size optional fields. This way, you can test your workflows without burning all API credits. 
If you are not familiar with n8n, check [quickstart guides](https://docs.n8n.io/try-it-out/).

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Serpstat API documentation](https://api-docs.serpstat.com/docs/serpstat-public-api/jenasqbwtxdlr-introduction-to-serpstat-api)

## Version history

0.1.0 - added domain competitors data collection.

