# n8n-nodes-data-converter

A comprehensive data conversion node for n8n that handles Base64, Binary, Format conversions (JSON/XML/YAML/CSV), HTML generation, and various encodings - all in one place.

## 🎯 Why This Node?

Stop writing Code nodes for common data transformations! This node provides a single, intuitive interface for all your data conversion needs:

- ✅ **Base64 Operations** - Encode/decode text, binary, JSON, and data URLs
- ✅ **Binary Handling** - Convert between JSON, text, and binary formats
- ✅ **Format Conversions** - Transform between JSON, XML, YAML, CSV, and Markdown
- ✅ **HTML Generation** - Create tables, lists, and formatted HTML from data
- ✅ **Text Encoding** - URL, HTML entity, and hex encoding/decoding
- ✅ **String Transformations** - Filename cleaning, case conversions, slugification, and text manipulation

## 📦 Installation

### Community Node (Recommended)

1. In n8n, go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-data-converter`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-data-converter
```

Then restart your n8n instance.

## 🚀 Quick Start

### Example 1: Base64 Encode JSON

Convert JSON data to Base64 for API calls:

```
Resource: Base64
Operation: JSON to Base64
```

### Example 2: Convert JSON to YAML

Transform JSON configuration to YAML format:

```
Resource: Format
Operation: JSON to YAML
```

### Example 3: Generate HTML Table

Create an HTML table from JSON data:

```
Resource: HTML
Operation: JSON to HTML Table
```

### Example 4: Chain Multiple String Operations

Clean and format filenames in one step:

```
Resource: String
Operation: Apply Multiple Operations
Operations:
  1. Remove Special Characters (Keep Filename Characters: ON)
  2. Convert to kebab-case
  3. Convert to lowercase
```

Input: `"My File (2024) - FINAL VERSION.pdf"`
Output: `"my-file-2024-final-version.pdf"`

## 📚 Operations Reference

### Base64 Operations

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| Text to Base64 | Encode plain text | String | Base64 string |
| Base64 to Text | Decode Base64 to text | Base64 string | Plain text |
| Binary to Base64 | Encode binary data | Binary | Base64 string |
| Base64 to Binary | Decode to binary | Base64 string | Binary data |
| JSON to Base64 | Encode JSON object | JSON | Base64 string |
| Base64 to JSON | Decode to JSON | Base64 string | JSON object |
| Create Data URL | Create data URL with MIME type | Binary/Text | Data URL |
| Parse Data URL | Extract data from data URL | Data URL | Binary + metadata |

### Binary Operations

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| JSON to Binary | Convert JSON to binary | JSON | Binary buffer |
| Binary to JSON | Parse binary as JSON | Binary | JSON object |
| Text to Binary | Convert text to binary | String | Binary buffer |
| Binary to Text | Convert binary to text | Binary | String |

### Format Conversions

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| JSON to XML | Convert JSON to XML | JSON | XML string |
| XML to JSON | Parse XML to JSON | XML string | JSON object |
| JSON to YAML | Convert JSON to YAML | JSON | YAML string |
| YAML to JSON | Parse YAML to JSON | YAML string | JSON object |
| JSON to CSV | Convert JSON array to CSV | JSON array | CSV string |
| CSV to JSON | Parse CSV to JSON | CSV string | JSON array |
| JSON to Markdown | Format JSON as Markdown | JSON | Markdown string |
| JSON to String | Extract/format JSON content | JSON | String/HTML |
| CSV to Markdown | Convert CSV to Markdown table | CSV string | Markdown table |

### HTML Generation

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| JSON to HTML Table | Create HTML table | JSON array | HTML table |
| JSON to HTML List | Create HTML list | JSON array | HTML ul/ol |
| CSV to HTML Table | Convert CSV to table | CSV string | HTML table |
| Markdown to HTML | Convert Markdown to HTML | Markdown | HTML string |
| HTML to Markdown | Convert HTML to Markdown | HTML | Markdown string |

### Encoding Operations

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| URL Encode | Encode for URLs | String | URL-encoded string |
| URL Decode | Decode from URLs | URL-encoded | Plain string |
| HTML Entity Encode | Encode HTML entities | String | HTML-safe string |
| HTML Entity Decode | Decode HTML entities | HTML string | Plain string |
| Hex Encode | Convert to hexadecimal | String/Binary | Hex string |
| Hex Decode | Convert from hexadecimal | Hex string | String/Binary |

### String Operations

