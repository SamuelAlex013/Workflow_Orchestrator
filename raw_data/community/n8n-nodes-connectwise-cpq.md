# n8n-nodes-connectwise-cpq

[![version](https://img.shields.io/npm/v/n8n-nodes-connectwise-cpq.svg)](https://www.npmjs.org/package/n8n-nodes-connectwise-cpq)
[![downloads](https://img.shields.io/npm/dt/n8n-nodes-connectwise-cpq.svg)](https://www.npmjs.org/package/n8n-nodes-connectwise-cpq)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow.svg)](https://buymeacoffee.com/msoukhomlinov)

Community node for ConnectWise CPQ (Sell) REST API, aligned with n8n v1+ node standard.

## Requirements

- ConnectWise CPQ 2022.2 or later (API key–based authentication only)
- API keys (Public/Private) and your Access Key

## Install (n8n UI)

1. Open n8n → Settings (cogwheel)
2. Community Nodes → Install
3. Enter `n8n-nodes-connectwise-cpq`
4. Accept the risk prompt → Install

## Credentials

Create new credentials: "ConnectWise CPQ (Sell) API" and set:

- Access Key: the CPQ site key from the Sell URL when logged in, e.g. `https://connectwise.quosalsell.com/QuosalWeb/home?accesskey=<accesskey>` (use the `<accesskey>` value). Do not use your email/domain or Manage company ID.
- Public Key: generated in CPQ (Settings → Organisation Settings → API Keys)
- Private Key: generated in CPQ (shown once)
- Base URL: `https://sellapi.quosalsell.com` (default; override only if instructed by ConnectWise)

Authentication header is Basic with username `<accesskey>+<publicKey>` and password `<privateKey>`.

Headers automatically set:

- `Content-Type: application/json; version=1.0`
- `Accept: application/json`
- `User-Agent: n8n-connectwise-cpq`

Optional settings:

- Enable Debug Logging: logs masked request details (method, URL, query, headers) and response status to the console.

## Supported resources and operations

- Quotes: get, getAll, delete, copy
- QuoteItems: get, getAll, create, update (PATCH), delete
- QuoteCustomers: getAll (by quote), update (PATCH), replace (PUT), delete
- QuoteTabs: getAll, getItemsByTab
- QuoteTerms: getAll (by quote), create, update (PATCH), delete
- RecurringRevenue: getAll
- TaxCodes: getAll
- Templates: getAll
- User: getAll, update (PATCH)

## Parameters

- Filters: `conditions` (raw) or the Condition Builder UI, `includeFields` (multi-select), `showAllVersions` (where supported)
- Pagination: `returnAll`, `limit`, `pageSize` (max 1000)

### Pagination behaviour

- When `Return All` is enabled: the node uses the maximum supported `pageSize` (1000) and paginates until the API returns fewer than requested results.
- When `Return All` is disabled: the node auto-manages pagination to satisfy `limit`. It will set the effective `pageSize` to `min(limit, 1000)` and fetch across pages until `limit` items are collected. You can still provide a `pageSize` but it will be bounded by the effective calculation.

## Error handling

- `continueOnFail`: errors are collected per item and execution continues
- Retries: 429/5xx responses retried up to 3 times with exponential backoff

## Examples

Example workflows are coming soon under `.docs/examples/`.

### Condition Builder

You can now construct `conditions` via a visual builder:

- Add rows with: Field, optional Reference Subfield (to become `field/subfield`), Operator (`=`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not contains`, `like`, `in`, `not in`), Value Type (String, Integer, Boolean, Datetime, List), and the Value(s).
- The builder auto-formats values according to the CPQ rules:
  - Strings are quoted: `name = "Acme"`
  - Booleans are `True`/`False`: `closedFlag = True`
  - Datetimes are wrapped in brackets: `lastUpdated = [2024-01-01T00:00:00Z]`
  - Lists produce parentheses: `status in ("Open","Closed")`
- Multiple rows are joined with the selected Logic (AND/OR). If you also provide a raw `conditions` string, it will be combined with the builder output using that Logic.

You may still enter a raw `conditions` string for advanced scenarios; the builder is optional and backward compatible.

### Include Fields

The `includeFields` parameter is a resource-aware multi-select. Options are populated dynamically from `/.docs/references/SellAPI.json` for the selected resource. You can also specify field names using an expression.

## Notes

- Only CPQ 2022.2+ is supported. Legacy username/password auth is not supported.
- This node consumes the official Swagger: see `references/SellAPI.json`.
