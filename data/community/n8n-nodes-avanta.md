# n8n-nodes-avanta

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

An n8n community node for integrating with the Avanta B2B E-Commerce platform. This node enables seamless integration with Avanta's comprehensive B2B commerce solution, allowing you to automate customer management, order processing, inventory tracking, and business reporting directly from your n8n workflows.

## Table of Contents

- [About Avanta](#about-avanta)
- [Installation](#installation)
- [Configuration](#configuration)
- [Operations](#operations)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## About Avanta

Avanta is a comprehensive B2B E-Commerce platform designed to streamline business-to-business transactions and relationships. The platform provides robust tools for managing customer companies, processing orders, handling complex pricing structures, and generating detailed business reports.

Key features of Avanta include:

- **Multi-Company Management**: Handle complex B2B customer hierarchies and relationships
- **Advanced Order Processing**: Support for bulk orders, custom pricing, and delivery scheduling
- **Comprehensive Reporting**: Detailed analytics for orders, shipments, invoices, and business performance
- **Flexible Product Catalog**: Manage extensive product catalogs with custom attributes and pricing
- **Integration Capabilities**: RESTful API for seamless integration with existing business systems

This n8n node provides direct access to Avanta's powerful API, enabling you to automate your B2B E-Commerce workflows and integrate Avanta with your existing business processes.

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install a community node**
3. Enter `n8n-nodes-avanta` in the npm package name field
4. Click **Install**

### Manual Installation

If you're running n8n locally, you can install this node manually:

```bash
# Navigate to your n8n installation directory
cd ~/.n8n

# Install the node
npm install n8n-nodes-avanta

# Restart n8n
```

### Docker Installation

For Docker installations, you can install community nodes by:

1. Using the n8n interface (recommended)
2. Building a custom Docker image with the node pre-installed

## Configuration

### Credentials Setup

1. In n8n, go to **Credentials** and create new **Avanta API** credentials
2. Fill in the required fields:
   - **Host**: Your Avanta API base URL including store scope (e.g., `https://your-avanta-instance.com/rest/STORE_CODE` or `https://your-avanta-instance.com/rest/all` for all stores)
   - **Access Token**: Your Avanta API access token

### Getting API Credentials

To obtain your Avanta API credentials, you'll need to generate an access token through the Avanta admin interface:

#### Step 1: Access the Admin Panel
1. Log into your Avanta system with administrator privileges
2. Navigate to **System > Integrations > API Tokens** in the admin menu

#### Step 2: Create a New Integration Token
1. Click **Add New Token** or **Create Integration**
2. Provide a descriptive name for your integration (e.g., "n8n Workflow Integration")
3. Select the appropriate **API Resources** and **Access Levels** based on your workflow needs:
   - **Companies**: For managing B2B customer companies and relationships
   - **Orders**: For order processing and management
   - **Products**: For catalog and inventory operations
   - **Reports**: For generating business analytics and reports
   - **Users**: For customer user management

#### Step 3: Configure Token Permissions
Set the appropriate access levels for each resource:
- **Read**: View existing data
- **Write**: Create and update data
- **Delete**: Remove data (use with caution)

#### Step 4: Generate and Secure Your Token
1. Click **Generate Token**
2. **Important**: Copy the generated access token immediately - it will only be displayed once
3. Store the token securely (consider using a password manager)
4. Note your API base URL including store scope (typically `https://your-domain.com/rest/STORE_CODE` or `https://your-domain.com/rest/all` for all stores)

#### Authentication Method
The Avanta API uses **Bearer Token Authentication**. All API requests must include the access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

#### Token Security Best Practices
- **Never share** your access token in public repositories or unsecured locations
- **Rotate tokens regularly** for enhanced security
- **Use separate tokens** for different environments (development, staging, production)
- **Monitor token usage** through the admin panel's API logs
- **Revoke unused tokens** to minimize security risks

#### Troubleshooting Authentication
If you encounter authentication issues:
1. Verify the token hasn't expired or been revoked
2. Check that the token has the necessary permissions for your operations
3. Ensure your API base URL is correct and accessible
4. Confirm your Avanta instance supports the API version being used

## Operations

The Avanta node supports comprehensive B2B E-Commerce operations across the following resources:

### Customer Companies
- **Create**: Register new B2B customer companies
- **Update**: Modify existing customer company profiles
- **Delete**: Remove customer companies from the platform

### Company Addresses
- **Create**: Add billing and shipping addresses for B2B customers
- **Update**: Modify existing company address information

### Company Contacts
- **Create**: Add contact persons for B2B customer companies
- **Update**: Update contact information and roles

### Company Users
- **Create**: Create user accounts for B2B customer access
- **Link**: Associate users with their respective companies

### Business Reports
- **Backorders**: Generate reports for items on backorder
- **Credit Memos**: Create credit memo documentation for returns
- **Invoices**: Generate invoice reports for B2B transactions
- **Orders**: Create comprehensive order reports and tracking
- **Reshipments**: Document reshipment activities and logistics
- **Shipments**: Track shipment status and delivery information
- **Trackings**: Monitor package tracking and delivery updates

### Product Catalog
- **Create**: Add new products to the B2B catalog
- **Update**: Modify existing product information and pricing

### Sales Organizations
- **Create**: Set up sales territories and organizational structures
- **Link**: Associate companies with their designated sales organizations

## Usage Examples

### Creating a Company

```json
{
  "name": "Example Corp",
  "email": "contact@example.com",
  "group_id": "1",
  "additionalFields": {
    "telephone": "+1-555-0123",
    "vat_id": "US123456789",
    "internet": "https://example.com"
  }
}
```

### Creating an Order Report

```json
{
  "customer_id": "CUST001",
  "company_id": 123,
  "customer_orderid": "ORD-2024-001",
  "order_positions": [
    {
      "item_pos": 1,
      "name": "Product A",
      "sku": "PROD-A-001",
      "qty": 5,
      "price": 29.99,
      "subtotal": 149.95
    }
  ]
}
```

### Creating a Company Address

```json
{
  "company_customer_id": "COMP001",
  "company_group_id": "1",
  "external_address_id": "ADDR001",
  "additionalFields": {
    "street": "123 Business Ave",
    "city": "Business City",
    "postcode": "12345",
    "country_id": "US",
    "address_type": 1
  }
}
```

## API Reference

### Authentication

All API requests require authentication using a Bearer token:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Base URL

All API endpoints are relative to your Avanta instance base URL including store scope:

```
https://your-avanta-instance.com/rest/STORE_CODE/V1/proline-admin/
```

Or for all stores:

```
https://your-avanta-instance.com/rest/all/V1/proline-admin/
```

### Common Parameters

Most operations support these common parameters:

- **bulk**: Boolean - Whether to process multiple items in a single request
- **return**: Boolean - Whether to return response to a webhook
- **extension_attributes**: Array - Custom attributes for extending data

### Error Handling

The node includes comprehensive error handling:

- **Continue on Fail**: Option to continue workflow execution even if the node fails
- **Detailed Error Messages**: Clear error descriptions for troubleshooting
- **Retry Logic**: Built-in retry mechanisms for transient failures

## Data Types and Validation

### Required Fields

Each B2B E-Commerce operation has specific required fields. Common required fields include:

- **Customer Company Operations**: `name`, `group_id` for company registration
- **Business Report Operations**: `customer_id`, `company_id` for transaction tracking
- **Address Operations**: `company_customer_id`, `company_group_id` for shipping/billing setup

### Optional Fields

Most B2B operations support additional optional fields through the "Additional Fields" collection, enabling:

- Custom business dates and delivery schedules
- Extension attributes for custom B2B requirements
- Document file attachments for compliance and documentation
- Custom pricing structures and quantity breaks
- Tax information and VAT handling
- Multi-currency support for international B2B transactions

### Date Formatting

Date fields are automatically formatted to ISO 8601 format when sent to the API.

## Workflow Integration

### B2B E-Commerce Use Cases

The Avanta node is designed for comprehensive B2B E-Commerce automation:

- **Customer Onboarding**: Automate new B2B customer registration and setup
- **Order Processing**: Streamline order intake, validation, and fulfillment workflows
- **Inventory Management**: Sync product catalogs and inventory levels
- **Business Reporting**: Generate automated reports for sales, shipments, and analytics
- **Multi-Company Management**: Handle complex B2B relationships and hierarchies

### Triggers

This node works well with:

- **Webhook triggers** for real-time order processing and customer updates
- **Schedule triggers** for batch reporting and inventory synchronization
- **Manual triggers** for on-demand B2B operations and testing

### Data Flow

The node can be chained with:

- **HTTP Request nodes** for additional API calls and third-party integrations
- **Set nodes** for data transformation and B2B-specific formatting
- **IF nodes** for conditional logic based on customer types or order values
- **Function nodes** for custom B2B business logic and calculations
- **Email nodes** for automated B2B communication and notifications

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify your API credentials are correct
   - Check that your access token hasn't expired
   - Ensure your host URL is correct

2. **Validation Errors**
   - Check that all required fields are provided
   - Verify data types match expected formats
   - Review field length limitations

3. **Connection Issues**
   - Verify network connectivity to your Avanta instance
   - Check firewall settings
   - Confirm SSL/TLS configuration

### Debug Mode

Enable debug mode in n8n to see detailed request/response information:

1. Set environment variable: `N8N_LOG_LEVEL=debug`
2. Restart n8n
3. Check logs for detailed API communication

## Contributing

We welcome contributions to improve this node! Here's how you can help:

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/ecoplan-avanta/n8n-nodes-avanta.git
cd n8n-nodes-avanta
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

4. Run linting:
```bash
npm run lint
```

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run tests and linting: `npm run lint`
5. Commit your changes: `git commit -m "Add your feature"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Submit a pull request

### Code Standards

- Follow TypeScript best practices
- Use ESLint configuration provided
- Add appropriate type definitions
- Include JSDoc comments for public methods
- Follow n8n node development guidelines

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

### Documentation

- [n8n Documentation](https://docs.n8n.io/)
- [Avanta API Documentation](https://docs.avanta.com/api)
- [Node Development Guide](https://docs.n8n.io/integrations/creating-nodes/)

### Community

- [n8n Community Forum](https://community.n8n.io/)
- [GitHub Issues](https://github.com/ecoplan-avanta/n8n-nodes-avanta/issues)

### Commercial Support

For commercial support and custom development:

- **Email**: info@ecoplan.com
- **Website**: https://www.ecoplan.com

## Changelog

### Version 0.1.9
- Fixed ESLint compliance issues
- Improved error handling
- Added comprehensive field validation
- Enhanced documentation

### Version 0.1.8
- Added support for bulk operations
- Improved API response handling
- Fixed authentication issues

### Version 0.1.7
- Initial release
- Basic CRUD operations for companies
- Report generation functionality
- Address and contact management

---

**Note**: This is a community-maintained node. For issues specific to the Avanta API itself, please contact Avanta support directly.
