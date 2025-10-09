# n8n-nodes-rd-station-marketing-conversion

![RD Station Marketing](https://avatars.githubusercontent.com/u/817058?s=200&v=4)
![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node. It lets you use RD Station Marketing Conversion API in your n8n workflows.

RD Station Marketing is an all-in-one Digital Marketing automation tool. This means that it brings together the main resources to carry out a Digital Marketing strategy in one place, and you can carry out different actions in a single software, with more efficiency and productivity.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Resources](#resources)
[Version history](#version-history)
[License](#license)

## Installation
### Community Nodes (Recommended)

For users on n8n v0.187+, your instance owner can install this node from [Community Nodes](https://docs.n8n.io/integrations/community-nodes/installation/).

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-rd-station-marketing-conversion` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

* All Operations
	* **New Conversion**: Allows you to record a conversion event in RD Station Marketing. [Reference](https://developers.rdstation.com/reference/conversao).

## Credentials

Step by step for configuration

1. Access the RD Station Marketing [App Store](https://appstore.rdstation.com/en/publisher);
2. Log in to the management page and click **Generate Key**;
3. In the top right menu, click **Generate API Key**;
4. The system will automatically display the Key created in the listing;
5. Define a name for the Key. This will help you manage and locate the Keys;
6. Choose whether the created Key will be active or inactive by clicking on the Status button;
7. Copy the Key code and paste it into the form script that you will use for conversion integrations with RD Station Marketing.

### **Important informations**

The API Key only supports conversion events;
You can create up to 5 Keys;
It is not possible to delete Keys, we only allow activation and deactivation;
It is not necessary to implement the OAuth protocol to use API Keys;
The RD Station Marketing user needs to have the Manager or Owner access profile to access the API Keys management screen.

## Compatibility

n8n v0.187+.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [RD Station Marketing API Key Authentication](https://developers.rdstation.com/reference/autenticacao-api-key)
* [RD Station Marketing API Key Conversion](https://developers.rdstation.com/reference/conversao)

## Version history

0.1.0

## License

MIT License

Copyright (c) 2023 Eduardo Matheus Bernardo Silva <bernardo@idxcode.com.br>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
