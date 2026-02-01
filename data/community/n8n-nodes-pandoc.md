# n8n-nodes-pandoc

This is a node for n8n that allows you to convert documents between different formats using Pandoc. It supports converting between various formats including Markdown, HTML, Microsoft Word (docx), LaTeX, and Plain Text.

# NOTICE

This is just a node that I needed for a project and thought I'd share. It is 95% ai generated, Written in a couple hours, so don't expect the world from it. It works for the workflow I needed it for ( to convert a docx to markdown ). It may get future updates, but I'm not promising anything.

## Prerequisites

- n8n installed
- Pandoc installed on the system

## Installation

1. In Community Nodes, install `@couleetech/n8n-nodes-pandoc`

2. **Important**: Pandoc must be installed on your system for this node to work.

### Docker Installation

If you're using n8n with Docker Compose, you'll need to modify your setup to include Pandoc. Here's how:

1. Create a `Dockerfile`:
   ```dockerfile
   FROM docker.n8n.io/n8nio/n8n

   USER root
   RUN apk add --no-cache pandoc

   USER node
   ```

2. Update your `docker-compose.yml`:
   ```yaml
   services:
     n8n:
       build: .
       # ... rest of your n8n configuration
   ```

   Instead of:
   ```yaml
   services:
     n8n:
       image: docker.n8n.io/n8nio/n8n
   ```

## Usage

The Pandoc Convert node provides the following functionality:

### Input Parameters

- **Binary Property**: Name of the binary property that contains the file to convert
- **From Format**: Input format of the document (markdown, html, docx, latex, plain)
- **To Format**: Output format for the conversion (markdown, html, docx, latex, plain)

### Supported Formats

- Markdown
- HTML
- Microsoft Word (docx)
- LaTeX
- Plain Text

### Example Workflow

1. Upload or input a document using nodes like HTTP Request, Read Binary File, etc.
2. Connect the output to the Pandoc Convert node
3. Configure the conversion parameters (from format and to format)
4. The node will output the converted document in the specified format

### Outputs

The node has two outputs:
1. Main output with the converted document
2. Secondary output for extracted images (if applicable)


## Support

For issues and feature requests, please [open an issue on GitHub](https://github.com/CouleeTechlinkInc/n8n-nodes-pandoc/issues). 