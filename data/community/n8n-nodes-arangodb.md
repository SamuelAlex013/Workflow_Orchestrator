# n8n-nodes-arangodb

This is an n8n community node. It lets you use ArangoDB in your n8n workflows.

ArangoDB is a multi-model NoSQL database system that supports document, graph, and key-value data models.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

* **Document Operations:** Create, read, update, and delete documents in collections.
* **AQL Queries:** Execute ArangoDB Query Language (AQL) queries.
* **Graph Operations:**
  * **Create Graph:** Create a new graph with specified edge definitions.
  * **Delete Graph:** Delete an existing graph.
  * **Add Vertex Collection:** Add a vertex collection to an existing graph.
  * **Remove Vertex Collection:** Remove a vertex collection from a graph.
  * **Add Edge Definition:** Add an edge definition (edge collection, from/to vertex collections) to a graph.
  * **Remove Edge Definition:** Remove an edge definition from a graph.

## Credentials

This node uses API Key authentication. You will need:

* **Host:** The endpoint of your ArangoDB instance (e.g., `http://localhost:8529`).
* **Database:** The name of the database to connect to.
* **Username:** Your ArangoDB username.
* **Password:** Your ArangoDB password.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
