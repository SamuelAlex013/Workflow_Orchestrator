# n8n-nodes-link-preview

This is an n8n community node for retrieving link previews with HTML sanitization and rich text support.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Link Preview

Retrieves preview information from a URL including:
- Title
- Description
- Favicons
- Images
- Videos

The node includes HTML sanitization to prevent XSS attacks while preserving rich text formatting.

#### Features
- URL normalization and validation
- HTML sanitization with DOMPurify
- Configurable timeout and redirect handling
- Rich text support with safe HTML tags
- Error handling and validation

#### Input Fields
- URL: The URL to get the preview from
- Timeout: Request timeout in milliseconds (default: 10000)
- Follow Redirects: Whether to follow redirects (default: true)

#### Output Fields
- title: The page title
- description: The page description
- favicons: Array of favicon URLs
- images: Array of image URLs
- videos: Array of video URLs
- siteName: The site name
- contentType: The content type
- mediaType: The media type

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [n8n Link Preview Node Documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkpreview/)

## Version history

### 1.0.0
- Initial release
- Basic link preview functionality
- HTML sanitization
- URL normalization
- Configurable options 