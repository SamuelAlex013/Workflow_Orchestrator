![Apollo](nodes/Apollo/apollo.svg)

# n8n-nodes-apollo

Community n8n node for the Apollo API. Supports People and Organization enrichment and search.

- Package: `n8n-nodes-apollo`
- Requires: Node.js >= 20
- License: MIT
- Repository: https://github.com/arturl95/n8n-nodes-apollo
- npm: https://www.npmjs.com/package/n8n-nodes-apollo

## Installation (in n8n)

1. In n8n, go to Settings → Community Nodes → Install.
2. Enter the package name: `n8n-nodes-apollo` and install.
3. Create credentials for “Apollo API” with your API key and optional base URL.

## Credentials

Credential: `Apollo API` (`credentials/ApolloApi.credentials.ts`)

- API Key: Injected via `x-api-key` header.
- Base URL: Defaults to `https://api.apollo.io`.
- Test: `GET /v1/auth/health` against the Base URL.

## Supported resources and operations

Resource: `Person`

- Enrich Person — POST `/api/v1/people/match`
- Search People — POST `/api/v1/mixed_people/search`
- Bulk Enrich People — POST `/api/v1/people/bulk_match`

Resource: `Organization`

- Enrich Organization — GET `/api/v1/organizations/enrich`
- Bulk Enrich Organizations — POST `/api/v1/organizations/bulk_enrich`
- Search Organizations — POST `/api/v1/mixed_companies/search`
- Get Job Postings — GET `/api/v1/organizations/{organization_id}/job_postings`

Resource: `Contact`

- Create Contact — POST `/api/v1/contacts`
- Update Contact — PUT `/api/v1/contacts/{contact_id}`
- Search Contacts — POST `/api/v1/contacts/search`

Resource: `Account`

- Search Accounts — POST `/api/v1/accounts/search`

Resource: `Deal`

- Create Deal — POST `/api/v1/opportunities`
- List All Deals — GET `/api/v1/opportunities/search`
- View Deal — GET `/api/v1/opportunities/{opportunity_id}`
- Update Deal — PATCH `/api/v1/opportunities/{opportunity_id}`

## Usage notes

- People Search does not generate new emails or phone numbers; use People Enrichment to retrieve contact details.
- Most filters are exposed as query parameters and support multiple values via n8n “Fixed Collection” fields (e.g., `person_titles[]`, `organization_locations[]`).
- Pagination parameters `page` and `per_page` are available where supported.
- Contact Create/Update body is constructed from simple fields and Fixed Collections (e.g., `label_names`). Pass `typed_custom_fields` as a JSON object string (e.g., `{ "60c39...": "2025-08-07" }`). Use Apollo’s Custom Fields API to discover field IDs and valid data types.
- Apollo does not deduplicate on Create Contact. If you create a contact that already exists, Apollo will create a separate new contact.
- Some workspace-only endpoints have limits or plan requirements:
  - Contacts/Accounts Search results are capped (100 per page, up to 500 pages). Narrow filters to stay within limits.
  - Deals endpoints require a master API key; otherwise you will receive 403 responses.

## Development

```bash
npm run lint
npm run build
npm run dev
```

Artifacts are emitted to `dist/`. Icons from `nodes/**` and `credentials/**` are copied to `dist` by the Gulp task `build:icons`.

## Changelog

- 0.1.1
  - Added Contact: Search Contacts; Create/Update field coverage and typed_custom_fields support
  - Added Account: Search Accounts with filtering, sorting, and pagination
  - Added Deal resource (UI label) with Create/List/View/Update endpoints
  - Alphabetized resource list and fixed lint issues; improved README usage notes

- 0.1.0
  - Initial release: Apollo credentials and node
  - Person: Enrich, Search, Bulk Enrich
  - Organization: Enrich, Bulk Enrich, Search, Job Postings

This repo contains example nodes to help you get started building your own custom integrations for [n8n](https://n8n.io). It includes the node linter and other dependencies.

To make your custom node available to the community, you must create it as an npm package, and [submit it to the npm registry](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry).

If you would like your node to be available on n8n cloud you can also [submit your node for verification](https://docs.n8n.io/integrations/creating-nodes/deploy/submit-community-nodes/).

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this starter

These are the basic steps for working with the starter. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your new repo:
   ```
   git clone https://github.com/<your organization>/<your-repo-name>.git
   ```
3. Run `npm i` to install dependencies.
4. Open the project in your editor.
5. Browse the examples in `/nodes` and `/credentials`. Modify the examples, or replace them with your own nodes.
6. Update the `package.json` to match your details.
7. Run `npm run lint` to check for errors or `npm run lintfix` to automatically fix errors when possible.
8. Test your node locally. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) for guidance.
9. Replace this README with documentation for your node. Use the [README_TEMPLATE](README_TEMPLATE.md) to get started.
10. Update the LICENSE file to use your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
