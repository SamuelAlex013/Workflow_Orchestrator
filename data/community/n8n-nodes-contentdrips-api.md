# n8n-nodes-contentdrips-api

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node that lets you use [Contentdrips](https://contentdrips.com) in your n8n workflows.

Contentdrips is a powerful API for creating carousels and static graphics programmatically. It enables you to automate content creation using templates, making it perfect for social media automation, marketing campaigns, and content generation workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### GUI Installation

1. Go to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-contentdrips-api`
4. Select **Install**

### Manual Installation

To get started, install the package in your n8n root directory:

```bash
npm install n8n-nodes-contentdrips-api
```

For Docker installations, add the following line before the font installation command in your n8n Dockerfile:

```dockerfile
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-contentdrips-api
```

## Operations

### Graphic Resource
- **Create**: Generate a static graphic using a Contentdrips template

### Carousel Resource  
- **Create**: Generate a multi-slide carousel using a Contentdrips template

### Job Resource
- **Get Status**: Check the processing status of a job
- **Get Result**: Get the final result of a completed job

## Credentials

You need to authenticate with the Contentdrips API using an API token.

### Prerequisites
1. Sign up for a [Contentdrips account](https://app.contentdrips.com)
2. Create an API token in your [API Management dashboard](https://app.contentdrips.com/api-management)

### Setup
1. In n8n, go to **Credentials** and create a new **Contentdrips API** credential
2. Enter your API token
3. Save the credential

## Configuration

### Template Setup
Before using this node, you need to:

1. Create templates in your Contentdrips dashboard
2. Label the elements you want to update dynamically:
   - Right-click on textboxes or images in the template editor
   - Select "Add Label" and give it a name (e.g., `title_1`, `hashtag_1`)
   - Use these labels in your n8n workflow to update content

### Execution Modes

The node supports two execution modes:

#### Synchronous Mode (Default - Recommended)
- **What it does**: Waits for job completion and returns final download URLs
- **Best for**: Most use cases where you want the final result immediately
- **Settings**: Configure polling interval (1-60 seconds) and max wait time (1-60 minutes)
- **Result**: Returns final download URLs and processing time

#### Asynchronous Mode (Advanced)
- **What it does**: Returns job ID immediately for manual status checking
- **Best for**: Complex workflows requiring parallel processing or custom job management
- **Usage**: Use with Job operations (Get Status, Get Result) for manual polling

### Supported Output Formats
- **PNG**: High-quality raster images 
- **PDF**: Perfect for print and professional documents

### Basic Usage

#### Creating a Static Graphic (Synchronous)

```json
{
  "resource": "graphic",
  "operation": "create",
  "templateId": "126130",
  "executionMode": "sync",
  "output": "png",
  "contentUpdates": {
    "updates": [
      {
        "type": "textbox",
        "label": "title_1",
        "value": "My Dynamic Title"
      },
      {
        "type": "textbox", 
        "label": "hashtag_1",
        "value": "#automation"
      }
    ]
  }
}
```

#### Creating a Carousel with Auto-Wait

```json
{
  "resource": "carousel",
  "operation": "create", 
  "templateId": "126130",
  "executionMode": "sync",
  "pollingInterval": 5,
  "maxWaitTime": 10,
  "output": "png",
  "enableIntroSlide": true,
  "introSlideHeading": "Welcome!",
  "introSlideDescription": "Let's get started",
  "contentSlidesInputMethod": "ui",
  "contentSlides": {
    "slide": [
      {
        "heading": "Step 1",
        "description": "First step details"
      },
      {
        "heading": "Step 2", 
        "description": "Second step details"
      }
    ]
  },
  "enableEndingSlide": true,
  "endingSlideHeading": "Thank you!",
  "endingSlideDescription": "Follow for more tips"
}
```

#### Advanced: Asynchronous Mode with Manual Job Management

```json
{
  "resource": "carousel",
  "operation": "create", 
  "templateId": "126130",
  "executionMode": "async",
  "output": "pdf",
  "contentSlidesInputMethod": "json",
  "contentSlidesJson": "{{ $json.dynamicSlides }}"
}
```

Then use Job operations:
1. **Job > Get Status** to check processing status
2. **Job > Get Result** to get final download URLs

### Flexible Carousel Structure

**Intro Slide** (Optional):
- Enable/disable toggle
- When enabled: heading, description, and image fields automatically appear

**Content Slides** (Main content):
- **Method 1 - Build in UI**: Manually add slides using the interface
- **Method 2 - JSON Expression**: Use dynamic data with expressions like `{{ $json.slides }}`

**Ending Slide** (Optional):
- Enable/disable toggle  
- When enabled: heading, description, and image fields automatically appear

### Branding

You can include branding information that will be automatically applied to templates with branding placeholders:

```json
{
  "addBranding": true,
  "branding": {
    "name": "John Doe",
    "handle": "@johndoe",
    "bio": "Content Creator & Marketer",
    "website_url": "https://johndoe.com",
    "avatar_image_url": "https://example.com/avatar.jpg"
  }
}
```

## Workflow Examples

### Simple Content Generation (Single Node)
```
Trigger → Contentdrips (Sync Mode) → Save to Drive
```
Perfect for most use cases - one node handles everything from creation to completion.

### Advanced Parallel Processing
```
Trigger → Split Data → Multiple Contentdrips (Async) → Job Status Checks → Job Results → Merge
```
For processing multiple graphics/carousels in parallel with custom job management.

### Social Media Automation
Create a workflow that:
1. Triggers on a schedule
2. Fetches content from a CMS or spreadsheet
3. Uses Contentdrips to generate social media graphics (sync mode)
4. Posts to social platforms automatically

### Marketing Campaign Generator
Build a workflow that:
1. Reads campaign data from Google Sheets
2. Generates branded graphics for each campaign (sync mode)
3. Stores results in cloud storage
4. Sends notification emails with download links

### Dynamic Content with Variable Slides
```
Google Sheets → Transform Data → Contentdrips (JSON method) → Cloud Storage
```

**Code Node example** to transform spreadsheet data:
```javascript
// Input: Array of tips from spreadsheet
const tips = $input.all()[0].json.tips;

// Transform to Contentdrips format
const slides = tips.map((tip, index) => ({
  heading: tip.title,
  description: tip.description,
  image: tip.image_url || `https://example.com/slide${index + 1}.jpg`
}));

return [{
  json: {
    slides: slides
  }
}];
```

## Troubleshooting

### Common Issues

**Authentication Errors**
- Verify your API token is correct
- Check that the token has proper permissions
- Ensure you're using the latest version of the node

**Template Errors**
- Confirm the template ID exists in your Contentdrips account
- Verify that labeled elements match your content updates
- Check that required fields are provided

**Job Processing (Sync Mode)**
- Jobs typically take 2-5 minutes to process
- Adjust polling interval and max wait time if needed
- Failed jobs will include error details in the response

**Job Processing (Async Mode)**
- Use the Job Status operation to monitor progress
- Failed jobs will include error details in the response

### Performance Tips

- **Sync Mode**: Use for individual graphics or when you need immediate results
- **Async Mode**: Use for batch processing or when integrating with other time-sensitive operations
- **Polling Settings**: Balance between responsiveness (shorter intervals) and API usage (longer intervals)

### Getting Help

- Check the [Contentdrips API documentation](https://app.contentdrips.com/api-management)
- Visit the [n8n community forum](https://community.n8n.io)
- Report bugs on the [GitHub repository](https://github.com/cho-media/n8n-nodes-contentdrips-api/issues)

## Resources

- [Contentdrips Website](https://contentdrips.com)
- [Contentdrips API Documentation](https://app.contentdrips.com/api-management)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)

## Compatibility

- Minimum n8n version: 0.198.0
- Tested with n8n version: 1.0.0+
- Node.js version: 20.15+

## Version History

### 1.2.0
- **NEW**: Synchronous execution mode (default) - automatically wait for job completion
- **NEW**: Asynchronous execution mode - return job ID immediately for advanced workflows
- **NEW**: Configurable polling settings (interval and timeout)
- **IMPROVED**: Enhanced error handling and status reporting
- **IMPROVED**: Better user experience with automatic completion waiting
- **FIXED**: Icon display issues in n8n interface
- **REMOVED**: Gulp dependency for cleaner builds

### 1.1.3
- Bug fixes and stability improvements

### 1.0.0
- Initial release
- Support for creating static graphics and carousels
- Job status and result management
- Branding and content update features
- Full API coverage for Contentdrips v1

## License

[MIT](LICENSE.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
