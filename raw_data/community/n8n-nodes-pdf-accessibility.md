# n8n-nodes-pdf-accessibility

AI-powered PDF accessibility automation for n8n workflows.

## Installation

### n8n Cloud & Desktop App
1. Go to Settings → Community Nodes
2. Click Install and enter: `n8n-nodes-pdf-accessibility`
3. Click Install and agree to the risks

### Self-Hosted n8n
```bash
npm install n8n-nodes-pdf-accessibility
```

### Docker
```bash
docker exec <container-id> npm install n8n-nodes-pdf-accessibility
docker restart <container-id>
```

## Features

Transform any PDF into a fully accessible, WCAG-compliant document through intelligent automation. This n8n community node provides enterprise-grade accessibility analysis, remediation, and professional audit reporting powered by AI.

### AI-Powered Accessibility Tools

This node includes 5 integrated accessibility tools:

- **Image Alt-Text** (WCAG 1.1.1) - AI-generated descriptive alt-text for images
- **Heading Structure** (WCAG 1.3.1, 2.4.6) - Document hierarchy optimization  
- **Table Accessibility** (WCAG 1.3.1, 1.3.2) - Headers, captions, and structure enhancement
- **Link Text** (WCAG 2.4.4, 2.4.9) - Meaningful link descriptions
- **Metadata Enhancer** (WCAG 3.1.1, 3.1.2) - PDF metadata and language detection

### Processing Modes

Choose from 4 intelligent processing modes:

- **Auto** - AI analyzes content and applies optimal accessibility improvements
- **Analyze** - Comprehensive accessibility analysis without modification
- **Remediate** - Apply accessibility improvements with detailed reporting  
- **Custom** - Select specific accessibility tools for targeted improvements

### WCAG Compliance Levels

- **Level A** - Essential accessibility (5 criteria)
- **Level AA** - Standard compliance (recommended)
- **Level AAA** - Highest accessibility (10 criteria)

## Configuration

### Required Settings

**Processing Mode**
- Auto: Complete AI-powered accessibility automation
- Analyze: Analysis only without document modification
- Remediate: Apply accessibility improvements
- Custom: User-defined tool selection

**WCAG Compliance Level**
- A: Essential accessibility compliance
- AA: Standard accessibility compliance (recommended)
- AAA: Highest accessibility compliance

**PDF Input Method**
- Binary Data: From previous n8n nodes (HTTP Request, Google Drive, etc.)
- URL: Download directly from URL (including Google Drive share links)
- File Path: Local file system access
- Base64: Encoded PDF data from previous nodes

### Optional Settings

**LLM Provider**
- Auto: AI selects optimal provider (recommended)
- Anthropic (Claude): Best for detailed analysis
- OpenAI (GPT): Great for creative content
- Google (Gemini): Cost-effective for structured tasks

**Advanced Settings**
- Processing Depth: Basic, Full, or Deep analysis
- Language: Primary document language (en, es, fr, de, etc.)
- Output Format: PDF, Report, Summary, Log combinations
- Debug Mode: Enable detailed logging
- Cost Estimation: Preview LLM costs before processing

## AI Provider Setup

Configure API credentials in n8n for AI-powered features:

**Anthropic API**
```
API Key: Your Anthropic Claude API key
```

**OpenAI API**
```
API Key: Your OpenAI GPT API key
```

**Google AI API**
```
API Key: Your Google AI Studio API key
```

Auto mode uses available credentials intelligently. Credentials only required when using specific providers.

## Usage Examples

### Complete Automation Workflow
```
HTTP Request Node (PDF Upload)
    ↓
PDF Accessibility
    ├── Mode: Auto
    ├── WCAG Level: AA
    └── LLM Provider: Auto
    ↓
Email Node (Send Report)
```

### Google Drive Integration
```
Google Drive Node (Download PDF)
    ↓
PDF Accessibility
    ├── Mode: Analyze
    ├── Input: Binary Data
    └── Output: Report + Summary
    ↓
Google Sheets Node (Log Results)
```

### Batch Processing
```
Schedule Trigger
    ↓
Read Binary Files Node
    ↓
Split in Batches Node
    ↓
PDF Accessibility
    ├── Mode: Auto
    └── WCAG Level: AA
    ↓
Merge Node
    ↓
Database Node (Save Results)
```

### Custom Tool Selection
```
Webhook Node (PDF Upload)
    ↓
PDF Accessibility
    ├── Mode: Custom
    ├── Operations: [alttext, tables, metadata]
    └── WCAG Level: AAA
    ↓
HTTP Response Node (JSON Report)
```

## Custom Operations

For Custom mode, specify operations:
- `alttext` - Image alt-text generation
- `headings` - Heading structure optimization
- `tables` - Table accessibility enhancement
- `links` - Link text improvement
- `metadata` - PDF metadata enhancement

Example:
```json
{
  "mode": "custom",
  "customOperations": ["alttext", "tables", "metadata"],
  "wcagLevel": "AA"
}
```

## Output Structure

### Auto Mode Response
```json
{
  "mode": "intelligent_auto",
  "wcagLevel": "AA",
  "documentInfo": {
    "fileName": "document.pdf",
    "pageCount": 12,
    "hasImages": true,
    "hasTables": true
  },
  "execution": {
    "toolsExecuted": 3,
    "totalIssuesFound": 15,
    "totalFixesApplied": 12,
    "success": true
  },
  "accessibilityReport": {
    "complianceScore": 87,
    "recommendations": ["Fix table headers", "Add image alt-text"]
  },
  "exports": {
    "json": "Full JSON report",
    "html": "Professional HTML report",
    "markdown": "Documentation format",
    "csv": "Data analysis format"
  }
}
```

## Performance

### Processing Times
- Simple Text (1-5 pages): 30-60s
- Mixed Content (5-15 pages): 60-180s  
- Image-Heavy (10-25 pages): 120-300s
- Complex Reports (15-50 pages): 90-240s

### Best Practices
- Use "Basic" depth for batch processing
- Enable cost estimation for large operations
- Process during off-peak hours for large documents
- Cache results to avoid re-processing

## Troubleshooting

### Common Issues

**"Binary data not found"**
- Ensure previous node provides PDF data
- Check binary property name configuration
- Verify file format is PDF

**"LLM provider authentication failed"**
- Check API credentials in n8n settings
- Verify API key permissions and quotas
- Enable debug mode for detailed error info

**"Processing timeout"**
- Large PDFs may need increased timeout
- Try Basic processing depth for faster results
- Consider splitting large documents

**"PDF validation failed"**
- Ensure PDF is not password-protected
- Check if PDF contains readable text (not just scanned images)
- Verify file size is within limits (default 20MB)

## Security & Privacy

- **No Data Storage**: PDFs processed in memory only
- **Secure Credentials**: API keys encrypted by n8n
- **HTTPS Only**: Secure communication with all providers
- **Auto Cleanup**: Temporary data cleared after processing
- **Audit Trail**: Complete processing logs available

## Support

- [GitHub Issues](https://github.com/joselhurtado/n8n-nodes-pdf-accessibility/issues) - Bug reports and feature requests
- [n8n Community Forum](https://community.n8n.io/) - General n8n support
- [Documentation](https://github.com/joselhurtado/n8n-nodes-pdf-accessibility/tree/main/docs) - Complete API reference

## License

MIT © [Jose Hurtado](mailto:hello@hurtadojose.com)

Built for [n8n](https://n8n.io) workflow automation