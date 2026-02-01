# n8n-nodes-googleanalytics  

This is an n8n community node. It lets you interact with Google Analytics in your n8n workflows.  

Google Analytics is a web analytics service that allows users to track and analyze website and app performance, providing insights into user behavior, traffic sources, and conversions.

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
git clone https://github.com/elevate-agency-data/n8n-nodes-googleanalytics.git 
cd n8n-nodes-googleanalytics 
npm install  
```  

Then, place the node file in the `~/.n8n/custom-nodes` directory (or follow instructions specific to your n8n installation).   

## Credentials  

To use this node, you need a Google Cloud API key with access to Google Analytics.  

## Operations  

This node supports the following operations within Google Analytics:  

* **Admin API (v1alpha)**
    - **Account**
        - Marks target account as soft-deleted (ie: "trashed") and returns it
        - Lookup for a single account
        - Gets data sharing settings on an account
        - Returns all accounts accessible by the caller
        - Updates an account
        - Requests a ticket for creating an account
        - Returns a customized report of data access records
        - Searches through all changes to an account or its children given the specified set of filters
    - **Account Access Binding**
        - Creates information about multiple access bindings
        - Deletes information about multiple access bindings
        - Gets information about multiple access bindings
        - Updates information about multiple access bindings
        - Creates an access binding
        - Deletes an access binding
        - Gets information about an access binding
        - Lists all access bindings
        - Updates an access bindingBatch Create Account Access Bindings
    - **Account Summary**
        - Returns summaries of all accounts accessible by the caller
    - **AdSense Link**
        - Creates an adsense link
        - Deletes an adsense link
        - Gets an adsense link
        - Lists an adsense link
    - **Audience**
        - Archives an audience
        - Creates an audience
        - Gets an audience
        - Lists audiences
        - Updates an audience
    - **BigQuery Link**
        - Creates a bigquery link
        - Deletes a bigquery link
        - Gets a bigquery link
        - Lists bigquery links
        - Updates a bigquery link
    - **Calculated Metric**
        - Creates a calculated metric
        - Deletes a calculated metric
        - Gets a calculated metric
        - Lists calculated metrics
        - Updates a calculated metric
    - **Channel Group**
        - Creates a channel group
        - Deletes a channel group
        - Gets a channel group
        - Lists channel groups
        - Updates a channel group
    - **Custom Dimension**
        - Archives a custom dimension
        - Create a custom dimension
        - Gets a custom dimension
        - Lists custom dimensions
        - Updates a custom dimension
    - **Custom Metric**
        - Archives a custom metric
        - Create a custom metric
        - Gets a custom metric
        - Lists custom metrics
        - Updates a custom metric
    - **Data Stream**
        - Creates a data stream
        - Deletes a data stream
        - Gets a data stream
        - Gets data redaction settings
        - Gets enhanced measurement settings
        - Gets a global site tag
        - Lists data streams
        - Updates a data streams
        - Updates data redaction settings
        - Updates enhanced measurement settings
    - **Display & Video 360 Advertiser Link**
        - Creates a display and video 360 advertiser link
        - Deletes a display and video 360 advertiser link
        - Gets a display and video 360 advertiser link
        - Lists display and video 360 advertiser links
        - Updates a display and video 360 advertiser link
    - **Display & Video 360 Advertiser Link Proposal**
        - Approves a display and video 360 advertiser link proposal
        - Cancels a display and video 360 advertiser link proposal
        - Creates a display and video 360 advertiser link proposal
        - Deletes a display and video 360 advertiser link proposal
        - Gets a display and video 360 advertiser link proposal
        - Lists display and video 360 advertiser link proposals
    - **Event Create Rule**
        - Creates an event create rule
        - Deletes an event create rule
        - Gets an event create rule
        - Lists event create rules
        - Updates an event edit rule
    - **Event Edit Rule**
        - Creates an event edit rule
        - Deletes an event edit rule
        - Gets an event edit rule
        - List event edit rules
        - Updates an event edit rule
        - Reorders event edit rules
    - **Expanded Data Set**
        - Creates an expanded data set
        - Deletes an expanded data set
        - Gets an expanded data set
        - Lists expanded data sets
        - Updates an expanded data set
    - **Firebase Link**
        - Creates a firebase link
        - Deletes a firebase link
        - Lists firebase links
    - **Google Ads Link**
        - Creates a google ads link
        - Deletes a google ads link
        - Lists google ads links
        - Updates google ads links
    - **Key Event**
        - Creates a key event
        - Deletes a key event
        - Gets a key event
        - Lists key events
        - Updates a key event
    - **Measurement Protocol Secret**
        - Creates a measurement protocol secret
        - Deletes a measurement protocol secret
        - Gets a measurement protocol secret
        - Lists measurement protocol secrets
        - Updates a measurement protocol secret
    - **Property**
        - Acknowledges the terms of user data collection for the specified property
        - Creates a connected site tag for a universal analytics property
        - Creates a property with the specified location and attributes
        - Create a roll-up property and all roll-up property source links
        - Deletes a connected site tag for a universal analytics property
        - Marks target property as soft-deleted (ie: "trashed") and returns it
        - Fetches the opt out status for the automated GA4 setup process for a universal Analytics property
        - Given a specified universal analytics property, looks up the ga4 property connected to it
        - Gets a single property
        - Gets attribution settings
        - Gets data retention settings
        - Gets google signals settings
        - Lists the connected site tags for a universal analytics property
        - List properties under the specified parent account
        - Updates a property
        - Create a subproperty and a subproperty event filter that applies to the created subproperty
        - Returns a customized report of data access records
        - Sets the opt out status for the automated ga4 setup process
        - Updates attribution settings
        - Updates data retention settings
        - Updates a google signals settings
    - **Property Access Binding**
        - Creates information about multiple access bindings
        - Deletes information about multiple access bindings
        - Gets information about multiple access bindings
        - Updates information about multiple access bindings
        - Creates an access binding
        - Deletes an access binding
        - Gets information about an access binding
        - Lists all access bindings
        - Updates an access binding
    - **Reporting Data Annotation**
        - Deletes a reporting data annotation
        - Gets a reporting data annotation
        - Lists reporting data annotations
        - Updates a reporting data annotation
    - **Rollup Property Source Link**
        - Creates a rollup property source link
        - Deletes a rollup property source link
        - Gets a rollup property source link
        - Lists rollup property source links
    - **Search Ads 360 Link**
        - Creates a search ads 360 link
        - Deletes a search ads 360 link
        - Gets a search ads 360 link
        - Lists search ads 360 links
        - Updates a search ads 360 link
    - **SKAdNetwork Conversion Value Schema**
        - Creates a skadnetwork conversion value schema
        - Deletes a skadnetwork conversion value schema
        - Gets a skadnetwork conversion value schema
        - Lists skadnetwork conversion value schemas
        - Updates a skadnetwork conversion value schema
    - **Subproperty Event Filter**
        - Creates a subproperty event filter
        - Deletes a subproperty event filter
        - Gets a subproperty event filter
        - LIsts subproperty event filters
        - Updates a subproperty event filter
* **Admin API (v1beta)**
    - **Account**
        - Deletes an account
        - Gets an account
        - Gets account data sharing settings
        - Lists accounts
        - Updates an account
        - Requests a ticket for creating an account
        - Runs an access report
        - Searches through all changes to an account or its children given the specified set of filters
    - **Account Summary**
        - Returns summaries of all accounts accessible by the caller
    - **Custom Dimension**
        - Archives a custom dimension
        - Create a custom dimension
        - Gets a custom dimension
        - Lists custom dimensions
        - Updates a custom dimension
    - **Custom Metric**
        - Archives a custom metric
        - Create a custom metric
        - Gets a custom metric
        - Lists custom metrics
        - Updates a custom metric
    - **Data Stream**
        - Creates a data stream
        - Deletes a data stream
        - Gets a data stream
        - Lists data streams
        - Updates a data stream
    - **Firebase Link**
        - Creates a firebase link
        - Deletes a firebase link
        - Lists firebase links
    - **Google Ads Link**
        - Creates a google ads link
        - Deletes a google ads link
        - Lists google ads links
        - Updates google ads links
    - **Key Event**
        - Creates a key event
        - Deletes a key event
        - Gets a key event
        - Lists key events
        - Updates a key event
    - **Measurement Protocol Secret**
        - Creates a measurement protocol secret
        - Deletes a measurement protocol secret
        - Gets a measurement protocol secret
        - Lists measurement protocol secrets
        - Updates a measurement protocol secret
    - **Property**
        - Acknowledges the terms of user data collection for the specified property
        - Creates a property with the specified location and attributes
        - Marks target property as soft-deleted (ie: "trashed") and returns it
        - Gets a single property
        - Gets data retention settings
        - List properties under the specified parent account
        - Returns a customized report of data access records
        - Updates a property
        - Updates a data retention settings on a property
* **Data (v1alpha)**
    - **Audience List**
        - Creates an audience list
        - Exports an audience list of users to a google sheet
        - Gets an audience list
        - Lists audience lists
        - Retrieves an audience list
    - **Property**
        - Gets all property quotas
        - Runs a funnel report
    - **Recurring Audience List**
        - Creates a recurring audience list
        - Gets a recurring audience list
        - Lists recurring audience lists
    - **Report Task**
        - Creates a report task
        - Gets a report task
        - Lists report tasks
        - Retrieves a report task
* **Data (v1beta)**
    - **Audience Export**
        - Creates an audience export
        - Gets an audience export
        - Lists audience exports
        - Retrieves an audience export
    - **Property**
        - Runs pivot reports in a batch
        - Runs reports in a batch
        - Checks for compatibility of dimensions and metrics
        - Gets metadata
        - Runs a pivot report
        - Runs a realtime report
        - Runs a report
* **User Deletion API**
    - Insert or update a user deletion request.

Retrieve information from the [Google Analytics APIs](https://developers.google.com/analytics/devguides/limits-and-quotas?hl=en). 

### Steps to obtain API credentials:  

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new project or use an existing one  
3. Enable the **Google Analytics API**  
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
- [Google Analytics APIs documentation](https://developers.google.com/analytics/devguides/limits-and-quotas?hl=en)