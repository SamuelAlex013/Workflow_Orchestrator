# n8n-nodes-kobana

This is an n8n community node for integrating with [Kobana API](https://github.com/universokobana/kobana-api-specs), enabling you to manage billing wallets (Carteiras de Cobrança) and bank slips (Boletos) directly from your n8n workflows.

## Installation

### Local Installation for Development

To install this package locally in your n8n instance:

1. **Build the package** (if not already built):
   ```bash
   npm install
   npm run build
   npm pack
   ```
   This creates a file `n8n-nodes-kobana-0.0.1.tgz`

2. **Install in your n8n custom folder**:
   ```bash
   # Navigate to your n8n custom nodes folder (usually ~/.n8n/custom/)
   cd ~/.n8n/custom/
   
   # Install the package from the .tgz file
   npm install /path/to/n8n-nodes-kobana/n8n-nodes-kobana-0.0.1.tgz
   ```

3. **Alternative: Link for development** (recommended for active development):
   ```bash
   # In the n8n-nodes-kobana directory
   npm link
   
   # In your n8n custom nodes folder
   cd ~/.n8n/custom/
   npm link n8n-nodes-kobana
   ```

4. **Restart n8n** to load the new nodes

### Community Installation (When Published)

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### npm (When Published)

```bash
npm install n8n-nodes-kobana
```

### n8n UI (When Published)

In n8n, go to **Settings** > **Community Nodes** and install `n8n-nodes-kobana`.

## Features

This n8n node provides **complete access to all 175 Kobana API endpoints** across both V1 and V2 APIs, organized by namespaces and resources.

### Two Node Implementations

1. **Kobana Node** - User-friendly interface for common operations with simplified field-based configuration
2. **Kobana Complete Node** - Full API access with dynamic endpoint selection for all 175 endpoints

## Complete API Coverage

## V1 API Resources (Complete List)

- **Bank Billets** - 9 operations
- **Bank Billet Accounts** - 7 operations  
- **Bank Billet Batches** - 8 operations
- **Bank Billet Discharges** - 2 operations
- **Bank Billet Payments** - 3 operations
- **Bank Billet Registrations** - 2 operations
- **Bank Billet Remittances** - 5 operations
- **Customers** - 6 operations
- **Customer Subscriptions** - 6 operations
- **Discharges** - 5 operations
- **Email Deliveries** - 3 operations
- **Events** - 2 operations
- **Imports** - 3 operations
- **Installments** - 5 operations
- **Remittances** - 6 operations
- **Reports** - 1 operation
- **SMS Deliveries** - 3 operations
- **User Info** - 1 operation
- **Webhook Deliveries** - 3 operations
- **Webhooks** - 5 operations

## V2 API Namespaces (Complete List)

### Admin Namespace (12 operations)
- User management (create, list, get, update, delete)
- Connection management
- Certificate management
- Subaccount management

### Charge Namespace (12 operations)
- PIX charge creation and management
- PIX account management
- Command tracking

### Data Namespace (1 operation)
- Bank billet queries

### EDI Namespace (2 operations)
- EDI box management

### Financial Namespace (11 operations)
- Financial account management
- Balance tracking
- Statement transactions
- Transaction imports and sync
- Provider management

### Payment Namespace (16 operations)
- Bank billet payments
- PIX payments
- DARF payments
- Utility payments
- Batch operations for all payment types

### Transfer Namespace (13 operations)
- Internal transfers
- PIX transfers
- TED transfers
- Batch transfers
- Transfer approval/rejection

## Authentication

The node requires a Kobana API token for authentication. You can obtain your API token from your Kobana account.

### Setting up credentials:
1. In n8n, go to **Credentials** > **New**
2. Select **Kobana API** from the list
3. Enter your API token
4. Choose the environment (Sandbox or Production)
5. Save the credentials

## Usage Examples

### Creating a Bank Slip

1. Add a **Kobana** node to your workflow
2. Select **Bank Slip** as the resource
3. Choose **Create** as the operation
4. Fill in the required fields:
   - Amount
   - Expiration date
   - Customer information (name, CPF/CNPJ, address, etc.)
5. Optionally add payment instructions, tags, and notification settings

### Listing Billing Wallets

1. Add a **Kobana** node to your workflow
2. Select **Billing Wallet** as the resource
3. Choose **Get Many** as the operation
4. Configure pagination options if needed
5. Execute to retrieve all billing wallets

### Getting a Bank Slip in PDF Format

1. Add a **Kobana** node to your workflow
2. Select **Bank Slip** as the resource
3. Choose **Get** as the operation
4. Enter the Bank Slip ID
5. Select **PDF** as the format
6. Execute to retrieve the PDF

## API Documentation

For detailed API documentation, please refer to:
- [Kobana API Specifications](https://github.com/universokobana/kobana-api-specs)
- [OpenAPI Specification](https://raw.githubusercontent.com/universokobana/kobana-api-specs/refs/heads/main/swagger/all-versions/kobana-api-all-versions-openapi-3_1.json)

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/universokobana/n8n-nodes-kobana.git
cd n8n-nodes-kobana

# Install dependencies
npm install

# Build the node
npm run build

# For development with watch mode
npm run dev
```

### Testing

```bash
# Run tests
npm test

# Run linting
npm run lint

# Fix linting issues
npm run lintfix
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and feature requests, please use the [GitHub Issues](https://github.com/universokobana/n8n-nodes-kobana/issues) page.

For Kobana API support, please contact [Kobana Support](mailto:dev@kobana.com.br).

## Resources

- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)
- [n8n Creator Hub](https://community.n8n.io/)
- [Kobana Website](https://kobana.com.br)

## Version History

### 0.0.1 - Complete API Implementation
- Initial release