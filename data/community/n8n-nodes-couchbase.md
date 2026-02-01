# n8n-nodes-couchbase

This is a collection of n8n community nodes for using Couchbase services within n8n workflows.

Couchbase is a distributed NoSQL cloud database that offers the robustness of a relational database with the flexibility of a JSON document database, featuring key-value operations, SQL++ querying, and powerful search capabilities including vector search.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Nodes](#nodes)
[Installation](#installation)
[Credentials](#credentials)  
[Compatibility](#compatibility)  

## Nodes
Click on the node name to view its detailed documentation.
- [**Couchbase**](nodes/Couchbase/README.md): This node allows you to perform operations on The Couchbase KV, Query, and Search services. It supports creating, reading, updating, and deleting documents, as well as executing SQL++ queries and full-text searches.
- [**Couchbase Search Vector Store**](nodes/vector_store/VectorStoreCouchbaseSearch/README.md): This node allows you to perform vector search operations using the Couchbase Search Service. It supports retrieving, updating, and inserting documents in a vector database, as well as using the vector store as a tool for AI agents.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Credentials

To use the Couchbase node, you'll need to set up Couchbase credentials in n8n:

1. **Prerequisites**:
	- A running Couchbase cluster (using [Couchbase Capella](https://cloud.couchbase.com/) in the cloud, or Couchbase Server)
	- [Database credentials](https://docs.couchbase.com/cloud/clusters/manage-database-users.html#create-database-credentials) with appropriate permissions for the operations you want to perform
   - [Allow IP address](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) for your n8n instance

2. **Credential Parameters**:
	- **Connection String**: The connection string to your Couchbase server (e.g., `couchbase://localhost`)
	- **Username**: Database access username
	- **Password**: Database access password

## Compatibility

This node has been tested with n8n version 1.86.0.

