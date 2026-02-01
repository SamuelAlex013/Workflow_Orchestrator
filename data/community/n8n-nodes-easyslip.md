# n8n-nodes-easyslip

<p align="center">
  <img src="https://easyslip.com/wp-content/uploads/2023/12/Design-V3-02-768x203.png" alt="EasySlip Logo" width="400"/>
</p>

![EasySlip Node](https://img.shields.io/badge/n8n-community--node-blue)
![Version](https://img.shields.io/badge/version-1.0.6-green)
![License](https://img.shields.io/badge/license-MIT-blue)

An n8n community node package for verifying bank slips and TrueMoney wallet slips using the EasySlip API. This node provides seamless integration with Thailand's digital payment verification system.

## Features

- 🏦 **Bank Slip Verification** - Verify bank transfer slips from all major Thai banks
- 💳 **TrueMoney Wallet Verification** - Verify TrueMoney wallet payment slips
- 🔍 **Multiple Input Methods** - Support for QR payload, image files, base64 data, and image URLs
- 🎯 **Smart Filtering** - Filter results by bank code or receiver name with dual outputs
- 🔒 **Duplicate Detection** - Built-in duplicate slip detection capabilities
- 🤖 **AI Agent Compatible** - Marked as `usableAsTool: true` for AI workflow integration

## Installation

### Prerequisites

- Node.js 20.15 or higher
- n8n installed globally: `npm install n8n -g`
- EasySlip API access token from [EasySlip Developer Portal](https://document.easyslip.com/documents/start)

### Install the Node

```bash
npm install n8n-nodes-easyslip
```

### Set up Credentials

1. In n8n, go to **Credentials** → **Create New**
2. Search for "EasySlip API"
3. Enter your Bearer token from the EasySlip Developer Portal
4. Test the connection and save

## Usage

## Node Behavior

### Resources

#### Bank Slip
Supports verification of bank transfer slips from major Thai banks including:
- Bangkok Bank (BBL) - Code: 002
- Krung Thai Bank (KTB) - Code: 006  
- Bank of Ayudhya (BAY) - Code: 025
- Kasikorn Bank (KBANK) - Code: 004
- And 17+ other banks

#### TrueMoney Wallet
Supports verification of TrueMoney wallet payment slips.

### Operations

#### Bank Slip Operations

**1. Verify by Payload**
- Uses QR code data from bank slip
- Method: GET request with query parameters
- Input: QR payload string
- Fastest verification method

**2. Verify by Image**
- Upload slip image file directly
- Method: POST with multipart form data
- Input: Binary image data from previous node
- Supports JPG, PNG formats

**3. Verify by Base64**
- Uses base64 encoded image data
- Method: POST with JSON payload
- Input: Base64 string of slip image

**4. Verify by URL**
- Fetches slip image from URL
- Method: POST with JSON payload
- Input: Public URL to slip image

#### TrueMoney Wallet Operations

**1. Verify by Image**
- Upload wallet slip image
- Method: POST with multipart form data
- Input: Binary image data

### Dual Output System

The node features a smart dual output system:

**Output 1: "Matched / All"**
- Contains items that match applied filters
- Contains all items when no filters are applied
- Contains error responses when "Continue on Fail" is enabled

**Output 2: "Not Matched"** 
- Contains items that don't match applied filters
- Empty when no filters are applied
- Only used for Bank Slip verification with filters

### Filtering Options (Bank Slip Only)

**Filter by Receiver Bank Code**
- Filter results by specific bank
- Non-matching items route to second output
- Supports all major Thai bank codes

**Filter by Receiver Name**
- Partial text matching on receiver name
- Case-insensitive search
- Non-matching items route to second output

## Usage Examples

### Basic Bank Slip Verification (Payload)

```json
{
  "resource": "bankSlip",
  "operation": "verifyByPayload", 
  "payload": "00020101021129370016A000000677010111011300...",
  "checkDuplicate": false
}
```

### Image-Based Verification

1. **Previous Node**: Upload or fetch slip image
2. **EasySlip Node Configuration**:
   ```json
   {
     "resource": "bankSlip",
     "operation": "verifyByImage",
     "imageBinaryProperty": "data",
     "checkDuplicate": true
   }
   ```

### Filtered Verification with Dual Outputs

```json
{
  "resource": "bankSlip",
  "operation": "verifyByPayload",
  "payload": "00020101021129370016A000000677010111011300...",
  "additionalOptions": {
    "receiverBankCode": "004",
    "receiverName": "John Doe"
  }
}
```

**Result**: 
- Matching slips → Output 1
- Non-matching slips → Output 2

### TrueMoney Wallet Verification

```json
{
  "resource": "truemoneyWallet",
  "operation": "verifyByImage",
  "imageBinaryProperty": "data",
  "checkDuplicate": true
}
```

## Response Format

### Successful Verification Response

```json
{
  "success": true,
  "data": {
    "receiver": {
      "account": {
        "name": {
          "th": "นายจอห์น โด"
        }
      },
      "bank": {
        "id": "004",
        "name": "ธนาคารกสิกรไทย"
      }
    },
    "amount": 1000.00,
    "transactionDate": "2024-01-15T10:30:00Z",
    "reference": "REF123456789"
  }
}
```

### Duplicate Slip Response

```json
{
  "success": false,
  "message": "duplicate_slip",
  "data": {
    // Original slip data
  }
}
```

**Note**: Duplicate slip responses are treated as valid data, not errors.


## Error Handling

### Built-in Error Handling
- **Duplicate Detection**: 400 `duplicate_slip` responses are treated as valid data
- **Continue on Fail**: Errors route to first output when enabled
- **Missing Binary Data**: Clear error messages for missing image data

### Debug Mode
Enable debug logging in Additional Options:
```json
{
  "additionalOptions": {
    "enableDebugLogging": true
  }
}
```

## Best Practices

### 1. Choose the Right Verification Method
- **Payload**: Fastest, use when QR data is available
- **Image**: Most reliable, use for image-based workflows
- **Base64**: Good for API integrations with base64 data
- **URL**: Convenient for web-scraped images

### 2. Implement Filtering Strategically
- Use bank code filtering for bank-specific workflows
- Use receiver name filtering for payment reconciliation
- Connect both outputs when using filters

### 3. Handle Duplicates Appropriately
- Enable `checkDuplicate` for payment processing
- Disable for verification-only workflows
- Process duplicate responses as valid data

### 4. Optimize for Performance
- Use payload verification when possible (fastest)
- Batch image processing for multiple slips
- Enable debug logging only during development

## Development

### Project Structure
```
├── nodes/
│   └── EasySlip/
│       ├── EasySlip.node.ts     # Main node implementation
│       └── easyslip.svg         # Node icon
├── credentials/
│   └── EasySlipApi.credentials.ts # API credentials setup
├── dist/                        # Compiled output
├── package.json                 # Project configuration
├── tsconfig.json               # TypeScript config
└── gulpfile.js                 # Build tasks
```

### Build Commands

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Development mode (watch)
npm run dev

# Lint code
npm run lint

# Auto-fix linting issues
npm run lintfix

# Format code
npm run format

# Pre-publish validation
npm run prepublishOnly
```

### Testing Locally

1. Build the project: `npm run build`
2. Link the package: `npm link`
3. In your n8n installation: `npm link n8n-nodes-easyslip`
4. Restart n8n to see the node in the palette

## API Documentation

- [EasySlip Developer Documentation](https://document.easyslip.com/documents/start)


## Release Automation

- Merging `dev` into `main` triggers the **Release and Publish to NPM** GitHub Actions workflow. The pipeline runs `npm ci`, linting (`lint` and `lint:prepublish`), and `npm run build` before publishing to npm using the version in `package.json`.
- Ensure the package version is bumped on the `dev` branch before opening the merge; npm rejects duplicate versions.
- The workflow requires an `NPM_TOKEN` secret with publish permissions for the `n8n-nodes-easyslip` package (`Settings → Secrets and variables → Actions`).
- The existing tag-based (`v*`) and manual (`workflow_dispatch`) triggers still work for ad-hoc releases outside of the `main` merge flow.
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support

- **Documentation**: [EasySlip API Docs](https://document.easyslip.com/documents/start)
- **Issues**: [GitHub Issues](https://github.com/M4h45amu7x/n8n-nodes-easyslip/issues)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io/)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.
