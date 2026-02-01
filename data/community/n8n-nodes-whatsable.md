<p align="center">
  <img src="https://d1pnnwteuly8z3.cloudfront.net/images/acc1c175-2e05-4bab-805e-64536550fa04/393f0ca5-e904-41f3-8eee-b2dab6bd4e0d.png" alt="WhatsAble Logo" width="160"/>
</p>

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Authentication](#authentication)
- [Features](#features)
- [How to Use WhatsAble Action Node](#how-to-use-whatsable-action-node)
- [How to Use WhatsAble Trigger Node](#how-to-use-whatsable-trigger-node)
- [How to Use Notifier Action Node](#how-to-use-notifier-action-node)
- [How to Use Notifier Trigger Node](#how-to-use-notifier-trigger-node)
- [How to Use Notifyer System Action Node](#how-to-use-notifyer-system-action-node)
- [How to Use Notifyer System Trigger Node](#how-to-use-notifyer-system-trigger-node)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)
- [Support](#support)
- [License](#license)
- [Resources](#resources)

---

# n8n-nodes-whatsable

This is an [n8n](https://n8n.io/) community node for integrating with the WhatsAble Suite, providing powerful WhatsApp messaging automation capabilities.

---

## Overview

The WhatsAble Suite offers a comprehensive set of messaging tools that integrate seamlessly with n8n, enabling powerful automation workflows for businesses of all sizes. The suite comprises three powerful messaging platforms:

### WhatsAble
- Ideal for small businesses and startups
- Simple integration with n8n
- Basic media support
- Subscription-based pricing
- 7-day free trial
- [Documentation](https://docs.whatsable.app/guides/whatsable/n8n)

### Notifier by WhatsAble
- Perfect for medium-sized businesses
- Enhanced template support
- Standard media capabilities
- Flexible pricing options
- Available free trial
- [Documentation](https://docs.whatsable.app/guides/notifier/n8n)

### Notifyer System
- Enterprise-grade solution
- Advanced template capabilities
- Full media support
- Enterprise pricing
- Try for free with 2 numbers
- [Documentation](https://docs.whatsable.app/guides/notifier-system/n8n-overview)

---

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

---

## Authentication

To use this node, you need to have an API key from your chosen WhatsAble Suite platform:

1. Sign up at [WhatsAble](https://whatsable.app)
2. Choose your platform (WhatsAble, Notifier, or Notifyer System)
3. Complete the verification process
4. Generate an API key from your platform's dashboard

> **Note:** Keep your API key secure and never share it publicly.

---

## Features

### WhatsAble Node
- Send messages
- Send template messages (Via Notifyer System)
- Send non-template messages
- Schedule messages
- Support for various media types
- [Documentation](https://docs.whatsable.app/guides/whatsable/n8n)

### WhatsAble Trigger Node
- Receive incoming messages
- Handle webhooks
- Process notifications
- Real-time message triggers
- [Documentation](https://docs.whatsable.app/guides/whatsable/n8n)

---

## How to Use WhatsAble Action Node

### Prerequisites
- An active WhatsAble subscription
- Access to n8n workflow automation platform
- A verified WhatsApp number in your WhatsAble dashboard

### Setup Process

1. **Subscribe to WhatsAble**
   - Log in to your WhatsAble dashboard
   - Click the Subscribe button
   - Start your 7-day free trial
   - Note: After trial, pricing is $8.99 per month per phone number
2. **Add and Verify Phone Number**
   - Navigate to Verified Numbers in your dashboard
   - Click Add New Number
   - Enter your phone number (with country code)
   - Complete the WhatsApp verification process
   - Note: Only first number needs verification
3. **Get Your API Key**
   - Go to API Keys in your WhatsAble dashboard
   - Copy your unique API key
   - Store it securely for the integration

### Integration Steps

1. Create a new workflow in n8n
2. Add your preferred trigger node and configure its settings
3. Add the WhatsAble node
4. In the WhatsAble node settings:
   - Select "Create new credential"
   - Enter your WhatsAble API key
   - Name your credential (e.g., "WhatsAble Production")
   - Click Save
5. Configure message settings:
   - Select "Send Message (WhatsAble)" operation
   - Fill in required and optional fields
6. Click "Test Step" to verify
7. Save your workflow and activate it

For detailed documentation, visit [WhatsAble n8n Integration Guide](https://docs.whatsable.app/guides/whatsable/n8n)

---

## How to Use WhatsAble Trigger Node

### Prerequisites
- An active WhatsAble subscription
- Access to n8n workflow automation platform
- A verified WhatsApp number in your WhatsAble dashboard

### Setup Process

1. **Get Your Webhook URL**
   - Open the WhatsAble Trigger Node in n8n
   - At the top of the node, locate "Webhook URLs"
   - Click the "Production URL" to copy it to your clipboard
   - This URL will be used to receive incoming messages
2. **Configure Credentials**
   - In the WhatsAble Trigger Node settings:
     - Paste the Production Webhook URL in the "Production URL" input box
     - Enter your WhatsAble API key in the "API Key" input box
     - Click Save
     - A green success message will appear if the configuration is successful
3. **Activate the Trigger**
   - Click "Test Step" to verify the connection
   - Save your workflow
   - Toggle "Active" to start receiving messages
   - Connect the trigger to any action node to process incoming messages

For detailed documentation, visit [WhatsAble n8n Integration Guide](https://docs.whatsable.app/guides/whatsable/n8n)

---

## How to Use Notifier Action Node

### Prerequisites
- An active Notifier account (Monthly or Pay-as-you-go plan)
- Access to n8n workflow automation platform
- Business information ready for configuration

### Setup Process

1. **Configure Business Information**
   - Log in to your Notifier dashboard
   - Navigate to Business Information
   - Complete required fields
   - Verify your WhatsApp number with the code sent
2. **Get Your API Key**
   - Go to API Keys in your Notifier dashboard
   - Copy your unique API key
   - Store it securely for the integration

### Integration Steps

1. Create a new workflow in n8n
2. Add your preferred trigger node and configure its settings
3. Add the WhatsAble node
4. In the WhatsAble node settings:
   - Select "Create new credential"
   - Enter your Notifier API key
   - Name your credential (e.g., "Notifier Production")
   - Click Save
5. Configure message settings:
   - Select "Send Message (Notifier)" operation
   - Fill in required and optional fields
6. Click "Test Step" to verify
7. Save your workflow and activate it

### Example Workflows with Notifier
- Lead Nurturing: Trigger on form submission, send personalized welcome, schedule follow-ups
- Order Confirmations: Trigger on order status change, send update with details
- Event Reminders: Trigger on calendar event, send reminder with RSVP link
- Customer Feedback: Trigger on purchase, send feedback request
- Support Ticket Updates: Trigger on ticket status change, send update

For detailed documentation, visit [Notifier n8n Integration Guide](https://docs.whatsable.app/guides/notifier/n8n)

---

## How to Use Notifier Trigger Node

### Prerequisites
- An active Notifier account
- Access to n8n workflow automation platform
- Business information configured in Notifier

### Setup Process

1. **Get Your Webhook URL**
   - Open the Notifier Trigger Node in n8n
   - At the top of the node, locate "Webhook URLs"
   - Click the "Production URL" to copy it to your clipboard
   - This URL will be used to receive incoming messages
2. **Configure Credentials**
   - In the Notifier Trigger Node settings:
     - Paste the Production Webhook URL in the "Production URL" input box
     - Enter your Notifier API key in the "API Key" input box
     - Click Save
     - A green success message will appear if the configuration is successful
3. **Activate the Trigger**
   - Click "Test Step" to verify the connection
   - Save your workflow
   - Toggle "Active" to start receiving messages
   - Connect the trigger to any action node to process incoming messages

For detailed documentation, visit [Notifier n8n Integration Guide](https://docs.whatsable.app/guides/notifier/n8n)

---

## How to Use Notifyer System Action Node

### Prerequisites
- An active Notifyer System account
- Access to n8n workflow automation platform
- Completed WhatsApp Business Platform embedding process

### Setup Process

1. **Complete Platform Embedding**
   - Connect your WhatsApp Business account
   - Complete Meta's business verification
   - Ensure compliance with WhatsApp Business Platform policies
2. **Set Up Message Templates**
   - Navigate to Templates in your dashboard
   - Create new templates and submit for review
3. **Get Your API Key**
   - Go to API Keys in your Notifyer dashboard
   - Copy your unique API key
   - Store it securely for the integration

### Integration Steps

1. Create a new workflow in n8n
2. Add your preferred trigger node and configure its settings
3. Add the WhatsAble node
4. In the WhatsAble node settings:
   - Select "Create new credential"
   - Enter your Notifyer System API key
   - Name your credential (e.g., "Notifyer System Production")
   - Click Save
5. Configure message settings:
   - Choose between template and non-template message operations
   - Fill in required and optional fields
6. Click "Test Step" to verify
7. Save your workflow and activate it

### Example Workflows with Notifyer System
- Order Confirmations: Trigger on new order, send template message with details
- Appointment Reminders: Trigger on calendar event, send template message
- Lead Notifications: Trigger on new CRM lead, send non-template message
- Customer Support: Trigger on new support ticket, send template message
- Delivery Updates: Trigger on shipping status change, send template message

For detailed documentation, visit [Notifyer System n8n Integration Guide](https://docs.whatsable.app/guides/notifier-system/n8n-overview)

---

## How to Use Notifyer System Trigger Node

### Prerequisites
- An active Notifyer System account
- Access to n8n workflow automation platform
- Completed WhatsApp Business Platform embedding process

### Setup Process

1. **Get Your Webhook URL**
   - Open the Notifyer System Trigger Node in n8n
   - At the top of the node, locate "Webhook URLs"
   - Click the "Production URL" to copy it to your clipboard
   - This URL will be used to receive incoming messages
2. **Configure Credentials**
   - In the Notifyer System Trigger Node settings:
     - Paste the Production Webhook URL in the "Production URL" input box
     - Enter your Notifyer System API key in the "API Key" input box
     - Click Save
     - A green success message will appear if the configuration is successful
3. **Activate the Trigger**
   - Click "Test Step" to verify the connection
   - Save your workflow
   - Toggle "Active" to start receiving messages
   - Connect the trigger to any action node to process incoming messages

For detailed documentation, visit [Notifyer System n8n Integration Guide](https://docs.whatsable.app/guides/notifier-system/n8n-overview)

---

## Common Use Cases

- Lead Qualification: Automated follow-up, lead scoring, response tracking
- Order Notifications: Confirmations, shipping updates, delivery notifications
- Appointment Reminders: Automated reminders, confirmations, calendar integration
- Customer Support: Ticket routing, automated responses, support updates
- Payment Reminders: Invoice notifications, payment confirmations, subscription reminders

---

## Support

For technical support and assistance:

- **Email Support**: Contact our dedicated support team
- **Video Tutorials**: Watch step-by-step integration guides
- **Implementation Help**: Get expert assistance with workflows

For enterprise-level support or custom solutions, contact our solution engineers at team@whatsable.app

---

## License

[MIT](LICENSE.md)

---

## Resources

- [WhatsAble Website](https://whatsable.app)
- [n8n Documentation](https://docs.n8n.io)
- [WhatsAble Suite n8n Overview](https://docs.whatsable.app/n8n-overview)

---

## Running Locally

To run and test this node on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Whatsable/n8n-nodes-whatsable.git
   cd n8n-nodes-whatsable
   ```
2. **Install dependencies**
   ```bash
   pnpm install
   ```
3. **Build the project**
   ```bash
   pnpm build
   ```
4. **Run tests**
   ```bash
   pnpm test
   ```
   > **Note:** Unit tests are included to ensure code quality. Please run tests before submitting a pull request.
5. **Link the node to your local n8n instance**
   - If you are developing a custom node, you can use [n8n's community node development guide](https://docs.n8n.io/integrations/community-nodes/create/) to link your node for local testing.
   - Typically, you can run:
     ```bash
     pnpm link --global
     cd ~/.n8n/custom
     pnpm link --global n8n-nodes-whatsable
     ```
   - Restart your n8n instance to load the custom node.
6. **Test your node**
   - Open n8n in your browser (usually at `http://localhost:5678`)
   - Create a workflow and add your custom node to test its functionality

> **Note:** Make sure you have [Node.js](https://nodejs.org/) and [pnpm](https://pnpm.io/) installed on your machine.

---

## Contributing

We welcome contributions from the community! To contribute:

1. **Fork the repository**: [https://github.com/Whatsable/n8n-nodes-whatsable](https://github.com/Whatsable/n8n-nodes-whatsable)
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and ensure code quality:
   - Follow the existing code style
   - Add or update documentation as needed
   - Run linter and tests before submitting
4. **Commit your changes**
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**
   - Go to the GitHub page for your fork
   - Click "Compare & pull request"
   - Describe your changes and submit the PR

### Reporting Issues
- If you find a bug or have a feature request, please [open an issue](https://github.com/Whatsable/n8n-nodes-whatsable/issues) with details and steps to reproduce.

### Code of Conduct
- Please be respectful and follow our [Code of Conduct](CODE_OF_CONDUCT.md) when participating in this project.
