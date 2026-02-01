# n8n-nodes-elevenlabs-conversational

This n8n community node enables seamless integration of **[ElevenLabs](https://elevenlabs.io) voice AI technology in your [n8n](https://n8n.io) workflows**.

## Features

- Text-to-Speech conversion with ElevenLabs AI voices
- Voice customization and selection
- Support for conversational AI workflows
- Integration with ElevenLabs API for high-quality voice synthesis
- Manage ElevenLabs Conversational Agents (create, get, list)
- Access ElevenLabs Voice Library
- Handle Conversations (list, get, delete, feedback)
- Knowledge Base management:
  - Upload documents from files or URLs
  - List, retrieve, and delete knowledge base documents
  - Get document content and chunks
  - Compute RAG (Retrieval Augmented Generation) indexes
  - View agents dependent on specific documents
- Phone Number management:
  - Create phone numbers with Twilio or SIP Trunk
  - List, retrieve, and delete phone numbers
  - Assign phone numbers to agents
- Make outbound phone calls via Twilio integration
- Generate shareable links for your agents

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Configuration

You will need an ElevenLabs API key to use this node. You can obtain one by signing up at [ElevenLabs](https://elevenlabs.io).

The API key must be included in the credentials for this node.

## More information

ElevenLabs provides state-of-the-art AI voice technology that enables you to create lifelike voice content for various applications including:
- Conversational AI assistants
- Content creation
- Audiobooks
- Virtual narration
- Localization

This node allows you to harness these capabilities within your n8n workflows.

## Compatibility

1.80.0 and above

## License

[MIT](https://github.com/lvalics/n8n-nodes-elevenlabs-conversational/blob/master/LICENSE.md)
