# n8n-nodes-fashn

This is an n8n community node. It lets you use [FASHN AI](https://fashn.ai/) that enables automated virtual try-on image generation in your n8n workflows.

FASHN AI helps you create virtual try-on images by combining model and garment photos, while automating workflows like product photography, e-commerce catalogs, and marketing campaigns.

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

## Operations

- Generate a virtual try-on

## Credentials

- You need an API Key for this integration to work
- You can get an API Key by signing up on [FASHN AI](https://fashn.ai/)
- Once you sign up, choose between one-time credit packs or a monthly subscription
- You can then head to Developer API > API Keys > Create new API Key to get your API Key
- You can use that API Key in the "API Key" field in the n8n Integration

## Compatibility

- Works on n8n > 1.00
- Created on n8n v1.107.4

## Usage

You can refer to [FASHN AI API Docs](https://docs.fashn.ai/) to refer to the APIs and their usage along with definitions, examples etc.

## Resources

* [FASHN AI API Docs](https://docs.fashn.ai/)

## Version history

#### 0.1.1

- Remove fashn sdk external dependency and use the API directly (Dependencies are not allowed in n8n community plugins)

#### 0.1.0

- Initial release
- Actions for generating virtual try-on
