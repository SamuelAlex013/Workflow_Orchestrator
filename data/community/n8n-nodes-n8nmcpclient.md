# n8n-nodes-n8nmcpclient

This is an n8n community node package. It provides nodes to interact with servers implementing the Model Context Protocol (MCP).

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This node package allows n8n workflows, especially AI Agents, to connect to and utilize MCP servers.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Nodes](#nodes)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation. Search for `n8n-nodes-n8nmcpclient`.


## Development

This section describes how to set up a local development environment to work on this node package. This method uses n8n installed as a development dependency, which avoids common issues with native modules like `sqlite3` when using globally installed n8n and `pnpm link`.

### Prerequisites

*   **Node.js**: Version 18.10 or later (check with `node -v`).
*   **pnpm**: Version 9.1 or later (check with `pnpm -v`). Install via `npm install -g pnpm`.
*   **(Windows Only) Build Tools**: To correctly build the `sqlite3` dependency, you need Python and the Microsoft C++ Build Tools.
    *   Install Python from the official website or Microsoft Store.
    *   Install Build Tools for Visual Studio (select the "Desktop development with C++" workload during installation).
    *   You might need to configure npm/pnpm to find the tools by setting the `GYP_MSVS_VERSION` environment variable (e.g., `$env:GYP_MSVS_VERSION='2022'`) before installing dependencies if `pnpm install` fails on `sqlite3`.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/golfamigo/n8n-nodes-n8nmcpclient.git
    cd n8n-nodes-n8nmcpclient
    ```

2.  **Install dependencies:**
    This will install the node's dependencies and n8n itself as a dev dependency.
    ```bash
    pnpm install
    ```
    *(If you encounter errors related to `sqlite3` on Windows, ensure the Build Tools prerequisites are met and try setting `GYP_MSVS_VERSION` before running `pnpm install` again, or run `npm rebuild sqlite3` after installation.)*

3.  **Build the node:**
    Compile the TypeScript code to JavaScript in the `dist` directory.
    ```bash
    pnpm run build
    ```

### Running Locally

1.  **Add a start script (Optional but recommended):**
    Add the following script to your `package.json` under `"scripts"` to easily start n8n with the correct settings. Choose the syntax for your preferred shell (cmd or PowerShell).

    ```json
    // package.json
    "scripts": {
      // ... other scripts ...
      "dev:n8n": "$env:DB_TYPE='sqlite'; $env:N8N_HOST='127.0.0.1'; $env:N8N_RUNNERS_ENABLED='true'; n8n start" // PowerShell syntax
      // or for cmd.exe:
      // "dev:n8n": "set DB_TYPE=sqlite&& set N8N_HOST=127.0.0.1&& set N8N_RUNNERS_ENABLED=true&& n8n start"
    }
    ```

2.  **Start n8n:**
    Run the script (if added) or the full command in the project's root directory:
    ```bash
    pnpm run dev:n8n
    ```
    Or directly:
    ```bash
    # PowerShell
    $env:DB_TYPE='sqlite'; $env:N8N_HOST='127.0.0.1'; $env:N8N_RUNNERS_ENABLED='true'; pnpm exec n8n start
    # cmd.exe
    set DB_TYPE=sqlite&& set N8N_HOST=127.0.0.1&& set N8N_RUNNERS_ENABLED=true&& pnpm exec n8n start
    ```
    n8n will start using the local `sqlite.db` file for storage and automatically load your custom node from the `dist` directory. Access n8n at `http://127.0.0.1:5678`.

### Development Workflow

1.  **Make changes** to the node's TypeScript source files (in `nodes/` or `credentials/`).
2.  **Stop** the running n8n instance (Ctrl+C in the terminal).
3.  **Rebuild** the node to compile your changes:
    ```bash
    pnpm run build
    ```
4.  **Restart** n8n using your start command (e.g., `pnpm run dev:n8n`).

*(Tip: You can run `pnpm run dev` in a separate terminal to automatically recompile TypeScript files on save. You'll still need to stop/restart n8n and manually run `pnpm run build` if you change icons or other assets handled by gulp.)*

## Publishing

To publish a new version of this package to npm:

1.  **Ensure tests pass** (if applicable).
2.  **Run the prepublish script:** This script typically builds the project and runs linters to ensure code quality.
    ```bash
    pnpm run prepublishOnly
    ```
3.  **Update the version number:** Edit the `version` field in `package.json` according to [Semantic Versioning](https://semver.org/).
4.  **Commit your changes:**
    ```bash
    git add .
    git commit -m "chore: release vX.Y.Z"
    *(Note: Only the contents of the `dist` directory, as specified in the `"files"` field of `package.json`, will be included in the published package. Development dependencies like `n8n` itself will not be published.)*

    git tag vX.Y.Z
    git push && git push --tags
    ```
5.  **Publish to npm:** Make sure you are logged into npm (`npm login`).
    ```bash
    pnpm publish
    ```

## Nodes

*   **Smart MCP Client (`smartMcp`)**: Connects to an MCP server via STDIO or SSE and allows interaction with its capabilities (tools, resources, prompts). Designed for use with n8n AI Agents.

## Operations (Smart MCP Client)

*   **Discover Capabilities (for AI Agent)**: Connects to the MCP server and lists all available tools, resources, and prompts. Resources and prompts are presented as pseudo-tools (prefixed with `resource_` or `prompt_`) with associated metadata, making them discoverable and usable by AI Agents through the standard tool execution mechanism. This is the recommended operation when using this node with an AI Agent.
*   **Execute Tool**: Executes a specific tool (either a real MCP tool or a pseudo-tool representing a resource read or prompt retrieval) on the connected MCP server. Requires the tool name and parameters in JSON format.
*   **Read Resource**: Reads the content of a specific resource URI from the MCP server.
*   **Get Prompt**: Retrieves a specific prompt template from the MCP server.
*   **List Tools**: Lists only the actual tools available on the MCP server.
*   **List Resources**: Lists only the resources available on the MCP server.
*   **List Resource Templates**: Lists the resource templates available on the MCP server.
*   **List Prompts**: Lists only the prompts available on the MCP server.

## Credentials

This node package includes two credential types:

1.  **MCP Client (STDIO) API (`mcpClientApi`)**:
    *   Used for connecting to MCP servers launched as local command-line processes via Standard Input/Output (STDIO).
    *   **Command**: The command to execute to start the MCP server (e.g., `node path/to/server.js`, `python script.py`).
    *   **Arguments**: Space-separated arguments to pass to the command.
    *   **Environments**: Comma-separated `NAME=VALUE` pairs for environment variables needed by the server (e.g., API keys).

2.  **MCP Client (SSE) API (`mcpClientSseApi`)**:
    *   Used for connecting to remote MCP servers via Server-Sent Events (SSE) over HTTP.
    *   **SSE URL**: The URL of the MCP server's SSE endpoint (e.g., `http://localhost:3001/sse`).
    *   **Messages Post Endpoint** (Optional): A custom URL endpoint for sending messages back to the server if it differs from the base SSE URL.
    *   **Additional Headers** (Optional): Headers to include in requests, typically for authentication (e.g., `Authorization: Bearer YOUR_TOKEN`). Format: one header per line (`Header-Name: Value`).

## Compatibility

*   Requires n8n version 1.0 or later.
*   Requires Node.js version 18.10 or later.

## Usage

When using the **Smart MCP Client** node with an n8n **AI Agent**:

1.  Add the **Smart MCP Client** node to your workflow.
2.  Configure the **Connection Type** and the corresponding **Credentials**.
3.  Set the **Operation** to **Discover Capabilities (for AI Agent)**.
4.  Connect the output of the **Smart MCP Client** node to the **Tool** input of the **AI Agent** node.

The AI Agent will automatically call the `discoverCapabilities` operation to learn about the available tools, resources, and prompts from the MCP server. It can then decide to use any of these capabilities by calling the `executeTool` operation on the Smart MCP Client node, passing the appropriate tool name (e.g., `get_weather`, `resource_userProfile`, `prompt_summarize`) and parameters.

For manual workflow usage (without an AI Agent), you can select specific operations like `Execute Tool`, `Read Resource`, etc., and provide the necessary parameters directly in the node's UI.

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
*   [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io)
*   [MCP Specification](https://spec.modelcontextprotocol.io)
*   [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
