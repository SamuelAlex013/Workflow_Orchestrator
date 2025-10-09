# n8n-nodes-erply-api

This is an n8n community node. It lets you use the Erply API, Service APIs and webhook triggers in your n8n workflows.

Erply is a multi store, retail chain and franchise point-of-sale platform.


[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)   
[Credentials](#credentials)    
[Compatibility](#compatibility)  
[Usage](#usage)   
[Limitations](#limitations)      
[Resources](#resources)        

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Credentials

Ensure that your Erply user has API access enabled. Some service endpoints (such as CDN) may require a JWT to be used instead of the default sessionKey. Additionally some service endpoints may incorrectly return an authentication error when using a JWT instead of sessionKey. You will have more success if you use the auth without JWT for all requests unless you're specificially required to use it.

## Compatibility

Tested on version 1.47.1

## Usage

<img width="633" alt="image" src="https://github.com/ashleygeorgeclarke/n8n-nodes-erply-api/assets/4650777/a71a2ad4-921a-40a3-ac11-bba77b7c59c2">

Some API endpoints might return the desired array behind an object root.

```
{
	someInfo: "string",
	actualData: [{}]
}
```
In this case, use the (JMES Path)[https://jmespath.org/] field to return the desired data.

### Erply API

Any calls to the [https://*.erply.com/api](https://learn-api.erply.com/requests) endpoint are handled by the Erply API node.

### Erply Service

All service APIs (PIM, inventory etc) are handled by Erply Service.

<img width="645" alt="image" src="https://github.com/ashleygeorgeclarke/n8n-nodes-erply-api/assets/4650777/80a4aa1c-c51f-4dfb-81a5-1b00e3841425">

The Endpoint Path Select options are dynamically fetched from the respective service api swagger doc json files. The use of this is simply a convenience and is not strictly necessary to use. 

![image](https://github.com/ashleygeorgeclarke/n8n-nodes-erply-api/assets/4650777/5e8a8061-be5d-486f-81db-d896ea20e3e1)

If the path contains a replacable components ({ids} etc), use .replace("{ids}", "myvalue") to set the desired values.

### Erply Trigger

[These webhooks](https://wiki.erply.com/en/article/760-introduction) will be dynamically created/destroyed, so there's no need to create them manually before use.

## Limitations

All authenticated requests get a new sessionKey and are not reused even though an expiry is provided. Erply returns status code 400 when a sessionKey is expired. A current limitation of n8n requires a 401 response to trigger a token refresh.

ErplyService should use [getServiceEndpoints](https://learn-api.erply.com/new-apis) as an input to list the correct endpoint base URLs for your account code. According to Erply, these service endpoints can change without prior notice.

Rate limiting is not currently handled.

Pagination is not currently supported, however using the take parameter for the service endpoints will return 100,000 results.

Currently some of the Erply service endpoint swagger json definition files are not returning valid json and will result in the 'endpoint path select' field unable to load options.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Erply API documentation](https://learn-api.erply.com/)


