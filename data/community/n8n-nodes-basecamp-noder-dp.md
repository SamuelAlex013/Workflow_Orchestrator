# n8n Basecamp Nodes

A comprehensive n8n community node package that provides integration with Basecamp 4 API, including full support for managing todos, todo lists, projects, people, and more.

## Features

This package includes nodes for:

### ✅ Todo Management (NEW!)
- **Todo Sets**: Get todo sets for projects
- **Todo Lists**: Create, read, update todo lists
- **Todos**: Full CRUD operations for individual tasks
  - Create todos with assignees, due dates, descriptions
  - Update todo details and assignments
  - Complete/uncomplete todos
  - Reposition todos within lists

### 📊 Project Management
- Get all projects or specific projects
- Create new projects
- Manage project access and people

### 👥 People Management
- Get all people or specific person details
- Get people on projects
- Update project access permissions
- Get pingable people

### 📋 Card Tables (Kanban)
- Manage card table columns
- Create, update, and move cards
- Column color management
- Watch/unwatch columns

### 🤖 Chatbots & Integrations
- Create and manage chatbots
- Send messages via chatbots
- Webhook management

### 📁 File Management
- Upload and manage attachments
- Document management
- Vault operations

### 📅 Schedule Management
- Create and manage schedule entries
- Update schedule settings
- Get schedule information

### 🔔 Notifications & Subscriptions
- Subscribe/unsubscribe from recordings
- Manage notification preferences

## Installation with Docker

### Prerequisites
- Docker and Docker Compose installed
- Basic understanding of n8n workflows

### Directory Structure

Create the following directory structure on your host machine:

```
n8n-basecamp/
├── docker-compose.yml
├── .env
├── data/                    # n8n data persistence
├── nodes/                   # Custom nodes location
│   └── @itustudentcouncil/
│       └── n8n-nodes-basecamp/
│           ├── dist/
│           ├── package.json
│           └── ...
└── README.md
```

### Step 1: Download the Node Package

1. Download or clone this repository
2. Copy the entire package to your `nodes/@itustudentcouncil/n8n-nodes-basecamp/` directory

```bash
# Create the directory structure
mkdir -p n8n-basecamp/nodes/@itustudentcouncil/

# Copy the package (adjust source path as needed)
cp -r /path/to/n8n-nodes-basecamp-main n8n-basecamp/nodes/@itustudentcouncil/n8n-nodes-basecamp
```

### Step 2: Create Environment File

Create a `.env` file in your `n8n-basecamp` directory:

```env
# n8n Configuration
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your_secure_password_here

# Basecamp API Configuration (optional - can be set per workflow)
BASECAMP_CLIENT_ID=your_basecamp_client_id
BASECAMP_CLIENT_SECRET=your_basecamp_client_secret
BASECAMP_ACCOUNT_ID=your_basecamp_account_id

# Timezone
GENERIC_TIMEZONE=America/New_York

# Security
N8N_SECURE_COOKIE=false

# Execution
N8N_DEFAULT_BINARY_DATA_MODE=filesystem
```

### Step 3: Create Docker Compose File

Use the provided `docker-compose.yml` below.

### Step 4: Start n8n

```bash
cd n8n-basecamp
docker-compose up -d
```

### Step 5: Access n8n

- Open your browser and go to `http://localhost:5678`
- Login with the credentials from your `.env` file
- The Basecamp nodes should now be available in the node palette

## Docker Compose Configuration

```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n-basecamp
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=${N8N_BASIC_AUTH_ACTIVE}
      - N8N_BASIC_AUTH_USER=${N8N_BASIC_AUTH_USER}
      - N8N_BASIC_AUTH_PASSWORD=${N8N_BASIC_AUTH_PASSWORD}
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - N8N_SECURE_COOKIE=${N8N_SECURE_COOKIE}
      - N8N_DEFAULT_BINARY_DATA_MODE=${N8N_DEFAULT_BINARY_DATA_MODE}
      # Custom nodes path
      - N8N_CUSTOM_EXTENSIONS=/home/node/.n8n/custom
    volumes:
      # Persist n8n data
      - ./data:/home/node/.n8n
      # Mount custom nodes
      - ./nodes:/home/node/.n8n/custom/node_modules:ro
    depends_on:
      - postgres

  postgres:
    image: postgres:13
    container_name: n8n-postgres
    restart: unless-stopped
    environment:
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=n8n_password
      - POSTGRES_DB=n8n
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres-data:
  n8n-data:
```

## Basecamp API Setup

### 1. Create Basecamp App

1. Go to [Basecamp Launchpad](https://launchpad.37signals.com/integrations)
2. Click "Register a new application"
3. Fill in your application details:
   - **Name**: Your application name
   - **Company**: Your company name
   - **Website**: Your website URL
   - **Redirect URI**: `http://localhost:5678/rest/oauth2-credential/callback` (adjust domain as needed)

### 2. Configure Credentials in n8n

1. In n8n, go to **Settings** → **Credentials**
2. Click **+ Add Credential**
3. Search for "Basecamp API" and select it
4. Fill in the required fields:
   - **Client ID**: From your Basecamp app
   - **Client Secret**: From your Basecamp app
   - **Basecamp ID**: Your Basecamp account ID (found in your Basecamp URL)
5. Click **Connect my account** and authorize the connection

## Usage Examples

### Create a Todo

```json
{
  "operation": "createTodo",
  "bucketId": "{{ $json.project_id }}",
  "todolistId": "{{ $json.todolist_id }}",
  "content": "Complete project documentation",
  "description": "Write comprehensive docs for the new feature",
  "due_on": "2025-08-01",
  "assignee_ids": [12345, 67890],
  "notify": true
}
```

### Get All Todos in a List

```json
{
  "operation": "getTodos",
  "bucketId": "{{ $json.project_id }}",
  "todolistId": "{{ $json.todolist_id }}",
  "status": "active",
  "completed": false
}
```

### Complete a Todo

```json
{
  "operation": "completeTodo",
  "bucketId": "{{ $json.project_id }}",
  "todoId": "{{ $json.todo_id }}"
}
```

## Troubleshooting

### Node Not Appearing

1. Check that the package is in the correct directory: `/home/node/.n8n/custom/node_modules/@itustudentcouncil/n8n-nodes-basecamp`
2. Restart the n8n container: `docker-compose restart n8n`
3. Check container logs: `docker-compose logs n8n`

### Authentication Issues

1. Verify your Basecamp app credentials
2. Ensure the redirect URI matches exactly
3. Check that your Basecamp account ID is correct

### Permission Errors

1. Ensure proper file permissions on mounted volumes
2. Check that the user running Docker has access to the directories

## File Locations in Container

- **n8n data**: `/home/node/.n8n`
- **Custom nodes**: `/home/node/.n8n/custom/node_modules`
- **Workflows**: `/home/node/.n8n/workflows`
- **Credentials**: `/home/node/.n8n/credentials`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `N8N_BASIC_AUTH_ACTIVE` | Enable basic authentication | `true` |
| `N8N_BASIC_AUTH_USER` | Basic auth username | `admin` |
| `N8N_BASIC_AUTH_PASSWORD` | Basic auth password | Required |
| `N8N_CUSTOM_EXTENSIONS` | Path to custom nodes | `/home/node/.n8n/custom` |
| `GENERIC_TIMEZONE` | Default timezone | `UTC` |

## Support

For issues and questions:

1. Check the [Basecamp API documentation](https://github.com/basecamp/bc3-api)
2. Review the [n8n community docs](https://docs.n8n.io/)
3. Open an issue in this repository

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
