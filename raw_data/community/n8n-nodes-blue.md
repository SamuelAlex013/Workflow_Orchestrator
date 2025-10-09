# n8n-nodes-blue

This is an n8n community node. It lets you use Blue Project Management in your n8n workflows.

Blue Project Management is a modern project management platform that provides powerful GraphQL APIs for managing projects, tasks, teams, and workflows.

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

### Companies
- **Get Companies** - List all companies you have access to

### Projects  
- **Get Projects** - List all projects within a specific company

### Records (Tasks/Todos)
- **Get Records** - Retrieve tasks/todos with advanced filtering (by project, search terms, completion status)
- **Create Record** - Create new tasks/todos with support for assignees, tags, custom fields, and checklists
- **Update Record** - Update existing records including core fields and custom field values

### Advanced
- **Custom Query** - Execute custom GraphQL queries against the Blue API for advanced use cases

## Credentials

### Getting Blue API Credentials

1. **Create Blue Account**
   - Sign up for a Blue Project Management account at [blue.cc](https://blue.cc)
   - Complete account verification and setup

2. **Generate API Tokens**
   - Log into your Blue account
   - Navigate to Account Settings → API Settings
   - Generate a new API token pair:
     - **Token ID**: Your unique identifier (e.g., `abc123def456`)
     - **Token Secret**: Your authentication secret (keep this secure!)
   - Copy both values - you'll need them for n8n configuration

3. **Note Your Company Access**
   - Ensure you have access to at least one company in Blue
   - API operations require company context
   - You can be a member of multiple companies

### Configuring in n8n

1. **Add Blue API Credential**
   - In n8n, go to **Settings** → **Credentials**
   - Click **Add Credential** → Search for "Blue API"
   - Fill in the credential form:

2. **Credential Configuration**
   ```
   Base URL: https://api.blue.cc/graphql (default - don't change)
   Token ID: [Your Blue API Token ID]
   Token Secret: [Your Blue API Token Secret]
   ```

3. **Test Connection**
   - Click **Test** to verify your credentials
   - You should see a successful connection message
   - If test fails, double-check your Token ID and Secret

4. **Save Credential**
   - Give your credential a descriptive name (e.g., "Blue Production API")
   - Click **Save**

### Authentication Flow

The node automatically handles all authentication:
- **Headers**: Adds `X-Bloo-Token-ID` and `X-Bloo-Token-Secret` to requests
- **Company Context**: Passes `X-Bloo-Company-ID` based on your operation selections
- **GraphQL Endpoint**: Routes all requests to Blue's GraphQL API at `https://api.blue.cc/graphql`

### Security Notes

- **Keep Token Secret Secure**: Never share or commit your Token Secret
- **Rotate Tokens**: Regularly regenerate tokens for security
- **Company Access**: Tokens only work with companies you have access to
- **Rate Limits**: Blue API has rate limiting - implement appropriate delays in high-volume workflows

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with**: n8n 1.x
- **Node API version**: 1

## Usage

### Example Workflows

#### Workflow 1: Task Management Dashboard
Create a workflow that monitors and manages tasks across projects:

1. **Trigger**: Schedule (runs every hour)
2. **Blue - Get Companies**: Retrieve available companies
3. **Loop**: For each company:
   - **Blue - Get Projects**: Get all projects for the company
   - **Blue - Get Records**: Fetch incomplete tasks with search filter
   - **Filter**: Identify overdue tasks
   - **Send Email**: Notify project managers of overdue items

#### Workflow 2: Automated Task Creation
Set up task creation from external sources:

1. **Trigger**: Webhook (from form submission/external system)
2. **Blue - Get Companies**: Select target company
3. **Blue - Get Projects**: Find appropriate project by name
4. **Blue - Create Record**: Create new task with:
   - Title and description from webhook data
   - Assignees based on project team
   - Custom fields populated from form data
   - Tags for categorization

#### Workflow 3: Weekly Project Reports
Generate automated project status reports:

1. **Trigger**: Schedule (weekly)
2. **Blue - Get Companies**: Get all companies
3. **Loop**: For each company:
   - **Blue - Get Projects**: Retrieve active projects
   - **Blue - Get Records**: Get tasks with completion filter
   - **Calculate**: Progress metrics (completed vs total tasks)
   - **Format**: Create summary report
   - **Send to Slack/Email**: Distribute reports to stakeholders

#### Workflow 4: Custom Data Integration
Sync data between Blue and other systems:

1. **External API**: Fetch data from CRM/ERP system
2. **Transform**: Map external data to Blue format
3. **Blue - Custom Query**: Execute complex GraphQL query to check for existing records
4. **Conditional**: Create or update based on existence
5. **Blue - Create/Update Record**: Sync the data with custom fields populated

### Quick Start Guide

**Step 1: Set up Credentials**
1. In n8n, go to Credentials → Add Credential → Blue API
2. Enter your Blue API Token ID and Secret
3. Test the connection

**Step 2: Basic Flow**
1. Add Blue node to your workflow
2. Select "Get Companies" operation
3. Execute to see available companies
4. Copy a Company ID for next steps

**Step 3: Explore Operations**
- Use Company ID to get projects
- Select a project to retrieve tasks
- Create new tasks with the Create Record operation

### Advanced Features

- **Custom Fields**: Both create and update operations support Blue's custom field system with dynamic field selection
- **Multiselect Dropdowns**: Assignees and tags use dynamic dropdowns populated from your Blue data based on selected company/project
- **GraphQL Power**: Use the Custom Query operation for complex data operations beyond standard CRUD
- **Intelligent Filtering**: Records support rich filtering - combine project filtering with search terms for precise results
- **Error Handling**: Comprehensive GraphQL error handling with detailed error messages and suggestions

### Operation Details

#### Get Records Options
- **Project Filter**: Limit results to specific project
- **Search**: Find records containing specific text
- **Show Completed**: Include/exclude completed tasks
- **Pagination**: Control result size with limit/skip

#### Create Record Features
- **Rich Content**: Title, description, due dates
- **Team Assignment**: Multi-select assignees from project team
- **Categorization**: Apply multiple tags for organization
- **Custom Fields**: Populate any custom fields defined in your Blue setup
- **Checklists**: Add sub-tasks during creation

#### Custom Query Power
Execute any GraphQL query against Blue's API:
```graphql
query GetProjectStats($projectId: ID!) {
  project(id: $projectId) {
    name
    todos {
      totalCount
    }
    todosCompleted: todos(completed: true) {
      totalCount
    }
  }
}
```

### Tips & Best Practices

- **Company Context**: Company ID is automatically passed as header for all operations after selection
- **Performance**: Use pagination and filtering to limit large result sets
- **Error Recovery**: Implement error handling for API rate limits and network issues
- **Data Validation**: Validate required fields before creating/updating records
- **Webhook Integration**: Use Blue's webhook system with n8n triggers for real-time automation

## Troubleshooting

### Common Issues

#### Authentication Errors
**Problem**: "Invalid credentials" or "Unauthorized" errors
**Solutions**:
- Verify Token ID and Secret are correct (copy-paste to avoid typos)
- Check that tokens haven't expired or been revoked
- Ensure you have access to at least one company in Blue
- Test credentials using the credential test function

#### Empty Company List
**Problem**: "Get Companies" returns empty results
**Solutions**:
- Confirm your Blue account has company access
- Check if you need to be invited to a company
- Verify your account is active and verified

#### Operation Failures
**Problem**: Operations fail with GraphQL errors
**Solutions**:
- Check that Company ID is valid and you have access
- Verify Project ID exists and is accessible
- For custom queries, validate GraphQL syntax
- Review Blue API documentation for field requirements

#### Dropdown Loading Issues
**Problem**: Assignees, Tags, or Custom Fields don't load
**Solutions**:
- Ensure Company and Project are selected first
- Check that the project has users/tags/custom fields configured
- Verify network connectivity to Blue API
- Try refreshing the dropdown options

#### Performance Issues
**Problem**: Slow response times or timeouts
**Solutions**:
- Use pagination for large result sets (limit/skip parameters)
- Add appropriate delays between API calls
- Filter results to reduce data transfer
- Check Blue API status for outages

### Getting Help

- **Blue API Issues**: Refer to [Blue API Documentation](https://www.blue.cc/en/api/start-guide/introduction)
- **n8n Node Issues**: Check [n8n Community](https://community.n8n.io/)
- **Bug Reports**: Submit issues to the [GitHub repository](https://github.com/datadoesntlie/n8n-nodes-blue/issues)

### Debug Tips

1. **Enable Detailed Logging**: Turn on n8n's detailed execution logging
2. **Test Operations Individually**: Isolate failing operations
3. **Verify Data**: Check that IDs and parameters are valid
4. **GraphQL Debugging**: Use Blue's GraphQL playground for query testing
5. **Network Issues**: Check firewall/proxy settings if requests fail

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Blue API Documentation](https://www.blue.cc/en/api/start-guide/introduction) - Official API guide and reference
* [Blue GraphQL Schema](https://api.blue.cc/graphql) - Interactive GraphQL playground
* [GitHub Repository](https://github.com/datadoesntlie/n8n-nodes-blue) - Source code and issue tracking

## License

[MIT](LICENSE.md)
