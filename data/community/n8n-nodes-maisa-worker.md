# n8n-nodes-maisa-worker

![Maisa Worker Node](https://img.shields.io/badge/n8n-node-FF6D5A?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

N8N community node for integrating with Maisa Worker API. This node allows you to run AI workers, poll for completion, and automatically download output files.

## Features

- 🚀 **Run Worker**: Execute workers and automatically wait for completion
- ⚡ **Async Execution**: Start workers without waiting for results
- 📊 **Status Polling**: Configurable polling interval to check execution status
- 📁 **File Handling**: Automatic download of output files
- 🔄 **Multiple Operations**: Run, get status, list files, and download files
- ⏱️ **Timeout Control**: Configurable timeout for long-running operations
- 📤 **File Upload**: Support for uploading input files to workers

## Installation

### Community Node Installation (Recommended)

1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter `n8n-nodes-maisa-worker`
4. Click **Install**

### Manual Installation

Navigate to your n8n installation directory and run:

```bash
npm install n8n-nodes-maisa-worker
```

For Docker installations:

```bash
docker exec -it n8n npm install n8n-nodes-maisa-worker
```

### Development Installation

Clone this repository and link it to your n8n installation:

```bash
# Clone the repository
git clone https://github.com/juanpedrolozano-cyber/MaisaWorkern8n.git
cd MaisaWorkern8n

# Install dependencies
npm install

# Build the node
npm run build

# Link to n8n (adjust path to your n8n installation)
npm link
cd /path/to/n8n
npm link n8n-nodes-maisa-worker
```

## Configuration

### Credentials Setup

1. In n8n, go to **Credentials** > **New**
2. Search for "Maisa Worker API"
3. Enter your API Key (ms-api-key)
4. Save the credentials

### Node Parameters

#### Base URL
The base URL of your Maisa Worker API endpoint.

Example: `https://api.maisaworker.com/v1`

## Operations

### 1. Run Worker (with polling)

Starts a worker execution and automatically polls until completion. Optionally downloads all output files.

**Parameters:**
- **Base URL**: API endpoint URL
- **Input Variables**: Array of name-value pairs to pass to the worker
- **Files**: Binary property names containing files to upload (comma-separated)
- **Polling Interval**: How often to check for completion (default: 5 seconds)
- **Timeout**: Maximum wait time (default: 300 seconds)
- **Auto Download Files**: Automatically download output files when complete (default: true)

**Example Input Variables:**
```json
[
  { "name": "excel_file", "value": "" },
  { "name": "prompt", "value": "Analyze this data" }
]
```

**Output:**
```json
{
  "id": "680b643bc199d0389c6babd1",
  "workerId": "...",
  "result": "Analysis complete",
  "steps": [...],
  "timeSpent": 45.2,
  "executionId": "680b643bc199d0389c6babd1",
  "outputFiles": [
    {
      "fileName": "story.pdf",
      "id": "6877baf9092a7c3b56d229bb"
    }
  ]
}
```

### 2. Run Worker (Async)

Starts a worker execution without waiting for completion. Returns the execution ID immediately.

**Parameters:**
- Same as Run Worker, but without polling options

**Output:**
```json
{
  "status": "success",
  "data": "680b643bc199d0389c6babd1"
}
```

### 3. Get Status

Retrieves the current status of a worker execution.

**Parameters:**
- **Execution ID**: The ID returned from Run Worker

**Output:**
```json
{
  "status": "success",
  "data": {
    "id": "680b643bc199d0389c6babd1",
    "workerId": "...",
    "result": "...",
    "steps": [...],
    "timeSpent": 45.2
  }
}
```

### 4. List Files

Lists all input and output files from a worker execution.

**Parameters:**
- **Execution ID**: The ID of the worker execution

**Output:**
```json
{
  "status": "success",
  "data": {
    "out": [
      {
        "id": "6877baf9092a7c3b56d229bb",
        "fileKey": "6877babcdcdedab5ff8865ad/output/story.pdf",
        "fileName": "story.pdf",
        "createdAt": "2025-07-16T14:45:13.999Z"
      }
    ],
    "in": null
  }
}
```

### 5. Download File

Downloads a specific file from a worker execution.

**Parameters:**
- **Execution ID**: The ID of the worker execution
- **File Name**: Name of the file to download
- **Binary Property**: Property name to store the downloaded file (default: "data")

**Output:**
Binary data stored in the specified property, accessible in subsequent nodes.

## Usage Examples

### Example 1: Simple Worker Execution

```
1. Maisa Worker Node (Run Worker)
   - Base URL: https://api.maisaworker.com/v1
   - Input Variables:
     - name: "prompt"
     - value: "Generate a report"
   - Auto Download Files: true

2. Output: Execution result + downloaded files as binary data
```

### Example 2: Upload File and Process

```
1. Read Binary File Node
   - Read: input.xlsx

2. Maisa Worker Node (Run Worker)
   - Base URL: https://api.maisaworker.com/v1
   - Input Variables:
     - name: "excel_file"
     - value: ""
   - Files: "data" (from previous node)
   - Polling Interval: 10 seconds

3. Output: Processed results + output files
```

### Example 3: Async Execution with Manual Status Check

```
1. Maisa Worker Node (Run Worker Async)
   - Base URL: https://api.maisaworker.com/v1
   - Input Variables: [...]
   
2. Wait Node
   - Wait: 30 seconds

3. Maisa Worker Node (Get Status)
   - Execution ID: {{$json["data"]}}

4. Maisa Worker Node (List Files)
   - Execution ID: {{$json["data"]["id"]}}

5. Maisa Worker Node (Download File)
   - Execution ID: {{$json["data"]["id"]}}
   - File Name: {{$json["data"]["out"][0]["fileName"]}}
```

## API Reference

This node implements the following Maisa Worker API endpoints:

- `POST /run` - Run worker endpoint
- `GET /run/{executionId}` - Get worker run status
- `GET /run/{executionId}/files` - List files
- `GET /run/{executionId}/files/{fileName}` - Download file

## Development

### Build

```bash
npm run build
```

### Watch Mode

```bash
npm run dev
```

### Lint

```bash
npm run lint
npm run lintfix
```

### Format

```bash
npm run format
```

## Troubleshooting

### Worker Timeout
If your worker takes longer than the default timeout (300 seconds), increase the **Timeout** parameter.

### Files Not Downloading
Ensure **Auto Download Files** is enabled and the worker has completed successfully.

### API Key Issues
Verify your API key is correct in the credentials and has the necessary permissions.

### Polling Too Frequent
If you're hitting rate limits, increase the **Polling Interval** parameter.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

- 📧 Email: jp@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/juanpedrolozano-cyber/MaisaWorkern8n/issues)
- 📖 Documentation: [Maisa Worker Docs](https://docs.maisaworker.com)

## Changelog

### 1.0.0 (2025-10-04)
- Initial release
- Run Worker with automatic polling
- Async worker execution
- Get status operation
- List files operation
- Download file operation
- Automatic file download on completion
- Configurable polling interval and timeout
