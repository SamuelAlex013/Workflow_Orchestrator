# n8n-nodes-beagle-security

This is an n8n community node that allows you to interact with [Beagle Security](https://beaglesecurity.com) API for automated vulnerability scanning and security testing.

[Beagle Security](https://beaglesecurity.com) is a web application and API security testing platform that helps identify vulnerabilities in your applications.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install**
3. Enter `n8n-nodes-beagle-security` as the package name
4. Click **Install**

### Manual Installation

To get started:

```bash
npm install n8n-nodes-beagle-security
```

Or install it globally:

```bash
npm install -g n8n-nodes-beagle-security
```

## Development

### Project Structure

- **`src/`** - TypeScript source code
- **`credentials/`** - Built credential files (auto-generated)
- **`nodes/`** - Built node files (auto-generated)
- **`docker/`** - Docker configurations
- **`scripts/`** - Build and deployment scripts

### Building

```bash
npm run build       # Build TypeScript to JavaScript
npm run lint        # Check code quality
npm run format      # Format code
```

## Credentials

You need to configure your Beagle Security API credentials:

1. Go to **Settings > Credentials** in n8n
2. Click **Add Credential**
3. Search for "Beagle Security API"
4. Enter your Beagle Security API token

### Getting Your API Token

1. Log in to your [Beagle Security dashboard](https://beaglesecurity.com)
2. Go to **Settings > API Keys**
3. Generate a new API token
4. Copy the token and use it in your n8n credentials

## Supported Operations

### Projects
- **Create** - Create a new project
- **Get All** - Retrieve all projects
- **Update** - Update an existing project
- **Delete** - Delete a project

### Applications
- **Create** - Create a new application in a project
- **Get** - Get application details
- **Get All** - Get all applications in a project
- **Update** - Update an existing application
- **Delete** - Delete an application
- **Verify Domain** - Verify domain ownership

### Tests
- **Start** - Start a security test on an application
- **Stop** - Stop a running test
- **Get Status** - Get the status of a running test
- **Get Result** - Get test results
- **Get Sessions** - Get test sessions for an application
- **Get Running Tests** - Get all currently running tests

## Example Usage

### Start a Security Test

1. Add a **Beagle Security** node to your workflow
2. Set **Resource** to "Test"
3. Set **Operation** to "Start"
4. Configure **Application Token** (you can get this from your Beagle Security dashboard)
5. Execute the workflow

### Get Test Results

1. Add another **Beagle Security** node
2. Set **Resource** to "Test"
3. Set **Operation** to "Get Result"
4. Use the **Application Token** and **Result Token** from the previous step
5. Execute to get detailed vulnerability report

## Resources

- [Beagle Security](https://beaglesecurity.com)
- [Beagle Security API Documentation](https://beaglesecurity.com/developer/apidoc)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
