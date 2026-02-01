# n8n-nodes-meetgeek

This is an n8n community node that lets you use MeetGeek in your n8n workflows.

MeetGeek is an AI-powered meeting assistant that automatically records, transcribes, and summarizes your meetings.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Meeting
- **Get Details**: Retrieve detailed information about a specific meeting

### Recording  
- **Upload**: Upload a recording file for analysis and transcription

### Highlight
- **Get**: Retrieve highlights from a specific meeting
- **Listen for New**: Webhook trigger that fires when a new highlight is created

## Credentials

This node uses the MeetGeek API credentials. You'll need to:

1. Go to your MeetGeek settings
2. Navigate to the Integration Tab
3. Copy your API token from Public API
4. Create new credentials in n8n using this token

## Compatibility

Tested with n8n version 0.220.0 and above.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [MeetGeek API Documentation](https://docs.meetgeek.ai)

## License

MIT
