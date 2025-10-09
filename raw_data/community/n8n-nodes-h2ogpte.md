# n8n-nodes-h2ogpte

This is an n8n community node that integrates n8n with h2oGPTe.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/) in the n8n community nodes documentation.

## Configuration

Before using this node, you need to configure your h2oGPTe credentials:

### Step 1: Create API Key

1. Log in to <https://h2ogpte.genai.h2o.ai>
2. Navigate to Settings > API Keys and create or get the API key.

### Step 2: Create h2oGPTe Credentials on your n8n instance

1. In n8n, go to Settings → Credentials
2. Add a new credential for "h2oGPTe API"
3. Enter your h2oGPTe instance URL (e.g., <https://h2ogpte.genai.h2o.ai>) and API token (e.g., sk-...)

## Supported Resources

This node provides full coverage of the h2oGPTe API. Additional documentation about the h2oGPTe API can be found in the official [h2oGPTe documentation](https://h2oai.github.io/h2ogpte/index.html).

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
