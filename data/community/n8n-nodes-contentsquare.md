# n8n-nodes-contentsquare  

This is an n8n community node. It lets you interact with Contentsquare in your n8n workflows.  

Contentsquare specializes in digital experience analytics, providing insights into user behavior to optimize website performance, enhance customer journeys, and drive business growth.

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
git clone https://github.com/elevate-agency-data/n8n-nodes-contentsquare.git 
cd n8n-nodes-contentsquare 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need an Contentsquare API key with access to Contentsquare.  

## Operations  

This node supports the following operations within Contentsquare:  

* **Data Export API**
    - Creates an export job 
    - Gets a specific job
    - Gets a specific job run
    - Lists all custom variables
    - Lists all dynamic variables
    - Lists all export jobs
    - Lists all exportable fields
    - Lists all job runs of a job
    - Lists all successful job runs
* **Metrics API**
    - Gets page activity rate
    - Gets page bounce rate
    - Gets page conversion rate
    - Gets page exit rate
    - Gets page fold height
    - Gets page height
    - Gets page interaction time
    - Gets page landing rate
    - Gets page scroll rate
    - Gets page time spent
    - Gets page unique visits
    - Gets page views
    - Gets page views per visit
    - Gets page visits
    - Gets page web vitals
    - Gets site bounce rate
    - Gets site cart average
    - Gets site conversion rate
    - Gets site conversions
    - Gets site pageview average
    - Gets site revenue
    - Gets site session time average
    - Gets site visits
    - Gets zone attractiveness rate
    - Gets zone click rate
    - Gets zone click recurrence
    - Gets zone conversion rate per click
    - Gets zone conversion rate per hover
    - Gets zone conversion rate per tap
    - Gets zone engagement rate
    - Gets zone exposure rate
    - Gets zone exposure time
    - Gets zone hesitation time
    - Gets zone hover rate
    - Gets zone hover time
    - Gets zone number of clicks
    - Gets zone revenue
    - Gets zone revenue per click
    - Gets zone revenue per tap
    - Gets zone swipe rate
    - Gets zone swipe rate recurrence
    - Gets zone tap before first tap
    - Gets zone tap rate
    - Gets zone tap recurrence
    - Gets zone time before first click
    - Lists all goals for a project
    - Lists all mappings for a project
    - Lists all page groups for a specific mapping
    - Lists all page groups metrics between two dates
    - Lists all segments for a project
    - Lists all site metrics between two dates
    - Lists all zone metrics between two dates
    - Lists all zones for a zoning
    - Lists all zonings for a page group
* **Speed Analysis API**
    - Creates an event
    - Deletes an event
    - Gets a list of events
    - Gets a scenario report
    - Gets an analysis report
    - Gets analysis HAR from an analysis
    - Gets scenario HAR from an analysis
    - Gets the list of monitorings
    - Gets the list of scenarios
    - Gets the monitoring last report
    - Gets the monitoring reports
    - Gets the scenario reports
    - Gets the scenario step report

Retrieve information from the [Contentsquare API](https://docs.contentsquare.com/en/api/export/). 

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
- [Contentsquare API documentation](https://docs.contentsquare.com/en/api/export/)