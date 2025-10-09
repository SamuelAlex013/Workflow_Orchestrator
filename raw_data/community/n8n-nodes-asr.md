# n8n-nodes-asr

A custom n8n node for automatic speech recognition (ASR), supporting audio file upload, format conversion, and integration with external ASR services.

## Features

- Download audio files from a URL and handle redirects
- Automatic format detection: if the input is already standard WAV (pcm_s16le, 44.1kHz, stereo), upload directly; otherwise, convert using ffmpeg
- Supports custom ffmpeg parameters (default: 44.1kHz, stereo)
- Multipart/form-data upload compatible with FastAPI and other ASR backends
- Returns parsed ASR results in n8n workflow

## Installation

```sh
npm install n8n-nodes-asr
```

## Usage

1. Add the node to your n8n custom nodes directory or install via npm.
2. Configure the node with your ASR service URL and API key.
3. Provide an audio file URL as input.
4. The node will download, (if needed) convert, and upload the audio to your ASR service, returning the transcription.

## Example Workflow

```json
{
  "nodes": [
    {
      "parameters": {
        "audioUrl": "https://example.com/audio.wav",
        "asrUrl": "http://your-asr-service/api/v1/asr",
        "apiKey": "your-api-key",
        "language": "auto"
      },
      "name": "ASR",
      "type": "n8n-nodes-asr"
    }
  ]
}
```

## Development

- Clone this repo and install dependencies:
  ```sh
  git clone https://github.com/youyouhe/n8n-nodes-asr.git
  cd n8n-nodes-asr
  npm install
  ```
- Build:
  ```sh
  npm run build
  ```
- Test in your n8n instance by copying the built files to your custom nodes directory.

## License

MIT

## Author

chimpansee (<chimpansee.he@gmail.com>)