![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-workfloows

This is an n8n community node. It lets you use [Workfloows Platform APIs](https://docs.workfloo.ws/) in your n8n workflows.

Workfloows Platform APIs is **a collection of pre-built agents and tools** designed to power workflows for lead generation, marketing, business intelligence, research, OSINT, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Health

- **Ping** (`GET /ping`): Check if connection to Workfloows API is working. Returns `pong`. 
- **Usage** (`GET /usage`): Get usage data for the account.

### Jobs

- **Jobs** (`GET /jobs`): List active jobs and current limits status.
- **Job status** (`GET /jobs/{jobId}`): Get status of a job by providing job ID (UUID). Returns status (`pending`, `processing`, `completed` or `failed`) and results (if available).

### Tools

- **Scrape web** (`POST /scrape/web`): Scrape content from a web page. Returns scraped content as plain text, HTML, Markdown and links. Optional proxy available.
- **Company contacts** (`POST /companies/contacts`): Crawl a company website and get the contact information.
- **Similar companies** (`POST /companies/similar`): Find similar companies by the company website.
- **Similar companies (deep)** (`POST /companies/similar/deep`): Run deep search for company lookalikes (asynchronous). Returns job ID (UUID).

## Credentials

You need to have a valid API key and positive account balance to fully use the service. You can get your API key by signing up at [Workfloows](https://workfloo.ws/login) and generating new key in tab "Keys". 

For more details regarding authentication, please refer to [Workfloows API documentation](https://docs.workfloo.ws/api-reference/authentication).

## Compatibility

Tested on n8n version 1.108.1. 

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Workfloows Platform documentation](https://docs.workfloo.ws/)

## Version history

- 0.1.0 (2025-08-31): Initial release


