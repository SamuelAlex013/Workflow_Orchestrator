# n8n-nodes-napcat

[![npm version](https://badge.fury.io/js/n8n-nodes-napcat.svg)](https://badge.fury.io/js/n8n-nodes-napcat)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive n8n community node for NapCat QQ Bot API integration. This node allows you to seamlessly integrate QQ bot functionality into your n8n workflows, enabling automated messaging, account management, and group operations.

## 🚀 Features

### 📱 Message Operations
- **Send Private Messages**: Send text, images, and other media to individual users
- **Send Group Messages**: Broadcast messages to QQ groups
- **Message History**: Retrieve private and group message history
- **Message Recall**: Recall sent messages when needed

### 👤 Account Operations
- **Account Information**: Get current bot account details
- **Friend Management**: Retrieve and manage friend lists
- **Group Management**: Access and manage group information

### 🏢 Group Operations
- **Group Information**: Get detailed group information
- **Member Management**: Retrieve group member lists
- **Group Settings**: Modify group names and settings

## 📦 Installation

### Method 1: Community Node Installation (Recommended)

1. Open your n8n instance
2. Go to **Settings** → **Community Nodes**
3. Click **Install a community node**
4. Enter package name: `n8n-nodes-napcat`
5. Click **Install** and wait for installation to complete

### Method 2: Manual Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/n8n-nodes-napcat.git
   cd n8n-nodes-napcat
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the project:
   ```bash
   npm run build
   ```

4. Copy the `dist` folder to your n8n community nodes directory:
   ```bash
   # For Docker installations
   docker cp dist/. your-n8n-container:/home/node/.n8n/community-packages/n8n-nodes-napcat/
   
   # For local installations
   cp -r dist ~/.n8n/community-packages/n8n-nodes-napcat/
   ```

5. Restart n8n

## 🔧 Configuration

### Prerequisites

Before using this node, ensure you have:

1. **NapCat Service Running**: Your NapCat QQ bot service must be running and accessible
2. **API Access**: Ensure your NapCat API is properly configured and accessible
3. **Valid Credentials**: Have your NapCat API credentials ready

### Setting Up Credentials

1. In your n8n workflow, add a NapCat node
2. Click on the **Credentials** field
3. Create new credentials with the following information:

   | Field | Description | Example |
   |-------|-------------|---------|
   | **API Base URL** | The base URL of your NapCat API server | `http://localhost:3000` |
   | **Access Token** | API access token (if required) | `your-access-token` |

### Node Parameters

#### Message Operations

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **Resource** | Options | Yes | Choose between "Message" or "Account" |
| **Operation** | Options | Yes | Select the specific operation to perform |
| **User ID** | String | For private messages | Target user's QQ number |
| **Group ID** | String | For group messages | Target group's QQ number |
| **Message Type** | Options | Yes | Choose "Text" or "Image" |
| **Message Content** | String | For text messages | The text content to send |
| **Image URL** | String | For image messages | URL or base64 data of the image |

#### Account Operations

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| **Resource** | Options | Yes | Set to "Account" |
| **Operation** | Options | Yes | Choose "Get Account Info" |

## 📖 Usage Examples

### Example 1: Send a Private Message

1. **Add NapCat Node**: Drag the NapCat node to your workflow
2. **Configure Node**:
   - Resource: `Message`
   - Operation: `Send Private Message`
   - User ID: `123456789` (target user's QQ number)
   - Message Type: `Text`
   - Message Content: `Hello from n8n!`
3. **Execute**: Run the workflow to send the message

### Example 2: Send a Group Message

1. **Add NapCat Node**: Drag the NapCat node to your workflow
2. **Configure Node**:
   - Resource: `Message`
   - Operation: `Send Group Message`
   - Group ID: `987654321` (target group's QQ number)
   - Message Type: `Text`
   - Message Content: `Automated message from n8n workflow`
3. **Execute**: Run the workflow to send the group message

### Example 3: Get Account Information

1. **Add NapCat Node**: Drag the NapCat node to your workflow
2. **Configure Node**:
   - Resource: `Account`
   - Operation: `Get Account Info`
3. **Execute**: Run the workflow to retrieve account information

### Example 4: Advanced Workflow - Automated Response

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Process Data",
      "type": "n8n-nodes-base.function",
      "parameters": {
        "functionCode": "// Process incoming data\nreturn { userId: $json.userId, message: $json.message };"
      }
    },
    {
      "name": "Send QQ Message",
      "type": "n8n-nodes-napcat.napCat",
      "parameters": {
        "resource": "message",
        "operation": "sendPrivateMessage",
        "userId": "={{ $json.userId }}",
        "messageType": "text",
        "messageContent": "={{ $json.message }}"
      }
    }
  ]
}
```

## 🔌 API Reference

This node integrates with the [NapCat API](https://napcat.apifox.cn/226888843e0) and supports the following endpoints:

### Message Endpoints
- `POST /send_private_msg` - Send private messages
- `POST /send_group_msg` - Send group messages
- `POST /get_friend_history_msg` - Get private message history
- `POST /get_group_history_msg` - Get group message history
- `POST /delete_msg` - Recall messages

### Account Endpoints
- `POST /get_login_info` - Get account information
- `POST /get_friend_list` - Get friend list
- `POST /get_group_list` - Get group list

### Group Endpoints
- `POST /get_group_info` - Get group information
- `POST /get_group_member_list` - Get group members
- `POST /set_group_name` - Set group name

## 🛠️ Development

### Prerequisites

- Node.js 18 or higher
- TypeScript 5.0 or higher
- n8n (for testing)

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/n8n-nodes-napcat.git
   cd n8n-nodes-napcat
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Build the project**:
   ```bash
   npm run build
   ```

4. **Run tests**:
   ```bash
   node test-node.js
   ```

### Development Scripts

| Script | Description |
|--------|-------------|
| `npm run build` | Build the TypeScript project |
| `npm run dev` | Start development mode with watch |
| `npm run lint` | Run ESLint for code quality |
| `npm run format` | Format code with Prettier |
| `npm test` | Run the test suite |

### Project Structure

```
n8n-nodes-napcat/
├── dist/                          # Built output
├── credentials/                   # Credential definitions
├── nodes/                        # Node implementations
├── examples/                     # Example workflows
├── src/                          # Source TypeScript files
├── package.json                  # Project configuration
├── tsconfig.json                 # TypeScript configuration
└── README.md                     # This file
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Node Not Appearing in n8n
**Problem**: NapCat node doesn't appear in the node palette
**Solution**: 
- Ensure the node is properly installed
- Restart n8n after installation
- Check n8n logs for any errors

#### 2. Authentication Failed
**Problem**: Getting authentication errors
**Solution**:
- Verify NapCat service is running
- Check API Base URL is correct
- Ensure Access Token is valid (if required)

#### 3. Message Sending Failed
**Problem**: Messages are not being sent
**Solution**:
- Verify User ID or Group ID is correct
- Check NapCat service logs
- Ensure the bot has proper permissions

#### 4. Network Connection Issues
**Problem**: Cannot connect to NapCat API
**Solution**:
- Check network connectivity
- Verify firewall settings
- Ensure NapCat service is accessible

### Debug Mode

Enable debug mode in n8n to see detailed logs:

1. Set environment variable: `N8N_LOG_LEVEL=debug`
2. Restart n8n
3. Check logs for detailed error information

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
1. Check existing issues first
2. Create a new issue with detailed description
3. Include steps to reproduce the problem
4. Provide relevant logs and error messages

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Development Guidelines
- Follow TypeScript best practices
- Write comprehensive tests
- Update documentation
- Follow the existing code style
- Ensure all tests pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [NapCat](https://github.com/Dituon/napcat) - The amazing QQ bot framework
- [n8n](https://n8n.io/) - The powerful workflow automation platform
- [n8n Community](https://community.n8n.io/) - For inspiration and support

## 📞 Support

- **Documentation**: Check this README and the [NapCat API docs](https://napcat.apifox.cn/226888843e0)
- **Issues**: [GitHub Issues](https://github.com/your-username/n8n-nodes-napcat/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/n8n-nodes-napcat/discussions)
- **Community**: [n8n Community Forum](https://community.n8n.io/)

## 🔄 Changelog

### v1.0.0 (2024-01-XX)
- Initial release
- Support for private and group messaging
- Account information retrieval
- Basic error handling and validation

---

**Made with ❤️ for the n8n and NapCat communities**