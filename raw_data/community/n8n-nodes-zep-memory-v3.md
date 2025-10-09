# n8n-nodes-zep-memory-v3

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node that provides Zep v3 Memory functionality for AI agents. It replaces the discontinued official Zep Memory node with enhanced v3 features.

## Features

- **Thread-based Memory**: Uses Zep v3 thread terminology instead of sessions
- **Message Filtering**: Automatically filters out empty messages (preserves original functionality)
- **Cloud & Open Source**: Supports both Zep Cloud and self-hosted Zep instances
- **Version Compatibility**: Multiple node versions for backward compatibility
- **AI Agent Integration**: Direct integration with n8n AI Agent nodes

## Installation

To install this community node in n8n:

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-zep-memory-v3`
4. Agree to the risks of using community nodes
5. Select **Install**

After installation restart n8n to see the node in the nodes panel.

## Configuration

### Credentials

1. Create new **Zep API** credentials
2. For **Zep Cloud**:
   - Set **Cloud** to `true`
   - Enter your **API Key**
3. For **Zep Open Source**:
   - Set **Cloud** to `false`
   - Enter your **API URL** (e.g., `http://localhost:8000`)
   - Enter your **API Key** (if required)

### Node Configuration

- **Thread ID**: The unique identifier for the conversation thread
  - Can use expressions like `{{ $json.threadId }}`
  - Supports different input methods based on node version

## Usage

1. Add the **Zep Memory v3** node to your workflow
2. Connect it between your **Chat Trigger** and **AI Agent** nodes
3. Configure the **Thread ID** to identify unique conversations
4. The node will automatically:
   - Load conversation history for context
   - Save new messages after AI responses
   - Filter out empty messages

### Example Workflow

```
Chat Trigger → Zep Memory v3 → AI Agent → Response
```

## Differences from Original Node

This community node maintains **100% compatibility** with the original discontinued node while adding:

- **v3 Terminology**: Uses `threadId` instead of `sessionId`
- **Enhanced Performance**: Leverages Zep v3 improvements
- **Future-Proof**: Built for long-term maintenance

## Migration from Original Node

To migrate from the discontinued official node:

1. Install this community node
2. Replace **Zep Memory** nodes with **Zep Memory v3**
3. Update parameter names: `sessionId` → `threadId`
4. Test your workflows

## Compatibility

- **n8n version**: 0.190.0 and above
- **Node.js**: 18.10 and above
- **Zep**: Cloud v3 and Open Source <= v0.27.2

## Support

This is a community-maintained node. For issues:

1. Check the [GitHub Issues](https://github.com/fabiohsan/n8n-nodes-zep-memory-v3/issues)
2. Create a new issue with detailed information
3. Community support via n8n Discord

## License

[MIT](https://github.com/fabiohsan/n8n-nodes-zep-memory-v3/blob/main/LICENSE.md)

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Zep Documentation](https://docs.getzep.com)
- [n8n Documentation](https://docs.n8n.io)