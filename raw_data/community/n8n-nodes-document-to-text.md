# n8n-nodes-document-to-text

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials) <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Development](#development)  
[Publishing](#publishing)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation. After publishing/installation, restart n8n so it picks up the node from your installed package.

## Operations

This package provides a single node: `Document To Text`.

- Converts PDF documents to plain text using Azure OpenAI vision-capable chat models.
- Renders each PDF page to a PNG image and sends it to your Azure OpenAI deployment via the Chat Completions API.
- Merges the per‑page responses in order into a single `output` string.

Inputs

- `Document` (required): Base64 string of the PDF to convert. In n8n, reference the incoming binary data with an expression like `{{ $binary.myPdf.data }}`.

Parameters

- `Model (Deployment) Name` (required): The Azure OpenAI deployment name for your vision‑enabled model (for example, `gpt-4o`, `gpt-4o-mini`).
- `System Prompt` (required): Prompt used to instruct the model. A sensible default is provided to extract text without summarizing.
- `Scale (Render Zoom)`: PDF render scale (affects image resolution and token usage). Default `1.6`.
- `Temperature`: Sampling temperature for the model. Default `0.2`.
- `Max Parallel Requests`: Number of per‑page requests to issue concurrently. Default `1` (increase cautiously to avoid rate limits).

Output

- A single item per input with `json.output` (the extracted text) and `json.pages` (number of PDF pages processed).

Notes

- Supported input format: PDF only.
- Each PDF page results in one Chat Completions request; costs scale with page count and render `Scale`.
- Built‑in retry logic handles transient HTTP errors (429/5xx) with exponential backoff.

## Credentials

Use the built‑in n8n credential type `Azure OpenAI API` (`azureOpenAiApi`).

Prerequisites

- An Azure OpenAI resource with a deployed, vision‑capable chat model (for example, `gpt-4o`, `gpt-4o-mini`).
- Your resource `Endpoint` URL (e.g., `https://<your‑resource>.openai.azure.com/`).
- An `API Key` for the resource.
- API version supporting image inputs (default used by the node: `2024-02-15-preview`, or newer).

Set up

1. In n8n, create credentials of type `Azure OpenAI API`.
2. Enter the Endpoint, API Key, and (optionally) API Version.
3. In the node, select these credentials and specify your `Model (Deployment) Name` exactly as it’s named in Azure.

## Compatibility

- Node.js: `>= 20.15` (see `engines` in `package.json`).
- n8n: Community nodes must be enabled. Uses the n8n Nodes API v1.
- Platforms: Works on common Node.js platforms without a headless browser. Rendering uses `pdfjs-dist` with `@napi-rs/canvas`.
- Azure model requirement: A vision‑enabled chat model deployment (e.g., `gpt-4o`, `gpt-4o-mini`).

## Usage

Basic flow

1. Obtain a PDF in binary form in n8n (e.g., via `HTTP Request`, `Webhook`, `Google Drive`, `S3`, etc.). The file should appear under `$binary` on the incoming item.
2. Add the `Document To Text` node and connect it.
3. In the `Document` field, use an expression to reference the PDF binary, for example:
   - If your binary property is `myPdf`: `{{ $binary.myPdf.data }}`
   - Adjust the property name to match your workflow.
4. Select your `Azure OpenAI API` credentials and set `Model (Deployment) Name` to your Azure deployment (e.g., `gpt-4o`).
5. Optionally adjust `Scale`, `Temperature`, and `Max Parallel Requests`.
6. Execute the workflow. The node outputs a JSON object with:
   - `output`: the extracted text for the whole document
   - `pages`: the number of pages processed

Tips

- Start with `Max Parallel Requests = 1` to avoid `429` rate limits; increase gradually if your quota allows.
- Higher `Scale` improves text/image detail but increases token usage and cost.
- For very large PDFs, consider splitting or pre‑processing to control cost and execution time.

## Development

n8n doesn’t hot‑reload community nodes. To test locally:

1. Build the node

   ```bash
   npm run build
   ```

2. Link into n8n’s custom folder (one‑time)

   ```bash
   npm link // execute in the root of the repository
   mkdir -p ~/.n8n/custom
   cd ~/.n8n/custom
   npm link n8n-nodes-document-to-text
   ```

3. Start n8n locally (with debug logs enabled)

   ```bash
   N8N_LOG_LEVEL=debug N8N_LOG_PRETTY=true N8N_RUNNERS_ENABLED=true npx -y n8n
   ```

4. Develop
   - After code changes, run `npm run build` again.
   - Restart n8n to load the new build.

Notes

- If you change `package.json` entries (like the `n8n` registration), rebuild and restart n8n.
- If you use Docker, you can bind‑mount this package into `/home/node/.n8n/custom/node_modules/n8n-nodes-document-to-text/` and restart the container after builds.

## Publishing

Follow these steps to publish the package to npm:

1. Login to npm

   ```bash
   npm login
   ```

2. Verify metadata in `package.json`
   - `name`, `version`, `description`, `keywords` (include `n8n-community-node-package`), `repository`, `license`.
   - `files` includes `dist`, `README.md`, `LICENSE`.
   - `n8n` section correctly references built files in `dist/`.

3. Build and lint

   ```bash
   npm run prepublishOnly
   ```

4. Bump the version

   ```bash
   npm version patch   # or minor / major
   ```

5. Publish publicly

   ```bash
   npm publish --access public
   ```

6. Verify installation
   - Install into a clean environment or link into `~/.n8n/custom/`.
   - Restart n8n and confirm the node appears and works.

7. Release housekeeping (optional)
   - Tag the release in Git and create a GitHub release/changelog.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
