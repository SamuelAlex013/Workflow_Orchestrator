# n8n-nodes-orgo

This is an n8n community node that provides comprehensive integration with Orgo, a multi-tenant SaaS platform for organizations specializing in membership management, event coordination, and community engagement.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Option 1: Community Nodes (Recommended)
1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install** and enter `n8n-nodes-orgo`
3. Click **Install**

### Option 2: Manual Installation
```bash
npm install n8n-nodes-orgo
```

After installation, restart your n8n instance to see the new nodes.

## Operations

This package provides two powerful nodes for comprehensive Orgo integration:

### Orgo Node
The main node for interacting with the Orgo API, supporting full CRUD operations across all resources.

**Available Resources:**

#### **User Management**
- **Get User**: Retrieve user details by ID
- **Get Many Users**: List multiple users with pagination
- **Create User**: Register new users with email, first name, and last name

#### **Contact Management**
- **Get Contact**: Retrieve contact details by ID
- **Get Many Contacts**: List multiple contacts with pagination
- **Create Contact**: Add new external contacts with name and email
- **Update Contact**: Modify contact information
- **Delete Contact**: Remove contacts from the system

#### **Event Management**  
- **Get Event**: Retrieve event details by UUID
- **Get Many Events**: List multiple events with pagination

#### **Event Registration**
- **Get Registration**: Retrieve event registration by ID
- **Get Event Registrations**: List all registrations for a specific event (paginated, 100 per page)
- **Register for Event**: Create new event registration (requires event UUID and user ID)
- **Update Registration Status**: Modify attendance status (Registered, Attended, Not Attending, Invited)
- **Cancel Registration**: Remove event registration

#### **Contract User Management**
- **Get Contract User**: Retrieve contract user details by ID
- **Get Many Contract Users**: List multiple contract users with pagination

#### **Payment Management**
- **Get Payment**: Retrieve payment record by ID  
- **Get Many Payments**: List payment records with pagination

#### **Webhook Management**
- **Get Webhook**: Retrieve webhook subscription by ID
- **Get Many Webhooks**: List webhook subscriptions
- **Create Webhook**: Set up new webhook subscriptions
- **Update Webhook**: Modify webhook configuration
- **Delete Webhook**: Remove webhook subscriptions
- **Test Webhook**: Send test webhook event

#### **Custom Endpoints**
- **Custom Request**: Make requests to any Orgo API endpoint

### Orgo Trigger Node
A trigger node that responds to Orgo webhooks for real-time automation and event-driven workflows.

**Supported Event Types:**
- **Contact Events**: `contact.created`, `contact.updated`, `contact.deleted`
- **Event Registration**: `event_attend.created`, `event_attend.updated`
- **User Role Events**: `user_role.created`, `user_role.deleted`
- **User Events**: `user.created`, `user.updated`

## Credentials

To use the Orgo nodes, you need to configure API credentials in n8n:

### Required Fields
1. **API Base URL**: Your Orgo instance API base URL
   - Format: `https://your-domain.com/api/v1`
   - Example: `https://app.orgo.space/api/v1`
   - For local development: `http://localhost:8000/api/v1`

2. **API Token**: Your personal API token from Orgo
   - Generated from your Orgo account settings
   - Used for authentication with the Orgo API

### Optional Fields
3. **Webhook Secret**: Secret key for webhook signature verification (recommended for security)
4. **Tenant ID**: Your organization/tenant ID (auto-detected if not provided)

### Getting Your API Token

1. Log into your Orgo account
2. Navigate to **Organization Settings > API & OAuth -> API
3. Generate a new API token or copy an existing one
4. Copy the token and paste it into your n8n Orgo API credentials

### Testing Your Credentials

The credential configuration includes a built-in test that verifies:
- API connectivity to your Orgo instance
- Token validity and permissions
- Proper API base URL configuration

## API Documentation

