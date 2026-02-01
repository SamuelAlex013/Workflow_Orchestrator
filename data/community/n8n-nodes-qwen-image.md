# n8n-nodes-qwen-image

🎨 **Dual-Purpose Image Generation Package**: Use as both an n8n community node and an AI tool for generating high-quality images using Qwen Image model from ModelScope.

## ✨ Features

- 🔄 **Dual Functionality**: Works as both n8n node and AI tool calling interface
- 🎨 **High-Quality Image Generation**: Powered by Qwen Image model from ModelScope
- 📝 **Flexible Prompting**: Support for positive and negative prompts
- 📐 **Multiple Sizes**: Configurable image dimensions (1024x1024, 720x1280, 1280x720)
- ⚙️ **Advanced Controls**: Seed, steps, CFG scale parameters
- 🔄 **Smart Polling**: Automatic task status checking with configurable intervals
- 🛡️ **Robust Error Handling**: Built-in retry mechanisms and comprehensive error handling
- 🔌 **AI Framework Compatible**: Supports OpenAI Functions, LangChain, and other AI frameworks

## 📦 Installation

### For n8n Usage

#### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-qwen-image`
4. Agree to the risks of using community nodes
5. Select **Install**

After installation, restart n8n to see the new nodes.

#### Manual Installation

```bash
npm install n8n-nodes-qwen-image
```

For Docker deployments:

```dockerfile
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-qwen-image
```

### For AI Tool Usage

```bash
npm install n8n-nodes-qwen-image
```

## 🚀 Usage

### 🔧 As n8n Node

1. Add the **Qwen Image** node to your workflow
2. Configure API credentials (ModelScope API key)
3. Set generation parameters
4. Connect to other nodes in your workflow

#### Example n8n Workflow

```json
{
  "nodes": [
    {
      "name": "Generate Image",
      "type": "n8n-nodes-qwen-image.qwenImage",
      "parameters": {
        "prompt": "A serene mountain landscape at sunset, digital art",
        "negativePrompt": "blurry, low quality, distorted",
        "size": "1024x1024",
        "steps": 25,
        "cfgScale": 7.5
      }
    }
  ]
}
```

### 🤖 As AI Tool

#### Basic Usage

```typescript
import { createQwenImageTool, generateImage } from 'n8n-nodes-qwen-image';

// Method 1: Using tool instance
const tool = createQwenImageTool({
  apiKey: 'your-modelscope-api-key',
  baseUrl: 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
});

const result = await tool.call({
  prompt: 'A beautiful sunset over mountains',
  size: '1024x1024',
  steps: 20
});

console.log(result);
// {
//   success: true,
//   data: {
//     task_id: 'xxx',
//     status: 'SUCCEEDED',
//     image_url: 'https://...',
//     prompt: 'A beautiful sunset over mountains',
//     ...
//   }
// }

// Method 2: Direct function call
const quickResult = await generateImage(
  { apiKey: 'your-api-key', baseUrl: 'https://...' },
  'A cyberpunk cityscape at night',
  { size: '1280x720', steps: 30 }
);
```

#### OpenAI Functions Integration

```typescript
import { QWEN_IMAGE_TOOL_FUNCTION, createQwenImageTool } from 'n8n-nodes-qwen-image';
import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: 'your-openai-key' });
const qwenTool = createQwenImageTool({ apiKey: 'your-modelscope-key' });

const response = await openai.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Generate an image of a sunset' }],
  tools: [{ type: 'function', function: QWEN_IMAGE_TOOL_FUNCTION }],
  tool_choice: 'auto'
});

// Handle tool calls
if (response.choices[0].message.tool_calls) {
  for (const toolCall of response.choices[0].message.tool_calls) {
    if (toolCall.function.name === 'generate_qwen_image') {
      const args = JSON.parse(toolCall.function.arguments);
      const result = await qwenTool.call(args);
      console.log('Generated image:', result);
    }
  }
}
```

#### LangChain Integration

```typescript
import { QwenImageTool, QWEN_IMAGE_TOOL_FUNCTION } from 'n8n-nodes-qwen-image';
import { DynamicTool } from 'langchain/tools';

const qwenImageTool = new DynamicTool({
  name: QWEN_IMAGE_TOOL_FUNCTION.name,
  description: QWEN_IMAGE_TOOL_FUNCTION.description,
  func: async (input: string) => {
    const tool = new QwenImageTool({ apiKey: 'your-api-key' });
    const args = JSON.parse(input);
    const result = await tool.call(args);
    return JSON.stringify(result);
  }
});

// Use with LangChain agents
const tools = [qwenImageTool];
// ... rest of your LangChain setup
```

