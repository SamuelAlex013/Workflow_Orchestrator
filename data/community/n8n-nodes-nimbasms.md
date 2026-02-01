# n8n-nodes-nimbasms

![npm version](https://img.shields.io/npm/v/n8n-nodes-nimbasms)
![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-nimbasms)
![License](https://img.shields.io/badge/license-MIT-green)
![n8n Community Node](https://img.shields.io/badge/n8n-community--node-ff6d5a)

A comprehensive n8n community node that integrates with the Nimba SMS API, enabling you to send SMS messages, manage contacts, create campaigns, and handle billing operations directly from your n8n workflows.

<p align="center"><img src="examples/automation_example.png" alt="Nimba SMS in n8n"></p>

## 🚀 Features

- ✅ **SMS Operations**: Send individual SMS and retrieve message history
- ✅ **Contact Management**: Create, update, delete, and organize contacts
- ✅ **Group Management**: Organize contacts into groups for targeted campaigns
- ✅ **Account Operations**: Check balance, view SMS packs, and monitor usage
- ✅ **Purchase Management**: View purchase history and invoices
- ✅ **Sender Name Management**: Manage custom sender names

## 📦 Installation

### Option 1: Install via n8n Community Nodes (Recommended)

1. Open your n8n instance
2. Go to **Settings > Community Nodes**
3. Click **Install**
4. Enter `n8n-nodes-nimbasms`
5. Click **Install**

### Option 2: Manual Installation

```bash
# For self-hosted n8n instances
npm install n8n-nodes-nimbasms

# For global n8n installation
npm install -g n8n-nodes-nimbasms
```

### Option 3: Docker Installation

Add to your n8n Docker configuration:

```dockerfile
FROM n8nio/n8n:latest
USER root
RUN npm install -g n8n-nodes-nimbasms
USER node
```

## 🔑 Credentials Setup

Before using this node, configure your Nimba SMS API credentials:

1. In n8n, go to **Credentials** and create **Nimba SMS API** credentials
2. Fill in the required information:
   - **Service ID (SID)**: Your Nimba SMS Service ID
   - **Secret Token**: Your Nimba SMS Secret Token
   - **Base URL**: Default is `https://api.nimbasms.com`

> 💡 Get your credentials from your [Nimba SMS Dashboard](https://wwww.nimbasms.com/app)

## 📱 Supported Operations

### SMS Operations
- **Send**: Send individual SMS messages
- **Get Many**: Retrieve SMS history with filtering options
- **Get**: Get details of a specific SMS message

### Contact Operations
- **Create**: Add new contacts with optional group assignment
- **Update**: Modify contact information and group memberships

### Group Operations
- **Get**: Retrieve group details

### Account Operations
- **Get Balance**: Check your SMS credit balance

### Purchase Operations
- **Get All**: Retrieve purchase history with filtering options
- **Get**: Get details of a specific purchase by UID

### Sender Name Operations
- **Get**: Check sender name status
- **Get Many**: List all your sender names

## 🎯 Quick Start Examples

### Send a Simple SMS

```json
{
  "resource": "sms",
  "operation": "send",
  "senderName": "YourBrand",
  "contact": "+224123456789",
  "message": "Hello from n8n! Your order has been confirmed."
}
```

### Get Purchase History

```json
{
  "resource": "purchase",
  "operation": "getAll",
  "returnAll": false,
  "limit": 10,
  "additionalFields": {
    "payment_type": "Orange",
    "start_date": "2024-01-01T00:00:00Z",
    "end_date": "2024-12-31T23:59:59Z"
  }
}
```

### Get Specific Purchase Details

```json
{
  "resource": "purchase",
  "operation": "get",
  "purchaseUid": "07cc67f4-45d6-494b-adac-09b5cbc7e2b5"
}
```

### Create a Contact with Group Assignment

```json
{
  "resource": "contact",
  "operation": "create",
  "numero": "+224123456789",
  "additionalFields": {
    "name": "John Doe",
    "groupes_id": "1,2,3"
  }
}
```

### Launch an SMS Campaign

```json
{
  "resource": "campaign",
  "operation": "create",
  "name": "Welcome Campaign",
  "senderName": "YourBrand",
  "message": "Welcome to our service! Enjoy 20% off your first order.",
  "groupsIds": "1,2"
}
```

### Check Account Balance

```json
{
  "resource": "account",
  "operation": "getBalance"
}
```

## 🌍 Regional Support

Optimized for African markets with:
- Guinea country code (+224) auto-formatting
- Support for local phone number formats

## 🛠️ Compatibility

- **n8n Version**: 0.190.0 or later
- **Node.js Version**: 16.x or later
- **API Version**: Nimba SMS API v1

## 📈 Use Cases

### E-commerce
- Order confirmations and shipping notifications
- Abandoned cart recovery campaigns
- Customer support and feedback collection

### Marketing
- Promotional campaigns and special offers
- Event notifications and reminders
- Customer segmentation and targeting

### Business Operations
- Employee notifications and alerts
- Appointment reminders
- System status updates and monitoring

### Customer Service
- Support ticket updates
- Account verification codes
- Service outage notifications

## 🤝 Support & Resources

- **Documentation**: [Nimba SMS API Docs](https://developers.nimbasms.com)
- **Community**: [n8n Community Forum](https://community.n8n.io)
- **Issues**: [GitHub Issues](https://github.com/nimbasms/n8n-nodes-nimbasms/issues)
- **Support**: Contact contact@nimbasms.com for API-related questions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [npm Package](https://www.npmjs.com/package/n8n-nodes-nimbasms)
- [Nimba SMS Website](https://www.nimbasms.com)
- [n8n Website](https://n8n.io)