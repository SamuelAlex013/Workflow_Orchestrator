# n8n-nodes-webmetic

This is an n8n community node that lets you use Webmetic in your n8n workflows.

[Webmetic](https://webmetic.de) provides company visitor tracking data for sales and marketing teams.

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

* **New Visits**
  * Get: Retrieve a list of companies that have visited a specified domain for the first time
* **Intensive Visits**
  * Get: Retrieve a list of companies that have had intensive visits to a specified domain
* **Returning Visits**
  * Get: Retrieve a list of companies that have visited a specified domain multiple times

## Credentials

To use this node, you need:

1. A Webmetic API key - Get yours from [Webmetic](https://webmetic.de)
2. Configure the API key in n8n's credentials

## Compatibility

* Requires n8n version 0.172.0 or later
* Tested with n8n version 1.0.0+

## Usage

1. Add the Webmetic node to your workflow
2. Create new Webmetic API credentials:
   - Enter your API key (starts with `wmtc_`)
3. Configure the node:
   - Select "New Visits", "Intensive Visits", or "Returning Visits" as the resource
   - Select "Get" as the operation
   - Enter the domain you want to track (e.g., `example.com`)
   - Optional: Configure additional fields for date filtering:
     - **From Date**: Start date or relative time period (default: "-30 days")
     - **To Date**: End date or "now" for current date (default: "now")
4. Execute the node to retrieve company visitor data

The node returns valuable sales intelligence about companies and their visiting behavior on your domain.

### Date Format Examples:
- **Relative times**: `-30 days`, `-12 hours`, `-45 minutes`, `-7 days`
- **Absolute dates**: `2023-01-01`, `2023-12-31`  
- **Current**: `now`
- **Minutes**: `-15 minutes`, `-30 minutes`, `-90 minutes`

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Webmetic API documentation](https://hub.webmetic.de/docs)