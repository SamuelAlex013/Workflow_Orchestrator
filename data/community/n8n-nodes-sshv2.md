![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

https://www.npmjs.com/package/n8n-nodes-sshv2

# n8n-nodes-sshv2

This package provides enhanced SSH functionality for n8n, including an AI-powered SSH tool node.

## Features

### 1. Hadidiz-AI Node
An AI-powered SSH tool that can be used with n8n's AI Agent for:
- Executing remote commands
- Downloading files
- Uploading files
- Dynamic connection parameters
- Support for both password and private key authentication

### 2. SSHv2 Node
A standard SSH node with enhanced capabilities for:
- Command execution
- File transfers
- Credential management
- Dynamic parameters

## Installation

### Local Installation
```bash
npm install n8n-nodes-sshv2
```

### n8n.cloud Installation
1. Go to Settings > Community Nodes
2. Select "Install"
3. Enter `n8n-nodes-sshv2`
4. Click "Install"

## Usage with AI Agent

To use the Hadidiz-AI node with the AI Agent, you need to:

1. Set the following environment variables:
```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

2. Add the AI Agent node to your workflow
3. Select "Tools Agent" as the agent type
4. Add "Hadidiz-AI" from the available tools

## Configuration

### SSH Credentials
The package supports two types of authentication:
- Password-based authentication
- Private key authentication

### Dynamic Parameters
Both nodes support dynamic parameters, allowing you to:
- Use different servers in the same workflow
- Pass credentials from previous nodes
- Use environment variables

## Development

### Building the Package

```bash
# Install dependencies
pnpm install

# Build the project
pnpm build

# Run linting
pnpm lint

# Format code
pnpm format
```

### Publishing to NPM

This package uses GitHub Actions to automatically publish to npm when version tags are pushed.

#### For Maintainers

1. **Set up NPM_TOKEN secret**: 
   - Go to repository Settings → Secrets and variables → Actions
   - Add a new secret named `NPM_TOKEN`
   - Value should be your npm authentication token (get from https://www.npmjs.com/settings/tokens)

2. **Release a new version**:
   ```bash
   # Update version in package.json
   npm version patch  # or minor, major
   
   # Push the tag to trigger publishing
   git push origin --tags
   ```

The workflow will automatically:
- Build and test the package
- Verify the workflow is triggered by a version tag
- Verify the version matches the tag
- Publish to npmjs.com

## License

[MIT](LICENSE.md)

## Credits

By Hadidizflow.com Your AI Solutions Partner.