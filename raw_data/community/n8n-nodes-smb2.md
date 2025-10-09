![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)
# n8n-nodes-smb2

This is an n8n community node that lets you interact with Samba/SMB2 file shares in your n8n workflows. It enables reading, writing, and managing files on SMB2-compatible network shares.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The node supports the following operations:

### Download
Downloads a file from the SMB share.
- **Path**: Full path to the file on the share (e.g., `/public/documents/file.txt`)
- **Put Output File in Field**: Name of the binary property to store the file data (default: `data`)

### Upload
Uploads a file to the SMB share.
- **Path**: Destination path on the share where the file will be saved

### List
Lists the contents of a directory on the SMB share.
- **Path**: Directory path to list (e.g., `/public/folder`)

### Delete
Deletes a file or folder from the SMB share.
- **Path**: Path to the file or folder to delete

### Rename/Move
Renames or moves a file or folder on the SMB share.
- **Old Path**: Current path of the file/folder
- **New Path**: New path/name for the file/folder

## Credentials

You need the following credentials to connect to an SMB share:

- **Host**: The hostname or IP address of the SMB server
- **Share Name**: The name of the share to connect to
- **Username**: Username for authentication
- **Password**: Password for authentication
- **Domain**: (Optional) Domain name for Active Directory authentication

## Compatibility

- Requires n8n version 1.0.0 or later
- Node.js v18.10 or later
- Compatible with SMB2/SMB3 protocol

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [SMB2 Protocol Documentation](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/5606ad47-5ee0-437a-817e-70c366052962)
* [Samba Documentation](https://www.samba.org/samba/docs/)

## Error Handling

The node provides detailed error messages for common SMB issues:
- Access denied errors
- Network connectivity issues
- File/path not found
- Share not found
- Authentication failures
- Quota issues
- File sharing violations
