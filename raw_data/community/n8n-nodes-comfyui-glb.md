![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-comfyui

This package provides n8n nodes to integrate with [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - A powerful and modular stable diffusion GUI with a graph/nodes interface.

## Features

- Execute ComfyUI workflows directly from n8n
- Support for workflow JSON import
- Automatic mesh retrieval from workflow outputs
- Progress monitoring and error handling
- Support for API key authentication
- Configurable timeout settings

## Prerequisites

- n8n (version 1.0.0 or later)
- ComfyUI instance running and accessible
- Node.js 16 or newer

## Installation

```bash
npm install n8n-nodes-comfyui-glb
```

## Node Configuration

### ComfyUI Node

This node allows you to execute ComfyUI workflows and retrieve generated meshes.

#### Settings

- **API URL**: The URL of your ComfyUI instance (default: http://127.0.0.1:8188)
- **API Key**: Optional API key if authentication is enabled
- **Output Format**: The file extension you wish to retrieve
- **Workflow JSON**: The ComfyUI workflow in JSON format

#### Outputs

The node outputs an array of generated meshes with:
- `filename`: Name of the generated image file
- `data`: Base64 encoded mesh data

## Usage Example

1. Export your workflow from ComfyUI as JSON
2. Create a new workflow in n8n
3. Add the ComfyUI node
4. Paste your workflow JSON
5. Configure the API URL
6. Execute and retrieve generated meshes

## Error Handling

The node includes comprehensive error handling for:
- API connection issues
- Invalid workflow JSON
- Execution failures
- Timeout conditions (default 30 minutes)

## Development

```bash
# Install dependencies
npm install

# Build
npm run build

# Test
npm run test

# Lint
npm run lint
```

## License

[MIT](LICENSE.md)
 