# n8n-nodes-ynab

This is a n8n community node. It lets you use **YNAB** in your n8n workflows.

**YNAB (You Need A Budget)** is a personal finance tool that helps you manage your money by creating spending plans and understanding where your money goes.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node currently supports the following operations with YNAB:

- **Fetch budgets**: Retrieve the list of budgets defined in your YNAB account.
- **Fetch categories**: Retrieve the list of categories for a budget in your YNAB account.
- **Fetch transactions**: Retrieve the list of transactions for a budget in your YNAB account.

## Credentials

This node uses a **Personal Access Token** for authentication.

### How to get your token:

1. Log in to your YNAB account.
2. Go to the [Personal Access Tokens page](https://api.ynab.com/#personal-access-tokens).
3. Generate a new token and copy it.
4. In n8n, create new credentials of type **YNAB API** and paste your token there.

## Compatibility

- Minimum n8n version: 1.65.2
- Tested on versions: 1.86.1
- Known issues: None so far

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [YNAB official website](https://www.ynab.com/)
- [YNAB API documentation](https://api.ynab.com/)
