
![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-comfyui-media

This package provides n8n nodes to integrate with [ComfyUI](https://github.com/comfyanonymous/ComfyUI) —  
a powerful and modular stable diffusion GUI with a graph/nodes interface.

## Features

- Execute full ComfyUI workflows from n8n
- Upload input media (images) to ComfyUI directly
- Generate **images and videos** from workflows
- Automatic output retrieval (images, gifs, mp4, webp, etc.)
- Progress monitoring and error handling
- API key authentication support
- Configurable timeout settings

## Prerequisites

- n8n (version 1.0.0 or later)
- ComfyUI instance running and accessible
- Node.js 18 or newer

## Installation

```bash
npm install n8n-nodes-comfyui-media
````

---

## Node Types

### 1. ComfyUI Media Upload Node

Uploads an image from your workflow to ComfyUI so it can be used as an input in a workflow.

#### Settings

* **API URL**: The URL of your ComfyUI instance (default: `http://127.0.0.1:8188`)
* **API Key**: Optional API key if authentication is enabled
* **Input Type**: Choose between `URL`, `Base64`, or `Binary`
* **Input Image**: URL or base64 string (when using URL/Base64)
* **Binary Property**: Name of the binary property containing the image (when using Binary)

#### Outputs

* Returns uploaded image metadata:

  * `name`: Filename assigned in ComfyUI
  * `subfolder`: Storage subfolder
  * `type`: File type

---

### 2. ComfyUI Workflow to Media Node

Executes a ComfyUI workflow and retrieves all generated media (images & videos).

#### Settings

* **API URL**: The URL of your ComfyUI instance (default: `http://127.0.0.1:8188`)
* **API Key**: Optional API key if authentication is enabled
* **Workflow JSON**: The ComfyUI workflow definition in JSON format
* **Timeout**: Maximum time in minutes to wait for workflow execution

#### Outputs

The node outputs one item per generated media file. Each output includes:

* **json**

  * `fileName`: Name of the file
  * `mimeType`: Detected MIME type
  * `data`: Base64 encoded data
  * `status`: Execution status
* **binary.data**

  * `fileName`: Same file name
  * `fileType`: `"image"` or `"video"`
  * `fileSize`: File size in KB
  * `fileExtension`: File extension (`png`, `jpg`, `gif`, `webp`, `mp4`)
  * `mimeType`: MIME type

> ⚡ The node automatically distinguishes between **images** and **videos** and returns both.

---

## Usage Examples

### Upload + Execute Workflow

1. Add **ComfyUI Media Upload** node

   * Configure input type (URL, Base64, or Binary)
   * Upload the image to your ComfyUI instance

2. Add **ComfyUI Workflow to Media** node

   * Paste your exported workflow JSON from ComfyUI
   * Configure timeout if needed
   * Run execution to generate **images/videos**

3. Use the resulting binary outputs in downstream n8n nodes (e.g., save to disk, upload to cloud, send via email).

---

## Error Handling

Both nodes include error handling for:

* API connection issues
* Invalid workflow JSON
* Invalid or missing input media
* Execution failures
* Timeout conditions

---

## Development

```bash
# Install dependencies
pnpm install

# Build
pnpm build

# Dev mode (watch)
pnpm dev

# Lint
pnpm lint

# Auto-fix lint issues
pnpm lintfix
```

---

## License

[MIT](LICENSE.md)

```
