# n8n-nodes-sambanova

This is an n8n community node. It lets you use **SambaNova Language Models** in your n8n workflows.

SambaNova provides advanced AI language models for natural language understanding and generation, enabling you to integrate state-of-the-art AI capabilities into your automation workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Connect to SambaNova's API to select and run language models.
- Fetch available models dynamically.
- Configure token limits and temperature for completions.
- Output a language model object to be used in AI chains or agents.

## Credentials

You need to provide an API key from SambaNova to use this node.

1. Sign up or log in to [SambaNova Cloud](https://cloud.sambanova.ai/?utm_source=continue&utm_medium=external&utm_campaign=cloud_signup).
2. Obtain your API key from the SambaNova dashboard.
3. In n8n, create new credentials of type **SambaNova**.
4. Enter your API key into the credentials form.

## Compatibility

- Minimum n8n version: 1.98.1 
- Tested on: n8n version 1.101.1
- Requires Node.js version >=20.15

## Usage

- Add the **SambaNova Chat Model** node to your workflow.
- Select your desired language model.
- Adjust options such as maximum tokens and temperature.
- Connect this node's output to AI chains or other compatible nodes.

If you're new to n8n, check out the [Try it out](https://docs.n8n.io/try-it-out/) guide to get started.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [SambaNova Cloud Documentation](https://docs.sambanova.ai/cloud/)

## Version history

- 0.1.0 - Initial release with support for basic SambaNova chat models.
