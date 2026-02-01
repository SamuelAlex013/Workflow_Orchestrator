# n8n-nodes-json-parser

[![npm version](https://badge.fury.io/js/n8n-nodes-json-parser.svg)](https://badge.fury.io/js/n8n-nodes-json-parser)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An n8n community node for extracting and parsing JSON from text, especially useful for processing AI model outputs that often embed JSON within conversational responses or markdown formatting.

## Features

🎯 **Multiple Extraction Methods**
- Smart Detection - Automatically finds JSON in various formats
- First/Last JSON Object - Extract specific occurrences
- All JSON Objects - Extract multiple JSON structures
- Between Markers - Custom delimiters (e.g., markdown code blocks)
- Custom Regex - Advanced pattern matching

🔧 **Intelligent Parsing**
- JSON5 support for relaxed syntax
- Automatic fixing of common issues:
  - Smart quotes → regular quotes
  - Trailing comma removal
  - Escape sequence correction
- Schema validation with detailed error messages

🤖 **AI-Ready**
- Compatible with AI Agent nodes (`usableAsTool: true`)
- Optimized for outputs from:
  - Google Gemini
  - OpenAI GPT
  - Anthropic Claude
  - And other AI models

## Installation

### Via n8n UI (Recommended)
1. Navigate to **Settings** → **Community Nodes**
2. Click **Install a community node**
3. Enter: `n8n-nodes-json-parser`
4. Click **Install**
5. Restart n8n

### Via npm
```bash
cd /path/to/n8n
npm install n8n-nodes-json-parser
```

### Docker
Add to your `docker-compose.yml`:
```yaml
environment:
  - N8N_COMMUNITY_PACKAGES_ENABLED=true
```
Then install via UI or exec into container.

## Usage

### Basic Example
1. Add the **JSON Parser** node to your workflow
2. Connect it to a node that outputs text (e.g., AI node, HTTP Request)
3. Configure the **Source Field** (default: `{{ $json.text }}`)
4. Select an **Extraction Method** (default: Smart Detection)
5. Execute the workflow

### Common Use Cases

#### Extract JSON from AI Response
```javascript
// Input from Gemini/GPT/Claude:
"Here's the analysis in JSON format:
```json
{
  "sentiment": "positive",
  "score": 0.85,
  "keywords": ["innovation", "growth"]
}
```
I hope this helps!"

// Output:
{
  "sentiment": "positive",
  "score": 0.85,
  "keywords": ["innovation", "growth"]
}
```

#### Fix Malformed JSON
```javascript
// Input with issues:
'{
  "name": "John",
  "age": 30,     // trailing comma
  "city": "NYC",
}'

// Output (with Fix Common Issues enabled):
{
  "name": "John",
  "age": 30,
  "city": "NYC"
}
```

#### Extract Multiple JSON Objects
Set **Extraction Method** to "All JSON Objects" and **Output Mode** to "New Items":
```javascript
// Input:
"User 1: {"id": 1, "name": "Alice"}
 User 2: {"id": 2, "name": "Bob"}"

// Output: Two separate items
// Item 1: {"id": 1, "name": "Alice"}
// Item 2: {"id": 2, "name": "Bob"}
```

## Node Parameters

### Basic Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **Source Field** | string | `{{ $json.text }}` | Expression pointing to the text containing JSON |
| **Extraction Method** | select | Smart Detection | How to find JSON in the text |
| **Output Mode** | select | Replace Input | How to return the extracted data |
| **On Error** | select | Stop Workflow | Error handling behavior |

### Advanced Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **Strict Mode** | boolean | false | Only accept valid JSON (no fixing) |
| **Fix Common Issues** | boolean | true | Auto-fix quotes, commas, etc. |
| **Allow JSON5** | boolean | false | Support relaxed JSON5 syntax |
| **JSON Schema** | json | - | Optional schema for validation |

### Extraction Methods

- **Smart Detection**: Automatically detects JSON in markdown, plain text, or mixed content
- **First JSON Object**: Finds the first valid `{...}` structure
- **Last JSON Object**: Finds the last valid `{...}` structure
- **All JSON Objects**: Extracts all valid JSON structures
- **Between Markers**: Extract between custom delimiters
- **Custom Regex**: Use your own regex pattern

### Output Modes

- **Replace Input**: Returns only the extracted JSON
- **Add to Input**: Adds extracted JSON as a new field
- **New Items**: Creates separate items for each JSON object

### Error Handling Options

- **Stop Workflow**: Throws an error and stops execution
- **Continue with Error**: Adds error info to output and continues
- **Output Original**: Returns the original input unchanged
- **Output Empty**: Returns an empty object

## Examples

### With AI Models

```yaml
Workflow:
  1. OpenAI Node → Generate structured data
  2. JSON Parser → Extract JSON from response
  3. Postgres Node → Store in database
```

### Data Processing Pipeline

```yaml
Workflow:
  1. Webhook Node → Receive mixed content
  2. JSON Parser → Extract JSON payload
  3. Transform Node → Process data
  4. HTTP Request → Send to API
```

### Log Processing

```yaml
Workflow:
  1. Read File → Load log file
  2. Split in Batches → Process line by line
  3. JSON Parser → Extract JSON from each line
  4. Aggregate → Combine results
```

## AI Agent Tool Usage

This node can be used as a tool by AI Agents:

1. Add an **AI Agent** node to your workflow
2. Connect the **JSON Parser** node to the Agent's tool input
3. The AI can now extract JSON from any text it processes

The node includes AI-friendly descriptions for all parameters, making it easy for AI models to understand when and how to use it.

## Development

### Setup
```bash
git clone https://github.com/jezweb/n8n-nodes-json-parser.git
cd n8n-nodes-json-parser
npm install
npm run build
```

### Testing
```bash
npm link
cd ~/.n8n/custom
npm link n8n-nodes-json-parser
# Restart n8n
```

### Contributing
Pull requests are welcome! Please read our contributing guidelines and ensure:
- All tests pass
- Code is linted and formatted
- Changes are documented

## Troubleshooting

### Node not appearing in n8n
- Ensure community nodes are enabled
- Check n8n version compatibility (>= 1.0.0)
- Restart n8n after installation

### Extraction not working
- Verify your input contains valid JSON
- Try different extraction methods
- Enable "Fix Common Issues" option
- Check execution logs for detailed errors

### Performance issues
- Use specific extraction methods instead of Smart Detection
- Limit input size for large datasets
- Disable schema validation if not needed

## Support

- **Issues**: [GitHub Issues](https://github.com/jezweb/n8n-nodes-json-parser/issues)
- **Community**: [n8n Community Forum](https://community.n8n.io)
- **Email**: jeremy@jezweb.net

## License

MIT - See [LICENSE](LICENSE.md) file for details

## Author

**Jeremy Dawes**
- Website: [jezweb.com.au](https://www.jezweb.com.au)
- GitHub: [@jezweb](https://github.com/jezweb)

## Acknowledgments

- n8n team for the excellent workflow automation platform
- Contributors and users of this node
- AI community for inspiring this tool's creation