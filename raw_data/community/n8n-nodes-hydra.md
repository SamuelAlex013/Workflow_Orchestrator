# HydraNode – Automated Brute Force Testing in n8n

This is a n8n community node.

HydraNode is an n8n integration for THC Hydra, a powerful and fast brute-force tool for testing login credentials against various services. This node allows security professionals to automate authentication testing across multiple protocols directly within n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Key Features

* Supports Multiple Services (not yet, only SSH) – SSH, FTP, HTTP, SMB, RDP, MySQL, and more.
* Custom Credential Lists – Use predefined or dynamic username/password lists.
* Parallel Attacks – Optimize brute-force speed with adjustable thread count.
* JSON Output – Structured results for easy analysis and integration.


## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install with `npm i n8n-nodes-hydra`

Need Hydra installed on n8n instance eg. `apt-get install hydra`

## Disclaimer
⚠ This node is intended for authorized security testing only. Unauthorized use may violate laws and ethical guidelines. Always obtain permission before testing any system. ⚠

## Compatibility

Developed using n8n version 1.64

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

