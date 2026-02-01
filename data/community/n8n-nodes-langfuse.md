# @bitovi/n8n-nodes-langfuse

This is an n8n community node. It lets you use Langfuse in your n8n workflows.

Langfuse is an open source LLM engineering platform that provides observability, metrics, evals, prompt management and a playground to debug and improve your LLM application.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

- Make sure to allow community nodes with `N8N_COMMUNITY_PACKAGES_ENABLED=true`
- Once logged in to your N8N web UI, go to `/settings/community-nodes` and type `@bitovi/n8n-nodes-langfuse`

## Operations

The Langfuse node supports the following operation:

- **Log To Langfuse**: Logs LLM input and output data to Langfuse for observability and analytics

## Credentials

No credential required to access this node's functionality

## Compatibility

- **Tested with**: n8n versions 1.104+

## Usage

The Langfuse node is designed to be used in workflows that involve LLM (Large Language Model) interactions. It helps you track and analyze your AI model usage by logging input prompts and generated outputs.

### Basic workflow:
1. Set up your LLM interaction (e.g., using OpenAI, Anthropic, or other AI nodes)
2. Add the Langfuse node after your LLM node
3. Configure the node with:
   - **LLM Input**: The prompt or input sent to your LLM
   - **LLM Output**: The response received from your LLM
4. The node will automatically create traces and spans in Langfuse for observability

### Example use cases:
- Monitor AI chatbot conversations
- Track prompt performance across different models
- Analyze LLM usage patterns and costs
- Debug and improve AI workflow performance
- A/B test different prompts and models

The node automatically creates:
- **Traces**: High-level workflow execution records
- **Spans**: Detailed LLM inference records with input/output data
- **Metadata**: Including workflow name and execution context

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Langfuse documentation](https://langfuse.com/docs)
* [Langfuse GitHub repository](https://github.com/langfuse/langfuse)

## Need help or have questions?

Need guidance on leveraging AI agents or N8N for your business? Our [AI Agents workshop](https://hubs.ly/Q02X-9Qq0) will equip you with the knowledge and tools necessary to implement successful and valuable agentic workflows.

## License

[MIT](./LICENSE.md)
