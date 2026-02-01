# n8n-nodes-awork

This is an n8n community node that lets you automate workflows with [awork](https://www.awork.com/), a modern project management tool. It provides seamless integration between awork and n8n, allowing you to manage projects, tasks, and company/client data within your automation workflows.

## Installation

### n8n Cloud
1. Select **+** on your canvas and type **awork**
2. Find **awork** in the **More from the community** section
3. Select **install**

Follow the [official installation guide](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/) for n8n community nodes.

### Self-Hosted Instance
1. Navigate to **Settings > Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-awork` in **Enter npm package name**
4. Select **Install**
5. **Restart your n8n instance** after installation

## Authentication

To use the awork node, you'll need API credentials from awork:

1. **Create an awork account** at [awork.com](https://www.awork.com/) if you don't have one
2. **Generate an API key** by following the instructions in the [awork API Authentication documentation](https://developers.awork.com/authentication#api-key)
3. **In n8n**, add new credentials:
   - Select **"awork API"** from the credentials list
   - Enter your API key
   - Test the connection to ensure it's working

## Available Operations

The awork node provide comprehensive access to awork's project management features, including:

### Projects
- **Create Project**: Start new projects with custom settings
- **Get Project**: Retrieve project information
- **List Projects**: Get all projects with filtering options
- **Change Project Status**: Changes the status of a project

### Tasks
- **Create Task**: Add new tasks to projects
- **Get Task**: Retrieve specific task information
- **List Tasks**: Get tasks with advanced filtering
- **Change Task Status**: Changes the status of a task
- **Set Task Custom Fields**: Sets the value of a task custom field
- **Add Task Comment**: Adds a comment to a task

### Companies
- **Create Company**: Add new companies to your workspace
- **Get Company**: Retrieve company details
- **List Companies**: Get all companies with filtering

### Users
- **List Users**: Get all users with filtering

### Other
- **HTTP**: With a generic HTTP Request, any awork API endpoint can be used

For detailed information about each operation and its parameters, visit the relevant sections in the [awork Developer Documentation](https://developers.awork.com/):
- [Projects](https://developers.awork.com/projects)
- [Tasks](https://developers.awork.com/tasks)
- [Companies](https://developers.awork.com/companies)
- [Users](https://developers.awork.com/users)

## Example Workflows

Here are some common use cases for the awork nodes:

1. **Automated Project Creation**: Create projects in awork when new deals are won in your CRM
2. **Task Synchronization**: Sync tasks between awork and other project management tools
3. **Company Management**: Automatically create companies in awork from form submissions
4. **Status Updates**: Update task statuses based on external triggers
5. **Reporting**: Extract project and task data for custom reporting dashboards

## Resources

- **awork Developer Documentation**: [developers.awork.com](https://developers.awork.com/)
- **awork Developer Forum**: [community.awork.com/c/developer-forum/17](https://community.awork.com/c/developer-forum/17)
- **n8n Documentation**: [docs.n8n.io](https://docs.n8n.io/)
- **n8n Community**: [community.n8n.io](https://community.n8n.io/)

## Support

If you encounter any issues or have questions:

- Check the [awork Developer Forum](https://community.awork.com/c/developer-forum/17) for API-related questions
- Visit the [n8n Community Forum](https://community.n8n.io/) for n8n-specific issues

## Local Development

For contributors and developers who want to test changes locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/awork-io/n8n-nodes-awork
   cd n8n-nodes-awork
   ```

2. Install dependencies and build:
   ```bash
   pnpm install
   pnpm run build
   ```

3. Link to your local n8n installation:
   ```bash
   pnpm link --global
   cd ~/.n8n/custom
   pnpm link n8n-nodes-awork
   ```

4. Start n8n:
   ```bash
   n8n start
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
