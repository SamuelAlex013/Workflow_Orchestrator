<div align="center">
  <img src="https://raw.githubusercontent.com/deeptaggerhq/n8n-nodes-deeptagger/master/nodes/DeepTagger/deeptagger.svg" alt="DeepTagger Logo" width="200"/>
  <h1>DeepTagger</h1>
  <p><strong>n8n-nodes-deeptagger</strong></p>
</div>

This is an n8n community node that integrates [DeepTagger](https://deeptagger.com) into your n8n workflows. DeepTagger is an AI-powered document intelligence platform that automatically extracts structured data from documents like invoices, receipts, forms, and contracts.

[n8n](https://n8n.io/) is a fair-code licensed workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Usage](#usage)
[Resources](#resources)

## What is DeepTagger?

DeepTagger uses machine learning to extract structured information from documents automatically. Instead of writing complex extraction rules, you simply annotate a few example documents, and DeepTagger learns to extract similar data from new documents. It's perfect for automating data entry from invoices, receipts, forms, contracts, and other business documents.

## What does this node do?

The DeepTagger node allows you to:
- **Extract structured data** from documents (PDF, images, text) using pre-trained DeepTagger projects
- **Process both files and text** - upload documents or send text directly
- **Return structured JSON** - get clean, structured data ready for use in your workflows
- **Automate document processing** - integrate document intelligence into your automation workflows

## Prerequisites

- An active [DeepTagger account](https://deeptagger.com)
- A DeepTagger API key (available in your account settings)
- At least one trained DeepTagger project with a Project ID

## Installation

### For n8n Cloud users

n8n Cloud users can install this node directly from the n8n interface once it has been verified by the n8n team.

### For self-hosted n8n instances

Install the node using npm:

```bash
npm install n8n-nodes-deeptagger
```

Then restart your n8n instance. The DeepTagger node should now appear in your node list.

Alternatively, you can install it directly from the n8n interface by going to **Settings > Community Nodes** and entering `n8n-nodes-deeptagger`.

## Credentials

To use this node, you'll need to configure your DeepTagger API credentials:

1. In n8n, click on **Credentials** in the left sidebar
2. Click **New Credential**
3. Search for and select **DeepTagger API**
4. Enter your credentials:
   - **API Key**: Your DeepTagger API key (find this in your DeepTagger account settings)
   - **Base URL**: Leave as default (`https://deeptagger.com/api/v1`) unless using a custom deployment
5. Click **Save**

## Operations

### Extract Data

Extracts structured data from a document or text using a trained DeepTagger project.

**Parameters:**
- **Project ID** (required): The ID of your DeepTagger project (e.g., `fo_1759714105892`)
  - Find your Project ID by browsing to https://deeptagger.com/das/fos and opening a project - the ID will be in the URL
- **Input Type**: Choose between `File` (default) or `Text`
  - **File**: Upload a document (PDF, image, etc.) from a binary property
  - **Text**: Send raw text for extraction
- **Binary Property** (for File input): Name of the binary property containing the file (default: `data`)
- **Text** (for Text input): The text content to extract data from
- **Unwrap Response** (default: `true`): Whether to return only the extracted data or the full API response
  - **Enabled (default)**: Returns only the extracted data from the `data` field - clean, ready-to-use structured data
  - **Disabled**: Returns the complete API response including metadata like request ID, timestamp, etc.

## Usage

### Example 1: Extract Invoice Data from Uploaded Files

**Workflow:**
1. **Webhook Trigger** - Receive file upload
2. **DeepTagger Node** - Extract invoice data
   - Operation: `Extract Data`
   - Project ID: `fo_1759714105892` (your invoice extraction project)
   - Input Type: `File`
   - Binary Property: `data`
3. **Process Data** - Use extracted fields (invoice number, total, date, etc.) in subsequent nodes

**Use Case:** Automatically extract invoice details from uploaded PDFs and save them to your accounting system or database.

### Example 2: Extract Receipt Data from Email Attachments

**Workflow:**
1. **Email Trigger** - Monitor inbox for new emails with attachments
2. **Filter** - Only process emails with PDF or image attachments
3. **DeepTagger Node** - Extract receipt data
   - Project ID: Your receipt extraction project ID
   - Input Type: `File`
4. **Spreadsheet Node** - Add extracted data to Google Sheets or Airtable

**Use Case:** Process expense receipts sent via email and automatically log them in a spreadsheet.

### Example 3: Extract Form Data from Text

**Workflow:**
1. **Webhook Trigger** - Receive form submission as text
2. **DeepTagger Node** - Extract structured fields
   - Operation: `Extract Data`
   - Project ID: Your form extraction project ID
   - Input Type: `Text`
   - Text: `{{$json["formContent"]}}`
3. **CRM Node** - Create or update contact with extracted data

**Use Case:** Parse unstructured form submissions and create structured records in your CRM.

### Example 4: Batch Process Documents from Cloud Storage

**Workflow:**
1. **Schedule Trigger** - Run daily at midnight
2. **Google Drive Node** - List new PDFs in a specific folder
3. **Loop Over Items**
4. **DeepTagger Node** - Extract data from each document
5. **Database Node** - Insert extracted data
6. **Google Drive Node** - Move processed files to archive folder

**Use Case:** Automatically process new documents uploaded to a shared drive overnight.

### Example 5: Extract Contract Details for Legal Review

**Workflow:**
1. **Dropbox Trigger** - Monitor contracts folder
2. **DeepTagger Node** - Extract key contract terms
   - Project ID: Your contract extraction project ID
   - Input Type: `File`
3. **Slack Node** - Send notification with extracted terms to legal team
4. **Airtable Node** - Create contract record with extracted metadata

**Use Case:** Automatically extract and catalog key terms from new contracts for review and tracking.

## Troubleshooting

### Error: "No API key found in request"

**Solution:** Make sure you've configured your DeepTagger API credentials correctly. The API key must be set in the credentials and properly selected in the node.

### Error: "Project not found" or 404

**Solution:** Verify your Project ID is correct. You can find it in the URL when viewing your project at https://deeptagger.com/das/fos.

### Node not appearing in n8n

**Solution:**
- Restart your n8n instance after installation
- Check that the package is installed: `npm list n8n-nodes-deeptagger`
- For n8n Cloud, wait for the node to be verified by the n8n team

### Extraction results are not accurate

**Solution:**
- This node uses your trained DeepTagger projects. If results aren't accurate, you may need to:
  - Add more training examples in DeepTagger
  - Review and correct annotations in your project
  - Check that you're using the correct Project ID for the document type

### Binary data / file upload issues

**Solution:**
- Ensure the previous node outputs binary data in the property you specified (default: `data`)
- Use the **Move Binary Data** node if needed to reorganize your binary properties
- Check that the file type is supported by your DeepTagger project

## Resources

- [DeepTagger Documentation](https://deeptagger.com/docs)
- [DeepTagger Dashboard](https://deeptagger.com/das/fos)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Community Forum](https://community.n8n.io)

## Support

For issues related to:
- **This n8n node**: Open an issue on [GitHub](https://github.com/deeptaggerhq/n8n-nodes-deeptagger/issues)
- **DeepTagger API or platform**: Contact support@deeptagger.com
- **n8n platform**: Visit the [n8n community forum](https://community.n8n.io)

## License

[MIT](LICENSE)

## Version History

### 0.1.7 (2025-01-06)
- Add Unwrap Response option to return clean extracted data by default
- Improve README documentation with centered logo and examples
- Add comprehensive troubleshooting section

### 0.1.0 (2025-01-06)
- Initial release
- Extract Data operation with file and text input support
