# n8n-nodes-clicksend

This is an n8n community node. It lets you use the ClickSend REST API in your n8n workflows.

[ClickSend](https://ClickSend.com) 
Business Communications. Solved.
Communicate with your customers and staff like never before via SMS, Email, Rich Media, Direct Mail and more.
From single to scale by web app or API.

There is a massive amount of endpoints available for ClickSend through their REST API. This is not the only API type they have. 

[ClickSend API Docs](https://developers.clicksend.com/docs/rest/v3/)

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Usage](#usage) 
[Resources](#resources)  
[Version history](#version-history) 

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Account
  - Get details
  - Get Usage
- SMS
  - History
  - Calculate SMS price
  - Send SMS
- MMS
  - History
  - Calculate MMS price
  - Send MMS
- Upload
  - Upload binary media file to be converted for use as a URL

## Credentials

This node uses basic HTTP authentication in the headers. `Authorization: Basic API KEY`
The API key is `username:password` Base64 encoded.
See the [oficial documentation](https://developers.clicksend.com/docs/rest/v3/) for more information.

## Compatibility

This is subject to change.

## Usage

Use the node as you would any other, but some tips 
  - Estimating cost for SMS/MMS uses the exact same fields as for sending them. So you should be able to flip back and forth between the different modes easily.
  - You must use the 'upload' operation before sending an MMS UNLESS your media is already a compatible format ([See Docs about that here](https://developers.clicksend.com/docs/rest/v3/?shell#ClickSend-v3-API-Upload))

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [clickuplookup docs and repository](https://github.com/Bwilliamson55/n8n-nodes-clicksend)

## Version history

- 0.1.0 - Initial release
  - Features:
    - Account
      - Get details
      - Get Usage
    - SMS
      - History
      - Calculate SMS price
      - Send SMS
    - MMS
      - History
      - Calculate MMS price
      - Send MMS
    - Upload
      - Upload binary media file to be converted for use as a URL
