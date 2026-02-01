# n8n-nodes-visualping

This is an n8n community node that integrates [Visualping](https://visualping.io) with your n8n workflows, allowing you to trigger workflows when website changes are detected.

[Visualping](https://visualping.io) is a web monitoring service that tracks changes on websites and sends notifications, while [n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform that allows you to connect various services.

## Table of contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [Version History](#version-history)
- [Troubleshooting](#troubleshooting)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node provides a trigger operation for Visualping.

### Triggers
- **Visualping Trigger**: Automatically starts an n8n workflow when a Visualping job detects changes on a monitored website
  - Configure webhook notifications for specific Visualping jobs
  - Receive change detection events in real-time
  - Supports job selection from list or by ID

## Credentials

To use this node, you need to authenticate with your Visualping account:

1. **Email and Password Authentication**
   - Configure your Visualping account credentials in the n8n credentials section under `Visualping Credentials API`
   - Provide your Visualping account email and password

## Compatibility

This node has been tested with n8n version 1.57.0 and requires Node.js version 20.15 or higher.

## Usage

1. **Create a Visualping Job**: Set up a new monitoring job on [Visualping](https://visualping.io) to track changes on your target website.
2. **Set up a workflow**: Create a new workflow in n8n.
3. **Add the Visualping Trigger node**: Insert the Visualping Trigger node into your workflow.
4. **Configure credentials**: Enter your Visualping account email and password.
5. **Select a job**: Choose the Visualping job you want to monitor for changes.
6. **Configure the trigger**: The node will automatically set up webhook notifications for the selected job.
7. **Execute the workflow**: The workflow will trigger whenever Visualping detects changes on the monitored website.

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Visualping API Documentation](https://api.visualping.io/doc.html)
- [Visualping Authentication Guide](https://api.visualping.io/doc.html#section/Authentication)

## Version history

Track changes and updates to the node here.

## Troubleshooting

### Common issues

1. **Authentication errors**
   - Verify your Visualping email and password are correct
   - Ensure your Visualping account is active

2. **Job not found**
   - Verify the job ID format (should be numeric)
   - Check if the job exists in your Visualping account
   - Ensure you have access to the job

3. **Webhook configuration issues**
   - Check that your n8n instance is accessible from the internet
   - Verify the webhook URL is correctly configured
   - Review Visualping job settings for webhook notifications

### Getting help

If you encounter issues:
1. Check the [Visualping API documentation](https://api.visualping.io/doc.html)
2. Review the [n8n Community Nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
3. Open an issue in the [GitHub repository](https://github.com/webmonitoring/n8n-nodes-visualping)
