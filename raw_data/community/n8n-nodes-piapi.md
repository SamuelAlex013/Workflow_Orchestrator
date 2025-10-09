# n8n-nodes-piapi

This is a **community-maintained** n8n node package that enables seamless integration with [PiAPI](https://piapi.ai/workspace?via=valics) - a centralized hub for generative AI APIs. This package allows you to leverage advanced AI capabilities directly in your n8n workflows.

> **Note**: This is an unofficial community project and is not developed or maintained by the PiAPI team.

## About PiAPI

PiAPI provides easy access to cutting-edge generative AI APIs for:
- Image generation (Midjourney, Flux)
- Video generation (Luma Dream Machine, Kling, Hailuo, WanX, Hunyuan)
- Music and audio generation
- Face swapping
- 3D model generation
- Large Language Models
- And much more!

## Features

This n8n package includes nodes for:

### 🎨 Image Generation & Manipulation
- **Flux** - Text to Image, Image to Image
- **Midjourney** - Advanced image generation
- **LLM (GPT-4o)** - Text to Image, Image to Image with natural language
- **Image Upscale** - Enhance image resolution
- **Remove Background** - Automatic background removal
- **Qubico Segment** - Advanced image segmentation

### 🎬 Video Generation & Editing
- **Dream Machine** - Text to Video, Image to Video, Video Extension
- **Kling** - Text to Video, Image to Video, Video Extension, Lip Sync, Effects, Virtual Try-On
- **Hailuo** - Text to Video, Image to Video, Subject Video (with Director Mode camera controls)
- **WanX** - Text to Video, Image to Video
- **Hunyuan** - Text to Video, Image to Video
- **Skyreels** - Image to Video
- **Video Upscale** - Enhance video resolution

### 🎵 Audio Generation
- **MMAudio** - Video to Audio generation
- **DiffRhythm** - Audio generation
- **Text to Speech** - Convert text to natural speech

### 🎭 Face & Character
- **Faceswap** - Image to Image, Video to Video (single and multi-face with index control)
- **Kling Lip Sync** - Synchronize lip movements
- **Kling Try-On** - Virtual clothing try-on

### 🎲 3D Generation
- **Trellis** - 3D model generation

### 🔧 Utilities
- **Task Status** - Check status of async operations
- **File Upload** - Temporary file storage

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Install
```bash
# In n8n
# Go to Settings > Community Nodes
# Install: n8n-nodes-piapi
```

## Credentials

You'll need an API key from [PiAPI](https://piapi.ai/workspace?via=valics):
1. Sign up at [piapi.ai](https://piapi.ai/workspace?via=valics)
2. Get your API key from the dashboard
3. Add the API key to the PiAPI credentials in n8n

## Usage

1. Add any PiAPI node to your workflow
2. Configure your PiAPI credentials
3. Select the operation you want to perform
4. Configure the node parameters
5. Execute your workflow

### Example: Text to Image with Flux
1. Add a "Flux Text to Image" node
2. Enter your prompt
3. Select model and parameters
4. Execute to generate your image

### Example: Director Mode with Hailuo
Use camera controls in your prompts:
```
[Push in, Pan right] A majestic eagle soaring through clouds
[Zoom out, Tilt up] City skyline at sunset
```

## Compatibility

- n8n version: 1.80.0 and above
- Node.js: 18.10 or higher

## Support

- **Issues**: [GitHub Issues](https://github.com/lvalics/n8n-nodes-piapi/issues)
- **PiAPI Documentation**: [PiAPI Docs](https://piapi.ai/docs)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](https://github.com/lvalics/n8n-nodes-piapi/blob/master/LICENSE.md)

## Disclaimer

This is an unofficial community node package and is not affiliated with, officially maintained, or endorsed by PiAPI. Use at your own discretion.