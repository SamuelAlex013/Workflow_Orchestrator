# n8n-nodes-googleforms  

This is an n8n community node. It lets you interact with Google Forms in your n8n workflows.  

Google Forms is a survey and data collection tool that allows users to create customizable forms and questionnaires, making it easy to gather information, conduct surveys, and analyze responses in real-time, providing valuable insights into user feedback, preferences, and operational data.

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
git clone https://github.com/elevate-agency-data/n8n-nodes-googleforms.git 
cd n8n-nodes-googleforms 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need a Google Cloud API key with access to Google Forms.  

## Operations  

This node supports the following operations within Google Forms:  

* **Form**
    - Changes the form with a batch of updates
    - Creates a new form
    - Gets a form
    - Updates the publish settings
* **Form Response**
    - Gets a response 
    - Lists responses
* **Form Watch**
    - Creates a new watch
    - Deletes a watch
    - Lists watches
    - Renews a watch

Retrieve information from the [Google Forms APIs](https://developers.google.com/workspace/forms/api/reference/rest?hl=en). 

### Steps to obtain API credentials:  

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new project or use an existing one  
3. Enable the **Google Forms API**  
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
- [Google Forms APIs documentation](https://developers.google.com/workspace/forms/api/reference/rest?hl=en)