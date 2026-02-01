# n8n-nodes-neo4jtool

This is an n8n community node. It lets you interact with a Neo4j database using a set of specialized nodes, particularly focused on booking system logic.

Neo4j is a native graph database platform, built from the ground up to leverage not only data but also data relationships.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)
[Development Notes](#development-notes)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This package provides a collection of specialized nodes for interacting with a Neo4j database based on a specific booking system schema. Key operations include:

*   Managing Users, Businesses, Services, Customers, Staff, Resources, and Bookings (CRUD operations).
*   Finding available booking slots based on business rules (`FindAvailableSlots`).
*   Setting staff availability.

For detailed usage instructions and examples, please refer to `USER_MANUAL.md` (中文) or `README.zh-TW.md` (中文).

## Credentials

To use these nodes, you need to configure Neo4j credentials named `neo4jApi` in n8n. This requires the following information from your Neo4j instance:

*   **Host**: The host address of your Neo4j instance, including the protocol (e.g., `neo4j://localhost`, `bolt://your-server.com`, `neo4j+s://your-aura-instance.databases.neo4j.io`).
*   **Port**: The Bolt port number for your Neo4j instance (typically `7687`).
*   **Database**: The name of the database to connect to (optional, defaults to `neo4j`).
*   **Username**: The username for authenticating with Neo4j.
*   **Password**: The password for the specified username.

## Compatibility

*   Minimum n8n version: (Requires testing, likely >=1.0)
*   Minimum Node.js version: >=18.10 (as specified in `package.json`)

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
*   [Neo4j Documentation](https://neo4j.com/docs/)
*   [Neo4j Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)

## Development Notes

*   **2025-04-29:** Updated the description for the `hoursData` parameter in `Neo4jSetBusinessHours.node.ts` to clarify the expected format for `day_of_week` (1-7, Sunday=7) and fixed angle bracket encoding for ESLint compliance.
*   **2025-04-29:** Generated `Docs/NodeDescriptions.md` containing descriptions for all nodes based on their `INodeTypeDescription` and properties. This file serves as a quick reference for node parameters and functionality.
*   **2025-04-29:** Updated the format of the `description` field for the `Neo4jCreateBooking` node in `Docs/NodeDescriptions.md` to be a single line with `\n` for line breaks.
