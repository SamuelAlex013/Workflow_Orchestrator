# n8n-nodes-hedy

[![npm version](https://badge.fury.io/js/n8n-nodes-hedy.svg)](https://www.npmjs.com/package/n8n-nodes-hedy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Community Node](https://img.shields.io/badge/n8n-Community%20Node-orange)](https://n8n.io)

This is an n8n community node that lets you integrate [Hedy](https://hedy.bot) - your AI-powered meeting intelligence assistant - into your n8n workflows.

Hedy helps you be the brightest person in the room by providing real-time transcription, meeting summaries, action items, and intelligent insights from your meetings.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## 🚀 Installation

### Community Nodes (Recommended)

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-hedy`
3. Click **Install**

### Manual Installation

```bash
# Navigate to your n8n custom nodes folder
cd ~/.n8n/custom

# Install the package
npm install n8n-nodes-hedy
```

### Docker Installation

Add the following to your docker-compose.yml:

```yaml
n8n:
  image: n8nio/n8n
  environment:
    - N8N_CUSTOM_EXTENSIONS=n8n-nodes-hedy
```

## 🔑 Authentication

1. Get your API key from [Hedy Dashboard](https://app.hedy.bot):
   - Navigate to Settings → API
   - Click "Generate New Key"
   - Copy the key (starts with `hedy_live_`)

2. In n8n:
   - Go to Credentials
   - Create new "Hedy API" credential
   - Paste your API key
   - Click "Save"

## 📦 Nodes Included

### Hedy Trigger
Receives real-time webhook notifications when events occur in Hedy:

- **Session Created** - When a new meeting session starts
- **Session Ended** - When a meeting session completes
- **Highlight Created** - When a highlight is created during a meeting
- **Todo Exported** - When a todo item is exported

### Hedy
Performs actions and retrieves data from Hedy:

- **Sessions**
  - Get Session - Retrieve detailed session information
  - Get Many Sessions - List multiple sessions with pagination
  
- **Highlights**
  - Get Highlight - Retrieve specific highlight details
  - Get Many Highlights - List multiple highlights
  
- **Todos**
  - Get Many Todos - List all todo items
  - Get Todos by Session - Get todos for a specific session

## 🎯 Example Workflows

### 1. Meeting Summary to Slack
Send meeting summaries to Slack when sessions end:

```
[Hedy Trigger: Session Ended]
    → [Hedy: Get Session Details]
    → [Slack: Send Message]
```

### 2. Highlight Collection to Notion
Save important highlights to a Notion database:

```
[Hedy Trigger: Highlight Created]
    → [Hedy: Get Highlight Details]
    → [Notion: Create Database Entry]
```

### 3. Todo Export to Project Management
Export todos to your project management tool:

```
[Hedy Trigger: Todo Exported]
    → [Jira/Trello/Asana: Create Task]
```

### 4. Daily Meeting Report
Generate daily meeting reports:

```
[Schedule Trigger: Daily at 5 PM]
    → [Hedy: Get Many Sessions (today)]
    → [Transform: Format Report]
    → [Email: Send Report]
```

## 📊 Data Structures

### Session Object
```json
{
  "id": "sess_abc123",
  "title": "Team Standup",
  "startTime": "2024-01-10T10:00:00Z",
  "endTime": "2024-01-10T10:30:00Z",
  "duration": 1800,
  "transcript": "Full transcript...",
  "conversations": [...],
  "meeting_minutes": "Meeting notes...",
  "recap": "Summary...",
  "user_todos": [...],
  "topic": {...}
}
```

### Highlight Object
```json
{
  "id": "high_xyz789",
  "sessionId": "sess_abc123",
  "timestamp": "2024-01-10T10:15:00Z",
  "title": "Key Decision",
  "rawQuote": "Original quote...",
  "cleanedQuote": "Cleaned quote...",
  "mainIdea": "Core concept...",
  "aiInsights": "Analysis..."
}
```

### Todo Object
```json
{
  "id": "todo_123",
  "sessionId": "sess_abc123",
  "text": "Follow up with marketing team",
  "dueDate": "2024-01-15",
  "completed": false,
  "topic": {...}
}
```

## ⚙️ Configuration

### Webhook Limits
- Maximum of 10 webhooks per Hedy account
- Webhooks must use HTTPS URLs
- Each webhook receives a unique signing secret for security

### Pagination
- Default page size: 50 items
- Maximum page size: 100 items
- Supports cursor-based pagination for large datasets

### Rate Limiting
The API follows standard rate limiting practices. If you encounter rate limit errors, implement exponential backoff in your workflows.

## 🔒 Security

### Webhook Signature Verification
All webhooks include an `X-Hedy-Signature` header for verification:

1. The signature is an HMAC SHA-256 hash of the request body
2. Each webhook has a unique signing secret
3. Signature verification is enabled by default (recommended)

### API Key Security
- Never share your API key publicly
- Rotate keys regularly (every 90 days recommended)
- Use n8n's built-in credential encryption
- Keys can be revoked instantly from the Hedy dashboard

## 🐛 Troubleshooting

### Common Issues

**Webhook Registration Fails**
- Ensure your n8n instance uses HTTPS
- Check you haven't exceeded the 10 webhook limit
- Verify your API key has the necessary permissions

**No Data Returned**
- Verify the resource ID exists
- Check your API key is valid
- Ensure you have access to the requested resource

**Signature Verification Fails**
- Don't modify webhook payloads
- Ensure signature verification is using the correct secret
- Check for clock skew between servers

## 📚 Resources

- [Hedy Website](https://hedy.bot)
- [Hedy API Documentation](https://api.hedy.bot/docs)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Community Forum](https://community.n8n.io)

## 💬 Support

- **Hedy Support**: support@hedy.bot
- **API Issues**: api@hedy.bot
- **n8n Node Issues**: [GitHub Issues](https://github.com/HedyAI/n8n-nodes-hedy/issues)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the n8n team for their excellent workflow automation platform
- Thanks to the Hedy team for providing comprehensive API documentation
- Thanks to all contributors and users of this node

## 📈 Version History

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each version.

---

Made with ❤️ by the Hedy team