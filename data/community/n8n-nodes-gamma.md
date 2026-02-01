# n8n-nodes-gamma

This is an n8n community node that lets you use [Gamma](https://gamma.app) in your n8n workflows.

Gamma is an AI-powered platform for creating beautiful presentations, documents, and social media posts. This node allows you to automate content generation using Gamma's API directly from your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Generate
Create a new Gamma presentation, document, or social post with AI-powered generation.

**Parameters:**
- **Input Text** (required): Text used to generate your gamma. Can be as little as a few words or pages of text (1-750,000 characters)
- **Text Mode**: How your input text is modified
  - `generate`: Rewrite and expand content (default)
  - `condense`: Summarize to fit content length
  - `preserve`: Retain exact text
- **Format**: Type of artifact to create
  - `presentation` (default)
  - `document`
  - `social`

**Additional Options:**
- **Theme Name**: Choose from 90+ Gamma themes (e.g., "Oasis", "Night Sky", "Coral Glow")
- **Number of Cards**: How many cards to create (Pro: 1-50, Ultra: 1-75)
- **Card Split**: How content is divided (`auto` or `inputTextBreaks`)
- **Additional Instructions**: Extra specifications about content and layouts (1-500 characters)
- **Export As**: Export to PDF or PPTX

**Text Options:**
- **Amount**: How much text per card (`brief`, `medium`, `detailed`, `extensive`)
- **Tone**: Mood or voice of the gamma (e.g., "professional and inspiring")
- **Audience**: Intended readers/viewers (e.g., "tech investors")
- **Language**: Output language (60+ languages supported, including English, Spanish, French, Chinese, etc.)

**Image Options:**
- **Source**: Where to source images
  - `aiGenerated` (default)
  - `pictographic`
  - `unsplash`
  - `giphy`
  - `webAllImages`
  - `webFreeToUse`
  - `webFreeToUseCommercially`
  - `placeholder`
  - `noImages`
- **Model**: AI image generation model (21 models available, 2-120 credits per image)
- **Style**: Artistic style description for AI-generated images

**Card Options:**
- **Dimensions**: Aspect ratio (format-specific options)
  - Presentation: `fluid`, `16x9`, `4x3`
  - Document: `fluid`, `pageless`, `letter`, `a4`
  - Social: `1x1`, `4x5`, `9x16`

**Sharing Options:**
- **Workspace Access**: Access level for workspace members (`noAccess`, `view`, `comment`, `edit`, `fullAccess`)
- **External Access**: Access level for external users (`noAccess`, `view`, `comment`, `edit`)

**Returns:**
- `generationId`: ID to check generation status
- `warnings`: Any parameter conflicts or issues (if applicable)

### Get Status
Get the status and URLs of a gamma generation.

**Parameters:**
- **Generation ID** (required): The generation ID returned from the Generate operation

**Returns:**
- `status`: Generation status (`pending` or `completed`)
- `generationId`: The generation ID
- `gammaUrl`: URL to view the gamma (when completed)
- `credits`: Credit information
  - `deducted`: Credits used for generation
  - `remaining`: Credits remaining in account

## Credentials

To use this node, you need a Gamma API key.

1. Sign up for a [Gamma Pro or Ultra account](https://gamma.app)
2. Navigate to your API settings to generate an API key
3. The API key format is: `sk-gamma-xxxxxxxxxx`

In n8n:
1. Go to **Credentials** → **New**
2. Search for "Gamma API"
3. Enter your API key
4. Click **Save**

**Note:** The Gamma API is currently in beta. Functionality, rate limits, and pricing are subject to change.

## Compatibility

- Minimum n8n version: 1.0.0
- Tested with n8n version: 1.113.3

## Usage

### Example 1: Generate a Presentation

1. Add the Gamma node to your workflow
2. Select **Generate** operation
3. Enter your **Input Text**: "Create a pitch deck about sustainable energy solutions"
4. Select **Text Mode**: Generate
5. Select **Format**: Presentation
6. In **Additional Options**:
   - Set **Theme Name**: "Oasis"
   - Set **Number of Cards**: 10
7. In **Text Options**:
   - Set **Amount**: Detailed
   - Set **Tone**: "professional and inspiring"
   - Set **Audience**: "investors and entrepreneurs"
8. Execute the node
9. Use the returned `generationId` in a **Get Status** node to check progress

**cURL Request:**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "Create a pitch deck about sustainable energy solutions",
    "textMode": "generate",
    "format": "presentation",
    "themeName": "Oasis",
    "numberOfCards": 10,
    "textOptions": {
      "amount": "detailed",
      "tone": "professional and inspiring",
      "audience": "investors and entrepreneurs"
    }
  }'
```

### Example 2: Check Generation Status

1. Add a Gamma node (or reuse existing)
2. Select **Get Status** operation
3. Enter the **Generation ID** from a previous Generate operation
4. Execute to see if generation is complete and get the Gamma URL

**cURL Request:**
```bash
curl -X GET https://api.gamma.app/api/v0.2/status/GENERATION_ID_HERE \
  -H "X-API-KEY: YOUR_API_KEY_HERE"
```

### Example 3: Generate Social Media Post

1. Add the Gamma node
2. Select **Generate** operation
3. Enter **Input Text**: "5 tips for productivity"
4. Select **Format**: Social
5. In **Card Options**:
   - Set **Dimensions**: 4x5 (Instagram/LinkedIn)
6. In **Image Options**:
   - Set **Source**: AI Generated
   - Set **Model**: Flux Fast 1.1 (2 credits)
   - Set **Style**: "minimal, colorful, modern"
7. Execute and get your social media content

**cURL Request:**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "5 tips for productivity",
    "format": "social",
    "cardOptions": {
      "dimensions": "4x5"
    },
    "imageOptions": {
      "source": "aiGenerated",
      "model": "flux-fast-1.1",
      "style": "minimal, colorful, modern"
    }
  }'
```

### Example 4: Automated Educational Mini-Books

Generate beautiful educational mini-books instantly using AI. Perfect for teachers, students, and educational content creators.

1. **Trigger**: Form submission or schedule
2. **Input**: Topic from form (e.g., "Introduction to Photosynthesis")
3. **Gamma Node**: Generate operation
   - **Format**: Document
   - **Text Mode**: Generate
   - **Additional Options**: Set Number of Cards to 8-12
   - **Text Options**: Set Audience to "middle school students"
4. **Output**: Educational document ready for classroom use

**cURL Request:**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "Introduction to Photosynthesis",
    "textMode": "generate",
    "format": "document",
    "numberOfCards": 10,
    "textOptions": {
      "audience": "middle school students"
    }
  }'
