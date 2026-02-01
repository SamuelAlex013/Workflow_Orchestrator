![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-zip-processor

This is an n8n community node. It lets you use ZIP compression and extraction capabilities in your n8n workflows.

This node allows you to create and extract ZIP files, with optional password protection, working with base64-encoded data.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **ZIP**: Compress files into a ZIP archive
  - Supports optional password protection using AES-256 encryption
  - Takes base64-encoded input and produces a base64-encoded ZIP file
  - Allows custom output filename

- **Unzip**: Extract files from a ZIP archive
  - Supports password-protected archives
  - Returns extracted files as base64-encoded data
  - Preserves original filenames

## Compatibility

This node has been tested with n8n version 1.0+ and requires the following dependencies:
- archiver
- archiver-zip-encrypted
- @zip.js/zip.js

## Usage

### Zipping Files
1. Provide a base64-encoded file buffer as input
2. Set the desired output filename
3. Optionally set a password for encryption
4. The node will return a base64-encoded ZIP file

### Extracting Files
1. Provide a base64-encoded ZIP file
2. If the archive is password-protected, provide the password
3. The node will return an array of extracted files with their names and base64-encoded content

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Archiver documentation](https://www.archiverjs.com/)
* [zip.js documentation](https://gildas-lormeau.github.io/zip.js/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
