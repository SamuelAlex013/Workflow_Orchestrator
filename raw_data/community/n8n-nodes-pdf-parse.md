# N8N PDF Parse Node

A robust N8N community node for parsing PDF files and extracting text content with advanced configuration options.

## Features

- 🤖 **AI-Optimized Text Extraction**: Enhanced pdf-parse engine with superior AI-friendly formatting
- 🖼️ **PDF to Image Conversion**: High-quality PDF to PNG/JPEG conversion using pdf2pic with GraphicsMagick backend
- ✅ **Raw Mode (Default)**: Preserves all line breaks and document structure for optimal AI processing
- ✅ **Multiple Formatting Options**: Raw, Smart, Minimal, Structured, Visual, and Compact modes
- ✅ **Perfect for Document Analysis**: Purchase orders, invoices, forms, and tables maintain layout
- ✅ **Enhanced Line Break Preservation**: Keeps document structure intact for LLM processing
- ✅ **Dual Operations**: Text parsing and image conversion in one node
- ✅ **Multiple Input Sources**: Binary data and URL sources
- ✅ **Advanced Options**: Page ranges, DPI control, custom dimensions, format selection
- ✅ **Comprehensive Output**: Text, images, metadata, and statistics
- ✅ **Robust Error Handling**: Detailed validation and graceful failure handling
- ✅ **TypeScript**: Full type safety and IntelliSense support

## Installation

### System Requirements

For **PDF to Image conversion** operations, the following system dependencies are required:

#### Docker Environment (N8N Docker)

##### Option 1: Using docker-compose with custom Dockerfile (Recommended)

Create a `Dockerfile` in your project directory:

```dockerfile
FROM n8nio/n8n:latest
USER root
# Alpine-based image uses apk package manager
RUN apk update && apk add --no-cache \
    graphicsmagick \
    ghostscript
USER node
```

Create a `docker-compose.yml` file:

```yaml
services:
  n8n:
    build: .
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=http://localhost:5678/
      - GENERIC_TIMEZONE=America/New_York
      # Allow community nodes
      - NODE_FUNCTION_ALLOW_EXTERNAL=n8n-nodes-pdf-parse
    volumes:
      - n8n_data:/home/node/.n8n
      - ./custom-nodes:/home/node/.n8n/nodes
    networks:
      - n8n-network

volumes:
  n8n_data:

networks:
  n8n-network:
    driver: bridge
```

Then run:
```bash
docker-compose up -d
```

##### Option 2: Quick installation in running container (Temporary)

If you're already running n8n in Docker and need a quick fix:

```bash
# Access the container (replace 'n8n' with your container name)
docker exec -it --user root n8n /bin/sh

# Install dependencies
apk update && apk add --no-cache graphicsmagick ghostscript

# Exit container
exit
```

**Note:** This method is temporary - packages will be lost when the container restarts. Use Option 1 for a permanent solution.

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install graphicsmagick ghostscript
```

#### CentOS/RHEL/Fedora
```bash
sudo yum install GraphicsMagick ghostscript
# or for newer versions:
sudo dnf install GraphicsMagick ghostscript
```

#### macOS
```bash
brew install graphicsmagick ghostscript
```

#### Windows
Download and install:
- [GraphicsMagick](http://www.graphicsmagick.org/download.html)
- [Ghostscript](https://www.ghostscript.com/download/gsdnld.html)

### Node Installation for Self-Hosted n8n

#### For Docker-Based n8n (Most Common)

If you're running n8n with Docker, you need to install the node inside the container. Add this to your docker-compose.yml:

```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=http://localhost:5678/
      - GENERIC_TIMEZONE=America/New_York
    volumes:
      - n8n_data:/home/node/.n8n
      - ./custom-nodes:/home/node/.n8n/nodes
    command: >
      /bin/sh -c "
        npm install -g n8n-nodes-pdf-parse &&
        n8n start
      "
    networks:
      - n8n-network

volumes:
  n8n_data:

networks:
  n8n-network:
    driver: bridge
```

**Note:** For PDF to Image conversion to work, you'll also need GraphicsMagick and Ghostscript. See the "System Requirements" section above for Docker setup with these dependencies.

#### Option 1: Install via npm (For Non-Docker Installations)

```bash
npm install n8n-nodes-pdf-parse
```

#### Option 2: Manual Installation

1. Navigate to your N8N installation directory
2. Go to the `~/.n8n/custom` directory (create if it doesn't exist)
3. Clone or download this repository
4. Install dependencies and build:

```bash
cd n8n-nodes-pdf-parse
npm install
npm run build
```

#### Option 3: Global Installation

```bash
npm install -g n8n-nodes-pdf-parse
```

After installation, restart your N8N instance to load the new node.

## Configuration

### Environment Variables

For self-hosted N8N instances, you can set these environment variables:

```bash
# Allow community nodes
N8N_NODES_INCLUDE=["n8n-nodes-pdf-parse"]

