# nele.ai n8n community node

This is an n8n community node that lets you use [nele.ai](https://www.nele.ai) AI tools, chat completions, image generators, and knowledge database operations in your n8n workflows.

[nele.ai](https://www.nele.ai) provides a unified API for a variety of AI models and tools, including chat, image generation, audio transcription, and document collection search.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following operations:

- **Chat**: Generate text responses via conversational AI models.
- **Image**: Generate and retrieve images based on text prompts.
- **Audio**: Transcribe audio files to text.
- **Knowledge Database**: Search and manage your knowledge databases (document collections).
- **Model**: List available AI models.

## Credentials

You need a nele.ai API key use this node.

1. Sign up at [nele.ai](https://www.nele.ai) and obtain your API key.
2. In n8n, add new credentials for "nele.ai API" and enter your API key.

For more details, see the [nele.ai manual](https://www.nele.ai/en/functions/information-for-users/program-settings/api-key).

## Compatibility

- Requires n8n version 1.109.1 or higher.
- Requires node.js version 22.19.0 or higher.

## Usage

After installing the node and configuring your credentials, you can add the "nele.ai" node to your workflows and select the desired resource and operation.

- Use **Chat** for conversational AI.
- Use **Image** to generate images from prompts.
- Use **Audio** to transcribe audio files.
- Use **Knowledge Database** to search your document collections.

Refer to the in-app parameter descriptions for guidance on each operation.

## Resources

- [nele.ai homepage](https://www.nele.ai)
- [nele.ai manual](https://www.nele.ai/en/functions)
- [nele.ai API documentation](https://api.aieva.io/docs)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
