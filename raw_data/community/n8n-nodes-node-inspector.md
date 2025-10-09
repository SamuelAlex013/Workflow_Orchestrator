# n8n Node Inspector API

This n8n custom extension provides an API endpoint to list all registered nodes on your n8n instance, including their properties, inputs, outputs, and other metadata.

## Features

-   Exposes a GET endpoint: `/custom/nodes`
-   Lists all core, community, and custom nodes.
-   Provides details for each node:
    -   `name`: Internal n8n name (e.g., `n8n-nodes-base.httpRequest`)
    -   `displayName`: User-friendly name (e.g., "HTTP Request")
    -   `type`: Categorized as 'core', 'core-contrib', 'community', or 'custom'
    -   `version`: Node version
    -   `description`: Node's purpose
    -   `inputs`: Array of input connection names (e.g., `["main"]`)
    -   `outputs`: Array of output connection names (e.g., `["main"]`)
    -   `credentials`: Array of credential types the node can use.
    -   `properties`: Detailed array of all configurable properties for the node.

## Prerequisites

-   A self-hosted n8n instance.
-   Node.js and npm/yarn installed for building the package.

## Building the Package

1.  Clone this repository (or create the files as described).
2.  Navigate to the package directory: `cd n8n-nodes-node-inspector`
3.  Install dependencies: `npm install` (or `yarn install`)
4.  Build the package: `npm run build`

This will compile the TypeScript code into the `dist` directory.

## Installation on n8n

There are two main ways to install custom extensions in n8n:

**Method 1: Manual Copy (for testing or simple setups)**

1.  Ensure the package is built (you should have a `dist` folder).
2.  Locate your n8n custom extensions directory. By default, this is `~/.n8n/custom/` (Linux/macOS) or `%USERPROFILE%/.n8n/custom/` (Windows).
3.  Create this directory if it doesn't exist.
4.  Copy the entire `n8n-nodes-node-inspector` package folder (including `dist`, `package.json`, etc.) into the `~/.n8n/custom/` directory.
    The structure should be: `~/.n8n/custom/n8n-nodes-node-inspector/package.json`, etc.
5.  Restart your n8n instance.

**Method 2: Docker Volume Mounting (recommended for Docker deployments)**

1.  Ensure the package is built.
2.  When running your n8n Docker container, mount the `n8n-nodes-node-inspector` package directory into `/home/node/.n8n/custom/` inside the container.

    Example `docker-compose.yml` snippet:

    ```yaml
    services:
      n8n:
        image: n8nio/n8n
        ports:
          - "5678:5678"
        environment:
          # Add other n8n environment variables as needed
        volumes:
          - ~/.n8n_data:/home/node/.n8n # For n8n data persistence
          - ./path/to/your/n8n-nodes-node-inspector:/home/node/.n8n/custom/n8n-nodes-node-inspector # Mount the custom extension
    ```
    Replace `./path/to/your/n8n-nodes-node-inspector` with the actual path to your built package on the host machine.

3.  Restart your n8n Docker container (`docker-compose up -d --force-recreate` or similar).

## Usage

Once installed and n8n is restarted, the API endpoint will be available at:

`http://<your-n8n-host>:<port>/custom/nodes`

For a local n8n instance running on port 5678, this would be:
`http://localhost:5678/custom/nodes`

You can access this URL with a browser, `curl`, Postman, or an n8n HTTP Request node.

## Example Output Snippet

```json
[
  {
    "name": "n8n-nodes-base.httpRequest",
    "displayName": "HTTP Request",
    "type": "core",
    "version": 1,
    "description": "Makes an HTTP request to a remote server",
    "inputs": ["main"],
    "outputs": ["main"],
    "credentials": [
      {
        "name": "httpBasicAuth",
        "required": false
      },
      {
        "name": "httpDigestAuth",
        "required": false
      }
      // ... and other credential types
    ],
    "properties": [
      {
        "displayName": "Authentication",
        "name": "authentication",
        "type": "options",
        "options": [ /* ... */ ],
        "default": "none"
      },
      {
        "displayName": "URL",
        "name": "url",
        "type": "string",
        "default": "",
        "placeholder": "http://localhost/webhook",
        "description": "The URL to make the request to",
        "required": true
      }
      // ... many more properties
    ]
  }
  // ... other nodes
]
```

## Development

-   `npm run dev`: To watch for changes in `src/` and recompile automatically.
-   `npm run lint`: To lint the TypeScript code.
-   `npm run format`: To format the code with Prettier.

You'll need to restart n8n after recompiling and updating the files in the `~/.n8n/custom` directory for changes to take effect. 