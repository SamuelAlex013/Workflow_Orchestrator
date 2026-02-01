# n8n-nodes-advanced-output-parser

![n8n.io - Workflow Automation](https://user-images.githubusercontent.com/65276001/173571060-9f2f6d7b-bac0-43b6-bdb2-001da9694058.png)

## Advanced Output Parser for n8n

This is a community node for n8n that provides an advanced output parser with dynamic expression support. It extends the functionality of the standard LangChain output parser by allowing you to use n8n expressions to dynamically create and modify JSON schemas at runtime.

### Note: This is not yet production ready. Use at your own risk

### Features

- **Dynamic Expression Support**: Use n8n expressions in JSON schemas and examples
- **Multiple Schema Modes**:
  - Static JSON Schema
  - Generate from JSON example with expressions
  - Fully dynamic schemas using expressions
- **Auto-Fix Functionality**: Automatically retry parsing with LLM assistance when output doesn't match schema
- **Expression-Powered**: Leverage workflow data to create context-aware schemas
- **Backward Compatible**: Works with existing static schemas

### Installation

To install this community node, you have several options:

#### Option 1: Install via n8n Community Nodes

1. Go to **Settings > Community Nodes** in your n8n interface
2. Enter `n8n-nodes-advanced-output-parser` in the npm package name field
3. Click **Install**

#### Option 2: Manual Installation

```bash
# In your n8n installation directory
npm install n8n-nodes-advanced-output-parser
```

#### Option 3: Docker

Add the package to your n8n Docker environment:

```dockerfile
FROM n8nio/n8n
USER root
RUN npm install -g n8n-nodes-advanced-output-parser
USER node
```

### Usage

1. **Add the Node**: Search for "Advanced Output Parser" in the node palette
2. **Connect to LangChain**: Connect it to any LangChain chain or agent node
3. **Configure Schema Mode**: Choose how you want to define your schema:
   - **Static**: Use a fixed JSON schema
   - **From Example**: Generate schema from a JSON example
   - **Dynamic**: Use expressions to build schemas from workflow data

### Schema Modes

#### Static JSON Schema

Use a traditional, fixed JSON schema:

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  }
}
```

#### From Example with Expressions

Generate schema from JSON examples that can include expressions:

```json
{
  "user": "{{ $json.username }}",
  "preferences": ["{{ $json.defaultPreference }}"],
  "metadata": {
    "source": "{{ $node.name }}"
  }
}
```

#### Dynamic Expression Schema

Build entire schemas using expressions:

```json
{{
  $json.userType === 'admin' ?
  {
    "type": "object",
    "properties": {
      "adminData": {"type": "object"},
      "permissions": {"type": "array"}
    }
  } :
  {
    "type": "object",
    "properties": {
      "userData": {"type": "object"}
    }
  }
}}
```

### Use Cases

- **Multi-tenant Applications**: Different schemas for different tenants
- **API Response Parsing**: Handle varying API response structures
- **Dynamic Form Processing**: Process forms with different field sets
- **Context-Aware Data Extraction**: Extract different data based on workflow context
- **Conditional Output Formatting**: Format output differently based on input data

### Expression Examples

#### Conditional Schemas

```javascript
{
  {
    $json.responseType === "user" ? $json.userSchema : $json.productSchema;
  }
}
```

#### Dynamic Field Generation

```javascript
{{
  {
    "type": "object",
    "properties": Object.fromEntries(
      $json.fields.map(field => [
        field.name,
        {"type": field.type, "description": field.description}
      ])
    )
  }
}}
```

#### Fallback Schemas

```javascript
{
  {
    $json.customSchema || $parameter.defaultSchema;
  }
}
```

### Configuration Options

| Option                       | Description                                                   |
| ---------------------------- | ------------------------------------------------------------- |
| **Schema Mode**              | How to define the output schema (Static/From Example/Dynamic) |
| **JSON Schema**              | The JSON schema definition (supports expressions)             |
| **JSON Example**             | Example JSON to generate schema from (supports expressions)   |
| **Make All Fields Required** | Whether generated schemas should make all fields required     |
| **Auto-Fix Format**          | Automatically retry parsing with LLM when format is incorrect |
| **Custom Prompt**            | Custom prompt for auto-fix functionality                      |

### Auto-Fix Functionality

When enabled, the auto-fix feature will:

1. Attempt to parse the LLM output with your schema
2. If parsing fails, automatically generate a retry prompt
3. Send the retry prompt to the connected LLM
4. Parse the corrected response

This is especially useful for complex schemas where the LLM might need guidance.

### Development

To contribute to this project:

```bash
# Clone the repository
git clone https://github.com/volkovmqx/n8n-nodes-advanced-output-parser.git

# Install dependencies
cd n8n-nodes-advanced-output-parser
npm install

# Build the project
npm run build

# Link for local development
npm link
```

### Requirements

- n8n version 1.0.0 or higher
- Node.js 18.10 or higher

### Dependencies

- `@langchain/core`: LangChain core functionality
- `langchain`: LangChain output parsers
- `zod`: Schema validation
- `generate-schema`: JSON schema generation
- `json-schema`: JSON Schema types

### License

MIT

### Support

For issues, questions, or contributions:

- GitHub Issues: [https://github.com/volkovmqx/n8n-nodes-advanced-output-parser/issues](https://github.com/volkovmqx/n8n-nodes-advanced-output-parser/issues)
- n8n Community: [https://community.n8n.io](https://community.n8n.io)

### Changelog

#### v1.0.0

- Initial release
- Dynamic expression support for JSON schemas
- Multiple schema modes (Static, From Example, Dynamic)
- Auto-fix functionality
- Full backward compatibility with standard output parsers

---

Made with ❤️ from Leipzig for the n8n community
