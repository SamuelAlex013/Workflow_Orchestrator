# n8n-nodes-iris

This is an n8n community node. It lets you use InterSystems IRIS in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Local Demo](#local-demo)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

* Execute Query - any plain SQL Queries, with dynamic parameters
* Insert - insert to spcified existing table, and with ability to link data to spcified columns

## Credentials

Standard InterSystems IRIS authentication required. Encrypted SSL connection not supported, yet.

## Compatibility

It was tested on n8n version 0.193. Supports any version of InterSystems IRIS.

## Usage

[Try it out](https://docs.n8n.io/try-it-out/) documentation from n8n

## Local Demo

Clone this repo, and start demo environment with docker-compose

```shell
git clone https://github.com/caretdev/n8n-nodes-iris.git
cd n8n-nodes-iris
docker-compose up -d
```

When all started go to <http://localhost:5678/workflow/1>

![screenshot](https://raw.githubusercontent.com/caretdev/n8n-nodes-iris/master/img/workflow.png)
_result.xlsx from the demo may appear in data folder of this project_

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [InterSystems Documentation](https://docs.intersystems.com)
* [InterSystems Developer Community](https://community.intersystems.com)
