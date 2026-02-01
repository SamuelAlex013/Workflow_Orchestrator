# n8n-nodes-moorcheh

![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

This is an [n8n](https://n8n.io/) Official node interfacing with [Moorcheh](https://moorcheh.ai).

Moorcheh is a powerful vector store and AI platform that enables semantic search, document storage, and AI-powered question answering across your data.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Namespace Operations
- **[Create](https://console.moorcheh.ai/docs/create-namespace/api-call)**: Create a new namespace for storing documents or vectors
- **[List](https://console.moorcheh.ai/docs/list-namespaces/api-call)**: List all available namespaces
- **[Delete](https://console.moorcheh.ai/docs/delete-namespace/api-call)**: Delete a namespace and all its contents

### Document Operations
- **[Upload](https://console.moorcheh.ai/docs/upload-text-data/api-call)**: Upload documents to a namespace for semantic search
- **[Get](https://console.moorcheh.ai/docs/get-documents/api-call)**: Retrieve specific documents by their IDs
- **[Delete](https://console.moorcheh.ai/docs/delete-data/api-call)**: Delete documents from a namespace

### Vector Operations
- **[Upload](https://console.moorcheh.ai/docs/upload-vector-data/api-call)**: Upload vector embeddings to a namespace
- **[Delete](https://console.moorcheh.ai/docs/delete-data/api-call)**: Delete vectors from a namespace

### Search Operations
- **[Search](https://console.moorcheh.ai/docs/search/api-call)**: Perform semantic search across namespaces using text queries or vector embeddings

### Answer Operations
- **[Generate](https://console.moorcheh.ai/docs/gen-ai-answer/api-call)**: Generate AI-powered answers based on namespace content using various LLM models

## Credentials

To use this node, you need a Moorcheh API key:

1. Sign up for a Moorcheh account at [console.moorcheh.ai](https://console.moorcheh.ai)
2. Navigate to your API settings
3. Generate an API key
4. Use the API key in the Moorcheh credentials in n8n

## Compatibility

- **n8n version**: 1.0.0 or later
- **Node.js version**: 20.15 or later

## Usage

### Creating a Namespace
1. Select the "Namespace" resource
2. Choose "Create" operation
3. Enter a namespace name
4. Select the type (Text or Vector)
5. For vector namespaces, specify the vector dimension

### Uploading Documents
1. Select the "Document" resource
2. Choose "Upload" operation
3. Enter the namespace name
4. Add documents with ID, text content, and optional metadata

### Searching Content
1. Select the "Search" resource
2. Choose "Search" operation
3. Enter your query (text or comma-separated vector values)
4. Specify target namespaces
5. Set top_k and threshold parameters

### Generating AI Answers
1. Select the "Answer" resource
2. Choose "Generate" operation
3. Enter the namespace name
4. Provide your question
5. Select an AI model and configure parameters

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Moorcheh API Documentation](https://console.moorcheh.ai/docs)
* [Moorcheh Console](https://console.moorcheh.ai)
