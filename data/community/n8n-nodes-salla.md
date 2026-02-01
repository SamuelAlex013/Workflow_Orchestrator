# n8n-nodes-salla

This is an n8n community node that lets you use Salla.sa e-commerce platform in your n8n workflows.

[Salla](https://salla.sa/) is a leading e-commerce platform in Saudi Arabia and the Middle East that allows merchants to create online stores and manage their business operations.



[n8n](https://n8n.partnerlinks.io/4wjly6af9vki) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[eCommerce Automation & Personalization](#eCommerce Automation & Personalization)  
[Installation](#installation) 
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## eCommerce Automation & Personalization
**[🚀 Join Our Community](https://www.linkedin.com/groups/10153121/)**
Building eCommerce automation tools? Connect with fellow developers, share insights, and discover cutting-edge approaches to personalization and automation in online retail.

**💡 What You'll Find**
Code reviews and architectural discussions
Integration patterns for eCommerce platforms
Performance optimization techniques
Real-world case studies from production environments
Early access to beta tools and libraries
Collaboration opportunities on open-source projects

**🤝 Who's Already There**
Frontend & Backend Developers building eCommerce solutions
DevOps Engineers scaling automated systems
Technical Leaders architecting personalization engines
Product Engineers implementing conversion optimization
Open Source Contributors sharing automation libraries


**[🔗 Join the eCommerce Automation & Personalization Community](https://www.linkedin.com/groups/10153121/)**
A space where code meets commerce. Share your implementations, get feedback on your approaches, and stay ahead of the latest trends in eCommerce technology.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-salla` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Operations

This node supports the following Salla.sa resources and operations:

### Orders
- **Get**: Retrieve a specific order by ID
- **Get All**: Retrieve all orders with optional filtering
- **Update**: Update an existing order
- **Cancel**: Cancel an order

### Products
- **Create**: Create a new product
- **Get**: Retrieve a specific product by ID
- **Get All**: Retrieve all products with optional filtering
- **Update**: Update an existing product
- **Delete**: Delete a product

### Customers
- **Get**: Retrieve a specific customer by ID
- **Get All**: Retrieve all customers with optional filtering
- **Update**: Update an existing customer
- **Delete**: Delete a customer

### Addresses
- **Create**: Create a new address
- **Get**: Retrieve a specific address by ID
- **Get All**: Retrieve all addresses with optional filtering
- **Update**: Update an existing address
- **Delete**: Delete an address

### Special Offers
- **Create**: Create a new special offer
- **Get**: Retrieve a specific special offer by ID
- **Get All**: Retrieve all special offers with optional filtering
- **Update**: Update an existing special offer
- **Delete**: Delete a special offer

### Coupons
- **Create**: Create a new coupon
- **Get**: Retrieve a specific coupon by ID
- **Get All**: Retrieve all coupons with optional filtering
- **Update**: Update an existing coupon
- **Delete**: Delete a coupon

### Shipments
- **Create**: Create a new shipment
- **Get**: Retrieve a specific shipment by ID
- **Get All**: Retrieve all shipments with optional filtering
- **Update**: Update an existing shipment
- **Track**: Track a shipment

### Digital Products
- **Create**: Create a new digital product
- **Get**: Retrieve a specific digital product by ID
- **Get All**: Retrieve all digital products with optional filtering
- **Update**: Update an existing digital product
- **Delete**: Delete a digital product

## Credentials

This node uses OAuth2.0 authentication to connect to Salla.sa. The credentials are fully configurable within the n8n interface, with automatic token management and refresh functionality.

### OAuth2.0 Setup

1. Create a Salla application in your [Salla Partner Dashboard](https://salla.partners/)
2. Configure your Client ID and Client Secret directly in n8n credentials
3. Complete the OAuth flow - tokens are automatically saved and refreshed

### Setting up Salla OAuth2.0

1. Go to [Salla Partner Dashboard](https://salla.partners/)
2. Create a new application or select an existing one
3. Note down your **Client ID** and **Client Secret**
4. Set up the redirect URI in your Salla app settings to match your n8n OAuth callback URL
5. In n8n, create new **Salla OAuth2 API** credentials and configure them

### Credential Configuration

When creating **Salla OAuth2 API** credentials in n8n, you can configure:

#### Required Fields
- **Environment**: Choose Production or Sandbox
- **Client ID**: Your Salla application Client ID from Partner Dashboard
- **Client Secret**: Your Salla application Client Secret from Partner Dashboard

#### OAuth Configuration
- **OAuth Scopes**: Permissions to request (default: `offline_access`)
  - Common scopes: `offline_access`, `read`, `write`, `orders`, `products`, `customers`
- **Auto Refresh Tokens**: Automatically refresh tokens before expiry (default: enabled)
- **Token Refresh Buffer**: Refresh tokens X minutes before expiry (default: 30 minutes)

#### API Settings
- **API Version**: Choose v1 or v2 (v2 recommended)
- **Rate Limit Handling**: How to handle rate limits (Retry recommended)
- **Max Retries**: Maximum retries for rate-limited requests (default: 3)

#### Optional Settings
- **Webhook Secret**: For validating incoming webhooks
- **Store Domain**: Your store domain (auto-detected from token)

### Automatic Token Management

The node includes sophisticated token management:

- **Automatic Saving**: OAuth tokens are automatically saved after authentication
- **Auto Refresh**: Tokens are refreshed automatically before expiry
- **14-Day Expiry Handling**: Accounts for Salla's 14-day token expiry period
- **Configurable Buffer**: Refresh tokens with configurable time buffer
- **Error Recovery**: Automatic re-authentication on token errors

### OAuth Flow Process

1. **Setup Credentials**: Enter Client ID and Client Secret in n8n
2. **OAuth Authorization**: Click "Connect my account" to start OAuth flow
3. **Salla Login**: You'll be redirected to Salla to authorize your application
4. **Grant Permissions**: Approve the requested scopes for your integration
5. **Automatic Return**: You'll be redirected back to n8n with tokens saved
6. **Ready to Use**: Start using the Salla node in your workflows

### Token Storage and Security

- **Secure Storage**: All tokens are securely stored by n8n's credential system
- **Encrypted**: Client secrets and tokens are encrypted at rest
- **Automatic Refresh**: Refresh tokens are used automatically to maintain access
- **Environment Isolation**: Production and sandbox credentials are separate

## Compatibility

This node has been tested with:
- n8n version 1.0.0 and above
- Salla API v2 (recommended) and v1

## Usage

### Basic Examples

#### Get All Orders
1. Add the **Salla** node to your workflow
2. Select **Order** as the resource
3. Select **Get All** as the operation
4. Configure your filters (optional)
5. Execute the node

#### Create a Product
1. Add the **Salla** node to your workflow
2. Select **Product** as the resource
3. Select **Create** as the operation
4. Fill in the **Additional Fields** with product information
5. Execute the node

#### Filter Orders by Status
1. Add the **Salla** node to your workflow
2. Select **Order** as the resource
3. Select **Get All** as the operation
4. In **Filters**, add status filter (e.g., "completed", "pending")
5. Execute the node

### Advanced Features

#### Token Refresh
The node automatically handles OAuth2.0 token refresh considering Salla's 14-day token expiry:
- Tokens are monitored for expiration
- Automatic refresh occurs before expiry (configurable buffer time)
- Failed requests trigger automatic re-authentication
- All token management is transparent to the user

#### Rate Limiting
The node includes built-in rate limiting handling:
- **Retry Mode**: Automatically retry requests after rate limit reset
- **Fail Mode**: Fail immediately when rate limited
- **Configurable Retries**: Set maximum number of retry attempts
- **Intelligent Delays**: Respect rate limit headers for optimal timing

#### Environment Support
Support for both Production and Sandbox environments:
- **Environment Selection**: Choose in credentials configuration
- **Automatic URL Switching**: API endpoints switch based on environment
- **Separate Credentials**: Maintain different credentials for each environment

#### Pagination
When using **Get All** operations, you can:
- **Return All**: Fetch all items across all pages automatically
- **Limit**: Set a specific limit for the number of items to return
- **Automatic Handling**: Pagination is handled transparently

#### Webhook Integration
Use the **Salla Trigger** node for webhook integration:
- **Event Filtering**: Choose specific events to listen for
- **Signature Validation**: Automatic webhook signature validation
- **Raw Data Option**: Get raw webhook data or parsed event data
- **Error Handling**: Robust error handling for webhook processing

### Configuration Examples

#### Basic Setup
```javascript
// Minimum required configuration
{
  "environment": "production",
  "clientId": "your-client-id",
  "clientSecret": "your-client-secret"
}
```

#### Advanced Configuration
```javascript
// Full configuration with all options
{
  "environment": "production",
  "clientId": "your-client-id",
  "clientSecret": "your-client-secret",
  "oauthScopes": "offline_access read write orders products customers",
  "apiVersion": "v2",
  "rateLimitHandling": "retry",
  "maxRetries": 5,
  "autoRefreshTokens": true,
  "tokenRefreshBuffer": 60,
  "webhookSecret": "your-webhook-secret"
}
```

## Resources

- [Salla API Documentation](https://docs.salla.dev/)
- [Salla Partner Dashboard](https://salla.partners/)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

## Support

For issues and feature requests, please use the [GitHub repository](https://github.com/aolamer/n8n-nodes-salla) issues page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 