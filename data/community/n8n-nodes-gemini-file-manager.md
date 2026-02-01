# n8n-nodes-gemini-file-manager

This is an n8n community node that allows you to manage files with the Google Gemini Files API. It enables batch uploading, listing, and managing files for use with Gemini AI models in your n8n workflows.

## Features

- **Upload Files**: Upload individual files to Gemini Files API from binary data or URLs
- **Batch Upload**: Upload multiple files at once for efficient processing
- **List Files**: Retrieve a list of all uploaded files with metadata
- **Get File Info**: Get detailed metadata about specific files
- **Delete Files**: Remove individual or multiple files from Gemini
- **Storage Integration**: (Planned) Upload files directly from Google Cloud Storage

## Installation

### Community Node (Recommended)

1. Go to **Settings** > **Community Nodes**
2. Select **Install a community node**
3. Enter `n8n-nodes-gemini-file-manager`
4. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-gemini-file-manager
```

## Prerequisites

You'll need a Google Gemini API key:

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Create or select a project
3. Generate an API key
4. Add the API key to your n8n credentials

## Credentials

This node uses the **Gemini API** credentials type. When setting up:

1. In n8n, go to **Credentials** > **New**
2. Search for "Gemini API"
3. Enter your API key
4. Save the credentials

## Usage

### Upload a Single File

1. Add the **Gemini File Manager** node to your workflow
2. Select **File** as the resource
3. Select **Upload** as the operation
4. Configure the input type (Binary or URL)
5. Connect your file source and execute

### Batch Upload Multiple Files

1. Select **Batch** as the resource
2. Select **Upload Multiple** as the operation
3. Specify comma-separated binary property names
4. Execute to upload all files in parallel

### Using Files with Gemini AI

After uploading files, you'll receive file URIs (e.g., `files/abc-123`) that can be used as references in Gemini AI model calls for multimodal processing.

## File Limitations

- **File Size**: Maximum 2GB per file
- **Storage**: Up to 20GB total per project
- **Expiry**: Files are automatically deleted after 48 hours
- **Supported Types**: Audio, video, images, documents (PDF, etc.)

## Node Reference

### Resources

- **File**: Operations on individual files
- **Batch**: Operations on multiple files

### Operations

#### File Resource
- **Upload**: Upload a single file
- **List**: List all uploaded files
- **Get**: Get file metadata
- **Delete**: Delete a file

#### Batch Resource
- **Upload Multiple**: Upload multiple files at once
- **Delete Multiple**: Delete multiple files
- **Upload from Storage**: (Planned) Upload from cloud storage

## Examples

### Example: Process Documents with AI

1. Upload multiple PDF documents using batch upload
2. Use the returned file URIs in a Gemini AI node
3. Ask questions about the documents' content

### Example: Media Analysis

1. Upload images or videos
2. Pass file references to Gemini for analysis
3. Extract insights, descriptions, or transcriptions

## Support

For issues and feature requests, please visit the [GitHub repository](https://github.com/jezweb/n8n-nodes-gemini-file-manager).

## License

MIT