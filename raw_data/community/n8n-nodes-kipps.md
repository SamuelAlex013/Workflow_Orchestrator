# n8n Nodes for Kipps.AI

This repository contains n8n nodes for interacting with the Kipps.AI platform. These nodes allow you to integrate your Kipps.AI chatbots and voicebots into your n8n workflows.

## Nodes

This package includes the following nodes:

- **Kipps.AI Chatbot**: Interact with a Kipps.AI chatbot.
- **Kipps.AI Voicebot**: Initiate, interact with, and end calls with a Kipps.AI voicebot.

## Installation

### Docker

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/KIPPS-AI/n8n-nodes-kipps.git
    ```
2.  **Navigate to the cloned directory:**
    ```bash
    cd n8n-nodes-kipps
    ```
3.  **Build the package:**

    ```bash
    npm install
    npm run build

    ```

4.  **Run the Docker container:**

    ```bash
    docker run -it --rm -p 5678:5678 `
    -v "${env:USERPROFILE}\.n8n:/home/node/.n8n" `
    -v "${PWD}:/home/node/.n8n/custom" `  -e N8N_CUSTOM_EXTENSIONS_MODE=paths`
    -e N8N_CUSTOM_EXTENSIONS=/home/node/.n8n/custom `
    n8nio/n8n
    ```

    On Linux/macOS, use:

    ```bash
    docker run -it --rm -p 5678:5678 \
    -v "$HOME/.n8n:/home/node/.n8n" \
    -v "$(pwd):/home/node/.n8n/custom" \
    -e N8N_CUSTOM_EXTENSIONS_MODE=paths \
    -e N8N_CUSTOM_EXTENSIONS=/home/node/.n8n/custom \
    n8nio/n8n
    ```

### npm (Bare-metal or Custom Node.js install)

1.  **Install the package:**
    ```bash
    npm install n8n-nodes-kipps
    ```
2.  **Restart your n8n instance.**

### Mount Instructions

If you are running n8n in a Docker container, you can mount the nodes into your container.

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/KIPPS-AI/n8n-nodes-kipps.git
    ```
2.  **Add the following to your `docker-compose.yml` file:**
    ```yaml
    volumes:
      - ./n8n-nodes-kipps:/root/.n8n/custom
    ```
3.  **Restart your n8n container.**

## Authentication

To use these nodes, you will need a Kipps.AI API key.

1.  **Obtain your API Key:**
    - Log in to your Kipps.AI account at [https://app.kipps.ai/](https://app.kipps.ai/).
    - Navigate to the API settings page (you might find it under "Developers" section).
    - Generate a new API key.

2.  **Add the Kipps.AI Credential in n8n:**
    - In your n8n instance, go to the "Credentials" section.
    - Click on "Add credential".
    - Search for "Kipps AI API" and select it.
    - Enter your API key in the credential configuration.
    - Save the credential.

## Node Parameters

### Kipps.AI Chatbot

- **Agent ID**: The ID of the chatbot agent to use.
- **Message**: The message to send to the chatbot.
- **Session ID**: Optional Conversation ID for context management.

### Kipps.AI Voicebot

- **Action**: The action to perform.
  - **Start Call**: Initiates a call.
  - **Send Audio/Text**: Sends audio or text to the call.
  - **End Call**: Ends the call.
- **Voicebot ID**: The ID of the voicebot to use.
- **Phone Number**: The phone number to call (required for `Start Call`).
- **Room Name**: The room name of the call to interact with.
- **Input Type**: The type of input to send (`Text` or `Audio`).
- **Text Input**: The text to send to the voicebot.
- **Audio Input**: The path to the audio file to send.

## Usage Examples

### Kipps.AI Chatbot

This example shows how to send a message to a Kipps.AI chatbot and receive a response.

1.  **Add the Kipps.AI Chatbot node to your workflow.**
2.  **Configure the node with your Agent ID and the message you want to send.**
3.  **Execute the workflow.**

The node will output the chatbot's response.

### Kipps.AI Voicebot

This example shows how to initiate a call, send a message, and end the call with a Kipps.AI voicebot.

1.  **Start a call:**
    - Add the Kipps.AI Voicebot node to your workflow.
    - Set the **Action** to `Start Call`.
    - Provide the **Voicebot ID** and the **Phone Number** to call.
2.  **Send a message:**
    - Add another Kipps.AI Voicebot node.
    - Set the **Action** to `Send Audio/Text`.
    - Provide the **Room Name** from the previous step.
    - Set the **Input Type** to `Text` and enter your message.
3.  **End the call:**
    - Add a final Kipps.AI Voicebot node.
    - Set the **Action** to `End Call`.
    - Provide the **Room Name**.

## Troubleshooting

- **401 Unauthorized**: Make sure your API key is correct and has the necessary permissions.
- **404 Not Found**: Double-check the Agent ID or Voicebot ID.
- **Network Errors**: Ensure that your n8n instance can reach the Kipps.AI API (`https://backend.kipps.ai`).
- **Credential Mistakes**: Verify that you have created a Kipps.AI API credential and selected it in the node.
