# @flagbit/n8n-nodes-msgraph - Multi-Tenant Microsoft Graph Node for N8N

This repository provides a custom N8N node for interacting with the Microsoft Graph API across **multiple tenants**, based on a fork of [`advenimuss-n8n-nodes-msgraph`](https://github.com/advenimus/n8n-nodes-msgraph). It extends the original node by allowing dynamic data retrieval from **many Microsoft tenants** using a **multi-tenant Azure app registration**.


## ⚙️ Prerequisites

Before you begin, you’ll need:

- An [Azure AD multi-tenant app](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant)
- Appropriate Microsoft Graph API permissions
- An N8N instance

## 🔐 Setting Up a Multi-Tenant App in Azure

To configure your Azure AD app for multi-tenant access:

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Azure Active Directory** > **App registrations**.
3. Click **New registration**.
4. Set the **Supported account types** to:  
   > ✅ *Accounts in any organizational directory (Any Azure AD directory - Multitenant)*
5. After registration:
   - Copy the **Application (client) ID**
   - Copy the **Directory (tenant) ID**
6. Go to **Certificates & secrets** and:
   - Create a **client secret** or upload a **certificate** for authentication.
7. In **API permissions**, add the required Microsoft Graph permissions (e.g., `User.Read.All`, `Group.Read.All`) and **grant admin consent**.
8. Share the **consent URL** with each tenant admin so they can authorize your app.


## 🚀 Basic Usage

1. **Install the NPM package** in your N8N instance using your preferred method (e.g., cloning the repo into your custom nodes directory).
2. **Restart N8N** to load the new node.
3. **Add the Microsoft Graph (Multi-Tenant)** node to your workflow.
4. **Provide a Tenant ID**:
   - Dynamically using expressions or looping over a list of tenant IDs.
   - Or statically by hardcoding a single tenant ID if only one is required.
5. **Configure the desired action** (e.g., list users, get groups, send email).
6. **Optionally add custom headers** for advanced API scenarios (e.g., API version, consistency level, preferences).
7. **Execute the workflow** to fetch data from the Microsoft Graph API.

## 📄 License

This project is licensed under the **MIT License**.

It is a fork of the original [advenimus/n8n-nodes-msgraph](https://github.com/advenimus/n8n-nodes-msgraph) project and includes modifications to support multi-tenant Microsoft Graph access in N8N.

See the [LICENSE](./LICENSE) file for full license details.
