# n8n-nodes-datadog

<img src="https://n8n.io/images/nodes/n8n.svg" width="100" height="100"/>
<img src="https://raw.githubusercontent.com/team-carepay/n8n-nodes-datadog/main/nodes/LogToDatadog/dd_logo_v_rgb.svg" width="100" height="100"/>

A community node for integrating Datadog with n8n, the workflow automation tool. This node allows you to interact with Datadog's API to log messages from your n8n workflows.

## Features

- **Logs**: Send logs to Datadog.

## Installation

To install the node, follow these steps:

1. Navigate to your n8n installation directory.
2. Install the node package:

   ```bash
   npm install n8n-nodes-datadog
   ```
3. Start or restart your n8n instance.   

## Configuration
Before using the Datadog node, you need to configure the Datadog API credentials in n8n.

1. Go to the n8n Credentials section.
2. Add new credentials and select "Datadog API".
3. Enter your Datadog API key.
4. Save the credentials.

## Usage
Once the credentials are set up, you can use the `Log messages to Datadog` node in your workflows.

1. **Add the `Log messages to Datadog` node**: Drag and drop the `Log messages to Datadog` node into your workflow.
2. **Select credentials to connect with** : Choose the credentials you configured in the previous step.
3. **Configure Parameters**: Condition, success and failure messages, tags and service name.
4. Execute Workflow: Run your workflow to interact with Datadog.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/team-carepay/n8n-nodes-datadog/blob/main/LICENSE.md) file for details.