![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# ZeptoMail integration with N8N

## About ZeptoMail
[ZeptoMail](https://www.zoho.com/zeptomail/) is a dedicated email service built specifically for user-triggered transactional emails. Businesses can integrated with ZeptoMail to deliver time sensitive emails like OTPs, password reset emails, welcome emails and more. The [N8N](https://n8n.io/) integration with ZeptoMail allows applications to create workflows to automatically send transactional emails for set triggers. 

## Pre-requisites

- N8n admin account (https://app.n8n.cloud/login)
- ZeptoMail account
- Verified domain added to ZeptoMail

## Installation
You can install the n8n ZeptoMail node through the npm package "n8n-nodes-zohozeptomail"
- Follow the steps below to install:
   - Login to your npm account.
   - Navigate to the settings section.
   - In the community nodes section -> Install community node.
   - Enter the npm package name: n8n-nodes-zohozeptomail.
   - The node will be installed successfully.

## Configuration
Once you install the package, you should integrate with n8n to start sending emails:
- Login to your n8n account.
- Click the down-arrow next to the <b>Create workflow</b> button and click Create credentials.
- In the Add credentials dialogue box, choose the appropriate authorization and access token URL.
- Go to the [Zoho developer console](https://api-console.zoho.com/) to generate a new client id and client secret. These parameters will connect ZeptoMail and n8n.
- Click Get started if you do not have any new client. If you have an existing client, click Add client.
- Select Server-based applications in the client type window.
- Provide an appropriate client name, your domain value in the homepage URL field, and the redirect URL copied from the Add credentials dialog box.
- Click Create to generate the client id and client secret.
- Copy the generated values and paste them in the Add credentials dialog box.
- The connection is established. You can now create workflows to send emails.

## Create workflows
- Click the <b>Create workflow</b> button.
- Select the appropriate trigger for which you wish to send emails.
- Click the Action in App option and lookup ZeptoMail from the list.
- Choose the type of action you wish to perform - send email, send template email.
- You can test your configuration by selecting the Test workflow button.




