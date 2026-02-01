# TailTrigger – Custom n8n Node for real-time Monitoring

This is a n8n community node.

TailTrigger allows real-time monitoring of a local file to start the workflow whenever a line is added.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install with `npm i n8n-nodes-tail`

## Usage
Disclaimer: It is not recommended to use this on large log files (such as nginx logs), as it may trigger an excessive number of workflows.

Tip: Use a command like ` | grep ` beforehand to filter the logs and create a smaller file for monitoring.

## Compatibility

Developed using n8n version 1.64

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

