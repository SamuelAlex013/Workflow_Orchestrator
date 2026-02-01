# n8n-nodes-azure-messagebus

This is an n8n community node. It lets you use the azure messagebus in your n8n workflows.

This is a very basic implementation that only allows you to send to a specific endpoint as part of configuration of the node

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

send message to azure messagebus 

## Credentials

use your connectionString to the message bus in the format:
``` Endpoint=sb://<HOSTNAME>.servicebus.windows.net/;SharedAccessKeyName=<SHAREDKEYNAME>;SharedAccessKey=<SHAREDKEY>;  ```

Note the ; at the end of the line

## Compatibility

Tested on 1.6.1

## Usage



_By the time users are looking for community nodes, they probably already know n8n basics. But if you expect new users, you can link to the [Try it out](https://docs.n8n.io/try-it-out/) documentation to help them get started._

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview

## Version history

v0.0.1 - basic funcionality.  no q change ability to make the node faster


