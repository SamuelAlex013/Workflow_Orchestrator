# n8n-nodes-flowise

A community node for n8n that allows you to integrate with Flowise AI workflows and chatflows.

## Features

- 🤖 **Chat Operations**: Send messages to Flowise chatflows
- 📚 **Vector Store Operations**: Upsert documents to vector stores  
- 🔐 **Authentication**: Support for API key authentication
- 📝 **Session Management**: Maintain chat sessions across conversations
- 🎯 **Custom Variables**: Pass custom variables to chatflows
- 📎 **File Uploads**: Support for file uploads in chat operations
- 🔄 **Chat History**: Maintain conversation history

## Installation

### Install from npm (when published)

```bash
npm install n8n-nodes-flowise
```

### Install from source

1. Clone this repository
2. Install dependencies: `pnpm install`
3. Build the node: `pnpm build`
4. Link to your n8n installation:
   ```bash
   cd /path/to/your/n8n
   npm install /path/to/n8n-nodes-flowise
   ```

## Prerequisites

- n8n installed and running
- Flowise instance running (locally or remote)
- Node.js 20.15 or higher

## Configuration

### Credentials

1. In n8n, go to **Settings** → **Credentials**
2. Click **Add Credential** and search for "Flowise API"
3. Configure the following:
   - **Base URL**: Your Flowise instance URL (e.g., `http://localhost:3000`)
   - **API Key**: Your Flowise API key (optional, required for secured instances)

### Testing Credentials

The node includes a built-in credential test that calls the `/api/v1/version` endpoint to verify connectivity.

## Usage

### Chat Operations

#### Send Message

Send a message to a Flowise chatflow and receive a response.

**Parameters:**
- **Chatflow ID**: The ID of your Flowise chatflow
- **Message**: The message to send  
- **Session ID** (optional): Unique session identifier for conversation continuity
- **Override Config** (optional): JSON object to override chatflow configuration
- **Custom Variables** (optional): JSON object with custom variables for the chatflow
- **Chat History** (optional): Array of previous chat messages for context
- **Uploads** (optional): Files to upload with the message

**Example:**
```json
{
  "chatflowId": "your-chatflow-id",
  "message": "Hello, how can you help me?",
  "sessionId": "user-123-session",
  "overrideConfig": {
    "temperature": 0.7
  },
  "vars": {
    "userName": "John Doe",
    "context": "customer_support"
  }
}
```

### Vector Store Operations

#### Upsert Document

Add or update documents in a Flowise vector store.

**Parameters:**
- **Chatflow ID**: The ID of your Flowise chatflow with vector store
- **Document**: The document content to upsert
- **Metadata** (optional): Additional metadata for the document

## Development

### Building

```bash
pnpm install
pnpm build
```

### Testing

Run the test suite to validate the node:

```bash
node test-flowise.js
```

### Code Quality

```bash
pnpm lint          # Check for linting issues
pnpm lintfix       # Fix linting issues automatically
pnpm format        # Format code with Prettier
```

## License

MIT License - see [LICENSE.md](LICENSE.md) for details.
