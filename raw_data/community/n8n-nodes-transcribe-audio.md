# n8n-nodes-transcribe-audio

This is an n8n community node. It lets you perform speech-to-text on audio files within your n8n workflows. This node provides local audio transcription; no internet or third-party APIs are required for processing.

It utilizes Hugging Face Transformers.js and Whisper models to transcribe audio.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Models](#models)
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- **Transcribe**: Takes an audio file (binary input) and returns the transcribed text. It can handle various audio formats (e.g., MP3, WAV) by converting them to the required WAV format (16kHz, 16-bit PCM, mono) using FFmpeg.

## Models

The node allows you to select from a list of pre-configured Xenova Whisper models:
- `Xenova/whisper-tiny.en`
- `Xenova/whisper-base.en`
- `Xenova/whisper-small.en`
- `Xenova/whisper-medium.en`

Larger models generally provide better accuracy but require more processing power and time.

## Credentials

This node does not require any credentials.

## Compatibility

- **n8n Version**: Tested with n8n versions `1.0.0` and above.
- **Node.js Version**: Requires Node.js version `>=20.15` as specified in the `package.json`.

## Usage

1.  **Input**: Provide an audio file via a binary property (default: `data`).
2.  **Binary Property Name**: Specify the name of the binary property containing the audio data if it's not `data`.
3.  **Model Selection**: Choose the desired Whisper model for transcription.
4.  **Output**: The node will output the transcribed text in `json.transcription` and potentially other related information.

Ensure FFmpeg is installed and accessible in your n8n environment if you plan to process audio formats other than WAV, as the node relies on it for audio conversion.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Hugging Face Transformers.js](https://huggingface.co/docs/transformers.js)
* [Xenova Whisper Models on Hugging Face](https://huggingface.co/Xenova?search_models=whisper)
* [ffmpeg](https://ffmpeg.org/)
* [Project Repository](https://github.com/dioveath/n8n-nodes-transcribe-audio)