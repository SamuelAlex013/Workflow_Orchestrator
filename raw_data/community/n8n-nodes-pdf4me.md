# n8n-nodes-pdf4me

This is an n8n community node that enables you to integrate PDF4ME's powerful PDF processing capabilities into your n8n workflows. PDF4ME is a comprehensive PDF processing API that allows you to convert, generate barcodes, process images, and manipulate documents programmatically.

n8n is a fair-code licensed workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Usage](#usage)
- [Resources](#resources)
- [Version History](#version-history)

## Installation

### Community Nodes (Recommended)

For users on n8n v0.187+, you can install this node directly from the n8n Community Nodes panel in the n8n editor:

1. Open your n8n editor
2. Go to **Settings > Community Nodes**
3. Search for "n8n-nodes-pdf4me"
4. Click **Install**
5. Reload the editor

### Global Installation (Recommended)

For global installation that makes the node available across all n8n projects:

```bash
# Install globally
npm install -g n8n-nodes-pdf4me

# Restart n8n to load the new node
n8n start
```

### Manual Installation

You can also install this node manually in a specific n8n project:

1. Navigate to your n8n installation directory
2. Run the following command:
   ```bash
   npm install n8n-nodes-pdf4me
   ```
3. Restart your n8n server

For Docker-based deployments, add the package to your package.json and rebuild the image:

```json
{
  "name": "n8n-custom",
  "version": "0.9.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "n8n"
  },
  "dependencies": {
    "n8n": "^1.0.0",
    "n8n-nodes-pdf4me": "^1.5.1"
  }
}
```

## What's New in Version 1.5.1

Version 1.5.1 brings stability improvements and code optimizations to the PDF4ME n8n node:

- **🔧 Code Refactoring**: Improved variable declarations and code structure
- **🖼️ Image Processing**: Enhanced MIME type handling for image operations
- **📝 Markdown Conversion**: Optimized Markdown to PDF conversion process
- **🔍 Resource Extraction**: Improved resource extraction functionality
- **✅ Stability**: Enhanced overall stability and performance
- **🔄 Backward Compatible**: All existing workflows continue to work seamlessly

## Operations

This node provides comprehensive document processing capabilities through PDF4ME's API. Here are the available features:

### 1. AI-Powered Document Processing
- **AI-Invoice Parser**: Extract structured data from invoices using AI/ML technology for automated data entry
- **AI-Process HealthCard**: Extract structured data from health cards using AI/ML technology for member management
- **AI-Process Contract**: Extract structured data from contracts using AI/ML technology for legal document analysis
- **Classify Document**: Classify documents using AI to determine document type and extract relevant information
- **Parse Document**: Parse documents to extract structured data using template-based parsing

### 2. PDF Processing & Manipulation
- **Add Attachment to PDF**: Attach files to PDF documents
- **Add Form Fields to PDF**: Add interactive form fields to PDF documents
- **Add HTML Header Footer**: Add custom HTML headers and footers to PDFs
- **Add Image Stamp to PDF**: Add image stamps with positioning and opacity controls
- **Add Margin to PDF**: Add margins to PDF documents
- **Add Page Number to PDF**: Add page numbers to PDF documents
- **Add Text Stamp to PDF**: Add text stamps with customizable formatting
- **Compress PDF**: Optimize PDF files for web, print, or screen viewing
- **Convert from PDF**: Convert PDFs to Word or Excel with OCR support
- **Convert PDF to Editable OCR**: Convert PDFs to editable text using OCR
- **Convert PDF to Excel**: Convert PDF tables to Excel spreadsheets
- **Convert PDF to PowerPoint**: Convert PDF content to PowerPoint presentations
- **Convert PDF to Word**: Convert PDFs to editable Word documents
- **Create Images from PDF**: Extract images from PDF documents
- **Delete Blank Pages from PDF**: Remove blank pages from PDF documents
- **Delete Unwanted Pages from PDF**: Remove specific pages from PDF documents
- **Extract Pages**: Extract specific pages from PDF documents
- **Extract Pages from PDF**: Extract pages with advanced options
- **Fill PDF Form**: Fill interactive PDF forms with data
- **Find and Replace Text**: Find and replace text in PDF documents
- **Flatten PDF**: Convert interactive PDF elements into static, non-editable content
- **Linearize PDF**: Optimize PDFs for web viewing with faster loading and progressive display
- **Merge Multiple PDFs**: Combine multiple PDF files into one
- **Overlay PDFs**: Overlay one PDF on top of another
- **Protect Document**: Add password protection and encryption to PDFs
- **Repair PDF Document**: Fix corrupted or damaged PDF files
- **Rotate Document**: Rotate entire PDF documents
- **Rotate Page**: Rotate specific pages within a PDF
- **Sign PDF**: Add digital signatures to PDF documents
- **Split PDF by Barcode**: Split PDFs based on barcode detection
- **Split PDF by Swiss QR**: Split PDFs based on Swiss QR code detection
- **Split PDF by Text**: Split PDFs based on text content
- **Split PDF Regular**: Split PDFs into equal parts or by page ranges
- **Unlock PDF**: Remove password protection from PDFs
- **Update Hyperlinks Annotation**: Modify hyperlinks and annotations in PDFs

### 3. Image Processing
- **Add Image Watermark to Image**: Add watermarks to images
- **Add Text Watermark to Image**: Add text watermarks to images
- **Compress Image**: Reduce image file sizes while maintaining quality
- **Convert Image Format**: Convert images between different formats (JPEG, PNG, etc.)
- **Crop Image**: Crop images with border or rectangle options
- **Flip Image**: Flip images horizontally, vertically, or both
- **Get Image Metadata**: Extract metadata from image files
- **Image Extract Text**: Extract text from images using OCR
- **Read Barcode from Image**: Read barcodes from images
- **Remove EXIF Tags from Image**: Remove metadata from images
- **Replace Text with Image**: Replace text in documents with images
- **Replace Text with Image in Word**: Replace text in Word documents with images
- **Resize Image**: Resize images to specific dimensions
- **Rotate Image**: Rotate images by specific angles
- **Rotate Image by EXIF Data**: Auto-rotate images based on EXIF orientation

### 4. Document Conversion
- **Convert to PDF**: Convert various document formats to PDF
- **Convert HTML to PDF**: Convert HTML content to PDF with multiple input options (Binary Data, Base64, HTML Code, URL)
- **Convert Image Format**: Convert images between different formats
- **Convert Markdown to PDF**: Convert Markdown files to PDF
- **Convert Visio**: Convert Visio diagrams to PDF
- **Convert Word to PDF Form**: Convert Word documents to PDF forms
- **JSON to Excel**: Convert JSON data to Excel spreadsheets
- **URL to PDF**: Convert web pages to PDF

### 5. Barcode Operations
- **Barcode Generator**: Generate various types of barcodes (QR, Code 128, EAN, UPC, etc.)
- **Read Barcode from Image**: Extract barcode data from images
- **Read Barcode from PDF**: Extract barcode data from PDF documents
- **Read Swiss QR Code**: Read Swiss QR codes from documents

### 6. Document Analysis & Extraction
- **Extract Attachment from PDF**: Extract attached files from PDFs
- **Extract Form Data from PDF**: Extract form field data from PDFs
- **Extract Pages from PDF**: Extract specific pages from PDFs
- **Extract Resources**: Extract resources from documents
- **Extract Table from PDF**: Extract tables from PDF documents
- **Extract Text by Expression**: Extract text using custom expressions
- **Extract Text from Word**: Extract text from Word documents
- **Get Document from PDF4ME**: Retrieve documents from PDF4ME storage
- **Get PDF Metadata**: Extract metadata from PDF files

### 7. Document Management & Generation
- **Create PDF/A**: Create PDF/A compliant documents
- **Create Swiss QR Bill**: Create Swiss QR Bills using all compliance standards for digital payment transactions
- **Disable Tracking Changes in Word**: Remove tracking changes from Word documents
- **Enable Tracking Changes in Word**: Enable tracking changes in Word documents
- **Generate Document Single**: Generate single documents from templates
- **Generate Documents Multiple**: Generate multiple documents from templates
- **Get Tracking Changes in Word**: Get tracking changes status from Word documents
- **Upload File to PDF4ME**: Upload files to PDF4ME for further processing

### 8. Advanced Features
- **Create Images from PDF**: Extract and process images from PDF documents
- **Document Processing**: Advanced document manipulation and processing

## Credentials

To use this node, you need a PDF4ME API key. Here's how to get started:

1. Sign up for a PDF4ME account at [PDF4ME Developer Portal](https://dev.pdf4me.com/)
2. Navigate to your dashboard and obtain your API key
3. In n8n, add your PDF4ME credentials by providing your API key

## Usage

This node allows you to automate document processing tasks in your n8n workflows. With version 1.5.1, the interface has been optimized for better performance and stability. Here are some common use cases:

### AI-Powered Document Processing
- Automatically extract invoice data for accounting systems
- Process health cards for member management systems
- Analyze contracts for legal document review
- Classify documents for automated routing and processing
- Parse structured data from various document types using templates

### Document Processing
- Convert PDF documents to editable Word format with OCR support
- Process complex PDFs with enhanced timeout handling (up to 25 minutes)
- Extract text from PDF documents for data processing
- Convert various document formats to PDF
- Extract specific pages from PDF documents for creating shorter versions or digital booklets
- Add watermarks, stamps, and annotations to documents
- Compress and optimize PDF files for different use cases
- Fill interactive PDF forms with data from your workflows
- Split PDFs based on content, barcodes, or page ranges

### Barcode Operations
- Generate QR codes for product tracking
- Create product barcodes (EAN-13, UPC-A) for inventory management
- Generate barcodes for document identification
- Embed barcodes in documents and reports
- Read barcodes from images and PDFs for automated processing
- Process Swiss QR codes for payment transactions

### Web Content Processing
- Convert web pages to PDF for archiving
- Automatically convert HTML reports to PDF
- **Write HTML code directly and convert to PDF** - No need to save HTML files first
- Capture web-based dashboards and reports
- Convert protected web content with authentication

### HTML to PDF Conversion Options
The Convert HTML to PDF operation supports multiple input methods for maximum flexibility:
- **Binary Data**: Use HTML files from previous workflow nodes
- **Base64 String**: Provide HTML content as base64 encoded strings
- **HTML Code**: Write HTML code directly in the interface (automatically converted to base64)
- **URL**: Convert HTML content from web URLs

**Example Use Cases for HTML Code Input:**
- **Dynamic Reports**: Generate PDFs from HTML templates with real-time data
- **Email Templates**: Convert HTML email content to PDF for archiving
- **Custom Dashboards**: Create PDF versions of HTML dashboards
- **Document Generation**: Build PDFs from HTML snippets without file management
- **Rapid Prototyping**: Quickly test HTML layouts by converting to PDF

### Data Export and Reporting
- Convert JSON data to Excel spreadsheets
- Transform API responses to formatted reports
- Export analytics data to Excel for stakeholder reports
- Create automated data processing pipelines
- Generate documents from templates with dynamic data

### Image Processing
- Crop images for specific dimensions
- Remove borders from scanned documents
- Process product images for e-commerce
- Create thumbnails and optimized images
- Add watermarks to images for branding
- Extract text from images using OCR
- Convert images between different formats

### Swiss QR Bill Generation
- Create compliant Swiss QR Bills for digital payment transactions
- Generate QR codes with all required payment information
- Support for multiple languages (English, German, French, Italian)
- Include creditor and debtor information with structured addresses
- Add billing information and unstructured messages
- Generate bills with different separator line styles
- Support for various reference types (QR Reference, Creditor Reference, No Reference)

### Document Generation & Management
- Generate documents from templates with dynamic data
- Create PDF/A compliant documents for long-term archiving
- Manage Word document tracking changes
- Process multiple documents in batch operations
- Extract and manage document metadata

### Automated Workflows
- Chain multiple PDF4ME operations together with simplified configuration
- Integrate with email nodes for automated document distribution
- Connect with storage services for file management
- Build complete document processing pipelines with enhanced reliability
- Automate document classification and routing
- Create end-to-end document workflows with improved error handling
- **Version 1.5.1**: Enhanced stability and performance for reliable workflow execution

For detailed examples and workflow templates, visit our documentation.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [PDF4ME API Documentation](https://dev.pdf4me.com/apiv2/documentation/)
- [PDF4ME Developer Portal](https://dev.pdf4me.com/)
- [PDF4ME Support](mailto:support@pdf4me.com)
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [Publishing Guide](PUBLISHING_GUIDE.md)

## Version History

### 1.5.1
- **Latest Version**: Stability improvements and code optimizations
- **Code Refactoring**: Improved variable declarations and code structure across actions
- **Image Processing**: Enhanced MIME type handling for image operations in extractResources
- **Markdown Conversion**: Optimized convertMarkdownToPdf functionality
- **Resource Extraction**: Improved resource extraction with better error handling
- **Performance**: Enhanced overall stability and processing speed
- **Maintained Compatibility**: All existing workflows continue to work seamlessly

### 1.5.0
- **Previous Version**: Major refactoring and enhanced user experience
- **Simplified Output Handling**: Removed complex binaryDataName parameters across all actions
- **Enhanced Response Processing**: Improved response handling to return raw data and metadata consistently
- **Streamlined Interface**: Simplified action configurations for better usability
- **Improved Descriptions**: Enhanced action descriptions for clarity and consistency
- **Better Error Handling**: Refined error handling and response processing
- **Code Optimization**: Significant code cleanup and optimization across all actions
- **Maintained Compatibility**: All existing workflows continue to work seamlessly
- **Enhanced Performance**: Improved processing speed and reliability

### 1.3.5
- **Previous Version**: Enhanced HTML to PDF conversion with direct HTML code input
- Added **HTML Code** input option for Convert HTML to PDF operation
- Users can now write HTML code directly in the interface without saving files first
- HTML code is automatically converted to base64 for API processing
- Enhanced input flexibility with 4 input methods: Binary Data, Base64, HTML Code, and URL
- Improved user experience for developers and content creators
- Maintains backward compatibility with existing workflows

### 1.3.0
- **Previous Version**: AI-powered document processing and enhanced features
- Added AI-Invoice Parser for automated invoice data extraction
- Added AI-Process HealthCard for health card data processing
- Added AI-Process Contract for contract analysis
- Added Classify Document for AI-powered document classification
- Added Parse Document for template-based document parsing
- Added Linearize PDF for web-optimized PDFs
- Added Flatten PDF for converting interactive elements to static content
- Enhanced error handling and response processing
- Improved support for JSON responses in AI processing operations
- Updated Node.js engine requirement to >=20.15
- Enhanced build and validation scripts

### 1.1.1
- **Previous Version**: Maintenance and dependency updates
- Updated dependencies for improved compatibility and security
- Minor bug fixes and codebase improvements
- Improved build and validation scripts for publishing
- **Note:** This version failed the n8n community package security scan due to an ESLint violation: use of restricted global 'setTimeout' is not allowed (see scan results for details).

### 1.1.0
- **Previous Version**: Security and compliance updates
- Updated to address n8n community package security scan results
- Added guidance for ESLint compliance and restricted imports
- Updated dependencies in package.json
- Improved documentation and publishing guides
- Minor bug fixes and codebase cleanup

### 1.0.0
- Production-ready release with comprehensive document processing capabilities
- 60+ document processing operations covering all major use cases
- Full integration with PDF4ME API services
- Complete PDF processing suite including conversion, manipulation, and analysis
- Advanced image processing capabilities with watermarking, cropping, and format conversion
- Comprehensive barcode generation and reading functionality
- Document conversion between multiple formats (PDF, Word, Excel, PowerPoint, HTML, etc.)
- Enhanced timeout handling for complex operations (up to 25 minutes)
- Improved async processing with exponential backoff and better error handling
- Support for multiple input types (Binary Data, Base64, URL, File Path)
- Advanced OCR capabilities with multi-language support
- Document protection, signing, and security features
- Metadata extraction and document analysis tools
- Swiss QR Bill generation with full compliance standards
- Document template generation and batch processing
- All critical lint errors resolved for production readiness
- Optimized package structure and build validation
- Enhanced error handling and debugging capabilities

### 0.9.0
- Comprehensive document processing capabilities with 50+ actions
- Full integration with PDF4ME API services
- Complete PDF processing suite including conversion, manipulation, and analysis
- Advanced image processing capabilities with watermarking, cropping, and format conversion
- Comprehensive barcode generation and reading functionality
- Document conversion between multiple formats (PDF, Word, Excel, HTML, etc.)
- Enhanced timeout handling for complex operations (up to 25 minutes)
- Improved async processing with exponential backoff and better error handling
- Support for multiple input types (Binary Data, Base64, URL, File Path)
- Advanced OCR capabilities with multi-language support
- Document protection, signing, and security features
- Metadata extraction and document analysis tools
- All critical lint errors resolved for production readiness
- Optimized package structure and build validation

### 0.8.0
- Comprehensive document processing capabilities
- Full integration with PDF4ME API services
- Support for barcode generation, URL to PDF conversion, PDF to Word conversion, JSON to Excel conversion, image cropping, and PDF page extraction
- Enhanced timeout handling for complex PDF to Word conversions (up to 25 minutes)
- Improved async processing with exponential backoff and better error handling
- Support for multiple input types (Binary Data, Base64, URL, File Path)
- Advanced OCR capabilities with multi-language support
- Comprehensive barcode generation with 100+ supported formats
- PDF page extraction for creating shorter versions and digital booklets
- Standardized API documentation URLs across all files
- Global installation support for cross-project availability

### 0.1.9
- Fixed package structure and build validation
- Improved error handling and debugging capabilities

### 0.1.3
- Added global installation support
- Enhanced package configuration for npm publishing

### 0.1.2
- Initial release with core functionality
