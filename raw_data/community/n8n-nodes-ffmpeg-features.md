# n8n-nodes-ffmpeg-features

**Based on [shmeller86/n8n-nodes-ffmpeg](https://github.com/shmeller86/n8n-nodes-ffmpeg)**

This package contains an n8n node that allows you to work with FFmpeg for video and audio file processing.

## Installation

**Important**: Make sure FFmpeg is installed on your system.

## Operations

The node supports the following operations:

### 1. Merge Videos
- Combines multiple video files into one
- Configurable minimum number of files to merge
- Support for custom FFmpeg arguments

### 2. Overlay Audio
- Overlays an audio track onto a video file
- Configurable encoding parameters

### 3. Media Info
- Get technical information about video/audio files
- Detailed information about streams, codecs, and metadata

### 4. Custom Command
- Execute arbitrary FFmpeg commands
- Full control over processing parameters

### 5. Convert Media
- Convert media files to different formats
- Support for various codecs and containers
- Configurable encoding parameters

## Parameters

### Common Parameters
- **Operation**: Choose operation (merge/overlay/info/custom)
- **Output File Name**: Name of the output file
- **Output Binary Property**: Name of the binary property for the output file

### Merge Parameters
- **Minimum Files to Merge**: Minimum number of files required before merging
- **FFmpeg Merge Arguments**: Command line arguments for merging

### Overlay Parameters
- **FFmpeg Overlay Arguments**: Command template for audio overlay

### Custom Parameters
- **Custom FFmpeg Command**: Arbitrary FFmpeg command

## Usage Examples

### Merging Videos
{
  "operation": "merge",
  "minFiles": 2,
  "outputFileName": "merged_video.mp4",
  "outputBinary": "mergedVideo",
  "ffmpegMergeArgs": "-f concat -safe 0 -i \"{input}\" -c:v libx264 -c:a aac \"{output}\""
}

### Overlaying Audio
{
  "operation": "overlay",
  "outputFileName": "video_with_audio.mp4",
  "outputBinary": "videoWithAudio",
  "ffmpegOverlayArgs": "-i \"{video}\" -i \"{audio}\" -c:v copy -c:a aac \"{output}\""
}

## License

[MIT](LICENSE.md)
