![image](https://raw.githubusercontent.com/Knowledge-Solutions/n8n-nodes-qontext/refs/heads/main/banner.png)

# n8n-nodes-qontext

This is an n8n community node. It lets you use Qontext in your n8n workflows.

[Qontext](https://www.qontext.ai/) is an LLM memory solution which gathers your company data and makes it AI-ready.

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

### Ingestion
- **Ingest Unstructured Text**: This operation allows you to send plain text or markdown to be ingested into a specified Qontext Knowledge Graph.
- **Ingest Website Data**: This operation crawls a website from a given URL and ingests the data into a Knowledge Graph.

### Retrieval
- **Get Context**: This operation retrieves relevant context from a Knowledge Graph based on a natural language prompt.

## Credentials
To use the Qontext API, you'll need an API key. This key is required for all requests and is included as an `X-API-Key` header. You can get your API key by signing up for an account on the Qontext website.

This authentication method ensures that your requests are secure and correctly associated with your workspace.

## Compatibility

This node is available for n8n versions >=2.220.0

## Usage
This node is designed to simplify interactions with the Qontext API by handling the ingestion and retrieval of data. While the core functionality is straightforward, there are a few things to keep in mind to ensure a smooth workflow.

**Using `workspaceId` and `knowledgeGraphId`**

Both the ingestion and retrieval operations require a workspaceId and a knowledgeGraphId. These IDs are fundamental to directing your data to the correct location within Qontext. You must obtain these IDs from your Qontext account dashboard before using the node. Make sure to use the correct IDs for the specific workspace and knowledge graph you want to interact with.

**Choosing the Right Retrieval Operation**:

The retrieval section offers two operations: **Get Context** and **Get Answer**.

**Get Context**: Use this operation when you want to retrieve the raw, relevant data from your knowledge graph. The response will provide the data that informed the answer. This is useful for building custom applications or performing further analysis on the retrieved information.

**Get Answer**: Use this operation when you simply want a direct, summarized answer to your prompt. The response will be a concise summary based on the retrieved context. This is ideal for generating quick, human-readable outputs or feeding answers directly into other systems.

For most use cases, **Get Answer** will be the most straightforward. However, if you need the underlying data for more complex workflows, **Get Context** is the better choice.

### Resources
For more detailed information and advanced use cases, refer to the official documentation.

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes): Learn more about community-created nodes and how they work within n8n.
* [Qontext API Documentation](https://docs.qontext.ai/): This is the official API documentation for the Qontext service. It provides comprehensive details on all available endpoints, parameters, and response formats.

### Version History
This is the initial version of the Qontext node, supporting core ingestion and retrieval operations. It's designed for seamless integration with the Qontext API. Future versions may introduce additional features and endpoints as they become available. We recommend keeping your n8n instance up-to-date to access the latest features and improvements.


