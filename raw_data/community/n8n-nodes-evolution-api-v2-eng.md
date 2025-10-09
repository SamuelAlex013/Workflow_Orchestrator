# N8N Evolution API v2 Community Node

This is a community node for N8N that allows integration with Evolution API v2 for WhatsApp.

## 🚀 Features

- **Instance Management**: Create, connect, disconnect and manage WhatsApp instances
- **Message Sending**: Send text and media messages
- **Group Management**: Create groups and search members
- **Chat Verification**: Check if a number is WhatsApp
- **Webhooks**: Configure webhooks for events
- **Integrations**: Support for Chatwoot integration

## 📦 Installation

### Via NPM (Recommended)

```bash
npm install n8n-nodes-evolution-api-v2-eng
```

### Via N8N Community Nodes

1. Go to **Settings** > **Community Nodes**
2. Click **Install**
3. Enter: `n8n-nodes-evolution-api-v2-eng`
4. Click **Install**

## 🔧 Configuration

### Credentials

1. Create a new credential of type **Evolution API**
2. Configure:
   - **Server URL**: URL of your Evolution API server
   - **API Token**: API authentication token

### Available Resources

#### Instance
- **Create Instance**: Creates a new WhatsApp instance
- **Fetch Instances**: Lists all available instances
- **Connect Instance**: Connects to a specific instance
- **Restart Instance**: Restarts an instance
- **Connection State**: Checks connection state
- **Logout**: Logs out of an instance
- **Delete Instance**: Removes an instance
- **Set Presence**: Sets presence status

#### Message
- **Send Text**: Sends a text message
- **Send Image**: Sends an image with caption

#### Group
- **Create Group**: Creates a new group
- **Find Members**: Lists group members

#### Chat
- **Check WhatsApp**: Checks if a number is WhatsApp

#### Event
- **Webhook**: Configures webhooks for events

#### Integration
- **Chatwoot**: Configures Chatwoot integration

## 🛠️ Development

### Prerequisites

- Node.js 18+
- npm or yarn

### Local Installation

```bash
git clone https://github.com/farazpawle/n8n-nodes-evolution-api-v2-eng.git
cd n8n-nodes-evolution-api-v2-eng
npm install
```

### Available Scripts

```bash
# Build project
npm run build

# Development with watch
npm run dev

# Linting
npm run lint

# Formatting
npm run format

# Release (patch, minor, major)
npm run release:patch
npm run release:minor
npm run release:major
```

## 📝 Usage Examples

### Send Text Message

```javascript
// Node configuration
{
  "resource": "message",
  "operation": "sendText",
  "instanceName": "my-instance",
  "number": "5511999999999",
  "messageText": "Hello! This is a test message."
}
```

### Create Group

```javascript
// Node configuration
{
  "resource": "group",
  "operation": "createGroup",
  "instanceName": "my-instance",
  "subject": "Test Group",
  "participants": ["5511999999999", "5511888888888"]
}
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Faraz Pawle** (Fork maintainer)
- Email: farazkhld@gmail.com
- GitHub: [@farazpawle](https://github.com/farazpawle)

**Original Author: JF Cardoso Santos**
- Email: jfcardososantos@gmail.com
- GitHub: [@jfcardososantos](https://github.com/jfcardososantos)

## 🔗 Links

- [N8N](https://n8n.io/)
- [Evolution API](https://doc.evolution-api.com/)
- [NPM Package](https://www.npmjs.com/package/n8n-nodes-evolution-api-v2-eng)

## 📈 Versioning

This project uses [SemVer](http://semver.org/) for versioning. To see available versions, check the [tags in this repository](https://github.com/farazpawle/n8n-nodes-evolution-api-v2-eng/tags).

## 🆘 Support

If you encounter any problems or have questions, please:

1. Check the [Evolution API documentation](https://doc.evolution-api.com/)
2. Open an [issue on GitHub](https://github.com/farazpawle/n8n-nodes-evolution-api-v2-eng/issues)
3. Contact via email: farazkhld@gmail.com 