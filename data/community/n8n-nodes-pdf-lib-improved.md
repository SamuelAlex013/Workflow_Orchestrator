# n8n-nodes-pdf-lib

This is an n8n community node package. It lets you use PDF utilities in your n8n workflows.

PDF utilities for n8n allow you to extract information from PDF files and split PDFs into smaller documents, all within your workflow automation.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Credits](#credits)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This package provides the following node:

- **PDF-LIB**: A unified node that allows you to choose between different PDF operations:
  - **Get PDF Info**: Extracts comprehensive information from a PDF file including metadata, technical details, and page analysis
  - **Split PDF**: Splits a PDF into smaller documents with three modes:
    - **By Chunk Size**: Splits into chunks of a specified number of pages (default 1)
    - **By Page Ranges**: Splits based on specific page ranges (e.g., "1-3,5,7-10")
    - **Custom Documents**: Create multiple documents with specific page selections (mixed pages)
  - **Extract Images**: Converts PDF pages to images in PNG, JPEG, or WebP formats with customizable resolution and quality

## Compatibility

- Requires n8n v1.0.0 or higher.
- Developed and tested with Node.js 20+.
- Uses the [pdf-lib](https://pdf-lib.js.org/) library for PDF processing.

## Usage

- **PDF-LIB**: Use this unified node to perform different PDF operations. Select the operation from the dropdown:
  - **Get PDF Info**: Extract comprehensive information from a PDF file. Pass the PDF as a binary property (default: `data`).
- **Split PDF**: Split a PDF into smaller documents using one of three methods:
  - **By Chunk Size**: Enter a number to split the PDF into chunks of that many pages each
  - **By Page Ranges**: Enter specific page ranges in text format (e.g., "1-3,5,7-10") to create custom splits
  - **Custom Documents**: Create multiple named documents with specific page selections (perfect for mixed pages)
  - All split modes share the **Include Original Name in Output** toggle, letting you decide whether the original PDF name is prefixed to each generated file.
- **Extract Images**: Convert PDF pages to high-quality images:
  - **Output Format**: Choose PNG (lossless), JPEG (lossy), or WebP (modern)
  - **Page Selection**: Extract all pages or specify page ranges (e.g., "1-3,5,7-10")
  - **DPI**: Set resolution from 72 to 600 DPI (default 150)
  - **Image Quality**: For JPEG format, set quality 1-100 (default 90)
  - **Output Mode**: Choose between binary files (traditional) or JSON with base64 encoded images

### Get PDF Info - Detailed Output

The **Get PDF Info** operation extracts comprehensive information from PDF files and returns a structured JSON object with the following data:

#### Basic Information

- `pageCount`: Total number of pages in the PDF
- `fileName`: Name of the PDF file
- `fileSizeBytes`: File size in bytes
- `fileSizeMB`: File size in megabytes (rounded to 2 decimals)

#### Metadata

- `title`: Document title (if set)
- `author`: Document author (if set)
- `subject`: Document subject (if set)
- `creator`: Application that created the PDF (if set)
- `producer`: Application that produced the PDF (if set)
- `keywords`: Document keywords (if set)
- `creationDate`: When the document was created (ISO 8601 format)
- `modificationDate`: When the document was last modified (ISO 8601 format)

#### Technical Information

- `version`: PDF version (e.g., "1.4", "1.7")
- `isEncrypted`: Whether the PDF is password-protected
- `embeddedFonts`: Number of embedded fonts
- `hasImages`: Whether the PDF contains images
- `hasAnnotations`: Whether the PDF contains annotations/comments
- `hasAcroForm`: Whether the PDF contains interactive forms

#### Page Statistics

- `totalPages`: Total number of pages
- `landscapePages`: Number of pages in landscape orientation
- `portraitPages`: Number of pages in portrait orientation
- `rotatedPages`: Number of pages with non-zero rotation
- `hasUniformSize`: Whether all pages have the same dimensions
- `uniqueSizes`: Array of unique page sizes found in the document

#### Detailed Page Information

- `pageDetails`: Array with detailed information for each page:
  - `pageNumber`: Page number (1-indexed)
  - `width`: Page width in points
  - `height`: Page height in points
  - `orientation`: "portrait" or "landscape"
  - `rotation`: Rotation angle in degrees (0, 90, 180, or 270)

### Split PDF Page Ranges Format

When using the "By Page Ranges" option, you can specify pages using this format:

- Single pages: `5` (extracts page 5)
- Page ranges: `1-3` (extracts pages 1, 2, and 3)
- Multiple selections: `1-3,5,7-10` (extracts pages 1-3, page 5, and pages 7-10)
- Spaces are ignored: `1-3, 5, 7-10` works the same as `1-3,5,7-10`

File names are generated automatically from the range descriptor. They are sanitised (spaces and special characters become underscores) and, if **Include Original Name in Output** is enabled, the original file name is prefixed. Duplicate names are suffixed with `_2`, `_3`, etc.

### Custom Documents - Mixed Page Selection (JSON powered)

The **Custom Documents** mode lets you submit a JSON array describing the output documents you want to build. Each entry can mix ranges and single pages, keep the order you provide, and even reuse the same page in multiple outputs. This makes it ideal when the source PDF contains interleaved content that must be regrouped.

#### Use Cases

- **Mixed document separation**: Extract alternating pages (e.g., pages 1,3,5 to one document and pages 2,4,6 to another)
- **Thematic grouping**: Combine non-consecutive pages into logical documents
- **Custom reorganization**: Create new document structures from existing PDFs

#### Configuration

Provide a JSON array where each object looks like:

```json
{
	"pdf_name": "Document_1",
	"pages": "3-5,1,6,2"
}
```

Key details:

- `pdf_name` becomes the base label for the generated file (after sanitising invalid characters).
- `pages` is a comma-separated string; ranges (`1-3`) and single pages (`5`) can be freely combined (`3-5,1,6,2`).
- Page order is preserved exactly as provided and duplicates are allowed.
- Pages may be reused across different objects in the array.
- The JSON editor in the node helps validate the format while you edit.

You can also control the naming of the resulting files with the **Include Original Name in Output** toggle. When enabled (default), the original PDF name is prefixed to each generated file. If multiple outputs resolve to the same name, an automatic numeric suffix (`_2`, `_3`, …) is appended to avoid overwriting.

#### Examples

**Example 1: Separate odd and even pages**

```json
[
	{ "pdf_name": "Odd_Pages", "pages": "1,3,5,7,9" },
	{ "pdf_name": "Even_Pages", "pages": "2,4,6,8,10" }
]
```

Result (default naming): `source_Odd_Pages.pdf` and `source_Even_Pages.pdf`

**Example 2: Create thematic sections**

```json
[
	{ "pdf_name": "Introduction", "pages": "1-3" },
	{ "pdf_name": "Main_Content", "pages": "4,7,9-12,15" },
	{ "pdf_name": "Appendix", "pages": "5-6,8,13-14" }
]
```

Result: `report_Introduction.pdf`, `report_Main_Content.pdf`, `report_Appendix.pdf`

**Example 3: Reorder pages deliberately**

```json
[
	{ "pdf_name": "Form_Pages", "pages": "1,4,7" },
	{ "pdf_name": "Supporting_Docs", "pages": "2,5" },
	{ "pdf_name": "Terms", "pages": "3-5,1,6,2" }
]
```

Here the third document intentionally reorders and repeats pages.

#### Output Information

When using Custom Documents mode, the JSON output includes additional information:

- `includeOriginalName`: Whether the generated files used the original name as a prefix
- `documents`: Array with details for each created document:
  - `pdf_name`: Name you provided in the JSON definition
  - `pageCount`: Number of pages in the document
  - `pages`: Array of page numbers included (in the exact order they were copied)
  - `pageSelection`: String representation of the selection (spaces removed)
  - `fileName`: Final file name that was produced (already deduplicated and sanitised)

The generated binary data also uses the deduplicated `fileName` values so you always know which PDF is which.

### Extract Images - Convert Pages to Images

The **Extract Images** operation converts PDF pages to high-quality images using the [pdftoimg-js](https://github.com/iqbal-rashed/pdftoimg-js) library. This is useful for creating previews, thumbnails, or image-based workflows.

#### Configuration Options

- **Output Format**: Choose from PNG (lossless), JPEG (lossy), or WebP (modern format)
- **Page Selection**:
  - **All Pages**: Extract every page from the PDF
  - **Page Ranges**: Extract specific pages using range notation (e.g., "1-3,5,7-10")
- **DPI (Resolution)**: Set output resolution from 72 to 600 DPI (default 150)
- **Image Quality**: For JPEG format only, set quality from 1-100 (default 90)
- **Output Mode**: Choose how the extracted images are returned:
  - **Binary Files**: Traditional n8n format with separate binary properties (`image_0`, `image_1`, etc.)
  - **JSON with Base64**: All images embedded in JSON as data URLs with metadata

#### Output

The operation returns different formats based on the **Output Mode**:

**Binary Files Mode (Default)**:
- **JSON data** with extraction metadata including format, DPI, pages extracted, and image count
- **Binary data** with each extracted image as a separate binary property (`image_0`, `image_1`, etc.)
- **Automatic naming**: Images are named using pattern `{original_name}_page_{num}.{format}` (e.g., `document_page_001.png`)

**JSON with Base64 Mode**:
- **JSON data** containing all extraction metadata plus an `images` array
- Each image in the array includes:
  - `pageNumber`: Source page number
  - `fileName`: Generated filename 
  - `mimeType`: Image MIME type
  - `base64`: Complete data URL (e.g., `data:image/png;base64,...`)
  - `sizeBytes`: Image file size in bytes

#### Use Cases

- Create image previews for PDF content
- Generate thumbnails for PDF galleries
- Extract specific pages as images for presentations
- Convert PDFs to image formats for image processing workflows

The node expects the PDF input as a binary property. You can use n8n's built-in nodes to fetch or generate PDF files before processing them with this node.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [pdf-lib documentation](https://pdf-lib.js.org/)

## Credits

This project is based on the original [n8n-nodes-pdf-lib](https://github.com/vvcent/n8n-nodes-pdf-lib) by Vincent Wong. This improved version adds enhanced functionality including page ranges support for PDF splitting operations.

## Version history

- 0.3.3 (unreleased):
  - Custom Documents input moved to JSON editor (`[{"pdf_name":"Doc","pages":"3-5,1,6"}]`)
  - Added `includeOriginalName` option and deterministic file name generation with automatic suffixes
  - Pages keep the exact order provided in JSON and may be reused across documents
- 0.3.2: **Added Custom Documents mode to Split PDF operation** with enhanced file naming and JSON output for document details.
- 0.3.0: **Major enhancement to Get PDF Info operation**. Now extracts comprehensive information including:
  - Complete metadata (title, author, subject, creator, producer, keywords, dates)
  - Technical details (PDF version, encryption status, embedded fonts, images, forms)
  - Page statistics (orientation counts, uniform sizing, rotation analysis)
  - Detailed per-page information (dimensions, orientation, rotation)
  - File size analysis
- 0.2.0: Added page ranges support to Split PDF operation. Now supports splitting by specific page ranges (e.g., "1-3,5,7-10") in addition to chunk size.
- 0.1.0: Initial release with GetPdfInfo and SplitPdf nodes.
