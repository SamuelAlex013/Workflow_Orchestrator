# n8n-nodes-formaloo

This package provides n8n nodes for integrating with [Formaloo](https://formaloo.com), a form builder platform.

## Nodes

### Formaloo Trigger
- **Node Name**: `Formaloo Trigger`
- **Type**: Trigger
- **Description**: Triggers workflows when forms are submitted or updated in Formaloo
- **Events Supported**:
  - Form Submit
  - Row Update
  - Payment Completed
  - All Events

### Formaloo Action
- **Node Name**: `Formaloo`
- **Type**: Action
- **Description**: Submit data to Formaloo forms with advanced field type handling
- **Operations**:
  - Submit Form: Submit data to a specific Formaloo form with automatic field type conversion

## Credentials

The nodes require Formaloo API credentials with the following fields:
- **Secret API**: Your Formaloo secret API key (used for JWT authentication)
- **API Key**: Your Formaloo API key (used for API requests)

These credentials are used to:
1. Generate JWT tokens for authentication
2. Make API requests to Formaloo endpoints
3. Create and manage webhooks

### Prerequisites
- A Formaloo account with API access
- Your Formaloo Secret API key
- Your Formaloo API key

## Compatibility

- **Minimum n8n version**: 0.1.0
- **Tested with n8n version**: 1.17.0+
- **Node.js version**: 20+

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Alternatively, you can install manually:

1. Install the package:
   ```bash
   npm install n8n-nodes-formaloo
   ```

2. Add the nodes to your n8n instance by copying the `dist` folder to your n8n custom nodes directory.

## Usage

### Setting up the Trigger Node

1. Add a "Formaloo Trigger" node to your workflow
2. Configure your Formaloo API credentials
3. Select the form you want to monitor
4. Choose the event type (form submit, row update, etc.)
5. The node will create a webhook in Formaloo and trigger your workflow when events occur

### Setting up the Action Node

1. Add a "Formaloo" node to your workflow
2. Configure your Formaloo API credentials
3. Select the form you want to submit to
4. Add form fields with their IDs and values
5. The node automatically handles field type conversion for complex fields

For new users, check out the [Try it out](https://docs.n8n.io/try-it-out/) documentation to get started with n8n.

## Field Types

### Unsupported Field Types
The following field types are currently **not supported** and will be filtered out from the field selection:
- `matrix` - Matrix fields
- `table` - Table fields
- `lookup` - Lookup fields
- `user` - User fields
- `profile` - Profile fields
- `linked_rows` - Linked rows fields
- `repeating_section` - Repeating section fields

### Multiple Choice Fields
For **Multiple Select** fields, use comma-separated values to select multiple options:

**Example:**
```
Field Value: "Option 1, Option 2, Option 3"
```

**Note:** Make sure to use the exact option titles as they appear in your Formaloo form.

### City/Country Fields
For **City** and **Country** fields, the node automatically searches and maps your input to the correct Formaloo option:

**Example:**
```
Field Value: "New York" or "United States"
```

The node will automatically find the matching city/country and submit the correct slug.

## API Endpoints

The nodes use the following Formaloo API endpoints:
- **Forms List**: `GET https://api.formaloo.me/v3.0/forms/`
- **Form Details**: `GET https://api.formaloo.me/v3.0/forms/{formSlug}/`
- **Webhooks**: `POST/GET/DELETE https://api.formaloo.me/v3.0/forms/{formSlug}/webhooks/`
- **Form Submit**: `POST https://api.formaloo.me/v3.0/form-displays/slug/{formSlug}/submit/`
- **Field Options**: `GET https://api.formaloo.me/v3.0/forms/{formSlug}/fields/{fieldSlug}/choices/`
- **City/Country Search**: `GET https://api.formaloo.me/v3.0/forms/{formSlug}/fields/{fieldSlug}/choices/`

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Formaloo API Documentation](https://docs.formaloo.com/)
* [Formaloo Website](https://formaloo.com)

## Development

1. Clone the repository
2. Install dependencies: `npm install`
3. Build the project: `npm run build`
4. Test locally with n8n

## Version History

### 0.1.0
- Initial release
- Support for Formaloo Trigger node
- Support for Formaloo Action node
- JWT authentication
- Webhook management
- Form submission with field type handling

## License

[MIT](LICENSE.md)
