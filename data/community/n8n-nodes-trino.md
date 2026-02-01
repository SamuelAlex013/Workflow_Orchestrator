# n8n-nodes-trino

![Banner image](docs/banner.png)

This is an n8n community node that allows you to use [Trino](https://trino.io/) in your n8n workflows.

Tested with n8n 1.90.2 and Trino 475. You may need to adjust dependencies according to your setup.

- Trino is a distributed SQL query engine designed for fast, interactive analytics with multiple connections to various SQL engines.
- [n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **Query**: Execute SQL queries against Trino. Node returns rows as items.

## Credentials

Configure your Trino connection details in the node's credentials.

For more information, please refer to the [Trino JDBC client documentation](https://trino.io/docs/current/client/jdbc.html).

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Trino docs](https://trino.io/docs/current/index.html)

## Attribution

This node is based on the original work by the n8n team's [Master node](https://github.com/n8n-io/n8n-nodes-starter/tree/master) and Jakub Kaflik's [Clickhouse node](https://github.com/jkaflik/n8n-nodes-clickhouse).