# Or allow all community nodes
N8N_NODES_EXCLUDE=[]
```

## Usage

### Basic Usage

1. Add the "PDF Parse" node to your workflow
2. Connect it to a node that provides PDF data (e.g., HTTP Request, File Read)
3. Configure the source type (Binary Data or URL)
4. Set the binary property name or URL
5. Configure additional options as needed

### Node Parameters

#### Required Parameters

- **Operation**: Choose between "Parse PDF" or "Convert to Image"
- **PDF Source**: Choose between "Binary Data" or "URL"
- **Binary Property**: Name of the binary property containing the PDF (when using binary data)
- **URL**: URL of the PDF file to parse (when using URL source)

#### Optional Parameters

- **Output Property Name**: Property name to store the result (default: "result")
- **Max Pages**: Maximum number of pages to process (0 = all pages)
- **Page Range Start**: Starting page number (1-based)
- **Page Range End**: Ending page number (0 = last page)

#### Text Parsing Options (Parse PDF Operation)
- **Text Formatting**: Choose formatting style:
  - **Raw (Best for AI)**: Preserves all line breaks and document structure
  - **Smart Layout**: Intelligent layout preservation with enhanced spacing
  - **Visual Layout**: Universal layout preservation - replicates human text selection patterns
  - **Minimal Cleanup**: Removes extra spaces but keeps line breaks
  - **Structured**: Cleans formatting while preserving structure
  - **Compact**: Removes most whitespace for compact text
- **Include Metadata**: Include PDF metadata in output
- **Split by Pages**: Return text split by pages as an array
- **Version**: PDF.js version to use for parsing

#### Image Conversion Options (Convert to Image Operation)
- **Image Format**: Choose between PNG or JPEG output
  - **PNG**: Better quality, transparency support, larger files
  - **JPEG**: Smaller files, no transparency, good for photos
- **DPI (Resolution)**: 72-600 dots per inch (default: 150)
  - Higher DPI = better quality but larger files
  - 72 DPI = screen resolution, 300 DPI = print quality
- **Width**: Custom width in pixels (0 = auto based on DPI)
- **Height**: Custom height in pixels (0 = auto based on DPI) 
- **Preserve Aspect Ratio**: Maintain original proportions when resizing (default: true)

### Example Workflows

#### Example 1: Parse PDF from URL

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "parse",
        "source": "url",
        "url": "https://example.com/document.pdf",
        "outputProperty": "extractedText",
        "additionalOptions": {
          "normalizeWhitespace": true,
          "includeMetadata": true
        }
      },
      "name": "PDF Parse",
      "type": "n8n-nodes-pdf-parse.pdfParse"
    }
  ]
}
```

#### Example 2: Parse PDF from Binary Data

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "parse",
        "source": "binary",
        "binaryPropertyName": "data",
        "outputProperty": "pdfText",
        "additionalOptions": {
          "maxPages": 10,
          "splitByPages": true
        }
      },
      "name": "PDF Parse",
      "type": "n8n-nodes-pdf-parse.pdfParse"
    }
  ]
}
```

#### Example 3: Parse Specific Page Range

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "parse",
        "source": "binary",
        "binaryPropertyName": "document",
        "additionalOptions": {
          "pageRangeStart": 5,
          "pageRangeEnd": 15,
          "normalizeWhitespace": true
        }
      },
      "name": "PDF Parse",
      "type": "n8n-nodes-pdf-parse.pdfParse"
    }
  ]
}
```

## Output Format

### Standard Output

```json
{
  "text": "Extracted PDF text content...",
  "numPages": 25,
  "pdfStats": {
    "textLength": 15420,
    "wordCount": 2156,
    "pageCount": 25
  }
}
```

### With Metadata

```json
{
  "text": "Extracted PDF text content...",
  "numPages": 25,
  "pdfMetadata": {
    "numPages": 25,
    "info": {
      "Title": "Document Title",
      "Author": "Document Author",
      "Creator": "PDF Creator",
      "Producer": "PDF Producer",
      "CreationDate": "D:20231201120000Z",
      "ModDate": "D:20231201120000Z"
    },
    "metadata": "Additional metadata...",
    "version": "1.7"
  },
  "pdfStats": {
    "textLength": 15420,
    "wordCount": 2156,
    "pageCount": 25
  }
}
```

