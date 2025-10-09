# n8n-nodes-vimeo

This is an n8n community node. It lets you use Vimeo in your n8n workflows.

Vimeo is a video hosting platform. This node allows you to upload videos to your Vimeo account using the Vimeo API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Upload Video
  - Upload a binary file from the current item to Vimeo using the TUS resumable upload approach.
  - Inputs:
    - Binary Property: name of the binary property that contains the video (default: `data`).
    - Title: optional video title.
    - Description: optional video description.
  - Output fields include:
    - `videoUri` – Vimeo video URI (e.g. `/videos/123456789`).
    - `link` – Public Vimeo link when available.
    - `name`, `mimeType`, `fileName` – basic metadata echoed back.

## Credentials

Create credentials in n8n with type `Vimeo API`:

- Client ID: from your Vimeo app (`https://developer.vimeo.com/apps`).
- Client Secret: from your Vimeo app.
- Access Token: a personal access token or OAuth token with at least `upload` and `edit` scopes.

The node authenticates requests using the Access Token via the `Authorization: Bearer <token>` header.

## Compatibility

- Node.js: 20+
- n8n Community Nodes API version: 1

## Usage

1. In your workflow, add a node that provides a binary file (for example, an HTTP Request node that downloads a file, or a Read Binary File node).
2. Add the Vimeo node and select the `Upload Video` operation.
3. Set the Binary Property to the property name that holds the video (default is `data`).
4. Optionally set Title and Description.
5. Select your `Vimeo API` credentials.
6. Run the workflow. The node returns the `videoUri` and `link` to the uploaded video once the upload is initiated and completed by Vimeo.

Notes:

- Uploads use Vimeo’s TUS endpoint; very large files are supported. This node performs a single-pass upload starting at offset `0`. If you need advanced resumable behavior across executions, consider externalizing the upload session management.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Vimeo API reference](https://developer.vimeo.com/api/reference)
- [Vimeo Node.js library (@vimeo/vimeo)](https://www.npmjs.com/package/@vimeo/vimeo)
- [TUS protocol (resumable upload)](https://tus.io/)

## Version history

- 0.1.0 — Initial release with Upload Video operation
