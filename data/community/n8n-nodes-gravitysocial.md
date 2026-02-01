# n8n-nodes-mixpost

This is an n8n community node that lets you integrate [Mixpost](https://mixpost.app) with your n8n workflows.

Mixpost is a self-hosted social media management software that helps you schedule and manage your social media content across multiple platforms including Facebook, Twitter/X, Instagram, LinkedIn, Pinterest, TikTok, YouTube, and more.

[n8n](https://n8n.io/) is a workflow automation platform.

## 🚀 Installation

### Automatic - From n8n UI (Recommended)

1. Navigate to **Settings** → **Community Nodes** in your n8n instance
2. Click **Install**
3. Enter `n8n-nodes-mixpost` in the package name field
4. Click **Install** to add it to your n8n instance

### Manual - Command Line Installation

Use this method if your n8n instance doesn't support installation through the in-app GUI.

#### Docker Installation

Access your Docker container:
```bash
docker exec -it <n8n_container_name> sh
```

Create `~/.n8n/nodes` if it doesn't already exist, and navigate into it:

```bash
mkdir ~/.n8n/nodes
cd ~/.n8n/nodes
npm init -y
```

Install the Mixpost node package:

```bash
npm install n8n-nodes-mixpost
```

Restart your n8n instance to load the new node.

#### Non-Docker Installation

Navigate to ` ~/.n8n`, and check if a `custom` folder exists. If not, create it, then add a new package.json file inside.

```bash
mkdir -p ~/.n8n/custom
npm init -y
```

Then, install the Mixpost node package:

```bash
npm install n8n-nodes-mixpost
```

Restart n8n to load the new node.

## 📋 Operations

### 📝 Posts
| Operation | Description |
|-----------|-------------|
| **Create** | Create a new social media post with content, media, and scheduling options |
| **Get** | Retrieve a specific post by UUID |
| **Get Many** | Retrieve multiple posts with filtering by status, account, or tags |
| **Update** | Update an existing post's content, media, or schedule |
| **Delete** | Delete a single post |
| **Delete Bulk** | Delete multiple posts at once |
| **Schedule** | Schedule a post |
| **Add to Queue** | Add a post to the publishing queue |
| **Approve** | Approve a post for publishing |

### 👥 Accounts
| Operation | Description |
|-----------|-------------|
| **Get** | Retrieve details of a specific social media account |
| **Get Many** | List all connected social media accounts in your workspace |

### 🖼️ Media
| Operation | Description |
|-----------|-------------|
| **Upload** | Upload images or videos |
| **Get** | Retrieve a specific media file by UUID |
| **Get Many** | List all media files in your workspace |
| **Update** | Update media file data (Alt Text) |
| **Delete** | Delete a media file from your workspace |

### 🏷️ Tags
| Operation | Description |
|-----------|-------------|
| **Create** | Create a new tag with name and color |
| **Get** | Retrieve a specific tag by UUID |
| **Get Many** | List all tags in your workspace |
| **Update** | Update tag properties (name, color) |
| **Delete** | Delete a tag from your workspace |

## 🔑 Credentials Setup

### Prerequisites
1. A running Mixpost instance
2. Admin access to generate API tokens

### Steps to Configure

1. **Generate API Token in Mixpost:** 
   - Read the [Mixpost API documentation](https://docs.mixpost.app/api/#generate-a-token) to learn how to generate an API token.
2. **Configure in n8n:**
   - In n8n, go to **Overview** → **Create Workflow**
   - Open nodes panel
   - Search for "Mixpost"
   - Add an **Mixpost** action to your workflow
   - Click on **Credentials** → **Create new credential**
   - Enter the following:
     - **Mixpost URL**: Your Mixpost instance URL with core path (e.g., `https://mixpost.yourdomain.com/mixpost`)
     - **Access Token**: The token you generated in step 1
   - Click **Save**

## 🔧 Workspace UUID

All operations require a Workspace UUID. To find yours:

1. Log in to Mixpost
2. Navigate to **Admin Console** -> **Workspaces**
3. Click **View** icon for your workspace.
4. Find the UUID in the **Usage in API** section.

## 📊 Supported Social Platforms

Mixpost supports posting to:
- ✅ Facebook Pages
- ✅ X
- ✅ Instagram (Business accounts)
- ✅ Threads
- ✅ LinkedIn (Profiles & Pages)
- ✅ Pinterest
- ✅ TikTok
- ✅ YouTube
- ✅ Google Business Profile
- ✅ Mastodon
- ✅ Bluesky

## ⚙️ Advanced Features

### Pagination
When using "Get Many" operation for **post** or **media** resource, you can control pagination:
- **Per Page Limit**: Set how many results to return per page (default is 50, max is 100)


### Filtering
Posts can be filtered by:
- **Status**: draft, scheduled, published, failed
- **Account ID**: Filter by specific social account
- **Tag**: Filter by tag name
- **Page**: Navigate through paginated results

## 🛠️ Development

### Prerequisites
- Node.js 18+
- npm or yarn
- TypeScript knowledge

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/inovector/n8n-nodes-mixpost.git
cd n8n-nodes-mixpost

# Install dependencies
npm install

# Build the node
npm run build

# Run in development mode (watch for changes)
npm run dev

# Run linter
npm run lint

# Format code with Prettier
npm run format

# Run tests (if available)
npm test
```

## 📚 Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Mixpost Documentation](https://docs.mixpost.app)
- [Mixpost API Reference](https://docs.mixpost.app/api)
- [n8n Workflow Examples](https://n8n.io/workflows)
- [Report Issues](https://github.com/inovector/n8n-nodes-mixpost/issues)

## 📄 License

[MIT License](https://github.com/inovector/n8n-nodes-mixpost/blob/master/LICENSE.md)

## 🤝 Support

Need help? Here's how to get support:

1. **Documentation First**: Check the [Mixpost docs](https://docs.mixpost.app)
2. **GitHub Issues**: [Report bugs or request features](https://github.com/inovector/n8n-nodes-mixpost/issues)
3. **Mixpost Community**: Join our community channels for help and discussions:
   - 💬 [Discord Server](https://mixpost.app/discord) - Real-time chat support
   - 🐦 [Facebook Group](https://www.facebook.com/groups/getmixpost) - Latest updates and announcements
4. **n8n Community**: Ask in the [n8n community forum](https://community.n8n.io)

## 🎯 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

### Development Workflow

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/n8n-nodes-mixpost.git`
3. **Create** a feature branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes and test thoroughly
5. **Commit** with clear messages: `git commit -m 'Add amazing feature'`
6. **Push** to your fork: `git push origin feature/amazing-feature`
7. **Open** a Pull Request with a detailed description

### Code Standards
- Follow existing code style
- Update documentation as needed
- Run `npm run format` & `npm run lint`  before submitting

## 🙏 Acknowledgments

- The n8n team for the amazing workflow automation platform
- The Mixpost team behind the coolest self-hosted social media management tool
- All contributors who help improve this node

---

**Made with ❤️ by [Inovector](https://inovector.com)**

*Star ⭐ this repository if you find it helpful!*