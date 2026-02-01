![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-akashchat

This is an n8n community node for AkashChat API integration. It allows you to interact with open-source AI models on the Akash Supercloud directly from your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[AkashChat](https://chatapi.akash.network/) is a platform that provides access to leading open-source AI models through a unified API.

## Features

- Interact with multiple open-source AI models
- Send chat messages to AI models
- Select from a variety of models (Llama, Qwen, DeepSeek, etc.)
- Simple integration with n8n workflows

## Installation

### Community Node (Recommended)

To install this node as a community node in n8n:

1. Open your n8n instance
2. Go to "Settings" > "Community Nodes"
3. Select "Install"
4. Enter `n8n-nodes-akashchat` in the "Enter npm package name" field
5. Agree to the risks of using community nodes (if prompted)
6. Click "Install"

After installation, the node will be available in the "AkashChat" category in the node palette.

### Manual Installation (Advanced)

If you prefer manual installation or are using a custom n8n setup:

1. Open your n8n installation directory
2. Navigate to the `nodes` subdirectory
3. Run the following command:
   ```
   npm install n8n-nodes-akashchat
   ```
4. Restart your n8n instance

**Note:** If you're using Docker or a server deployment, you may need to rebuild your container or restart your server for the changes to take effect.



## Usage

1. Add the AkashChat node to your workflow
2. Configure the AkashChat API credentials (see Configuration section)
3. Enter your prompt and select a model
4. Execute the node to receive the AI's response

## Model Selection

Choose from a variety of open-source models, including Llama, Qwen, DeepSeek, and more. Model descriptions are available in the node for easy selection.

## Configuration

### AkashChat API Credentials

To use this node, you need to set up AkashChat API credentials:

1. Sign up for an account at [AkashChat](https://chatapi.akash.network/)
2. Generate an API key in your AkashChat dashboard
3. In n8n, create a new credential of type 'Akash Chat API'
4. Enter your API key

### Node Parameters

- **Prompt**: The user's input message to the AI
- **Model**: Select the AI model you want to use

## Examples

### Basic Chat Workflow

1. Add a "Manual" trigger node
2. Connect an AkashChat node
3. Configure the AkashChat node:
   - Model: Choose a model (e.g., "Meta-Llama-3-1-8B-Instruct-FP8")
   - Prompt: "Hello, who are you?"
4. Execute the workflow
5. The AkashChat node will return the AI's response



## Support

If you encounter any issues or have questions about this node, please [open an issue](https://github.com/fenilmodi00/n8n-nodes-akashchat/issues) on the GitHub repository.

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

## About AkashChat
AkashChat is a platform that provides a unified API to access various open-source AI models. It allows developers to integrate multiple AI services into their applications without managing separate API integrations for each model provider. AkashChat supports a wide range of models, making it easier to experiment with and deploy various AI capabilities in your workflows.

## About Akash Network

[Akash Network](https://akash.network/) is a decentralized, open-source cloud computing marketplace. It enables anyone to rent and lease computing resources securely and efficiently, with competitive pricing compared to traditional cloud providers. Akash empowers developers and businesses to deploy applications in a permissionless, censorship-resistant, and cost-effective environment, leveraging the power of blockchain and open-source technologies.

## Changelog

### 0.1.2
- Initial release with chat/completions support and model selection.
