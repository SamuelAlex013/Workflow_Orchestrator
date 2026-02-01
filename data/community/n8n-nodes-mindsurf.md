# n8n-nodes-mindsurf

This is an n8n community node that provides Playwright-based web browser automation capabilities. It allows you to automate web browser interactions, capture screenshots, extract data, and perform end-to-end testing directly within your n8n workflows.

## Features

Mindsurf provides comprehensive browser automation with the following operation categories:

### 🧭 Navigation
- Navigate to URLs
- Go back/forward in browser history
- Reload pages
- Wait for navigation events

### 📸 Screenshot & PDF
- Capture full page or element screenshots
- Generate PDFs from web pages
- Support for various image formats and quality settings

### 🖱️ Interaction
- Click, double-click, right-click elements
- Type text and fill forms
- Select dropdown options
- Check/uncheck checkboxes
- Hover, focus, and scroll
- Drag and drop
- File uploads
- Mobile gestures (tap, swipe)

### 🔧 Evaluate
- Execute JavaScript in page context
- Extract text, attributes, and properties
- Check element states (visible, enabled, checked)
- Count elements and verify existence

### ⏳ Wait
- Wait for elements to appear/disappear
- Wait for page load states
- Wait for JavaScript functions
- Wait for network requests/responses
- Wait for downloads and popups

### 🌐 Network
- Set HTTP headers and authentication
- Intercept and modify requests
- Mock API responses
- Emulate network conditions
- Block resource types

### 🍪 Storage
- Manage cookies
- Access local storage and session storage
- Save and load browser state

### 🔐 Session Management
- Save login sessions with cookies and localStorage
- Load saved sessions to restore login state
- List and manage multiple saved profiles
- Export/import session profiles for sharing

### ♿ Accessibility
- Get accessibility tree
- Run accessibility audits
- Check ARIA attributes
- Test keyboard navigation

### 📁 File
- Upload files
- Handle downloads
- Manage file chooser dialogs

### 🗂️ Tab
- Open new tabs and windows
- Switch between tabs
- Manage window size and position
- Control fullscreen mode

### 🤖 AI Features
- Natural language commands for browser automation
- Automatic selector detection
- Smart wait strategies
- Proxy rotation with geographic filtering

## Installation

### Community Node (Recommended)

1. Go to **Settings > Community Nodes** in n8n
2. Select **Install**
3. Enter `n8n-nodes-mindsurf` in the package name field
4. Accept the risks and click **Install**

### Manual Installation

```bash
# Navigate to your n8n installation's custom nodes folder
cd ~/.n8n/custom

# Install the node
npm install n8n-nodes-mindsurf
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/dandacompany/n8n-nodes-mindsurf.git

# Install dependencies
cd n8n-nodes-mindsurf
npm install

# Install Playwright browsers
npm run install-browsers

# Build the node
npm run build

# Link for local development
npm link

# In your n8n installation
cd ~/.n8n/custom
npm link n8n-nodes-mindsurf
```

## Usage

1. Add the **Mindsurf** node to your workflow
2. Select a browser (Chromium, Firefox, or WebKit)
3. Choose an operation category
4. Select the specific operation
5. Configure the operation parameters
6. Optionally set browser options (headless mode, viewport size, etc.)
7. Use a Session ID to reuse browser contexts across node executions

### Example: Take a Screenshot

```json
{
  "browser": "chromium",
  "category": "navigation",
  "navigationOperation": "goto",
  "url": "https://example.com"
}
```

Then add another Mindsurf node:

```json
{
  "browser": "chromium",
  "category": "screenshot",
  "screenshotOperation": "screenshot",
  "screenshotOptions": {
    "fullPage": true,
    "type": "png"
  }
}
```

### Session Management

#### Basic Session Management
Use the Session ID parameter to maintain browser state across multiple node executions. This allows you to:
- Keep login sessions active
- Reuse the same browser context
- Maintain cookies and local storage
- Improve performance by avoiding repeated browser launches

#### Login Session Persistence
Save and restore login sessions to skip repetitive authentication:

1. **Save Login Session** - After logging in:
```json
{
  "browser": "chromium",
  "category": "session",
  "sessionOperation": "saveSession",
  "profileName": "My Gmail Account",
  "profileDescription": "Personal Gmail with 2FA"
}
```

2. **Load Saved Session** - Restore login state later:
```json
{
  "browser": "chromium",
  "category": "session",
  "sessionOperation": "loadSession",
  "profileId": "profile_123456789",
  "createNewSession": true
}
```

3. **Manage Saved Sessions**:
- List all saved sessions: `sessionOperation: "listSavedSessions"`
- Delete a saved session: `sessionOperation: "deleteSavedSession"`

Saved sessions are stored locally in `~/.n8n/mindsurf-profiles/` and include:
- Cookies
- Local Storage
- Session Storage
- Authentication tokens

## Browser Options

Configure browser behavior with these options:
- **Headless**: Run browser without GUI
- **Viewport**: Set browser window dimensions
- **User Agent**: Custom user agent string
- **Locale & Timezone**: Emulate different regions
- **Permissions**: Grant specific browser permissions
- **Network**: Set proxy, offline mode, HTTP credentials
- **JavaScript**: Enable/disable JavaScript execution

## Requirements

- n8n version 0.170.0 or higher
- Node.js 16.x or higher
- Playwright browsers (automatically installed) or system browsers

## 🐳 Docker Support

This node supports Docker environments with system-installed browsers. See [DOCKER_SETUP.md](./DOCKER_SETUP.md) for detailed instructions.

### Quick Docker Setup

```dockerfile
FROM n8nio/n8n:latest-alpine
RUN apk add --no-cache chromium chromium-chromedriver
RUN npm install -g n8n-nodes-mindsurf
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
ENV PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Playwright documentation](https://playwright.dev/)

## License

[MIT](https://github.com/dandacompany/n8n-nodes-mindsurf/blob/main/LICENSE.md)

## 📮 Support

- 📧 Email: [datapod.k@gmail.com](mailto:datapod.k@gmail.com)
- 🐛 Issues: [GitHub Issues](https://github.com/dandacompany/n8n-nodes-mindsurf/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/dandacompany/n8n-nodes-mindsurf/discussions)
- 📺 YouTube: [Dante Labs](https://youtube.com/@dante-labs)
- 🎥 Tutorials: Check out our YouTube channel for tutorials and guides

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/) for reliable browser automation
- Powered by [n8n](https://n8n.io/) workflow automation platform
- Thanks to the n8n community for continuous support and feedback

---

Made with ❤️ for the n8n community