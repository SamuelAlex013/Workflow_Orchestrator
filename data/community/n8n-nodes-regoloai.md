# n8n-nodes-regoloai

This is an n8n community node. It lets you use **RegoloAI** in your n8n workflows.

RegoloAI is an European, green, OpenAI-compatible inference provider offering endpoints for *chat completions*, *text completions*, *embeddings*, and *image generation*, making it easy to integrate advanced AI features into your automations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)    
[Resources](#resources)

--- 
## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-regoloai
```

After installation, restart n8n. You will find the **Regolo AI** node in the editor.

---

## Operations

The Regolo AI node supports the following operations:

### **Chat**

* Create **chat completions** (multi-turn conversations, system/user/assistant roles)

### **Text**

* Generate text completions from a prompt
* Generate vector **embeddings** for input text

### **Image**

* Create images from a text prompt
* Return results as **image URLs** or as **binary files** (PNG)

---

## Credentials

To use this node, you need a **Regolo AI API Key**.

1. Sign up or log in at [RegoloAI](https://regolo.ai).
2. Go to your dashboard and create an API key.
3. In n8n, add new credentials:

	* **API Key**: paste the key you generated
	* **Base URL**: defaults to `https://api.regolo.ai/v1` 

The credentials use **Bearer token authentication**.

---

## Compatibility

* **Minimum n8n version**: 1.40.0
* **Node.js version**: >= 20.15
* Tested with: Regolo AI API (OpenAI-compatible endpoints)

There are no known incompatibilities.

---

## Usage

* Add the **Regolo AI** node in your workflow (you can find it in the "AI" category).
* Select a **Resource** (`Chat`, `Text`, `Image`) and then the desired **Operation**.
* Configure the parameters (model, prompt, options).
* Connect the node to other n8n nodes to automate your AI-driven workflows.

### Notes

* Models are dynamically loaded from the `/models` or `/model/info` endpoints.
* When selecting **Custom (Type Manually)**, you must provide a valid model ID in the **Custom Model** field.
* For image generation, you can choose to return either **URLs** or **binary PNGs**.

---

## Resources

* [n8n Community Nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [RegoloAI documentation](https://docs.regolo.ai/)
* [RegoloAI](https://api.regolo.ai/)
* [n8n](https://n8n.io)

---

## Version history

* **0.1.0**

	* Initial release
	* Added support for:

		* Chat completions
		* Text completions
		* Text embeddings
		* Image generation
	* Added simplified output modes for text and embeddings
	* Binary output support for images
