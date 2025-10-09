# n8n-nodes-splitaudio

[![npm version](https://badge.fury.io/js/n8n-nodes-splitaudio.svg)](https://badge.fury.io/js/n8n-nodes-splitaudio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an n8n community node that lets you split audio files into smaller chunks in your n8n workflows.

The Split Audio node is a powerful utility that breaks large audio files into smaller segments of a specified size, which is useful for processing, analyzing, or uploading large audio files in manageable chunks.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
  - [Dependencies](#dependencies)
- [Operations](#operations)
  - [Split Audio Options](#split-audio-options)
- [Compatibility](#compatibility)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Example with Binary Files](#example-with-binary-files)
  - [Example with File Path](#example-with-file-path)
- [Resources](#resources)
- [Support](#support)
- [License](#license)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Dependencies

This node requires FFmpeg to be installed on your system. Please make sure FFmpeg is installed and available in your system's PATH.

- For Windows: You can download FFmpeg from [their official website](https://ffmpeg.org/download.html) or install it via [Chocolatey](https://chocolatey.org/) with `choco install ffmpeg`
- For macOS: You can install FFmpeg using Homebrew with `brew install ffmpeg`
- For Linux: You can install FFmpeg using your distribution's package manager, e.g., `apt install ffmpeg` for Debian/Ubuntu

## Operations

The Split Audio node supports the following operation:

- **Split Audio**: Divides an audio file into multiple chunks of a specified size

### Split Audio Options

- **Input Type**: Choose between binary data or file path input
- **Chunk Size**: Size of each audio chunk in MB
- **Output Prefix**: Prefix for chunk filenames
- **Output Format**: Format for output chunks (Same as Input, MP3, M4A, WAV)
- **Memory Management**: Standard or Low Memory mode for handling large files
- **Delete Original**: Option to delete the original file after processing (when using file path input)

## Compatibility

This node has been tested with n8n version 1.90.2 and above.

## Usage

### Basic Usage

1. Add the Split Audio node to your workflow.
2. Connect it to a node that provides an audio file (e.g., HTTP Request, Read Binary Files).
3. Configure the chunk size and other parameters.
4. The node will output multiple items, each containing a chunk of the original audio file.

### Example with Binary Files

1. Add a **Read/Write Files from Disk** node to read an audio file.
2. Connect the **Split Audio** node after it.
3. Set the Input Type to "Binary Data".
4. Configure the chunk size (e.g., 10 MB).
5. Run the workflow to split the audio file.

You can also use any node that provides binary data as output, such as the **Google Drive** node or the **HTTP Request** node.

### Example with File Path

1. Add a **Read/Write Files from Disk** node to get the file path.
2. Connect the **Split Audio** node after it.
3. Set the Input Type to "File Path".
4. Set the File Path Field to the expression `{{ $json.directory }}/{{ $json.fileName }}`.
5. Configure the chunk size and other options.
6. Run the workflow to split the audio file.

## Example Workflow

A typical workflow using the Split Audio node might look like:

1. Trigger Node → 2. Read Audio File → 3. Split Audio Node → 4. Process Individual Chunks

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [n8n official website](https://n8n.io)
* [FFmpeg documentation](https://ffmpeg.org/documentation.html)

## Support

If you have any questions or issues with this node, please:

* Check the [n8n community forum](https://community.n8n.io/)
* Open an issue on the [GitHub repository](https://github.com/edsonbraz/n8n-nodes-splitaudio)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
