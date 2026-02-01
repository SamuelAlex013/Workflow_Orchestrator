# n8n-nodes-ministryplatform

![n8n](https://img.shields.io/badge/n8n-Community%20Node-blue)
![npm](https://img.shields.io/npm/v/n8n-nodes-ministryplatform)
![license](https://img.shields.io/npm/l/n8n-nodes-ministryplatform)

This is an n8n community node that lets you use MinistryPlatform in your n8n workflows.

[MinistryPlatform](https://ministryplatform.com/) is a comprehensive church management system that provides tools for managing contacts, events, donations, groups, and more. This integration allows you to automate workflows between MinistryPlatform and other systems.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Features

- **Organized Resource Interface**: Clean separation between Table and Stored Procedure operations
- **Full CRUD Operations**: Create, Read, Update, and Delete records in any MinistryPlatform table
- **Stored Procedure Support**: Execute stored procedures with parameters and retrieve all available procedures
- **OAuth2 Client Credentials**: Secure server-to-server authentication with automatic token management
- **Advanced Filtering**: Use MS SQL syntax for complex queries
- **Pagination Support**: Handle large datasets efficiently
- **All Tables Supported**: Works with any table in your MinistryPlatform instance
- **AI Tool Compatible**: Can be used as a tool in AI workflows and agents

## Installation

### Community Nodes (Recommended)

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) for your n8n setup to install `n8n-nodes-ministryplatform`.

### Manual Installation

### Docker Installation

#### Option 1: Manual Installation 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ACST-Innovation/ministryplatform-n8n.git
   cd ministryplatform-n8n
   ```

2. **Install dependencies and build:**
   ```bash
   npm install
   npm run build
   ```

3. **Copy to n8n Docker container:**
   ```bash
   # Copy the entire project to the custom extensions directory
   docker cp . n8n:/home/node/.n8n/custom/ministryplatform-n8n/
   
   # Fix file permissions
   docker exec -it n8n chown -R node:node /home/node/.n8n/custom/
   ```

4. **Set environment variable and restart:**
   
   **Important:** Use absolute path, not tilde (`~`)
   
   ```bash
   # Stop container
   docker stop n8n
   
   # Remove old container
   docker rm n8n
   
   # Start with custom extensions environment variable
   docker run -d \
     --name n8n \
     -p 5678:5678 \
     -e N8N_CUSTOM_EXTENSIONS=/home/node/.n8n/custom \
     -v n8n_data:/home/node/.n8n \
     n8nio/n8n:latest
   ```

#### Option 2: Custom Docker Build (ECR Ready)

Build a custom n8n image with the MinistryPlatform node pre-installed:

1. **Build custom image:**
   ```bash
   # Use any custom Dockerfile that includes this setup
   docker build -t n8n-ministryplatform .
   ```

2. **Run the custom image:**
   ```bash
   docker run -d \
     --name n8n \
     -p 5678:5678 \
     -v n8n_data:/home/node/.n8n \
     n8n-ministryplatform
   ```

3. **ECR Deployment:**
   - Tag and push to ECR: `docker tag n8n-ministryplatform:latest your-ecr-repo:latest`
   - Deploy anywhere with the node pre-installed
   - No manual setup required

### NPM Installation

For self-hosted n8n instances, you can install directly via npm:

```bash
npm install n8n-nodes-ministryplatform
```

Then restart your n8n instance to load the new node.

## Operations

The MinistryPlatform node is organized into two main resources for better usability:

### Table Operations

Direct access to MinistryPlatform's table API, allowing you to work with any table in your MinistryPlatform instance.

**Available Operations:**
- **Create**: Add new records to any table
- **Get**: Retrieve a specific record by ID
- **List**: Retrieve multiple records with filtering and pagination
- **Update**: Modify existing records
- **Delete**: Remove records

**Table Configuration:**

For all operations, you need to specify:
- **Table Name**: The exact name of the MinistryPlatform table (e.g., `Contacts`, `Events`, `Donations`, `Households`)

**List Operation Parameters:**

The List operation supports these query parameters:

- **select**: Comma-separated list of fields to return (e.g., `Contact_ID,Display_Name,Email_Address`)
- **filter**: MS SQL WHERE clause syntax (e.g., `Contact_ID > 1000`, `Email_Address='user@example.com'`)
- **orderby**: Field to sort by (e.g., `Display_Name asc`, `Created_Date desc`)
- **groupby**: Field to group results by
- **having**: Having clause for grouped results
- **top**: Maximum number of records to return (e.g., `100`)
- **skip**: Number of records to skip for pagination (e.g., `50`)
- **distinct**: Return only unique records (boolean)
- **userId**: User ID for context-sensitive queries
- **globalFilterId**: Apply a global filter by ID

### Stored Procedure Operations

Access to MinistryPlatform's stored procedure API for executing predefined procedures.

**Available Operations:**
- **Get All**: Retrieve a list of all available stored procedures with metadata
- **Execute**: Execute a specific stored procedure with JSON parameters

**Stored Procedure Configuration:**
- **Stored Procedure Name**: The name of the procedure to execute (e.g., `api_Common_GetLookupRecords`)
- **Parameters**: JSON object containing parameters to pass to the procedure (e.g., `{"DomainID": 1, "Congregation_ID": 5}`)

### MS SQL Filter Examples

```
# String equality (use single quotes)
Email_Address='john@example.com'

# String contains (LIKE with wildcards)
Display_Name LIKE '%Smith%'

# Number comparison
Contact_ID > 1000

# Date comparison  
Created_Date >= '2024-01-01'

# Multiple conditions
Contact_ID > 1000 AND Email_Address LIKE '%gmail.com%'

# Null checks
Email_Address IS NOT NULL

# IN clause
Contact_ID IN (1001, 1002, 1003)
```

### Common Table Names

- `Contacts` - Contact records
- `Events` - Event records
- `Donations` - Donation records
- `Households` - Household records
- `Participants` - Event participants
- `Groups` - Group records
- `Users` - User accounts

## Credentials

This node uses OAuth2 Client Credentials flow for server-to-server authentication. You'll need to configure:

### MinistryPlatform OAuth App Setup
1. Create an OAuth application in your MinistryPlatform instance
2. Configure it for **Client Credentials** grant type (no redirect URI needed)
3. Note down your Client ID and Client Secret

### n8n Credential Configuration
In n8n, create new MinistryPlatform API credentials with:

1. **Base URL**: Your MinistryPlatform base URL (e.g., `https://your-instance.ministryplatform.com`)
2. **Client ID**: From your MinistryPlatform OAuth app
3. **Client Secret**: From your MinistryPlatform OAuth app
4. **Scope**: `http://www.thinkministry.com/dataplatform/scopes/all`

**Note:** Replace `your-instance` with your actual MinistryPlatform subdomain. This uses the Client Credentials flow which is ideal for server-to-server automation.

## Troubleshooting

### Node Not Appearing
- Ensure `N8N_CUSTOM_EXTENSIONS` uses absolute path: `/home/node/.n8n/custom` (not `~/.n8n/custom`)
- Verify file permissions: `docker exec -it n8n chown -R node:node /home/node/.n8n/custom/`
- Check n8n logs: `docker logs n8n`

### OAuth Issues
- Ensure MinistryPlatform OAuth app is configured for Client Credentials grant type
- Verify Client ID and Client Secret are correct
- Check that the scope `http://www.thinkministry.com/dataplatform/scopes/all` is properly configured
- **Token Management**: Tokens are automatically managed and refreshed by the node

### Filter Issues
- Use single quotes for string values: `Email_Address='user@example.com'`
- Use standard SQL operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Use `LIKE '%text%'` for contains, not `contains()`
- Check field names match exactly (case-sensitive)
- Use `AND`/`OR` for multiple conditions, not `and`/`or`

### Query Parameter Issues
- **Top parameter ignored**: If using List operation, ensure you're setting the `top` parameter in the Additional Fields, not expecting automatic pagination
- **All records returned**: The `top` parameter is now respected - if not set, all records will be paginated and returned

### Build Issues
- Run `npm install` before `npm run build`
- Check for TypeScript compilation errors
- Ensure all dependencies are installed

## Development

### Build Commands
- `npm run build` - Compile TypeScript and build icons
- `npm run dev` - Watch mode for development
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## Compatibility

Tested with n8n version 1.0+

## Testing

### Postman Collection

A Postman collection is included in the `postman/` directory for testing the MinistryPlatform API directly:

- **Collection**: `postman/MinistryPlatform-API.postman_collection.json`
- **Documentation**: `postman/README.md`

The collection includes examples for all operations (Create, Get, List, Update, Delete) with proper OAuth2 configuration.

## Examples

### Table Operations Examples

#### List Contacts with Email Filtering
Configure the MinistryPlatform node with:
- **Resource**: Table
- **Operation**: List
- **Table Name**: `Contacts`
- **Additional Fields**:
  - **Select**: `Contact_ID,Display_Name,Email_Address,Mobile_Phone`
  - **Filter**: `Email_Address LIKE '%gmail.com%'`
  - **Order By**: `Display_Name ASC`
  - **Top**: `50`

#### Create New Contact
Configure the MinistryPlatform node with:
- **Resource**: Table
- **Operation**: Create
- **Table Name**: `Contacts`
- **Records**: 
```json
[{
  "Display_Name": "John Smith",
  "Email_Address": "john.smith@example.com",
  "Mobile_Phone": "555-123-4567",
  "First_Name": "John",
  "Last_Name": "Smith"
}]
```

#### Update Contact Information
Configure the MinistryPlatform node with:
- **Resource**: Table
- **Operation**: Update
- **Table Name**: `Contacts`
- **Records**:
```json
[{
  "Contact_ID": 1234,
  "Email_Address": "newemail@example.com",
  "Mobile_Phone": "555-987-6543"
}]
```

#### Get Specific Event
Configure the MinistryPlatform node with:
- **Resource**: Table
- **Operation**: Get
- **Table Name**: `Events`
- **Record ID**: `789` (Event_ID)

### Stored Procedure Operations Examples

#### Get All Available Stored Procedures
Configure the MinistryPlatform node with:
- **Resource**: Stored Procedure
- **Operation**: Get All

#### Execute Stored Procedure with Parameters
Configure the MinistryPlatform node with:
- **Resource**: Stored Procedure
- **Operation**: Execute
- **Stored Procedure**: `api_Common_GetLookupRecords`
- **Parameters**:
```json
{
  "DomainID": 1,
  "Congregation_ID": 5,
  "UserID": 123
}
```

## Changelog

### Version 1.1.0
- **NEW**: Organized interface with Resource → Operation structure (Table Actions / Stored Procedure Actions)
- **NEW**: Stored Procedure support with Get All and Execute operations  
- **NEW**: AI Tool compatibility for use in AI workflows and agents
- **NEW**: Released to npm package registry
- **IMPROVED**: Better parameter validation with proper n8n error types
- **IMPROVED**: Updated documentation with new structure and examples

### Version 1.0.1
- Updated documentation for OAuth2 Client Credentials flow
- Improved examples with step-by-step configuration
- Enhanced error handling and token management
- Updated branding and contact information
- Fixed credential test authorization issue

### Version 1.0.0
- Initial release
- Full CRUD operations for all MinistryPlatform tables
- OAuth2 Client Credentials authentication
- MS SQL syntax filtering
- Pagination support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions:
- GitHub Issues: [Report a bug or request a feature](https://github.com/ACST-Innovation/ministryplatform-n8n/issues)
- n8n Community: [Get help from the community](https://community.n8n.io/)

## License

MIT - see [LICENSE](LICENSE) file for details.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [MinistryPlatform Developer Resources](https://help.acst.com/en/ministryplatform/developer-resources/developer-resources)
* [MinistryPlatform Tables API Documentation](https://help.acst.com/en/ministryplatform/developer-resources/developer-resources/rest-api/tables)
