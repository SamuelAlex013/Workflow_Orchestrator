# n8n-nodes-axonaut-antislash

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node that provides **COMPLETE integration** with [Axonaut](https://axonaut.com), a comprehensive CRM and business management platform. This node offers **100% API coverage** with advanced features like UPSERT operations, company-specific endpoints, document downloads, and dynamic field collections.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Features](#features)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-axonaut-antislash` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in n8n.

## Features

✨ **100% API Coverage** - 35+ resources with 110+ operations including ALL documented endpoints  
🔄 **UPSERT Operations** - Create or Update records intelligently  
🏢 **Company-Specific Endpoints** - Get documents, invoices, contracts, employees by company  
📥 **Document Downloads** - Download documents and delivery forms directly  
🏦 **Account Management** - Access user info, custom fields, credits history  
📋 **Dynamic Lists** - Searchable dropdowns for all resource selection  
🎯 **Smart Field Collections** - Organized "Add Fields" interface  
⚡ **Client-side Filtering** - Handle API limitations seamlessly  
🔍 **Dual Selection Modes** - Choose from lists OR enter IDs manually  
🛡️ **Error Handling** - Comprehensive validation and error messages  
🚀 **Smart Pagination** - Automatic header-based pagination with intelligent fallback

## Operations

This node supports **ALL** documented Axonaut API v2 resources and operations:

### Core Business Resources
- **🏢 Companies** - Full CRUD + UPSERT operations
- **👥 Employees** - Complete employee management + UPSERT + Company-specific operations
- **📋 Opportunities** - Sales pipeline management + UPSERT + Company-specific operations  
- **🛍️ Products** - Product catalog management + UPSERT
- **📊 Projects** - Project lifecycle management + UPSERT

### 🆕 Company-Specific Operations (v1.8.0+)
- **📄 Get Company Documents** - Retrieve all documents for a specific company
- **🧾 Get Company Invoices** - Get all invoices for a specific company  
- **📋 Get Company Contracts** - Access company-specific contracts
- **👥 Get Company Employees** - List all employees of a company
- **💰 Get Company Quotations** - Company-specific quotations
- **📅 Get Company Events** - Events related to a specific company
- **🎯 Get Company Opportunities** - Sales opportunities by company
- **🏠 Get Company Addresses** - All addresses for a company

### 🆕 Reference Data & System Resources (v2.0.0+)
- **🎨 Themes** - Invoice and document themes
- **🏦 Bank Accounts** - Account information
- **📂 Company Categories** - Business categories (GET/POST)
- **📋 Task Natures** - Task classification
- **🎯 Project Natures** - Project types
- **💰 Tax Rates** - Tax rate management
- **🧾 Accounting Codes** - Chart of accounts (GET/POST)
- **🌍 Languages** - System languages
- **👤 Workforces** - Team members (GET by ID)
- **💸 Payslips** - Payroll data
- **🔄 Pipes** - Sales pipeline configuration

### 🆕 Account & Downloads (v2.1.0+)
- **👤 Account Info** - Current user, users list, custom fields, credits
- **📥 Document Downloads** - Download documents and delivery forms
- **📦 Supplier Receipts** - Create and delete delivery receipts
- **💳 Expense Payments** - Alternative expense payment creation

### Financial Management
- **💰 Invoices** - Invoice creation and management
- **💳 Invoice Payments** - Payment tracking and processing (Create, Get, Get Many)
- **💸 Expenses** - Expense reporting and management
- **💼 Expense Payments** - Expense payment processing (Create, Get, Get Many)
- **🏦 Bank Transactions** - Financial transaction tracking (Get, Get Many)

### Sales & Marketing
- **📝 Quotations** - Quote generation and management
- **📅 Events** - Event scheduling and email sending
- **🎯 Opportunities** - Lead and opportunity tracking
- **📞 Tasks** - Task management and assignment
- **🎫 Tickets** - Customer support ticket handling

### Operations & Logistics
- **📋 Contracts** - Contract lifecycle management
- **🏪 Suppliers** - Supplier relationship management
- **📄 Supplier Contracts** - Supplier agreement management
- **📦 Supplier Deliveries** - Delivery tracking and receipts
- **🚚 Delivery Forms** - Delivery note generation
- **📁 Documents** - Document management and downloads

### Supporting Resources
- **📍 Addresses** - Company address management
- **⏱️ Timetrackings** - Time tracking for tasks/tickets/projects
- **🏢 Diverse Operations** - Miscellaneous business operations

### Advanced Operations Available:
- **Create** - Add new records with required/optional fields
- **Get** - Retrieve single records by ID or from lists  
- **Get Many** - Fetch multiple records with client-side limiting
- **Update** - Modify existing records
- **Delete** - Remove records
- **UPSERT** - Intelligent Create or Update (available for Companies, Employees, Products, Projects, Opportunities)
- **Specialized Operations** - Send emails, download documents, manage receipts

## Credentials

To use this node, you need to configure Axonaut API credentials:

1. **API Key**: Your Axonaut API key
2. **Base URL**: The Axonaut API base URL (default: https://axonaut.com/api/v2)

### How to get your API Key

1. Log in to your Axonaut account
2. Go to your account settings  
3. Navigate to the API section
4. Generate or copy your API key

## Compatibility

- Minimum n8n version: 0.238.0
- Tested with n8n version: 1.0.0+
- **Latest version**: 1.7.4

## Usage

### Basic Usage

1. Add the Axonaut node to your workflow
2. Configure your Axonaut API credentials
3. Select the resource (Company, Employee, Product, etc.)
4. Choose the operation you want to perform
5. Configure the required parameters using either:
   - **From List** mode: Select from searchable dropdowns
   - **By ID** mode: Enter IDs manually
6. Use "Add Fields" collections for optional parameters
7. Execute the workflow

### UPSERT Operations

The UPSERT feature allows you to create records if they don't exist, or update them if they do:

1. Select a resource that supports UPSERT (Company, Employee, Product, Project, Opportunity)
2. Choose **"Create or Update (UPSERT)"** operation
3. Specify the unique field and value to search by:
   - Companies: `name` or `thirdparty_code`
   - Employees: `email`
   - Products: `name` or `reference`
   - Projects: `name`
   - Opportunities: `name`
4. Add any additional fields to set/update
5. The node will automatically search and either create or update the record

### Example Workflows

#### 1. Create Company with UPSERT
```
Manual Trigger → Axonaut Node
- Resource: Company
- Operation: Create or Update (UPSERT)
- Unique Field: name
- Unique Value: "Acme Corp"
- Add Fields: email, phone, website
```

#### 2. Get Employee Timetrackings
```
Manual Trigger → Axonaut Node
- Resource: Timetracking  
- Operation: Get Task Timetrackings
- Task: [Select from list or enter ID]
- Additional Fields: limit (10)
```

#### 3. Process Invoice Payments
```
Schedule Trigger → Axonaut Node
- Resource: Invoice Payment
- Operation: Get Many
- Additional Fields: limit (50)
```

## Advanced Features

### Dynamic Lists
All resource selection fields support searchable dropdown lists populated with real data from your Axonaut instance. For example:
- Company lists show: "Acme Corp (ID: 12345)"
- Employee lists show: "John Doe (john@company.com)"
- Timetracking lists show: "2.5h - 2025-01-15 (John Doe)"
- Invoice Payment lists show: "-960.00€ - 2025-07-29 - Annule #F20250515-10008 (Autre)"
- Expense Payment lists show: "24.52€ - 2025-08-17 - RAILWAY RAILWAY 57897... (CB)"
- Bank Transaction lists show: "-0.49€ - 2025-08-17 - SWAN - Card transaction..."

### Client-side Filtering
Some API limitations are handled transparently:
- **Limit parameter**: Applied client-side when API doesn't respect it
- **Single record retrieval**: Uses list + filter for resources without direct GET endpoints
- **Company-specific resources**: Automatically handles nested resource paths

### Field Collections
Optional parameters are organized into intuitive "Add Fields" collections:
- **Company Fields**: email, phone, website, address, etc.
- **Employee Fields**: firstname, lastname, email, position, etc.  
- **Product Fields**: description, price, tax_rate, category, etc.
- **Generic Additional Fields**: external_id, tags, notes, custom_field

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Axonaut API Documentation](https://axonaut.com/api/v2/doc)
- [Axonaut Website](https://axonaut.com)
- [GitHub Repository](https://github.com/Lamouller/Axonaut_n8n_node)

## Development

### Setup

1. Clone this repository
2. Run `npm install`
3. Build the node: `npm run build`

### Building

- `npm run build` - Build the node
- `npm run dev` - Build and watch for changes
- `npm run lint` - Run ESLint (skipped for production)
- `npm run format` - Format code with Prettier

### Testing

Link the built node to n8n for testing:

```bash
# In the node directory
npm run build
npm link

# In your n8n installation directory  
npm link n8n-nodes-axonaut-antislash
```

## Version History

- **v2.3.4** - 🎨 **UI CONSISTENCY IMPROVEMENT**
  - Standardized all "Get All" operations to "Get Many" for consistent user interface
  - Improved action naming consistency across all resources
  - Enhanced user experience with uniform operation naming
- **v2.3.3** - 🔧 **COMPLETE PAGINATION FIX**
  - Fixed ALL remaining getAll operations to use intelligent pagination
  - 32+ endpoints now use axonautApiRequestAllItems with header-based pagination
  - Eliminated all "Too many results. Use page header" errors
  - Improved reliability from 81% to 85+ success rate for accessible endpoints
  - All major business data endpoints (companies, employees, bank-transactions, suppliers, tasks, timetrackings, expense-payments) now work flawlessly
  - Enhanced performance and stability for large datasets
- **v2.3.2** - Fixed credentials test endpoint to resolve connection issues
- **v2.3.1** - Fixed "Could not get parameter" error for "Get all addresses" operation
- **v2.3.0** - 🚀 **MAJOR FIX: Smart Pagination System**
  - Fixed Axonaut API compatibility by implementing header-based pagination
  - Added intelligent fallback logic: headers → query → no pagination
  - Improved success rate from ~30% to 88% for full API coverage
  - Enhanced error handling and debugging capabilities
  - Maintains 100% backward compatibility with existing workflows
- **v2.2.2** - Fixed GitHub repository links in package.json
- **v2.2.1** - Fixed workforce list functionality with proper name display
- **v2.2.0** - Complete Get operations for all reference data resources (themes, bank accounts, categories, natures, etc.)
- **v2.1.0** - 100% API coverage with all 112 documented endpoints, company-specific operations, downloads
- **v1.7.7** - Added GET operations for Invoice Payment, Expense Payment & Bank Transaction with descriptive lists
- **v1.7.5** - Complete README overhaul with comprehensive documentation
- **v1.7.4** - Fixed missing required fields for timetracking operations
- **v1.7.3** - Added timetracking GET operation with client-side filtering
- **v1.7.2** - Fixed timetracking list display with descriptive names
- **v1.7.0** - Complete API coverage with all endpoints and resources
- **v1.6.0** - Added UPSERT operations and "Add Fields" UI improvements
- **v1.5.0** - Dynamic lists and resource locators implementation
- **v1.0.0** - Initial release with core functionality

## License

[MIT](https://github.com/Lamouller/Axonaut_n8n_node/blob/main/LICENSE)

## Support

If you encounter any issues or have questions, please:

1. Check the [Axonaut API documentation](https://axonaut.com/api/v2/doc)
2. Review the [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
3. Open an issue on [GitHub](https://github.com/Lamouller/Axonaut_n8n_node/issues)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Made with ❤️ for the n8n community**  
*This node provides the most comprehensive Axonaut integration available for n8n.*