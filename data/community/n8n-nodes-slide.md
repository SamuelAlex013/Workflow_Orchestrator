# n8n-nodes-slide

This is an n8n community node. It lets you use [Slide](https://slide.tech) in your n8n workflows.

> Slide offers a Modern Business Continuity & Disaster Recovery (BCDR) Solution Purpose-built for MSPs. The legacy backup solutions rely on outdated technology and offer substandard support. Slide has reimagined the BCDR from the ground up by combining modern software, high-performance hardware, and end-to-end encryption at no extra cost. The result is a faster, more secure, more cost-effective solution.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Agents
* [x] List agents
* [x] Create an agent for an auto-pair installation
* [x] Get agent
* [x] Update agent
* [x] Add agent passphrase
* [x] Delete agent passphrase
* [x] Pair agent
### Devices
* [x] List devices
* [x] Get device
* [x] Update device
* [x] Power off a device
* [x] Reboot a device
### Backups
* [x] List backups
* [x] Start backup
* [x] Get backup
### Snapshots
* [x] List snapshots
* [x] Get snapshot
### Restores (File)
* [x] List file restores
* [x] Create file restore
* [x] Delete file restore
* [x] Get file restore
* [x] Browse file restore
### Restores (Virtual Machine)
* [x] List virtual machines
* [x] Create virtual machine
* [x] Delete virtual machine
* [x] Get virtual machine
* [x] Update virtual machine
### Restores (Image)
* [x] List image exports
* [x] Create image export
* [x] Delete image export
* [x] Get image export
* [x] Update image export
* [x] Browse image export
### Networks
* [x] List networks
* [x] Create network
* [x] Delete network
* [x] Get network
* [x] Update network
* [x] Create IPsec connection
* [x] Delete IPsec connection
* [x] Update IPsec connection
* [x] Create port forward
* [x] Delete port forward
* [x] Update port forward
* [x] Create WireGuard peer
* [x] Delete WireGuard peer
* [x] Update WireGuard peer
### Users
* [x] List users
* [x] Get user
### Alerts
* [x] List alerts
* [x] Get alert
* [x] Update alert
### Accounts
* [x] List accounts
* [x] Get account
* [x] Update account
### Clients
* [x] List clients
* [x] Create client
* [x] Delete client
* [x] Get client
* [x] Update client
### Audits
* [x] List audit logs
* [x] Get audit log
* [x] List audit actions
* [x] List audit resource types

## Credentials

n8n-nodes-slide requires an API token from Slide. Retreive an API token by logging into the [Slide console](https://console.slide.tech).

## Compatibility

Tested against n8n version 1.103.2

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Slide API documentation](https://docs.slide.tech/api/)

## Version history

### 0.1.0
Initial release with basic support for List and Get actions on each endpoint

### 0.1.1
Populated README file and fixed the Slide icon to use an SVG

### 0.1.2
Fix minor bug with Restores Type showing on all resources

### 0.1.3
Add all filter options for List and Get actions on each endpoint.

### 0.2.0
**NOTE: 0.2.0 introduces breaking changes to the Restore actions nodes.**

Adds all of the Restore and Audit Log actions as well as many of the Network actions.

### 1.0.0

n8n-nodes-slide now has nodes for every Slide API endpoint!