```

### Example 5: Automated Client Onboarding Presentations

Our agent automates client onboarding by taking webform data, performing deep research, and generating custom presentations.

**Workflow:**
1. **Trigger**: New client onboarding form submitted
2. **HTTP Request Node**: Fetch client information from webform
3. **OpenAI Node**: Research client company and industry
4. **OpenAI Node**: Generate 20-30 slide presentation outline based on knowledge base rules
5. **Gamma Node - Generate**: Create presentation with AI-generated content
   - **Input Text**: Use the outline from OpenAI
   - **Format**: Presentation
   - **Export As**: PPTX
   - **Additional Options**: Set theme matching client brand
6. **Gamma Node - Get Status**: Check generation status and retrieve download URL
7. **Slack Node**: Send PPTX download link to team channel

**cURL Request (Generate):**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "Your detailed client onboarding presentation outline here...",
    "textMode": "preserve",
    "format": "presentation",
    "numberOfCards": 25,
    "exportAs": "pptx",
    "themeName": "Consultant"
  }'
```

**cURL Request (Get Status):**
```bash
curl -X GET https://api.gamma.app/api/v0.2/status/GENERATION_ID_HERE \
  -H "X-API-KEY: YOUR_API_KEY_HERE"
```

### Example 6: Automated Sales Presentations from CRM

Create personalized sales presentations automatically when meetings are scheduled.

**Workflow:**
1. **HubSpot Trigger**: New meeting scheduled
2. **HubSpot Node**: Fetch lead information and company data
3. **OpenAI Node**: Research lead and gather relevant information
4. **OpenAI Node**: Generate sales presentation outline tailored to lead
5. **Gamma Node - Generate**: Create professional sales deck
   - **Input Text**: Sales outline from OpenAI
   - **Format**: Presentation
   - **Text Options**:
     - Tone: "professional and persuasive"
     - Audience: Lead's industry and role
   - **Theme Name**: Select professional theme (e.g., "Consultant")
6. **Email/Slack**: Send presentation link to sales rep

**cURL Request:**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "Your personalized sales presentation outline here...",
    "textMode": "generate",
    "format": "presentation",
    "themeName": "Consultant",
    "textOptions": {
      "tone": "professional and persuasive",
      "audience": "enterprise technology decision makers"
    }
  }'
```

### Example 7: Investment Memo to Presentation Pipeline

Automate creation of investor presentations from investment memos containing text and images.

**Workflow:**
1. **Trigger**: New investment memo uploaded or created
2. **Extract Node**: Parse investment memo (text and image references)
3. **OpenAI Node**: Structure memo content into presentation format
4. **Gamma Node - Generate**: Create investor presentation
   - **Input Text**: Structured memo content
   - **Format**: Presentation
   - **Card Split**: Input Text Breaks (for manual control)
   - **Image Options**:
     - Source: AI Generated or Unsplash
     - Style: "professional, financial, clean"
   - **Text Options**:
     - Tone: "data-driven and persuasive"
     - Audience: "venture capital investors"
5. **Export**: Download as PPTX and store in company drive
6. **Notification**: Alert investment team of new presentation

**cURL Request:**
```bash
curl -X POST https://api.gamma.app/api/v0.2/generate \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_API_KEY_HERE" \
  -d '{
    "inputText": "Your structured investment memo content here...",
    "textMode": "preserve",
    "format": "presentation",
    "cardSplit": "inputTextBreaks",
    "exportAs": "pptx",
    "imageOptions": {
      "source": "aiGenerated",
      "style": "professional, financial, clean"
    },
    "textOptions": {
      "tone": "data-driven and persuasive",
      "audience": "venture capital investors"
    }
  }'
```

## Real-World Use Cases

- **Education**: Generate course materials, study guides, and lesson plans
- **Sales**: Automate pitch decks personalized for each prospect
- **Marketing**: Create campaign presentations and content calendars
- **Investment**: Transform memos into investor-ready presentations
- **Onboarding**: Generate custom client or employee onboarding materials
- **Content Creation**: Bulk-generate social media content with consistent branding
- **Reporting**: Convert data reports into visual presentations automatically

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Gamma API Documentation](https://developers.gamma.app)
* [Gamma Website](https://gamma.app)

## License

[MIT](LICENSE.md)
