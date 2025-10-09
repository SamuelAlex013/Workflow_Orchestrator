# n8n-nodes-scrapfly

This is an n8n community node. It lets you use ScrapFly in your n8n workflows. [n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[ScrapFly.io](https://scrapfly.io/) provides data collection APIs for web page scraping, screenshots, and AI data extraction at scale. Integrating ScrapFly within a workflow enables extracting web page sources, parsing for structured data, or taking screenshots as binary files.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation. See examples
from [Scrapfly documentation](https://scrapfly.io/docs/integration/n8n) to see usage.

## Operations
- __Scrape web page URLs__  
Scrapes the HTML source of a given web page URL with the support of headless browsers, proxies, and anti-bot bypass.
- __Extract Data From an HTML, Text, or Markdown Document Using AI__  
Automatically parse HTML, Text, or Markdown documents using pre-defined templates or LLM prompts to extract structured data.
- __Capture web page screenshot__  
Takes a screenshot of a web page as an image file given its URL.
- __Get account info__  
Get information about the current account subscription and its usage.

## Credentials

ScrapFly API key is used as a credential key. To get your API key, register for free.

## Usage

For example, regarding usage and predefined workflow templates, please look at [ScrapFly's n8n integration docs](https://scrapfly.io/docs/integration/n8n).

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [ScrapFly documentation](https://scrapfly.io/docs)

## Development 

To publish a new release, you need repo access and play command like `make bump-version VERSION=0.1.3`
