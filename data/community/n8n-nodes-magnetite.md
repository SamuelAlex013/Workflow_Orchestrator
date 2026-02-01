# n8n-nodes-magnetite

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node for [Magnetite](https://magnetite.ai). It lets you generate AI-powered, personalized lead magnets directly in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-magnetite` in **Enter npm package name**.
4. Agree to the risks of installing unverified code from a public source.
5. Select **Install**.

After installing the node, you can use it like any other node in your workflows.

## Operations

### Lead Magnet

- **Generate**: Create a personalized lead magnet for a lead
- **Get Status**: Retrieve the status of a lead magnet generation job

## Credentials

This node requires a Magnetite API key. You can obtain this from your Magnetite dashboard:

1. Log in to your [Magnetite dashboard](https://app.magnetite.ai)
2. Go to **Project Settings** → **API & Integrations**
3. Copy your API key

Configure the credentials in n8n:
- **API Key**: Your Magnetite API key
- **Base URL**: `https://app.magnetite.ai` (default)

## Compatibility

- Minimum n8n version: 0.198.0
- Tested up to n8n version: 1.98.1

## Usage

### Basic Lead Magnet Generation

1. Add the **Magnetite** node to your workflow
2. Set **Operation** to **Generate**
3. Configure the required fields:
   - **Project ID**: Your Magnetite project ID
   - **Email**: Lead's email address
4. Optionally add lead information:
   - Full Name, Company, Domain, Industry, etc.
5. Add custom fields as JSON if your project requires them

### Checking Generation Status

1. Use the **Get Status** operation
2. Provide the **Job ID** from a previous generation request
3. The node returns the current status and results when complete

### Example Workflow

```json
{
  "nodes": [
    {
      "name": "Magnetite",
      "type": "n8n-nodes-magnetite.magnetite",
      "parameters": {
        "operation": "generate",
        "projectId": "proj_abc123",
        "email": "{{$json.email}}",
        "leadData": {
          "fullName": "{{$json.name}}",
          "company": "{{$json.company}}"
        }
      }
    }
  ]
}
```

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Magnetite help](https://help.magnetite.ai)
- [Magnetite API documentation](https://app.magnetite.ai/docs)

## Version history

### 1.0.4
- Updated API docs url to https://app.magnetite.ai/docs

### 1.0.2
- Fixed credential test endpoint
- Improved connection reliability

### 1.0.1
- Updated GitHub repository URL
- Documentation improvements

### 1.0.0
- Initial release
- Generate lead magnets
- Check generation status
- Support for all standard lead fields
- Custom fields support via JSON
- Webhook notifications support

## License

[MIT](https://github.com/MagnetiteAI/n8n-nodes-magnetite/blob/main/LICENSE)