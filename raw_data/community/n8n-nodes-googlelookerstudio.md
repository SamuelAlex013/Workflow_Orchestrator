# n8n-nodes-googlelookerstudio  

This is an n8n community node. It lets you interact with Google Looker Studio in your n8n workflows.  

Google Looker Studio is a data visualization and reporting tool that allows users to create interactive dashboards and reports by connecting to various data sources, including Google Looker Studio, providing clear insights into performance, user behavior, and business metrics.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.  

[Installation](#installation)  
[Credentials](#credentials)    
[Operations](#operations)   
[Using as a Tool](#using-as-a-tool)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation  

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.  

Alternatively, you can manually install it:  

```sh  
git clone https://github.com/elevate-agency-data/n8n-nodes-googlelookerstudio.git 
cd n8n-nodes-googlelookerstudio 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need a Google Cloud API key with access to Google Looker Studio.  

## Operations  

This node supports the following operations within Google Looker Studio:  

* **Asset**
    - Searches an user Looker Studio asset
* **Permission**
    - Adds members to a Looker Studio asset
    - Gets the permissions for a Looker Studio asset
    - Removes members from a Looker Studio asset
    - Updates permissions for a Looker Studio asset

Retrieve information from the [Google Looker Studio APIs](https://developers.google.com/looker-studio/integrate/api/reference?hl=en). 

### Steps to obtain API credentials:  

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new project or use an existing one  
3. Enable the **Google Looker Studio API**  
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
- [Google Looker Studio APIs documentation](https://developers.google.com/looker-studio/integrate/api/reference?hl=en)