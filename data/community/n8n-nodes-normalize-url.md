# n8n-nodes-normalize-url

This is an n8n community node. It lets you normalize URLs in your workflows.
Eseentially just a wrapper around [normalize-url](https://www.npmjs.com/package/normalize-url).

This custom node was generated almost entirely by a single V0.dev prompt:

> Write a custom n8n node that uses the normalize-url package from npm. The custom node needs to be able to take a URL as input, normalize it using the package, and then output it. Also expose all the parameters of the library so that I can toggle them from the custom n8n node.
> 
> Boolean options:
> 
> normalizeProtocol  
> forceHttp  
> forceHttps  
> stripAuthentication  
> stripHash  
> stripProtocol  
> stripTextFragment  
> stripWWW  
> removeQueryParameters  
> removeTrailingSlash  
> removeSingleSlash  
> removeDirectoryIndex  
> removeExplicitPort  
> sortQueryParameters

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Compatibility

Tested with n8n v1.62.4

## Version history

v0.1.0 (2024-12-22)
* Initial release
