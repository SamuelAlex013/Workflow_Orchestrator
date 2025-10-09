![Straico Banner](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-straico-official

This is an n8n community node. It lets you use **Straico** in your n8n workflows.

**Straico** is an AI-powered platform that provides advanced prompt completion, image generation, agent management, and Retrieval-Augmented Generation (RAG) capabilities via a RESTful API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

- [Installation](#installation)  
  - [Self-Hosted Installation](#self-hosted-installation)
  - [Cloud Installation](#cloud-installation)
- [Operations](#operations)  
- [Credentials](#credentials)  
- [Compatibility](#compatibility)  
- [Usage](#usage)  
  - [Example Workflow](#example-workflow)  
- [Resources](#resources)  
- [Version History](#version-history)

---

## Installation

### Cloud Installation

> **Note**: Limited to n8n instance owners

Only the n8n instance owner can install and manage verified community nodes. The instance owner is the person who sets up and manages user management. All members of an n8n instance can use already installed community nodes in their workflows.

Admin accounts can also uninstall any community node, verified or unverified. This helps them remove problematic nodes that may affect the instance's health and functionality.

#### Install a Community Node

To install this verified community node:

1. Go to the Canvas and open the nodes panel (either by selecting '+' or pressing Tab)
2. Search for "Straico". You will see it in the "More from the community" section at the bottom of the nodes panel
3. Select the node to view detailed information about supported actions
4. Click "Install". This will install the node for your instance and enable all members to use it

#### Enable Installation of Verified Community Nodes

Some users may not want to show verified community nodes in the nodes panel of their instances. On n8n cloud, instance owners can toggle this in the Cloud Admin Panel.

#### Uninstall a Community Node

To uninstall the community node:

1. Go to Settings > Community nodes
2. On the node you want to uninstall, select Options (three dots menu)
3. Select "Uninstall package"
4. Confirm uninstallation in the modal

### Self-Hosted Installation

For self-hosted n8n instances:

1. Install the community node package:

   ```bash
   npm install n8n-nodes-straico-official
   ```

2. Restart your n8n instance to load the new node

3. In n8n, go to **Settings/Community Nodes** and enable **n8n-nodes-straico-official** if it isn't already

---

## Operations

The Straico node supports the following **resources** and **operations**:

- **User**
  - **Get Info**: Retrieve account details for the authenticated user.
- **Models**
  - **Get All**: List all available chat and image models.
- **Prompt**
  - **Completion**: Generate text completions using either specified models or the smart LLM selector.
- **Image**
  - **Generate Image**: Create images with customizable parameters (model, size, variations, etc.).
- **Agent**
  - **Create**, **Get Details**, **List**, **Add RAG**, **Update**, **Delete**, **Prompt Completion**.
- **File**
  - **Upload**: Upload binary files for RAG or prompt operations.
- **RAG**
  - **Create**, **List**, **Get**, **Update**, **Delete**, **Prompt Completion**.

---

## Credentials

To authenticate requests, you need a **Straico API Key**:

1. Sign up or log in at [Straico](https://straico.com/) and copy your API key from the dashboard.
2. In n8n, go to **Credentials/New Credential/Straico API**.
3. Paste your API key and save.

All node operations will automatically use this credential.

---

## Compatibility

- **Minimum n8n version**: `1.0.0`  
- **Tested with**: n8n `1.x` and Straico API `v1`  
- **Known issues**: None at this time. If you encounter any, please open an issue in the [GitHub repo](https://github.com/your-org/n8n-nodes-straico-official).

---

## Usage

1. **Add Straico Official** node to your workflow.
2. **Select Resource** and **Operation**.
3. **Configure Parameters** according to the selected operation.
4. **Connect** to other nodes as needed.

### Example Workflow

Below is a simple example to generate a text completion and then an image:

```json
[
  {
    "nodes": [
      {
        "parameters": {
          "resource": "prompt",
          "operation": "completion",
          "models": ["gpt-4"],
          "message": "Write a short poem about autumn.",
          "additionalFields": {
            "temperature": 0.8,
            "max_tokens": 100
          }
        },
        "name": "Straico Prompt",
        "type": "n8n-nodes-straico-official.StraicoOfficial",
        "typeVersion": 1,
        "position": [250, 300]
      },
      {
        "parameters": {
          "resource": "image",
          "operation": "generate",
          "model": "openai/dall-e-3",
          "description": "A serene autumn forest with falling leaves",
          "size": "landscape",
          "variations": 1,
          "enhance": true,
          "customEnhancer": "Make it more vibrant and warm"
        },
        "name": "Straico Image",
        "type": "n8n-nodes-straico-official.StraicoOfficial",
        "typeVersion": 1,
        "position": [450, 300]
      }
    ],
    "connections": {
      "Straico Prompt": {
        "main": [
          [
            {
              "node": "Straico Image",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    }
  }
]
```

---

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)  
- [Straico API Documentation](https://documenter.getpostman.com/view/5900072/2s9YyzddrR)  
- [n8n Forum](https://community.n8n.io/) – for community support  

---

## Version History

- **2.0.0** (2025-06-25)  
  - Initial public release  
  - Supports User, Models, Prompt, Image, Agent, File, and RAG operations  
- **2.1.0** (pending)  
  - Planned: Add webhook support and batch RAG uploads

---