# n8n-nodes-emailverify

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node that lets you use EmailVerify.io in your n8n workflows.

EmailVerify.io is a powerful email verification service that helps you validate email addresses, find emails, and check your account balance.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-emailverify` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in your workflow.

## Operations

* **Verify Email**: Verify the validity of an email address
* **Find Email**: Find an email address using a name and domain
* **Check Account Balance**: Check your account balance and remaining credits

## Credentials

You need to configure EmailVerify.io API credentials:

1. Get your API key from [EmailVerify.io](https://emailverify.io)
2. In n8n, go to **Credentials > New Credential**
3. Search for "EmailVerify.io API"
4. Enter your API key

## Compatibility

Tested with n8n version 1.0.0 and above.

## Usage

### Verify Email

This operation verifies whether an email address is valid.

**Input Parameters:**
- **Email**: The email address to verify (required)

**Output:**
Returns detailed information about the email address including:
- Validity status
- Deliverability information
- Risk factors
- Provider information

### Find Email

This operation finds email addresses based on a person's name and domain.

**Input Parameters:**
- **Name**: The person's name (required)
- **Domain**: The company domain (required)

**Output:**
Returns found email addresses and confidence scores.

### Check Account Balance

This operation returns your current account balance and remaining credits.

**Output:**
Returns account information including available credits.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [EmailVerify.io API documentation](https://www.emailverify.io/api/docs/)
* [EmailVerify.io website](https://emailverify.io)

## License

[MIT](https://github.com/Clustox/n8n-nodes-emailverify/blob/main/LICENSE) 