### Split by Pages

```json
{
  "text": [
    "Page 1 text content...",
    "Page 2 text content...",
    "Page 3 text content..."
  ],
  "numPages": 3,
  "pdfStats": {
    "textLength": 2340,
    "wordCount": 456,
    "pageCount": 3
  }
}
```

## Error Handling

The node includes comprehensive error handling:

- **Invalid PDF files**: Validates PDF magic number
- **Network errors**: Handles URL fetch failures
- **Empty files**: Detects and reports empty PDF files
- **Invalid URLs**: Validates URL format
- **Missing properties**: Validates required parameters

When "Continue on Fail" is enabled, errors are added to the output data:

```json
{
  "error": "Error message describing what went wrong"
}
```

## Supported PDF Features

- ✅ Text extraction from standard PDFs
- ✅ Multi-page documents
- ✅ Password-protected PDFs (basic support)
- ✅ Various PDF versions (1.0 - 2.0)
- ✅ Embedded fonts and text encoding
- ⚠️ OCR for scanned documents (not supported - text-based PDFs only)
- ⚠️ Complex layouts with tables/forms (basic support)

## Performance Considerations

- **Large PDFs**: Use page range options to limit processing
- **Memory usage**: Large PDFs may require more memory
- **Processing time**: Scales with document size and complexity
- **Network timeouts**: URLs should be accessible and responsive

## Dependencies

### Node.js Dependencies
- `pdf-parse`: Enhanced PDF parsing library with AI-optimized text extraction
- `pdfjs-dist`: Mozilla's PDF.js library for reliable PDF text parsing
- `pdf2pic`: Robust PDF to image conversion library
- `n8n-workflow`: N8N workflow types and utilities

### System Dependencies (Image Conversion Only)
- **GraphicsMagick**: High-performance image processing library
- **Ghostscript**: PostScript and PDF interpreter (required by GraphicsMagick for PDF handling)

**Note**: Text parsing operations require no system dependencies - only Node.js packages. Image conversion operations require GraphicsMagick and Ghostscript to be installed on the system.

## Development

### Setup

```bash
git clone https://github.com/ConniAU/n8n-pdf-parse.git
cd n8n-nodes-pdf-parse
npm install
```

### Build

```bash
npm run build
```

### Lint and Format

```bash
npm run lint
npm run format
```

### Test

```bash
npm test
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## Complete Docker Setup Example

For self-hosted n8n users who want both the PDF Parse node AND image conversion capabilities, here's a complete setup:

### Step 1: Create a Dockerfile

```dockerfile
FROM n8nio/n8n:latest

USER root

# Install system dependencies for PDF to Image conversion
RUN apk update && apk add --no-cache \
    graphicsmagick \
    ghostscript \
    nodejs \
    npm

# Install the PDF Parse node globally
RUN npm install -g n8n-nodes-pdf-parse

USER node
```

### Step 2: Create docker-compose.yml

```yaml
version: '3.8'

