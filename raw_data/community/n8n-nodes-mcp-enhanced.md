[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/bd76f121-1c8f-4f5d-9c65-1eac5d81b6af)

# @scalogicai/n8n-nodes-mcp-enhanced

> **Enhanced MCP Client with Additional Features**
> 
> This is an enhanced version of the n8n MCP client with additional features for prompt parameters and multi-tenant support, designed for users who need these specific capabilities.

## 🙏 Attribution

This enhanced node is built upon the excellent foundation created by **Jd Fiscus** ([@nerding-io](https://github.com/nerding-io)):

- **Original Project**: [n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)
- **npm Package**: [n8n-nodes-mcp](https://www.npmjs.com/package/n8n-nodes-mcp)
- **Creator**: Jd Fiscus (jd@nerding.io)

We're grateful for the original work that made this enhanced version possible. All core MCP protocol implementation and transport handling comes from the original project.

## 🔧 What's Different?

This version adds two specific features while maintaining full compatibility with the original:

### **Additional Features:**
- **Prompt Parameters**: Pass JSON parameters to prompts (original accepts prompt name only)
- **Tenant ID Support**: Optional field for multi-tenant MCP servers
- **Enhanced Validation**: Additional JSON parameter validation and error handling

### **What's Identical:**
- **Resource handling**: listResources, readResource, listResourceTemplates work exactly the same
- **Tool execution**: Same functionality for executing MCP tools
- **Transport types**: Same support for STDIO, SSE, and HTTP Streamable
- **Core MCP protocol**: Full compatibility with MCP specification

## 🎯 When to Use This Version

Choose this enhanced version if:
- Your MCP server accepts parameterized prompts
- You work with multi-tenant MCP implementations
- You need the specific additional features listed above

Otherwise, the [original version](https://www.npmjs.com/package/n8n-nodes-mcp) works perfectly for standard MCP operations!

## 🚀 Additional Features in Detail

### **1. Prompt Parameters**

**Original Version:**
```
- Prompt Name: "write_email"
- Result: Gets generic email template
```

**Enhanced Version:**
```
- Prompt Name: "write_email"
- Prompt Parameters: {"tone": "formal", "recipient": "manager", "topic": "project update"}
- Result: Gets customized email with your specific requirements
```

### **2. Tenant ID Support**

**Enhanced Version:**
```
- Prompt Name: "format_document"
- Prompt Parameters: {"style": "academic"}
- Tenant ID: "team-marketing"
- Result: Gets team-specific document formatting and templates
```

## 📝 Parameter Formatting Guide

### **JSON Parameter Examples:**

**Simple text customization:**
```json
{
  "language": "Spanish", 
  "style": "casual"
}
```

**Content parameters:**
```json
{
  "topic": "renewable energy",
  "audience": "general public",
  "length": "short",
  "include_examples": true
}
```

**User preferences:**
```json
{
  "user": {
    "name": "Alex",
    "skill_level": "beginner"
  },
  "output_format": "markdown",
  "include_links": false
}
```

**Complex nested parameters:**
```json
{
  "content": {
    "type": "tutorial",
    "sections": ["intro", "examples", "conclusion"]
  },
  "formatting": {
    "style": "academic",
    "citations": true
  },
  "output": {
    "format": "pdf",
    "language": "English"
  }
}
```

### **Common Parameter Types:**
- **Text**: `"language": "French"`
- **Numbers**: `"word_count": 500`
- **Booleans**: `"include_summary": true`
- **Arrays**: `"topics": ["climate", "technology", "health"]`
- **Objects**: `"format": {"type": "list", "numbered": true}`

## 🌟 Real-World Examples

### **Example 1: Content Creation**
```json
{
  "prompt_name": "write_article",
  "parameters": {
    "topic": "sustainable living",
    "tone": "informative",
    "word_count": 800,
    "target_audience": "beginners",
    "include_tips": true
  }
}
```

### **Example 2: Data Processing**
```json
{
  "prompt_name": "analyze_data",
  "parameters": {
    "data_type": "sales_figures",
    "time_period": "last_quarter",
    "include_charts": true,
    "focus_areas": ["trends", "anomalies"]
  }
}
```

### **Example 3: Personal Workflows**
```json
{
  "prompt_name": "organize_notes",
  "parameters": {
    "category": "meeting_notes",
    "priority_level": "high",
    "tags": ["project_alpha", "urgent"],
    "format": "structured_list"
  }
}
```

### **Example 4: Team Environments**
```json
{
  "prompt_name": "create_report",
  "parameters": {
    "department": "engineering",
    "report_type": "weekly_standup",
    "include_metrics": true
  },
  "tenant_id": "team-backend"
}
```

## 🔄 Migration from Original Version

This version is a **drop-in replacement** for the original:

1. **Existing workflows continue to work unchanged**
2. **New features are optional** - only activate when you use them
3. **Same operations available**: Execute Tool, List Tools, Get Prompt, etc.
4. **Same credential types**: STDIO, SSE, HTTP Streamable

To use the new features, simply:
- Add parameters to your "Get Prompt" operations when needed
- Include tenant ID if your MCP server supports multi-tenancy
- Leave these fields empty for standard MCP operations

## 🛠️ Troubleshooting Enhanced Features

### **JSON Parameter Issues**

**Invalid JSON Error:**
```
❌ Error: Invalid JSON in prompt parameters
✅ Fix: Ensure proper JSON formatting with quotes around strings
```

**Example fixes:**
```json
❌ {name: "John", active: true}
✅ {"name": "John", "active": true}

❌ {"list": [item1, item2]}
✅ {"list": ["item1", "item2"]}
```

### **Empty Parameters**

If your prompt doesn't need parameters, use:
```json
{}
```

Or leave the field empty - both work fine.

### **Tenant ID Usage**

- **Optional field** - only use if your MCP server supports tenants
- **Leave empty** for single-tenant or standard MCP servers
- **No impact** on servers that don't use tenant IDs

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Credentials](#credentials)
[Environment Variables](#environment-variables)
[Operations](#operations)
[Using as a Tool](#using-as-a-tool)
[Compatibility](#compatibility)
[Resources](#resources)

## Getting Started

Official Quickstart Video:

[![MCP Client Node Quickstart](/assets/mcp-n8n.png)](https://youtu.be/1t8DQL-jUJk)



### Community Videos

Shoutout to all the creators of the following n8n community videos that are great resources for learning how to use this node:

- [Is MCP the Future of N8N AI Agents? (Fully Tested!)](https://youtu.be/sb5hCcFYPIE)
- [Connect N8N AI Agents to EVERYTHING using MCP?](https://youtu.be/tTDRgkD-120)
- [Build an AI Agent That Can Use Any Tool (MCP in n8n Tutorial)](https://www.youtube.com/watch?v=SVZe2rdhYmA)
- [The NEW N8N MCP is an Absolute Game-Changer (Brave Search MCP)](https://youtu.be/RxXS_FpJyGM)
- [MCP & n8n Automation: The Ultimate Guide for MCP AI Agents (2025)](https://www.youtube.com/watch?v=mbQsnrxHPwE)
- [REVOLUÇÃO na criação de AGENTES no N8N com o MCP Server!!!](https://www.youtube.com/watch?v=zgH85dJcs5c) (Portuguese)

If you have a great video that you'd like to share, please let me know and I'll add it to the list!

#### Interested a deeper dive into MCP?

Check out my YouTube Series [MCP Explained](https://www.youtube.com/playlist?list=PLjOCx_PNfJ4S_oOSqrMi6t9_x1GllvQZO) for more information about the Model Context Protocol.

### Security Assessment
[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/nerding-io-n8n-nodes-mcp-badge.png)](https://mseep.ai/app/nerding-io-n8n-nodes-mcp)


## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Also pay attention to Environment Variables for [using tools in AI Agents](#using-as-a-tool). It's mandatory to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true` if you want to use the MCP Client node as a tool in AI Agents.

## Credentials

The MCP Client Enhanced node supports three types of credentials to connect to an MCP server:

### Command-line Based Transport (STDIO)

![MCP Client STDIO Credentials](./assets/credentials.png)

- **Command**: The command to start the MCP server
- **Arguments**: Optional arguments to pass to the server command
- **Environment Variables**: Variables to pass to the server in NAME=VALUE format

### HTTP Streamable Transport (Recommended)

- **HTTP Streamable URL**: The HTTP endpoint that supports streaming responses (e.g., http://localhost:3001/stream)
- **Additional Headers**: Optional headers to send with requests (format: name:value, one per line)

HTTP Streamable is the recommended and modern method for all new integrations, providing better efficiency and flexibility compared to SSE.

#### Example: Using a Local MCP Server with HTTP Streamable

This example shows how to connect to a locally running MCP server using HTTP Streamable:

1. Start a local MCP server that supports HTTP Streamable:
   ```bash
   npx @modelcontextprotocol/server-example-streamable
   ```

2. Configure MCP Client credentials:
   - In the node settings, select **Connection Type**: `HTTP Streamable`
   - Create new credentials of type **MCP Client Enhanced (HTTP Streamable) API**
   - Set **HTTP Streamable URL**: `http://localhost:3001/stream`
   - Add any required headers for authentication

3. Create a workflow using the MCP Client Enhanced node:
   - Add an MCP Client Enhanced node
   - Set the Connection Type to `HTTP Streamable`
   - Select your HTTP Streamable credentials
   - Execute the workflow to see the results

### Server-Sent Events (SSE) Transport (Deprecated, still available for legacy use)

- **SSE URL**: The URL of the SSE endpoint (default: http://localhost:3001/sse)
- **Messages Post Endpoint**: Optional custom endpoint for posting messages if different from the SSE URL
- **Additional Headers**: Optional headers to send with requests (format: name:value, one per line)

> **Deprecated:** SSE is deprecated and will not receive further updates, but remains available for legacy compatibility. For new projects, use HTTP Streamable.

#### Example: Using a Local MCP Server with SSE (legacy)

This example shows how to connect to a locally running MCP server using Server-Sent Events (SSE):

1. Start a local MCP server that supports SSE:
   ```bash
   npx @modelcontextprotocol/server-example-sse
   ```

2. Configure MCP Client credentials:
   - In the node settings, select **Connection Type**: `Server-Sent Events (SSE)`
   - Create new credentials of type **MCP Client Enhanced (SSE) API**
   - Set **SSE URL**: `http://localhost:3001/sse`
   - Add any required headers for authentication

3. Create a workflow using the MCP Client Enhanced node:
   - Add an MCP Client Enhanced node
   - Set the Connection Type to `Server-Sent Events (SSE)`
   - Select your SSE credentials
   - Execute the workflow to see the results

> **Note:** For new projects, HTTP Streamable is strongly recommended.

## Environment Variables

The MCP Client Enhanced node supports passing environment variables to MCP servers using the command-line based transport in two ways:

### 1. Using the Credentials UI

You can add environment variables directly in the credentials configuration:

![Environment Variables in Credentials](./assets/credentials-envs.png)

This method is useful for individual setups and testing. The values are stored securely as credentials in n8n.

### 2. Using Docker Environment Variables

For Docker deployments, you can pass environment variables directly to your MCP servers by prefixing them with `MCP_`:

```yaml
version: '3'

services:
  n8n:
    image: n8nio/n8n
    environment:
      - MCP_BRAVE_API_KEY=your-api-key-here
      - MCP_OPENAI_API_KEY=your-openai-key-here
      - MCP_CUSTOM_SETTING=some-value
    # other configuration...
```

These environment variables will be automatically passed to your MCP servers when they are executed.

### Example: Using Brave Search MCP Server

This example shows how to set up and use the Brave Search MCP server:

1. Install the Brave Search MCP server:
   ```bash
   npm install -g @modelcontextprotocol/server-brave-search
   ```

2. Configure MCP Client credentials:
   - **Command**: `npx`
   - **Arguments**: `-y @modelcontextprotocol/server-brave-search`
   - **Environment Variables**: `BRAVE_API_KEY=your-api-key` Add a variables (space comma or newline separated)

3. Create a workflow that uses the MCP Client Enhanced node:
   - Add an MCP Client Enhanced node
   - Select the "List Tools" operation to see available search tools
   - Add another MCP Client Enhanced node
   - Select the "Execute Tool" operation
   - Choose the "brave_search" tool
   - Set Parameters to: `{"query": "latest AI news"}`

![Brave Search Example](./assets/brave-search-example.png)

The node will execute the search and return the results in the output.

### Example: Multi-Server Setup with AI Agent

This example demonstrates how to set up multiple MCP servers in a production environment and use them with an AI agent:

1. Configure your docker-compose.yml file:

```yaml
version: '3'

services:
  n8n:
    image: n8nio/n8n
    environment:
      # MCP server environment variables
      - MCP_BRAVE_API_KEY=your-brave-api-key
      - MCP_OPENAI_API_KEY=your-openai-key
      - MCP_SERPER_API_KEY=your-serper-key
      - MCP_WEATHER_API_KEY=your-weather-api-key

      # Enable community nodes as tools
      - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
    ports:
      - "5678:5678"
    volumes:
      - ~/.n8n:/home/node/.n8n
```

2. Create multiple MCP Client Enhanced credentials in n8n:

   **Brave Search Credentials**:
   - Command: `npx`
   - Arguments: `-y @modelcontextprotocol/server-brave-search`

   **OpenAI Tools Credentials**:
   - Command: `npx`
   - Arguments: `-y @modelcontextprotocol/server-openai`

   **Web Search Credentials**:
   - Command: `npx`
   - Arguments: `-y @modelcontextprotocol/server-serper`

   **Weather API Credentials**:
   - Command: `npx`
   - Arguments: `-y @modelcontextprotocol/server-weather`

3. Create an AI Agent workflow:
   - Add an AI Agent node
   - Enable MCP Client Enhanced as a tool
   - Configure different MCP Client Enhanced nodes with different credentials
   - Create a prompt that uses multiple data sources

![Multi-Server Setup](./assets/multi-server-example.png)

Example AI Agent prompt:
```
I need you to help me plan a trip. First, search for popular destinations in {destination_country}.
Then, check the current weather in the top 3 cities.
Finally, find some recent news about travel restrictions for these places.
```

With this setup, the AI agent can use multiple MCP tools across different servers, all using environment variables configured in your Docker deployment.

## Operations

The MCP Client Enhanced node supports the following operations:

![MCP Client Operations](./assets/operations.png)

- **Execute Tool** - Execute a specific tool with parameters
- **Get Prompt** - Get a specific prompt template (with enhanced parameter support)
- **List Prompts** - Get a list of available prompts
- **List Resources** - Get a list of available resources from the MCP server
- **List Tools** - Get a list of available tools
- **Read Resource** - Read a specific resource by URI

### Example: List Tools Operation

![List Tools Example](./assets/list-tools.png)

The List Tools operation returns all available tools from the MCP server, including their names, descriptions, and parameter schemas.

### Example: Execute Tool Operation

![Execute Tool Example](./assets/execute-tool.png)

The Execute Tool operation allows you to execute a specific tool with parameters. Make sure to select the tool you want to execute from the dropdown menu.

### Example: Enhanced Get Prompt Operation

The enhanced Get Prompt operation includes additional fields:

- **Prompt Name**: Name of the prompt template (same as original)
- **Prompt Parameters**: JSON parameters to customize the prompt (new feature)
- **Tenant ID**: Optional tenant identifier for multi-tenant servers (new feature)

Example usage:
```
Prompt Name: "summarize_text"
Prompt Parameters: {"length": "short", "style": "bullet_points", "language": "English"}
Tenant ID: "team-content" (optional)
```

## Using as a Tool

This node can be used as a tool in n8n AI Agents. To enable community nodes as tools, you need to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true`.

### Setting the Environment Variable

**If you're using a bash/zsh shell:**
```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
n8n start
```

**If you're using Docker:**
Add to your docker-compose.yml file:
```yaml
environment:
  - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

**If you're using the desktop app:**
Create a `.env` file in the n8n directory:
```
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

**If you want to set it permanently on Mac/Linux:**
Add to your `~/.zshrc` or `~/.bash_profile`:
```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

Example of an AI Agent workflow results:

![AI Agent Example](./assets/execute-tool-result.png)

After setting this environment variable and restarting n8n, your MCP Client Enhanced node will be available as a tool in AI Agent nodes.

## Compatibility

- Requires n8n version 1.0.0 or later
- Compatible with MCP Protocol version 1.0.0 or later
- Supports both STDIO and SSE transports for connecting to MCP servers
- SSE transport requires a server that implements the MCP Server-Sent Events specification
- **Fully backward compatible** with workflows using the original MCP client

## Support & Questions

For questions about the enhanced features or issues specific to this version:
- **Email**: contact@scalogic.ai
- **Issues**: [GitHub Issues](https://github.com/ScalogicAI/n8n-nodes-mcp-enhanced/issues)

For questions about core MCP functionality, please refer to the [original project](https://github.com/nerding-io/n8n-nodes-mcp).

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/)
* [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [MCP Transports Overview](https://modelcontextprotocol.io/docs/concepts/transports)
* [Using SSE in MCP](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/src/client/sse.ts)

## License

MIT License - see LICENSE file for details

---

**Built with ❤️ by ScalogicAI** | **Foundation by Jd Fiscus (@nerding-io)**