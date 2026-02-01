<div align="center">
  <img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" alt="n8n" width="120" height="120">
  <span style="font-size: 50px; margin: 0 20px;">+</span>
  <img src="./nodes/Shopier/shopier.svg" alt="Shopier" width="120" height="120">
</div>

<div align="center">
  
![n8n.io - Shopier](https://img.shields.io/badge/n8n.io-Shopier-orange.svg)
![Version](https://img.shields.io/npm/v/n8n-nodes-shopier.svg)
![Downloads](https://img.shields.io/npm/dt/n8n-nodes-shopier.svg)
![License](https://img.shields.io/npm/l/n8n-nodes-shopier.svg)

</div>

<div align="center">
  
  **A powerful n8n community node for Shopier API integration**
  
  *Seamlessly automate your Shopier e-commerce workflows with n8n*
</div>

---

**What is this?**
A custom n8n node for integrating with Shopier API. This node enables seamless automation workflows between Shopier and other services through n8n's visual workflow builder.

**What is n8n?**
[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform that lets you connect different services and automate tasks visually.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Contributing](#contributing)
- [Development Setup](#development-setup)
- [Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Install via n8n Community Nodes

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-shopier`
4. Agree to the risks: **I understand the risks of installing unverified code from a public source**
5. Select **Install**

> **That's it!** After installation, the Shopier node will be available in your n8n palette.

## Features

This Shopier node provides comprehensive integration with the Shopier API, supporting:

### **Products**

- `Get Many` - Retrieve all products with comprehensive filtering options:

  - **Status Filters**: Active, Inactive, Draft products
  - **Category Filtering**: Filter by specific category ID
  - **Product Identification**: SKU and name filtering
  - **Date Range**: Filter by creation date range (created_from, created_to)
  - **Pagination**: Efficient data retrieval with limit controls
  - **Return All**: Option to retrieve all products with automatic pagination

- `Get` - Retrieve a specific product by ID with detailed information

## Credentials

To use this node, you need to authenticate with Shopier using your API credentials. Here's how to set it up:

### Prerequisites

1. You must have a Shopier account
2. Access to Shopier Developer Panel for API credential generation

### Authentication Setup

1. Log in to your Shopier account
2. Navigate to the Developer Panel or API settings
3. Generate a Personal Access Token
4. Note down your **Personal Access Token**

### Credential Configuration

When setting up the Shopier API credentials in n8n:

- **Personal Access Token**: Your Shopier Personal Access Token for API authentication

The node uses Bearer Token authentication with your Personal Access Token.

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node version**: 1.0
- **Tested with**: n8n 1.x
- **Node.js**: >=22.16

This node uses the Shopier API and should be compatible with all current Shopier configurations.

## Usage

### Quick Start

1. Install the node using n8n's community node installation process
2. Set up your Shopier API credentials
3. Create a new workflow and add the Shopier node
4. Configure your desired operation (Product management)

### Resource Operations

**Product Operations**: Retrieve and filter your product catalog with comprehensive filtering options matching official Shopier API specifications.

### Advanced Configuration

**Pagination**: Use limit parameters for large datasets to efficiently manage API calls and response sizes.

**Advanced Product Filtering**: Apply comprehensive filters following official Shopier API specification:

- **Status Filters**: active, inactive, draft
- **Identification**: sku, name, category_id
- **Date Filtering**: created_from, created_to for creation date range
- **Pagination**: limit parameter for efficient data retrieval

**Error Handling**: The node includes comprehensive error handling with detailed error messages for troubleshooting.

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button on GitHub to create your own copy
2. **Clone Your Fork**: `git clone https://github.com/YOUR_USERNAME/n8n-nodes-shopier.git`
3. **Create a Branch**: `git checkout -b feature/your-feature-name`
4. **Make Your Changes**: Implement your feature or fix
5. **Test Your Changes**: Ensure everything works correctly
6. **Commit Your Changes**: `git commit -am 'Add some feature'`
7. **Push to Your Branch**: `git push origin feature/your-feature-name`
8. **Create a Pull Request**: Submit your changes for review

### Code Standards

- Follow the existing TypeScript code style
- Use meaningful variable and function names
- Add JSDoc comments for new functions
- Ensure all new code is properly typed

### Reporting Issues

Found a bug or have a feature request? Please check existing issues first, then create a new issue with:

- Clear description of the problem or request
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your environment details (n8n version, Node.js version, etc.)

## Development Setup

### Prerequisites

- Node.js >=22.16
- n8n (for testing)
- Shopier Account with API access

### Setup Instructions

1. **Clone the Repository**

   ```
   git clone https://github.com/YOUR_USERNAME/n8n-nodes-shopier.git
   cd n8n-nodes-shopier
   ```

2. **Install Dependencies**

   ```
   npm install
   ```

3. **Build the Project**

   ```
   npm run build
   ```

4. **Linting and Formatting**
   ```
   npm run lint        # Check for linting issues
   npm run lintfix     # Fix auto-fixable issues
   npm run format      # Format code with prettier
   ```

### Project Structure

```
├── credentials/                 # Authentication credential definitions
│   └── ShopierApi.credentials.ts
├── nodes/
│   └── Shopier/
│       ├── Shopier.node.ts        # Main node orchestrator
│       ├── GenericFunctions.ts    # Shared utility functions
│       ├── types/                 # TypeScript type definitions
│       │   └── index.ts
│       ├── operations/            # Resource operation implementations
│       │   ├── index.ts
│       │   └── product.operations.ts
│       ├── node-definition/       # Node UI property definitions
│       │   ├── index.ts
│       │   ├── resources.ts
│       │   ├── operations.ts
│       │   └── fields.ts
│       ├── endpoints/             # API endpoint definitions
│       │   └── products.endpoints.ts
│       └── shopier.svg            # Node icon
├── dist/                       # Compiled output
├── gulpfile.js                 # Build configuration
├── package.json               # Project configuration
└── tsconfig.json              # TypeScript configuration
```

### Testing Your Changes

1. Build the project: `npm run build`
2. Link to n8n: Follow n8n's community node development guide
3. Test your changes in n8n workflows
4. Verify all operations work as expected with real Shopier API

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/#community-nodes)
- [n8n Node Development Guide](https://docs.n8n.io/integrations/creating-nodes/)
- [Shopier Developer Documentation](https://developer.shopier.com/reference)
- [Shopier API Documentation](https://developer.shopier.com/reference)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the n8n team for creating an amazing workflow automation platform
- Thanks to Shopier for providing a comprehensive e-commerce API
- Thanks to all contributors who help improve this node

---

**Need Help?**

- Check out the [Issues](../../issues) for common problems
- Create a new issue if you can't find a solution
- Join the [n8n community](https://community.n8n.io/) for general n8n support
- Review [Shopier API documentation](https://developer.shopier.com/reference) for API-specific questions
