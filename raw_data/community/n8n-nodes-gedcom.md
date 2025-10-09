# n8n-nodes-gedcom

An n8n community node for parsing GEDCOM genealogy files and computing ancestry trees.

## Features

- 🔍 **Parse GEDCOM files** - Extract persons and families from standard GEDCOM files
- 🌳 **Compute ancestry trees** - Generate multi-generation ancestor trees for any individual
- 📁 **Multiple input sources** - Support binary data and URL downloads
- 🔤 **Encoding support** - Handle UTF-8, UTF-16 with BOM detection and fallback for legacy encodings
- ⚡ **Performance optimized** - Efficient parsing for files up to several MB
- 🧪 **Well tested** - Comprehensive unit tests and E2E workflows

## Installation

### Via N8N_CUSTOM_EXTENSIONS (Recommended)

```bash
# Set custom extensions directory
export N8N_CUSTOM_EXTENSIONS="$HOME/.n8n/custom"
mkdir -p "$N8N_CUSTOM_EXTENSIONS"

# Clone and build the node
git clone https://github.com/your-username/n8n-nodes-gedcom.git
cd n8n-nodes-gedcom
pnpm install
pnpm run build

# Copy to extensions directory
cp -R dist "$N8N_CUSTOM_EXTENSIONS/n8n-nodes-gedcom"
cp package.json "$N8N_CUSTOM_EXTENSIONS/n8n-nodes-gedcom/"

# Start n8n
n8n start
```

### Manual Installation

```bash
# Install in your n8n custom nodes directory
mkdir -p ~/.n8n/custom/n8n-nodes-gedcom
cd ~/.n8n/custom/n8n-nodes-gedcom

# Copy built files
cp -R /path/to/n8n-nodes-gedcom/dist/* .
cp /path/to/n8n-nodes-gedcom/package.json .

# Restart n8n
```

## Usage

## Test your node locally
You can test your node as you build it by running it in a local n8n instance.

Install n8n using npm:

```bash
npm install n8n -g
```

When you are ready to test your node, publish it locally:

```bash
# In your node directory
npm run build
npm link
```

Install the node into your local n8n instance:

```bash
# In the nodes directory within your n8n installation
# node-package-name is the name from the package.json
npm link n8n-nodes-gedcom
```

### Check your directory

Make sure you run `npm link n8n-nodes-gedcom` in the nodes directory within your n8n installation. This can be:

*   `~/.n8n/custom/`
*   `~/.n8n/<your-custom-name>`: if your n8t installation set a different name using `N8N_CUSTOM_EXTENSIONS`.

Start n8n:

```bash
n8n start
```

Open n8n in your browser. You should see your nodes when you search for them in the nodes panel.

### Node names

Make sure you search using the node name, not the package name. For example, if your npm package name is `n8n-nodes-gedcom`, and the package contains nodes named `Gedcom`, you should search for `Gedcom`, not `n8n-nodes-gedcom`.

The GEDCOM node provides two main operations:

### Parse Operation

Extracts all persons and families from a GEDCOM file.

**Parameters:**
- **Operation**: Parse
- **Source**: Binary Data or URL
- **Binary Property**: Property name containing GEDCOM data (default: "data")
- **URL**: HTTP/HTTPS URL to download GEDCOM file

**Output:**
```json
{
  "meta": {
    "individuals": 150,
    "families": 75,
    "encodingTag": "UTF-8"
  },
  "persons": [
    {
      "id": "@I1@",
      "name": "Doe/John/",
      "birthDate": "01 JAN 1900",
      "deathDate": "15 DEC 1980",
      "famc": ["@F1@"],
      "fams": ["@F2@"]
    }
  ],
  "families": [
    {
      "id": "@F1@",
      "husband": "@I1@",
      "wife": "@I2@",
      "children": ["@I3@", "@I4@"]
    }
  ]
}
```

### Ancestors Operation

Computes the ancestry tree for a specific person up to N generations.

**Parameters:**
- **Operation**: Ancestors
- **Source**: Binary Data or URL
- **Root Person ID**: ID of person to trace (e.g., "@I0074@" or "I0074")
- **Max Generations**: Number of generations to retrieve (1-15, default: 9)

