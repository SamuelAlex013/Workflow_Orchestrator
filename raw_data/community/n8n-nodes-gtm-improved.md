# n8n-nodes-gtm-improved  

This is an improved n8n community node for Google Tag Manager (GTM). It lets you interact with GTM in your n8n workflows with better data structure and direct array returns.

## 🚀 Improvements over original:
- **Direct array returns** - No more nested response objects
- **Cleaner data structure** - Arrays come directly without wrapper objects  
- **Better user experience** - Data ready to use immediately

Google Tag Manager is a tag management system that allows users to quickly and easily update tags and code snippets on their websites or mobile apps.  

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.  

[Installation](#installation)  
[Credentials](#credentials)    
[Operations](#operations)   
[Using as a Tool](#using-as-a-tool)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation  

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.  

Install via npm:
```bash
npm install n8n-nodes-gtm-improved
```

Or install directly in n8n using the package name: `n8n-nodes-gtm-improved`

Source code available at:
```sh  
git clone https://github.com/marcosvb1/n8n-nodes-gtm-improved.git 
cd n8n-nodes-gtm-improved 
npm install  
```   

## Credentials  

This node uses Google OAuth2 (single-service) credentials for Google Tag Manager. Create OAuth credentials and configure them in n8n using the built-in Google OAuth single-service credential type.  

Reference: https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service  

## Operations  

This node supports the following operations within Google Tag Manager:  

* **Account**
    - Gets an account
    - List all accounts
    - Updates an account
* **Built-In Variable**
    - Create a built-in variable
    - Delete a built-in variable
    - Lists all the enabled built-in variables
    - Reverts changes to a built-in variable
* **Client**
    - Creates a client
    - Deletes a client
    - Gets a client
    - Lists all clients
    - Reverts changes to a client
    - Updates a client
* **Container**
    - Combines containers
    - Creates a container
    - Deletes a container
    - Gets a container
    - Lists all containers
    - Looks up a container
    - Move tag ID out of a container
    - Gets the tagging snippet for a container
    - Updates a container
* **Destination**
    - Gets a destination
    - Adds a destination
    - Lists all destinations
* **Environment**
    - Creates an environment
    - Deletes an environment
    - Gets an environment
    - Lists all environments
    - Re-generates the authorization code for an environment
    - Updates an environment
* **Folder**
    - Creates a folder
    - Deletes a folder
    - List all entities in a folder
    - Gets a folder
    - Lists all folders
    - Moves entities to a folder
    - Reverts changes to a folder
    - Updates a folder
* **Google Tag Configuration**
    - Creates a google tag config
    - Deletes a google tag config
    - Gets a google tag config
    - Lists all google tag configs
    - Updates a google tag config
* **Tag**
    - Creates a tag
    - Deletes a tag
    - Gets a tag
    - Lists all tags
    - Reverts changes to a tag
    - Updates a tag
* **Template**
    - Creates a custom template
    - Deletes a template
    - Gets a template
    - Imports a template from gallery
    - Lists all templates
    - Reverts changes to a template
    - Updates a templates
* **Transformation**
    - Creates a transformation
    - Deletes a transformation
    - Gets a transformation
    - Lists all transformations
    - Reverts changes to a transformation
    - Updates a transformation
* **Trigger**
    - Creates a trigger
    - Deletes a trigger
    - Gets a trigger
    - Lists all triggers
    - Reverts changes to a trigger
    - Updates a trigger
* **User Permission**
    - Creates a user's permissions
    - Remove a user's permissions
    - Gets a user's permissions
    - Lists all users that have access
    - Updates a user's permissions
* **Variable**
    - Creates a variable
    - Deletes a variable
    - Gets a variable
    - Lists all variables
    - Reverts changes to a variable
    - Updates a variable
* **Version Header**
    - Gets the latest container version header
    - Lists all container versions
* **Version**
    - Deletes a version
    - Gets a version
    - Gets the live version
    - Publishes a version
    - Sets the latest versions
    - Undeletes a version
    - Updates a version
* **Workspace**
    - Creates a workspace
    - Creates a container version from the entities present in the workspace
    - Deletes a workspace
    - Finds conflicting and modified entities in the workspace
    - Gets a workspace
    - Lists all workspaces
    - Quick previews a workspace
    - Resolves a merge conflict for a workspace entity
    - Syncs a workspace to the latest container version
    - Updates a workspace
* **Zone**
    - Creates a zone
    - Deletes a zone
    - Gets a zone
    - Lists all zones
    - Reverts changes to a zone
    - Updates a zone

Retrieve information from the [GTM API](https://developers.google.com/tag-platform/tag-manager/api/v2?hl=fr). 

### Steps to obtain API credentials:  

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new project or use an existing one  
3. Enable the **Google Tag Manager API**  
4. Create API credentials (API key or OAuth 2.0)  
5. Add your API key to the authentication settings in n8n  

## Using as a Tool

This node can be used as a tool in n8n AI Agents. To enable community nodes as tools, you need to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true`.

### Setting the Environment Variable

**If you're using a bash/zsh shell:**
```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
n8n start
```

**If you're using Docker:**
Add to your docker-compose.yml file:
```yaml
environment:
  - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

**If you're using the desktop app:**
Create a `.env` file in the n8n directory:
```
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

**If you want to set it permanently on Mac/Linux:**
Add to your `~/.zshrc` or `~/.bash_profile`:
```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

## Compatibility  

- Tested with: 1.80.5 (Success)

## Resources  

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)  
- [Google Tag Manager API documentation](https://developers.google.com/tag-platform/tag-manager/api/v2)