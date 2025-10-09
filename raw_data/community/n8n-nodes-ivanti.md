# n8n-nodes-ivanti

This is an n8n community node package. It allows you to use Ivanti Service Manager (ISM) in your n8n workflows.

This node enables interaction with your on-premise Ivanti installation's API, allowing you to automate tasks related to incidents, changes, users, and other Ivanti business objects via its OData API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Supported Operations](#supported-operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Supported Operations

This node supports the following Ivanti resources and operations:

*   **Change**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update
*   **Custom Business Object**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update
*   **Employee**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update
*   **Event**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update
*   **Incident**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update
*   **Task**
    *   Create
    *   Delete
    *   Get
    *   Get Count
    *   Get Many
    *   Link
    *   Update

## Credentials

To use this node, you need to configure Ivanti API credentials in n8n.

1.  **API Key:**
    *   You will need to generate an API key within your Ivanti Service Manager instance. This is typically done through the administrator interface.
    *   Log in to Ivanti Service Manager as an Administrator.
    *   Navigate to the Configuration Console by clicking the Wrench icon (Configure Application).
    *   Go to **Security Controls** > **API Keys**.
    *   Select an existing **Key Group** (like `rest_api_key_group`) or create a new one.
    *   Within the group, click **Add New Key**. Provide a **Name** (e.g., `n8n-integration`) and select an appropriate **Role** (often `Admin` or a dedicated API role).
    *   Click **Save Key**.
    *   Copy the **Generated Key** shown. This is your API key.
2.  **Base URL:**
    *   This is the main URL of your Ivanti instance used to access the API.
    *   For example: `https://yourcompany.ivanti-itsm.com` or `https://ivanti.yourcompany.com`.
    *   **Important:** The URL should be provided *without* the `/HEAT/api/...` suffix. The node will add this part automatically.

When creating the credentials in n8n, enter the obtained API key and your Ivanti instance's Base URL into the respective fields.

## Compatibility

This node was developed using n8n Nodes API version 1. It should work with most recent n8n versions, but using n8n v1.0.0 or newer is recommended.

Tested with Ivanti Service Manager (ISM) version: **2024**

## Resources

*   [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
*   [Ivanti Service Manager API Documentation (Web Service API - includes OData/REST)](https://help.ivanti.com/ht/help/en_US/ISM/2024/admin/Content/Configure/API/Web_Service_API.htm)
*   [Ivanti Service Manager OData API Syntax Reference](https://help.ivanti.com/ht/help/en_US/ISM/2024/admin/Content/Configure/API/OData-API-Syntax.htm)
