# n8n-nodes-simplified

This is an n8n community node. It lets you use **Simplified** in your n8n workflows.

**Simplified** is a content creation and marketing platform that helps teams generate, schedule, and manage social media content using AI.

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

Option 1: Install via n8n UI
1. Go to Settings > Community Nodes
2. Click on Install
3. Enter n8n-nodes-simplified in the npm Package Name field
4. Click on Install

Option 2: Install the node from npm:

```bash
npm install n8n-nodes-simplified
```

Then follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) for community nodes in the n8n documentation.

---

## Operations

### 1. Get Social Accounts

Retrieve all social media accounts connected to your Simplified workspace.

**Use case**: Useful for previewing accounts or selecting the correct ID for post publishing.

**Output**:  
Returns a list of connected account objects, including platform, ID, name, and more.

---

### 2. Create Post

Create a new social media post for one of your connected accounts.

**Input Parameters**:

| Field              | Type                                | Required | Description |
|--------------------|-------------------------------------|----------|-------------|
| Action             | Options: Add as Draft, Schedule, Add to Queue | ✅ Yes | Defines how the post should be handled:<br>• Add as Draft – Save the post without publishing.<br>• Schedule – Publish at a specified date/time.<br>• Add to Queue – Add to your platform's posting queue. |
| Network Type       | Options (Facebook, LinkedIn, etc.)  | ✅ Yes   | Target social media platform. |
| Account ID         | Dropdown (auto-loaded)              | ✅ Yes   | Connected account to publish the post to. |
| Message            | String (text area)                  | ❌ No    | The text content of the post. Optional if the post is media-only. |
| Schedule Date      | DateTime                            | ❌ No    | Required only if Action is Schedule. Defines when the post will be published. |
| Media              | List of URLs or Asset IDs           | ❌ No    | Attach media to the post (URLs or Simplified asset IDs). |
| Platform Settings  | Object                              | ❌ No    | Optional advanced configuration for the selected platform. |

**Output**:  
Returns an array containing the post or draft IDs that were created.

```json
[
  {
    "ids": [
      "685d4e9f5cdd5047220f6a43"
    ]
  }
]
```

**Usage in expressions**:
```scss
{{$json["ids"][0]}}
```

---

## Credentials

This node requires authentication with Simplified. You will need an API key to connect your account.

🔗 [Simplified Authentication Documentation](https://simplified.readme.io/reference/authentication)

---

## Compatibility

- Requires **n8n v1.40.0 or higher**
- Developed and tested with Node.js 20+
- No known incompatibilities at this time.

---

## Usage

Use this node to prepare and publish AI-generated content to all your connected social media accounts directly from n8n.

Examples:
- Prepare content with ChatGPT or OpenAI node.
- Use this node to **schedule or queue** posts for Simplified-connected platforms.
- Retrieve and display connected accounts before publishing.

---

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Simplified API documentation](https://simplified.readme.io/reference/authentication)
- [Simplified App](https://simplified.com)

---

## Version history

### 1.0.0
- Initial release
- Supports:
  - Get Social Accounts
  - Create Post with scheduling, media upload, and advanced platform settings
