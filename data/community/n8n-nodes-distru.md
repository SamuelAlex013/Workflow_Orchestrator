![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-distru

This is an n8n community node for integrating with Distru, a cannabis ERP software. It provides a comprehensive set of operations to interact with the Distru API.

## Installation

Follow these steps to install this node in your n8n instance:

```bash
npm install n8n-nodes-distru
```

For n8n versions < 0.200, use:
```bash
npm install n8n-nodes-distru@^1.0.0
```

## Credentials

You need to configure your Distru API credentials before using this node:

1. Open your n8n instance
2. Go to Settings > Credentials
3. Click on "Add Credential"
4. Search for "Distru API"
5. Enter your API Token
6. (Optional) Enable "Use Staging" if you want to use the staging environment

## Operations

### Get Operations
- **Get Assembly**: Retrieve assembly information
- **Get Batch**: Get batch details
- **Get Company**: Retrieve company information
- **Get Contact**: Get contact details
- **Get Inventory**: Retrieve inventory information
- **Get Invoice**: Get invoice details
- **Get Location**: Retrieve location information
- **Get Package**: Get package details
- **Get Payment Method**: Retrieve payment method information
- **Get Product**: Get product details
- **Get Purchase**: Retrieve purchase information
- **Get Sales Order**: Get sales order details
- **Get Stock Adjustment**: Retrieve stock adjustment information
- **Get Strain**: Get strain details
- **Get User**: Retrieve user information

### Create/Update Operations
- **Create Batch**: Create a new batch
- **Create Product**: Create a new product
- **Update Product**: Update an existing product
- **Upsert Invoice**: Create or update an invoice
- **Upsert Purchase**: Create or update a purchase
- **Upsert Sales Order**: Create or update a sales order

### Payment Operations
- **Invoice Payment**: Process invoice payments
- **Purchase Payment**: Process purchase payments

## Additional Fields

Most operations support additional fields for filtering and customization:
- Page Number
- Page Size
- Inserted Datetime
- Updated Datetime
- Various IDs for specific resources

## Example Usage

### Get Product Information
```json
{
  "operation": "getProduct",
  "additionalFields": {
    "id": "product-id-here",
    "page_size": 1
  }
}
```

### Create a Purchase Order
```json
{
  "operation": "upsertPurchase",
  "company_id": "company-id-here",
  "billing_location_id": "location-id-here",
  "items": [
    {
      "product_id": "product-id-here",
      "quantity": 10,
      "price": 100,
      "location_id": "location-id-here"
    }
  ]
}
```

## Support

For issues and feature requests, please [create an issue](https://github.com/Sebbytea/distru-n8n/issues) on GitHub.

## License

[MIT](LICENSE.md)

## 🎯 Features

The package currently includes a single consolidated node:

### Distru
- Company: Get (with filtering and pagination)
- Product: Create, Update, Get (with filtering and pagination)
- Sales Order: Upsert, Get (with filtering and pagination)

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:
- [Node.js](https://nodejs.org/en/) version 18.12 or higher
- [pnpm](https://pnpm.io/) package manager (version 9.1 or higher)
- [n8n](https://n8n.io/) installed globally (`pnpm install -g n8n`)
- A Distru account with API access

### Configuration

1. In your n8n instance, go to **Settings** > **Credentials**
2. Click on **New Credential**
3. Search for "Distru API"
4. Enter your Distru API token
5. (Optional) Toggle "Use Staging Environment" if you want to use the staging API

## 🔧 Development Setup

If you want to contribute or modify this node:

1. Clone the repository:
   ```bash
   git clone https://github.com/Sebbytea/distru-n8n.git
   cd distru-n8n
   ```
2. Install dependencies:
   ```bash
   pnpm install
   ```
3. Build the package:
   ```bash
   pnpm build
   ```
4. Link to your local n8n installation:
   ```bash
   pnpm link
   ```

## 📚 Usage Examples

### Paginated GET Requests

All GET operations (Company, Product, Sales Order) support filtering and pagination via the **Additional Fields** collection:

- **ID**: If set, fetches a single record by ID. If not found, falls back to filtering by ID in the collection endpoint.
- **Page Number**: The page number to fetch (default: 1).
- **Page Size**: The number of records per page (defaults: 5000 for Company/Product, 500 for Sales Order; these are also the max values).
- **Other Filters**: Use any other available fields to filter results (e.g., Inserted Datetime, Updated Datetime, Status, etc.).

#### Example: Get All Products, 5000 Per Page

1. Add the **Distru** node to your workflow
2. Select the "Product: Get" operation
3. In **Additional Fields**, set:
   - Page Number: `1`
   - Page Size: `5000`
   - (Optional) Add filters like Inserted Datetime, Updated Datetime, etc.
4. Run the node to retrieve up to 5000 products on the first page

#### Example: Get a Company by ID

1. Add the **Distru** node
2. Select the "Company: Get" operation
3. In **Additional Fields**, set:
   - ID: `<company_id>`
4. Run the node to retrieve the company by ID

#### Example: Get Orders with Status Filter and Pagination

1. Add the **Distru** node
2. Select the "Sales Order: Get" operation
3. In **Additional Fields**, set:
   - Status: `PENDING`
   - Page Number: `1`
   - Page Size: `500`
4. Run the node to retrieve the first 500 pending orders

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the [MIT License](LICENSE.md).

## 🔗 Useful Links

- [Distru API Documentation](https://apidocs.distru.dev/)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [n8n Community Forum](https://community.n8n.io/)

## 📫 Support

For support with this node, please:
1. Check the [GitHub Issues](https://github.com/Sebbytea/distru-n8n/issues) for existing problems and solutions
2. Create a new issue if your problem isn't already reported
3. Contact Distru support for API-specific questions

---

Made with ❤️ by Sebastian Tidwell
