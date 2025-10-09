![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-chat-wait

A custom n8n node for implementing branch flow control and multi-turn conversations with context memory support.

## Features

- **Branch Flow Control**: Node can immediately output data from previous nodes while waiting for user input
- **Multi-turn Conversations**: Support waiting for user input and continuing workflow
- **Context Memory**: Automatically save and manage conversation history
- **Session Management**: Support multi-user session isolation
- **Timeout Control**: Configurable timeout for waiting user input
- **Webhook Integration**: Receive user input through webhooks

## Installation

```bash
npm install n8n-nodes-chat-wait
```

## Usage

### Basic Configuration

1. **Prompt Message**: Set the message to display to users
2. **Timeout**: Set timeout for waiting user input (seconds)
3. **Enable Context Memory**: Turn on conversation history functionality
4. **Memory Storage Key**: Set the key name for storing conversation history
5. **Session ID Field**: Specify the field name for distinguishing user sessions

### Output Ports

- **Continue**: Immediately output data from previous nodes (if immediate output is enabled)
- **User Input**: Output user input data and related context

### Webhook Usage

The node automatically generates a webhook URL for receiving user input. POST request format:

```json
{
  "chatWaitId": "generated wait ID",
  "userInput": "user input content",
  "sessionId": "session ID (optional)"
}
```

### Conversation History Format

```json
{
  "chatHistory": [
    {
      "type": "user",
      "message": "user message",
      "timestamp": "2025-07-03T10:00:00.000Z"
    }
  ]
}
```

## Workflow Example

1. **Trigger Node** → **Data Processing** → **Chat Wait Node**
2. Chat Wait node immediately outputs processed data to Continue port
3. Simultaneously generates webhook waiting for user input
4. User sends message to webhook through chat interface
5. Node receives user input and outputs to User Input port
6. Continue with subsequent workflow

## Integration with Simple Memory

Can be used with Simple Memory and other memory nodes:

```
Previous Node → Chat Wait → Simple Memory → AI Processing → Chat Wait → ...
```

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this starter

These are the basic steps for working with the starter. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your new repo:
   ```
   git clone https://github.com/<your organization>/<your-repo-name>.git
   ```
3. Run `npm i` to install dependencies.
4. Open the project in your editor.
5. Browse the examples in `/nodes` and `/credentials`. Modify the examples, or replace them with your own nodes.
6. Update the `package.json` to match your details.
7. Run `npm run lint` to check for errors or `npm run lintfix` to automatically fix errors when possible.
8. Test your node locally. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) for guidance.
9. Replace this README with documentation for your node. Use the [README_TEMPLATE](README_TEMPLATE.md) to get started.
10. Update the LICENSE file to use your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
