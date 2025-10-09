# n8n-nodes-scoro 🚀

This is an n8n community node. It lets you use **[Scoro](https://www.scoro.com/)** in your n8n workflows.

> Scoro is an end-to-end work management software designed for service-based businesses like consultancies, agencies, and IT firms. The cloud-based platform integrates projects, resources, sales, and finances into a single system, eliminating the need to switch between different applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation-💾)
[Operations](#operations-✨)
[Credentials](#credentials-🔑)
[Compatibility](#compatibility-📦)
[Resources](#resources-📚)
[Version history](#version-history-📜)

<!-- [Usage](#usage-💻) -->

## Installation 💾

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations ✨

The **Scoro** node supports a variety of operations across different resources:

| Resource           | Create | Get | Get Many | Update | Delete | Set Done |
| :----------------- | :----: | :-: | :------: | :----: | :----: | :------: |
| **Calendar**       |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Client Profile** |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Comment**        |   ✅   |     |    ✅    |   ✅   |   ✅   |          |
| **Company**        |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Invoice**        |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Project**        |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Role**           |        | ✅  |    ✅    |        |        |          |
| **Status**         |        |     |    ✅    |        |        |          |
| **Task**           |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **Time Entry**     |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |    ✅    |
| **Trigger**        |   ✅   | ✅  |    ✅    |   ✅   |   ✅   |          |
| **User**           |        | ✅  |    ✅    |        |        |          |

## Credentials 🔑

To use the Scoro node, you need to:

1.  Sign up for a scoro account at [https://www.scoro.com/](https://www.scoro.com/).
2.  Get your Company Account ID, API key, and Base URL from your Scoro account settings.
3.  In n8n, add the following to the node's credentials:
    - **Company Account ID**: Your Scoro company account ID, found in your Scoro URL (e.g., `your-company.scoro.com`).
    - **API Key**: The API key for your Scoro account.
    - **Base URL**: The URL for the Scoro API.

The node authenticates by sending these credentials in the body of a POST request.

> ⚠️ Do not share your API key or other sensitive information with anyone who does not have permission to access it. Keep them secure! 🔒

## Compatibility 📦

- Minimum n8n version: `1.0.0`
- Tested against n8n versions: `1.0.0`
- Node.js version: `18` or higher

<!-- ## Usage 💻 -->

<!-- This section is optional. It is recommended for developers to add an example of a workflow that uses the node to showcase its functionalities. -->

## Resources 📚

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Official Scoro API documentation](https://api.scoro.com/api/v2)

## Version history 📜

- **Version 0.2.1**: Updated README to the reflect the`Comment` resource update.
- **Version 0.2.0**: Added the `Comment` resource with create, get many, update, and delete operations.
- **Version 0.1.0**: Initial release of the community node.
