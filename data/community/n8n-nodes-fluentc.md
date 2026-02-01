# FluentC N8N Plugin

This N8N community plugin provides integration with the FluentC AI Translation API, enabling you to translate text and HTML content and detect languages within your N8N workflows.

## Features

- **Translation**: Support for both real-time and batch translation modes
- **Language Detection**: Detect the language of input content
- **Language Retrieval**: Fetch lists of supported and source languages
- **Dynamic Language Selection**: Dropdown menus populated with your API key's enabled languages
- **Format Support**: Handle both text and HTML content
- **Automatic Polling**: Batch jobs are automatically polled until completion
- **Comprehensive Output**: Returns all metadata including token counts, detected languages, and model information
- **Error Handling**: Graceful error handling with continue-on-fail support
- **Language Management**: Direct link to manage enabled languages on your account

## Installation

The installation method depends on your n8n setup. Choose the appropriate method below:

### Method 1: n8n GUI Installation (Recommended for self-hosted n8n)

This is the easiest method for self-hosted n8n instances:

1. **Open n8n Settings**: In your n8n instance, go to **Settings** > **Community Nodes**
2. **Install Node**: Click **Install** 
3. **Enter Package Name**: Enter `n8n-nodes-fluentc` in the "Enter npm package name" field
4. **Accept Risk**: Check "I understand the risks of installing unverified code from a public source"
5. **Install**: Click **Install**
6. **Restart**: The nodes will be available immediately after installation

### Method 2: Verified Community Nodes (for n8n Cloud and recent versions)

If this package gets verified by n8n (future goal):

1. **Open Nodes Panel**: Go to the Canvas and open the nodes panel (click '+' or press Tab)
2. **Search**: Search for "FluentC" 
3. **Install from Community**: Look for the "More from the community" section
4. **Install**: Click on the FluentC node and select **Install**

### Method 3: Manual Installation (for Docker/advanced setups)

For Docker containers, queue mode, or when GUI installation isn't available:

#### For Docker Containers:

1. **Access Docker Shell**: 
   ```bash
   docker exec -it [your-n8n-container-name] sh
   ```

