



# n8n-nodes-imagerouter

This is an n8n community node. It lets you use [ImageRouter.io](https://imagerouter.io) in your n8n workflows.

[ImageRouter.io](https://imagerouter.io) is a platform for generating images and videos using AI. [n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[What AI models are available?](#what-ai-models-are-available)  
[Resources](#resources)  
[Development](#development)  

## Installation

The package is published on [NPM](
https://www.npmjs.com/package/n8n-nodes-imagerouter), so it's pretty easy to install in n8n.

1. Open `Settings`: <img width="498" height="223" alt="Screenshot_20250815_154224" src="https://github.com/user-attachments/assets/3c4b8293-81c2-421c-acec-ee018f6d919d" />
2. Go to `Community Nodes`: <img width="1010" height="741" alt="Screenshot_20250815_154251" src="https://github.com/user-attachments/assets/90c3732b-41d7-4130-8eef-1a0d09dd22eb" />
3. Install a new community node. Enter `n8n-nodes-imagerouter`: <img width="1010" height="741" alt="Screenshot_20250815_154304" src="https://github.com/user-attachments/assets/782095a7-e3c2-4fa9-991e-82c9fe9c1d89" />

For CLI install, follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **Image**
  - Text to Image
  - Image to Image
- **Video**
  - Text to Video
  - Image to Video
- **Models**
  - Get All Models

## Credentials

1. Sign up for [ImageRouter](https://imagerouter.io)
2. Go to https://imagerouter.io/api-keys and create an API key.

## Usage

<img width="841" height="545" alt="Screenshot_20250815_153907" src="https://github.com/user-attachments/assets/2fb5711d-14fb-4af0-8afb-0b3a4375501a" />
<img width="1393" height="935" alt="Screenshot_20250815_153957" src="https://github.com/user-attachments/assets/2e736fcc-b6e4-42cb-a006-29e651b02f8a" />
<img width="478" height="594" alt="Screenshot_20250815_153821" src="https://github.com/user-attachments/assets/4ef5bee7-69cf-4da4-9902-cb8eeb32c8d1" />

## What AI models are available?

More than 80+ image and video model, see the full list here: https://imagerouter.io/models

or download as JSON: https://api.imagerouter.io/v1/models

## Resources

* [ImageRouter.io](https://imagerouter.io)
* [ImageRouter.io API documentation](https://docs.imagerouter.io)
* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)

## Development

Build the image and start a local n8n instance with the ImageRouter node already available:

```bash
# From the repository root
npm run build
docker compose up --build
```

Open http://localhost:5678 in your browser and search for **ImageRouter** in the node panel to start using the node.

Publish to NPM:

```bash
npm publish
```