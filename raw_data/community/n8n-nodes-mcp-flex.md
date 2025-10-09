# n8n-nodes-mcp-flex

Enhanced n8n community node for **Model Context Protocol (MCP)** with **flexible parameter handling** and improved **AI Agent integration**.

## 🚀 What's New in MCP Flex

### ✨ Key Features

- **🔧 Flexible Parameter Modes**: Choose between JSON string (backward compatible) or individual fields (user-friendly)
- **🤖 Enhanced AI Agent Integration**: Optimized for use with n8n AI Agents
- **🔄 Backward Compatible**: All existing workflows continue to work unchanged
- **📝 Individual Parameter Fields**: No more JSON editing - configure parameters in separate fields
- **⚡ Auto Mode**: Intelligent fallback from individual fields to JSON string

### 🆚 Original vs. Flex

| Feature | Original MCP Client | MCP Client Flex |
|---------|-------------------|-----------------|
| Parameter Input | JSON string only | JSON + Individual fields + Auto mode |
| Calendar Events | `{"calendar_href":"/path/","summary":"{{$json.title}}"}` | Separate fields: Calendar Href, Summary, etc. |
| Error Prone | ❌ JSON syntax errors | ✅ Individual fields prevent errors |
| AI Agent Ready | ✅ Basic support | ✅ Enhanced integration |
| Backward Compatible | - | ✅ 100% compatible |

## 📦 Installation

1. **Install the node package:**
   ```bash
   npm install n8n-nodes-mcp-flex
   ```

2. **Enable community nodes as tools** (for AI Agents):
   ```bash
   export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
   ```

3. **Restart n8n**

## 🔧 Configuration

### Parameter Modes

#### 1. **JSON String (Original)** - Backward Compatible
```json
{
  "calendar_href": "/calendars/admin/personal/",
  "summary": "{{$json.event_title}}",
  "start_datetime": "{{$json.time_from}}",
  "end_datetime": "{{$json.time_until}}"
}
```

#### 2. **Individual Fields** - User Friendly
- **Calendar Href**: `/calendars/admin/personal/`
- **Summary**: `{{$json.event_title}}`
- **Start DateTime**: `{{$json.time_from}}`
- **End DateTime**: `{{$json.time_until}}`
- **Description**: `{{$json.description}}` (optional)

#### 3. **Auto Mode** - Best of Both Worlds
- Uses individual fields if any are filled
- Falls back to JSON string if individual fields are empty
- Perfect for mixed workflows

### Common Parameter Fields

#### 📅 Calendar/Event Operations
- `calendar_href` - Calendar path
- `summary` - Event title/summary  
- `start_datetime` - Start date/time
- `end_datetime` - End date/time
- `description` - Event description

#### 🔍 Search Operations
- `query` - Search query text

#### 📁 File Operations  
- `file_path` - Path to file

#### ⚙️ Custom Parameters
- `Custom Parameter 1-3` - Format: `key:value`

## 🎯 Use Cases

### Voice Calendar Management
```
Voice Input → AI Agent → MCP Client Flex → Nextcloud Calendar
```

**Individual Fields Mode:**
- Calendar Href: `/calendars/admin/personal/` 
- Summary: `{{$json.event_titel}}`
- Start DateTime: `{{$json.time_from}}`
- End DateTime: `{{$json.time_until}}`

### AI Agent Integration
The node automatically appears as a tool in AI Agent nodes when `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true` is set.

## 📋 Operations

- **Execute Tool** - Run MCP tools with flexible parameters
- **List Tools** - Get available tools from MCP server  
- **List Resources** - Get available resources
- **Read Resource** - Read specific resource by URI
- **List Prompts** - Get available prompts
- **Get Prompt** - Retrieve specific prompt

## 🔗 Credentials

Supports all original MCP Client credential types:

### Command Line (STDIO)
- **Command**: `npx`
- **Arguments**: `-y @modelcontextprotocol/server-brave-search`  
- **Environment Variables**: `BRAVE_API_KEY=your-key-here`

### Server-Sent Events (SSE)
- **SSE URL**: `http://localhost:3001/sse`
- **Additional Headers**: Optional authentication headers

### HTTP Streamable (Recommended)
- **Streamable URL**: `http://localhost:3001/stream`
- **Additional Headers**: Optional authentication headers

## 🛠️ Example: Voice Calendar Workflow

### Before (Original MCP Client)
```
Voice → Transcribe → AI Agent → TextParser → Switch → MCP Client → Nextcloud
```
**Hard-coded JSON**: `{"calendar_href":"/calendars/admin/personal/","summary":"{{$json.event_titel}}"}`

### After (MCP Client Flex)  
```
Voice → AI Agent (with MCP Tool) → Nextcloud
```
**Individual Fields**: Easy configuration, no JSON errors, faster execution

## 🔒 Security

- ✅ No credentials in code
- ✅ Uses n8n's secure credential system
- ✅ All sensitive data stays in your n8n instance
- ✅ Standard n8n security patterns

## 🐛 Troubleshooting

### "Tool not available in AI Agent"
Make sure `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true` is set and n8n is restarted.

### "Invalid JSON in toolParameters"  
Switch to "Individual Fields" or "Auto" mode to avoid JSON syntax errors.

### "No parameters provided"
In "Individual Fields" mode, at least one parameter field must be filled.

## 🚀 Migration from Original

Your existing workflows will continue to work without changes. To benefit from new features:

1. **Keep existing workflows** - They work as-is
2. **New workflows** - Use "Individual Fields" or "Auto" mode  
3. **AI Agents** - Will automatically use the enhanced version

## 🤝 Contributing

Based on the excellent work by [nerding-io/n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp).

### Development

```bash
git clone https://github.com/Thornbeard65/n8n-nodes-mcp-flex.git
cd n8n-nodes-mcp-flex
npm install
npm run build
```

## 📄 License

MIT License - Same as original MCP Client node.

## 🙏 Credits

- Original MCP Client: [Jd Fiscus](https://github.com/nerding-io)
- MCP Protocol: [Anthropic](https://github.com/modelcontextprotocol)
- n8n: [n8n.io](https://n8n.io)

---

**Ready to make your MCP workflows more flexible!** 🎯
