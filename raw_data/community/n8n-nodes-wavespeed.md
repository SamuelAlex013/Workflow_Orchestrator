# N8N Nodes for WaveSpeed AI

N8N nodes for WaveSpeed AI API - comprehensive multimodal AI models supporting 15 categories with dynamic model selection and parameter rendering.

## Features

### Universal AI Task Node (Recommended)
- **WaveSpeed Task Submit**: A universal node with dynamic model selection and intelligent parameter rendering
  - Supports all 15 model categories with automatic parameter adaptation
  - Dynamic model loading based on selected category
  - Resource mapper for easy parameter configuration
  - **Supported Categories**:
    - Text to Video - Generate videos from text prompts
    - Text to Image - Generate images from text prompts  
    - Image to Video - Convert images to videos
    - Image to Image - Transform and edit images
    - Video Effects - Apply effects to videos
    - Image Effects - Apply effects to images
    - Video to Video - Transform videos
    - Text to Audio - Generate audio from text
    - Image to 3D - Convert images to 3D models
    - Scenario Marketing - Marketing scenario models
    - Training - Train custom models
    - Image Tools - Image processing tools
    - Audio to Video - Generate videos from audio
    - Text to Text - Text processing and generation
    - Image to Text - Extract text from images

### Specialized Nodes
- **WaveSpeed Task Submit by JSON**: Submit tasks using custom JSON parameters
- **WaveSpeed Task Status**: Check the status of AI generation tasks with intelligent polling
- **WaveSpeed Loras**: Config Loras
- **WaveSpeed Upload Media**: Upload media files (images, videos, audio) to WaveSpeed platform

## Installation

1. Open the N8N Settings page
2. Go to the Community nodes page and click Install
3. Enter the npm Package Name [n8n-node-wavespeed] and then wait for the installation to complete
4. Refresh the page and enter "wavespeed" to search for nodes

## Configuration

### Credentials

You need to configure your WaveSpeed API credentials:

1. **API Key**: Your WaveSpeed API key from the dashboard

### WaveSpeed Task Submit Node

The main node for submitting AI tasks with the following features:

#### Model Selection
- **Category Selection**: Choose from 15 AI model categories
- **Dynamic Model Loading**: Models are loaded automatically based on selected category
- **Model Information**: Each model includes description and parameter details

#### Parameter Configuration
- **Required Parameters**: Automatically loaded based on selected model
- **Resource Mapper**: Easy-to-use interface for parameter configuration
- **Parameter Validation**: Built-in validation for parameter types and constraints

### WaveSpeed Upload Media Node

Upload media files to WaveSpeed platform with support for:

#### Supported Media Types
- **Images**: JPG, JPEG, PNG, WebP, GIF, BMP, TIFF
- **Videos**: MP4, AVI, MOV, WMV, FLV, WebM, MKV, 3GP, OGV
- **Audio**: MP3, WAV, OGG, AAC, FLAC, WebM, M4A, Opus

#### Input Methods
1. **URL Input**: Download files from a URL and upload to WaveSpeed
2. **File Input**: Use n8n file data directly (Binary)
 
 
## Example Workflows

### Basic Image Generation
```
WaveSpeed Task Submit → Use Result
```

### Media Upload and Processing
```
Load File → WaveSpeed Upload Media → WaveSpeed Task Submit → Use Result
```

### LoRA Model Usage
```
WaveSpeed Loras → WaveSpeed Task Submit → Use Result
```

## Troubleshooting

### Common Issues

1. **API Key Invalid**: Check your API key in credentials
2. **Model Not Found**: Verify model ID and category selection
3. **Parameter Errors**: Check required parameters and their formats
4. **Upload Failures**: Verify file format and size limits
5. **Timeout Issues**: Adjust timeout settings for large files


## License

Apache-2.0

## Support

For support, please contact:
- **Email**: support@wavespeed.ai
- **Documentation**: [WaveSpeed AI Documentation](https://wavespeed.ai/docs)
- **GitHub**: [WaveSpeed N8N Repository](https://github.com/WaveSpeedAI/wavespeed-n8n)

## Version History

- **v1.0.1**: Enhanced error handling, improved polling, signal handling
- **v1.0.0**: Initial release with core functionality

