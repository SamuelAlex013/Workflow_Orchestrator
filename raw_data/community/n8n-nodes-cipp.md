# n8n-nodes-cipp

This is an n8n community node. It lets you use CIPP in your n8n workflows.

CIPP (CyberDrain Improved Partner Portal) is an open-source Microsoft 365 multi-tenant management solution designed for MSPs. It provides centralized user management, standardization tools, security features, and comprehensive reporting across multiple Microsoft 365 tenants.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following operations:

### Calendar Permission
- **List Calendar Permissions**: Retrieve calendar permissions for a specific user.
- **Edit Calendar Permissions**: Modify calendar permissions for users.

### Group
- **Create Or Add Group**: Create a new group or add to existing groups.
- **Edit Group**: Modify group settings, add/remove members and owners.
- **List Groups**: Retrieve a list of groups with optional filtering.

### License
- **Create Or Update Excluded Licenses**: Manage excluded licenses configuration.
- **List Licenses**: Retrieve license information for tenants.

### Tenant
- **Edit Tenant**: Update tenant configuration including alias and groups.
- **Get Tenant**: Retrieve detailed information about a specific tenant.
- **List Shared Mailbox Statistics**: Get statistics for shared mailboxes.
- **List Tenants**: Retrieve a list of all managed tenants.

### User
- **Add Guest**: Invite guest users to tenants.
- **Add User**: Create new users with comprehensive configuration options.
- **Edit User**: Modify user settings, manager, and group memberships.
- **Exec Restore Deleted User**: Restore previously deleted users.
- **List All Users**: Retrieve a complete list of users across all tenants.
- **List User**: Get detailed information about specific users.
- **List User Conditional Access Policies**: View conditional access policies affecting users.
- **List User Counts**: Get user count statistics for tenants.
- **List User Devices**: Retrieve devices associated with users.
- **List User Groups**: Show group memberships for users.
- **Offboard User**: Execute comprehensive user offboarding process.
- **Universal Search**: Search across multiple user-related data sources.

## Credentials

To use this node, you'll need to set up OAuth2 credentials with CIPP. Here's how:

1. **Access your CIPP Portal**:
   - Log in to your CIPP instance
   - Navigate to **CIPP** > **Integrations** > **CIPP-API**
   - Create a new integration or use existing API settings

2. **Azure AD Application Setup**:
   - Create an Azure AD application in your tenant
   - Note down the Client ID and Client Secret
   - Configure the application with appropriate API permissions
   - Set up the redirect URIs as required

3. **In n8n**:
   - Create new credentials for "CIPP OAuth2 API"
   - Enter the following information:
     - **Access Token URL**: `https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token`
     - **API URL**: Your CIPP instance URL (e.g., `https://cippxyz123.azurewebsites.net`)
     - **Scope**: `api://CLIENT_ID/.default` (replace CLIENT_ID with your Azure AD application client ID)
     - **Client ID**: Your Azure AD application client ID
     - **Client Secret**: Your Azure AD application client secret
   - Save the credentials

For detailed setup instructions, refer to the [CIPP API Documentation](https://docs.cipp.app/api-documentation/setup-and-authentication).

## Compatibility

This node is compatible with n8n version 1.0.0 and above.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [CIPP](https://cipp.app/)
* [CIPP Documentation](https://docs.cipp.app/)
* [CIPP GitHub Repository](https://github.com/KelvinTegelaar/CIPP)
* [CIPP API Documentation](https://docs.cipp.app/api-documentation/setup-and-authentication)


