# n8n-nodes-azure-deepseek

This is an n8n node to interact with the DeepSeek LLM model available on Azure AI Foundry.

## Features

- Chat Completion: Generate responses from the DeepSeek LLM model
- Supports various parameters for controlling the model's behavior:
  - Temperature
  - Max Tokens
  - Top P
  - Frequency and Presence Penalties
  - Streaming capabilities

## Prerequisites

- n8n instance (v1.0.0+)
- Azure account with access to Azure AI Foundry
- A deployed DeepSeek LLM model on Azure AI Foundry

## Installation

### Installation via n8n Admin Panel

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-azure-deepseek` in "Enter npm package name"
4. Click **Install**

### Installation via npm

1. Go to your n8n installation directory
2. Run `npm install n8n-nodes-azure-deepseek`
3. Start n8n

## Credentials

To use this node, you need to create credentials for the Azure DeepSeek API:

1. In n8n, go to **Credentials** and click **Create New**
2. Search for "Azure DeepSeek API" and select it
3. Enter the following details:
   - **API Key**: Your Azure AI Foundry API key
   - **Endpoint**: Your Azure AI Foundry endpoint URL (e.g., `https://your-resource-name.openai.azure.com`)
   - **Deployment ID**: The deployment ID of your DeepSeek model

## Usage

1. Add the "Azure DeepSeek LLM" node to your workflow
2. Connect it to a trigger or previous node
3. Configure the operation (currently only "Chat Completion" is supported)
4. Define your messages in JSON format:
   ```json
   [
     {
       "role": "system",
       "content": "You are a helpful assistant."
     },
     {
       "role": "user",
       "content": "Tell me about DeepSeek LLM."
     }
   ]
   ```
5. Configure any additional parameters as needed (temperature, max tokens, etc.)
6. Execute the workflow

## Development

If you want to contribute to this node:

1. Clone this repository
2. Install dependencies: `npm install`
3. Build the code: `npm run build`
4. Link to your n8n installation: `npm link` (from this directory) and `npm link n8n-nodes-azure-deepseek` (from your n8n installation directory)

## License

[MIT](LICENSE)