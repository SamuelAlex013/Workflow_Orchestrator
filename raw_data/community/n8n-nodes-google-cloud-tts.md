

```bash
npm install n8n-nodes-google-cloud-tts
```

For Docker-based deployments, add the following to your n8n Dockerfile:

```dockerfile
RUN npm install -g n8n-nodes-google-cloud-tts
```

## Operations

### Speech Resource

#### Synthesize
- **Description**: Convert text to speech using Google Cloud Text-to-Speech API
- **Parameters**:
  - `text`: The text to convert to speech (required)
  - `languageCode`: Language code (e.g., 'de-DE', 'en-US')
  - `voiceName`: Specific voice name (optional)
  - `voiceGender`: Voice gender (NEUTRAL, MALE, FEMALE)
  - `audioEncoding`: Audio format (MP3, LINEAR16, OGG_OPUS)
  - `speakingRate`: Speaking speed (0.25 to 4.0)
  - `pitch`: Voice pitch (-20.0 to 20.0)
  - `outputFormat`: Return format (Base64 String or Binary Data)

### Voice Resource

#### List
- **Description**: List available voices from Google Cloud Text-to-Speech
- **Parameters**:
  - `languageCodeFilter`: Filter voices by language code (optional)

## Credentials

This node supports two authentication methods:

1. **Google OAuth2 API (Recommended)** - Use n8n's built-in Google OAuth2 credentials
2. **Service Account Key** - Traditional JSON key file approach

### Method 1: Google OAuth2 API (Recommended)

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable the Text-to-Speech API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Cloud Text-to-Speech API"
   - Click "Enable"

3. **Configure in n8n**:
   - Create new credentials of type **"Google OAuth2 API"** (this is n8n's standard Google OAuth2 credential)
   - Set the scope to include: `https://www.googleapis.com/auth/cloud-platform`
   - Complete the OAuth flow by signing in with Google
   - This credential can be reused for multiple Google Cloud services

### Method 2: Service Account Key

1. **Create Service Account**:
   - Go to "IAM & Admin" > "Service Accounts"
   - Click "Create Service Account"
   - Give it a name and description
   - Assign the "Cloud Text-to-Speech User" role
   - Generate and download the JSON key file

2. **Configure in n8n**:
   - Create new credentials of type "Google Cloud Text-to-Speech API"
   - Paste the entire JSON key file content into the "Service Account Key" field
   - Optionally set the Project ID

## Compatibility

- **n8n version**: 0.198.0 or later
- **Node.js**: 18.10 or later

## Usage

### Basic Text-to-Speech Example

1. **Add the Google Cloud TTS node** to your workflow
2. **Select "Speech" > "Synthesize"**
3. **Configure the parameters**:
   ```
   Text: "Hello, this is a test message in German."
   Language Code: de-DE
   Voice Gender: FEMALE
   Audio Encoding: MP3
   ```
4. **Run the workflow**

The node will return the synthesized speech as either:
- **Base64 String**: Audio data encoded as base64
- **Binary Data**: Direct binary audio file

### Advanced Example with Dynamic Text

```json
{
  "nodes": [
    {
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "position": [250, 300]
    },
    {
      "name": "Google Cloud TTS",
      "type": "n8n-nodes-google-cloud-tts.googleCloudTts",
      "position": [450, 300],
      "parameters": {
        "resource": "speech",
        "operation": "synthesize",
        "text": "={{ $json.message }}",
        "languageCode": "de-DE",
        "voiceGender": "FEMALE",
        "outputFormat": "binary"
      }
    }
  ]
}
```

### List Available Voices

Use the "Voice" > "List" operation to discover available voices:

```json
{
  "parameters": {
    "resource": "voice",
    "operation": "list",
    "languageCodeFilter": "de-DE"
  }
}
```

## Supported Languages

The node supports all languages available in Google Cloud Text-to-Speech, including:

- **German (de-DE)**: Multiple neural and WaveNet voices
- **English (en-US, en-GB)**: Wide variety of voices
- **Spanish (es-ES)**: Male and female voices
- **French (fr-FR)**: Multiple voice options
- **Italian (it-IT)**: Neural voices available
- **Portuguese (pt-BR)**: Brazilian Portuguese
- **Japanese (ja-JP)**: Natural-sounding voices
- **Chinese (zh-CN)**: Mandarin Chinese
- **Korean (ko-KR)**: Korean voices

For a complete list, use the "List Voices" operation.

## Examples

### 1. Multi-Language Text-to-Speech

```javascript
// Input data
[
  {
    "text": "Hello World",
    "language": "en-US"
  },
  {
    "text": "Hallo Welt",
    "language": "de-DE"
  },
  {
    "text": "Bonjour le monde",
    "language": "fr-FR"
  }
]

// Node configuration
{
  "text": "={{ $json.text }}",
  "languageCode": "={{ $json.language }}",
  "voiceGender": "NEUTRAL",
  "outputFormat": "binary"
}
```

### 2. Dynamic Voice Selection

```javascript
// Use different voices based on content type
{
  "text": "={{ $json.message }}",
  "languageCode": "de-DE",
  "voiceName": "={{ $json.isNews ? 'de-DE-News-K' : 'de-DE-Wavenet-F' }}",
  "speakingRate": "={{ $json.isUrgent ? 1.2 : 1.0 }}"
}
```

### 3. Batch Processing

```javascript
// Process multiple texts in one workflow
{
  "resource": "speech",
  "operation": "synthesize",
  "text": "={{ $json.texts.join('. ') }}",
  "languageCode": "de-DE",
  "outputFormat": "binary"
}
```

## Error Handling

The node includes comprehensive error handling:

- **Authentication errors**: Invalid service account credentials
- **API errors**: Quota exceeded, invalid parameters
- **Network errors**: Connection timeout, DNS resolution
- **Validation errors**: Missing required parameters

Enable "Continue on Fail" in the node settings to handle errors gracefully in your workflow.

## Performance Tips

1. **Batch Processing**: Combine multiple short texts into longer requests
2. **Caching**: Store frequently used audio files to avoid repeated API calls
3. **Audio Format**: Use MP3 for smaller file sizes, LINEAR16 for highest quality
4. **Voice Selection**: Neural voices provide better quality but consume more quota

## Resources

- [Google Cloud Text-to-Speech Documentation](https://cloud.google.com/text-to-speech/docs)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Voice Samples](https://cloud.google.com/text-to-speech/docs/voices)
- [SSML Guide](https://cloud.google.com/text-to-speech/docs/ssml)

## Support

For issues with this community node:

1. Check the [n8n community forum](https://community.n8n.io/)
2. Review [Google Cloud Text-to-Speech documentation](https://cloud.google.com/text-to-speech/docs)
3. Open an issue in the [project repository](https://github.com/gogomann/n8n-nodes-google-cloud-tts)

## License

[MIT](https://github.com/gogomann/n8n-nodes-google-cloud-tts/blob/master/LICENSE.md)

## Version History

### 0.2.0
- **NEW**: OAuth2 authentication support
- Added Google Cloud Text-to-Speech OAuth2 API credentials
- Improved authentication handling with fallback support
- Updated documentation with OAuth2 setup instructions

### 0.1.0
- Initial release
- Speech synthesis with full parameter control
- Voice listing functionality
- Base64 and binary output formats
- Support for all Google Cloud TTS languages
- Comprehensive error handling