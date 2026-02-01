# n8n-nodes-media-decrypt

An n8n community node for decrypting WhatsApp media files with comprehensive error handling, proper MAC verification, and seamless integration with OpenAI for audio transcription.

![n8n-nodes-media-decrypt](https://img.shields.io/badge/n8n-community%20node-blue)
![Version](https://img.shields.io/badge/version-0.1.4-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## Installation

To install this community node in n8n, use one of the following methods:

### Method 1: Direct GitHub Installation
```bash
npm install https://github.com/Drishtech/n8n-nodes-media-decrypt
```

### Install from npm (when published)
```bash
npm install n8n-nodes-media-decrypt
```

## Features

- 🔓 **Decrypt WhatsApp media files** (images, videos, audio, documents)
- ✅ **Proper MAC verification** with multiple fallback methods for enhanced compatibility
- 🎯 **Dynamic MIME type dropdown** that changes based on message type selection
- 🤖 **OpenAI Integration Ready** - binary output compatible with OpenAI transcription
- 🛡️ **Comprehensive error handling** with detailed debugging information
- 🔄 **Retry logic** for downloads with exponential backoff
- 📊 **Support for large files** (up to 100MB)
- 🔍 **Enhanced input validation** with base64 media key verification

## Usage

### Basic Setup
1. **URL**: The direct download URL of the encrypted WhatsApp media file (usually ends with `.enc`)
2. **Media Key**: The base64-encoded media key from the WhatsApp message metadata
3. **Message Type**: Select the appropriate message type - this dynamically updates available MIME types
4. **MIME Type**: Select from context-aware dropdown that only shows relevant formats

### Integration with OpenAI
This node is designed to work seamlessly with OpenAI's audio transcription:

**WhatsApp Media Decrypt** → **OpenAI (Audio Transcribe)**

The binary output is automatically named with the generated filename, making it directly compatible with OpenAI's audio transcription service.

## Dynamic MIME Type Selection

The MIME Type dropdown is **context-aware** and dynamically updates based on your Message Type selection:

### 🎵 Audio Message
- **OGG (WhatsApp Voice Messages)** - Default for voice notes
- MP3, MP4/M4A, WAV, AAC

### 🖼️ Image Message  
- **JPEG** - Default for photos
- PNG, WebP, GIF

### 🎬 Video Message
- **MP4** - Default for videos
- WebM, AVI, MOV (QuickTime)

### 📄 Document Message
- **PDF** - Default for documents
- Word (.docx), Excel (.xlsx), PowerPoint (.pptx)
- ZIP, RAR archives
- Plain text, Binary/Unknown files

## What's New in v0.1.4

### 🤖 **OpenAI Integration Fix**
- **Fixed binary field naming** for seamless OpenAI compatibility
- Binary data now uses filename as key instead of generic 'data'
- **Direct compatibility** with OpenAI audio transcription workflows

### 🎯 **Enhanced Dynamic Dropdown**
- **Real-time MIME type filtering** based on message type selection
- **Improved user experience** with context-aware options
- **Better organization** of supported formats

### 🔧 **Improved Build Process**
- **Fixed compilation issues** that were preventing latest changes
- **Proper file structure** in dist folder
- **Consistent builds** across different environments

## What's Fixed in v0.1.4 (Previous Releases)

### 🔧 **MAC Verification Algorithm**
- **Complete rewrite** of the WhatsApp media decryption algorithm
- **Proper HKDF implementation** with empty 32-byte salt as per WhatsApp specification
- **Multiple MAC verification methods** with fallback support:
  - Primary: `HMAC-SHA256(macKey, iv + encrypted)` truncated to 10 bytes
  - Fallback: `HMAC-SHA256(macKey, encrypted)` for older formats
- **Enhanced debugging** with detailed error information

### 🛡️ **Enhanced Security & Validation**
- **Base64 media key validation** to catch encoding issues early
- **Comprehensive input validation** with specific error messages
- **URL truncation** in logs for security
- **No sensitive data logging**

### 🔄 **Download Reliability**
- **Retry logic** for failed downloads (up to 3 attempts with exponential backoff)
- **Increased timeout** to 60 seconds for large files
- **Support for files up to 100MB**
- **User-Agent header** for better compatibility with WhatsApp servers
- **Better error reporting** for network issues

## Troubleshooting

### MAC Verification Failed Error
If you encounter MAC verification errors, the enhanced v0.1.4 provides detailed debugging:

1. **Check the media key**: Ensure it's valid base64 and complete
   ```
   Error: Media Key must be valid base64 encoded string
   ```

2. **Verify message type**: Must match the actual WhatsApp message type
   ```
   Error: Invalid message type. Must be one of: audioMessage, imageMessage, videoMessage, documentMessage
   ```

3. **Check the URL**: Ensure it points to the actual encrypted file
   ```
   Error: Failed to download file after 3 attempts
   ```

4. **File integrity**: The download might be corrupted or incomplete
   ```
   Error: Downloaded file is too small (X bytes). WhatsApp encrypted files must be at least 10 bytes
   ```

The error message now includes comprehensive debug information:
- File sizes and key lengths
- Message type and encryption parameters
- Specific suggestions for resolution

### OpenAI Integration Issues

**Problem**: `The item has no binary field 'filename.ext'`

**Solution**: Ensure you're using v0.1.4+ which fixes binary field naming for OpenAI compatibility.

### Installation Issues
```bash
# Clear npm cache and reinstall
npm cache clean --force
npm uninstall n8n-nodes-media-decrypt
npm install https://github.com/Drishtech/n8n-nodes-media-decrypt
```

## Example Workflow

### WhatsApp Audio → OpenAI Transcription
1. **WhatsApp Media Decrypt Node**:
   - URL: `https://example.whatsapp.net/media.enc`
   - Media Key: `your-base64-media-key==`
   - Message Type: `Audio Message`
   - MIME Type: `Audio - OGG (WhatsApp Voice Messages)`

2. **OpenAI Node** (Audio Transcribe):
   - Will automatically detect the binary field from step 1
   - Transcribes the decrypted audio to text

## Version History

### v0.1.4 (Latest) 🚀
- 🤖 **OpenAI Integration**: Fixed binary field naming for seamless OpenAI compatibility
- 🎯 **Enhanced Dynamic Dropdown**: Real-time MIME type filtering
- 🔧 **Improved Build Process**: Fixed compilation and file structure issues
- 📦 **Better Package Management**: Optimized for GitHub installation

### v0.1.3
- ✅ **Complete rewrite** of WhatsApp media decryption algorithm
- ✅ **Fixed MAC verification** with proper HKDF implementation
- ✅ **Smart MIME type dropdown** with context-aware filtering
- ✅ **Enhanced error handling** with detailed debugging information

### v0.1.2
- ✅ Enhanced MIME type dropdown with better organization
- ✅ Smart default MIME type selection based on message type
- ✅ Improved error messages and validation

### v0.1.1
- Initial release with basic decryption functionality

## Technical Details

### Encryption Algorithm
This node implements the correct WhatsApp media decryption algorithm based on the latest research:

1. **HKDF Key Derivation**: 
   - Uses empty 32-byte salt: `Buffer.alloc(32, 0)`
   - Derives 112 bytes: IV (16) + cipher key (32) + MAC key (32) + refKey (32)
   
2. **MAC Verification**: 
   - Primary method: `HMAC-SHA256(macKey, iv + encrypted)` truncated to 10 bytes
   - Fallback method: `HMAC-SHA256(macKey, encrypted)` for compatibility
   
3. **AES-256-CBC Decryption**: Decrypts the media content with proper padding

4. **Binary Output**: Uses filename as binary field key for OpenAI compatibility

### Binary Data Format
```javascript
{
  binary: {
    "whatsapp_audio_2025-06-03T20-42-42.ogg": {
      data: "base64-encoded-data",
      fileName: "whatsapp_audio_2025-06-03T20-42-42.ogg",
      mimeType: "audio/ogg"
    }
  }
}
```

### Security Features
- Media keys are never logged or stored
- URLs are truncated in output for security
- Proper error handling prevents information leakage
- Input validation prevents injection attacks

## Supported WhatsApp Media Types

- ✅ **Voice Messages** (OGG format)
- ✅ **Audio Files** (MP3, AAC, etc.)
- ✅ **Images** (JPEG, PNG, WebP, GIF)
- ✅ **Videos** (MP4, WebM, AVI, MOV)
- ✅ **Documents** (PDF, Office files, Archives)

## Requirements

- **n8n version**: 1.0.0 or higher
- **Node.js**: Compatible with n8n requirements
- **Dependencies**: axios for HTTP requests

## License

MIT License - see [LICENSE.md](LICENSE.md) for details

## Credits

- **Original algorithm**: Based on [sostenesapollo/baileys-decode-enc-by-url](https://github.com/sostenesapollo/baileys-decode-enc-by-url)
- **WhatsApp decryption research**: Thanks to the Baileys and reverse engineering community

## Contributing

Contributions are welcome! Please feel free to:
- Submit bug reports or feature requests
- Fork the repository and submit pull requests
- Improve documentation

## Repository

- **GitHub**: [https://github.com/Drishtech/n8n-nodes-media-decrypt](https://github.com/Drishtech/n8n-nodes-media-decrypt)
- **Issues**: [Report issues](https://github.com/Drishtech/n8n-nodes-media-decrypt/issues)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your inputs (media key, message type, URL)
3. Look at the detailed error messages for specific guidance
4. Open an issue on GitHub with debug information if needed

---

**Made with ❤️ for the n8n community** 

- **Email**: info@drishtech.com 