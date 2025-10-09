![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-google-document-ai

This is an n8n community node. It lets you use Google Document AI in your n8n workflows.

Google Document AI is a cloud-based document processing service that uses machine learning to automatically extract text, tables, and other data from documents.

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

- Extract text from documents
- Extract tables from documents
- Extract entities from documents

## Credentials

To use this node, you need to authenticate with Google Cloud. You will need:

1. A Google Cloud Project with Document AI enabled
2. A Service Account with appropriate permissions
3. A JSON key file for the Service Account

### Getting the JSON Key
1. Go to the [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to "IAM & Admin" > "Service Accounts"
3. Create a new service account or select an existing one
4. Under "Keys", click "Add Key" > "Create new key"
5. Select "JSON" as the key type and click "Create"
6. Save the downloaded JSON key file securely

**Important Security Note**: Keep your service account JSON key secure and never share it publicly. In n8n, the key is stored encrypted in the credentials. When adding the credentials to n8n, you'll need to paste the entire contents of the JSON key file.

## Compatibility

This node is compatible with n8n version 0.150.0 and above. It has been tested with the latest version of n8n.

## Usage

This node allows you to process documents using Google Document AI. You can provide the document content as a binary file or a base64-encoded string. The node will return the extracted text, tables, and entities.

## Development

To develop this node, you can use the following commands:

```bash
npm install
npm link
npm run dev
```
In a separate terminal, run the following command to start the n8n server:

Locate the n8n directory and run the following 
( Note: to locate the .n8n directory - when starting the server `n8n start` look for the message: "User settings loaded from: ..." ) 

command:
```bash
cd .n8n
# ensure the custom folder is in the .n8n directory with npm initialised
mkdir custom    
cd custom 
npm init
npm link @n8n-nodes-google-document-ai
npm start
```


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Google Document AI documentation](https://cloud.google.com/document-ai/docs)

## Version history

### 1.0.0
- Initial release of the Google Document AI node.

### 1.1.0
- Added support for extracting tables and entities from documents.

### 1.2.0
- Improved error handling and added compatibility with n8n version 0.150.0 and above.

### 1.3.0
- Added support for processing binary files.
- Added support for processing file paths.
- Support for continueOnFail.
- Support for Google Cloud Vision API using credentials from Google Cloud Service Account JSON.

