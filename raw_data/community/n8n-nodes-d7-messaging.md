![D7 Messaging Logo](dist/src/nodes/D7Messaging/d7.svg)

# D7Networks Messaging Integration for n8n

## Installation

### 1. Install D7Networks Node
1. Open your n8n workspace
2. Click on Settings (⚙️) in the bottom left corner
3. Select Community Nodes from the sidebar
4. Search for `n8n-nodes-d7-messaging`
5. Click Install
6. Restart n8n when prompted

### 2. Verify Installation
1. Refresh your n8n workspace
2. Open the nodes panel (right sidebar)
3. Search for "D7"
4. You should see "D7 SMS" and "D7 WhatsApp" nodes
5. Try dragging either node into your workflow

### 3. Configure Authentication
1. Get your API key from [D7 Networks](https://app.d7networks.com/api-tokens)
2. In your n8n workflow:
   * Add D7 SMS or D7 WhatsApp node
   * Click "Create New Credential"
   * Enter your API key
   * Save credential

## Creating Messaging Workflows

### Basic Workflow Structure
```
[Contact Source] → [Function Node] → [D7 SMS/WhatsApp Node]
```

### Step 1: Import Contacts
Choose any contact source node:
- Google Sheets
- Airtable
- Database nodes
- Google Contacts
- CSV
- Any CRM integration

### Step 2: Process Contact Data
Add a Function node to format your contacts:

```javascript
// Format contacts for D7 nodes
return items.map(item => ({
  json: {
    recipient: item.json.phone,  // or any field containing phone number
    name: item.json.name,        // or any field containing name
  }
}));
```

### Step 3: Configure D7 Node

#### For SMS:
1. Connect Function node to D7 SMS node
2. Configure fields:
   * Recipients: `{{ $json.recipient }}`
   * Message: `Hello {{ $json.name }}, your message here`

#### For WhatsApp:
1. Connect Function node to D7 WhatsApp node
2. Configure fields:
   * Recipients: `{{ $json.recipient }}`
   * Choose message type (Template/Text/Media)
   * Add message content or template parameters

## Testing Your Workflow

1. Start with test contacts (2-3 numbers)
2. Activate workflow
3. Check message delivery
4. Monitor for any errors
5. Scale up after successful testing

## Common Issues & Solutions

### Invalid Phone Numbers
- Ensure numbers are in E.164 format
- Add validation in Function node:
```javascript
// Phone number validation
function validatePhone(phone) {
  const cleaned = phone.replace(/\D/g, '');
  return cleaned.startsWith('+') ? cleaned : '+' + cleaned;
}
```

### Message Delivery Issues
- Verify API credentials
- Check recipient number format
- Ensure sufficient credit balance

Need help? Contact 
## Support

- **Email**: [support@d7networks.com](mailto:support@d7networks.com)
- **Website**: [Visit Our Website](https://d7networks.com)
