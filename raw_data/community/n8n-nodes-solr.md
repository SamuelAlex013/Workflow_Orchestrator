# n8n-nodes-solr

This is an n8n community node. It lets you use Apache Solr in your n8n workflows.

Apache Solr is an open-source enterprise-search platform, written in Java. Its major features include full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, database integration, and rich document (e.g., Word, PDF) handling.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

*   **Search By Query**: Perform a search using a Solr query.
*   **Add or Update Document**: Add a new document or update an existing one. Can handle single documents or an array of documents.
*   **Delete All Documents**: Deletes all documents from the Solr core.
*   **Delete by ID**: Deletes a document by its ID.
*   **Delete by Field**: Deletes documents that match a specific field-value pair.
*   **Delete by Query**: Deletes documents that match a given query.

## Credentials

To use this node, you need to configure your Solr connection details:
*   **Host**: The hostname or IP address of your Solr server.
*   **Port**: The port number your Solr server is running on.
*   **Core**: The name of the Solr core/collection you want to interact with.
*   **Path**: The path to your Solr instance (e.g., `/solr`).
*   **Secure**: Whether to use HTTPS.
*   **Username/Password**: If your Solr instance requires basic authentication.

## Compatibility

This node was developed against n8n version `1.99.1` and should be compatible with n8n versions `1.0.0` and higher.

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
*   [Apache Solr Reference Guide](https://solr.apache.org/guide/solr/latest/index.html)
