# n8n-nodes-anchorbrowser

An n8n community node for integrating with the Anchor Browser API. This node provides comprehensive browser automation capabilities including session management, web scraping, AI-powered tasks, and OS-level control.

## Features

### Browser Sessions
- **Create Session**: Start new browser sessions with customizable configurations
- **Get Session**: Retrieve details of specific sessions
- **List All Sessions**: Get status of all active sessions
- **End Session**: Terminate specific sessions
- **End All Sessions**: Terminate all active sessions
- **Get Recordings**: Retrieve session recordings
- **Get Downloads**: Get session downloads

### Profiles
- **Get Profile**: Retrieve profile details
- **List Profiles**: View all available profiles
- **Update Profile**: Modify existing profiles (description only)
- **Delete Profile**: Remove profiles

### Tools
- **Fetch Webpage**: Get webpage content as HTML or Markdown (requires either Session ID or URL)
- **Perform Web Task**: Execute AI-powered web tasks using various agents (requires either Session ID or URL)
- **Take Screenshot**: Capture screenshots with customizable options (requires either Session ID or URL)

> **Note**: Tools operations are flexible - you can either provide a Session ID to use an existing session, or provide a URL and let the system create a new session automatically. This makes the Tools operations perfect for quick, one-off tasks without needing to manage sessions manually.

### OS Level Control
- **Mouse Actions**: Click, double-click, move, drag and drop (requires Session ID)
- **Keyboard Input**: Type text, use shortcuts (requires Session ID)
- **Scrolling**: Scroll pages with customizable parameters (requires Session ID)
- **Clipboard**: Get/set clipboard content, copy/paste text (requires Session ID)
- **Navigation**: Navigate to URLs (requires Session ID)
- **Screenshots**: Capture current session screenshots (requires Session ID)

## Installation

1. Install the node package:
```bash
npm install n8n-nodes-anchorbrowser
```

2. Or build from source:
```bash
git clone https://github.com/anchorbrowser/n8n-nodes-anchorbrowser.git
cd n8n-nodes-anchorbrowser
npm install
npm run build
```

## Configuration

### Credentials

1. Get your API key from [Anchor Browser Dashboard](https://app.anchorbrowser.io?utm_source=n8n-node)
2. In n8n, go to Credentials and create a new "Anchor Browser API" credential
3. Enter your API key and base URL (default: https://api.anchorbrowser.io)

### Node Usage

1. Add the "Anchor Browser" node to your workflow
2. Select the resource type (Browser Session, Profile, Tools, etc.)
3. Choose the operation you want to perform
4. Configure the parameters as needed
5. Connect the node to your workflow

## Examples

### Basic Web Scraping

1. **Create Session**: Start a new browser session
2. **Navigate**: Go to the target website using OS Control
3. **Fetch Webpage**: Get the page content as HTML or Markdown
4. **End Session**: Clean up the session

### AI-Powered Task Automation

1. **Perform Web Task**: Use AI to complete tasks like form filling or data extraction (provides URL directly)
2. **Get Results**: Retrieve the task results

### Session-Based Automation

1. **Create Session**: Start a browser session
2. **Navigate**: Go to target website using OS Control
3. **Mouse Actions**: Click buttons, fill forms using OS Control
4. **Take Screenshot**: Capture the result
5. **End Session**: Clean up

### Profile Management

1. **List Profiles**: View all available profiles
2. **Get Profile**: Retrieve specific profile details
3. **Update Profile**: Modify profile description
4. **Delete Profile**: Remove unused profiles

## Configuration Options

### Session Configuration
- **Initial URL**: Starting page for the browser
- **Recording**: Enable/disable video recording
- **Timeouts**: Set maximum duration and idle timeouts
- **Live View**: Configure read-only viewing options

### Browser Configuration
- **Profile Management**: Use existing profiles or create new ones
- **Ad Blocking**: Enable/disable ad blocking
- **Captcha Solving**: Configure AI-powered captcha solving
- **Viewport**: Set browser window dimensions
- **Headless Mode**: Run browser in headless or headful mode
- **Web Security**: Disable web security features if needed

### Proxy Configuration
- **Anchor Proxies**: Use Anchor's residential, mobile, or government proxies
- **Custom Proxies**: Configure your own proxy servers
- **Geographic Targeting**: Select specific countries, regions, or cities

### Tools Configuration
- **Session ID**: Optional - if not provided, a new session will be created automatically
- **URL**: Required for Tools operations if Session ID is not provided
- **Format**: Choose between HTML and Markdown for webpage content
- **AI Models**: Select from various AI providers (OpenAI, Groq, etc.)
- **Screenshot Options**: Configure image quality, dimensions, and capture settings

## API Reference

For detailed API documentation, visit [Anchor Browser API Docs](https://docs.anchorbrowser.io?utm_source=n8n-node).

## Support

- **Documentation**: [https://docs.anchorbrowser.io?utm_source=n8n-node](https://docs.anchorbrowser.io?utm_source=n8n-node)
- **Support**: [support@anchorbrowser.io](mailto:support@anchorbrowser.io)
- **GitHub Issues**: [https://github.com/anchorbrowser/n8n-nodes-anchorbrowser/issues](https://github.com/anchorbrowser/n8n-nodes-anchorbrowser/issues)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and submit pull requests to our [GitHub repository](https://github.com/anchorbrowser/n8n-nodes-anchorbrowser).

## Changelog

### v0.1.0
- Initial release
- Browser session management (create, get, list, end)
- Profile management (get, list, update, delete)
- Tools operations (fetch webpage, perform web task, screenshot)
- OS-level control (mouse, keyboard, scrolling, clipboard, navigation)
- Flexible session handling - Tools operations can work with or without existing sessions
- Comprehensive parameter validation and error handling
- Support for binary data (screenshots) with proper n8n formatting
- AI-powered task execution with multiple provider support