# n8n-nodes-matrix42

This is an n8n community node that integrates with the Matrix42 ESMP Web Services API. It allows you to retrieve and work with Data Fragments from Matrix42 Data Definitions directly in your n8n workflows.

Matrix42’s ESMP API exposes CRUD‑style endpoints for data fragments, supporting OData‑like filtering, column selection, paging, sorting, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports multiple operations across different resources:

### Data Fragments (asql)

-   **Get Fragments** (`getFragments`): Retrieve data fragments from a specified Data Definition.

-   **Add Fragment** (`addFragment`): Create a new data fragment in the specified Data Definition.

-   **Update Fragment** (`updateFragment`): Update an existing data fragment by its ID.

-   **Delete Fragment** (`deleteFragment`): Remove a data fragment by its ID.


### Data Objects (asql)

-   **Add Object** (`addObject`): Create a new Data Object under a given fragment.

-   **Get Object** (`getObject`): Retrieve a Data Object by its ID.

-   **Update Object** (`updateObject`): Update an existing Data Object by its ID.

-   **Delete Object** (`deleteObject`): Delete a Data Object by its ID.


### Tickets

-   **Create Ticket** (`createTicket`): Open a new ticket in the Service Desk.

-   **Close Ticket** (`closeTicket`): Close an existing ticket by ID.

-   **Transform Ticket** (`transformTicket`): Apply a transformation to a ticket.


### Import

-   **Execute Import Definition** (`executeImportDefinition`): Run a predefined import definition to ingest data.

## Credentials

> **Prerequisite:** You must have access to a running Matrix42 instance with appropriate API permissions.

This node supports two authentication methods. Configure these under **Workflow → Credentials**.

### Matrix42 Token Auth

1.  **API Token** — Your long‑lived Matrix42 API Token.

2.  **Base URL** — Your Matrix42 server URL (e.g. `https://api.mycompany.com`).


On execution, the node:

-   Exchanges the API Token for a short‑lived Bearer (JWT) token via `GenerateAccessTokenFromApiToken`.

-   Uses the Bearer token in the `Authorization` header for all subsequent calls.


> **Self‑signed certificates**: If your Matrix42 server uses a self‑signed SSL certificate, you must add its CA certificate to n8n’s trusted certificate store. For details, see the n8n docs on adding self‑signed certificates: https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority/

### Matrix42 Basic Auth

1.  **Username** and **Password** — Your Matrix42 user credentials.

2.  **Base URL** — As above.

## Compatibility

-   **n8n**: Tested with v1.100.1 and later.

-   **Node.js**: v22.17.0 or higher.

-   **Matrix42 ESMP API**: Tested with Matrix42 12.1.2.5325.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Matrix42 Web Services](https://help.matrix42.com/030_ESMP/030_INT/Business_Processes_and_API_Integrations/Matrix42_Web_Services_API#Public_API)

## Version History

**0.1.0:**
  - Initial release supporting operations across multiple resources:
    -   Data Fragments: `getFragments`, `addFragment`, `updateFragment`, `deleteFragment`
    -   Data Objects: `addObject`, `getObject`, `updateObject`, `deleteObject`
    -   Tickets: `createTicket`, `closeTicket`, `transformTicket`
    -   Import: `executeImportDefinition`

  - Authentication methods:
    -   Matrix42 Token API (API Token ↔︎ Bearer JWT exchange)
    -   Matrix42 Basic API (HTTP Basic Authentication)