For detailed API reference, visit: [docs.orgo.space/api-reference](https://docs.orgo.space/api-reference)

The Orgo API provides comprehensive endpoints for:
- User and identity management
- Event and attendance tracking
- Payment and subscription handling
- Contract and document management
- Profile and badge systems
- Voting and discussion features

## Webhook Setup

The Orgo Trigger node provides automated webhook management:

### Automatic Management
- **Auto-Registration**: Webhooks are automatically created when workflows are activated
- **Auto-Cleanup**: Webhooks are automatically removed when workflows are deactivated
- **Event Filtering**: Subscribe only to the events you need
- **Signature Verification**: Optional webhook signature validation for security

### Webhook Payload Structure

Orgo webhooks deliver standardized payloads:

```json
{
  "id": "wh_evt_123456789abcd",
  "event": "user.created",
  "api_version": "2024-01",
  "created": 1705320600,
  "data": {
    "object": {
      "id": 123,
      "email": "user@example.com",
      "firstName": "John",
      "lastName": "Doe"
    },
    "previous_attributes": {
      "email": {
        "old": "old@example.com",
        "new": "user@example.com"
      }
    }
  },
  "tenant_id": 1,
  "request": {
    "id": "req_987654321efgh",
    "idempotency_key": null
  }
}
```

### Accessing Webhook Data in n8n

In your workflow, access webhook data using:
- `{{$json.object}}` - Main entity data
- `{{$json.event}}` - Event type (e.g., "user.created")
- `{{$json.previous_attributes}}` - Changed fields for update events
- `{{$json.tenant_id}}` - Organization ID
- `{{$json.created}}` - Event timestamp

## Example Workflows

### User Registration Automation
Automatically welcome new users and sync them to external systems:

```json
{
  "name": "New User Onboarding",
  "nodes": [
    {
      "name": "Orgo User Created",
      "type": "n8n-nodes-orgo.orgoTrigger",
      "parameters": {
        "events": ["user.created"],
        "verifySignature": true
      }
    },
    {
      "name": "Send Welcome Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "toEmail": "={{$json.object.email}}",
        "subject": "Welcome to {{$json.object.organization}}!",
        "text": "Hello {{$json.object.firstName}}, welcome to our community!"
      }
    },
    {
      "name": "Create CRM Contact",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "POST",
        "url": "https://your-crm.com/api/contacts",
        "body": {
          "email": "={{$json.object.email}}",
          "first_name": "={{$json.object.firstName}}",
          "last_name": "={{$json.object.lastName}}",
          "source": "orgo_registration"
        }
      }
    }
  ]
}
```

### Event Registration Management
Handle event registrations and send confirmations:

```json
{
  "name": "Event Registration Handler",
  "nodes": [
    {
      "name": "Event Registration",
      "type": "n8n-nodes-orgo.orgoTrigger",
      "parameters": {
        "events": ["event_attend.created"]
      }
    },
    {
      "name": "Get Event Details",
      "type": "n8n-nodes-orgo.orgo",
      "parameters": {
        "resource": "event",
        "operation": "get",
        "id": "={{$json.object.eventId}}"
      }
    },
    {
      "name": "Send Confirmation Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "toEmail": "={{$json.object.user.email}}",
        "subject": "Event Registration Confirmed: {{$node['Get Event Details'].json.title}}",
        "html": "Your registration for {{$node['Get Event Details'].json.title}} on {{$node['Get Event Details'].json.date}} has been confirmed!"
      }
    }
  ]
}
```

### Payment Processing Workflow
Automate payment confirmations and notifications:

```json
{
  "name": "Payment Processing",
  "nodes": [
    {
      "name": "Payment Events",
      "type": "n8n-nodes-orgo.orgoTrigger",
      "parameters": {
        "events": ["product_payment.created", "product_payment.updated"]
      }
    },
    {
      "name": "Check Payment Status",
      "type": "n8n-nodes-base.switch",
      "parameters": {
        "dataPropertyName": "object.status",
        "rules": {
          "values": [
            {"value": "completed"},
            {"value": "failed"},
            {"value": "pending"}
          ]
        }
      }
    },
    {
      "name": "Send Receipt (Success)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "toEmail": "={{$json.object.user.email}}",
        "subject": "Payment Receipt - {{$json.object.amount}} {{$json.object.currency}}",
        "text": "Thank you for your payment of {{$json.object.amount}} {{$json.object.currency}}."
      }
    }
  ]
}
```

## Multi-Tenant Architecture

Orgo's multi-tenant design ensures data isolation and security:

- **Automatic Tenant Scoping**: All API requests are automatically scoped to your organization
- **Tenant ID Inclusion**: Webhook events include `tenant_id` for proper filtering
- **Permission Respect**: User permissions and access levels are automatically enforced
- **Cross-Tenant Security**: No access to data from other organizations

## Error Handling & Reliability

The nodes include comprehensive error handling:

### API Error Handling
- **Detailed Error Messages**: Clear error descriptions from the Orgo API
- **HTTP Status Codes**: Proper handling of 4xx and 5xx responses
- **Validation Errors**: Field-level validation error reporting

### Webhook Reliability
- **Signature Verification**: Prevents unauthorized webhook requests
- **Payload Validation**: Ensures webhook data integrity
- **Retry Logic**: Automatic retry for failed webhook deliveries

### Network Resilience
- **Connection Timeouts**: Configurable request timeouts
- **Rate Limiting**: Automatic handling of API rate limits
- **Graceful Degradation**: Continues operation during temporary outages

## Performance & Best Practices

### Pagination
- Use the `limit` parameter to control response sizes
- Default limit is 25 items per request
- Implement pagination for large datasets

### Webhook Events
- Subscribe only to necessary events to reduce noise
- Use event filtering to improve workflow performance
- Enable signature verification for security

### API Usage
- Cache frequently accessed data when possible
- Use batch operations for multiple related requests
- Monitor API usage to stay within rate limits

## Compatibility

**Tested Compatibility:**
- n8n version 1.0.0 and above
- Node.js 18.x and above
- Orgo API version 2024-01

**Browser Support:**
- Works in all modern browsers that support n8n
- Compatible with n8n Cloud and self-hosted instances

## Troubleshooting

### Common Issues

**Authentication Errors**
- Verify your API token is correct and hasn't expired
- Ensure the API Base URL doesn't include `/api/v1`
- Check that your account has the necessary permissions

**Webhook Not Receiving Events**
- Verify the webhook URL is accessible from the internet
- Check that the selected events are being triggered in Orgo
- Ensure webhook signature verification is properly configured

**API Request Failures**
- Confirm the Orgo instance is running and accessible
- Check network connectivity and firewall settings
- Verify the API endpoint exists and accepts the request method

### Debug Mode
Enable n8n debug logging to troubleshoot issues:
```bash
N8N_LOG_LEVEL=debug n8n start
```
## Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/Orgo-space/n8n-nodes-orgo/issues)
- **n8n Community**: [Get help from the n8n community](https://community.n8n.io/)
- **Orgo Documentation**: [docs.orgo.space/api-reference](https://docs.orgo.space/api-reference)

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Orgo Platform](https://app.orgo.space)
- [Orgo API Documentation](https://docs.orgo.space/api-reference)
- [n8n Workflow Examples](https://n8n.io/workflows/)

## License

[MIT](LICENSE.md)

---

**Keywords**: n8n, community-node, orgo, webhook, automation, workflow, membership-management, event-management, api-integration