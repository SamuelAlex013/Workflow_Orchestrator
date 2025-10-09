# n8n-nodes-bvq

This is an n8n community node developed by SVA System Vertrieb Alexander GmbH. It lets you use BVQ data in your n8n workflows.
For further Information regarding BVQ visit the offical BVQ Website https://www.bvq-software.de/en.

BVQ is a cross-platform software designed for automated monitoring of your entire data center, including computing, SAN, and storage layers. It offers monitoring, reporting, alerting, and analysis functions with an intelligent connection to ITSM systems.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.
- [Contact](#contact)  
- [Installation](#installation) 
- [Operations](#operations)  
- [Credentials](#credentials)
- [Usage](#usage) 
- [Resources](#resources)
- [Version History](#version-history)    

## Contact

E-Mail: automation-solutions@sva.de <br>
Website: https://www.sva.de/en<br>
Company: SVA System Vertrieb Alexander GmbH<br>
Department: SVA Automation Solutions<br>
<pre>
Borsigstraße 26
65205 Wiesbaden-Nordenstadt
Germany
</pre>

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Installation

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-bvq` in **Enter npm package name**
4. Agree to the risks of using community nodes
5. Select **Install**

**Note:** After installation, you need to restart your n8n instance for the new node to be recognized!


## Operations

In the UI there is a dropdown to select what data shall be retrieved from the BVQ API.
You can choose between "Alerts" and "Events". Furthermore, you can select the source and the type of "Alerts" and "Events" to specify the requested data.
The data is limited by the given time value and unit. 

Only if "All" as an "Alert Source" is selected there is no option to specify the data by a time and "Alerts" of all sources and types are provided.  

## Credentials

You need the following credentials to establish an API connection:

- Username (from your BVQ-Account)
- Password (from your BVQ-Account)
- URL (Can be found in your local BVQ-Instance under "Connectors" > "Integrations")
- API-Key only mandatory/used for "All Alerts" (Can be generated in your local BVQ-Instance under "Connectors" > "Integrations")

Furthermore there is a checkbox named "Ignore SSL Issues", which you can tick to trust invalid or self-signed SSL-Certificates. If you persist to only trust valid SSL-Certificates, keep the checkbox at "false", which is the default value. If you do so, the Authentication of your API-Connection might fail.


## Usage

The data is submitted in a json formatted array and can be used for any use case.
Please note that extending the time period for the requested data may result in a longer response time from the API. Please be aware that the response time may as well exceed the execution time limit of your n8n instance.


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)


## Version History

### 3.0.1

- Bugfixes

### 3.0.0

- Initial release/Republish