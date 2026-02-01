# n8n-nodes-ai-switch

This is an n8n node that provides intelligent routing for your n8n workflows based on content analysis. The AI Switch analyzes incoming messages or data using keyword matching or AI-powered content classification, then routes the flow to the appropriate output. 

## Installation

Follow these steps to install the node in your n8n instance:

### Using NPM ( easiest )

```
npm i n8n-nodes-ai-switch
```
### Local Installation

1. Clone this repository:
```bash
git clone https://github.com/deepsuthar496/n8n-nodes-ai-switch.git
```

2. Navigate to the project directory:
```bash
cd n8n-nodes-ai-switch
```

3. Install dependencies:
```bash
npm install
```

4. Build the node:
```bash
npm run build --ignore-scripts
```

5. Copy the built files to your n8n custom nodes directory:
```bash
# Windows (PowerShell)
robocopy "dist" "C:\Users\YOUR_USERNAME\.n8n\custom\node_modules\n8n-nodes-ai-switch\dist" /E
Copy-Item -Path "dist/package.json" -Destination "C:\Users\YOUR_USERNAME\.n8n\custom\node_modules\n8n-nodes-ai-switch\" -Force
Copy-Item -Path "index.js" -Destination "C:\Users\YOUR_USERNAME\.n8n\custom\node_modules\n8n-nodes-ai-switch\" -Force

# Mac/Linux
mkdir -p ~/.n8n/custom/node_modules/n8n-nodes-ai-switch/
cp -r dist ~/.n8n/custom/node_modules/n8n-nodes-ai-switch/
cp dist/package.json ~/.n8n/custom/node_modules/n8n-nodes-ai-switch/
cp index.js ~/.n8n/custom/node_modules/n8n-nodes-ai-switch/
```

6. Restart your n8n instance to load the new node.

## Operations

The AI Switch offers several powerful routing capabilities:

- **Keyword-Based Routing**: Route based on keyword matching in the content
- **AI-Powered Classification**: Use AI language models to intelligently classify content
- **Fallback Routing**: Default route if no match is found
- **Multiple Output Paths**: Dynamic routing based on your defined routes
- **Debug Mode**: Detailed logging to understand routing decisions

## Compatibility

This node has been developed and tested with n8n versions 1.0.0 and later.

- Supports AI Agent outputs
- Works with Chat Message triggers
- Compatible with n8n's Language Models and external LLMs

## Usage

1. **Add the AI Switch node** to your workflow between your input node and the branching paths
2. **Connect both inputs**:
   - Main Input: Connect your trigger or data source
   - LM Input: Connect your AI language model
3. **Configure Analysis Field**:
   - Specify which field contains the content to analyze (e.g., `message`, `content`, `text`)
   - Leave empty to auto-detect common field names
4. **Define Routes**:
   - Add routes with clear names and descriptions
   - For each route, provide a detailed description of when content should follow that path
5. **Enable Debug Mode** during testing to see detailed routing decisions

### Example Workflow

A common use case is routing customer inquiries:

1. When a chat message is received
2. AI Switch analyzes the content
3. Routes to different departments based on the message content:
   - Technical support
   - Billing inquiries
   - General information

## License

[MIT](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/LICENSE.md)
