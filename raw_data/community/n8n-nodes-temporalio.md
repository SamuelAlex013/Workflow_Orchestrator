![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-temporal

This package contains a custom n8n node for integrating with [Temporal](https://temporal.io/), a microservice orchestration platform. It allows you to execute and manage Temporal workflows directly from your n8n workflows.

## Features

- **Start Workflows**: Launch new Temporal workflow executions with custom inputs
- **Get Workflow Status**: Monitor the status of running or completed workflows
- **Secure Connection**: Supports TLS authentication for secure Temporal cluster connections
- **Namespace Support**: Connect to specific Temporal namespaces
- **Task Queue Management**: Specify custom task queues for workflow execution

## Installation

1. Install the package:
   
   ```bash
   npm install n8n-nodes-temporal
   ```

2. Restart your n8n instance

## Usage

### Credentials

To use this node, you'll need to configure Temporal credentials:

1. Address: Your Temporal server address (e.g., `localhost:7233`)
2. Namespace: The Temporal namespace to use
3. (Optional) TLS Certificate and Key paths for secure connections

### Operations

The node supports two main operations:

1. **Start Workflow**
   - Workflow ID: Unique identifier for the workflow execution
   - Workflow Type: The type of workflow to execute
   - Task Queue: The queue to use for workflow tasks (defaults to 'default')
   - Input: JSON input data for the workflow

2. **Get Workflow Status**
   - Workflow ID: The ID of the workflow to check
   - Returns: Status, start time, close time, and other workflow details

## Resources

- [Temporal Documentation](https://docs.temporal.io/)
- [n8n Node Development Guide](https://docs.n8n.io/integrations/creating-nodes/)
- [Temporal TypeScript SDK](https://docs.temporal.io/dev-guide/typescript/)

## License

[MIT](LICENSE.md)
