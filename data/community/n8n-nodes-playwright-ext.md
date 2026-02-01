# n8n-nodes-playwright-ext

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

An n8n node for advanced browser automation using [Playwright](https://playwright.dev/). Execute custom scripts, capture screenshots and PDFs, scrape content, and automate web interactions with support for Chromium, Firefox, and WebKit. Leverage Playwright's powerful API alongside n8n's workflow capabilities for robust browser automation tasks.

## How to Install

### Community Nodes (Recommended)

For n8n version later, install this node through the Community Nodes panel:

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-playwright-ext` in **Enter npm package name**
4. Agree to the risks of using community nodes
5. Select **Install**

### Manual Installation

For a standard installation:

```bash
# Navigate to your n8n root directory
cd /path/to/n8n

# Install the package
npm install n8n-nodes-playwright-ext
```

### Docker Installation (Recommended for Production)

Use the provided Docker setup to include all necessary dependencies:

1. Clone this repository or copy the Docker files
2. Build the Docker image:
   ```bash
   docker build -t n8n-playwright-ext -f docker/Dockerfile docker/
   ```
3. Run the container:
   ```bash
   docker run -it \
     -p 5678:5678 \
     -v ~/.n8n:/home/node/.n8n \
     n8n-playwright-ext
   ```

## Features

- **Multi-browser Support**: Automate with Chromium, Firefox, and WebKit
- **Operations**:
  - Get page content (HTML)
  - Capture screenshots (PNG, JPEG)
  - Generate PDFs
  - Run custom Playwright scripts
- **Advanced Configuration**:
  - Emulate devices and viewports
  - Set custom headers and user agents
  - Configure navigation timeouts and wait conditions
  - Proxy support

## Custom Scripts

The Custom Script operation provides full access to the Playwright API for complex automation scenarios. You can use:

- `$page` - Current page instance
- `$browser` - Browser instance
- `$playwright` - Playwright library

Example script:
```javascript
// Navigate to a page
await $page.goto('https://example.com');

// Extract data
const title = await $page.title();
const content = await $page.textContent('h1');

// Return results
return [{ title, content, ...$json }];
```

## Troubleshooting

- For missing browser dependencies, install the required system packages or use the Docker setup
- For connection issues, verify browser executable paths or WebSocket endpoints
- Refer to the [Playwright troubleshooting guide](https://playwright.dev/docs/troubleshooting) for additional help


## Acknowledgments

This project draws significant inspiration from and builds upon the excellent work done in the [n8n-nodes-puppeteer](https://github.com/drudge/n8n-nodes-puppeteer) project by Nicholas Penree. The structure, approach to integrating browser automation with n8n, and many implementation patterns were adapted from that repository.

Special thanks to Nicholas Penree and the contributors to n8n-nodes-puppeteer for pioneering this approach to browser automation within the n8n ecosystem. Their work served as a valuable reference and foundation for developing this Playwright-based extension.