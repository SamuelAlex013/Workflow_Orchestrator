# n8n-nodes-smtp-simple

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

A simple SMTP community node for [n8n](https://n8n.io/) that allows you to send emails via any SMTP server.

## Features

- ✅ Simple SMTP email sending
- ✅ Support for both plain text and HTML emails
- ✅ CC and BCC recipients
- ✅ Custom reply-to addresses
- ✅ Use data from previous nodes with expressions
- ✅ Error handling with continue on fail option
- ✅ Works with any SMTP server (Gmail, Outlook, custom servers, etc.)

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-smtp-simple`
4. Agree to the risks of using community nodes
5. Select **Install**

After installation restart n8n to see the new node in the nodes panel.

### Manual Installation

To get started install the package in your n8n root directory:

```bash
npm install n8n-nodes-smtp-simple
```

For Docker-based deployments add the following line before the font installation command in your [n8n custom Docker image](https://docs.n8n.io/integrations/community-nodes/installation/docker/):

```bash
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-smtp-simple
```

## Configuration

### 1. Create SMTP Credentials

Before using the node, you need to set up SMTP credentials:

1. Go to **Settings > Credentials**
2. Click **Add Credential**
3. Select **SMTP** from the list
4. Fill in your SMTP server details:
   - **Host**: Your SMTP server (e.g., `smtp.gmail.com`)
   - **Port**: SMTP port (587 for TLS, 465 for SSL, 25 for plain)
   - **Secure Connection**: Enable for port 465, disable for 587/25
   - **Username**: Your email username
   - **Password**: Your email password or app-specific password
   - **From Email**: Default sender email address
   - **From Name**: Default sender name (optional)

### 2. Using the Node

1. Add the **SMTP Simple** node to your workflow
2. Connect it to a trigger or other nodes
3. Select your SMTP credentials
4. Configure the email parameters:
   - **To Email**: Recipient email (can use expressions like `{{$json["email"]}}`)
   - **Subject**: Email subject line
   - **Email Type**: Choose Text or HTML
   - **Message**: Email content (text or HTML)
   - **Options**: CC, BCC, Reply-To (optional)

## Usage Examples

### Basic Text Email

```javascript
// Previous node data:
{
  "email": "recipient@example.com",
  "name": "John Doe",
  "message": "Hello John, welcome to our service!"
}

// SMTP Simple node configuration:
To Email: {{$json["email"]}}
Subject: Welcome {{$json["name"]}}!
Email Type: Text
Message: {{$json["message"]}}
```

### HTML Email with Data

```javascript
// SMTP Simple node configuration:
To Email: customer@example.com
Subject: Order Confirmation #{{$json["orderNumber"]}}
Email Type: HTML
Message: |
  <h2>Order Confirmation</h2>
  <p>Dear {{$json["customerName"]}},</p>
  <p>Your order <strong>#{{$json["orderNumber"]}}</strong> has been confirmed.</p>
  <p>Total: ${{$json["total"]}}</p>
  <p>Thank you for your purchase!</p>
```

### Bulk Email from Array

When processing multiple items from previous nodes, the SMTP Simple node will send one email per input item automatically.

## Common SMTP Providers

### Gmail
- Host: `smtp.gmail.com`
- Port: `587`
- Secure: `false`
- Note: Use App Password instead of regular password

### Outlook/Hotmail
- Host: `smtp.live.com`
- Port: `587`
- Secure: `false`

### Yahoo
- Host: `smtp.mail.yahoo.com`
- Port: `587`
- Secure: `false`

### Custom SMTP
Configure according to your provider's documentation.

## Error Handling

The node supports n8n's "Continue on Fail" option. When enabled:
- Failed emails won't stop the workflow
- Error details are returned in the output data
- Successful emails continue to be processed

## Output Data

Each successful email sends returns:
```javascript
{
  "success": true,
  "messageId": "<unique-message-id>",
  "response": "250 OK",
  "to": "recipient@example.com",
  "subject": "Email subject"
}
```

Failed emails (with Continue on Fail enabled):
```javascript
{
  "success": false,
  "error": "Error message details"
}
```

## Development

```bash
# Clone the repository
git clone <repository-url>
cd n8n-node-smtp-simple

# Install dependencies
npm install

# Build the node
npm run build

# Watch for changes during development
npm run dev
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Support

For issues and questions:
- Create an issue in this repository
- Ask in the [n8n community](https://community.n8n.io/)

---

**Note:** This is a community node and is not officially supported by n8n. Use at your own risk and test thoroughly before using in production environments.