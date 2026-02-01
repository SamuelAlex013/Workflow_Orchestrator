# n8n-nodes-neo4j

This is an n8n community node for Neo4j integration with LangChain support. It provides both vector store and graph database operations.

[Neo4j](https://neo4j.com/) is a graph database with vector search for knowledge graphs.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)  
[Version history](#version-history)


## Features

- Vector Store Operations:
  - Similarity Search: Search for similar vectors in the database
  - Add Texts: Add new texts to the vector store

- Graph Database Operations:
  - Execute Query: Run custom Cypher queries
  - Create Node: Create new nodes with labels and properties
  - Create Relationship: (Coming soon) Create relationships between nodes

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Vector Store Operations

#### Similarity Search
1. Select "Vector Store" as the resource
2. Choose "Similarity Search" operation
3. Enter the query text
4. Execute to find similar vectors

#### Add Texts
1. Select "Vector Store" as the resource
2. Choose "Add Texts" operation
3. Enter the texts to add
4. Execute to store the texts as vectors

### Graph Database Operations

#### Execute Query
1. Select "Graph Database" as the resource
2. Choose "Execute Query" operation
3. Enter your Cypher query
4. Execute to run the query

#### Create Node
1. Select "Graph Database" as the resource
2. Choose "Create Node" operation
3. Enter the node label
4. Provide node properties as JSON
5. Execute to create the node

## Credentials

1. Add Neo4j credentials in n8n:
   - Connection URI (e.g., `neo4j://localhost:7687`)
   - Username
   - Password
   - Database name

2. The node will appear in the n8n nodes panel under "Neo4j"

## Compatibility

Tested against n8n 1.88.0

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Neo4j LanchainJS documentation](https://neo4j.com/labs/genai-ecosystem/langchain/?utm_source=Google&utm_medium=PaidSearch&utm_campaign=UCGenAI&utm_content=AMS-Search-SEMCO-UCGenAI-None-SEM-SEM-NonABM&utm_term=neo4j%20ai&utm_adgroup=genai-llm&gad_source=1&gclid=CjwKCAjw1emzBhB8EiwAHwZZxeV_k7HJ0bkZyfLqozioVYpxQtNyzFMjkO1ZTXZyIXiRec_ScCLKThoC_RUQAvD_BwE)

## Version history

1.0 : first runnable version of Neo4j VectorStore node


## Development

1. Clone this repository
2. Install dependencies: `npm install`
3. Build: `npm run build`
4. Link to n8n: `npm link`
5. In your n8n installation: `npm link n8n-nodes-neo4j`

## Version history

### Version 0.1.x
tested against n8n 1.45.1 to 1.86.0
include vector stores retrieval only

### Version 0.2.x
tested against n8n 1.88.0
include vector stores and graph 

## License

MIT 