| Operation | Description | Input | Output |
|-----------|-------------|-------|--------|
| Apply Multiple Operations | Chain multiple string operations in sequence | String | Transformed string |
| Clean Filename | Remove unsafe characters from filenames | String | Safe filename |
| Slugify | Create URL-friendly slug | String | Slug string |
| Title Case | Convert to Title Case | String | Title Case String |
| Camel Case | Convert to camelCase | String | camelCase string |
| Kebab Case | Convert to kebab-case | String | kebab-case string |
| Snake Case | Convert to snake_case | String | snake_case string |
| Upper Case | Convert to UPPERCASE | String | UPPERCASE STRING |
| Lower Case | Convert to lowercase | String | lowercase string |
| Normalize Whitespace | Clean up extra spaces | String | Normalized string |
| Parse Email Address | Extract name, email, domain from email strings | String | Object with parts |
| Remove Special Chars | Keep only letters/numbers (with options) | String | Clean string |
| Capitalize First | Capitalize first letter | String | Capitalized string |
| Reverse Text | Reverse character order | String | Reversed string |
| Truncate | Shorten text with suffix | String | Truncated... |
| Pad Text | Add padding characters | String | Padded string |

#### Apply Multiple Operations

The **Apply Multiple Operations** feature allows you to chain multiple string transformations in a single operation:

- **Sortable operations list** - Drag and drop to reorder operations
- **All operations supported** - Combine any string operations
- **Configurable options** - Each operation can have its own settings
- **Sequential processing** - Operations are applied in the order specified

**Example combinations:**
- Remove Special Characters → Convert to snake_case
- Normalize Whitespace → Slugify → Truncate
- Clean Filename → Convert to kebab-case → Lower Case

#### JSON to String Operation

The **JSON to String** operation provides flexible ways to extract or format JSON content:

**Extraction Modes:**
- **Pretty Print** - Format JSON with customizable indentation
- **Compact** - Minified JSON without whitespace
- **Extract Field** - Extract specific field values using dot notation (e.g., `data.items[0].name`)
- **Template** - Format using templates with `{{field}}` placeholders

**Use Cases:**
- Extract HTML content from JSON fields for direct rendering
- Generate HTML from JSON using templates
- Extract specific values from nested JSON structures
- Format JSON for display or API requirements

**Template Example:**
```html
<div class="card">
  <h2>{{title}}</h2>
  <p>{{description}}</p>
  <span>Price: ${{price}}</span>
</div>
```

#### Remove Special Characters Options

When using **Remove Special Characters**, you can configure:
- **Keep File Extension** - Preserves the file extension (last dot and everything after)
- **Keep Filename Characters** - Preserves dots (.), hyphens (-), and underscores (_) for filenames
- **Keep Numbers** - Whether to keep numeric characters
- **Keep Spaces** - Whether to preserve spaces

## 💡 Common Use Cases

### Webhook Data Processing
```
Webhook → Data Converter (Base64 to Binary) → Save to Storage
```

### API Integration
```
Database → Data Converter (JSON to XML) → SOAP API
```

### Report Generation
```
Data → Data Converter (JSON to Markdown) → Email/Slack
```

### File Upload Handling
```
Form Data → Data Converter (Base64 to Binary) → Cloud Storage
```

### Filename Sanitization
```
User Input → Data Converter (Clean Filename) → File System
```

### URL Generation
```
Blog Title → Data Converter (Slugify) → URL Path
```

## 🤖 AI Agent Compatibility

This node is fully compatible with AI agents (`usableAsTool: true`). All operations include:
- Clear descriptions
- Example inputs/outputs
- Structured error messages
- Predictable behavior

## ⚙️ Advanced Options

### Error Handling
- All operations support `continueOnFail`
- Clear error messages with recovery suggestions
- Input validation with helpful feedback

### Performance
- Efficient memory usage for large files
- Streaming support for compatible operations
- Optimized for batch processing

## 🐛 Troubleshooting

### Common Issues

**"Invalid Base64 string"**
- Ensure the input is properly Base64 encoded
- Check for spaces or special characters

**"Cannot parse JSON"**
- Validate JSON syntax
- Check for trailing commas or unquoted keys

**"CSV parsing failed"**
- Verify delimiter settings
- Check for inconsistent column counts

## 📝 Changelog

### Latest Updates (v0.3.3)
- **Keep File Extension** option for Remove Special Characters - preserves file extensions when cleaning filenames
- **Apply Multiple Operations** - Chain multiple string transformations in sequence
- **Keep Filename Characters** option for Remove Special Characters operation
- Fixed options display in Apply Multiple Operations mode

See [CHANGELOG.md](CHANGELOG.md) for full version history.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT - See [LICENSE](LICENSE) file

## 🙏 Credits

Created by [Jez (Jeremy Dawes)](https://www.jezweb.com.au)

## 🔗 Links

- [GitHub Repository](https://github.com/jezweb/n8n-nodes-data-converter)
- [npm Package](https://www.npmjs.com/package/n8n-nodes-data-converter)
- [n8n Community](https://community.n8n.io)

---

**Need help?** Open an issue on GitHub or reach out in the n8n community forum!