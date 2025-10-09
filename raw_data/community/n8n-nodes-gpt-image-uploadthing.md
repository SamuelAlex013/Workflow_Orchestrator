![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-gpt-image-uploadthing

Generate images with OpenAI and upload them to UploadThing directly from n8n.

This community node adds a single node: `OpenAI → UploadThing`, which:
- Generates an image using OpenAI’s Images API (`gpt-image-1`)
- Uploads the resulting image to UploadThing using `UTApi`

References:
- UploadThing server API (UTApi, UTFile): https://docs.uploadthing.com/api-reference/server
- OpenAI JavaScript SDK: https://www.npmjs.com/package/openai

## Prerequisites

- Node.js ≥ 20
- n8n installed and running
- OpenAI API key
- UploadThing token

## Installation

Install as a community node in n8n or via npm in your n8n extensions setup:

```
npm install n8n-nodes-gpt-image-uploadthing
```

Restart n8n so it loads the package.

## Credentials

Create two credentials in n8n:

1) OpenAI API
- API Key: your OpenAI key

2) UploadThing API
- Token: your UploadThing token

These correspond to the credential types exported by the package: `OpenAiApi` and `UploadThingApi`.

## Usage

Add the node “OpenAI → UploadThing” to your workflow and configure:

- Prompt: Text prompt to generate the image.
- Size: One of `1024×1024`, `1536×1024`, `1024×1536`.
- File Name: Output file name (e.g. `generated.png`).
- ACL: `public-read` or `private`.
- Content Disposition: `inline` or `attachment`.

Outputs (`json`):

- fileKey: UploadThing file key
- url: Public URL (respecting ACL)
- name: Stored file name
- sizeBytes: File size in bytes
- plus the input fields for reference

## Local development

```
npm i
npm run build
```

Link or install the built `dist` into your n8n environment. Lint and format:

```
npm run lint
npm run format
```

## Security notes

- Keep your OpenAI API key and UploadThing token secret in n8n credentials.
- If you set ACL to `private`, use signed URLs to access files as needed via UploadThing APIs.

## License

MIT
