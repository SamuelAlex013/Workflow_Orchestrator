# n8n-nodes-ocrspace

An n8n community node for extracting text from images using the [OCR.space](https://ocr.space) API.

## Features

- **Text Extraction**: Extract text from images in various formats (PNG, JPG, GIF, TIF, BMP, PDF)
- **Multiple Languages**: Support for 25+ languages including English, Spanish, French, German, Chinese, Arabic, and more
- **Flexible Input**: Process images from any binary field in your n8n workflow
- **Advanced Options**: 
  - Choose between OCR engines for optimal accuracy
  - Auto-detect image orientation
  - Extract word-level coordinates
  - Image scaling for better recognition

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-ocrspace
```

## Credentials

You need an OCR.space API key to use this node:

1. Sign up at [OCR.space](https://ocr.space/ocrapi)
2. Get your free API key (25,000 requests/month)
3. In n8n, create new "OCR.space API" credentials with your API key

## Node Configuration

### Required Parameters
- **Binary Property**: Name of the binary field containing the image (default: "data")

### Optional Parameters
- **Language**: OCR language (default: English)
- **OCR Engine**: Choose Engine 1 (default) or Engine 2
- **Additional Options**:
  - Detect Orientation: Auto-rotate images
  - Get Word Coordinates: Return bounding boxes for each word
  - Scale Image: Improve accuracy for small text

## Usage Example

1. Use a "HTTP Request" node to download an image
2. Connect to the "OCR.space" node
3. Configure the binary property name (usually "data")
4. Select your preferred language and options
5. The extracted text will be available in `extractedText` field

## Output

The node returns:
- `extractedText`: The extracted text content
- `ocrResults`: Additional metadata including processing time, orientation, and confidence scores
- `wordCoordinates`: Word-level bounding boxes (if enabled)

## Supported Image Formats

- PNG, JPG, GIF, TIF, BMP
- PDF (up to 3 pages on free tier)
- Maximum file size: 1MB

## Rate Limits

- Free tier: 25,000 requests per month
- Rate limit: 500 requests per day per IP address

## License

[MIT](LICENSE.md)
