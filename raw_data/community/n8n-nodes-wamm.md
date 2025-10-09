# n8n-nodes-wamm

This is an n8n community node. It lets you use WAMM PRO service in your n8n workflows.

WAMM PRO is a service that enables sending WhatsApp messages directly through the WAMM API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow these steps to install and configure the `n8n-nodes-wamm` custom node in your n8n instance.
settings/ comunity nodes / install / n8n-nodes-wamm
**Installing the `n8n-nodes-wamm` Community Nodes**

1. **Open Settings**
   * Click your avatar (bottom-left) and select **Settings**.
2. **Navigate to Community Nodes**
   * In the left sidebar, choose **Community nodes**.
3. **Launch the Install Dialog**
   * Click the **Install** button at the top right of the Community nodes panel.
4. **Specify the NPM Package**
   * In the **npm Package Name** field, enter:
     ```
     n8n-nodes-wamm
     ```
5. **Acknowledge the Risk**
   * Tick the checkbox **I understand the risks of installing unverified code from a public source**.
6. **Install**
   * Click **Install** and wait for the process to complete.
After installation, the `n8n-nodes-wamm` nodes will appear in your workflow editor.

## Operations

This node supports the following operations:

- **Send Message**: Send a direct text message via WhatsApp
- **Send Media & File**: Send media or files via WhatsApp
- **Send Template**: Send a template-based message via WhatsApp
- **Add to Contact List**: Add a contact to a contact list
- **Remove from Contact List**: Remove a contact from a list or all lists

## Credentials

To use this node, you need a WAMM PRO account. You can get one by visiting the [WAMM website](https://wamm.pro/).

When setting up the credentials, you'll need:
- **API Token**: The access token for the WAMM API
- **Email**: The email address associated with your WAMM account

## Compatibility

This node is compatible with n8n version 1.0.0 or later.

## Usage

### Sending WhatsApp Messages
1. Add the WAMM PRO node to your workflow
2. Select the "Send Message" operation
3. Configure your WAMM instance ID
4. Add the recipient's phone number (in international format, without +)
5. Enter the message you want to send
6. Optionally, you can schedule the message by specifying date and time

### Sending Media or Files
1. Add the WAMM PRO node to your workflow
2. Select the "Send Media & File" operation
3. Configure your WAMM instance ID
4. Add the recipient's phone number
5. Specify the URL of the media file you want to send
6. Enter the message to accompany the media file

### Using Templates
1. Add the WAMM PRO node to your workflow
2. Select the "Send Template" operation
3. Configure your WAMM instance ID
4. Add the recipient's phone number
5. Specify the template ID you want to use
6. Add the template parameters in JSON format

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [WAMM API Documentation](https://wamm.pro/apidoc/)
* [GitHub: n8n-nodes-wamm](https://github.com/ulmeanuadrian/n8n-nodes-wamm)
