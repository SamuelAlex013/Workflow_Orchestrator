# n8n-nodes-vectorx

This is an n8n community node. It lets you use **VectorX** in your n8n workflows.

**VectorX** is a fast, developer-friendly vector database. It allows you to store embeddings, perform similarity searches, and manage indexes for AI-powered applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage) 

---

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

To install manually:

```bash
cd ~/.n8n/custom
git clone https://github.com/owais0604/n8n-nodes-vectorx.git
cd n8n-nodes-vectorx
npm install
npm run build
n8n start
```

## Operations

The VectorX node supports the following operations:

- **Upsert** – Insert or update vectors in a VectorX index.
- **Similarity Search** – Find the most similar vectors for a given embedding.

---

## Credentials

To use the VectorX node, you need:

- **API Key** – Your VectorX API token.
- **Index Name** – The index where vectors will be stored or queried.

### Setup steps

1. Sign up for VectorX and generate an API key.
2. Create or configure an index in VectorX.
3. In n8n, add **VectorX API** credentials with your API key and index name.

---

## Compatibility

- **Minimum n8n version:** 1.0.0
- **Tested with Node.js:** `>=20.19 <=24.x`
- No known incompatibility issues at this time.

---

## Usage

- Use the **OpenAI Embeddings node** (or another embedding generator) to convert text into embeddings.
- Pass the embeddings into the **VectorX node**.
- Choose the operation:  
  - **Upsert** → Store vectors in your VectorX index.  
  - **Similarity Search** → Retrieve nearest neighbors for a query embedding.