## ⚙️ Configuration

### API Credentials

You need ModelScope API credentials:

1. **API Key**: Your ModelScope API key (required)
2. **Base URL**: API endpoint (optional, has default)

### Getting ModelScope API Key

1. Visit [ModelScope](https://modelscope.cn/)
2. Sign up or log in
3. Go to profile settings
4. Generate an API key
5. Copy for use in your application

## 📋 Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | ✅ | - | Text description of the image to generate |
| `negative_prompt` | string | ❌ | - | What to avoid in the image |
| `size` | string | ❌ | '1024x1024' | Image dimensions (1024x1024, 720x1280, 1280x720) |
| `seed` | integer | ❌ | -1 | Random seed for reproducible results (-1 for random) |
| `steps` | integer | ❌ | 20 | Denoising steps (1-50) |
| `cfg_scale` | number | ❌ | 7 | Classifier-free guidance scale (1-20) |
| `polling_interval` | integer | ❌ | 5 | Time between status checks (1-60 seconds) |
| `max_polling_time` | integer | ❌ | 300 | Maximum wait time (60-1800 seconds) |

## 📤 Output

### n8n Node Output

```json
{
  "taskId": "unique-task-identifier",
  "status": "SUCCEEDED",
  "imageUrl": "https://generated-image-url",
  "imageData": "base64-encoded-image-data",
  "metadata": {
    "prompt": "original-prompt",
    "size": "1024x1024",
    "steps": 20,
    "cfgScale": 7
  }
}
```

### AI Tool Output

```typescript
interface ToolCallResult {
  success: boolean;
  data?: {
    task_id: string;
    status: string;
    image_url: string;
    prompt: string;
    negative_prompt?: string;
    size: string;
    seed: number;
    steps: number;
    cfg_scale: number;
    metadata: any;
  };
  error?: string;
}
```

## 🔧 Advanced Usage

### Custom Configuration

```typescript
import { QwenImageAPI } from 'n8n-nodes-qwen-image/core';

// Direct API usage
const api = new QwenImageAPI({
  apiKey: 'your-key',
  baseUrl: 'custom-endpoint'
});

const result = await api.generateImage(
  {
    prompt: 'A futuristic robot',
    size: '1024x1024',
    steps: 30,
    cfgScale: 8
  },
  {
    pollingInterval: 3,
    maxPollingTime: 600
  }
);
```

### Tool Metadata

```typescript
import { QWEN_IMAGE_TOOL_METADATA } from 'n8n-nodes-qwen-image';

console.log(QWEN_IMAGE_TOOL_METADATA);
// {
//   name: 'qwen-image-generator',
//   version: '2.0.0',
//   description: 'AI tool for generating images using Qwen Image model',
//   capabilities: ['text-to-image', 'negative-prompting', ...],
//   supported_sizes: ['1024x1024', '720x1280', '1280x720'],
//   ...
// }
```

## 🛠️ Error Handling

Both n8n node and AI tool include comprehensive error handling:

- ✅ API authentication errors
- ✅ Network connectivity issues
- ✅ Task timeout scenarios
- ✅ Invalid parameter validation
- ✅ Rate limiting responses
- ✅ Malformed API responses

### Error Examples

```typescript
// AI Tool error handling
const result = await tool.call({ prompt: '' }); // Invalid prompt
console.log(result);
// {
//   success: false,
//   error: 'Missing or invalid prompt parameter'
// }

// API error handling
try {
  const result = await api.generateImage(params, options);
} catch (error) {
  console.error('Generation failed:', error.message);
}
```

## 🔍 Troubleshooting

### Common Issues

1. **Authentication Failed**
   - ✅ Verify API key is correct
   - ✅ Check ModelScope account credits
   - ✅ Ensure API key has proper permissions

2. **Task Timeout**
   - ✅ Increase `max_polling_time` parameter
   - ✅ Check ModelScope service status
   - ✅ Try with simpler prompts

3. **Invalid Parameters**
   - ✅ Ensure prompt is not empty
   - ✅ Verify size is supported (1024x1024, 720x1280, 1280x720)
   - ✅ Check numeric parameters are within valid ranges

4. **Import Issues**
   - ✅ Ensure package is properly installed
   - ✅ Check TypeScript configuration
   - ✅ Verify import paths are correct

## 📚 API Reference

### Core Classes

- `QwenImageAPI`: Core API client
- `QwenImageTool`: AI tool wrapper
- `QwenImage`: n8n node implementation

### Utility Functions

- `createQwenImageTool(config)`: Create tool instance
- `generateImage(config, prompt, options)`: Quick generation

### Constants

- `QWEN_IMAGE_TOOL_FUNCTION`: OpenAI Functions schema
- `QWEN_IMAGE_TOOL_METADATA`: Tool metadata
- `VERSION`: Package version

## 📄 License

[MIT](https://github.com/xwang152-jack/n8n-nodes-qwen-image/blob/main/LICENSE)

## 🤝 Support

If you have any issues or questions:

- 🐛 [Open an issue](https://github.com/xwang152-jack/n8n-nodes-qwen-image/issues) on GitHub
- 💬 Join our community discussions
- 📧 Contact the maintainer

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for details about changes in each version.

## 🏷️ Version 2.0.0

**New in v2.0.0:**
- ✨ Dual-purpose functionality (n8n node + AI tool)
- 🔌 OpenAI Functions compatibility
- 🦜 LangChain integration support
- 🏗️ Improved architecture with core API separation
- 📚 Enhanced documentation and examples
- 🛡️ Better error handling and validation
- 📦 Modern package structure with proper exports

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Operations](#operations)
- [Credentials](#credentials)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Compatibility](#compatibility)
- [Contributing](#contributing)
- [Resources](#resources)  

## 🚀 Installation

### Method 1: Via n8n Community Nodes (Recommended)

1. Open your n8n instance
2. Go to **Settings** → **Community Nodes**
3. Click **Install a community node**
4. Enter the package name: `n8n-nodes-qwen-image`
5. Click **Install**
6. Restart your n8n instance

### Method 2: Via npm (Self-hosted)

```bash
# Navigate to your n8n installation directory
cd ~/.n8n

# Install the community node
npm install n8n-nodes-qwen-image

# Restart n8n
n8n start
```

### Method 3: Docker

If you're using n8n with Docker, add the package to your Dockerfile:

```dockerfile
FROM n8nio/n8n
USER root
RUN npm install -g n8n-nodes-qwen-image
USER node
```

For more detailed installation instructions, follow the [official n8n community nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/).

## ⚡ Quick Start

1. **Install the node** using one of the methods above
2. **Get your ModelScope API key** from [ModelScope Console](https://www.modelscope.cn/)
3. **Create credentials** in n8n (Settings → Credentials → Add Credential → ModelScope API)
4. **Add the Qwen Image node** to your workflow
5. **Configure and execute** your first image generation!

## 🛠️ Operations

### Generate Image

The primary operation allows you to create stunning images from text descriptions with extensive customization options:

#### Core Parameters
- **Prompt** (required): Detailed text description of the image you want to generate
- **Image Size**: Choose from multiple aspect ratios:
  - `1024x1024` - Square format (default)
  - `720x1280` - Portrait format
  - `1280x720` - Landscape format

#### Advanced Parameters
- **Negative Prompt**: Specify what you don't want in the image
- **Seed**: Set a specific seed for reproducible results (optional)
- **Steps**: Number of inference steps (1-50, default: 20)
- **CFG Scale**: Classifier-free guidance scale (1-20, default: 7)
- **Poll Interval**: How often to check task status in seconds (default: 5)
- **Max Poll Attempts**: Maximum polling attempts before timeout (default: 60)

## 🔐 Credentials

### Setting up ModelScope API Credentials

#### Step 1: Get Your API Key
1. Visit [ModelScope](https://www.modelscope.cn/) and create an account
2. Navigate to your [API Keys page](https://www.modelscope.cn/my/myaccesstoken)
3. Generate a new API key or copy your existing one

#### Step 2: Configure in n8n
1. In your n8n instance, go to **Settings** → **Credentials**
2. Click **Add Credential**
3. Search for and select **"ModelScope API"**
4. Enter your API key in the **API Key** field
5. Test the connection and save

#### Security Notes
- Keep your API key secure and never share it publicly
- Use environment variables for production deployments
- Regularly rotate your API keys for enhanced security

## ⚙️ Configuration

### Environment Variables (Optional)

For production deployments, you can set environment variables:

```bash
# ModelScope API Configuration
MODELSCOPE_API_KEY=your_api_key_here
MODELSCOPE_API_URL=https://api-inference.modelscope.cn
```

## 🔄 Compatibility

| Component | Version Requirement |
|-----------|--------------------|
| **n8n** | >= 1.0.0 |
| **Node.js** | >= 18.0.0 |
| **npm** | >= 8.0.0 |

### Tested Versions
- ✅ n8n 1.32.2+
- ✅ Node.js 18.x, 20.x, 22.x
- ✅ npm 8.x, 9.x, 10.x

### Platform Support
- ✅ Linux (Ubuntu, CentOS, Alpine)
- ✅ macOS (Intel & Apple Silicon)
- ✅ Windows 10/11
- ✅ Docker containers

## 📖 Usage Examples

### Example 1: Basic Image Generation

```json
{
  "prompt": "A majestic dragon flying over a medieval castle at sunset, fantasy art style",
  "imageSize": "1024x1024",
  "steps": 20,
  "cfgScale": 7
}
```

### Example 2: Advanced Configuration with Negative Prompts

```json
{
  "prompt": "Professional headshot of a business person, clean background, high quality",
  "negativePrompt": "blurry, low quality, distorted, cartoon, anime",
  "imageSize": "720x1280",
  "seed": 12345,
  "steps": 30,
  "cfgScale": 8
}
```

### Example 3: Batch Image Generation Workflow

1. **HTTP Request Node**: Fetch prompts from an API
2. **Code Node**: Process and format the prompts
3. **Qwen Image Node**: Generate images for each prompt
4. **Google Drive Node**: Save generated images to cloud storage

### Example 4: Content Creation Pipeline

1. **Webhook Node**: Receive content requests
2. **OpenAI Node**: Generate image descriptions
3. **Qwen Image Node**: Create images from descriptions
4. **Slack Node**: Send results to team channel

### Pro Tips

- **Detailed Prompts**: More specific prompts yield better results
- **Negative Prompts**: Use to avoid unwanted elements
- **Seed Values**: Use the same seed for consistent results
- **Aspect Ratios**: Choose based on your intended use case

## 🔧 Troubleshooting

### Common Issues

#### "Authentication Failed"
- ✅ Verify your ModelScope API key is correct
- ✅ Check if your API key has sufficient permissions
- ✅ Ensure the credential is properly configured in n8n

#### "Task Timeout"
- ✅ Increase the `maxPollAttempts` parameter
- ✅ Check ModelScope service status
- ✅ Try with a simpler prompt

#### "Invalid Image Size"
- ✅ Use only supported sizes: `1024x1024`, `720x1280`, `1280x720`
- ✅ Check for typos in the imageSize parameter

#### "Rate Limit Exceeded"
- ✅ Implement delays between requests
- ✅ Check your ModelScope API quota
- ✅ Consider upgrading your ModelScope plan

### Debug Mode

Enable debug logging in n8n to see detailed request/response information:

```bash
N8N_LOG_LEVEL=debug n8n start
```

### Getting Help

- 📖 Check the [ModelScope API Documentation](https://www.modelscope.cn/docs/)
- 💬 Join the [n8n Community](https://community.n8n.io/)
- 🐛 Report issues on [GitHub](https://github.com/your-username/n8n-nodes-qwen-image/issues)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-username/n8n-nodes-qwen-image.git
cd n8n-nodes-qwen-image

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint

# Run tests
npm test
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Code Standards

- Follow TypeScript best practices
- Maintain test coverage above 80%
- Use ESLint configuration provided
- Write clear commit messages
- Update documentation for new features

### Reporting Issues

When reporting issues, please include:
- n8n version
- Node.js version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs

## 📚 Resources

### Official Documentation
- 📖 [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- 🔧 [ModelScope API Documentation](https://www.modelscope.cn/docs/)
- 🚀 [ModelScope Inference API](https://api-inference.modelscope.cn/)
- 💡 [n8n Node Development Guide](https://docs.n8n.io/integrations/creating-nodes/)

### Community & Support
- 💬 [n8n Community Forum](https://community.n8n.io/)
- 💭 [n8n Discord Server](https://discord.gg/n8n)
- 🐛 [Report Issues](https://github.com/your-username/n8n-nodes-qwen-image/issues)
- 📧 [Contact Support](mailto:support@example.com)

### Related Projects
- 🎨 [Qwen Image Model](https://www.modelscope.cn/models/qwen/Qwen-VL)
- 🤖 [Other n8n AI Nodes](https://www.npmjs.com/search?q=n8n-nodes-ai)
- 🔗 [ModelScope Community](https://www.modelscope.cn/community)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the [n8n team](https://n8n.io/) for creating an amazing automation platform
- Thanks to [Alibaba Cloud](https://www.alibabacloud.com/) for the Qwen Image model
- Thanks to the [ModelScope](https://www.modelscope.cn/) team for providing the API
- Thanks to all contributors who help improve this project

---

<div align="center">
  <strong>Made with ❤️ for the n8n community</strong>
</div>
