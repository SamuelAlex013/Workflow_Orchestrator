# n8n-nodes-llms-qianfan

![NPM Downloads](https://img.shields.io/npm/dm/n8n-nodes-llms-qianfan)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/htynkn/n8n-nodes-llms-qianfan/latest)


This is an n8n community node. It lets you use Baidu QianFan in your n8n workflows.

Baidu QianFan is Baidu's advanced AI platform designed to provide comprehensive AI solutions for various industries. It offers robust AI infrastructure, pre-trained models, and development tools to help enterprises and developers build, deploy, and manage AI applications efficiently.

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

There are two ways to install community nodes:

### Within n8n using the GUI

+ Access your n8n with url ${n8nBaseUrl}/settings/community-nodes
+ Enter n8n-nodes-llms-qianfan and Click Install Button

### Manually from the command line
use this method if your n8n instance doesn't support installation through the in-app GUI.

+ Create ~/.n8n/nodes if it doesn't already exist, and navigate into it
+ npm i n8n-nodes-llms-qianfan


## Credentials

To access the Qianfan big model securely, you need to use security authentication with Access Key (AK) and Secret Key (SK). Follow the steps below to obtain your Access Key (AK) and Secret Key (SK). For more details, please refer to [How to Get AK/SK](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb).

+ Log in to Baidu AI Cloud Qianfan Console Log in to the Baidu AI Cloud Qianfan Console, and click on "User Account -> Security Authentication" to enter the Access Key management interface.

+ View Security Authentication Access Key/Secret Key Check your security authentication Access Key (AK) and Secret Key (SK).


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Baidu QianFan documentation](https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html)

## Version history

* 0.1.0 something just works
* 0.2.0 add more model options
* 0.3.0 add model list
