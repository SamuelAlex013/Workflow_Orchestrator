# n8n-nodes-onetap

<img src="https://onetap-web-assets.sfo2.cdn.digitaloceanspaces.com/logos/onetap-logo-light.png" alt="OneTap Logo" width="100" height="100">

![OneTap Check-in Journey](https://onetap-web-assets.sfo2.cdn.digitaloceanspaces.com/app-assets/check-in-journey.jpg)

An n8n community node for integrating with [OneTap](https://onetapcheckin.com) - a powerful visitor management and check-in system.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Quick Start Guide](#quick-start-guide)  
[Available Nodes](#available-nodes)  
[Supported Resources & Operations](#supported-resources--operations)  
[Usage Examples](#usage-examples)  
[Advanced Features](#advanced-features)  
[Troubleshooting](#troubleshooting)  
[Authentication](#authentication)  
[Compatibility](#compatibility)  
[Developer](#developer)  
[Resources](#resources)  
[Version](#version)  
[Support](#support)  

## About OneTap

OneTap Check-in is a digital check-in platform designed to simplify guest registration and tracking. It enables fast, touchless check-ins for events, offices, or secure locations, enhancing the experience for both visitors and organizers.

> **Note**: This integration is maintained by One Tap, Inc.

## Features

- **Complete API Coverage**: All 36 operations across 5 resources
- **Profile Management**: Get, create, update, delete profiles with custom fields and avatar support
- **Advanced Search**: Search profiles by name, email, or phone number with sorting
- **Passport Operations**: Manage visitor passes with SMS/email sending capabilities
- **Punch Pass System**: Create, track, and redeem punch passes with check-in limits
- **Participant Management**: Handle event participants with check-in/check-out workflows
- **List Management**: Create and manage event lists with scheduling and survey data
- **Real-time Triggers**: Webhook and polling support for live event monitoring
- **Flexible Filtering**: Advanced filtering options with pagination support
- **Environment Support**: Production and staging environment configurations
- **Custom Fields**: Dynamic custom field support for profiles and participants
- **Check-in Codes**: Manage unique alphanumeric check-in codes

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Alternatively, you can install this community node in n8n:

1. Go to **Settings** → **Community Nodes**
2. Click **Install a community node**
3. Enter `n8n-nodes-onetap`
4. Click **Install**

You can also install it via npm in your n8n installation:

```bash
npm install n8n-nodes-onetap
```

## Configuration

### Credentials

To use this node, you need to configure your OneTap API credentials:

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for **OneTap API**
3. Enter your **API Key** (obtainable from your OneTap dashboard)
4. Test the connection

### API Documentation

For detailed API information, visit: [https://apidocs.onetapcheckin.io](https://apidocs.onetapcheckin.io)

More comprehensive documentation on the OneTap public API, including detailed endpoint references, request/response examples, and authentication guides, can be found at [https://apidocs.onetapcheckin.io/](https://apidocs.onetapcheckin.io/).

## Quick Start Guide

### Step 1: Install the Node
1. In n8n, go to **Settings** → **Community Nodes**
2. Click **Install a community node**
3. Enter `n8n-nodes-onetap`
4. Click **Install** and wait for completion

### Step 2: Set Up Credentials
1. Visit the [OneTap Dashboard](https://dashboard.onetapcheckin.com/)
2. Navigate to **Account Settings** → **API Integrations**
3. Copy your API key
4. In n8n, go to **Credentials** → **Add Credential**
5. Search for **OneTap API** and select it
6. Paste your API key and click **Test** to verify connection

### Step 3: Create Your First Workflow
1. Create a new workflow in n8n
2. Add a **Manual Trigger** node
3. Add an **OneTap** node
4. Configure the node:
   - **Resource**: Profile
   - **Operation**: Get All Profiles
   - **Credentials**: Select your OneTap API credential
5. Click **Test workflow** to fetch your profiles

### Step 4: Explore Advanced Features
- Try different resources (Participants, Lists, Passports)
- Set up webhooks using the **OneTap Trigger** node
- Use the **OneTap Webhook Manager** to register webhooks
- Combine with other n8n nodes for powerful automations

## Available Nodes

This package includes three specialized nodes:

### 1. OneTap Node
The main node for all OneTap operations across 5 resources:

### 2. OneTap Trigger Node
Listen for OneTap events in real-time:
- **Webhook Support**: Direct webhook integration
- **Polling Support**: Regular API polling for events
- **Event Types**: Check-ins, check-outs, new participants, profile changes
- **Environment Selection**: Production or staging environments

### 3. OneTap Webhook Manager Node
Register and manage webhooks:
- **Webhook Registration**: Register new webhooks with OneTap
- **Event Subscription**: Subscribe to specific events or all events
- **Webhook Management**: List, update, and unregister webhooks

## Supported Resources & Operations

### Profile Resource (9 operations)
- **Get All Profiles**: Retrieve all visitor profiles with filtering and search
- **Get Single Profile**: Get a specific profile by ID
- **Create Profile**: Create new visitor profiles
- **Update Profile**: Update existing profiles with custom fields
- **Delete Profile**: Delete a specific profile
- **Delete Multiple Profiles**: Bulk delete profiles
- **Update Avatar**: Update profile avatar image
- **Get Custom Fields**: Retrieve custom fields schema
- **Find by Check-in Code**: Locate profile using check-in code

### Passport Resource (6 operations)
- **Get All Passports**: Fetch passes for profiles or participants
- **Get by Participant**: Get passport for specific participant
- **Get by Profile**: Get passes for specific profile
- **Get Groups**: Fetch all group passes
- **Delete Passport**: Delete a group pass
- **Send Passport**: Send passport via SMS or email

### Punch Pass Resource (5 operations)
- **Create Punch Pass**: Create new punch passport with check-in limits
- **Get All Punch Passes**: Retrieve punch passes for a profile
- **Get Single Punch Pass**: Get punch pass with associated check-ins
- **Update Punch Pass**: Update punch passport details
- **Redeem Punch Pass**: Associate check-in with punch passport

### Participant Resource (9 operations)
- **Create Participants**: Add participants to events and lists
- **Get Single Participant**: Retrieve specific participant details
- **Update Participant**: Modify participant information
- **Get All Participants**: Fetch participants with advanced filtering
- **Delete Participant**: Remove participant from events
- **Check In**: Process participant check-in with location/method tracking
- **Check Out**: Process participant check-out
- **Undo Check In**: Reverse check-in operation
- **Undo Check Out**: Reverse check-out operation

### List Resource (7 operations)
- **Create List**: Create new event lists with scheduling
- **Get All Lists**: Retrieve lists with filtering and sorting
- **Get Single List**: Get specific list details
- **Update List**: Modify list configuration
- **Delete Single List**: Remove specific list
- **Delete Multiple Lists**: Bulk delete lists
- **Get Survey Data**: Retrieve survey data for lists

## Usage Examples

### Search for Profiles
```json
{
  "resource": "profile",
  "operation": "getAll",
  "additionalFields": {
    "search": "john@example.com",
    "sortBy": "name",
    "sortOrder": "asc",
    "favorite": true
  }
}
```

### Create Participant and Check In
```json
{
  "resource": "participants",
  "operation": "create",
  "listId": "list123",
  "profileId": "profile456",
  "additionalFields": {
    "source": "n8n-automation",
    "notes": "VIP guest"
  }
}
```

### Set Up Event Trigger
```json
{
  "triggerOn": "checkin",
  "triggerMethod": "webhook",
  "additionalFilters": {
    "method": ["TAP", "QR"],
    "source": "mobile-app"
  }
}
```

### Create Punch Pass
```json
{
  "resource": "punchPasses",
  "operation": "create",
  "profileId": "profile123",
  "startsAt": "2024-01-01T00:00:00Z",
  "createFields": {
    "name": "Coffee Loyalty Card",
    "checkInsLimit": 10,
    "expiresAt": "2024-12-31T23:59:59Z"
  }
}
```

### Register Webhook
```json
{
  "operation": "register",
  "webhookUrl": "https://your-n8n-instance.com/webhook/abc123",
  "events": ["participant.checkin", "participant.checkout"],
  "additionalSettings": {
    "name": "n8n-checkin-webhook",
    "description": "Process check-ins in n8n workflow"
  }
}
```

## Example Workflows

### Check-in Analytics with Airtable Integration

We've included a complete example workflow that demonstrates how to build a powerful check-in analytics system using OneTap and Airtable:

**📁 [Example Workflow](./examples/example_n8n_workflow.json)**

[Example workflow /w video 📺](https://community.onetapcheckin.com/t/n8n-integration-coming-out-soon/155)

This workflow:
1. **Fetches all profiles** from your OneTap account using your API key
2. **Loops through each profile** to get the number of check-ins performed
3. **Updates an Airtable sheet** with the check-in analytics data

**Key Features:**
- **Manual Trigger**: Currently triggered manually, but easily configurable for automation
- **Scheduled Execution**: Can be automated to run on a schedule (daily, weekly, etc.)
- **Webhook Integration**: For advanced setups, connect to webhooks for real-time updates when check-ins happen
- **Analytics Dashboard**: Creates a comprehensive view of check-in activity in Airtable

**Use Cases:**
- Track employee attendance and check-in frequency
- Monitor event participation rates
- Generate check-in reports for compliance
- Create automated attendance dashboards

To use this workflow:
1. Import the JSON file into your n8n instance
2. Configure your OneTap API credentials
3. Set up your Airtable connection
4. Customize the schedule or webhook triggers as needed


## Advanced Features

### Custom Fields Support
The node supports dynamic custom fields for profiles:
```json
{
  "customFields": {
    "customField": [
      {
        "name": "employeeId",
        "type": "string",
        "value": "EMP001"
      },
      {
        "name": "department",
        "type": "string", 
        "value": "Engineering"
      }
    ]
  }
}
```

### Environment Configuration
Select between production and staging environments:
- **Production**: `https://api-beta.onetapcheckin.com`
- **Staging**: For development and testing

### Pagination & Filtering
Most operations support advanced pagination and filtering:
- **Return All**: Automatically paginate through all results
- **Custom Pagination**: Control page size and offset
- **Advanced Filtering**: Filter by dates, locations, methods, and custom criteria
- **Sorting**: Sort by multiple fields with ascending/descending order

## Troubleshooting

### Authentication Issues

**Problem**: "Invalid API key" or "Unauthorized" errors
- **Solution**: Verify your API key in the [OneTap Dashboard](https://dashboard.onetapcheckin.com/) under Account Settings → API Integrations
- **Check**: Ensure you have a Pro Plus plan or higher for API access
- **Verify**: Test the credential in n8n using the "Test" button

**Problem**: "403 Forbidden" errors
- **Solution**: Check your OneTap plan - API access requires Pro Plus plans or higher
- **Upgrade**: Visit the [pricing page](https://www.onetapcheckin.com/pricing) to upgrade your plan

### Common API Errors

**Problem**: "Profile not found" or "Invalid ID" errors
- **Solution**: Verify the profile/participant/list ID exists in your OneTap account
- **Check**: IDs are case-sensitive and must match exactly
- **Test**: Try fetching all profiles first to get valid IDs

**Problem**: "Rate limit exceeded" errors
- **Solution**: Reduce the frequency of API calls
- **Implement**: Add delays between requests using n8n's "Wait" node
- **Contact**: Reach out to support for rate limit increases if needed

### Webhook Issues

**Problem**: Webhooks not triggering
- **Solution**: Check that your n8n instance is publicly accessible
- **Verify**: Ensure the webhook URL is correct and responding
- **Test**: Use the OneTap Webhook Manager to re-register webhooks
- **Debug**: Check n8n execution logs for incoming webhook data

**Problem**: Webhook registration fails
- **Solution**: Verify your webhook URL is publicly accessible
- **Check**: Ensure the URL returns a 200 status code
- **Format**: URL should be `https://your-n8n-instance.com/webhook/your-webhook-id`

### Node Configuration Issues

**Problem**: "Required parameter missing" errors
- **Solution**: Check that all required fields are filled
- **Profile operations**: Profile ID is required for single profile operations
- **Participant operations**: Participant ID and List ID may be required
- **Validation**: Use the node's built-in validation hints

**Problem**: Custom fields not updating
- **Solution**: Ensure custom field names match exactly (case-sensitive)
- **Check**: Verify custom field types (string, number, boolean, date, array)
- **Test**: Use "Get Custom Fields" operation to see available fields

### Performance Issues

**Problem**: Slow response times
- **Solution**: Use pagination instead of "Return All" for large datasets
- **Optimize**: Implement proper filtering to reduce data transfer
- **Batch**: Process operations in smaller batches

**Problem**: Memory issues with large datasets
- **Solution**: Enable pagination and process data in chunks
- **Limit**: Set reasonable page sizes (50-100 items per page)
- **Stream**: Process data as it arrives rather than loading all at once

### Need More Help?

If you're still experiencing issues:
1. Check the [OneTap Community](https://community.onetapcheckin.com/) for similar issues
2. Review the [API documentation](https://apidocs.onetapcheckin.io/) for detailed endpoint information
3. Contact the developer at developer@onetapcheckin.com
4. Report bugs on the [GitHub repository](https://github.com/one-tap-inc/one-tap-n8n)

## Authentication

This node uses API Key authentication. The API key is sent via the `X-API-Key` header to the OneTap API.

### Getting Your API Key

1. Visit the [OneTap Dashboard](https://dashboard.onetapcheckin.com/)
2. Navigate to **Account Settings** → **API Integrations**
3. Copy your API key from this section

### Plan Requirements

**Important**: Public API integrations are available starting from the **Pro Plus plans** and above. Please check the [pricing page](https://www.onetapcheckin.com/pricing) and your current plan details to ensure you have API access.

If you're on a lower plan (Individual, Basic, Standard, or Pro), you'll need to upgrade to access the API functionality.

## Compatibility

| Requirement | Version/Details |
|-------------|----------------|
| **Minimum n8n version** | 0.190.0 |
| **Tested with n8n versions** | 0.190.0, 1.0.0+ |
| **Node.js version** | 20.15 or higher |
| **n8n API version** | 1 |
| **Compatibility** | Self-hosted and cloud versions |

## Developer

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/one-tap-inc/one-tap-n8n.git
   cd one-tap-n8n
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Build the node:**
   ```bash
   npm run build
   ```

4. **Run n8n locally:**
   ```bash
   # Install n8n globally if not already installed
   npm install -g n8n
   
   # Start n8n
   n8n start
   ```

### Side-loading the Node into n8n

If you want to manually install the node without using the community nodes installation:

#### Method 1: Custom Nodes Directory
1. **Locate your n8n custom nodes directory:**
   - **Linux/Mac**: `~/.n8n/custom/`
   - **Windows**: `%USERPROFILE%\.n8n\custom\`

2. **Copy the built node files:**
   ```bash
   # After building the project
   cp -r dist/* ~/.n8n/custom/
   ```

3. **Restart n8n:**
   ```bash
   n8n start
   ```

#### Method 2: Using N8N_CUSTOM_EXTENSIONS Environment Variable
1. **Set the custom extensions path:**
   ```bash
   export N8N_CUSTOM_EXTENSIONS="./dist"
   ```

2. **Start n8n:**
   ```bash
   n8n start
   ```

#### Method 3: Development Mode (Symlink)
1. **Create a symlink in the custom directory:**
   ```bash
   # Create custom directory if it doesn't exist
   mkdir -p ~/.n8n/custom
   
   # Create symlink to your development directory
   ln -s /path/to/one-tap-n8n/dist ~/.n8n/custom/n8n-nodes-onetap
   ```

2. **Restart n8n:**
   ```bash
   n8n start
   ```

### Development Commands

| Command | Description |
|---------|-------------|
| `npm run build` | Build the node for production |
| `npm run dev` | Watch for changes and rebuild automatically |
| `npm run lint` | Run ESLint to check code quality |
| `npm run lintfix` | Automatically fix linting issues |
| `npm run format` | Format code with Prettier |

### Testing Your Changes

1. **Make your changes** to the node files
2. **Rebuild the node**: `npm run build`
3. **Restart n8n** to load the updated node
4. **Test the changes** in n8n workflows

### Resources for n8n Node Development

- [n8n Node Development Documentation](https://docs.n8n.io/integrations/creating-nodes/)
- [n8n Community Nodes Guidelines](https://docs.n8n.io/integrations/community-nodes/)
- [n8n TypeScript Node Template](https://github.com/n8n-io/n8n-nodes-starter)

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [OneTap API Documentation](https://apidocs.onetapcheckin.io/)
* [OneTap Platform](https://onetapcheckin.com/)
* [OneTap Community](https://community.onetapcheckin.com/)
* [OneTap Pricing](https://www.onetapcheckin.com/pricing)
* [OneTap n8n Integration Discussion](https://community.onetapcheckin.com/t/n8n-integration-coming-out-soon/155)

## API Endpoints

- **Production**: `https://api-beta.onetapcheckin.com`
- **Staging**: Available for development/testing

## Version

Current version: **0.2.2**

## License

MIT

## Repository

[https://github.com/one-tap-inc/one-tap-n8n](https://github.com/one-tap-inc/one-tap-n8n)

## Support

For support and questions:
- **OneTap Support**: hello@onetapcheckin.com
- **Developer Contact**: developer@onetapcheckin.com
- **OneTap Community**: Join the [OneTap Community](https://community.onetapcheckin.com/) to share your use cases, discuss this integration, and get help from other users
- **Node Issues**: Please report issues on the [GitHub repository](https://github.com/one-tap-inc/one-tap-n8n)
- **n8n Community**: Join the [n8n community](https://community.n8n.io/) for general n8n support

## Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues on the GitHub repository.
