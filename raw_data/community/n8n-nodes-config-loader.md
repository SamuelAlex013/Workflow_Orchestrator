# n8n-nodes-config-loader

**Config Loader** is an n8n community node that lets you load arbitrary configuration or credential data from a single JSON blob (stored in credentials) and inject it directly into your workflow’s data. This makes it easy to centralize environment-specific settings, API endpoints, tokens, or other variables without hard-coding them into each node.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

---

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation to install this node in your n8n instance.

---

### What It Does

* Reads a JSON object from the **Config Loader Auth** credential.
* Safely parses the JSON.
* Merges all properties from the JSON into the current item’s `json` at the root level.

This allows you to keep all of your configuration (URLs, keys, IDs, feature flags, etc.) in one place, then use built-in n8n filters or expressions elsewhere in your workflow to pick out exactly what you need.

---

## Credentials: Config Loader Auth

Before using the node, you must create the **Config Loader Auth** credential:

1. In n8n, go to **Credentials** → **New Credential** → **Config Loader Auth**.
2. In the **Configuration JSON** field, paste a valid JSON object. For example:

   ```json
   {
     "serviceA": {
       "host": "https://api.servicea.com",
       "apiKey": "YOUR_API_KEY"
     },
     "serviceB": [
       {
         "id": "dev",
         "endpoint": "dev.example.com",
         "token": "DEV_TOKEN"
       },
       {
         "id": "prod",
         "endpoint": "api.example.com",
         "token": "PROD_TOKEN"
       }
     ],
     "featureFlagX": true,
     "timeout": 30
   }
   ```

---

## Usage

1. **Drag** the **Config Loader** node into your workflow.

2. **Select** the **Config Loader Auth** credential you configured.

3. **Connect** it to the rest of your workflow.

4. **Run** the workflow. All keys and values from your JSON will be available at the root of each item under `{{$json}}`.

5. **Filter** or **extract** the specific values you need using n8n’s existing **Split Out**, **Filter**, **IF**, or **Function** nodes.

---

## Examples

* 🔑 **Inject API Credentials**
  Store all your API endpoints, keys, and secrets in one JSON blob. Use **Config Loader** at the start of your workflow to inject, then pass specific values into HTTP Request nodes.

* 🛠️ **Feature Flags**
  Toggle features on or off by storing boolean flags in the JSON. Combine with an **IF** node to control branching logic without editing each node.

---

## Compatibility

Tested with n8n **v1.91.3** and above. Should work with any later versions, but please report issues if you encounter problems on significantly newer releases.

---

## Resources

* Node repository: [https://github.com/vgdss/n8n-nodes-config-loader](https://github.com/vgdss/n8n-nodes-config-loader)
* Community nodes installation guide: [https://docs.n8n.io/integrations/community-nodes/installation/](https://docs.n8n.io/integrations/community-nodes/installation/)
* n8n expressions & parameter documentation: [https://docs.n8n.io/nodes/expressions/](https://docs.n8n.io/nodes/expressions/)

---

## Version History

* **0.1.1**

  * Initial release
  * Config Loader Auth credential
  * Config Loader node that injects JSON data at root level

---

*Feel free to open issues or submit PRs to enhance the node!*
