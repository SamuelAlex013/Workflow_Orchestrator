<img src="https://raw.githubusercontent.com/octionic/n8n-nodes-appflowy/refs/heads/master/nodes/Appflowy/appflowy.svg" align="left" style="margin-right: 20px; height: 74px; width: 74px;">

# n8n-nodes-appflowy

This is an n8n community node. It lets you use AppFlowy in your n8n workflows. It comes with a Regular as well as a Trigger Node and is also available as Tool in AI Agents.

AppFlowy is a privacy-first, open source workspace for your notes, wikis, projects, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Set the environment variable `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true` to enable the Tool usage for AI agents.

## Operations

### Trigger

- Row Added to Database
- Row Updated in Database

### Node

Workspaces
- Get Many

Databases
- Get Many

Database Rows
- Create
- Create or Update
- Get
- Get Many

## Credentials

### Prerequisites

This works for both AppFlowy Cloud and self-hosted AppFlowy instances. The following describes how to set up the credentials for AppFlowy Cloud:

- Signup for AppFlowy Cloud
- Login to the admin panel here: https://beta.appflowy.cloud/
- Navigate to "Change Password" and set a new password

### Create credential

- Create a new credential for AppFlowy in n8n
- Set the following values:
  - `Host`: `https://beta.appflowy.cloud/`
  - `Username`: your email adress (could be from the connected Gmail account)
  - `Password`: the password you just defined


## Compatibility

This Node has been built with n8n Version `1.79.0`, which is the first one that supports the Tool usage for AI agents.

## Usage

### Use custom JSON for properties

While properties can be mapped comfortably, in some cases you might need a more dynamic input. For that you can specify a JSON object defining the properties and their values.

In general the property can be referenced by its ID or name. Except for options of SingleSelect and MultiSelect. There it only works by name.

Some examples:

**SingleSelect:**

```json
"Status": "Done"
```

**MultiSelect:**

```json
"Tags": ["yellow", "orange"]
```

**Checkbox:**

```json
"External": true
```

**DateTime:**
requires UTC timestamp in seconds

```json
"Due Date": {
  "timestamp": "1739746800",
  "end_timestamp": "1739800800",
  "is_range": true,
  "include_time": true
}
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [AppFlowy Documentation](https://docs.appflowy.io/docs)
* [AppFlowy API Documentation](https://github.com/AppFlowy-IO/AppFlowy-Docs/tree/main/documentation/appflowy-cloud/openapi)

## Version history

See: https://github.com/octionic/n8n-nodes-appflowy/releases