**Output:**
```json
{
  "root": "@I0074@",
  "generations": [
    ["@I0074@"],
    ["@I100@", "@I101@"],
    ["@I200@", "@I201@", "@I202@", "@I203@"]
  ],
  "nodes": [
    {
      "id": "@I0074@",
      "name": "Smith/John/",
      "birthDate": "15 MAR 1985",
      "deathDate": "",
      "famc": ["@F50@"],
      "fams": []
    }
  ],
  "edges": [
    {
      "parent": "@I100@",
      "child": "@I0074@", 
      "relation": "father"
    },
    {
      "parent": "@I101@",
      "child": "@I0074@",
      "relation": "mother"
    }
  ]
}
```

## Encoding Support

The node automatically detects and handles various encodings:

- **UTF-8** (with or without BOM) - Primary support
- **UTF-16LE/BE** (with BOM detection) - Full support  
- **Legacy encodings** (ANSEL, CP1252, etc.) - Fallback parser

When the primary parser fails or detects non-UTF-8 encoding tags, the node automatically attempts parsing with the fallback parser (`read-gedcom`) for better compatibility with older GEDCOM files.

## Examples

### Example 1: Parse a GEDCOM file from binary data

```
Read Binary File → GEDCOM (Parse) → Process Results
```

### Example 2: Get 5 generations of ancestors

```
HTTP Request (GEDCOM URL) → GEDCOM (Ancestors, rootId="@I123@", maxGenerations=5) → Visualize Tree
```

### Example 3: Find all descendants (using Parse + custom logic)

```
Read Binary File → GEDCOM (Parse) → Code Node (filter/traverse) → Results
```

## Error Handling

The node provides clear error messages for common issues:

- **File not found**: "GEDCOM file is empty or could not be read"
- **Invalid URL**: "Failed to download GEDCOM file from URL: 404"
- **Missing root person**: "Root person with ID '@I999@' not found in GEDCOM data"
- **Encoding issues**: "Failed to parse GEDCOM file with both parsers..."
- **Missing parameters**: "Root Person ID is required for ancestors operation"

## Limitations

### Current Version (v0.1.0)
- Names with multiple `NAME` tags: Only the first name is captured
- Dates are preserved as raw text (no normalization for "ABT 1900", etc.)
- No duplicate detection or individual merging
- No descendants computation (ancestors only)
- No GEDCOM export functionality
- No visual tree rendering

### File Size Limits
- Recommended: Files up to 5-10 MB
- Memory usage: Entire file loaded into memory
- Streaming not supported in this version

## Testing

The project includes comprehensive tests:

```bash
# Run unit tests
pnpm run test

# Run type checking
pnpm run typecheck

# Run linting
pnpm run lint

# Build project
pnpm run build
```

### Test Fixtures
- `test/fixtures/minimal.ged` - Basic 3-person family
- `test/fixtures/sample-utf8.ged` - Multi-generation UTF-8 file

### E2E Workflows
- `workflows/e2e-parse.workflow.json` - Test parsing operation
- `workflows/e2e-ancestors.workflow.json` - Test ancestry computation

## Development

### Project Structure
```
src/
  nodes/
    Gedcom/
      Gedcom.node.ts          # Main node implementation
test/
  unit/
    gedcom.parse.spec.ts      # Parse operation tests
    gedcom.ancestors.spec.ts  # Ancestors operation tests
  fixtures/
    *.ged                     # Test GEDCOM files
workflows/
  e2e-*.workflow.json         # n8n workflow tests
```

### Building from Source

```bash
git clone https://github.com/your-username/n8n-nodes-gedcom.git
cd n8n-nodes-gedcom
pnpm install
pnpm run build
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass: `pnpm run test && pnpm run typecheck && pnpm run lint`
5. Submit a pull request

## License

MIT License - see [LICENSE.md](LICENSE.md) for details.

## Dependencies

- **parse-gedcom** (^2.0.1) - Primary GEDCOM parser
- **read-gedcom** (^0.3.2) - Fallback parser for legacy encodings

## Support

- 📖 **Documentation**: This README
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/n8n-nodes-gedcom/issues)
- 💬 **Community**: [n8n Community Forum](https://community.n8n.io/)

---

*Generated with ❤️ for the n8n community*
