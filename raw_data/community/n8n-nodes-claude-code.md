# n8n-nodes-claude-code

This is an n8n community node that provides integration with Claude Code SDK, allowing you to execute Claude commands programmatically within your n8n workflows.

## Features

- **Direct SDK Integration**: Uses the Claude Code SDK instead of shell commands
- **No Shell Escaping**: Eliminates complex escaping issues with quotes and special characters
- **Existing Credentials**: Automatically uses Claude CLI credentials already configured on your server
- **Flexible Configuration**: Support for all Claude CLI options through the UI
- **Multiple Output Formats**: Text, JSON, or full response data

## Installation

### In n8n

1. Go to **Settings > Community Nodes**
2. Select **Install a community node**
3. Enter `n8n-nodes-claude-code`

### Manual installation

To install this node manually:

```bash
cd ~/.n8n/custom
npm install n8n-nodes-claude-code
```

## Prerequisites

- Claude CLI must be installed and configured on the server
- Valid Claude API credentials (the SDK will use existing CLI authentication)

## Node Reference

### Input Parameters

- **Prompt** (required): The main prompt to send to Claude (equivalent to `-p` flag)
- **Context** (optional): Additional context or file content (equivalent to `-c` flag)

### Options

- **Allowed Tools**: Comma-separated list of allowed tools (e.g., `Bash(git log:*),Bash(git diff:*)`)
- **System Prompt**: Custom system instructions
- **Max Turns**: Maximum number of conversation turns (default: 1)
- **Output Format**: Choose between Text, JSON, or Full Response
- **Non-Interactive**: Run in non-interactive mode (default: true)
- **Permission Mode**: Standard, Strict, or Relaxed

## Usage Examples

### Basic Usage

1. Add the Claude Code node to your workflow
2. Enter your prompt in the Prompt field
3. Optionally add context
4. Configure allowed tools if needed
5. Execute the node

### Example: Git Operations

**Prompt**: "Show me the last 5 commits"

**Allowed Tools**: `Bash(git log:*)`

### Example: Code Analysis

**Prompt**: "Analyze this code and suggest improvements"

**Context**: `[paste your code here]`

### Migrating from Execute Command

Instead of using Execute Command node with:
```bash
script -q -c "claude --allowedTools 'Bash(git log:*)' -p \"Your prompt\"" /dev/null
```

Simply use this node with:
- Prompt: "Your prompt"
- Allowed Tools: "Bash(git log:*)"

## Development

To build this node locally:

```bash
# Install dependencies
npm install

# Build
npm run build

# Run linter
npm run lint
```

## License

[MIT](LICENSE.md)