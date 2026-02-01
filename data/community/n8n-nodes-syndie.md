# Syndie n8n Community Node

Easily connect your n8n workflows to [Syndie.io](https://syndie.io) using OAuth2 and webhooks.

## Features

-   Secure OAuth2 authentication (PKCE flow)
-   Webhook trigger for Syndie events
-   Send webhook registration to your backend
-   Use with Google Sheets, HTTP Request, and more

---

## Getting Started

### 1. Install the Node

```bash
npm install n8n-nodes-syndie
```

Or, for local development:

```bash
npm run build
npm link
# In your n8n custom directory:
npm link n8n-nodes-syndie
```

### 2. Add the Syndie Node to Your Workflow

* In n8n, search for "Syndie" in the nodes panel.
* Drag the node into your workflow.

### 3. Connect to Syndie.io (OAuth2)

* Click the node and select "Syndie OAuth2 API" credentials.
* Click "Connect" and follow the OAuth2 flow.


### 4. Webhook Registration

* Execute the node to send the webhook url to the backend for testing 
* Alternatively you can just activate your n8n workflow to execute this node and send the webhook to the backend

---

## Example Workflow: Syndie → Google Sheets

1.  **Syndie Trigger Node**
    * Triggers on Syndie webhook event
2.  **Google Sheets Node**
    * Appends received data to a sheet

### Sample Workflow Steps

* Add the Syndie node (as trigger)
* Add a Google Sheets node (as action)
* Connect them
* Map the incoming data from Syndie to the columns in Google Sheets


## Troubleshooting

* Ensure OAuth2 credentials are set up in n8n
* Check the n8n logs for webhook registration errors

---

## License

MIT

## Support

For help, contact [support@syndie.io](mailto:support@syndie.io)

## Links

* [Syndie.io](https://syndie.io)
* [n8n Documentation](https://docs.n8n.io)
