# 🚀 Auggie CLI for n8n

**Bring the power of Auggie CLI directly into your n8n automation workflows!**

Imagine having an AI coding assistant that can analyze your codebase, fix bugs, write new features, manage databases, interact with APIs, and automate your entire development workflow - all within n8n. That's exactly what this node enables.

[![npm version](https://badge.fury.io/js/n8n-nodes-auggie-cli.svg)](https://badge.fury.io/js/n8n-nodes-auggie-cli)
[![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-auggie-cli.svg)](https://npmjs.com/package/n8n-nodes-auggie-cli)
[![GitHub stars](https://img.shields.io/github/stars/bottazzo/n8n-nodes-auggie-cli.svg)](https://github.com/bottazzo/n8n-nodes-auggie-cli/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n](https://img.shields.io/badge/n8n-community_node-orange.svg)](https://n8n.io/)
[![Auggie CLI](https://img.shields.io/badge/Auggie%20CLI-Powered-blue.svg)](https://docs.augmentcode.com/cli/overview)
[![npm](https://img.shields.io/npm/v/n8n-nodes-auggie-cli.svg)](https://www.npmjs.com/package/n8n-nodes-auggie-cli)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

## 🌟 What Can You Build?

### 🔧 **Automated Code Reviews**
Create workflows that automatically review pull requests, suggest improvements, and even fix issues before merging.

### 🐛 **Intelligent Bug Fixing**
Connect error monitoring tools to Auggie CLI - automatically diagnose and fix production issues in real-time.

### 📊 **Database Management**
Let Auggie CLI write complex SQL queries, optimize database schemas, and generate migration scripts based on your requirements.

### 🤖 **Self-Improving Workflows**
Build n8n workflows that can modify and improve themselves using Auggie CLI's capabilities.

### 📝 **Documentation Generation**
Automatically generate and update documentation for your entire codebase, APIs, or databases.

### 🔄 **Code Migration**
Automate the migration of legacy codebases to modern frameworks with intelligent refactoring.

### 🎫 **Customer Support Automation**
Transform support tickets into code fixes automatically:
- Analyze customer bug reports and reproduce issues
- Generate fixes for reported problems
- Create test cases to prevent regression
- Update documentation based on common questions
- Auto-respond with workarounds while fixes are deployed

## ⚡ Quick Start

### Prerequisites
1. **Auggie CLI** (required on your n8n server):
   ```bash
   npm install -g @augmentcode/auggie
   auggie login  # Authenticate with your Augment account
   ```

### Install in n8n

#### Option 1: Via n8n UI (Recommended)
1. Open your n8n instance
2. Go to **Settings** → **Community Nodes**
3. Click **Install a community node**
4. Enter: `n8n-nodes-auggie-cli`
5. Click **Install**
6. Restart n8n when prompted

#### Option 2: Manual Installation
```bash
cd ~/.n8n/nodes
npm install n8n-nodes-auggie-cli
# Restart n8n
```

#### Option 3: Docker
```bash
docker run -it --rm \
  -p 5678:5678 \
  -e N8N_COMMUNITY_NODE_PACKAGES=n8n-nodes-auggie-cli \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

**Note**: For Docker, you'll need to ensure Auggie CLI is installed inside the container. Consider creating a custom Dockerfile.

## 🎯 Real-World Use Cases

### 1. **GitHub Issue to Code**
```
Webhook (GitHub Issue) → Auggie CLI → Create PR → Notify Slack
```
Automatically implement features or fix bugs when issues are created.

### 2. **Database Query Builder**
```
Form Trigger → Auggie CLI → Execute Query → Send Results
```
Natural language to SQL - let non-technical users query databases safely.

### 3. **Code Quality Guardian**
```
Git Push → Auggie CLI → Analyze Code → Block/Approve → Notify
```
Enforce coding standards and catch issues before they reach production.

### 4. **API Integration Builder**
```
HTTP Request → Auggie CLI → Generate Integration → Test → Deploy
```
Automatically create integrations with third-party APIs.

### 5. **Intelligent Log Analysis**
```
Error Logs → Auggie CLI → Diagnose → Create Fix → Open PR
```
Turn error logs into actionable fixes automatically.

### 6. **Customer Support to Code Fix**
```
Support Ticket → Auggie CLI → Reproduce Issue → Generate Fix → Test → Deploy → Auto-Reply
```
Transform customer complaints into deployed fixes in minutes, not days.

## 🛠️ Powerful Features

### **Project Context Awareness**
Set a project path and Auggie CLI understands your entire codebase context:
- Analyzes existing code patterns
- Follows your coding standards
- Understands your architecture
- Respects your dependencies

### **AI Model Selection**
Choose the best AI model for your specific task:
- **Claude Sonnet 4.5**: Latest and most capable model by Anthropic (default)
- **Claude Sonnet 4**: Powerful reasoning and code understanding
- **GPT-5**: Latest OpenAI model with advanced capabilities

### **Multiple Output Modes**
- **Print**: Execute once and return output (perfect for automation)
- **Quiet**: Only return final output without intermediate steps
- **Compact**: Tool calls, results, and responses as one line each

### **Advanced Configuration**
Fine-tune Auggie CLI's behavior with these powerful options:
- 🔧 **Custom Arguments**: Pass additional CLI arguments
- 🚫 **Debug Mode**: Enable detailed logging for troubleshooting
- ⏱️ **Timeout Control**: Set maximum execution time
- 📁 **Project Path**: Specify working directory for context

## 📋 Configuration Examples

### Simple Code Analysis
```javascript
{
  "operation": "execute",
  "prompt": "Analyze this codebase and suggest performance improvements",
  "projectPath": "/path/to/your/project",
  "outputMode": "print"
}
```

### Advanced Database Operations
```javascript
{
  "operation": "execute",
  "prompt": "Create an optimized query to find users who haven't logged in for 30 days",
  "projectPath": "/path/to/project",
  "outputMode": "quiet"
}
```

### Customer Support Automation
```javascript
{
  "operation": "execute",
  "prompt": "Customer reports: 'Login button not working on mobile devices'\n\nAnalyze this issue, find the root cause, and create a fix",
  "projectPath": "/path/to/web-app",
  "outputMode": "print",
  "additionalOptions": {
    "debug": true,
    "customArgs": "--verbose"
  }
}
```

## 🔄 Workflow Patterns

### Pattern 1: Continuous Code Improvement
```
Schedule Trigger (Daily)
  ↓
Auggie CLI (Analyze codebase for improvements)
  ↓
Create GitHub Issues
  ↓
Assign to Team
```

### Pattern 2: Natural Language to Code
```
Slack Command
  ↓
Auggie CLI (Generate code from description)
  ↓
Create Pull Request
  ↓
Run Tests
  ↓
Notify Results
```

### Pattern 3: Intelligent Monitoring
```
Error Webhook
  ↓
Auggie CLI (Diagnose issue)
  ↓
If (Can fix automatically)
  ├─ Yes: Create Fix PR
  └─ No: Create Detailed Issue
```

## 🚦 Getting Started

### 1. **Verify Prerequisites**
Make sure Auggie CLI is installed and authenticated on your n8n server:
```bash
auggie --version  # Should show the version
```

If not installed, see the [Quick Start](#-quick-start) section above.

### 2. **Create Your First Workflow**
1. In n8n, create a new workflow
2. Add a **Manual Trigger** node (for testing)
3. Add the **Auggie CLI** node
4. Configure:
   - **Operation**: Execute
   - **Prompt**: "Analyze the code in this directory and suggest improvements"
   - **Project Path**: `/path/to/your/project`
   - **Output Mode**: Print (for automation) or Interactive (for manual use)
5. Click **Execute Workflow**
6. Watch Auggie CLI analyze your project!

### 3. **Explore Advanced Features**
- Try different output modes for different use cases
- Use project paths for better context and results
- Enable debug mode for troubleshooting
- Chain multiple Auggie CLI operations for complex workflows

## 💡 Pro Tips

### 🎯 **Use Project Paths**
Always set a project path for better context and results:
```
/home/user/projects/my-app
```

### 🔗 **Chain Operations**
Use multiple Auggie CLI nodes to build complex multi-step workflows while maintaining context.

### 📊 **Output Modes**
- **Print**: For automation and chaining with other nodes
- **Quiet**: For clean, final results without intermediate steps
- **Interactive**: For manual debugging and exploration

## 🤝 Community & Support

- 📖 [Auggie CLI Documentation](https://docs.augmentcode.com/cli/overview)
- 🐛 [Report Issues](https://github.com/yourusername/n8n-nodes-auggie-cli/issues)
- 💬 [Discussions](https://github.com/yourusername/n8n-nodes-auggie-cli/discussions)
- 🌟 [Star on GitHub](https://github.com/yourusername/n8n-nodes-auggie-cli)

## 📄 License

MIT - Build amazing things!

---

**Ready to revolutionize your development workflow?** Install Auggie CLI for n8n today and join the future of automated software development!
