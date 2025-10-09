# n8n-nodes-figma  

This is an n8n community node. It lets you interact with Figma in your n8n workflows.  

Figma is a collaborative interface design tool that allows users to create, prototype, and share interactive designs in real time, making it easy to collaborate across teams, iterate quickly, and deliver high-quality user experiences, while providing valuable insights into design workflows, user feedback, and product usability.

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
git clone https://github.com/elevate-agency-data/n8n-nodes-figma.git 
cd n8n-nodes-figma 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need a Figma API key with access to Figma.  

## Operations  

This node supports the following operations within Figma:  

* **Comment**
    - Adds a comment
    - Adds comment reactions
    - Deletes a comment
    - Deletes a comment reaction
    - Gets comment reactions
    - Lists comments
* **Component and Style**
    - Gets a component
    - Gets a component set
    - Gets a style
    - Lists file component sets
    - Lists file components
    - Lists file styles
    - Lists team components
    - Lists team components sets
    - Lists team styles
* **Dev Resource**
    - Creates dev resources
    - Deletes dev resources
    - Gets dev resources
    - Updates dev resources
* **Figma File**
    - Get File
    - Get File Metadata
    - Get File Nodes
    - Get Image
    - Get Image Fills
* **Library Analytics**
    - Lists component actions
    - Lists component usages
    - Lists styles actions
    - Lists styles usages
    - Lists variables actions
    - Lists variables usages
* **Project**
    - Lists project files
    - Lists team projects
* **User**
    - Gets me
* **Variable**
    - Creates, updates or deletes variable
    - Lists local variables
    - Lists published variables
* **Version History**
    - Gets file versions
* **Webhook V2**
    - Creates a webhook
    - Deletes a webhook
    -Gets a webhook
    - Lists webhook requests
    - Lists webhooks
    - Updates a webhook

Retrieve information from the [Figma APIs](https://www.figma.com/developers/api).

## Using as a Tool

This node can be used  as a tool in n8n AI Agents. To enable community nodes as tools, you need to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true`.

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
- [Figma APIs documentation](https://www.figma.com/developers/api)