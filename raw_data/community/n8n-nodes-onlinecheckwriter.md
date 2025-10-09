# n8n-nodes-onlinecheckwriter

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/n8n-nodes-onlinecheckwriter/main/assets/banner.png" alt="OnlineCheckWriter for n8n" width="600">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/n8n-nodes-onlinecheckwriter"><img src="https://img.shields.io/npm/v/n8n-nodes-onlinecheckwriter.svg" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/n8n-nodes-onlinecheckwriter"><img src="https://img.shields.io/npm/dm/n8n-nodes-onlinecheckwriter.svg" alt="npm downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

This is an n8n community node that provides a complete integration with [OnlineCheckWriter](https://www.onlinecheckwriter.com/) for check printing, mailing, ACH payments, wire transfers, virtual cards, and more.

## 🚀 Features

### ✅ Check Operations (7 operations)
- **Create Check** - Generate checks programmatically
- **Get Check** - Retrieve check details
- **List Checks** - View all checks with filtering
- **Void Check** - Cancel issued checks
- **Print Check** - Generate PDFs (supports bulk printing)
- **Email Check** - Send checks electronically
- **Mail Check** - Physical USPS mailing with tracking

### 💳 Payment Operations (3 operations)
- **Virtual Card** - Create single-use or multi-use virtual cards
- **Wire Transfer** - Send domestic and international wires
- **Credit Card** - Process credit card payments

### 👥 Payee Management
- **Create Payee** - Add individuals or businesses with full details

### 📄 Document Operations
- **Mail Document** - Send PDFs via USPS
- **Save Payment Form** - Capture custom form payments

## 📦 Installation

### Community Node (Recommended)
In n8n, go to **Settings** > **Community Nodes** and search for:
```
n8n-nodes-onlinecheckwriter
```

### Manual Installation
```bash
npm install -g n8n-nodes-onlinecheckwriter
```

### Local Development
```bash
git clone https://github.com/yourusername/n8n-nodes-onlinecheckwriter.git
cd n8n-nodes-onlinecheckwriter
npm install
npm run build
npm link
cd ~/.n8n/nodes
npm link n8n-nodes-onlinecheckwriter
n8n start
```

## 🔑 Authentication

1. Sign up for [OnlineCheckWriter](https://www.onlinecheckwriter.com/)
2. Get your API key from the dashboard
3. In n8n, add OnlineCheckWriter credentials:
   - **API Key**: Your OnlineCheckWriter API key
   - **Environment**: Choose Sandbox for testing or Production
   - **Auto-validate Bank**: Enable to check bank verification
   - **Auto-check Balance**: Enable to verify sufficient funds

## 📖 Usage Examples

### Example 1: Create and Mail a Check
```json
{
  "resource": "check",
  "operation": "create",
  "bankAccountId": "bnk_xxxxx",
  "payee": "John Smith",
  "amount": 250.00,
  "additionalFields": {
    "memo": "Invoice Payment",
    "addressLine1": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001"
  }
}
```

### Example 2: Create Virtual Card
```json
{
  "resource": "payment",
  "operation": "virtualCard",
  "cardType": "single",
  "amount": 500.00,
  "cardholderName": "Marketing Team",
  "additionalOptions": {
    "merchantCategory": "online",
    "notes": "For Facebook Ads"
  }
}
```

### Example 3: Send Wire Transfer
```json
{
  "resource": "payment",
  "operation": "wireTransfer",
  "amount": 5000.00,
  "recipientName": "ABC Corporation",
  "recipientAccountNumber": "123456789",
  "recipientRoutingNumber": "021000021",
  "recipientBankName": "Chase Bank"
}
```

## 🔄 Workflow Templates

### Accounts Payable Automation
1. **Trigger**: New approved invoice in accounting system
2. **Create Check** with invoice details
3. **Email or Mail** check based on vendor preference
4. **Update** invoice status

### Expense Reimbursement
1. **Trigger**: Approved expense report
2. **Create** ACH payment or check
3. **Send** notification to employee
4. **Log** in accounting system

### Virtual Card for Subscriptions
1. **Trigger**: Monthly/recurring
2. **Create** virtual card with spending limit
3. **Use** for SaaS subscriptions
4. **Track** and reconcile

## ⚙️ Configuration

### Bank Account Verification
Before creating checks, ensure your bank account is verified in OnlineCheckWriter dashboard.

### Balance Requirements
The node can automatically check your OCW account balance before transactions. Enable this in credentials.

### Sandbox Testing
Use the sandbox environment for testing:
- No real money is moved
- Test all operations safely
- Same API structure as production

## 🐛 Troubleshooting

### Common Issues

**"Bank account not verified"**
- Verify your bank account in the OCW dashboard
- Wait for micro-deposit verification (1-2 business days)

**"Insufficient balance"**
- Add funds to your OCW account
- Check if auto-balance checking is enabled

**"Invalid routing number"**
- Ensure 9-digit ABA routing number
- Verify with your bank

### Debug Mode
Enable debug logging in n8n:
```bash
export N8N_LOG_LEVEL=debug
n8n start
```

## 📊 API Limits

- **Rate Limit**: 100 requests per minute
- **Bulk Operations**: Up to 100 checks per print request
- **File Size**: PDFs up to 10MB for mailing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## 🔗 Resources

- [OnlineCheckWriter API Documentation](https://docs.onlinecheckwriter.com/)
- [n8n Documentation](https://docs.n8n.io/)
- [Support Forum](https://community.n8n.io/)
- [Report Issues](https://github.com/yourusername/n8n-nodes-onlinecheckwriter/issues)

## 💖 Credits

Created and maintained by [Your Name/Company]

Special thanks to:
- OnlineCheckWriter team for API support
- n8n community for feedback and testing

---

*Note: This is a community node and is not officially affiliated with OnlineCheckWriter or n8n.*
