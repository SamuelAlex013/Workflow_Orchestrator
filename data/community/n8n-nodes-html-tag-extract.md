# n8n-nodes-html-tag-extract

This is an n8n community node. It lets you use extract common HTML tags from an HTML string in your n8n workflows.

This is my first community node for n8n, I've also included a JSON parse helper node that I use in my workflows. 
I find it useful to have a node that can parse JSON strings and return the parsed object, 
because repeating the same custom code node for all my workflows is a bit cumbersome.

HTML Tag Extract, provides helper nodes to extract HTML tags, parse JSON... and that's basically it.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Usage](#usage)  
[Acknowledgements](#acknowledgements)  
[Further (future) development](#further-future-development)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

* Extract HTML Tags
* Parse JSON

## Usage

### Extract HTML Tags
* Pass a string containing HTML to the Extract HTML Tags node, and it will return the data object containing the tags name and the tag's content.
* Some tags will be an array of objects, for example, the heading tags (h1, h2, h3, h4, h5, h6) will be an array of objects, each object containing the tag's name and content.
* There is also a word and character count for the text content of the page.

### Parse JSON
* Pass a string containing JSON to the Parse JSON node, and it will return the parsed object.
* Sometimes LLM output contains a JSON string within a code block: \```json {"key": "value"} ``` and this node will remove the junk and return the parsed object.

## Acknowledgements

* [Cheerio provides the HTML Tag Extract node](https://www.npmjs.com/package/cheerio)
* N8N team for the great platform and documentation
* Aider, mainly for commit messages

## Further (future) development

I'm planning to add more features to this node, such as allowing for extracting specific tags and CSS selectors.

Also:
* Parse YouTube iframes / links and extract the video ID
* Extract images with alt text (currently only extracts the image URL)
* Find all articles
* List internal and external links separately
* Implement better cleanup methods for the text content
* Maybe include Markdown as an output format, but there's already a community node for [HTML to Markdown conversion](https://www.npmjs.com/package/n8n-nodes-turndown-html-to-markdown)
