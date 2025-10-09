# n8n-nodes-clientify

[![npm version](https://badge.fury.io/js/n8n-nodes-clientify.svg)](https://www.npmjs.com/package/n8n-nodes-clientify)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official n8n node for integrating with Clientify CRM via Model Context Protocol (MCP). This node provides seamless access to all Clientify CRM operations including contacts, companies, deals, tasks, and more.

## Table of Contents

- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Available Operations](#available-operations)
- [Trigger Events](#trigger-events)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Support](#support)
- [License](#license)

## Installation

### In n8n (GUI)

1. Go to **Settings** → **Community Nodes**
2. Click **Install**
3. Enter: `n8n-nodes-clientify`
4. Click **I understand the risks** and then **Install**
5. **Restart n8n** (important - the node won't appear until you restart)

### Via npm (Command Line)

```bash
cd ~/.n8n/nodes
npm install n8n-nodes-clientify
# Restart n8n
```

### Docker

If running n8n in Docker, ensure you persist the nodes directory:

```yaml
volumes:
  - n8n_data:/home/node/.n8n
```

Or enable auto-reinstall on restart:

```yaml
environment:
  - N8N_REINSTALL_MISSING_PACKAGES=true
```

## Prerequisites

- **n8n version:** 0.180.0 or higher
- **Node.js version:** 20.15 or higher
- **Clientify Account:** Active Clientify CRM account with API access
- **Authentication Token:** JWT token from Clientify MCP server

## Configuration

### Step 1: Obtain Your Clientify MCP Token

1. Log into your Clientify account
2. Navigate to API settings or contact your Clientify administrator
3. Generate or copy your MCP authentication token (JWT format)

### Step 2: Add Credentials in n8n

1. In n8n, go to **Credentials** → **New**
2. Search for **"Clientify MCP API"**
3. Enter your **Authentication Token** (JWT)
4. Click **Save**

### Step 3: Use the Node

1. In your workflow, click **+** to add a node
2. Search for **"Clientify"**
3. Select the **Clientify** node
4. Choose your saved credentials
5. Select an operation from the dropdown
6. Configure the parameters for your operation

## Available Operations

This node dynamically supports **26 operations** from the Clientify MCP API:

### 📊 Companies
- **List Companies** - Retrieve all companies with pagination
- **Get Company** - Get detailed information for a specific company by ID
- **Create Company** - Create a new company in the CRM
- **Update Company** - Update an existing company
- **Delete Company** - Remove a company from the CRM
- **Search Companies** - Search for companies by criteria

### 👥 Contacts
- **List Contacts** - Retrieve all contacts or search for specific contacts
- **Get Contact** - Get detailed information for a specific contact by ID
- **Create Contact** - Create a new contact in the CRM
- **Update Contact** - Update an existing contact
- **Delete Contact** - Remove a contact from the CRM

### 💼 Deals
- **List Deals** - Retrieve all deals with filtering and pagination
- **List Deals By Stage** - Filter deals by pipeline stage
- **Get Deal** - Get detailed information for a specific deal by ID
- **Create Deal** - Create a new deal/opportunity
- **Update Deal** - Update an existing deal
- **Delete Deal** - Remove a deal from the CRM
- **Mark Deal Won** - Mark a deal as won/closed successfully
- **Mark Deal Lost** - Mark a deal as lost/closed unsuccessfully

### ✅ Tasks
- **List Tasks** - Retrieve all tasks with pagination
- **Get Task** - Get detailed information for a specific task by ID
- **Create Task** - Create a new task/activity
- **List Activity Types** - Get available activity types for tasks

### ⚙️ Configuration & Utilities
- **List Pipelines** - Retrieve all available sales pipelines
- **Get Current User** - Get information about the authenticated user
- **Get Current Time** - Get current date/time with timezone awareness

## Trigger Events

**NEW in v0.2.0!** The Clientify Trigger node enables automatic workflow execution when events occur in Clientify CRM. With 16 event types covering contacts, companies, deals, and tasks, you can automate workflows instantly when things happen in your CRM.

### How It Works

1. Add "Clientify Trigger" node to your n8n workflow
2. Select which event should start the workflow (e.g., "Contact Created")
3. Activate the workflow to get your unique webhook URL
4. Configure the webhook in Clientify to point to your n8n URL
5. When the event happens in Clientify, your workflow runs automatically with the data

### 16 Available Triggers

| Event | Trigger Name | When It Fires | Common Use Cases |
|-------|--------------|---------------|------------------|
| 👥 **Contacts** | | | |
| | Contact Created | New contact added | Welcome email, create follow-up task, add to CRM |
| | Contact Updated | Contact details changed | Sync to other systems, log changes, update records |
| | Contact Deleted | Contact removed | Archive data, remove from email lists, cleanup |
| 📊 **Companies** | | | |
| | Company Created | New company added | Research company, assign account manager, notify team |
| | Company Updated | Company details changed | Update external systems, track changes |
| | Company Deleted | Company removed | Clean up related data, archive records |
| 💼 **Deals** | | | |
| | Deal Created | New deal/opportunity created | Notify sales team, create tasks, log in analytics |
| | Deal Updated | Deal details changed | Track value changes, update forecasts, log activity |
| | Deal Won | Deal closed successfully | Send celebration, create invoice, start onboarding |
| | Deal Lost | Deal closed unsuccessfully | Add to nurture campaign, analyze loss reason |
| | Deal Stage Changed | Deal moved to different stage | Stage-specific actions (send pricing, generate contract) |
| | Deal Deleted | Deal removed | Log deletion, archive data |
| ✅ **Tasks** | | | |
| | Task Created | New task added | Add to calendar, notify assignee, sync to project tools |
| | Task Completed | Task marked complete | Log activity, update metrics, trigger next steps |
| | Task Due Soon | Task approaching due date | Send reminder to assignee |
| | Task Overdue | Task past due date | Escalate to manager, send urgent notification |

### Setup Instructions

**In n8n:**
1. Add "Clientify Trigger" node to your workflow
2. Select the event from the dropdown
3. Choose your Clientify MCP credentials
4. Save and **activate** the workflow (toggle ON)
5. Click the trigger node → Expand "Webhook URLs"
6. Switch to "Production URL" tab
7. Copy the webhook URL

**In Clientify:**
1. Go to Settings → Webhooks
2. Click "Add Webhook"
3. Select the matching event (e.g., "contact.created")
4. Paste your n8n webhook URL
5. Set status to "Active"
6. Save

**Test It:**
Create a contact, deal, or task in Clientify → Check n8n executions → Your workflow should have run!

### Data You'll Receive

All webhook data is automatically flattened so you can easily access it in your workflow. Here's what you get for each event type:

**Contact Events** (`contact.created`, `contact.updated`, `contact.deleted`)
```json
{
  "event": "contact.created",
  "timestamp": "2025-10-02T15:30:00Z",
  "contact_id": 12345,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "company_id": 456,
  "company_name": "Acme Corp",
  "changes": { /* only for .updated events */ }
}
```
Access with: `{{$json.first_name}}`, `{{$json.email}}`, `{{$json.company_name}}`

**Company Events** (`company.created`, `company.updated`, `company.deleted`)
```json
{
  "event": "company.created",
  "timestamp": "2025-10-02T18:00:00Z",
  "company_id": 999,
  "name": "Tech Startup Inc",
  "domain": "techstartup.com",
  "industry": "Technology",
  "size": "50-100",
  "country": "USA"
}
```
Access with: `{{$json.name}}`, `{{$json.domain}}`, `{{$json.industry}}`

**Deal Events** (`deal.created`, `deal.updated`, `deal.won`, `deal.lost`, `deal.stage_changed`, `deal.deleted`)
```json
{
  "event": "deal.won",
  "timestamp": "2025-10-02T23:00:00Z",
  "deal_id": 98765,
  "title": "Enterprise License Sale",
  "value": 60000,
  "currency": "USD",
  "contact_id": 12345,
  "contact_name": "John Doe",
  "company_id": 999,
  "company_name": "Tech Startup Inc",
  "stage_name": "Won",
  "won_at": "2025-10-02T23:00:00Z"
}
```
Access with: `{{$json.title}}`, `{{$json.value}}`, `{{$json.contact_name}}`

**Task Events** (`task.created`, `task.completed`, `task.due_soon`, `task.overdue`)
```json
{
  "event": "task.created",
  "timestamp": "2025-10-03T03:00:00Z",
  "task_id": 5555,
  "title": "Follow up with John Doe",
  "description": "Discuss pricing options",
  "type": "call",
  "contact_id": 12345,
  "contact_name": "John Doe",
  "deal_id": 98765,
  "assigned_to_name": "Sales Rep",
  "due_date": "2025-10-05"
}
```
Access with: `{{$json.title}}`, `{{$json.contact_name}}`, `{{$json.due_date}}`

### Important Notes

- **Event names are case-sensitive**: Use exact names like `contact.created` (not `Contact.Created`)
- **Webhook URLs are unique** per workflow - if you recreate a workflow, you'll get a new URL
- **Workflows must be active** for webhooks to work - inactive workflows won't receive events
- **All data includes `_raw`** field with the original payload for advanced use cases
- **Update events include `changes`** object showing what changed (old/new values)

## Usage Examples

### Example 1: List All Contacts

Retrieve a paginated list of all contacts in your CRM.

**Configuration:**
- **Operation:** `List Contacts`
- **Parameters:** Leave empty for all contacts, or add filters

**Output:** Array of contact objects with names, emails, phone numbers, and IDs.

```json
[
  {
    "id": 123,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "company_id": 456
  }
]
```

---

### Example 2: Create a New Company

Add a new company to your Clientify CRM.

**Configuration:**
- **Operation:** `Create Company`
- **Parameters:**
  - **name** (required): `Acme Corporation`
  - **domain**: `acme.com`
  - **industry**: `Technology`
  - **description**: `Leading software provider`

**Output:** Created company object with assigned ID.

```json
{
  "id": 789,
  "name": "Acme Corporation",
  "domain": "acme.com",
  "industry": "Technology",
  "created_at": "2025-10-01T12:00:00Z"
}
```

---

### Example 3: Update a Deal and Mark as Won

Update deal details and mark it as successfully closed.

**Workflow:**
1. **First Node:** Get the deal you want to update
   - **Operation:** `Get Deal`
   - **deal_id:** `{{$json.deal_id}}`

2. **Second Node:** Update the deal
   - **Operation:** `Update Deal`
   - **deal_id:** `{{$json.id}}`
   - **value:** `50000`
   - **notes:** `Final negotiations completed`

3. **Third Node:** Mark as won
   - **Operation:** `Mark Deal Won`
   - **deal_id:** `{{$json.id}}`

---

### Example 4: Search Companies and Create Contacts

Find a company by name and create a new contact associated with it.

**Workflow:**
1. **Search Companies:**
   - **Operation:** `Search Companies`
   - **query:** `Acme`

2. **Create Contact:**
   - **Operation:** `Create Contact`
   - **first_name:** `Jane`
   - **last_name:** `Smith`
   - **email:** `jane.smith@acme.com`
   - **company_id:** `{{$json.id}}` (from previous node)

---

### Example 5: List All Deals in a Specific Pipeline Stage

Retrieve deals that are in the "Negotiation" stage.

**Configuration:**
- **Operation:** `List Deals By Stage`
- **Parameters:**
  - **stage:** `Negotiation`

**Use Case:** Create automated alerts when deals reach certain stages, or generate reports on pipeline health.

---

### Example 6: Auto-Send Welcome Email (Using Trigger)

**NEW in v0.2.0!** Automatically send a welcome email when a new contact is created.

**Workflow:**
1. **Clientify Trigger**
   - Event: `Contact Created`

2. **Send Email**
   - To: `{{$json.email}}`
   - Subject: `Welcome {{$json.first_name}}!`
   - Body: Welcome message

3. **Create Task**
   - Title: `Follow up with {{$json.first_name}} {{$json.last_name}}`
   - Contact ID: `{{$json.contact_id}}`
   - Due: 3 days from now

**Result:** When someone creates a contact "Jane Smith" in Clientify:
- Jane automatically receives welcome email
- Follow-up task is created for sales team
- All happens instantly without manual intervention

---

### Example 7: Deal Won Notification (Using Trigger)

**NEW in v0.2.0!** Notify your team when a deal is won.

**Workflow:**
1. **Clientify Trigger**
   - Event: `Deal Won`

2. **Slack** (or Email)
   - Message: `🎉 Deal Won! {{$json.title}} - ${{$json.value}} - {{$json.contact_name}}`
   - Channel: `#sales-wins`

3. **Clientify** (Action Node)
   - Operation: `Create Task`
   - Title: `Onboard {{$json.contact_name}}`
   - Deal ID: `{{$json.deal_id}}`

**Result:** When a deal is marked as won:
- Team gets instant Slack notification
- Onboarding task is automatically created
- No manual steps required

---

## Troubleshooting

### Node Doesn't Appear After Installation

**Problem:** The Clientify node doesn't show up in the node panel after installing.

**Solution:**
1. **Restart n8n completely** (required for new nodes)
2. Clear your browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
3. Search for "Clientify" (not the package name) in the node search
4. Verify installation in **Settings → Community Nodes**

### Authentication Errors

**Problem:** "Authentication failed" or 401/403 errors.

**Solution:**
1. Verify your JWT token is valid and not expired
2. Check that the token has the correct permissions in Clientify
3. Ensure you're using the Clientify MCP token (not a regular API key)
4. Try creating a new credential with a fresh token

### "Missing required parameter" Errors

**Problem:** Operation fails with missing parameter errors.

**Solution:**
1. Check which fields are marked as **required** (indicated by red asterisk)
2. Some operations require specific IDs (contact_id, company_id, etc.)
3. Use `Get` operations first to retrieve IDs, then pass them to `Update` or `Delete` operations
4. Review the parameter descriptions for expected format

### Operations Return Empty Results

**Problem:** List operations return no results even though data exists.

**Solution:**
1. Check pagination parameters (page, page_size)
2. Verify your token has permission to access the requested resources
3. Try without filters first to confirm data access
4. Check the Clientify web UI to confirm data exists

### Node Execution Fails in Docker

**Problem:** Node fails with "package not found" errors in Docker environments.

**Solution:**
1. Ensure nodes directory is persisted in volumes:
   ```yaml
   volumes:
     - n8n_data:/home/node/.n8n
   ```
2. Or enable auto-reinstall:
   ```yaml
   environment:
     - N8N_REINSTALL_MISSING_PACKAGES=true
   ```
3. Restart the container after installing the node

### Rate Limiting Errors

**Problem:** "Too many requests" or 429 errors.

**Solution:**
1. Add delay between operations using n8n's **Wait** node
2. Reduce the frequency of scheduled workflows
3. Batch operations where possible
4. Contact Clientify support to increase rate limits if needed

## Parameter Reference

### Common Parameters

Most operations support these common parameters:

- **page** (number): Page number for pagination (default: 1)
- **page_size** (number): Number of results per page (default: 20, max: 100)
- **sort_by** (string): Field to sort by (e.g., "created_at", "name")
- **sort_order** (string): Sort direction ("asc" or "desc")

### ID Parameters

Operations that work with specific records require an ID parameter:

- **company_id** (number): Unique identifier for a company
- **contact_id** (number): Unique identifier for a contact
- **deal_id** (number): Unique identifier for a deal
- **task_id** (number): Unique identifier for a task

## Advanced Usage

### Combining Multiple Operations

Create powerful workflows by chaining operations:

```
Trigger → Search Companies → Create Contact → Create Deal → Create Task
```

### Error Handling

Use n8n's built-in error handling:

1. Enable **"Continue On Fail"** in node settings
2. Add an **IF** node to check for errors
3. Route errors to notification nodes (Email, Slack, etc.)

### Data Transformation

Use n8n's **Code** or **Function** nodes to transform data between operations:

```
List Contacts → Code Node (transform) → External API
```

## Development & Contribution

This is an official Clientify node. Contributions are welcome!

**Repository:** https://github.com/contacteitor/clientify_n8n

**Report Issues:** https://github.com/contacteitor/clientify_n8n/issues

**Documentation:** See the repository for full documentation

## Support

- **Issues & Bugs:** https://github.com/contacteitor/clientify_n8n/issues
- **Email:** develop@clientify.com
- **Clientify Documentation:** https://mcp.clientify.com/docs

## Version History

- **v0.2.0** (2025-10-02): Trigger support added
  - **NEW:** Clientify Trigger node for webhook events
  - 16 trigger events (contact, company, deal, task)
  - Automatic workflow execution on Clientify events
  - Flattened webhook payload for easy data access

- **v0.1.0** (2025-10-01): Initial release
  - 26 MCP operations supported
  - Dynamic field generation from MCP API
  - Full CRUD operations for contacts, companies, deals, tasks
  - Pipeline and user management

## License

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Clientify

---

**Made with ❤️ by Clientify**

*This is an official Clientify node. n8n is a trademark of its respective owner.*
