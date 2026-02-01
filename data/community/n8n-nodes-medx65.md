# n8n-nodes-medx65

This is an n8n community node that lets you interact with the MedX65 medical system API in your n8n workflows.

[MedX65](https://medx65-v65teste.azurewebsites.net) is a medical practice management system that provides API endpoints for managing appointments, patients, contacts, and users.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Agenda
- **Create**: Create a new agenda entry
- **Get**: Get agenda entries within a date range
- **Get by User**: Get agenda entries by specific user
- **Get by Sector**: Get agenda entries by sector
- **Update**: Update an existing agenda entry

### Contact
- **Create**: Create a new contact
- **Get by ID**: Get contact by ID
- **Search**: Search contacts by name, CPF, or phone

### Patient
- **Get All**: Get all patients

### User
- **Get Agenda Users**: Get all users available for agenda scheduling

### Sector
- **Get All**: Get all sectors
- **Get Status Names**: Get status names for agenda entries

## Credentials

The MedX65 node uses API credentials. You'll need:

1. **Integration Token**: Obtained from the MedX65 system under "Ajustes > integração para websites e links"
2. **Environment**: Choose between Production and Test environments

## Compatibility

This node has been tested with n8n version 1.0.0 and above.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [MedX65 API Documentation](https://medx65-v65teste.azurewebsites.net)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)