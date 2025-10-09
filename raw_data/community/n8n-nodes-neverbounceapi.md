![NeverBounce Logo](https://www.neverbounce.com/images/logo.png)

# n8n-nodes-neverbounce

This repository contains [n8n](https://n8n.io) nodes for [NeverBounce](https://www.neverbounce.com/) email verification services. These nodes allow you to integrate NeverBounce's powerful email verification capabilities into your n8n workflows.

## Available Nodes

### NeverBounce Email Verification

The NeverBounce Email Verification node connects to the NeverBounce API to validate email addresses. It checks if an email address is valid, invalid, disposable, a catch-all address, or if its status is unknown. The node provides detailed verification results including status codes, flags, and suggested corrections for potentially misspelled domains.

### Email Verification Hints

The Email Verification Hints node enhances email verification results by adding contextual guidance for agents (AI or human) on how to best handle email communications. It adds an "agent_instructions" field containing predefined prompts based on the verification outcome, providing best practices for email communication to improve deliverability, compliance, and user experience in automation flows.

## Prerequisites

You need the following to use these nodes:

* [n8n](https://n8n.io/) (Minimum version: Node 20)
* A [NeverBounce](https://www.neverbounce.com/) account and API key

## Installation

Follow these steps to install the NeverBounce nodes in your n8n instance:

```bash
npm install nb-email-verification nb-email-verification-hints
```

Alternatively, you can install them directly from the n8n Community Nodes panel in your n8n instance.

## Usage

1. Add your NeverBounce API credentials in the n8n credentials manager
2. Add either the NeverBounce Email Verification or Email Verification Hints node to your workflow
3. Configure the node according to your requirements
4. Connect it to other nodes in your workflow

For detailed usage instructions, refer to the README files for each node:
- [NeverBounce Email Verification](./nodes/NbEmailVerification/README.md)
- [Email Verification Hints](./nodes/EmailVerificationHints/README.md)

## Example Workflows

### Basic Email Verification

1. **HTTP Request node**: Receives a webhook with an email to verify
2. **NeverBounce Email Verification node**: Verifies the email address
3. **IF node**: Routes the workflow based on verification results
   - If valid, proceed with sending email
   - Otherwise, handle invalid email (e.g., notify user, log error)

### Enhanced Email Verification with AI

1. **Spreadsheet node**: Reads a list of email addresses
2. **NeverBounce Email Verification node**: Verifies each email address
3. **Email Verification Hints node**: Adds communication guidelines
4. **OpenAI node**: Uses the verification results and hints to generate appropriate email content
5. **Send Email node**: Sends the generated email

## Development

If you want to contribute to this project:

## Development Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

1. Clone the repository:
   ```
   git clone https://github.com/NeverBounce/n8n-nodes-neverbounce.git
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Build all nodes:
   ```
   npm run build:all
   ```
4. Test your changes locally by linking the package to your n8n installation

## More information
Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/NeverBounce/n8n-nodes-neverbounce/blob/master/LICENSE.md)
