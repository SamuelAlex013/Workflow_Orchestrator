# n8n-nodes-tavily

This is an n8n community node. It lets you use Tavily in your n8n workflows.

Designed exclusively for AI agents, Tavily is a search engine providing real-time, accurate results and advanced research features.

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

Quick Installation

  1.  Go to Settings > Community Nodes
  2. Select Install
  3. Enter n8n-nodes-tavily in Enter npm package name
  4. Agree to the risks of using community nodes
  5. Select Install

Install and Usage video on [YouTube](https://www.youtube.com/watch?v=Yf2hNwPOVaU)

## Operations

### Search

  - Search Tavily with using a String query like  "How can I create a n8n custom nodes"
  - For more details on the options head over to [Tavily Search Docs](https://docs.tavily.com/api-reference/endpoint/search)

### Extract
- Extract will call Tavily to scrape and summarize the URLs you passed.
- For more details on the options head over to [Tavily Extract Docs](https://docs.tavily.com/api-reference/endpoint/extract)

## Credentials

Head to Tavily's [login](https://tavily.com/). It should take you straight to create an API Key.

## Compatibility

This node has been tested on version 1.77.3.

## Usage

Install and Usage video on [YouTube](https://www.youtube.com/watch?v=Yf2hNwPOVaU)

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [tavily documentation](https://docs.tavily.com/welcome) 
* [tavily search](https://docs.tavily.com/api-reference/endpoint/search)
* [tavily extract](https://docs.tavily.com/api-reference/endpoint/extract)

## Version history

v0.1.5 - Updated README.md
v0.1.4 - Updated README.md and fixed issue with Extract operation and multiple URLs

