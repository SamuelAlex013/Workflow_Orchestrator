# n8n-nodes-_node-name_

This is an n8n community node. It lets you use [MeshCentral](https://github.com/Ylianst/MeshCentral) in your n8n workflows.

MeshCentral is a full computer management web site. With MeshCentral, you can run your own web server to remotely manage and control computers on a local network or anywhere on the internet. Once you get the server started, create device group and download and install an agent on each computer you want to manage. A minute later, the new computer will show up on the web site and you can take control of it. MeshCentral includes full web-based remote desktop, terminal and file management capability.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[How it works](#how-it-works)
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation. Remember to restart your n8n instance after updating community node(s).

## Operations

At the moment it runs every meshctrl command except: showevents, upload, download, agentdownload. It always returns a JSON response. Responses that don't contain data appear in a `{result}` key.

Beware that this node accepts a single input, which may provide multiple items / variables. Further inputs are discarded (Execute Once by default). [Expressions](https://docs.n8n.io/code-examples/expressions/) are supported in the command input.

## Credentials

You can use your meshcentral account credentials or login token (don't confuse with server login key). 2FA is not supported, you need to add your n8n's server IP to meshcentral's `skip2factor` configuration.

You may also use a proxy.

## Compatibility

Tested with n8n Version 0.222.0 and MeshCentral 1.1.4

## How it works

Under the hood this package includes a copy of meshctrl.js and runs it on the n8n server. If you enable debug you can see the rendered commands and stderr in your n8n debug logs.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [meshctrl documentation](https://ylianst.github.io/MeshCentral/meshctrl/)

## Version history

1.0.0

- Initial Release, includes [MeshCentral PR #5068](https://github.com/Ylianst/MeshCentral/pull/5068)

1.0.1

- Added support for n8n expressions

1.0.3

- Fix meshctrl.js paths for production