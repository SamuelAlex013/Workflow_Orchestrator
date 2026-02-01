# n8n-nodes-featherless

This is an n8n community node for Featherless API integration. It allows you to interact with various AI models through the Featherless AI platform directly from your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Featherless](https://featherless.ai/) is a platform that provides access to over 10,000+ open-weight models through a unified API.

## Features

- Interact with multiple AI models through a single node
- Send chat messages to AI models
- Customize model parameters such as temperature, max tokens, frequency penalty, and presence penalty
- View truncated model descriptions in the model selector
- Easy integration with n8n workflows

## Installation

### Community Node (Recommended)

To install this node as a community node in n8n, follow these steps:

1. Open your n8n instance
2. Go to "Settings" > "Community Nodes"
3. Select "Install"
4. Enter `n8n-nodes-featherless` in the "Enter npm package name" field
5. Agree to the risks of using community nodes (if prompted)
6. Click "Install"

After installation, the node will be available in the "Featherless" category in the node palette.

### Manual Installation (Advanced)

If you prefer manual installation or are using a custom n8n setup:

1. Open your n8n installation directory
2. Navigate to the `nodes` subdirectory
3. Run the following command:
   ```
   npm install n8n-nodes-featherless
   ```
4. Restart your n8n instance

**Note:** If you're using Docker or a server deployment, you may need to rebuild your container or restart your server for the changes to take effect.

### Troubleshooting

If you encounter issues with the node not updating to new versions correctly or not displaying changes inside n8n, try the following:

1. Clear your browser cache
2. Restart your n8n instance
3. If using Docker, rebuild and restart your container:
   ```
   docker-compose down
   docker-compose build
   docker-compose up -d
   ```
4. For server deployments, restart the n8n service:
   ```
   sudo systemctl restart n8n
   ```

## Usage

1. Add the Featherless node to your workflow
2. Configure the Featherless API credentials (see Configuration section)
3. Select the desired operation (currently only 'Chat' is available)
4. Enter the model ID you want to use (click "View Available Models" button to see options)
5. (Optional) Provide a system prompt to set the behavior of the AI
6. Enter your message
7. Adjust additional parameters as needed (temperature, max tokens, etc.)
8. Execute the node to receive the AI's response

## Model Selection

Enter the model ID directly in the "Model Name or ID" field. Use the "View Available Models" button next to the input field to open the [Featherless Models page](https://featherless.ai/models) in a new tab, where you can browse and copy the model IDs of available models.

## Configuration

### Featherless API Credentials

To use this node, you need to set up Featherless API credentials:

1. Sign up for an account at [Featherless](https://featherless.ai/)
2. Generate an API key in your Featherless dashboard
3. In n8n, create a new credential of type 'Featherless API'
4. Enter your API key

### Node Parameters

- **Operation**: Currently, only 'Chat' is available
- **Model**: Enter the model ID you want to use (e.g., "meta-llama/Meta-Llama-3.1-8B-Instruct")
- **System Prompt**: (Optional) Set the behavior or role of the AI assistant
- **Message**: The user's input message to the AI
- **Temperature**: Controls the randomness of the AI's output (0.0 to 1.0)
- **Additional Fields**: 
  - **Frequency Penalty**: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far.
  - **Max Tokens**: The maximum number of tokens to generate in the chat completion.
  - **Presence Penalty**: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far.
  - **Top P**: An alternative to sampling with temperature, called nucleus sampling. Top_p of 0.1 means only the tokens comprising the top 10% probability mass are considered.

## Examples

### Basic Chat Workflow

1. Add a "Manual" trigger node
2. Connect an Featherless node
3. Configure the Featherless node:
   - Operation: Chat
   - Model: Enter a model ID (e.g., "deepseek-ai/DeepSeek-V3-0324")
   - Message: "Hello, can you explain what n8n is?"
4. Execute the workflow
5. The Featherless node will return the AI's response explaining n8n

### Dynamic System Prompt

1. Start with a "Manual" trigger node
2. Add a "Set" node to define a variable for the system prompt
3. Connect a Featherless node
4. Configure the Featherless node:
   - Operation: Chat
   - Model: Enter a model ID (use the "View Available Models" button to see options)
   - System Prompt: {{$node["Set"].json["systemPrompt"]}}
   - Message: "What's your primary function?"
5. Execute the workflow
6. The AI will respond based on the system prompt set in the "Set" node

## Support

If you encounter any issues or have questions about this node, please [open an issue](https://github.com/darinverheijke/n8n-nodes-featherless/issues) on the GitHub repository.

## Contributing

Contributions to improve this node are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the [MIT License](LICENSE.md).

## About n8n
n8n is a free and open [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation tool. It can be self-hosted, easily extended, and used to automate workflows across various services and applications. n8n enables you to connect anything to everything.

## About Featherless
Featherless AI is a serverless AI inference platform that offers access to over 10,000+ open-source models. Our goal is to make all AI models available for serverless inference. We provide inference via API to a continually expanding library of open-weight models.

## Changelog

For a full list of changes, please refer to the [CHANGELOG.md](CHANGELOG.md) file.