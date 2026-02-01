# n8n-nodes-clipmagic

An n8n community node for integrating with the ClipMagic API - a powerful suite of video and audio processing tools.

## Features

- **Convert Media**: Convert videos and audio files to different formats and resolutions
- **Trim Media**: Extract single or multiple segments from media files
- **Compress Video**: Reduce video file size with configurable quality settings
- **Burn Captions**: Hard-code subtitles into videos
- **Generate AI Clips**: Create short, social-media-ready clips with optional karaoke-style subtitles

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install** and enter: `n8n-nodes-clipmagic`
3. Click **Install** and wait for the installation to complete

### Manual Installation

1. Install the package in your n8n installation:
   ```bash
   npm install n8n-nodes-clipmagic
   ```

2. Restart your n8n instance

## Prerequisites

- n8n version 0.187.0 or higher
- A ClipMagic API account and API key

## Getting Started

### 1. Get Your API Key

1. Sign up for a ClipMagic account at [clipmagic.pro](https://clipmagic.pro)
2. Navigate to your account dashboard
3. Generate an API key

### 2. Configure Credentials

1. In n8n, go to **Credentials** and create a new **ClipMagic API** credential
2. Enter your API key
3. (Optional) Modify the base URL if using a different endpoint
4. Test the connection

### 3. Use the Node

1. Add the **ClipMagic** node to your workflow
2. Select your credential
3. Choose an operation and configure the parameters
4. Execute the workflow

## Operations

### Convert Media

Convert videos or audio files to different formats and resolutions.

**Parameters:**
- **Media URL**: Direct file URL or Google Drive share link
- **Output Format**: Target format (MP3, WAV, AAC, MP4, MOV)
- **Resolution**: Video resolution (360p, 480p, 720p, 1080p)
- **Bitrate**: Target bitrate in kbps (optional)

**Example Use Cases:**
- Convert MP4 videos to MP3 audio
- Resize videos for social media
- Convert audio formats for compatibility

### Trim Media

Extract one or multiple segments from media files.

**Parameters:**
- **Media URL**: Input media URL
- **Trim Mode**: Single segment or multiple segments
- **Start/End Time**: Define clip boundaries
- **Output Format**: Target format for trimmed clips

**Example Use Cases:**
- Extract highlights from long recordings
- Create multiple clips from a single video
- Remove unwanted sections from media

### Compress Video

Reduce video file size using x264 encoding.

**Parameters:**
- **Video URL**: Input video URL
- **Preset**: Encoding speed (ultrafast to placebo)
- **CRF**: Quality setting (18=high quality, 28=low quality)
- **Output Format**: Container format

**Example Use Cases:**
- Reduce file sizes for faster uploads
- Optimize videos for web streaming
- Balance quality and file size

### Burn Captions

Hard-code subtitles into video files.

**Parameters:**
- **Video URL**: Input video URL
- **Subtitle URL**: SRT or ASS subtitle file URL
- **Font Size**: Caption font size in pixels
- **Font Color**: Hex color code for text
- **Position**: Caption position (top, middle, bottom)

**Example Use Cases:**
- Add permanent subtitles to videos
- Create accessible content
- Localize videos with translated captions

### Generate AI Clips

Automatically create short clips from long-form videos with optional karaoke-style subtitles.

**Parameters:**
- **Video URL**: Source video URL
- **Generate Subtitles**: Enable karaoke-style captions
- **Highlight Color**: Color for current spoken word
- **Resolution**: Output resolution
- **Orientation**: Clip orientation (horizontal/vertical)

**Example Use Cases:**
- Create social media clips from podcasts
- Generate promotional content from webinars
- Extract key moments with animated subtitles

## Output

The ClipMagic node outputs:
- **Binary Data**: Processed media files
- **JSON Metadata**: Operation details, filename, content type
- **Error Information**: If something goes wrong (when "Continue on Fail" is enabled)

## Error Handling

Common HTTP status codes:
- **401**: Invalid or missing API key
- **402**: Insufficient credits
- **422**: Invalid request parameters
- **500**: Server error

Enable "Continue on Fail" to handle errors gracefully in your workflow.

## Examples

### Basic Video Conversion
```json
{
  "operation": "convert",
  "url": "https://example.com/video.mp4",
  "outputFormat": "mp3",
  "resolution": "720p"
}
```

### Multi-Segment Trim
```json
{
  "operation": "trim",
  "url": "https://example.com/video.mp4",
  "trimMode": "multiple",
  "segments": [
    {"start": "00:01:00", "duration": "30"},
    {"start": "00:05:00", "end": "00:05:15"}
  ]
}
```

### AI Clip Generation
```json
{
  "operation": "generateClips",
  "url": "https://example.com/long-video.mp4",
  "subtitles": true,
  "highlightColor": "#00FFFF",
  "resolution": "1080p",
  "orientation": "vertical"
}
```

## Support

- **Documentation**: [ClipMagic API Docs](https://clipmagic.pro/docs)
- **Issues**: Report bugs and request features on GitHub
- **Community**: Join the n8n community for help and discussion

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Changelog

### 1.0.0
- Initial release
- Support for all ClipMagic API operations
- Binary file handling for media outputs
- Comprehensive parameter validation
- Error handling and credential testing