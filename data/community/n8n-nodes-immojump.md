# n8n-nodes-immojump

ImmoJump n8n Community Nodes (Trigger + Actions)

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The ImmoJump n8n Community Nodes provide comprehensive automation capabilities:

### Actions (ImmoJump Node)
* **User Operations**
  - Get Many Users
  - Get User by ID
  - Create User

* **Company Operations**
  - Get Many Companies (with pagination)

* **Immobilie Operations**
  - Get Many Immobilies (with pagination)
  - Get Immobilie by ID
  - Create Immobilie
  - Update Status
  - Assign Tag
  - Remove Tag

### Triggers (ImmoJump Trigger Node)
* **Status Changed** - Triggers when an immobilie status changes
* **Tag Assigned** - Triggers when a tag is assigned to an immobilie
* **Tag Removed** - Triggers when a tag is removed from an immobilie
* **New Immobilie Created** - Triggers when a new immobilie is created

Each trigger supports filtering options to only trigger on specific conditions.

### Dynamic option loading (Tags & Status)

Both the action and trigger nodes reuse the same tag and immobilie status catalogue that powers our Vite frontend. When you open a dropdown in n8n the node performs a live lookup against your running ImmoJump backend using the credentials you configure:

- `GET /api/statuses/statuses` → returns the status list (matching the TypeScript shape in `immobilien-ka/src/types/ImmobilienStatus.ts` and the helper in `immobilien-ka/src/Services/Api/ImmobilienStatusApiService.ts`). The endpoint scopes results to the organisation from `X-Organisation-Id` (or the caller’s `current_organisation_id`).
- `GET /api/integrations/tags` → returns the tag list (see `immobilien-ka/src/Services/Api/TagApiService.ts`).

Because the node talks directly to the app, any change you make in the UI (adding a new status, renaming a tag, rearranging pipeline stages, etc.) is immediately reflected inside n8n. For local development start the stack with `make start-flask` (or `make tmux` for the full environment) so the endpoints are reachable from n8n. Custom implementations must respond with JSON arrays, for example:

```json
[
  { "id": 42, "name": "Besichtigung geplant" }
]
```

If the endpoint is unreachable the node falls back to a debug placeholder so you instantly see that the lookup failed.

## Credentials

_If users need to authenticate with the app/service, provide details here. You should include prerequisites (such as signing up with the service), available authentication methods, and how to set them up._

## Compatibility

_State the minimum n8n version, as well as which versions you test against. You can also include any known version incompatibility issues._

## Usage

_This is an optional section. Use it to help users with any difficult or confusing aspects of the node._

_By the time users are looking for community nodes, they probably already know n8n basics. But if you expect new users, you can link to the [Try it out](https://docs.n8n.io/try-it-out/) documentation to help them get started._

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [ImmoJump API documentation](https://docs.immojump.com/)

## Version history

_This is another optional section. If your node has multiple versions, include a short description of available versions and what changed, as well as any compatibility impact._
