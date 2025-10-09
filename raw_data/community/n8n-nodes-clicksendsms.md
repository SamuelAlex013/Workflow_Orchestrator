ClickSend n8n Node
Overview
The ClickSend n8n node allows you to interact with ClickSend's API to perform various messaging actions and trigger workflows on incoming messages. This node provides actions to send SMS, MMS, Fax, Voice messages, Letters, and Postcards, and it can also trigger workflows when an SMS is received.

Features
Actions:
Send SMS
Send SMS to Contact List
Send Fax
Send Voice Message
Send MMS
Send Letter
Send Postcard
Trigger:
Receive inbound SMS
Requirements
An active ClickSend account.
API credentials from ClickSend.
n8n workflow automation tool.
Installation
Clone or download this repository.
Install n8n if you haven't already:
bash
Copy code
npm install n8n -g
Add the ClickSend node to your n8n setup.
Configuration
Credentials:

Obtain your API key from ClickSend.
Add the ClickSend credentials in n8n by navigating to Credentials and adding ClickSend API.
Node Parameters:

Send SMS:
From: The sender's phone number.
To: The recipient's phone number.
Message: The message content.
Send SMS to Contact List:
Contact List ID: The ID of the contact list.
Message: The message content.
Send Fax:
From: The sender's fax number.
To: The recipient's fax number.
Media File URL: The URL of the media file.
Subject: The subject of the fax.
Send Voice Message:
From: The sender's number.
To: The recipient's number.
Voice Message: The voice message content.
Send MMS:
From: The sender's number.
To: The recipient's number.
Media File URL: The URL of the media file.
Subject: The subject of the MMS.
Body: The body of the message.
Send Letter:
Address Details: Details of the recipient's address.
Letter Content: The content of the letter.
Send Postcard:
From: The sender's address.
To: The recipient's address.
Message: The message content.
Image URL: The URL of the image for the postcard.
Trigger - Receive Inbound SMS:
Setup a webhook in ClickSend to trigger this node when an SMS is received.
Usage
Send SMS Example:

Add the ClickSend node to your workflow.
Select Send SMS as the action.
Fill in the required parameters (From, To, Message).
Execute the workflow.
Receive Inbound SMS Example:

Add the ClickSend Trigger node to your workflow.
Configure ClickSend to send incoming SMS data to the n8n webhook URL.
Define the workflow actions to be triggered on receiving an SMS.
Error Handling
Ensure that all required parameters are correctly filled.
Verify your ClickSend API credentials.
Check the ClickSend API documentation for detailed error codes and messages.
Support
For any issues or questions, please refer to the ClickSend API documentation or create an issue in this repository.
