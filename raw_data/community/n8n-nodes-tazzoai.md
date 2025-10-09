# n8n-nodes-tazzoai

This is an n8n community node. It lets you use Tazzo.ai in your n8n workflows.

Tazzo.ai is a voice agent platform that enables automated outbound voice calls with AI-powered conversational agents.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)   
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Or install directly via npm:

```bash
npm install n8n-nodes-tazzoai
```

Or via the n8n UI:
* Go to **Settings > Community Nodes**
* Click **Install a Community Node**
* Enter: `n8n-nodes-tazzoai`

## Operations

* **Trigger Outbound Call** - Initiate outbound voice calls using Tazzo.ai's voice agents

## Credentials

Before using the node, set up your Tazzo.ai login credentials:

* Go to **Credentials > Create New**
* Select: **Tazzo.ai API**
* Fill in:
   * **Email** – your Tazzo.ai account email
   * **Password** – your Tazzo.ai account password
* Click **Save**


## Usage

### Using the Node in a Workflow

* Drag the **Tazzo.ai** node into your workflow
* Select the credentials you just created
* Provide the required input parameters:
   * **Agent ID** – ID of the agent who will make the call
   * **Contact Number** – the phone number to be dialed
* (Optional) Connect it with a trigger node like Webhook or Schedule
* Run the workflow

✅ This will trigger an outbound voice call via the Tazzo.ai platform.

### Sample Output

```json
[
  {
    "message": "Call originated successfully",
    "data": {
      "channelId": "12345678-abcd-efgh-ijkl-9876543210ab",
      "callType": "Outbound",
      "outboundNumber": "9988776655",
      "extension": "1122334455",
      "agentId": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
      "campaignBody": {
        "contactNumber": "9988776655",
        "agentId": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
        "originateEndpoint": "1122334455"
      }
    }
  }
]
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Source Code](https://github.com/legitbytes/n8n-nodes-tazzoai)
* [npm Package](https://www.npmjs.com/package/n8n-nodes-tazzoai)

**Maintainer**: Legitbytes  
**License**: MIT © 2025 Legitbytes