services:
  n8n:
    build: .
    container_name: n8n-with-pdf-parse
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      # Basic n8n configuration
      - N8N_HOST=${N8N_HOST:-localhost}
      - N8N_PORT=5678
      - N8N_PROTOCOL=${N8N_PROTOCOL:-http}
      - NODE_ENV=production
      - WEBHOOK_URL=${WEBHOOK_URL:-http://localhost:5678/}
      - GENERIC_TIMEZONE=${TIMEZONE:-America/New_York}
      
      # Database configuration (optional - uses SQLite by default)
      - DB_TYPE=sqlite
      # For PostgreSQL, uncomment and configure:
      # - DB_TYPE=postgresdb
      # - DB_POSTGRESDB_HOST=postgres
      # - DB_POSTGRESDB_PORT=5432
      # - DB_POSTGRESDB_DATABASE=${DB_POSTGRESDB_DATABASE:-n8n}
      # - DB_POSTGRESDB_USER=${DB_POSTGRESDB_USER:-n8n}
      # - DB_POSTGRESDB_PASSWORD=${DB_POSTGRESDB_PASSWORD:-n8n}
      
      # Security
      - N8N_BASIC_AUTH_ACTIVE=${N8N_BASIC_AUTH_ACTIVE:-false}
      - N8N_BASIC_AUTH_USER=${N8N_BASIC_AUTH_USER:-}
      - N8N_BASIC_AUTH_PASSWORD=${N8N_BASIC_AUTH_PASSWORD:-}
      
      # Allow external npm modules (required for community nodes)
      - NODE_FUNCTION_ALLOW_EXTERNAL=*
      - NODE_FUNCTION_ALLOW_BUILTIN=*
      
    volumes:
      # Persist n8n data
      - n8n_data:/home/node/.n8n
      # Optional: Mount local workflows directory
      # - ./workflows:/home/node/.n8n/workflows
      # Optional: Mount custom nodes directory
      # - ./custom-nodes:/home/node/.n8n/nodes
      
    networks:
      - n8n-network
    
    # Health check
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:5678/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  # Optional: PostgreSQL database for production use
  # postgres:
  #   image: postgres:14-alpine
  #   container_name: n8n-postgres
  #   restart: unless-stopped
  #   environment:
  #     - POSTGRES_USER=${DB_POSTGRESDB_USER:-n8n}
  #     - POSTGRES_PASSWORD=${DB_POSTGRESDB_PASSWORD:-n8n}
  #     - POSTGRES_DB=${DB_POSTGRESDB_DATABASE:-n8n}
  #   volumes:
  #     - postgres_data:/var/lib/postgresql/data
  #   networks:
  #     - n8n-network

volumes:
  n8n_data:
  # postgres_data:

networks:
  n8n-network:
    driver: bridge
```

### Step 3: Create .env file (optional)

```env
# n8n Configuration
N8N_HOST=localhost
N8N_PROTOCOL=http
WEBHOOK_URL=http://localhost:5678/
TIMEZONE=America/New_York

# Authentication (uncomment to enable)
# N8N_BASIC_AUTH_ACTIVE=true
# N8N_BASIC_AUTH_USER=admin
# N8N_BASIC_AUTH_PASSWORD=your-secure-password

# Database (for PostgreSQL)
# DB_POSTGRESDB_DATABASE=n8n
# DB_POSTGRESDB_USER=n8n
# DB_POSTGRESDB_PASSWORD=your-secure-password
```

### Step 4: Deploy

```bash
# Build and start the services
docker-compose up -d

# View logs
docker-compose logs -f n8n

# Stop services
docker-compose down

# Stop and remove volumes (caution: deletes all data)
docker-compose down -v
```

### Step 5: Access n8n

Open your browser and navigate to `http://localhost:5678`

The PDF Parse node should be available in the node selection panel under the "Transform" category.

## Troubleshooting

### Common Issues

1. **Node not appearing in N8N**
   - Ensure the package is properly installed
   - Restart N8N after installation
   - Check N8N logs for loading errors

2. **"Invalid PDF" errors**
   - Verify the file is actually a PDF
   - Check if the PDF is corrupted
   - Try with a different PDF file

3. **Image conversion errors (Missing system dependencies)**
   - **Error**: `Command failed: execvp failed, errno = 2 (No such file or directory) gm identify`
   - **Cause**: GraphicsMagick not installed
   - **Solution**: Install GraphicsMagick and Ghostscript (see System Requirements above)
   
   **Docker Environment**: Use custom Dockerfile with dependencies:
   ```dockerfile
   FROM n8nio/n8n:latest
   USER root
   RUN apt-get update && apt-get install -y graphicsmagick ghostscript
   USER node
   ```

4. **Memory issues with large PDFs**
   - Use page range options to limit processing
   - Increase Node.js memory limit: `--max-old-space-size=4096`

5. **Network timeout errors**
   - Check URL accessibility
   - Verify network connectivity
   - Consider downloading the file first

### Debug Mode

Enable debug logging by setting the environment variable:

```bash
N8N_LOG_LEVEL=debug
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Changelog

### Version 1.0.0
- Initial release
- PDF text extraction with pdf-parse
- Support for binary data and URL sources
- Advanced parsing options
- Comprehensive error handling
- TypeScript implementation

## Support

For issues, questions, or contributions:

- GitHub Issues: [https://github.com/ConniAU/n8n-pdf-parse/issues](https://github.com/ConniAU/n8n-pdf-parse/issues)
- N8N Community: [https://community.n8n.io](https://community.n8n.io)

## Acknowledgments

- Built with [pdf-parse](https://www.npmjs.com/package/pdf-parse)
- Designed for [N8N](https://n8n.io) workflow automation
- Inspired by the N8N community's needs for PDF processing