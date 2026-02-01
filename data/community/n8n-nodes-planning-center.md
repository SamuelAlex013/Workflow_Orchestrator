# n8n-nodes-planning-center

This is an n8n community node. It interacts with the Planning Center API to work with your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Calendar

#TODO

### Check-Ins

#TODO

### Giving

#TODO

### Groups

#TODO

### People

* Create a person (Creates a Person)
* Delete a person (Delete a person, requires Person ID)
* Get a person (Return person object, requires Person ID)
* Get field definition (Get a field definition, requires Field Definition Name or ID from dropdown)
* Get many people (Return people objects based on given parameters)
* Update a person (Updates given fields, requires ID)

#TODO add planned operations

### Publishing

* Create an episode (Creates episode, requires Channel Name or ID from dropdown)
* Get a channel (Return channel object, requires Channel Name or ID from dropdown)
* Get a series (Return series object, requires Series Name or ID from dropdown)
* Get a speaker (Return speaker object, requires Speaker Name or ID from dropdown)
* Get an episode (Return episode object, requires Episode ID)
* Get many channels (Return channel objects based on given parameters)
* Get many episodes (Return episode objects based on given parameters)
* Get many series (Return series objects based on given parameters)
* Get many speakers (Return speaker objects based on given parameters)

#TODO add planned operations

### Registrations

#TODO

### Services

#TODO

## Credentials

Planning Center uses [two types of authentication](https://developer.planning.center/docs/#/overview/authentication), Personal Access Tokens (PATs) and OAuth2. The current credential type integrated into n8n is OAuth2. Developers can connect an application by going to the [OAuth Portal](https://api.planningcenteronline.com/oauth/applications) and creating an OAuth Application for n8n.

* **Application Name**: n8n
* **Application Type**: Confidential
* **Application Description**: n8n
* Enter Email
* Enter both URL and Support URL
* Enter the Authorization Callback URL as shown by n8n
  * Self-Hosting: `https://subdomain.domain.tld/rest/oauth2-credential/callback`
  * Local Testing with `n8n start`: `http://localhost:5678/rest/oauth2-credential/callback`
* Choose API versions, newest by default

## Compatibility

* Tested with n8n Version: 1.104.2

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
