# n8n-nodes-icount

[![npm version](https://badge.fury.io/js/n8n-nodes-icount.svg)](https://badge.fury.io/js/n8n-nodes-icount)
[![Tests](https://github.com/binesamit/n8n-nodes-icount/actions/workflows/test.yml/badge.svg)](https://github.com/binesamit/n8n-nodes-icount/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/binesamit/n8n-nodes-icount/branch/master/graph/badge.svg)](https://codecov.io/gh/binesamit/n8n-nodes-icount)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Community node for n8n to work with iCount - Israeli accounting system.

[n8n](https://n8n.io/) is an automation platform with [fair-code license](https://docs.n8n.io/reference/license/).

## Installation

1. Open n8n
2. Go to Settings → Community Nodes
3. Click "Install a community node"
4. Enter: `n8n-nodes-icount`
5. Click Install

Or follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n documentation.

## Credentials Setup

Before you start, you'll need to create an API Token in iCount:

1. Log in to iCount
2. Go to Settings → API
3. Create a new API Token
4. Copy the Token

### Creating Credentials in n8n

1. Open the workflow editor
2. Add an iCount node
3. Click "Credential to connect with"
4. Click "+ Create New"
5. Enter your API Token
6. Save

**Note:** You must use an API Token, not cid/user/pass!

---

## Resources

### 📄 Document

Manage accounting documents - invoices, receipts, quotes, and more.

### 👥 Customer

Manage customers - create, update, retrieve, and list.

---

## Document Operations

### 1. Create - Create New Document

**When to use:** When you want to create an invoice, receipt, quote, or other document.

**Required Fields:**
- **Document Type:** Loaded dynamically from the API - select from the updated list
  - Includes: Tax Invoice, Tax Invoice Receipt, Receipt, Order, Quote, Delivery Note, and more

- **Client Name:** Full name of the client

**Important Optional Fields:**
- **Client ID:** Existing client ID in the system
- **Email:** Email address to send the document
- **VAT ID:** Tax ID number
- **Phone:** Phone number
- **Address:** Address

**Items:**
- **Description:** Item description
- **Quantity:** Quantity
- **Unit Price:** Unit price
- **VAT:** VAT percentage (default: 18)

**Example:**
```
Document Type: invoice
Client Name: John Doe
Email: john@example.com
VAT ID: 123456789
Items:
  - Description: Consulting Services
    Quantity: 10
    Unit Price: 500
    VAT: 18
```

**Output:**
- `doc_id` - Document ID (UUID)
- `doc_number` - Document number
- `pdf_link` - PDF download link

---

### 2. Convert - Convert Document

**When to use:** When you want to convert a document from one type to another (e.g., quote to order).

**Required Fields:**
- **Document Type:** Current document type (loaded dynamically from API)
- **Document Number:** Document number to convert

**Fields:**
- **Get Conversion Options:**
  - `ON` (default) - Returns list of available conversion options
  - `OFF` - Performs conversion (requires Conversion Type)
- **Conversion Type:** Type of conversion (only when Get Conversion Options is off)

**Example - Get Options:**
```
Document Type: 300 (Quote)
Document Number: 1001
Get Conversion Options: ON
```

**Example - Perform Conversion:**
```
Document Type: 300 (Quote)
Document Number: 1001
Get Conversion Options: OFF
Conversion Type: order
```

---

### 3. Update Income Type - Update Document Income Type

**When to use:** When you want to change the income type assigned to a document (for reporting purposes).

**Required Fields:**
- **Document Type:** Document type (loaded dynamically from API)
- **Document Number:** Document number

**Fields:**
- **Income Type:** Choose between ID or Name
  - `Income Type ID` - Numeric ID of the income type
  - `Income Type Name` - Name of income type (will be created automatically if doesn't exist)

**Example:**
```
Document Type: 320 (Tax Invoice)
Document Number: 2007
Income Type: Income Type Name
Income Type Name: Technical Consulting
```

---

### 4. Cancel - Cancel Document

**When to use:** When you want to cancel a document (creates a cancellation document in the system).

**Required Fields:**
- **Document Type:** Document type
- **Document Number:** Document number to cancel

**Optional Fields:**
- **Refund Credit Card:**
  - `OFF` - Only cancel the document
  - `ON` - Also refund credit card transaction if exists
- **Cancellation Reason:** Reason for cancellation

**Example:**
```
Document Type: invoice
Document Number: 2007
Refund Credit Card: OFF
Cancellation Reason: Customer requested cancellation
```

**Important:** If Refund Credit Card is checked, the system will try to cancel the credit card transaction. If no transaction exists - you'll get an error.

---

### 5. Close - Close Document

**When to use:** When you want to close a document (e.g., mark an order as "completed").

**Required Fields:**
- **Document Type:** Document type
- **Document Number:** Document number

**Optional Fields:**
- **Based On Documents:** List of base documents (JSON)

**Example:**
```
Document Type: order
Document Number: 1001
Based On Documents: [{"doctype": "offer", "docnum": 500}]
```

---

### 6. Get - Get Specific Document

**When to use:** When you want to retrieve all details of a specific document.

**Required Fields:**
- **Document Type:** Document type
- **Document Number:** Document number

**Example:**
```
Document Type: invoice
Document Number: 2007
```

**Output:**
- All document details
- Client information
- Items
- Prices and totals
- PDF link

---

### 7. Search - Search Documents

**When to use:** When you want to find documents by various criteria.

**Fields:**
- **Return All:** Whether to return all results (up to 1000)
- **Max Results:** Maximum number of results (if Return All is off)
- **Detail Level:** Detail level (0-10)
  - `0` - Basic (doctype + docnum)
  - `1` - Standard (+ date, client, amount)
  - `10` - Complete (everything)

**Filters:**
- **Client ID:** Search by client ID
- **Client Name:** Search by client name
- **Email:** Search by email
- **Document Type:** Filter by document type
- **Document Number:** Specific document number
- **Document Status:**
  - `0` - Open
  - `1` - Closed
  - `2` - Partially closed
- **Start Date / End Date:** Date range
- **Sort Field:** Field to sort by (date, number, client name)
- **Sort Order:** Sort order (ASC / DESC)

**Example - Search client invoices:**
```
Return All: true
Detail Level: Complete (Everything)
Filters:
  Client ID: 2
  Document Type: invoice
  Start Date: 2025-01-01
  Sort Field: Issue Date
  Sort Order: DESC
```

---

### 8. List - List Documents

**When to use:** When you want to get a list of all documents (without filters).

**Fields:**
- **Return All:** Whether to return everything
- **Limit:** Maximum number of results
- **Additional Fields:**
  - **Combine All Items:**
    - `OFF` (default) - Each document as a separate item
    - `ON` - All documents in one item

**Example:**
```
Return All: false
Limit: 50
Additional Fields:
  Combine All Items: OFF
```

---

### 9. Get Document URL - Get Document Link

**When to use:** When you want to get a link to view the document (PDF) without downloading.

**Required Fields:**
- **Document Type:** Document type
- **Document Number:** Document number

**Optional Fields:**
- **Language:** Language (Hebrew/English)
- **Original Document:** Original or copy
- **Hide ILS Prices:** Hide ILS prices (for foreign currency documents)
- **Document Language:** Document language (overrides API language)
- **Email To:** Email for tracking

**Example:**
```
Document Type: invoice
Document Number: 2007
Language: Hebrew
Original Document: true
```

**Output:**
- `url` - Direct link to PDF document

---

## Customer Operations

### 1. Create - Create New Customer

**When to use:** When you want to create a new customer in the system.

**Required Fields:**
- **Client Name:** Customer name

**Optional Fields:**
- **Email:** Email
- **Phone:** Phone
- **Mobile:** Mobile
- **HP Number (Tax ID):** Tax ID or personal ID number (saved in `vat_id` field)
- **Client Type:** Client type (loaded dynamically from API)
- **Bank:** Bank (loaded dynamically from API)
- **Employee Assigned:** Assigned employee (loaded dynamically from API)
- **Address, City, Zip:** Full address
- **Home Address Fields:** Full residential address
- **Payment Terms:** Payment terms (in days)

**Example:**
```
Client Name: Example Company Ltd.
Email: info@example.com
Phone: 03-1234567
Mobile: 050-1234567
HP Number: 123456789
Client Type: Company
Bank: Bank Leumi
City: Tel Aviv
Payment Terms: 30
```

---

### 2. Update - Update Existing Customer

**When to use:** When you want to update details of an existing customer.

**Required Fields:**
- **Client ID:** Customer ID

**Fields to Update:**
- All fields are available for update (Email, Phone, Address, etc.)

**Example:**
```
Client ID: 123
Email: new-email@example.com
Phone: 03-9999999
```

---

### 3. Upsert - Create or Update Customer

**When to use:** When you want to add a new customer or update an existing one.

**How it works:**
- The system searches for a customer by Tax ID or email
- If found - updates
- If not - creates new

**Required Fields:**
- **Client Name:** Customer name

**Optional Fields:**
- **Email:** Email
- **Phone:** Phone
- **Mobile:** Mobile
- **VAT ID:** Tax ID
- **Address, City, Zip:** Full address
- **Payment Terms:** Payment terms (in days)

**Example:**
```
Client Name: Example Company Ltd.
Email: info@example.com
Phone: 03-1234567
Mobile: 050-1234567
VAT ID: 123456789
Address: Example Street 1
City: Tel Aviv
Zip: 12345
Payment Terms: 30
```

**Output:**
- `client_id` - Customer ID in the system
- All customer details

---

### 4. Get - Get Customer by ID

**When to use:** When you have a customer ID and want to get all their details.

**Required Fields:**
- **Client ID:** Customer ID

**Example:**
```
Client ID: 2
```

**Output:**
- All customer details
- Activity history
- Open documents

---

### 5. Delete - Delete Customer

**When to use:** When you want to delete a customer from the system.

**Required Fields:**
- **Client ID:** Customer ID to delete

**Example:**
```
Client ID: 123
```

---

### 6. List - List Customers

**When to use:** When you want to get a list of all customers in the system.

**Fields:**
- **Return All:** Whether to return all customers
- **Limit:** Maximum number (if Return All is off)
- **Additional Fields:**
  - **Combine All Items:**
    - `OFF` (default) - Each customer as a separate item
    - `ON` - All customers in one item

**Example:**
```
Return All: true
Additional Fields:
  Combine All Items: OFF
```

**Output:**
- Array of all customers with all details

---

### 7. Get Open Docs - Get Open Documents for Customers

**When to use:** When you want to see which customers have open documents (debts).

**Optional Fields:**
- **Client ID:** Filter specific customer
- **Options:**
  - **Document Type:** Specific document type
  - **Get Items:** Include item details too
  - **Email:** Filter by email
  - **Client Name:** Filter by name

**Example - All open documents:**
```
(Leave empty to get all)
```

**Example - Open documents for specific customer:**
```
Client ID: 2
Options:
  Get Items: true
```

**Output:**
- List of open documents
- Amounts due
- Customer details

---

### 8. Get Contacts - Get Customer Contacts

**When to use:** When you want to get a list of contacts for a specific customer.

**Required Fields:**
- **Client ID:** Customer ID

**Example:**
```
Client ID: 123
```

**Output:**
- List of contacts with all details

---

### 9. Add Contact - Add Contact to Customer

**When to use:** When you want to add a new contact to an existing customer.

**Required Fields:**
- **Client ID:** Customer ID
- **Contact Name:** Contact name

**Optional Fields:**
- **Contact Type:** Contact type (loaded dynamically from API)
- **Email:** Email
- **Phone:** Phone
- **Mobile:** Mobile
- **Notes:** Notes

**Example:**
```
Client ID: 123
Contact Name: John Smith
Contact Type: Primary Contact
Email: john@example.com
Phone: 03-1234567
```

---

### 10. Update Contact - Update Contact

**When to use:** When you want to update details of an existing contact.

**Required Fields:**
- **Client ID:** Customer ID
- **Contact ID:** Contact ID

**Fields to Update:**
- **Contact Name:** New name
- **Contact Type:** New type (loaded dynamically from API)
- **Email, Phone, Mobile:** Updated contact details

**Example:**
```
Client ID: 123
Contact ID: 456
Contact Name: John Smith (Updated)
Email: john.new@example.com
```

---

### 11. Delete Contact - Delete Contact

**When to use:** When you want to delete a contact from a customer.

**Required Fields:**
- **Client ID:** Customer ID
- **Contact ID:** Contact ID to delete

**Example:**
```
Client ID: 123
Contact ID: 456
```

---

## Special Features

### Dynamic Dropdowns

The node supports dropdowns that load automatically from the iCount API:

- **Document Type** - In nodes: Create, Convert, Update Income Type
- **Bank** - In nodes: Create Customer, Update Customer, Upsert Customer
- **Employee Assigned** - In nodes: Create Customer, Update Customer, Upsert Customer
- **Client Type** - In nodes: Create Customer, Update Customer, Upsert Customer
- **Contact Type** - In nodes: Add Contact, Update Contact

All lists update automatically based on what's configured in your iCount system.

---

## Complete Workflow Examples

### Example 1: Create Invoice from Webhook

```
1. Webhook (receive order)
   ↓
2. iCount - Upsert Customer
   - Client Name: {{ $json.customer_name }}
   - Email: {{ $json.customer_email }}
   - Phone: {{ $json.customer_phone }}
   ↓
3. iCount - Create Document
   - Document Type: invoice
   - Client ID: {{ $('iCount').item.json.client_id }}
   - Client Name: {{ $json.customer_name }}
   - Items:
     - Description: {{ $json.product_name }}
     - Quantity: {{ $json.quantity }}
     - Unit Price: {{ $json.price }}
   ↓
4. Send Email
   - To: {{ $json.customer_email }}
   - Subject: Invoice #{{ $('iCount1').item.json.doc_number }}
   - Body: Document link: {{ $('iCount1').item.json.pdf_link }}
```

---

### Example 2: Daily Report of Open Documents

```
1. Schedule Trigger (every morning)
   ↓
2. iCount - Get Open Docs
   - Return All: true
   ↓
3. Filter (only debts over 30 days)
   ↓
4. Send Email (report to manager)
```

---

### Example 3: Sync Customers from CRM

```
1. HTTP Request (get customers from CRM)
   ↓
2. Loop Over Items
   ↓
3. iCount - Upsert Customer
   - Client Name: {{ $json.name }}
   - Email: {{ $json.email }}
   - Phone: {{ $json.phone }}
   - VAT ID: {{ $json.vat_id }}
   ↓
4. Set (save IDs)
```

---

### Example 4: Search and Cancel Invoices

```
1. iCount - Search Documents
   - Document Type: invoice
   - Client ID: 2
   - Document Status: Open
   ↓
2. Filter (by specific criteria)
   ↓
3. iCount - Cancel
   - Document Type: invoice
   - Document Number: {{ $json.docnum }}
   - Cancellation Reason: Automatic cancellation
```

---

## Common Errors and Solutions

### Error: "auth_required"
**Solution:** Verify that the API Token is correct and created in iCount.

### Error: "bad_doctype"
**Solution:** Use the correct values: invoice, invrec, receipt, refund, order, offer, delivery, deal

### Error: "missing_client_name"
**Solution:** Client name is required when creating a document.

### Error: "doc_not_found"
**Solution:** Verify that the document number and document type are correct.

### Empty customer/document list
**Solution:** Check the debug output in the response, the response might be in a different field.

---

## Tips and Tricks

### Using Expressions
```javascript
// Use current date
{{ $now.format('yyyy-MM-dd') }}

// Calculate total
{{ $json.quantity * $json.price * 1.18 }}

// String concatenation
{{ "Invoice for customer " + $json.client_name }}
```

### Loop Over Items
If you have multiple items, use a Loop:
```
1. Set (prepare items array)
2. Loop Over Items
3. iCount - Create Document (one item at a time)
```

### Save Results
Use a Set node to save IDs:
```javascript
{
  "invoice_id": "{{ $('iCount').item.json.doc_id }}",
  "invoice_number": "{{ $('iCount').item.json.doc_number }}",
  "pdf_url": "{{ $('iCount').item.json.pdf_link }}"
}
```

---

## Testing

This project includes comprehensive testing infrastructure with **330 passing tests** and **~90% code coverage**.

### CI/CD & Automation

**🔧 First Time Setup:** See [SETUP_TOKENS.md](SETUP_TOKENS.md) for Codecov and npm publishing configuration.

- ✅ GitHub Actions - Automated testing on every push/PR
- ✅ Codecov Integration - Automatic coverage reports
- ✅ Automated npm Publishing - One-click releases

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch

# Run specific test suites
npm run test:unit
npm run test:integration
npm run test:e2e
npm run test:performance
```

### Test Coverage

| Component | Tests | Coverage |
|-----------|-------|----------|
| Utils | 36 | 100% ✅ |
| Load Options | 107 | 100% ✅ |
| Integration Tests | 149 | ~95% ✅ |
| E2E Workflow Tests | 17 | ~90% ✅ |
| Performance Tests | 21 | N/A |
| Overall | **330** | ~90% ✅ |

See [TESTING.md](TESTING.md) for detailed testing documentation.
See [PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md) for performance testing guide.

**Test Breakdown:**
- ✅ Utils (36 tests): Idempotency (14) + API Request (22)
- ✅ Load Options (107 tests): Banks (13) + Document Types (15) + Users (25) + Client Types (26) + Contact Types (28)
- ✅ Document Operations (54 tests): Create (16) + Search (18) + Cancel (20)
- ✅ Customer Operations (95 tests): Create (29) + Update (30) + Delete (18) + Upsert (18)
- ✅ E2E Workflows (17 tests): Customer Management (8) + Document Lifecycle (9)
- ✅ Performance Tests (21 tests): Load Testing (8) + Stress Testing (6) + Rate Limit Testing (7)

---

## Additional Resources

- [iCount API Documentation (official)](https://apiv3.icount.co.il/docs/iCount/)
- [n8n Documentation](https://docs.n8n.io/)
- [Workflow Examples](https://n8n.io/workflows)
- [Testing Documentation](TESTING.md)

## Support

For issues and questions:
- [Open an issue on GitHub](https://github.com/binesamit/n8n-nodes-icount/issues)
- [n8n Community](https://community.n8n.io/)

## License

MIT

## Disclaimer

This project is provided "as is", without any warranty of any kind, express or implied.
Use it at your own risk.

The purpose of this repository is to share knowledge and provide tools for the community.
The maintainers are not responsible for any issues, damages, or losses caused by the use of this code.

For the official iCount API documentation, please refer to:
👉 [https://apiv3.icount.co.il/docs/iCount/](https://apiv3.icount.co.il/docs/iCount/)

---

**Current Version:** 1.0.54

**Last Updated:** January 2025

## Version History

### v1.0.54 (latest)
- ✅ Restructured project - moved all files to root directory
- ✅ Improved standard npm package layout

### v1.0.53
- ✅ Updated repository URL

### v1.0.52
- ✅ Updated comprehensive README with all features and operations

### v1.0.51
- ✅ Fixed Document Types dropdown - correct reading from `doctypes` field
- ✅ Added dynamic dropdowns to Convert Document and Update Income Type

### v1.0.50
- ✅ Added dynamic dropdown for Document Types
- ✅ Added Convert Document node - document conversion
- ✅ Added Update Income Type node - update income type
- ✅ Removed Update Document node (doesn't work in API)

### v1.0.49
- ✅ Added Combine All Items option in List operations
- ✅ Option to get all items in one item or each item separately

### v1.0.48
- ✅ Fixed List operations to return each item separately
- ✅ Correct handling of objects returned by API

### v1.0.47
- ✅ Restored Home Address fields for customers
- ✅ Fixed HP/VAT ID saving (using vat_id)

### v1.0.42-45
- ✅ Added dynamic dropdowns: Bank, Employee Assigned, Client Type, Contact Type
- ✅ Fixed handling of objects from API

### Earlier Versions
- Basic support for documents and customers
- Basic CRUD operations
