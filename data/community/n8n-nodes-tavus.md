# n8n-nodes-tavus

This n8n community node enables seamless integration of **[Tavus](https://tavus.io) in your [n8n](https://n8n.io) workflows**. Tavus is a platform for creating AI-driven digital replicas and generating personalized videos.

## Features

- Create and manage AI replicas for digital twin video generation
- Generate and retrieve videos using your replicas with custom scripts
- Manage conversations, personas, and speech synthesis for advanced AI workflows
- Create, list, and retrieve lipsync videos by synchronizing video and audio
- Full support for Tavus API resources:
  - **Video**: create, get, list
  - **Replica**: create, get, list
  - **Conversation**: create, get, list, delete, end
  - **Speech**: create, get, list
  - **Persona**: create, get, list
  - **Lipsync**: create, get, list

## Prerequisites

- You need a Tavus account and API key
- Videos for replica training must meet specific requirements:
  - 1-2 minutes in length (1.5-2 minutes is optimal)
  - .mp4 format encoded with h.264
  - Minimum frame rate of 25fps
  - Include the required consent statement
  - Less than 750MB in size

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-tavus
```

## Usage

1. Add your Tavus API credentials in n8n (API Key and Domain, e.g. `https://tavusapi.com/v2`)
2. Use the Tavus node in your workflows to:
   - Create and manage AI replicas
   - Generate and retrieve videos
   - Manage conversations and personas
   - Synthesize speech with your replicas
   - Create and manage lipsync videos by providing video and audio URLs
   - Retrieve information about all supported Tavus resources

## Supported Operations

| Resource     | Operations                                 |
|--------------|--------------------------------------------|
| Video        | Create, Get, List                          |
| Replica      | Create, Get, List                          |
| Conversation | Create, Get, List, Delete, End             |
| Speech       | Create, Get, List                          |
| Persona      | Create, Get, List                          |
| Lipsync      | Create, Get, List                          |

## Resources

- [Tavus API Documentation](https://docs.tavus.io/api-reference/introduction)
- [Tavus Phoenix Replica Model](https://docs.tavus.io/api-reference/phoenix-replica-model/create-replica)

## Compatibility

n8n version 1.80.0 and above

## License

[MIT](https://github.com/lvalics/n8n-nodes-tavus/blob/master/LICENSE.md)
