<img src="images/voyage-ai.png" alt="Voyage AI Logo" width="100" align="right" />

# Embeddings Voyage AI (n8n node)

> ℹ️ Only supports `Text Embeddings`: https://docs.voyageai.com/docs/embeddings

This node integrates [Voyage AI](https://www.voyageai.com/) with [n8n](https://n8n.io), allowing you to generate high-quality text embeddings using Voyage’s models. It is compatible with n8n’s AI embedding interface.

![](images/voyage-ai-by-mongodb-white.png)

https://www.voyageai.com/

![](/screenshots/workflow-canvas.png)

# Install `n8n-nodes-voyageai-embeddings-unofficial`

> Requires self-hosted n8n

![](/screenshots/install.png)

## Features

- Supports all major Voyage AI embedding models
- Uses LangChain’s `VoyageEmbeddings`
- Configurable output dimensions, batch size, and timeout
- Works with vector stores and retrievers in n8n

## Setup

1. After installing, find the **Embeddings Voyage AI** node in the n8n node palette
   when adding an embedding node.
   
   > ![](/screenshots/find-embedding.png)
   > ![](/screenshots/new-node.png)

2. Create a new credential using your Voyage AI API key.

  > ![](/screenshots/choose-credential.png)
  > ![](/screenshots/credentials.png)

2. That's it! You can choose text embedding models.

  > ![](/screenshots/models.png)