# OnlyOffice n8n Node

A comprehensive n8n node for integrating with OnlyOffice Document Server, providing full folder and file management capabilities.

## Features

### Folder Operations
- **List Folders**: List all folders you have access to
- **Create Folder**: Create new folders in your OnlyOffice instance
- **Rename Folder**: Rename existing folders
- **Move/Copy Folder**: Move or copy folders to different locations
- **Delete Folder**: Delete folders (with option for immediate deletion or trash)

### File Operations
- **List Files**: List all files within your OnlyOffice instance
- **Create File**: Create new documents (Word, Excel, PowerPoint)
- **Rename File**: Rename existing files
- **Move/Copy File**: Move or copy files to different locations
- **Delete File**: Delete files (with option for immediate deletion or trash)

## Installation

### Self-Hosted n8n

1. Install the package in your n8n instance:
   ```bash
   npm install n8n-nodes-onlyoffice
   ```

2. Restart your n8n instance to load the new node.

### n8n Cloud

⚠️ **Important**: This community node is currently **not verified** for n8n Cloud. n8n Cloud only supports verified community nodes for security and stability reasons.

**Options for n8n Cloud users:**

1. **Request Verification**: Contact n8n support to request verification of this node for cloud use
2. **Self-Host**: Consider using a self-hosted n8n instance which supports all community nodes
3. **Alternative**: Use built-in HTTP Request nodes to interact with the OnlyOffice API directly

**Why the limitation?** n8n Cloud maintains a curated list of verified community nodes to ensure security, performance, and reliability for all cloud users. While this node works perfectly in self-hosted environments, it requires verification before being available in n8n Cloud.

## Configuration

### Credentials Setup

1. In n8n, go to **Credentials** and create a new **OnlyOffice API** credential
2. Configure the following:
   - **Base URL**: Your OnlyOffice instance URL (e.g., `https://your-onlyoffice-instance.com`)
   - **Access Token**: Your OnlyOffice API token

### Getting Your API Token

1. Log into your OnlyOffice instance
2. Go to **Settings** → **Integration** → **API**
3. Generate a new API token
4. Copy the token to use in n8n credentials

## Usage Examples

### List Files in My Documents
1. Add the OnlyOffice node to your workflow
2. Set **Resource** to "File"
3. Set **Operation** to "List"
4. Set **Folder ID** to `@my` (for My Documents) or `@common` (for Common Documents)

### Create a New Document
1. Set **Resource** to "File"
2. Set **Operation** to "Create"
3. Set **Parent Folder ID** to `@my`
4. Set **Title** to your desired filename (without extension)
5. Choose **File Type** (Document, Spreadsheet, or Presentation)

### Move a File
1. Set **Resource** to "File"
2. Set **Operation** to "Move"
3. Set **Item ID** to the ID of the file to move
4. Set **Destination Folder ID** to the target folder ID
5. Choose **Conflict Resolution** strategy

## Folder IDs

- `@my` - My Documents folder
- `@common` - Common Documents folder
- `@shared` - Shared Documents folder
- `@trash` - Trash folder
- Or use specific folder IDs obtained from list operations

## File Types

When creating files, you can choose from:
- **Document (.docx)**: Microsoft Word compatible documents
- **Spreadsheet (.xlsx)**: Microsoft Excel compatible spreadsheets
- **Presentation (.pptx)**: Microsoft PowerPoint compatible presentations

## Conflict Resolution

When moving or copying files/folders, you can choose how to handle conflicts:
- **Skip**: Skip the operation if a file/folder with the same name exists
- **Overwrite**: Replace the existing file/folder
- **Duplicate**: Create a copy with a different name

## API Endpoints Used

This node uses the OnlyOffice Document Server API v2.0:
- `GET /api/2.0/files/{folderId}` - List folder contents
- `POST /api/2.0/files/folder/{parentFolderId}` - Create folder
- `POST /api/2.0/files/{parentFolderId}/file` - Create file
- `PUT /api/2.0/files/folder/{itemId}` - Rename folder
- `PUT /api/2.0/files/file/{itemId}` - Rename file
- `PUT /api/2.0/files/fileops/move` - Move items
- `PUT /api/2.0/files/fileops/copy` - Copy items
- `DELETE /api/2.0/files/folder/{itemId}` - Delete folder
- `DELETE /api/2.0/files/file/{itemId}` - Delete file

## Development

### Building the Node

```bash
npm install
npm run build
```

### Development Mode

```bash
npm run dev
```

### Linting

```bash
npm run lint
npm run lintfix
```

## License

MIT

## Support

For issues and feature requests, please create an issue in the GitHub repository.
