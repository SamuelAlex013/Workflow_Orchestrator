# n8n-nodes-anymailfinder

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node that lets you use [Anymailfinder](https://anymailfinder.com) in your n8n workflows.

Anymailfinder is a powerful email discovery and verification service that helps you find and verify email addresses for lead generation, sales prospecting, and marketing campaigns.

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
3. Enter `n8n-nodes-anymailfinder` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

### Person Email
- **Find Email**: Find a person's email address by providing their name and company information

### Company Emails  
- **Find Emails**: Find all email addresses associated with a company

### Decision Maker
- **Find Email**: Find decision maker's email address at a company

### LinkedIn Email
- **Find Email**: Find email address associated with a LinkedIn profile URL

### Email Verification
- **Verify Email**: Verify if an email address is valid and deliverable

### Account Info
- **Get Info**: Retrieve account details and remaining API credits

## Credentials

You need an Anymailfinder API key to use this node. You can get your API key by:

1. Creating an account at [Anymailfinder](https://anymailfinder.com)
2. Going to **My Account > API** in your dashboard
3. Clicking **Enable API** to generate your API key

The API key should be entered in the credentials configuration in n8n.

## Compatibility

- Minimum n8n version: **0.198.0**
- Tested with n8n version: **1.0.0+**

## Usage

### Finding a Person's Email

1. Add the Anymailfinder node to your workflow
2. Select **Person Email** as the resource
3. Choose **Find Email** as the operation
4. Enter the person's full name
5. Provide either the company domain (e.g., "apple.com") or company name (e.g., "Apple Inc")
6. Configure your Anymailfinder API credentials
7. Execute the workflow

### Verifying Email Addresses

1. Add the Anymailfinder node to your workflow
2. Select **Email Verification** as the resource
3. Choose **Verify Email** as the operation
4. Enter the email address to verify
5. Execute the workflow

### Getting Account Information

1. Add the Anymailfinder node to your workflow
2. Select **Account Info** as the resource
3. Choose **Get Info** as the operation
4. Execute the workflow to see your remaining credits

## Cost Information

- **Person Email Search**: 1 credit (only charged for valid emails found)
- **Company Email Search**: 1 credit per valid email found
- **Decision Maker Search**: 2 credit per valid email found
- **LinkedIn Email Search**: 2 credit per valid email found
- **Email Verification**: 0.2 credits per verification
- **Account Info**: Free

Searches that don't find valid emails or return risky/blacklisted emails are free. Duplicate searches within 30 days are also free.

## Rate Limits

Anymailfinder doesn't impose hard rate limits. The system automatically scales to handle high volumes of requests. However, searches are performed in real-time and can take up to 2 minutes for complex queries.

## Error Handling

The node includes comprehensive error handling for:
- Invalid API credentials
- Missing required parameters
- API timeouts
- Network errors
- Invalid email formats

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Anymailfinder API documentation](https://anymailfinder.com/email-finder-api/docs)
* [Anymailfinder website](https://anymailfinder.com)

## License

[MIT](https://github.com/your-username/n8n-nodes-anymailfinder/blob/master/LICENSE.md)
