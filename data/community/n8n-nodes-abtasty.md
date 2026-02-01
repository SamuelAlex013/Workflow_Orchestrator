# n8n-nodes-abtasty  

This is an n8n community node. It lets you interact with AB Tasty in your n8n workflows.  

AB Tasty specializes in experience optimization, offering solutions for A/B testing, personalization, and user engagement to boost marketing performance and drive business growth.

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
git clone https://github.com/elevate-agency-data/n8n-nodes-abtasty.git 
cd n8n-nodes-abtasty 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need an AB Tasty API key with access to AB Tasty.  

## Operations  

This node supports the following operations within AB Tasty:  

* **Data Explorer API**
    - Sends a query
* **Public API**
    - Changes an access to a user
    - Deletes the ab tasty script
    - Gets a user of an account
    - Gets information of one test
    - Gets one specific modification
    - Gets one specific variation
    - Gets the framework checksum
    - Gets thid party tool link of one test
    - Gives an access to a user
    - Lists all modifications of a variation
    - Lists all tests of an account
    - Lists all third party tool links of one test
    - Lists events set up in a test
    - Lists tests statistics of an account
    - Lists the variations of a test
    - Lists users of an account
    - Pauses a test
    - Plays a test
    - Revokes an access to a user
    - Updates the ab tasty script
* **Universal Data Connector API**
    - List Visitor Segments
    - Upload Segments

Retrieve information from the [AB Tasty API](https://developers.abtasty.com/docs/data/data-getting-started). 

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

- Tested with: 1.84.1 (Success)

## Resources  

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)  
- [AB Tasty API documentation](https://developers.abtasty.com/docs/data/data-getting-started)