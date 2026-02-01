# n8n-nodes-insyte

This is an n8n community node for the [Insyte CRM API](https://new-api.insyteblinds.com/swagger/index.html), specifically designed for the Window Furnishings Industry.

## 🤖 AI Tool Support (v0.2.0+)

This node is **AI-tool ready** and can be used with n8n's AI Agent nodes for natural language CRM operations.

### Using with AI Agents

1. Add an **AI Agent** node to your workflow
2. Add the **Insyte CRM** node
3. Connect Insyte to the AI Agent's **tool port**
4. Configure the tool in AI Agent with a descriptive name and description
5. For community nodes, ensure environment variable is set:
   ```bash
   N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
   ```

### AI Mode Features

- **Natural Language Queries**: Use plain English to interact with the CRM
- **Smart Resource Detection**: Automatically identifies whether you're working with contacts, companies, jobs, etc.
- **Intelligent Operation Mapping**: Understands "find", "search", "get" from context, plus "book appointment" and "check availability" for Live Diary
- **Parameter Extraction**: Extracts names, emails, locations from natural language

### Example AI Queries

- "Find all contacts in NSW"
- "Get invoices from last month"
- "Search for companies named Acme"
- "Check available appointment slots next week"
- "Book an appointment for John Doe"

## Features

### Read-Only CRM Data Access

Access Insyte CRM data (read-only):
- 📋 **Activities** - View tasks and activity records
- 🏢 **Companies** - View business entities
- 👤 **Contacts** - View customer contact information
- 💵 **Invoices** - View invoice records
- 🔨 **Jobs** - View job/project data
- 💼 **Opportunities** - View sales opportunity pipeline
- 💰 **Payments** - View payment records

### Lead Booking (Write Access)

Create new leads with scheduled appointments:
- 📅 **Live Diary** - Check availability and book sales appointments
  - **Check Availability**: Query available time slots for sales meetings
  - **Book Lead**: Create new lead with contact details and scheduled appointment

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Local Installation

1. Navigate to your n8n installation directory
2. Install the package:
```bash
npm install n8n-nodes-insyte
```
3. Restart n8n

### Docker Installation

Add the following to your docker-compose.yml:

```yaml
environment:
  - N8N_COMMUNITY_PACKAGES_ENABLED=true
```

Then install via the n8n UI or by adding to your dockerfile.

## Credentials

To use this node, you'll need:

1. **API Key** - Your Insyte API authentication key
2. **Base URL** - Default: `https://new-api.insyteblinds.com`
3. **API Version** - Choose between v1 or v2 (v2 recommended)

### Getting API Credentials

Contact your Insyte administrator or refer to the [Insyte API documentation](https://new-api.insyteblinds.com/swagger/index.html) for obtaining API credentials.

## Operations

### CRM Data Resources (Read-Only)

Standard resources (Activities, Companies, Contacts, Invoices, Jobs, Opportunities, Payments) support:

- **Search** - Search for records using natural language or filters (AI-optimized)
- **Get Many** - Retrieve multiple records with OData filtering
- **Get** - Retrieve a single record by ID

> **Note**: The Insyte API provides read-only access to CRM data. To create or modify records, use the Insyte application directly.

### Live Diary Operations (Write Access)

The Live Diary resource provides the only write operations available via the API:

- **Check Availability** - Query available appointment slots (location, date range, duration, filters)
- **Book Lead** - Create a new lead with contact details and scheduled sales appointment

### OData Query Support

The node supports OData query parameters for filtering and sorting:

- `$filter` - Filter results (e.g., `FirstName eq 'John'`)
- `$select` - Select specific fields
- `$orderby` - Sort results (e.g., `LastName desc`)
- `$expand` - Include related entities
- `$top` / `$skip` - Pagination

## Example Workflows

### 1. Get All Contacts

```json
{
  "resource": "contact",
  "operation": "getAll",
  "returnAll": true
}
```

### 2. Create a New Contact

```json
{
  "resource": "contact",
  "operation": "create",
  "fields": {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "+61 2 9999 9999"
  }
}
```

### 3. Filter Companies by State

```json
{
  "resource": "company",
  "operation": "getAll",
  "additionalFields": {
    "filter": "State eq 'NSW'",
    "orderby": "Name asc"
  }
}
```

## Resources

### Contact Fields
- `FirstName`, `LastName`
- `Email`, `Phone`, `Mobile`
- `CompanyID`
- `Address`, `City`, `State`, `Postcode`

### Company Fields
- `Name`, `TradingName`
- `ABN`
- `Email`, `Phone`
- `Address`, `City`, `State`, `Postcode`

### Activity Fields
- `Subject`, `Description`
- `Type`, `Status`, `Priority`
- `DueDate`
- `ContactID`, `CompanyID`, `AssignedTo`

### Opportunity Fields
- `Name`, `Description`
- `Stage`, `Probability`, `Amount`
- `CloseDate`
- `ContactID`, `CompanyID`, `OwnerID`

### Job Fields
- `JobNumber`, `Description`
- `Status`
- `StartDate`, `EndDate`
- `TotalAmount`
- `ContactID`, `CompanyID`
- `SiteAddress`

### Invoice Fields
- `InvoiceNumber`
- `Date`, `DueDate`
- `Status`
- `TotalAmount`, `TaxAmount`
- `ContactID`, `CompanyID`, `JobID`

### Payment Fields
- `PaymentNumber`
- `Date`, `Amount`
- `Method`, `Reference`
- `ContactID`, `CompanyID`, `InvoiceID`

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/jezweb/n8n-nodes-insyte.git

# Install dependencies
npm install

# Build the node
npm run build

# Run tests
npm test
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and feature requests, please use the [GitHub issues page](https://github.com/jezweb/n8n-nodes-insyte/issues).

## License

[MIT](LICENSE.md)

## Disclaimer

This is a community node and is not officially supported by Insyte or n8n. Use at your own risk.