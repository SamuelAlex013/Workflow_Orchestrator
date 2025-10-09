# n8n-nodes-bitrix

This is an n8n community node. It lets you use **Bitrix24** in your n8n workflows.

**Bitrix24** is a powerful collaboration platform that includes CRM, tasks, projects, communications, and more — all in a unified workspace. This node allows you to interact with core Bitrix24 entities such as contacts, leads, companies, and deals.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

---

## Installation

Follow the installation guide in the n8n community nodes documentation.

1. Go to **Settings** > **Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-bitrix` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**. 

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.


---

## Operations

This node supports the following Bitrix24 modules and operations:

### Modules

* `crm.company`
* `crm.contact`
* `crm.deal`
* `crm.lead`
* (more coming soon)

### Supported operations per entity:

* **Create** (Add a new entity)
* **Get** (Get an entity by ID)
* **Update** (Update an entity by ID)
* **Delete** (Delete an entity by ID)
* **List** (Query/filter entities)
* **Get Fields Description** (Fetch metadata for custom fields)

Each operation supports:

* **Field-by-field input** or **raw JSON** input
* Filtering, sorting, and field selection for list queries

---

## Credentials

This node supports two authentication methods:

### 1. Bitrix Webhook

Use a webhook URL from Bitrix24 (e.g. `https://yourdomain.bitrix24.ru/rest/1/abc123xyz/`).

To set this up:

* In Bitrix24, go to **Developer tools → Webhooks**
* Create an inbound webhook and select required access
* Copy the webhook URL and use it in credentials

### 2. OAuth2 (Bitrix24 REST API)

If you want to use OAuth2:

* Create an application in Bitrix24
* Use the client ID, secret, and domain in the OAuth2 credential
* Supports automatic token refresh and secure API access

---

## Compatibility

* **Tested on:** `1.92.2`

Known limitations:

* Some custom fields in Bitrix may require extra formatting depending on field type.

---

## Usage

When creating or updating records, you can choose to:

* Fill fields one-by-one (dynamic list of available fields is loaded)
* Or provide the full data in raw JSON

When listing entities, you can:

* Use simple filters (field, operator, value)
* Or provide complex JSON filters (e.g., combined filters, nested conditions)

Field names are loaded dynamically based on selected entity (e.g., `crm.contact`), making it easier to work with custom fields.

---

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Bitrix24 REST API documentation](https://training.bitrix24.com/rest_help/)
* [Bitrix24 Webhooks Guide](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html)

---

## Version history

| Version  | Changes                                                                                                                    |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| 1.0.0    | Initial release with support for CRM module (contact, company, deal, lead), including create/get/update/delete/list/fields |
| 1.1.0    | Added support for both OAuth2 and Webhook auth, improved filter and JSON input modes                                       |
| 1.2.x    | Bug-fixes. Added Custom Method                                                                                             |
| 1.3.x    | Added Universal Methods for Core Elements ( crm.item.* )                                                                   |
| Upcoming | Support for tasks, users, and activity logging                                                                             |
