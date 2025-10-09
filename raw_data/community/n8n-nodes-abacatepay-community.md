# n8n-nodes-abacatepay-community

[![npm version](https://badge.fury.io/js/n8n-nodes-abacatepay-community.svg)](https://badge.fury.io/js/n8n-nodes-abacatepay-community)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

n8n community node for integrating with AbacatePay API - a Brazilian payment gateway for PIX, billing, and customer management.

## Features

### 🥑 AbacatePay Node
Complete integration with AbacatePay's REST API:

- **Customer Management**: Create and list customers with automatic CPF/CNPJ validation
- **Billing System**: Create and manage bills with multiple products and coupon support
- **PIX Payments**: Generate instant PIX QR codes with customizable expiration
- **Coupon System**: Create percentage or fixed-value discount coupons
- **Withdraw Management**: Create and track PIX withdrawals

### 🔔 AbacatePay Trigger
Real-time webhook monitoring with intelligent event processing:

- **16 Event Types**: Monitor PIX payments, billing changes, customer creation, coupon usage, and withdrawals
- **Smart Detection**: Automatically detects resource type from webhook data
- **Enriched Data**: Provides formatted amounts, parsed names, document validation, and status flags
- **Flexible Authentication**: Supports none, basic auth, and header-based authentication

## Installation

Install from npm:

```bash
npm install n8n-nodes-abacatepay-community
```

## Setup

1. **Get AbacatePay API Key**: Sign up at [AbacatePay](https://abacatepay.com) and get your API key
2. **Add Credentials**: In n8n, create new "AbacatePay API" credentials with your API key
3. **Configure Webhooks**: Set up webhook URLs in your AbacatePay dashboard to receive real-time events

## Usage Examples

### Create a Customer
```typescript
// Node: AbacatePay - Customer - Create
{
  "name": "João Silva Santos",
  "cellphone": "(11) 99999-8888",
  "email": "joao@example.com",
  "taxId": "123.456.789-01"
}
```

### Generate PIX Payment
```typescript
// Node: AbacatePay - PIX QR Code - Create
{
  "amount": 5000, // R$ 50.00 in cents
  "description": "Premium Plan Payment",
  "expiresIn": 1800, // 30 minutes
  "customer": {
    "name": "João Silva Santos",
    "email": "joao@example.com"
  }
}
```

### Monitor Payments
```typescript
// Trigger: AbacatePay Trigger
// Events: ["pix.payment.completed", "billing.paid"]
// Automatically receives enriched data:
{
  "event": "pix.payment.completed",
  "resourceType": "pix",
  "amounts": {
    "raw": 5000,
    "reais": "50.00",
    "net": 4920,
    "netReais": "49.20"
  },
  "customer": {
    "name": {
      "first": "João",
      "full": "João Silva Santos"
    },
    "document": {
      "type": "CPF",
      "cleaned": "12345678901"
    }
  }
}
```

## Supported Operations

### Customer Resource
- **Create**: Register new customers with validation
- **List**: Retrieve all registered customers

### Billing Resource  
- **Create**: Generate payment links with multiple products
- **List**: View all created bills and their status

### PIX QR Code Resource
- **Create**: Generate instant PIX QR codes
- **Simulate Payment**: Test payments in development mode
- **Check Status**: Verify payment status

### Coupon Resource
- **Create**: Create discount coupons (percentage or fixed value)
- **List**: Manage all created coupons

### Withdraw Resource
- **Create**: Process PIX withdrawals to bank accounts
- **List**: Track withdrawal history and status

## Webhook Events

The AbacatePay Trigger monitors these event types:

| Event | Description |
|-------|-------------|
| `customer.created` | New customer registered |
| `customer.updated` | Customer data updated |
| `pix.payment.completed` | PIX payment successful |
| `pix.payment.expired` | PIX QR code expired |
| `pix.payment.cancelled` | PIX payment cancelled |
| `pix.qrcode.created` | PIX QR code generated |
| `billing.created` | New bill created |
| `billing.paid` | Bill payment confirmed |
| `billing.expired` | Bill expired |
| `billing.cancelled` | Bill cancelled |
| `coupon.created` | New coupon created |
| `coupon.redeemed` | Coupon used |
| `coupon.expired` | Coupon expired |
| `withdraw.created` | Withdrawal initiated |
| `withdraw.completed` | Withdrawal processed |
| `withdraw.failed` | Withdrawal failed |

## Data Enrichment

The trigger automatically enriches webhook data with:

- **Formatted Amounts**: Converts cents to Brazilian Real (R$)
- **Net Calculations**: Deducts platform fees automatically
- **Name Parsing**: Extracts first/last names from full names
- **Document Validation**: Identifies CPF vs CNPJ documents
- **Email Analysis**: Extracts domains and identifies personal emails
- **Status Flags**: Boolean flags for quick conditional logic

## Authentication

Configure your AbacatePay credentials in n8n:

1. **API Key**: Your AbacatePay Bearer token
2. **Base URL**: Default is `https://api.abacatepay.com` (change for different environments)

## Automation Examples

### Welcome Email Flow
1. **Trigger**: Customer created
2. **Action**: Send personalized welcome email
3. **Action**: Create welcome discount coupon
4. **Action**: Update CRM with new customer

### Payment Confirmation
1. **Trigger**: PIX payment completed
2. **Condition**: Check payment amount
3. **Action**: Send receipt email
4. **Action**: Activate purchased service
5. **Action**: Update analytics

## Requirements

- n8n version 0.198.0 or higher
- Node.js 20.15 or higher
- AbacatePay account with API access


## License

MIT License - see LICENSE file for details.

## Support

- 📧 **Email**: ajuda@abacatepay.com
- 📖 **Documentation**: [AbacatePay API Docs](https://docs.abacatepay.com)

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests to our repository.

---

Made with ❤️ for the n8n community and Brazilian payment automation.
