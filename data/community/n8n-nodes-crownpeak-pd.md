
<a href="http://www.crownpeak.com" target="_blank">
  <img src="./images/logo/crownpeak-logo.png" alt="Crownpeak Logo" title="Crownpeak Logo" />
</a>

# n8n-nodes-crownpeak-pd

## Overview

This repository provides a custom n8n integration node for the [Fredhopper Product Discovery API](https://crownpeak.gitbook.io/product-discovery). It enables direct access to product discovery operations such as authentication, item management, catalog, category tree, and locale configuration within an n8n workflow.

## What is it?

An n8n node module designed to simplify integration with Crownpeak Fredhopper Product Discovery's API using secure credential management. It supports:

- Secure authentication using username/password and OAuth2 token endpoint
- Manage product items: create, update, delete, and upsert
- Manage item schemas and catalogs
- Manage category trees and locale settings
- Chain operations using dynamic expressions for automated product data pipelines

## What is it for?

This module is useful for organizations looking to build automated product onboarding, enrichment, and publishing pipelines into the Crownpeak Fredhopper ecosystem.

---


## Supported Resources & Operations

| Resource         | Operations Supported                  |
|------------------|----------------------------------------|
| Authentication   | Get Token                             |
| Product Items    | Get, Create, Update, Delete, Upsert, Batch Operations |
| Item Schemas     | Create, Get, Update, Delete           |
| Catalogs         | Get, Create, Create with Default Batch, Delete, Activate, List  |
| Category Tree    | Get, Create, Update, Delete, List    |
| Locales          | Set, Get, Delete                      |


| Feature | Method | Endpoint | Description |
|---------|--------|----------|-------------|
| Get Token | POST | /auth/realms/solutions/protocol/openid-connect/token | Obtain authentication token |
| Upsert Items | POST | /items | Create a new product item |
| Patch Items | PATCH | /items | Update existing product item attributes |
| Delete Items | DELETE | /items | Delete product item |
| Create an Item Schema | POST | /item-schemas | Create a new item schema |
| Update an Item Schema | PUT | /item-schemas/{name} | Update an existing item schema |
| Delete an Item Schema | DELETE | /item-schemas/{name}/{version} | Delete an item schema |
| Get an Item Schema | GET | /item-schemas/{name}/{version} | Get an item schema by name and version |
| Create Batch | POST | /batch-imports | Create a new batch for item operations |
| List Batches | GET | /batch-imports | List all batches |
| Add Items to Batch | POST | /batch-imports | Add items to an existing batch |
| Modify Items in Batch | PATCH | /batch-imports/items | Modify items in an existing batch |
| Delete Items from Batch | DELETE | /batch-imports/items/delete | Delete items from an existing batch |
| Submit Batch Ingestion | POST | /batch-imports/ingestion | Submit batch for processing |
| Get Batch Ingestion Status | GET | /batch-imports/ingestion/{id} | Get status of batch ingestion |
| List Batch Ingestions | GET | /batch-imports/ingestion | List all batch ingestions |
| Delete Batch Ingestion | DELETE | /batch-imports/ingestion/{id} | Delete a batch ingestion |
| Create a Catalog | POST | /catalogs | Create a new catalog |
| Create Catalog With Default Batch | POST | /catalogs?createBatchImport=true | Create a catalog and automatically create a default batch with ID matching the catalog version |
| Delete a Catalog | DELETE | /catalogs/{name}/{version} | Delete an inactive catalog |
| Activate a Catalog Version | PUT | /catalogs/{name}/{version}/activate | Activate a catalog version |
| Get Active Catalog Version | GET | /catalogs/{name}/active | Get the currently active catalog version |
| List Catalogs | GET | /catalogs | List all catalogs |
| Create a Category Tree | POST | /category-trees | Create a new category tree |
| Update a Category Tree | PUT | /category-trees/{name} | Update an existing category tree |
| List Category Trees | GET | /category-trees | List all category trees |
| Get a Category Tree | GET | /category-trees/{name}/{version} | Get a category tree by name and version |
| Delete a Category Tree | DELETE | /category-trees/{name}/{version} | Delete a category tree |
| Set Default Locale | POST | /locales | Set the default locale for an item schema |
| Get Default Locale | GET | /locales/{name} | Get the default locale for an item schema |
| Delete Default Locale | DELETE | /locales/{name} | Delete the default locale for an item schema |

Each method supports query parameterization using dynamic expressions and securely authenticates using credentials.

## Installation & Usage

### As a Private Node
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/Crownpeak/n8n-nodes-crownpeak-pd.git
   ```
2. Build the node module:
   ```sh
   cd n8n-nodes-crownpeak-pd
   npm install
   npm run build
   ```
3. Copy the `dist/` folder to your n8n instance's custom nodes directory:
   ```sh
   docker cp ./dist n8n-dev:/home/node/.n8n/custom-nodes/crownpeak-pd
   ```
4. Restart your n8n Docker container:
   ```sh
   docker restart n8n-dev
   ```
5. Log in to n8n and the node will appear as Fredhopper Product Discovery.

> ℹ️ If it doesn't appear, ensure you are mounting or copying to the correct container path and that `NODE_FUNCTION_ALLOW_EXTERNAL` is not overly restricted.

### As a Community Node (once approved)
Once this node is approved and published on the official [n8n integrations registry](https://n8n.io/integrations), installation will be as simple as:
```sh
n8n install n8n-nodes-crownpeak-pd
```
And in `n8n@1.100.0+` via the UI:

1. Open Settings → Community Nodes
2. Click Install a Community Node
3. Search or paste: `n8n-nodes-crownpeak-pd`
4. Click Install

---

## 📸 Screenshots
1. A basic workflow example using n8n Crownpeak PD Node
   ![A basic workflow example using n8n Crownpeak PD Node](./images/screenshots/basic-workflow-example-1.png "A basic workflow example using n8n Crownpeak PD Node")

2. The result of /items POST
   ![The result of /items POST](./images/screenshots/basic-workflow-example-2.png "The result of /items POST")

---

## Credentials

This node supports authentication against the Crownpeak Product Discovery API. You’ll need the following credentials:

- Username and Password
- OAuth2 Token URL

Refer to the [Product Discovery documentation](https://crownpeak.gitbook.io/product-discovery/) for full details on credential setup.

---

## Support

- This repository is maintained by Crownpeak and released under the MIT License.
- For Crownpeak platform questions, please contact your Customer Success Manager or [support@crownpeak.com](mailto:support@crownpeak.com).
- For n8n integration issues or pull requests, use GitHub Issues or Discussions.

## License

MIT © Crownpeak Technology, Inc.
See [LICENSE](./LICENSE) for details.
