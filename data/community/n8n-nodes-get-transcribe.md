# n8n-nodes-get-transcribe

This is an n8n node for integrating with the GetTranscribe API, which allows you to transcribe videos from social media platforms like Instagram, TikTok, YouTube, and more.

## Features

### Transcriptions
- **Create**: Create a new transcription from a video URL
- **Get**: Get a specific transcription by ID
- **List**: List all transcriptions with optional filters

### Folders
- **Create**: Create new folders to organize transcriptions
- **List**: List all folders
- **Update**: Update properties of existing folders

### User
- **Get**: Get user information and account statistics

## Installation

### Installation on n8n Cloud

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-get-transcribe`
3. Click **Install**

### Installation on self-hosted n8n

1. Go to your n8n installation root directory
2. Run: `npm install n8n-nodes-get-transcribe`
3. Restart n8n

## Configuration

### Credentials

To use this node, you need to configure your GetTranscribe credentials:

1. In n8n, go to **Credentials** and create new credentials of type **GetTranscribe API**
2. Enter your **API Key** from GetTranscribe
   - You can find your API Key in your GetTranscribe account settings
   - The API Key should have the format: `gt_...`

### Credential test URL

The node will automatically verify your credentials by making a request to `/users/me` on the GetTranscribe API.

## Usage

### Create a Transcription

1. Add the **GetTranscribe** node to your workflow
2. Select **Transcription** as resource
3. Select **Create** as operation
4. Enter the URL of the video you want to transcribe
5. Optionally, select a folder ID to organize the transcription

Supported URL examples:
- Instagram: `https://www.instagram.com/p/ABC123/`
- TikTok: `https://www.tiktok.com/@user/video/123456789`
- YouTube: `https://www.youtube.com/watch?v=ABC123`

### List Transcriptions

1. Select **Transcription** as resource
2. Select **List** as operation
3. Configure optional filters:
   - **Limit**: Maximum number of results
   - **Skip**: Number of results to skip (for pagination)
   - **Folder ID**: Filter by specific folder
   - **Platform**: Filter by platform (Instagram, TikTok, YouTube)

### Folder Management

#### Create Folder
1. Select **Folder** as resource
2. Select **Create** as operation
3. Enter the folder name
4. Optionally, specify a parent folder ID to create subfolders

#### List Folders
1. Select **Folder** as resource
2. Select **List** as operation
3. Configure the result limit

### User Information

1. Select **User** as resource
2. Select **Get** as operation
3. Enter your user ID (you can use your own ID)

## API Response

### Transcription

```json
{
  "id": 4032,
  "user_id": 2,
  "transcription": "Transcribed text from the video...",
  "platform": "instagram",
  "url": "https://www.instagram.com/p/DM1P8q1MzaG/",
  "thumbnail_url": "https://...",
  "download_video_url": "https://...",
  "download_audio_url": "https://...",
  "duration": "0:30",
  "duration_seconds": 30.159864,
  "word_count": 91,
  "char_count": 515,
  "folder_id": null,
  "transcription_analysis": null,
  "original_transcription": "Original text...",
  "transcription_segments": [...],
  "transcription_words": [...],
  "created_at": "2025-08-07T17:43:15.822Z",
  "updated_at": "2025-08-07T17:43:15.822Z"
}
```

## Workflow Examples

### Automatic Transcription from Webhook

1. **Webhook Trigger** - Receives video URLs
2. **GetTranscribe Node** - Transcribes the video
3. **Set Node** - Processes the transcribed text
4. **HTTP Request** - Sends the transcription to another service

### Batch Processing

1. **Schedule Trigger** - Runs periodically
2. **GetTranscribe Node** - Lists pending transcriptions
3. **If Node** - Checks if there are new transcriptions
4. **Loop** - Processes each transcription

## Support

- **Documentation**: [https://www.gettranscribe.ai/n8n-transcription-instagram-tiktok-automation](https://www.gettranscribe.ai/n8n-transcription-instagram-tiktok-automation)
- **Support**: [support@gettranscribe.ai](mailto:daniel@gettranscribe.ai)
- **GitHub**: [https://github.com/get-transcribe/n8n-nodes-get-transcribe](https://github.com/get-transcribe/n8n-nodes-get-transcribe)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Contributors

Thanks to all the people who have contributed to this project:

- [danielevz](https://github.com/emeagenciadigital) - Contributor

## License

MIT

## Changelog

### v0.1.1
- Updated GitHub repository URLs in package.json

### v0.1.0
- Initial release
- Support for transcriptions (create, get, list)
- Support for folders (create, list, update)
- Support for user information
- API Key authentication
