# n8n-nodes-neuphonic

🎤 **Transform text into natural speech with AI-powered voices**

This is an n8n community node that integrates [Neuphonic](https://www.neuphonic.com/)'s advanced Text-to-Speech API into your workflows. Generate high-quality, natural-sounding speech from text using state-of-the-art AI voice synthesis technology.

Neuphonic provides enterprise-grade text-to-speech capabilities with ultra-realistic voices, low latency, and extensive customization options for professional audio applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## 📋 Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [Version History](#version-history)

## 🚀 Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes** in your n8n instance
2. Enter `n8n-nodes-neuphonic` in the npm package name field
3. Click **Install**

Alternatively, you can install it manually:

```bash
npm install n8n-nodes-neuphonic
```

## ⚡ Operations

The Neuphonic node currently supports:

- **Text to Speech**: Convert text input into high-quality audio speech
  - Multiple voice options
  - Configurable output formats (MP3, WAV)
  - Support for long-form text conversion
  - Real-time processing capabilities

## 🔐 Credentials

To use this node, you need a Neuphonic API account:

1. **Sign up** at [Neuphonic](https://www.neuphonic.com/) to create an account
2. **Generate an API key** from your Neuphonic dashboard
3. **Configure credentials** in n8n:
   - Go to **Credentials > New**
   - Select **Neuphonic API**
   - Enter your API key

> 🔒 **Security Note**: Your API key is stored securely and never logged or exposed in error messages.

## 🔧 Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: 20.15+
- **Tested with**: n8n 1.x latest versions

> 📝 **Note**: This package is actively maintained and tested against the latest stable n8n releases.

## 💡 Usage

### Basic Text-to-Speech

1. **Add the Neuphonic node** to your workflow
2. **Connect your credentials** (Neuphonic API)
3. **Configure the node**:
   - **Text**: Enter the text you want to convert to speech
   - **Voice**: Select from available voice options
   - **Format**: Choose output format (MP3 or WAV)
4. **Execute** the workflow

### Example Use Cases

- **Content Creation**: Generate voiceovers for videos and podcasts
- **Accessibility**: Convert written content to audio for visually impaired users
- **E-learning**: Create audio lessons and educational content
- **Customer Service**: Generate automated voice responses
- **Multi-language Support**: Create audio content in different languages

### Workflow Integration

The Neuphonic node works seamlessly with other n8n nodes:

```
📝 Google Docs → 🎤 Neuphonic → 📧 Email (send audio attachment)
🐦 Twitter → 🎤 Neuphonic → 💾 Google Drive (save audio files)
📊 Airtable → 🎤 Neuphonic → 🎵 Spotify (podcast automation)
```

## 📚 Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Neuphonic API Documentation](https://docs.neuphonic.com/)
- [Neuphonic Voice Gallery](https://www.neuphonic.com/voices)
- [Text-to-Speech Best Practices](https://docs.neuphonic.com/best-practices)

## 📖 Version History

### v0.1.1 (Latest)
- ✅ Fixed package dependencies and loading issues
- ✅ Improved error handling and validation
- ✅ Optimized package size and structure
- ✅ Enhanced compatibility with latest n8n versions

### v0.1.0
- 🎉 Initial release
- ✨ Basic Text-to-Speech functionality
- 🔐 Secure API key authentication
- 🎵 Support for MP3 and WAV output formats

---

**Made with ❤️ by [Agboola Abdulkabir](https://github.com/Abdk4Moura)**

*If you find this node useful, please consider starring the repository and sharing it with the n8n community!*
