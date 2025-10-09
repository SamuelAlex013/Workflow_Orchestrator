# n8n-nodes-ikoula

**Developed by Ascenzia**

> ⚠️ **BETA STATUS**: All nodes in this package are currently in beta. While functional, they may have limitations and are subject to changes. Use with caution in production environments.

A comprehensive collection of n8n nodes for integrating with the Ikoula API ecosystem. This package provides seamless access to all Ikoula services including cloud computing, dedicated servers, web hosting, domain management, SSL certificates, and business solutions.

## Installation

To install this community node package in your n8n instance:

```bash
npm install n8n-nodes-ikoula
```

## Authentication

All nodes in this package require Ikoula API credentials. You'll need to configure the `ikoulaApi` credential with:

- **Email**: Your Ikoula account email
- **Password**: Your Ikoula account password
- **API URL**: The Ikoula API endpoint (default: https://api.ikoula.com)

The nodes use embedded RSA encryption for secure password transmission. Your password is automatically encrypted when making API calls to Ikoula services.

## Available Nodes

### Core Infrastructure Nodes

#### Ikoula API CS (Cloud Server) - **BETA**
**Developed by Ascenzia**

Manage Ikoula CloudStack API for billing and consumption operations:
- **List Bills**: Lists bills associated to the account
- **Get Billing Grid**: Retrieves billing grid
- **Get Current Consumption**: Retrieves current consumption
- **Get Billing Consumption**: Gets the consumption for a specific billing

#### Ikoula API IKIC (Infrastructure) - **BETA**
**Developed by Ascenzia**

Access Ikoula's infrastructure management capabilities for advanced cloud operations.

#### Ikoula VPS API - **BETA**
**Developed by Ascenzia**

Comprehensive VPS (Virtual Private Server) management including creation, configuration, and monitoring.

#### Ikoula API Dedicated Server - **BETA**
**Developed by Ascenzia**

Full control over dedicated server resources with provisioning and management operations.

#### Ikoula API Platform - **BETA**
**Developed by Ascenzia**

Platform-as-a-Service operations for application deployment and management.

### Backup & Security Nodes

#### Ikoula API Veeam - **BETA**
**Developed by Ascenzia**

Integrate with Veeam backup solutions for enterprise data protection and recovery.

#### Ikoula API Acronis - **BETA**
**Developed by Ascenzia**

Access Acronis backup and cyber protection services through the Ikoula platform.

#### Ikoula API ESET - **BETA**
**Developed by Ascenzia**

Manage ESET antivirus and security solutions with operations:
- **List Accounts**: Get all ESET service accounts
- **Get Account Details**: Retrieve detailed information for a specific ESET account

### Microsoft Solutions

#### Ikoula API Microsoft - **BETA**
**Developed by Ascenzia**

Comprehensive Microsoft services integration with four main resources:

**Microsoft Resource:**
- List Accounts
- Get Account Details

**Licence Resource:**
- List Account Licences
- List Orderable Licences
- Order Licence
- Terminate Licence

**User Resource:**
- List Users
- Get User Details
- Create User
- Update User
- Delete User
- Assign Licence to User
- Unassign Licence from User
- Reset User Password
- Get User Licences

**Invoice Resource:**
- List Invoices
- Get Invoice Details

### Virtualization & Enterprise

#### Ikoula VMware API - **BETA**
**Developed by Ascenzia**

VMware virtualization platform management with operations:
- **List Accounts**: Get all VMware service accounts
- **Get Account Details**: Retrieve detailed VMware account information

#### Ikoula Business API - **BETA**
**Developed by Ascenzia**

Comprehensive business process management with operations:
- **List Accounts**: Get all business service accounts
- **Get Account Details**: Retrieve detailed business account information
- **List Orderable Services**: Browse available business services
- **Order Service**: Place new service orders
- **List Payment Methods**: Get available payment options
- **Get Invoice Details**: Retrieve specific invoice information
- **List Invoices**: Get all invoices
- **List Terminable Services**: Get services eligible for termination
- **Terminate Service**: Cancel existing services

#### Ikoula Zimbra API - **BETA**
**Developed by Ascenzia**

Zimbra email and collaboration platform management:
- **List Accounts**: Get all Zimbra service accounts
- **Get Account Details**: Retrieve detailed Zimbra account information

#### Ikoula HEB API - **BETA**
**Developed by Ascenzia**

HEB (Hébergement) web hosting services management:
- **List Accounts**: Get all HEB service accounts
- **Get Account Details**: Retrieve detailed HEB account information

#### Ikoula Plesk Managed API - **BETA**
**Developed by Ascenzia**

Plesk managed hosting platform operations:
- **List Accounts**: Get all Plesk managed service accounts
- **Get Account Details**: Retrieve detailed Plesk account information

### Domain & Certificate Management

#### Ikoula NDD API - **BETA**
**Developed by Ascenzia**

Domain name and DNS management services:
- **List Accounts**: Get all domain service accounts
- **Get Account Details**: Retrieve detailed domain account information
- **Add DNS Registration**: Add DNS registration for Certbot SSL automation
- **Delete DNS Registration**: Remove DNS registration for Certbot

#### Ikoula SSL API - **BETA**
**Developed by Ascenzia**

SSL certificate services management:
- **List Subscriptions**: Get all SSL certificate subscriptions
- **Get Subscription Details**: Retrieve detailed SSL subscription information

## Beta Status & Limitations

⚠️ **Important Beta Information:**

- **All nodes are in beta status** and may have limitations or bugs
- **API coverage may be incomplete** - not all Ikoula API endpoints are implemented
- **Breaking changes possible** in future versions during beta period
- **Limited testing** - nodes have been tested with basic use cases but may fail with edge cases
- **Documentation gaps** - some features may not be fully documented
- **Production use caution** - while nodes are functional, use with care in production environments

**Beta Testing Feedback:**
If you encounter issues or have suggestions, please report them through the appropriate channels. Your feedback helps improve the package for stable release.

## Features

- **Secure Authentication**: RSA-encrypted password transmission
- **Flexible Response Formats**: Support for both JSON and XML responses
- **Error Handling**: Comprehensive error handling with continue-on-fail options
- **Type Safety**: Full TypeScript implementation with proper type definitions
- **Consistent API**: Unified interface across all Ikoula services

## Usage Examples

### Basic Account Listing

```json
{
  "nodes": [
    {
      "name": "List VPS Accounts",
      "type": "n8n-nodes-ikoula.ikoulaVpsApi",
      "parameters": {
        "resource": "vps",
        "operation": "listAccounts",
        "format": "json"
      },
      "credentials": {
        "ikoulaApi": "your-ikoula-credentials"
      }
    }
  ]
}
```

### SSL Certificate Management

```json
{
  "nodes": [
    {
      "name": "Get SSL Details",
      "type": "n8n-nodes-ikoula.ikoulaSslApi",
      "parameters": {
        "resource": "ssl",
        "operation": "getSubscriptionDetails",
        "subscrId": 12345,
        "format": "json"
      },
      "credentials": {
        "ikoulaApi": "your-ikoula-credentials"
      }
    }
  ]
}
```

### Domain DNS Management

```json
{
  "nodes": [
    {
      "name": "Add Certbot DNS",
      "type": "n8n-nodes-ikoula.ikoulaNddApi",
      "parameters": {
        "resource": "ndd",
        "operation": "addDnsRegistration",
        "certbotDomain": "example.com",
        "certbotValidation": "validation-string",
        "format": "json"
      },
      "credentials": {
        "ikoulaApi": "your-ikoula-credentials"
      }
    }
  ]
}
```

## Requirements

- n8n version 1.112.0 or higher
- Node.js 20.15 or higher
- Valid Ikoula API credentials
- Ikoula RSA public key file (`Ikoula.API.RSAKeyPub.pem`)

## Support

For support and documentation regarding the Ikoula API, please refer to the official Ikoula API documentation or contact Ikoula support.

## Development

This package is **developed by Ascenzia** and provides comprehensive integration with the Ikoula ecosystem for n8n automation workflows.

### Building from Source

```bash
npm install
npm run build
```

### Linting

```bash
npm run lint
npm run lintfix
```

## License

MIT

---

**Developed by Ascenzia** - Professional n8n node development for enterprise automation solutions.
