![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)
# Zoho TeamInbox integration with n8n
Zoho TeamInbox is a multichannel shared inbox platform that enables teams to manage conversations from business WhatsApp, Telegram, Facebook, Instagram DMs, and emails—all in one shared space that enhance collaboration and transparency.
With n8n’s integration, you can align Zoho TeamInbox with your business processes by custom-designing workflows using triggers and actions to automate your operations.
To learn more about n8n
[n8n homepage](https://n8n.io/).
To learn more about Zoho TeamInbox
[Zoho Calendar homepage]( https://www.zoho.com/teaminbox/ )
In case of any technical queries 
[Contact sales]( https://www.zoho.com/teaminbox/contact.html )
## Pre-requisites
- n8n admin login account (https://app.n8n.cloud/login)
- TeamInbox account
- Verified domain added to TeamInbox
## Installation 
You can install the nodes for n8n via [npm]( https://www.npmjs.com/ ) with the package name as "n8n-nodes-zohoteaminbox".
- To install :
  - Log in to your n8n account.
  - Navigate to more options->Settings->Community nodes->Install.
  - Enter the package name (n8n-nodes-zohoteaminbox)
  - The node will be installed successfully.

## Configuration 
Follow the steps below to integrate Zoho TeamInbox from n8n.
- Log in to your n8n account.
- Select Create Credential -> Add Credential dialog box -> Enter Zoho TeamInbox OAuth2 API -> Click Continue.
- Copy the Authorized Redirection URL from the connection page.
- Access the [Zoho Developer Console](https://api-console.zoho.com/) to create a new Client ID and Client Secret to establish the connection between n8n and Zoho TeamInbox.
- Click on Get Started if you have no existing Client. If you have an existing client, click on Add Client in the top-right corner. Select Server-based Applications in the Client Type window.
- Provide the appropriate Client Name and your domain in the Homepage URL along with the Authorized Redirect URL copied from the Connection page.
- Click Create to generate the Client ID and Client Secret.
- Enter the Client ID and Client secret in the Connection Page and click Connect my account.
- Now, the connection between n8n and Zoho TeamInbox is established, and the next step is to create your workflow.
- Click Create Workflow -> Add first step -> search and select Zoho TeamInbox on the right pane.
- Build your desired workflow with the list of actions (Send an email or Create contact).
- Once the workflow is created, you can test it by selecting the Test Workflow option.
## Troubleshooting 
Write to us in case of any queries
[Contact support]( support@zohoteaminbox.com )

### Description
This page explains the integration of Zoho TeamInbox with n8n. n8n is a powerful, open-source workflow automation software that allows you to connect with different apps and automate tasks with ease.

For more information on Zoho TeamInbox: https://www.zoho.com/teaminbox/
  
### Required :
- Zoho TeamInbox account and n8n admin account.
- Module installation and configuration
- Information on how the integration between Zoho TeamInbox and n8n can be made is found in this Readme file.
- For further queries, visit :  https://www.zoho.com/teaminbox/contact.html  