2. **Create nodes directory** (if it doesn't exist):
   ```bash
   mkdir -p ~/.n8n/nodes
   cd ~/.n8n/nodes
   ```

3. **Install the package**:
   ```bash
   npm install n8n-nodes-fluentc
   ```

4. **Restart n8n container**

#### For npm-based installations:

1. **Navigate to n8n nodes directory**:
   ```bash
   cd ~/.n8n/nodes
   ```
   (Create the directory if it doesn't exist: `mkdir -p ~/.n8n/nodes`)

2. **Install the package**:
   ```bash
   npm install n8n-nodes-fluentc
   ```

3. **Restart n8n**

### Method 4: Custom Docker Build

For permanent installation in a custom Docker image:

```dockerfile
FROM n8nio/n8n:latest
RUN cd ~/.n8n/ && mkdir -p nodes && cd nodes && npm install n8n-nodes-fluentc
```

## Verification

After installation, verify the nodes are available:

1. Create a new workflow
2. Click the '+' button to add a node
3. Search for "FluentC" in the node search
4. You should see:
   - **FluentC Translate** (with package icon)
   - **FluentC Check Language** (with package icon)
   - **FluentC Languages** (with package icon)

## Setup

### 1. Create FluentC API Credentials

1. In N8N, go to **Credentials** > **New**
2. Search for "FluentC API" and select it
3. Enter your FluentC API key (obtained from the FluentC sales website)
4. Test and save the credential

### 2. Using the Nodes

#### FluentC Translate Node

This node handles text and HTML translation with support for both real-time and batch modes.

**Parameters:**
- **Mode**: Choose between "Real-time" (synchronous) or "Batch" (asynchronous)
- **Input**: Text or HTML content to translate (max 100,000 bytes)
- **Input Format**: Select "Text" or "HTML"
- **Target Language**: Dropdown populated with your enabled target languages
- **Source Language**: Dropdown with your enabled source languages (optional, includes "Auto-detect")
- **Max Polling Attempts**: (Batch mode only) Maximum polling attempts for batch jobs (default: 30)

**Language Management:**
The language dropdowns are dynamically populated based on your API key's enabled languages. If you need additional languages, you'll see a link to visit www.fluentc.io to manage your language access.

**Output:**
The node returns all available data including:
- `translation`: The translated content
- `token_count`: Number of tokens used
- `source_language_detected`: Detected source language
- `model_used`: AI model used for translation
- `metadata`: Additional metadata
- `mode`: Translation mode used
- `input_format`: Input format processed
- `target_language`: Target language

#### FluentC Check Language Node

This node detects the language of input content.

**Parameters:**
- **Input**: Text or HTML content to analyze
- **Input Format**: Select "Text" or "HTML"

**Output:**
- `detected_language`: Two-letter language code of detected language
- `confidence`: Confidence score (0-1) for the detection
- `input_format`: Input format processed
- `input_length`: Length of analyzed content

#### FluentC Languages Node

This node fetches the lists of supported and source languages from your FluentC account.

**Parameters:**
This node has no parameters. It only requires a configured FluentC API credential.

**Output:**
- `supported_languages`: An array of objects, each with `code` and `name` of a language available for translation as a target.
- `source_languages`: An array of objects, each with `code` and `name` of a language available as a source for translation.

## Usage Examples

### Basic Translation Workflow

1. Add a **FluentC Translate** node to your workflow
2. Configure it with:
   - Mode: "Real-time"
   - Input: "Hello, how are you today?"
   - Input Format: "Text"
   - Target Language: Select "Spanish (es)" from dropdown
3. The output will include the Spanish translation and metadata

### Batch Translation for Large Content

1. Use **FluentC Translate** node with:
   - Mode: "Batch"
   - Input: Your large HTML or text content
   - Target Language: Your desired language code
2. The node will automatically poll until the translation is complete

### Language Detection Before Translation

1. Add a **FluentC Check Language** node first
2. Connect it to a **FluentC Translate** node
3. Use the detected language as the source language parameter

### Retrieving Language Lists

1. Add a **FluentC Languages** node to your workflow.
2. Execute the node.
3. The output will contain two arrays: `supported_languages` and `source_languages`, which you can then use in other parts of your workflow.

## Troubleshooting

### Nodes Not Appearing

If nodes don't appear after installation:

1. **Check Installation Method**: Ensure you used the correct method for your setup
2. **Restart n8n**: Always restart n8n after manual installation
3. **Check Directory**: For manual installs, verify the package is in `~/.n8n/nodes/`
4. **Check Permissions**: Ensure n8n has read permissions for the nodes directory
5. **Check Logs**: Look at n8n logs for any error messages during startup

### Permission Issues

For Docker installations, you might need to ensure proper permissions:

```bash
# Inside the container
chown -R node:node ~/.n8n/nodes
```

### Queue Mode

If you're running n8n in queue mode, you **must** use manual installation (Method 3).

## Error Handling

The plugin includes comprehensive error handling:

- **Content Size Validation**: Prevents requests exceeding 100,000 bytes
- **Batch Timeout Protection**: Limits polling attempts to prevent infinite loops  
- **API Error Handling**: Gracefully handles API errors and rate limits
- **Continue on Fail**: Option to continue workflow execution even if translation fails

## API Rate Limits

The plugin respects FluentC API rate limits and uses the recommended polling intervals returned by the batch API to avoid overwhelming the service.

## Development & Publishing

This package follows n8n community node standards:

- ✅ Package name starts with `n8n-nodes-`
- ✅ Includes `n8n-community-node-package` keyword
- ✅ No runtime dependencies (only devDependencies)
- ✅ Proper n8n configuration in package.json
- ✅ Built TypeScript with proper exports

## Support

For issues related to this N8N plugin, please check:

1. **FluentC API Documentation**: https://fluentc.ai/docs
2. **N8N Community**: https://community.n8n.io
3. **Plugin Repository**: https://github.com/FluentC/n8n-nodes-fluentc
4. **n8n Community Nodes Documentation**: https://docs.n8n.io/integrations/community-nodes/

## License

MIT License - see LICENSE file for details.

---

**Note**: You need a valid FluentC API key to use this plugin. API keys are obtained through the FluentC sales website.