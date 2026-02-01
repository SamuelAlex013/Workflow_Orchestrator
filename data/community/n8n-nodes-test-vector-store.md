# n8n-nodes-couchbase-vector-store

This is an n8n community node. It lets you use Couchbase Vector Store in your n8n workflows. Couchbase is the multipurpose NoSQL database for transactional, analytical, mobile, and AI applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation) \
[Operations](#operations) \
[Credentials](#credentials) \
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Get Many - get many ranked documents from the vector store using a query
- Insert Documents - insert documents into the vector store
- Update Documents - update documents in the vector store using the document's ID
- Retrieve Documents (As Vector Store for Chain/Tool) - retrieve documents from the vector store to be used by the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore/)
- Retrieve Documents (As Tool for AI Agent) - retrieve documents from the vector store to be used as tool by the AI Agent directly

## Credentials

- [Connecting to Couchbase Server](https://docs.couchbase.com/server/current/guides/connect.html)
- [Connecting to Couchbase Capella](https://docs.couchbase.com/cloud/get-started/connect.html)

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Couchbase documentation](https://docs.couchbase.com/home/index.html)
