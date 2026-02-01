## Presenton for n8n

Generate professional presentations with the Presenton API directly from your n8n workflows. This community node supports asynchronous presentation generation, file uploads, and task status checks.

Homepage: [presenton.ai](https://presenton.ai) • API docs: [presenton.ai/docs/api-reference](https://presenton.ai/docs/api-reference)

### Features

- **Generate Presentation (Async)**: Kick off a background job to create PPTX or PDF
- **Check Presentation Status**: Poll a task by ID until it’s complete
- **Upload File**: Upload binary files and reference them during generation

## Installation

### Install in n8n (Community nodes)

1. In n8n, go to Settings → Community Nodes → Install.
2. Search for or enter the package name: `n8n-nodes-Presenton`.
3. Confirm installation and restart n8n if prompted.

### Self-hosted filesystem install

If you mount community nodes from disk, add this package to your custom nodes directory and install:

```bash
npm install n8n-nodes-Presenton
```

Minimum Node.js version: 20

## Credentials

Create credentials of type `Presenton API`:

- **API Key**: Your Presenton API key
- **Base API URL** (optional): Override the default `https://api.presenton.ai` for staging or self-hosted deployments

The node adds the `Authorization: Bearer <apiKey>` header automatically.

## Node operations

### Generate Presentation (Async)

Starts a background job: `POST /api/v1/ppt/presentation/generate/async`

- **content**: Main content to generate from
- **slides_markdown**: Optional list of slide markdown strings
- **instructions**: Additional guidance for the generator
- **tone**: `default | professional | educational | funny | sale_pitch | causal`
- **verbosity**: `standard | concise | text-heavy`
- **web_search**: Allow web search during generation (boolean)
- **image_type**: `stock | ai-generated`
- **theme**: Theme name (string)
- **noOfSlides**: Number of slides (number)
- **language**: e.g. `English`
- **template**: e.g. `general`
- **include_table_of_contents**: boolean
- **include_title_slide**: boolean
- **files**: A file ID returned by the Upload File operation (string[])
- **export_as**: `pptx | pdf`

The node cleans empty values before sending. Response typically includes a task identifier you can pass to Check Presentation Status.

### Check Presentation Status

Checks a task: `GET /api/v1/ppt/presentation/status/{taskId}`

- **taskId**: The ID returned by Generate Presentation (Async)

Returns the current status. When complete, the API usually includes result metadata (such as download links) defined by Presenton.

### Upload File

Uploads a binary file: `POST /api/v1/ppt/files/upload`

- **binaryPropertyName**: Name of the binary property on the incoming item (default: `data`)

Returns a file ID you can set in the `files` field of the Generate Presentation (Async) operation.

## Typical workflow examples

### Generate a presentation from text

1. Set operation to “Generate Presentation (Async)”.
2. Fill in `content`, choose `export_as` (e.g. `pptx`), adjust options (tone, verbosity, slides, etc.).
3. Use “Check Presentation Status” with the returned `taskId` until status is complete.

### Upload then generate

1. Add a node with operation “Upload File” and set `binaryPropertyName` to the property holding your file.
2. From its response, read the returned `file id`.
3. Pass that id into the `files` field of “Generate Presentation (Async)”, then check status as above.

## Error handling

- The node validates required parameters and throws meaningful errors (e.g., invalid slide count, missing task ID, or missing binary data).
- If you enable “Continue On Fail”, errors are returned in the item’s JSON so your workflow can handle them.

## Development

Clone, install, and build:

```bash
npm i
npm run dev   # TypeScript watch
# or
npm run build # build to dist
```

Linting and formatting:

```bash
npm run lint
npm run lintfix
npm run format
```

To test locally, follow n8n’s guide to running custom nodes and point n8n to your built `dist` directory.

## License

MIT
