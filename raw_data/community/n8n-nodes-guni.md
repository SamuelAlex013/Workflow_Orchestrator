# n8n Guni Node

A Guni node for sending as well as receivng SMS And MMS via the Guni API.

## Features

Send promotional or notification SMS

Send promotional or notification MMS

Receive SMS or MMS

## Installation

Install from npm:

```
bash or powershell:
npm install n8n-nodes-guni
```

## Operations

The Guni SMS node supports:

SMS

Send SMS – Send messages to one or multiple phone numbers.

Campaign Type – Promotional or Notification.

Sender ID – Sender ID from Your Sender Id list in Node.

MMS

Send MMS – Send multimedia messages with a media URL.

Campaign Type – Promotional or Notification.

Sender ID – Sender ID from Your Sender Id list in Node.


## Credentials

To use this node, you need a Guni API token.

Sign up for a Guni account.
* [Didn't have account? Want to SignUp](https://app.gunisms.com.au/signup)

Want to send using your Business name ?
* [Here is how you can get one.](https://help.gunisms.com.au/kb/set-sender-id/)

Generate an API token from your Guni dashboard.
* [Check Here How to get API token from your Guni dashboard.](https://help.gunisms.com.au/kb/how-to-generate-api-token/)

Add a new credential in n8n:

Credential Name: Guni API

API Token: Your generated token

The node automatically validates the token when saving.

## Compatibility

Minimum n8n version: 2.0.0


## Usage

Add the Guni SMS or Guni MMS node to your workflow.

Select your Sender ID from your account.

Choose Campaign Type.

Enter your SMS or MMS content in the Message field or it will take it from previous node also.

Also Enter URL in case of MMS.

Provide input data JSON with contacts :
```
{
  "body": {
    "contacts": ["61439554019", "61439543139"],
    "message": "Hello test SMS"
  }
}
```

```
{
  "body": {
    "contacts": ["61439543031", "61439551969"],
    "message": "Hello test MMS"
     "media": "https://example.com/myImage.jpg",
  }
}
```

Execute the workflow to send SMS or MMS.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Gunisms help](https://help.gunisms.com.au/)

## Version history

v1.0.2 – Initial release. Supports sending as well as receiving SMS And MMS via Guni API with dynamic sender IDs and message type selection.


 