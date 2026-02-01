# n8n Community Node: Markdown → DOCX

Convert Markdown text into a DOCX file inside your n8n workflows. This node uses `@mohtasham/md-to-docx` to generate a `.docx` and outputs it as binary data. No Pandoc or custom builds required.

- **Purpose**: Turn Markdown content from incoming items into a Word document with customizable formatting
- **Input sources**: JSON field (string) or Binary text file
- **Output**: Binary `.docx` on a configurable property
- **Document types**: Standard documents or report-style formatting
- **Advanced formatting**: Font sizes, alignment, spacing, and RTL text support

Powered by `@mohtasham/md-to-docx` ([repo](https://github.com/MohtashamMurshid/md-to-docx)).

## Installation

Follow n8n’s Community Nodes installation guide:
- In n8n: Settings → Community Nodes → Install
- Search for this package (or install from your local build while developing)
- Docs: https://docs.n8n.io/integrations/community-nodes/installation/

If developing locally, run:
```
npm install
n8n-node build
n8n-node dev
```
This will launch an instance of N8N, where you can test out the node locally.

## Node: Markdown to DOCX

- **Display name**: Markdown to DOCX
- **Name**: mdToDocx
- **Group**: transform
- **Version**: 1.0.2

### Parameters

- **Markdown Source** (options)
  - From Field: read Markdown from a JSON field
  - From Binary (Text File): read Markdown from an incoming binary property
- **Markdown Field** (string, required when source = From Field)
  - Name of the JSON field containing the Markdown string (default: `markdown`)
- **Binary Property** (string, required when source = From Binary)
  - Binary property name that holds a text/markdown file (default: `data`)
- **Filename** (string, required)
  - Output filename for the generated docx (default: `document.docx`)
- **Output Binary Property** (string, required)
  - Binary property to store the generated docx (default: `data`)
- **Document Type** (options)
  - Document: Standard document format
  - Report: Report-style document format
- **Advanced Options** (collection, optional)
  - **Title Size** (number): Font size for document title in half-points (default: 48 = 24pt)
  - **Heading 1 Size** (number): Font size for H1 headings in half-points (default: 48 = 24pt)
  - **Heading 2 Size** (number): Font size for H2 headings in half-points (default: 36 = 18pt)
  - **Paragraph Size** (number): Font size for paragraphs in half-points (default: 24 = 12pt)
  - **Paragraph Alignment** (options): Text alignment - Left, Right, Center, or Justified (default: Left)
  - **Line Spacing** (number): Line spacing multiplier (default: 1.15)
  - **Heading Spacing** (number): Spacing before/after headings (default: 240)
  - **Paragraph Spacing** (number): Spacing before/after paragraphs (default: 240)
  - **Text Direction** (options): Left to Right (LTR) or Right to Left (RTL) for international text support (default: LTR)

### Inputs

- Main (JSON and/or Binary)
  - Provide Markdown via the configured source

### Outputs

- Main (JSON + Binary)
  - Adds a binary property (as configured in "Output Binary Property") containing the generated DOCX
  - MIME type: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`

## Usage Examples

### Example 1: Markdown from JSON field

1. Add a Set node that outputs a field `markdown` with your Markdown content, for example:
   - `# Title\n\nSome paragraph with **bold**.`
2. Add the “Markdown to DOCX” node:
   - Markdown Source: From Field
   - Markdown Field: `markdown`
   - Filename: `my-doc.docx`
   - Output Binary Property: `file`
3. Add a node that can handle binary output (e.g. “Write Binary File” or any downstream consumer).

### Example 2: Markdown from Binary

1. Ingest a text/markdown file as binary (e.g. via HTTP Request → Binary or Read Binary File)
2. Add the “Markdown to DOCX” node:
   - Markdown Source: From Binary (Text File)
   - Binary Property: `data` (or your binary key)
   - Filename: `converted.docx`
   - Output Binary Property: `docx`

### Example 3: Custom Formatting

1. Add a Set node with Markdown content
2. Add the "Markdown to DOCX" node:
   - Markdown Source: From Field
   - Markdown Field: `markdown`
   - Document Type: Report
   - Filename: `styled-report.docx`
   - Advanced Options:
     - Title Size: 56 (28pt)
     - Paragraph Size: 22 (11pt)
     - Paragraph Alignment: Justified
     - Line Spacing: 1.5
     - Text Direction: RTL (for Arabic/Hebrew content)

## Compatibility

- Node.js: >= 20
- n8n Nodes API: 1

## Resources

- n8n Community Nodes docs: https://docs.n8n.io/integrations/#community-nodes
- md-to-docx: https://github.com/MohtashamMurshid/md-to-docx

## Maintainer

GitHub: [@elabbarw](https://github.com/elabbarw)

## Disclaimer

This project is provided as-is. The maintainer does not take responsibility for supporting this node or for any outputs or consequences resulting from its use.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
