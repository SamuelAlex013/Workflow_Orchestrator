# n8n-nodes-recraft-v3

![npm version](https://img.shields.io/npm/v/n8n-nodes-recraft-v3)
![License](https://img.shields.io/npm/l/n8n-nodes-recraft-v3)
![Downloads](https://img.shields.io/npm/dt/n8n-nodes-recraft-v3)

> **⚠️ Disclaimer**: This is an **unofficial community node** created for testing and educational purposes using Claude Sonnet 4. While built following n8n best practices and thoroughly tested, this node is **not officially supported by Recraft AI or n8n**. Use at your own discretion and always test thoroughly in non-production environments first.

This is an n8n community node for the **Recraft v3 AI image generation and editing API** - the #1 ranked text-to-image model on Hugging Face's benchmark.

## 🏆 Why Recraft v3?

Recraft V3 secured #1 place on Hugging Face's Text-to-Image Model Leaderboard with an ELO rating of 1172, outperforming Midjourney, OpenAI DALL-E, and all other major image generation models.

## ✨ Features (v1.1.4 - Complete API Coverage)

### 🎨 **Image Generation** 
- **Text-to-Image**: Generate stunning images from text prompts (up to 1000 bytes)
- **Multiple Images**: Generate 1-6 images per request
- **Vector & Raster**: Support for both vector and raster image generation
- **Multiple Styles**: Realistic images, digital illustrations, vector illustrations, and icons
- **Sub-styles**: 25+ sub-styles including hand drawn, pixel art, cartoon, anime, 3D render, and more
- **Custom Styles**: Create and use custom brand styles from reference images
- **Negative Prompts**: Specify what you DON'T want in images
- **Advanced Controls**: Color control, background color, artistic level, and text positioning

### 🛠️ **Image Editing**
- **Image-to-Image**: Transform existing images based on prompts with strength control
- **Inpainting**: Replace specific parts of images using masks
- **Background Operations**: Replace or remove backgrounds automatically
- **Vectorization**: Convert raster images to scalable SVG format
- **Upscaling**: Both crisp and creative upscaling for enhanced resolution

### 📊 **Account Management**
- **User Info**: Get account information and credits balance
- **API Usage**: Monitor your API usage and remaining credits

## 🚀 Installation

### Option 1: n8n Community Nodes (Recommended)
1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Click **Install** and enter: `n8n-nodes-recraft-v3`
3. Click **Install**

### Option 2: Manual Installation
```bash
# In your n8n installation directory
npm install n8n-nodes-recraft-v3
```

## 📋 Prerequisites

1. **Recraft Account**: Sign up at [recraft.ai](https://recraft.ai)
2. **API Key**: Get your API key from your [Recraft profile](https://app.recraft.ai/profile/api)
3. **API Credits**: Purchase API units to use the service ($0.04 per raster image, $0.08 per vector image)

## ⚙️ Setup

1. **Add Credentials**:
   - Go to **Credentials** in n8n
   - Click **Add Credential** and search for "Recraft API"
   - Enter your API token from Recraft

2. **Add Node**:
   - Add the **Recraft v3** node to your workflow
   - Configure the operation you want to perform

## 💡 Usage Examples

### Basic Text-to-Image Generation
```yaml
Resource: Image
Operation: Generate
Prompt: "A serene landscape with mountains reflected in a crystal-clear lake at golden hour"
Model: Recraft V3
Style: Realistic Image
Size: 1024x1024
Number of Images: 1
```

### Advanced Generation with Controls
```yaml
Resource: Image
Operation: Generate
Prompt: "A modern office space with plants"
Model: Recraft V3
Style: Digital Illustration
Sub Style: Modern Folk
Number of Images: 3
Negative Prompt: "cluttered, dark, messy"
Advanced Options:
  Colors (JSON): [{"rgb": [46, 125, 50]}, {"rgb": [255, 193, 7]}]
  Background Color: [245, 245, 245]
  Artistic Level: 3
  No Text: false
```

### Custom Brand Style Creation
```yaml
Resource: Style
Operation: Create
Base Style: Digital Illustration
Reference Images: data (binary property with 3-5 brand reference images)
```

### Image Transformation
```yaml
Resource: Image
Operation: Image to Image
Input Image: data (binary property with source image)
Prompt: "Transform to a winter scene with snow and ice"
Strength: 0.7
Style: Realistic Image
Number of Images: 2
Negative Prompt: "summer, warm colors"
```

### Vector Art Generation
```yaml
Resource: Image
Operation: Generate
Prompt: "Clean geometric logo of a mountain peak with sun rays"
Style: Vector Illustration
Sub Style: Line Art
Size: 1024x1024
```

### Background Operations
```yaml
Resource: Image
Operation: Replace Background
Input Image: data (source image)
Prompt: "Professional office environment with soft lighting"
Style: Realistic Image
Number of Images: 1
Response Format: URL
```

## 🎯 Complete API Coverage

### Image Operations
- **Generate**: Create images from text prompts ✅
- **Image to Image**: Transform images with prompts ✅
- **Inpaint**: Replace masked areas in images ✅
- **Replace Background**: Change image backgrounds ✅
- **Remove Background**: Remove backgrounds completely ✅
- **Vectorize**: Convert to SVG format ✅
- **Crisp Upscale**: Enhance resolution (sharp) ✅
- **Creative Upscale**: Enhance resolution (detailed) ✅

### Style Operations
- **Create**: Build custom styles from reference images ✅

### User Operations
- **Get Info**: Retrieve account and credit information ✅

### All Parameters Supported
- ✅ **prompt** (required) - Text description
- ✅ **n** - Number of images (1-6)
- ✅ **style_id** - Custom style ID
- ✅ **style** - Predefined styles
- ✅ **substyle** - Style refinements
- ✅ **model** - recraftv3 or recraftv2
- ✅ **response_format** - url or b64_json
- ✅ **size** - All 15 supported sizes
- ✅ **negative_prompt** - Unwanted elements
- ✅ **text_layout** - Precise text positioning (V3 only)
- ✅ **controls** - All advanced controls:
  - ✅ **colors** - Color preferences (JSON array)
  - ✅ **background_color** - Background color control
  - ✅ **artistic_level** - Artistic tone (0-5)
  - ✅ **no_text** - Prevent text embedding

## 🎨 Available Styles & Sub-styles

### Base Styles
- **Realistic Image**: Photo-like images from digital cameras
- **Digital Illustration**: Hand-drawn or computer-generated art
- **Vector Illustration**: Clean vector graphics with flat colors
- **Icon**: Simple, recognizable symbols
- **Any**: Let the model choose the best style

### Sub-styles (Digital Illustration)
- Hand Drawn, Pixel Art, Cartoon, Anime, 3D Render
- 2D Art Poster, Bold Fantasy, Child Book, Cover
- Engraving Color, Expressionism, Grain, Modern Folk
- Neon Calm, Noir, Pastel Gradient, Plastic
- Pop Art, Street Art, Urban Glow, and more...

## 📐 Supported Image Sizes

All 15 official Recraft sizes supported:
- **Square**: 1024x1024
- **Landscape**: 1365x1024, 1536x1024, 1820x1024, 2048x1024, 1434x1024, 1280x1024, 1707x1024
- **Portrait**: 1024x1365, 1024x1536, 1024x1820, 1024x2048, 1024x1434, 1024x1280, 1024x1707

## 🔧 Advanced Features

### Dynamic Color Control
Perfect for brand consistency - map colors directly from your database:
```json
[{"rgb": [255, 0, 0]}, {"rgb": [0, 255, 0]}, {"rgb": [0, 0, 255]}]
```

### Background Color Control
Set specific background colors:
```json
[245, 245, 245]
```

### Artistic Level Control
- **0**: Simple, static, clean style
- **1-2**: Slightly more dynamic
- **3**: Balanced (default)
- **4-5**: Dynamic, eccentric, creative

### Text Layout (Recraft V3 Only)
Position text elements precisely using bounding box coordinates:
```json
[[0.3, 0.45], [0.6, 0.45], [0.6, 0.55], [0.3, 0.55]]
```

### Negative Prompts
Avoid unwanted elements:
```
"blurry, low quality, distorted, watermark, text"
```

### Custom Styles
Upload 3-5 reference images to create brand-consistent styles for all your generations.

## 📁 File Support

- **Input Formats**: PNG, JPG, JPEG, WEBP
- **Output Formats**: PNG, JPG, WEBP, SVG (vectorization)
- **Maximum File Size**: 5 MB
- **Maximum Resolution**: 16 MP (4 MP for crisp upscale)
- **Maximum Dimension**: 4096 pixels
- **Minimum Dimension**: 256 pixels (32 for crisp upscale)

## 💰 Pricing

- **Recraft V3 Raster**: $0.04 per image (40 API units)
- **Recraft V3 Vector**: $0.08 per image (80 API units)
- **Recraft V2 Raster**: $0.022 per image (22 API units)
- **Recraft V2 Vector**: $0.044 per image (44 API units)
- **Image Operations**: $0.004-$0.25 depending on operation
- **API Units**: $1.00 = 1,000 units

## 🚨 Error Handling

The node includes comprehensive error handling:
- File size and format validation
- API rate limit handling
- Network error recovery
- Clear error messages with specific guidance
- Continue on fail option
- JSON validation for dynamic fields

## 🔗 Resources

- [Recraft Website](https://www.recraft.ai)
- [Recraft API Documentation](https://www.recraft.ai/docs)
- [Get API Key](https://app.recraft.ai/profile/api)
- [n8n Community](https://community.n8n.io)

## 📝 License

MIT License - see LICENSE file for details.

## ⚠️ Important Disclaimers

### Unofficial Community Node
- This node is **not officially endorsed or supported** by Recraft AI or n8n
- Created by the community for educational and testing purposes
- Built using Claude Sonnet 4 AI assistance following n8n development standards

### Development & Testing
- Code follows n8n best practices and includes comprehensive error handling
- Thoroughly reviewed against 2025 n8n community node standards and latest Recraft API
- **Recommended**: Test in development environments before production use
- Always validate outputs and monitor API usage

### Support & Liability
- Community-supported through GitHub issues
- No warranty or guarantee of functionality
- Users responsible for API costs and usage
- Not affiliated with Recraft AI - please respect their terms of service

### Contributing & Feedback
- Bug reports and contributions welcome via GitHub
- This is a learning project - improvements and suggestions appreciated
- Help make this the best community Recraft integration possible!

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 🐛 Support

- Check the [Recraft documentation](https://www.recraft.ai/docs)
- Visit the [n8n community forum](https://community.n8n.io)
- Open an issue on this repository

---

## 🆕 Changelog

### v1.1.4 - Complete API Coverage
- ✅ Added `n` parameter (number of images 1-6)
- ✅ Added `negative_prompt` support for all applicable operations  
- ✅ Added `artistic_level` control (0-5)
- ✅ Added `background_color` control with RGB values
- ✅ Added `no_text` control to prevent text embedding
- ✅ Improved color handling with JSON array support for dynamic mapping
- ✅ Added all 25+ digital illustration sub-styles
- ✅ Added all 15 official image sizes
- ✅ Enhanced error handling and validation
- ✅ Full compatibility with latest Recraft API documentation
