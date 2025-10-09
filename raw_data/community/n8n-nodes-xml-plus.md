# n8n-nodes-xml-plus

An alternative XML node based on fast-xml-parser as opposed to xml2js that's used in the built-in XML node. Designed for performance with larger datasets as well as adding additional customizability. 

I built this node after running into some limitations using the bundled XML node, specifically when I was working with Google's older Data APIs. Chunks of this code are based on the original XML node. It might be a little buggy but hopefully someone else finds it as useful as I did. 

This is an n8n community node. It lets you transform XML data with a high level of customizability in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

TL;DR: Open Settings within N8N > Community Nodes > Install > Enter: "n8n-nodes-xml-plus" into "npm Package Name"


## Operations

- Parse XML to JSON
- Build XML from JSON
- XML Validation
- Processing of XML, HTML, and DOCTYPE entities
- Escaping of special characters
- Manipulation of declaration in XML
- Parse numbers using strnum
- Supports unpaired tags and comments
- Preservation of XML tag order
- Rebuilding of XML after using an XML to JSON operation

## Compatibility

Tested on versions >1.78.0 but will probably work with older versions as well.

## Usage

Specify Input Property field that contains JSON or XML to be converted.

## Resources

Additional documentation on the options included in this node can be found on the fast-xml-parser GitHub page [here](https://github.com/NaturalIntelligence/fast-xml-parser/tree/master/docs/v4)

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)


## Version history

1.0.0 - Major overhaul of validation options as well as how the input and output fields function. Bumped fast-xml-parser dependency to v5.0.8

0.0.3 - Bug fix with how incoming JSON was processed.

0.0.2 - Added option to choose incoming JSON field.

0.0.1 - Initial release.

