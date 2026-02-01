# n8n-nodes-yourang

This is an n8n community node. It lets you use Yourang.ai in your n8n workflows.

Yourang.ai is a 24/7 AI phone assistant that handles calls, appointments, and customer interactions automatically. It provides intelligent call routing, appointment scheduling, transcription services, and customer data collection.

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

This node supports the following operations:

### Call History Operations
- **Get**: Retrieve details of a specific call by ID
- **Get All**: Retrieve all calls with optional filtering by sort order, call type, call status, outbound/inbound, phone number, and contact ID

### Contact Operations
- **Create**: Add a new customer contact with first name, phone number, and optional last name, email, and address
- **Update**: Modify existing contact information by contact ID
- **Get**: Retrieve details of a specific contact by contact ID
- **Delete**: Remove a contact by contact ID
- **Get All**: List all contacts with optional search and sort filters

### Action Operations
- **List Actions**: Retrieve available action configurations
- **Execute Single**: Execute an action for a single phone number using a configuration ID
- **Execute Batch Numbers**: Execute an action for multiple phone numbers (batch processing)
- **Execute Batch Contacts**: Execute an action for multiple contacts using contact IDs (batch processing)
- **Get Action History**: Retrieve action execution history with optional filtering by configuration ID and batch ID
- **Get Action History Details**: Get detailed information about a specific action execution
- **Get Batch History**: Retrieve batch execution history
- **Get Batch History Details**: Get detailed information about a specific batch execution

## Credentials

To use this node, you need to set up authentication with Yourang.ai:

1. Sign up for a Yourang.ai account at [yourang.ai](https://yourang.ai/)
2. Access your dashboard to generate an API key
3. In n8n, create new credentials for "Yourang API"
4. Enter your API key and base URL (default: https://api.yourang.ai/v1)

The node uses Bearer token authentication for all API requests.

## Compatibility

- **Minimum n8n version**: 0.87.0
- **Tested with**: n8n 1.105.4

## Usage

### Basic Workflow Examples

1. **Call History Analysis**: Monitor and analyze call history data to track performance metrics and customer interactions
2. **Contact Management**: Automatically create and update customer contacts in your CRM systems
3. **Automated Actions**: Execute single or batch phone calls using predefined action configurations
4. **Action Tracking**: Monitor and analyze action execution history for performance insights

### Common Use Cases

- Sync call history and contact data to external CRM systems
- Execute bulk phone campaigns using batch action operations
- Monitor action execution status and track campaign performance
- Automatically update contact information from call interactions
- Generate reports on action execution history and success rates

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Yourang.ai website](https://yourang.ai/)
* [Yourang.ai Developer Documentation](https://developers.yourang.ai/)

## License

[MIT](LICENSE.md)
