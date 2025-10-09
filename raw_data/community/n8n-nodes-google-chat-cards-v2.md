# n8n-nodes-google-chat-cards-v2

This is an n8n community node that lets you create rich, interactive Google Chat messages using the Cards v2 API with a visual builder interface.

## Features

- 🎨 **Visual Card Builder** - Create cards without writing JSON
- 📝 **Simple Mode** - Quick cards with basic elements (header, text, buttons)
- 🔧 **JSON Mode** - Full control with raw JSON input for advanced users
- 🎯 **Rich Widgets Support**:
  - Text with formatting
  - Images with click actions
  - Buttons with custom actions
  - Decorated text with icons
  - Grids for organized layouts
  - Text inputs for user feedback
  - Selection inputs (dropdown, radio, checkbox)
  - Dividers for visual separation
- 🧵 **Thread Support** - Group messages in conversations
- ⚡ **Dual Authentication** - OAuth2 or Webhook URL

## Installation

### In n8n

1. Go to **Settings** > **Community Nodes**
2. Search for `n8n-nodes-google-chat-cards-v2`
3. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-google-chat-cards-v2
```

Then restart your n8n instance.

## Setup

### Option 1: Webhook URL (Simple)

1. **Get Webhook URL**:
   - Open your Google Chat space
   - Click on the space name > "Manage webhooks"
   - Create a new webhook and copy the URL

2. **Configure in n8n**:
   - Select "Webhook URL (Simple)" as authentication method
   - Paste your webhook URL
   - Start sending messages!

### Option 2: OAuth2 (Advanced)

1. **Google Cloud Console Setup**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable the Google Chat API

2. **Create OAuth2 Credentials**:
   - Go to APIs & Services > Credentials
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Web application"
   - Add authorized redirect URI: `https://your-n8n-instance.com/rest/oauth2-credential/callback`

3. **Configure OAuth Consent Screen**:
   - Add required scopes: `https://www.googleapis.com/auth/chat.messages`

4. **n8n Credentials Setup**:
   - In n8n, go to **Credentials**
   - Create new **Google Chat OAuth2 API** credential
   - Enter your Client ID and Client Secret
   - Authenticate with Google

## Usage

### Simple Mode

Perfect for quick notifications and basic messages:

1. Select **Simple Card** mode
2. Add optional header with title and image
3. Enter your main message text
4. Add buttons for actions
5. Include additional widgets as needed

**Example Simple Card:**
- Header: "Deployment Complete ✅"
- Text: "Your application has been successfully deployed to production."
- Button: "View Application" → Opens URL

### JSON Mode

For advanced users who need full control:

1. Select **JSON Input** mode
2. Enter complete Cards v2 JSON structure
3. Reference [Google Chat Cards API](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards)

**Example JSON:**
```json
{
  "cardsV2": [
    {
      "card": {
        "header": {
          "title": "Custom Card",
          "subtitle": "With full JSON control"
        },
        "sections": [
          {
            "widgets": [
              {
                "textParagraph": {
                  "text": "Your custom content here"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Supported Widgets

### Text Paragraph
Basic text content with optional markdown formatting.

### Images
Display images with optional click actions to open URLs.

### Decorated Text
Text with icons, top/bottom labels for rich information display.

### Buttons
Interactive buttons that can:
- Open URLs
- Trigger custom actions with parameters

### Grid (v0.2.0)
Display items in an organized grid layout with:
- Configurable columns
- Image support
- Title and subtitle for each item

### Text Input (v0.2.0)
Collect user input with:
- Single or multi-line text fields
- Labels and hints
- Initial values

### Selection Input (v0.2.0)
Provide selection options:
- Dropdown menus
- Radio buttons
- Checkboxes
- Multi-select support

### Dividers
Visual separators between content sections.

## Examples

### Deployment Notification
```javascript
// Simple Mode Configuration
{
  "buildMode": "simple",
  "simpleHeader": {
    "title": "Deployment Status",
    "subtitle": "Production Environment",
    "imageUrl": "https://example.com/deploy-icon.png",
    "imageType": "CIRCLE"
  },
  "simpleText": "Version 2.1.0 has been successfully deployed",
  "simpleButtons": [
    {
      "text": "View Changes",
      "actionType": "openLink",
      "url": "https://github.com/repo/releases"
    }
  ]
}
```

### Alert Message
```javascript
// Simple Mode with Decorated Text
{
  "buildMode": "simple",
  "simpleText": "System alert triggered",
  "simpleWidgets": {
    "decoratedText": [
      {
        "text": "CPU Usage: 95%",
        "topLabel": "Alert Type",
        "bottomLabel": "Immediate attention required",
        "icon": "CLOCK"
      }
    ]
  }
}
```

### Feedback Form (v0.2.0)
```javascript
// Using new input widgets
{
  "buildMode": "simple",
  "simpleText": "Please provide your feedback",
  "simpleWidgets": {
    "textInput": [
      {
        "name": "feedback",
        "label": "Your Comments",
        "multiline": true,
        "hintText": "Tell us what you think"
      }
    ],
    "selectionInput": [
      {
        "name": "rating",
        "label": "Rate our service",
        "type": "dropdown",
        "items": [
          {"text": "Excellent", "value": "5"},
          {"text": "Good", "value": "4"},
          {"text": "Average", "value": "3"}
        ]
      }
    ]
  }
}
```

## Limitations

- Google Chat supports limited markdown (bold, italic, strikethrough)
- Images must be HTTPS URLs
- Maximum 100 widgets per card
- Some advanced Cards v2 features may require JSON mode

## Changelog

### v0.2.2 (Latest)
- ✅ Fixed Grid widget to use Items instead of confusing Rows/Cells structure
- ✅ Grid items now support title, subtitle, image, and click actions
- ✅ Clearer UI that explains items auto-arrange into rows based on columns

### v0.2.1
- ✅ Fixed webhook 503 error by changing request method

### v0.2.0
- ✅ Added webhook URL authentication method
- ✅ New Grid widget for organized layouts
- ✅ Text Input widget for user feedback
- ✅ Selection Input widget (dropdown, radio, checkbox)
- ✅ Enhanced Simple Mode with more widget types

### v0.1.0
- Initial release with OAuth2 authentication
- Simple and JSON modes
- Basic widgets support

## Roadmap

Future enhancements planned:
- 🎨 Full visual builder with drag-and-drop
- 📚 Template library for common use cases
- 🔄 Card preview before sending
- 🎯 Advanced action handlers
- 🔧 Webhook response handling

## Resources

- [Google Chat Cards v2 Documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards)
- [n8n Community](https://community.n8n.io)
- [Report Issues](https://github.com/jezweb/n8n-nodes-google-chat-cards-v2/issues)

## License

MIT

## Author

Jeremy Dawes - [Jezweb](https://www.jezweb.com.au)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.