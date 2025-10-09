# n8n-nodes-qonekto

This is an n8n community node that lets you use the Qonekto API in your n8n workflows.

Qonekto provides an HTTP API for managing customers and related resources. This node wraps common endpoints so you can
automate tasks in n8n.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Resources](#resources)
[Version history](CHANGELOG.md)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community
nodes documentation.

## Operations

The node exposes the following resources and operations.

- Kunde (Customer)
    - Create Kunde — POST /kunde
    - Filter Kunden — POST /kunde/filter
    - List Kunden — GET /kunde
    - Show Kunde — GET /kunde/{ameise_id}
    - Update Kunde — PUT /kunde/{ameise_id}
    - Upsert Kunde — PUT /kunde/upsert
  - Upload File — POST /kunde/{kunde_ameise_id}/archiveintrag
  - Create File — POST /kunde/{kunde_ameise_id}/archiveintrag

- Kunden-Tag (Customer Tags)
    - List Customer Tags — GET /kunde/{ameise_id}/tags
    - Set Customer Tags — PUT /kunde/{ameise_id}/tags
    - Add Customer Tags — POST /kunde/{ameise_id}/tags
    - Remove Customer Tags — DELETE /kunde/{ameise_id}/tags

- Listen (Lookup lists)
    - Anreden — GET /anreden
    - Gesellschaften — GET /gesellschaften
    - Kunden Detail Felder — GET /kunden_detail_felder
    - Länder — GET /laender
    - Rechtsformen — GET /rechtsformen
    - Sparten — GET /sparten
    - Status — GET /status
    - Vermittler — GET /vermittler
    - Zahlweisen — GET /zahlweisen

- Panda
    - Create A Customer Link — POST /panda/customer-links
    - Create A Tender — POST /panda/tenders
    - Get Active Tenders For A Customer — GET /panda/tenders
    - Get All Customer Links — GET /panda/customer-links
    - Imports An Ameise Customer Into Panda — POST /panda/customers/{ameiseId}/import

- Pipeline
    - Trigger Pipeline Import From CRM — GET /pipeline/{pipeline_id}/trigger-from-crm

- Misc
    - Who Am I — GET /whoami

Note: The exact input fields for each operation are provided in the node’s parameters within n8n (see the Fields panel
when configuring the node).

## Credentials

This node uses a bearer token, a tenant identifier, and a selectable base URL to authenticate against the Qonekto API.

- API Token (required): Used as a Bearer token for the Authorization header.
- Tenant (required): Your Qonekto tenant identifier used to build the base URL.
- Base URL (required): The API host to use. Currently available option: Production (https://app.qonekto.de/api/).

Behavior

- Effective Base URL: {base_url}{tenant}
- Credential Test: The credential test performs a request to GET /whoami to verify access.

How to obtain credentials

- Visit the Admin > API Tokens page in your Qonekto backend
- Create a new Token and enter a corresponding name, for example "n8n automation"

Security

- n8n stores credentials securely. Avoid hardcoding tokens; configure them via n8n’s Credentials UI.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Qonekto API Docs](https://app.qonekto.de/api/docs/)
- Repository: https://github.com/supersonic-group/n8n-nodes-qonekto
- Issues: https://github.com/supersonic-group/n8n-nodes-qonekto/issues
