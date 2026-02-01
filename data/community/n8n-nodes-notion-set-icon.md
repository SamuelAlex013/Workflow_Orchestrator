# n8n-nodes-notion-set-icon

[![npm version](https://badge.fury.io/js/n8n-nodes-notion-set-icon.svg)](https://www.npmjs.com/package/n8n-nodes-notion-set-icon)
[![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-notion-set-icon.svg)](https://www.npmjs.com/package/n8n-nodes-notion-set-icon)
[![CI/CD](https://github.com/oriolrius/n8n-nodes-notion-set-icon/actions/workflows/ci.yml/badge.svg)](https://github.com/oriolrius/n8n-nodes-notion-set-icon/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

This is an n8n community node that allows you to set custom icons for Notion pages.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

**Table of Contents**
- [Key Features](#key-features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Development](#development)
- [Testing](#testing)
- [Changelog](#changelog)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Built With](#built-with)
- [Support](#support)

## Key Features

- 🎨 **Custom Page Icons** - Set icons via external URL or file upload
- 📁 **Filesystem Binary Mode Support** (v1.2.0+) - Compatible with `N8N_DEFAULT_BINARY_DATA_MODE=filesystem`
- 📦 **Large File Handling** - Works seamlessly with S3 and filesystem-based binary storage
- 🔄 **Flexible Page ID Format** - Accepts Notion URLs, UUIDs with/without hyphens, or raw hex
- 🧪 **Production Tested** - Comprehensive Playwright test suite with Docker e2e integration tests
- ⚡ **Automated Releases** - Built-in release automation with bumpr

## Quick Start

After installation, create a simple workflow:

1. **Add Notion Set Icon node** to your workflow
2. **Configure credentials** (token_v2, space_id, user_id) - [see how](#credentials)
3. **Enter Page ID**: `214c413b-2a68-800f-9f9a-d234e37d1380` (or paste full Notion URL)
4. **Choose Icon Source**: URL or Upload File
5. **Execute** ✅

> 💡 **Tip**: Extract Page ID from any Notion URL - the node handles formatting automatically

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-notion-set-icon` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

This node supports the following operations:

### Page
- **Set Icon**: Set a custom icon for a Notion page using either:
  - External image URL
  - Upload a local image file (supports memory, filesystem, and S3 binary storage modes)

## Credentials

This node requires Notion Set Icon API credentials. You need to provide:

- **Token V2**: Your Notion `token_v2` cookie value
- **Space ID**: Your Notion workspace space ID
- **User ID**: Your Notion user ID

### How to get credentials

1. **Token V2**:
   - Open your browser's developer tools while logged into Notion
   - Go to Application/Storage > Cookies > https://www.notion.so
   - Find and copy the `token_v2` value

2. **Space ID & User ID**:
   - In the same cookies section, look for `notion-space-id` and `notion-user-id`
   - Or inspect network requests to find these values in API calls

## Compatibility

### Requirements

| Component | Version | Notes |
|-----------|---------|-------|
| n8n | ≥1.56.0 | Tested up to latest |
| Node.js | ≥18.10 | Required for dependencies |
| Binary Mode | All modes | ✅ Memory, Filesystem, S3 (v1.2.0+) |

### Performance

- 📦 **Small files** (<1MB): Any version works
- 📦 **Large files** (>1MB): Requires v1.2.0+ for filesystem mode compatibility
- 🚀 **Bulk operations**: Rate limited by Notion API (~3 req/sec)

This node was developed and tested with n8n version 1.56.0+ and supports Node.js 18, 20, and 22.

## Usage

### Setting an icon from URL

1. Add the **Notion Set Icon** node to your workflow
2. Configure your credentials
3. Set **Icon Source** to "URL"
4. Enter the **Page ID** (can be extracted from Notion page URL)
5. Enter the **Icon URL** pointing to your image

### Uploading and setting an icon from file

1. Add the **Notion Set Icon** node to your workflow
2. Configure your credentials
3. Set **Icon Source** to "Upload File"
4. Enter the **Page ID**
5. Specify the **Input Binary Field** containing your image data

### Page ID formats supported

The node accepts page IDs in multiple formats:
- Full UUID: `214c413b-2a68-800f-9f9a-d234e37d1380`
- Notion URL: `https://www.notion.so/workspace/page-title-214c413b2a68800f9f9ad234e37d1380`
- Raw hex: `214c413b2a68800f9f9ad234e37d1380`

## Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| ❌ "Not authenticated" | Refresh your `token_v2` - it expires after ~90 days of inactivity |
| ❌ "Block not found" | Verify page ID format and ensure you have access to the workspace |
| ❌ "No permission" | Ensure the user has edit rights to the target page |
| ❌ Large file upload fails | ✅ v1.2.0+ fixed this! Update to latest version for filesystem binary mode support |
| ❌ Invalid page ID error | Check page ID format - node accepts URLs, UUIDs, or 32-char hex strings |

**Still stuck?** Check our [Technical Specification](docs/NOTION_ICON_TECHNICAL_SPEC.md) or [open an issue](https://github.com/oriolrius/n8n-nodes-notion-set-icon/issues).

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- 📖 [Technical Specification](docs/NOTION_ICON_TECHNICAL_SPEC.md) - Deep dive into Notion API internals (460+ lines)
- 🔒 [Security Policy](docs/SECURITY.md) - Credential management and security best practices
- 🤝 [Contributing Guide](docs/CONTRIBUTING.md) - Development workflow and contribution guidelines
- 🧬 [Binary Mode Compatibility](docs/binary-mode-compatibility.md) - Filesystem storage mode explained
- 🧪 [Test Suite Documentation](tests/README.md) - E2E and integration test documentation

## Development

### Local Testing Environment

This project includes a local n8n test environment for development and testing:

1. **Setup Environment Variables**:
   ```bash
   cp .env.example .env
   # Fill in your actual Notion credentials in the .env file
   ```

2. **Start Test Environment**:
   ```bash
   pnpm start
   # or
   ./start-n8n.sh
   ```

3. **Development Workflow**:
   ```bash
   # Make changes to the node code
   pnpm build          # Rebuild the node
   pnpm start          # Restart n8n (changes auto-available)
   ```

4. **Access n8n**: Open `http://localhost:5678` in your browser

### Code Quality

```bash
pnpm lint           # Check for linting errors
pnpm lintfix        # Auto-fix linting errors
pnpm format         # Format code with Prettier
```

### Release Process

This project uses a custom `bumpr` tool for automated releases:

```bash
pnpm release         # Patch: 1.3.0 → 1.3.1
pnpm release:minor   # Minor: 1.3.0 → 1.4.0
pnpm release:major   # Major: 1.3.0 → 2.0.0
```

The `bumpr` tool automatically handles:
- Version bumping in package.json
- Git commit and tagging
- Pushing to remote repository
- Creating GitHub releases
- Triggering npm publication via CI/CD

## Testing

### Running Tests

```bash
pnpm test                    # Run all Playwright tests
pnpm test:docker            # Docker e2e tests
pnpm test:headed            # UI mode for debugging
pnpm test:debug             # Debug mode
pnpm test:ui                # Interactive UI mode
```

### Test Coverage

This project includes comprehensive test coverage:

- ✅ **E2E Workflow Tests** - Complete workflow execution validation
- ✅ **Docker Integration Tests** - Full n8n environment tests
- ✅ **Direct Notion API Tests** - Raw API interaction tests
- ✅ **Production NPM Package Tests** - Real-world installation validation

**Test Suite Highlights:**
- Playwright-based browser automation
- Docker containerized n8n environment
- Fixture-based test data management
- Cookie and credential handling tests
- Network packet capture for debugging

See [Test Documentation](tests/README.md) for detailed information.

### Prerequisites for Testing

- Docker and Docker Compose
- Node.js 18+ and pnpm
- `.env` file with Notion credentials:
  - `NOTION_TOKEN_V2`
  - `SPACE_ID`
  - `NOTION_USER_ID`

## Changelog

See [Releases](https://github.com/oriolrius/n8n-nodes-notion-set-icon/releases) for detailed version history.

### Recent Updates

- **v1.3.0** (Sep 2025) - Integrated `bumpr` for automated release management
- **v1.2.0** (Sep 2025) - 🎯 **Critical**: Filesystem binary mode compatibility for large files and S3 storage
- **v1.1.2** (Jun 2025) - Production test improvements and npm installation fixes
- **v1.1.1** (Jun 2025) - Icon path fixes for production builds
- **v1.1.0** (Jun 2025) - Docker setup enhancements and type improvements

## Security

### Security Notice

⚠️ **Important**: The `token_v2` credential provides **full access** to your Notion workspace.

**Best Practices:**
- 🔑 Store credentials in n8n's encrypted credential system
- 🔄 Rotate tokens every 90 days
- 🚫 Never commit credentials to git or version control
- 📊 Monitor API usage for anomalies
- 🔒 Use environment variables for local development

See [Security Policy](docs/SECURITY.md) for detailed security guidelines.

### Reporting Vulnerabilities

If you discover a security vulnerability, please report it responsibly:
- **Do not** open a public GitHub issue
- Contact the maintainer directly (see Support section)
- Include description, reproduction steps, and potential impact

## Contributing

Contributions are welcome! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for:
- Development setup instructions
- Code style guidelines
- Pull request process
- Testing requirements

Quick contribution workflow:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run `pnpm lint && pnpm build`
5. Submit a pull request

## License

[MIT](LICENSE.md)

Copyright (c) 2025 Oriol Rius

## Built With

- **TypeScript** - Type-safe node development
- **n8n-workflow** - n8n node framework
- **Playwright** - E2E testing framework
- **GitHub Actions** - CI/CD automation
- **bumpr** - Custom release automation tool
- **Docker** - Integration test environment
- **pnpm** - Fast, disk space efficient package manager

**Special Thanks:**
- n8n community for the workflow automation platform
- Notion for the (unofficial) internal API

## Support

If you encounter any issues or have questions:

- 📚 Check the [Documentation](#documentation) section
- 🐛 [Open an issue](https://github.com/oriolrius/n8n-nodes-notion-set-icon/issues) on GitHub
- 💬 Review [existing issues](https://github.com/oriolrius/n8n-nodes-notion-set-icon/issues?q=is%3Aissue)

**Useful Resources:**
- [npm package](https://www.npmjs.com/package/n8n-nodes-notion-set-icon)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Notion API documentation](https://developers.notion.com/)
- [GitHub Repository](https://github.com/oriolrius/n8n-nodes-notion-set-icon)

---

**Note:** This is a community implementation using reverse-engineered Notion internal APIs. Notion may change these endpoints at any time without notice. The node is provided as-is under the MIT license.