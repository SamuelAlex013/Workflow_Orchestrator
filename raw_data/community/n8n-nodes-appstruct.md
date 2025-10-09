# n8n-nodes-appstruct

![AppStruct Logo](https://raw.githubusercontent.com/AppStructAI/n8n-nodes-appstruct/main/Logo.svg)

This is an n8n community node that lets you use [AppStruct](https://appstruct.ai) in your n8n workflows.

AppStruct is a no-code backend platform that lets you create APIs, databases, and backend logic without writing code.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Projects
- **Get Many**: Retrieve all projects from your AppStruct account

### Tables  
- **Get Many**: List all tables in a project
- **Create**: Create a new table
- **Get Schema**: Get table structure and column information
- **Delete**: Remove a table

### Records
- **Get Many**: Retrieve records from a table with optional limit
- **Create**: Insert a new record into a table
- **Update**: Modify an existing record
- **Delete**: Remove a record from a table

### Columns
- **Add**: Add a new column to an existing table

## Credentials

You need to configure AppStruct API credentials:

1. **Email**: Your AppStruct account email
2. **Password**: Your AppStruct account password

The node will automatically handle authentication and obtain access tokens.

## Compatibility

This node is compatible with n8n version 1.0.0 and above.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [AppStruct Documentation](https://appstruct.cloud/docs)
- [GitHub Repository](https://github.com/AppStructAI/n8n-nodes-appstruct)

## License

MIT

## Support

For support, please contact [support@appstruct.cloud](mailto:support@appstruct.cloud) or visit [AppStruct website](https://appstruct.cloud).