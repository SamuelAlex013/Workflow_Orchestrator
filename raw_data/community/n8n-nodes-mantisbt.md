# n8n-nodes-mantisbt

This is an n8n community node. It lets you use **MantisBT** in your n8n workflows.

**MantisBT** is an open-source, web-based bug tracking system written in PHP, supporting MySQL/MariaDB and PostgreSQL, with role-based access control, email notifications, plugin support, and integration capabilities via REST API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Implementation](#implementation)  
[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Implementation status

### Issues

| Endpoint                               | Implemented | Omitted | Note            | Tested |
| -------------------------------------- | ----------- | ------- | --------------- | ------ |
| Get an issue                           |             | x       | merged into one |        |
| Get an issue (specific fields)         | x           |         |                 |        |
| Get issue files                        | x           |         |                 |        |
| Get issue file (single)                | x           |         |                 |        |
| Get all issues                         |             | x       | merged into one | x      |
| Get all issues (specified fields)      | x           |         |                 |        |
| Get issues for a project               |             | x       | merged into one |        |
| Get issues matching filter             |             | x       | merged into one |        |
| Get issues assigned to me              |             | x       | merged into one |        |
| Get issues reported by me              |             | x       | merged into one |        |
| Get issues monitored by me             |             | x       | merged into one |        |
| Get unassigned issues                  |             | x       | merged into one |        |
| Create an issue (minimal)              |             |         |                 |        |
| Create an issue                        |             |         |                 |        |
| Create an issue with attachments       |             |         |                 |        |
| Update an issue (minimal)              |             |         |                 |        |
| Update an issue                        |             |         |                 |        |
| Delete an issue                        |             |         |                 |        |
| Monitor an issue                       |             |         |                 |        |
| Monitor an issue (for specified users) |             |         |                 |        |
| Attach a tag to issue                  |             |         |                 |        |
| Detach a tag from an issue             |             |         |                 |        |
| Add an issue relationship              |             |         |                 |        |
| Delete an issue relationship           |             |         |                 |        |

### Issue Notes and Attachments

| Endpoint                                | Implemented | Omitted | Note | Tested |
| --------------------------------------- | ----------- | ------- | ---- | ------ |
| Create an issue note                    |             |         |      |        |
| Create an issue note with time tracking |             |         |      |        |
| Create an issue note with attachment    |             |         |      |        |
| Delete an issue note                    |             |         |      |        |
| Add attachments to issue                |             |         |      |        |

### Projects

| Endpoint         | Implemented | Omitted | Note | Tested |
| ---------------- | ----------- | ------- | ---- | ------ |
| Project Users    |             |         |      |        |
| Project Versions |             |         |      |        |
| Sub-Projects     |             |         |      |        |
| Get all projects | x           |         |      |        |
| Get a project    | x           |         |      |        |
| Create a project |             |         |      |        |
| Update a project |             |         |      |        |
| Delete a project |             |         |      |        |

### Filters

| Endpoint        | Implemented | Omitted | Note | Tested |
| --------------- | ----------- | ------- | ---- | ------ |
| Get all filters |             |         |      |        |
| Get a filter    |             |         |      |        |
| Delete a filter |             |         |      |        |

### Users

| Endpoint                  | Implemented | Omitted | Note            | Tested |
| ------------------------- | ----------- | ------- | --------------- | ------ |
| Get My User Info          |             | x       | merged into one |        |
| Get My User Info (select) | x           |         |                 |        |
| Get User By Id            |             | x       | merged into one |        |
| Get User By Id (select)   | x           |         |                 |        |
| Get User By Username      |             |         |                 |        |
| Create a user             |             |         |                 |        |
| Create a user (minimal)   |             |         |                 |        |
| Update User               |             |         |                 |        |
| Reset user password       |             |         |                 |        |
| Delete a user             |             |         |                 |        |

### User Tokens

| Endpoint              | Implemented | Omitted | Note | Tested |
| --------------------- | ----------- | ------- | ---- | ------ |
| Create token for me   |             |         |      |        |
| Delete token for me   |             |         |      |        |
| Create token for user |             |         |      |        |
| Delete token for user |             |         |      |        |

### Config

| Endpoint                           | Implemented | Omitted | Note | Tested |
| ---------------------------------- | ----------- | ------- | ---- | ------ |
| Get Configuration Option           |             |         |      |        |
| Get Multiple Configuration Options |             |         |      |        |
| Set Configs                        |             |         |      |        |

### Lang

| Endpoint                       | Implemented | Omitted | Note | Tested |
| ------------------------------ | ----------- | ------- | ---- | ------ |
| Get a localized string         |             |         |      |        |
| Get multiple localized strings |             |         |      |        |

### Pages

| Endpoint            | Implemented | Omitted | Note | Tested |
| ------------------- | ----------- | ------- | ---- | ------ |
| Get Issue View Page | x           |         |      |        |

### Impersonation

| Endpoint                            | Implemented | Omitted | Note | Tested |
| ----------------------------------- | ----------- | ------- | ---- | ------ |
| Get My User Info with Impersonation |             |         |      |        |

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

_List the operations supported by your node._

## Credentials

_If users need to authenticate with the app/service, provide details here. You should include prerequisites (such as signing up with the service), available authentication methods, and how to set them up._

## Compatibility

_State the minimum n8n version, as well as which versions you test against. You can also include any known version incompatibility issues._

## Usage

_This is an optional section. Use it to help users with any difficult or confusing aspects of the node._

_By the time users are looking for community nodes, they probably already know n8n basics. But if you expect new users, you can link to the [Try it out](https://docs.n8n.io/try-it-out/) documentation to help them get started._

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [MantisBT website](https://mantisbt.org/)
- [MantisBT documentation](https://mantisbt.org/documentation.php)

## Version history

_This is another optional section. If your node has multiple versions, include a short description of available versions and what changed, as well as any compatibility impact._
