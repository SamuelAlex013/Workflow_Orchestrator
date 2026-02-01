![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-unlockpdf

An n8n community node for unlocking password-protected PDF files using the pdfmunk API.

## What is PDF Unlocking?

PDF unlocking is the process of removing password protection from encrypted PDF documents. Many PDF files are protected with user passwords or owner passwords that restrict access to viewing, editing, printing, or copying content. This node allows you to programmatically remove these restrictions when you have the correct password.

### Types of PDF Protection

- **User Password (Open Password)**: Prevents opening and viewing the PDF
- **Owner Password (Permissions Password)**: Restricts editing, printing, copying, and other operations
- **Certificate-based Security**: Uses digital certificates for access control

## Features

- **Password-Protected PDF Unlocking**: Remove password protection from encrypted PDF files
- **Batch Processing**: Process multiple PDF files in a single workflow
- **Binary Data Support**: Handle PDF files as binary data within n8n workflows
- **Multiple Output Formats**: Choose between URL links or direct binary downloads
- **Error Handling**: Comprehensive validation and error reporting
- **Secure Credential Management**: API keys stored securely in n8n's credential system
- **File Validation**: Automatic validation of PDF file integrity and format

## Use Cases

### 1. Document Management Systems
- **Automated Archive Processing**: Unlock legacy PDF documents for digital archiving
- **Content Migration**: Remove protection when migrating documents between systems
- **Backup Preparation**: Ensure backup copies are accessible without password constraints

### 2. Business Process Automation
- **Invoice Processing**: Unlock password-protected invoices for automated data extraction
- **Contract Management**: Remove protection from signed contracts for processing workflows
- **Report Generation**: Unlock protected reports before merging or analyzing data
- **Compliance Documentation**: Process protected compliance documents for audit trails

### 3. Data Processing Workflows
- **Text Extraction**: Unlock PDFs before extracting text content for analysis
- **PDF Merging**: Remove protection before combining multiple PDFs
- **Format Conversion**: Unlock files before converting to other formats (Word, Excel, etc.)
- **OCR Processing**: Remove protection before applying optical character recognition

### 4. Educational and Research
- **Academic Paper Processing**: Unlock research papers for institutional repositories
- **Library Systems**: Process protected documents for digital collections
- **Student Submission Processing**: Handle password-protected assignments and projects

### 5. Legal and Financial Services
- **Document Discovery**: Unlock protected legal documents for review processes
- **Financial Report Processing**: Remove protection from financial statements for analysis
- **Due Diligence**: Process protected documents during merger and acquisition activities

### 6. Content Publishing
- **Publishing Workflows**: Remove protection from manuscripts before editorial processing
- **Translation Services**: Unlock documents before sending for translation
- **Quality Assurance**: Process protected documents through review workflows

### 7. Customer Service Automation
- **Support Ticket Processing**: Unlock customer-submitted protected documents
- **Document Verification**: Process protected identity documents for verification
- **Claims Processing**: Handle password-protected insurance or warranty claims

## Workflow Examples

### Example 1: Batch Document Processing
```
Email Trigger → Extract Attachments → Unlock PDF → Extract Text → Store in Database
```

### Example 2: Archive Management
```
Schedule Trigger → Read Files from Folder → Unlock PDF → Convert to Searchable PDF → Upload to Cloud Storage
```

### Example 3: Invoice Processing
```
Webhook → Receive PDF Invoice → Unlock PDF → Extract Invoice Data → Update Accounting System
```

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install a community node**
3. Enter `n8n-nodes-unlockpdf` in the npm package name field
4. Click **Install**

### Manual Installation

1. Navigate to your n8n installation directory
2. Run: `npm install n8n-nodes-unlockpdf`
3. Restart your n8n instance

## Prerequisites

- An active pdfmunk API account and API key
- n8n version 0.187.0 or later
- [git](https://git-scm.com/downloads)
- Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
- Install n8n with:
  ```
  npm install n8n -g
  ```
- Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Getting Started with pdfmunk API

### How to Get Your pdfmunk API Key

1. **Sign up for pdfmunk**
   - Visit [pdfmunk.com](https://pdfmunk.com)
   - Click on "Sign Up" or "Get Started"
   - Create your account with your email and password

2. **Verify Your Account**
   - Check your email for a verification link
   - Click the verification link to activate your account

3. **Access Your Dashboard**
   - Log in to your pdfmunk account
   - Navigate to the API section or Dashboard

4. **Generate API Key**
   - Look for "API Keys" or "Developer" section in your dashboard
   - Click "Generate New API Key" or "Create API Key"
   - Copy and securely store your API key
   - **Important**: Keep your API key secure and never share it publicly

5. **Check Your Plan Limits**
   - Review your current plan's API usage limits
   - Upgrade your plan if needed for higher usage requirements

### API Key Security Best Practices

- Store your API key in n8n's credential system (never hardcode it)
- Rotate your API keys regularly
- Monitor your API usage in the pdfmunk dashboard
- Use different API keys for development and production environments

## Configuration

### 1. Set up pdfmunk API Credentials

1. In your n8n instance, go to **Settings > Credentials**
2. Click **Create New Credential**
3. Search for "pdfmunk API" and select it
4. Enter your pdfmunk API key obtained from the steps above
5. Optionally, add a name to identify this credential (e.g., "pdfmunk Production")
6. Test the connection to ensure your API key is valid
7. Save the credential

### 2. Add the Unlock PDF Node

1. In your workflow, click the **+** button to add a new node
2. Search for "Unlock PDF"
3. Select the "Unlock PDF" node

## Usage

### Input Parameters

- **PDF File in Binary**: Name of the binary property containing the PDF file (default: "data")
- **Password**: The password required to unlock the PDF file
- **Output Name**: Desired filename for the unlocked PDF (default: "unlocked_file.pdf")
- **Output Type**: Choose between:
  - **URL**: Returns a download URL for the unlocked PDF
  - **Download**: Returns the PDF file as binary data

### Example Workflow

1. **Read Binary Files** node → Upload or read a password-protected PDF
2. **Unlock PDF** node → Configure with password and output preferences
3. **Write Binary File** node (if using Download output) → Save the unlocked PDF

### Sample Configuration

```json
{
  "binaryPropertyName": "data",
  "password": "your_pdf_password",
  "outputName": "unlocked_document.pdf",
  "outputType": "download"
}
```

## Error Handling

The node includes comprehensive error handling for:
- Invalid binary data
- Empty PDF files
- Authentication failures
- API connection issues
- Incorrect passwords

Enable "Continue on Fail" in the node settings to handle errors gracefully in your workflow.

## API Reference

This node uses the pdfmunk API endpoint:
- **URL**: `https://pdfmunk.com/api/v1/unlockPdf`
- **Method**: POST
- **Format**: multipart/form-data

## Troubleshooting

### Common Issues

1. **"Invalid binary data" error**
   - Ensure the binary property name matches your input data
   - Verify the PDF file is properly uploaded

2. **Authentication failed**
   - Check your pdfmunk API credentials
   - Ensure your API key has sufficient permissions

3. **"Empty binary data" error**
   - Verify the PDF file isn't corrupted
   - Check that the binary data property contains valid data

## Development

### Building from Source

```bash
git clone https://github.com/yourusername/n8n-nodes-unlockpdf.git
cd n8n-nodes-unlockpdf
npm install
npm run build
```

### Testing

```bash
npm run test
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature`
6. Submit a pull request

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- [Issues](https://github.com/yourusername/n8n-nodes-unlockpdf/issues)
- [n8n Community Forum](https://community.n8n.io/)
- [pdfmunk API Documentation](https://pdfmunk.com/docs)

## Changelog

### v2.0.0
- Initial release
- Support for password-protected PDF unlocking
- Multiple output format options
- Comprehensive error handling

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.
