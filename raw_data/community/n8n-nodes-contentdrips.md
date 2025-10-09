# n8n-nodes-contentdrips

An n8n community node for the [Contentdrips API](https://app.contentdrips.com) that enables you to create carousels and static graphics for social media content automation.

## Features

- **Generate Static Graphics**: Create PNG or PDF graphics from templates
- **Generate Carousels**: Create multi-slide carousels with intro, content slides, and ending slides
- **Template-based**: Use your existing Contentdrips templates
- **Content Updates**: Update text and images using labeled elements
- **Branding Support**: Apply consistent branding (name, handle, bio, website, avatar)
- **Job Management**: Check status and retrieve results from asynchronous jobs

## Installation

### n8n Cloud

For n8n Cloud users:

1. Go to **Settings > Community Nodes** in your n8n Cloud instance
2. Click **Install a community node**  
3. Enter `n8n-nodes-contentdrips`
4. Click **Install**

The node will be automatically installed and available in your workflow editor.

### Self-hosted n8n

For self-hosted installations, you have several options:

#### Option 1: Community Nodes UI (Easiest)
1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter `n8n-nodes-contentdrips`
4. Click **Install**

#### Option 2: Docker Compose

Add the following to your `docker-compose.yml` environment variables:
```yaml
environment:
  - NODE_FUNCTION_ALLOW_EXTERNAL=*
```

Then modify your Dockerfile or create a custom image:
```dockerfile
FROM n8nio/n8n:latest
USER root
RUN npm install -g n8n-nodes-contentdrips
USER node
```

#### Option 3: Manual Installation

```bash
# Navigate to your n8n installation directory
cd ~/.n8n

# Install the node
npm install n8n-nodes-contentdrips

# Restart n8n
```

## Prerequisites

1. **Contentdrips Account**: Sign up at [Contentdrips](https://app.contentdrips.com)
2. **API Token**: Generate your API token from [API Management](https://app.contentdrips.com/api-management)
3. **Templates**: Create and configure templates in Contentdrips editor

## Configuration

### Credentials Setup

1. In n8n, go to **Credentials** 
2. Click **+ Add Credential**
3. Search for **Contentdrips API**
4. Enter your API token from Contentdrips

### Template Preparation

1. Create templates in Contentdrips editor
2. Add labels to text boxes and images you want to update:
   - Right-click on element → "Add Label" → Enter label name
3. Note your template ID from the URL or template settings

## Operations

### Generate Graphic

Create static graphics (PNG/PDF) from templates:

```json
{
  "operation": "generateGraphic",
  "templateId": "126130",
  "output": "png",
  "branding": {
    "name": "Jane Doe",
    "handle": "@janedoe",
    "bio": "Content Creator",
    "website_url": "https://janedoe.com",
    "avatar_image_url": "https://example.com/avatar.jpg"
  },
  "contentUpdates": [
    {
      "type": "textbox",
      "label": "title_1", 
      "value": "New Post Title"
    }
  ]
}
```

### Generate Carousel

Create multi-slide carousels:

```json
{
  "operation": "generateCarousel",
  "templateId": "126130",
  "output": "pdf",
  "carousel": {
    "intro_slide": {
      "heading": "Start Here",
      "description": "Tips that work",
      "image": "https://example.com/intro.jpg"
    },
    "slides": [
      {
        "heading": "Tip 1",
        "description": "Post daily content",
        "image": "https://example.com/slide1.jpg"
      }
    ],
    "ending_slide": {
      "heading": "Follow for more", 
      "description": "New tips weekly",
      "image": "https://example.com/end.jpg"
    }
  }
}
```

### Check Job Status

Monitor background job processing:

```json
{
  "operation": "checkJobStatus",
  "jobId": "15bf4a39-876a-4780-aaa9-4be6fe2c61b4"
}
```

### Get Job Result

Retrieve completed job results:

```json
{
  "operation": "getJobResult", 
  "jobId": "15bf4a39-876a-4780-aaa9-4be6fe2c61b4"
}
```

## Example Workflows

### Blog to Carousel Automation

1. **RSS Trigger** → Get new blog posts
2. **Code Node** → Extract title, summary, and key points
3. **Contentdrips Node** → Generate carousel with:
   - Intro slide: Blog title and summary
   - Content slides: Key points
   - Ending slide: Call-to-action

### Social Media Graphics

1. **Schedule Trigger** → Daily at 9 AM
2. **Google Sheets** → Get daily quote and image
3. **Contentdrips Node** → Generate quote graphic
4. **Social Media Node** → Post to platforms

## API Response Examples

### Successful Job Creation
```json
{
  "job_id": "15bf4a39-876a-4780-aaa9-4be6fe2c61b4",
  "status": "queued",
  "message": "Job has been queued for processing",
  "estimated_time": "2-5 minutes"
}
```

### Completed Job Result
```json
{
  "date": "2025-06-02T16:31:18.633Z",
  "type": "carousel", 
  "export_url": "https://contentdrips2.s3.amazonaws.com/server/104017/uploads/carousel-output.pdf"
}
```

## Troubleshooting

### Common Issues

1. **Authentication Error**: Verify your API token in credentials
2. **Template Not Found**: Check template ID exists and is accessible
3. **Label Not Found**: Ensure labels are properly set in template editor
4. **Job Timeout**: Large carousels may take longer to process

### Error Handling

The node supports n8n's **Continue on Fail** option. When enabled, errors are returned as data instead of stopping the workflow.

## Support

- **Documentation**: [Contentdrips API Docs](https://app.contentdrips.com/api-management)
- **GitHub Issues**: Report bugs and feature requests
- **Community Forum**: Get help from other users

## License

MIT License - see [LICENSE.md](LICENSE.md) for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
