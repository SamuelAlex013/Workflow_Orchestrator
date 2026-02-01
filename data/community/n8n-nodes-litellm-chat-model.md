# n8n-nodes-litellm

This is an n8n community node package for LiteLLM. It allows you to make `acompletion` requests to a LiteLLM proxy.

## Installation

1.  Go to **Settings > Community Nodes**.
2.  Select **Install**.
3.  Enter `n8n-nodes-litellm` in the **Enter npm package name** field.
4.  Agree to the risks and select **Install**.

## Credentials

This node uses a custom credential to connect to your self-hosted LiteLLM instance. You will need to provide:

*   **Base URL**: The URL of your LiteLLM proxy (e.g., `http://localhost:4000`).
*   **API Key**: The API key for your LiteLLM proxy, if required.

## Usage

The node provides an `acompletion` operation with the following inputs:

*   **Model**: The model to use for the completion (e.g., `gemini/gemini-pro`).
*   **Messages**: The message(s) to send to the model.
*   **Tools**: The tools to make available to the model.

## License

[MIT](LICENSE.md)
