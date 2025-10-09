# n8n-nodes-serb2b

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node for SerB2B e-commerce platform. It lets you use SerB2B in your n8n workflows.

SerB2B is a comprehensive B2B e-commerce platform that provides APIs for managing orders, products, customers, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### SerB2B Trigger

Triggers workflows when events occur in SerB2B:
- Order events (create, update, delete)
- Product events (create, delete)
- Customer events (create, delete, approve)
- Supplier events (create, delete, approve, decline, quantity change)
- Marketplace events (create, price approved)

### SerB2B Node

Performs actions in SerB2B:

#### Customer
- Create customer
- Delete customer
- Get customer
- Get all customers
- Update customer

#### Order
- Create order
- Delete order
- Get order
- Get all orders
- Update order

#### Product
- Create product
- Delete product
- Get product
- Get all products
- Update product

#### Category
- Get category
- Get all categories

#### Brand
- Get brand
- Get all brands

## Credentials

You need the following credentials for this node:

- **API Token**: Your SerB2B API token (available in Admin Panel > Settings > API Settings)
- **Domain**: Your SerB2B instance URL (e.g., https://your-domain.com)

### Getting API Token

1. Login to your SerB2B admin panel
2. Navigate to Settings > API Settings
3. Copy your API token
4. In n8n, create new credentials and paste the token

## Compatibility

- n8n version 0.170.0 or later
- SerB2B platform with API access

## Usage

### Example 1: Order Processing Workflow

```
SerB2B Trigger (Order Created) → Email Node → Slack Node
```

This workflow:
1. Triggers when a new order is created
2. Sends an email notification
3. Posts a message to Slack

### Example 2: Product Management

```
Schedule Trigger → SerB2B Node (Get All Products) → Filter Node → SerB2B Node (Update Product)
```

This workflow:
1. Runs daily at 9 AM
2. Gets all products from SerB2B
3. Filters products with low stock
4. Updates product status

### Example 3: Customer Onboarding

```
SerB2B Trigger (Customer Created) → SerB2B Node (Get Customer) → Email Node → CRM Node
```

This workflow:
1. Triggers when a new customer registers
2. Gets customer details
3. Sends welcome email
4. Adds customer to CRM

## Webhook Setup

The SerB2B Trigger node automatically manages webhooks:
- Creates webhooks when workflow is activated
- Deletes webhooks when workflow is deactivated
- No manual webhook management needed

## Event Data Format

### Order Events
```json
{
  "event": "orders/create",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": 12345,
    "order_number": "ORD-12345",
    "customer_id": 123,
    "customer_name": "John Doe",
    "total": 299.99,
    "items_count": 3
  }
}
```

### Product Events
```json
{
  "event": "products/create",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": 456,
    "name": "Product Name",
    "code": "PROD001",
    "price": 99.99,
    "stock": 100
  }
}
```

### Customer Events
```json
{
  "event": "customers/create",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "id": 789,
    "name": "Jane Doe",
    "email": "jane@example.com",
    "company": "ACME Corp"
  }
}
```

## Error Handling

The node provides detailed error messages for common issues:
- Invalid API credentials
- Network connectivity problems
- Invalid data formats
- Rate limiting

## Rate Limits

SerB2B API has the following rate limits:
- 1000 requests per hour per API token
- Webhooks are processed asynchronously

## Security

- API tokens are securely stored in n8n credentials
- Webhook signatures are verified using HMAC-SHA256
- All API requests use HTTPS

## Support

For support with this n8n node:
1. Check the [n8n community forum](https://community.n8n.io/)
2. Review SerB2B API documentation
3. Contact SerB2B technical support

## Development

To contribute to this node:

1. Clone the repository
2. Install dependencies: `npm install`
3. Build the node: `npm run build`
4. Test locally in n8n

## License

[MIT License](LICENSE)

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [SerB2B API documentation](https://docs.serb2b.com/api)
- [n8n workflow examples](https://n8n.io/workflows/)