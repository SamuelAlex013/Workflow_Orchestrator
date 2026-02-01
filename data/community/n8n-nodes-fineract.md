# n8n-nodes-fineract

![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

This package provides n8n nodes for integrating with the [Fineract API](https://demo.mifos.io/api-docs/apiLive.htm), enabling you to manage clients and loans in your microfinance operations through n8n workflows.

## Features

- **Unified Fineract Node**: Single node with Client and Loan resources for comprehensive Fineract API integration
- **Client Management**: Complete client lifecycle management with 20+ operations including create, update, activate, close, transfer, and more
- **Loan Management**: Comprehensive loan operations including 15+ transaction commands for the complete loan lifecycle
- **Secure Authentication**: Support for Fineract's authentication system with tenant isolation
- **Comprehensive API Coverage**: Full support for Fineract's client and loan management APIs
- **Advanced Filtering**: Powerful search and filtering capabilities for both clients and loans
- **Transaction Management**: Complete loan transaction support including repayments, write-offs, refunds, and more

## Installation

To use this package in your n8n instance:

1. Install the package:

   ```bash
   npm install n8n-nodes-fineract
   ```

2. Restart your n8n instance to load the new nodes.

## Configuration

### Fineract API Credentials

Before using the nodes, you need to configure your Fineract API credentials. The node supports two authentication methods:

#### Username/Password Authentication

1. **Base URL**: The URL of your Fineract instance (e.g., `https://your-fineract-instance.com`)
2. **Authentication Method**: Select "Username/Password"
3. **Username**: Your Fineract username
4. **Password**: Your Fineract password
5. **Tenant ID**: The tenant identifier (usually "default" for single-tenant setups)

#### OIDC Access Token Authentication

1. **Base URL**: The URL of your Fineract instance (e.g., `https://your-fineract-instance.com`)
2. **Authentication Method**: Select "OIDC Access Token"
3. **Access Token**: Your OIDC access token
4. **Tenant ID**: The tenant identifier (usually "default" for single-tenant setups)

> **Note**: For OIDC authentication, you'll need to obtain an access token from your Fineract instance's OIDC provider. The token should have the necessary scopes to access the Fineract API.

## Usage

### Fineract Node

The Fineract node provides two main resources:

#### Client Resource

The Client resource provides comprehensive client lifecycle management with the following operations:

**Basic Operations:**

- **List**: Retrieve a list of clients with advanced filtering options
- **Get**: Retrieve a specific client by ID with field selection
- **Create**: Create a new client with complete information
- **Update**: Update an existing client's information
- **Delete**: Delete a client

**Client Lifecycle Management:**

- **Activate**: Activate a client account
- **Close**: Close a client account
- **Reject**: Reject a client application
- **Withdraw**: Withdraw a client application
- **Reactivate**: Reactivate a closed client
- **Undo Rejection**: Reverse a client rejection
- **Undo Withdrawal**: Reverse a client withdrawal

**Staff Management:**

- **Assign Staff**: Assign staff member to a client
- **Unassign Staff**: Remove staff assignment from a client

**Transfer Operations:**

- **Propose Transfer**: Propose transferring client to another office
- **Withdraw Transfer**: Withdraw a proposed transfer
- **Accept Transfer**: Accept a proposed client transfer
- **Reject Transfer**: Reject a proposed client transfer
- **Propose and Accept Transfer**: Propose and accept transfer in one step

**Account Management:**

- **Update Savings Account**: Update default savings account for a client

#### Loan Resource

The Loan resource provides comprehensive loan lifecycle management with the following operations:

**Basic Operations:**

- **List**: Retrieve a list of loans with advanced filtering options (status, office, account number, etc.)
- **Get**: Retrieve a specific loan by ID with field selection
- **Create**: Create a new loan application with complete details
- **Update**: Update an existing loan's information

**Loan Lifecycle Management:**

- **Approve**: Approve a loan application
- **Disburse**: Disburse an approved loan
- **Close**: Close a loan account

**Payment Operations:**

- **Repay**: Record loan repayments
- **Down Payment**: Record down payments on loans
- **Recovery Payment**: Record recovery payments on written-off loans

**Refund Operations:**

- **Refund by Cash**: Process cash refunds
- **Merchant Issued Refund**: Process merchant-issued refunds
- **Credit Balance Refund**: Process credit balance refunds

**Interest Management:**

- **Waive Interest**: Waive interest on loans
- **Goodwill Credit**: Apply goodwill credits to loans

**Loan Status Management:**

- **Write Off**: Write off loan amounts
- **Undo Write Off**: Reverse write-off transactions
- **Charge Off**: Charge off loans
- **Foreclosure**: Process loan foreclosures

**Advanced Filtering:**

- Filter by loan status (Active, Approved, Closed, etc.)
- Filter by office ID and hierarchy
- Search by account number or external ID
- SQL-based custom filtering
- Order by various fields (account number, display name, office, etc.)

### Example Workflows

#### Complete Client Onboarding Process

1. **Create Client**: Add a "Fineract" node with "Client" → "Create" operation
   - Configure: First Name, Last Name, Office ID, Activation Date
   - Optional: Mobile number, email, external ID
2. **Activate Client**: Add another "Fineract" node with "Client" → "Activate" operation
3. **Assign Staff**: Add a "Fineract" node with "Client" → "Assign Staff" operation
   - Set staff ID and assignment date

#### Complete Loan Lifecycle Management

1. **Create Loan Application**: Add a "Fineract" node with "Loan" → "Create" operation
   - Configure: Client ID, Product ID, Principal Amount, Interest Rate, Term
2. **Approve Loan**: Add a "Fineract" node with "Loan" → "Approve" operation
   - Set approval date and approved amount
3. **Disburse Loan**: Add a "Fineract" node with "Loan" → "Disburse" operation
   - Set disbursement date and transaction amount
4. **Record Repayment**: Add a "Fineract" node with "Loan" → "Repay" operation
   - Set transaction date, amount, and payment type

#### Advanced Loan Management

1. **Search Active Loans**: Add a "Fineract" node with "Loan" → "List" operation
   - Filter by status: "Active"
   - Order by: "Account No"
2. **Process Interest Waiver**: Add a "Fineract" node with "Loan" → "Waive Interest" operation
   - Set transaction date and amount to waive
3. **Handle Write-off**: Add a "Fineract" node with "Loan" → "Write Off" operation
   - Set transaction date and write-off amount
4. **Process Recovery**: Add a "Fineract" node with "Loan" → "Recovery Payment" operation
   - Record recovery payments on written-off loans

#### Client Transfer Process

1. **Propose Transfer**: Add a "Fineract" node with "Client" → "Propose Transfer" operation
   - Set destination office and transfer date
2. **Accept Transfer**: Add a "Fineract" node with "Client" → "Accept Transfer" operation
   - Complete the transfer process

#### Bulk Operations

1. **List Clients by Office**: Use "Client" → "List" with office ID filter
2. **Process Multiple Repayments**: Loop through loan list and process repayments
3. **Generate Reports**: Use list operations with various filters to generate reports

## Supported Operations Summary

### Client Operations (20 total)

- **Basic**: List, Get, Create, Update, Delete
- **Lifecycle**: Activate, Close, Reject, Withdraw, Reactivate, Undo Rejection, Undo Withdrawal
- **Staff**: Assign Staff, Unassign Staff
- **Transfer**: Propose Transfer, Withdraw Transfer, Accept Transfer, Reject Transfer, Propose and Accept Transfer
- **Account**: Update Savings Account

### Loan Operations (15 total)

- **Basic**: List, Get, Create, Update
- **Lifecycle**: Approve, Disburse, Close
- **Payments**: Repay, Down Payment, Recovery Payment
- **Refunds**: Refund by Cash, Merchant Issued Refund, Credit Balance Refund
- **Interest**: Waive Interest, Goodwill Credit
- **Status**: Write Off, Undo Write Off, Charge Off, Foreclosure

### Advanced Features

- **Pagination**: Support for large datasets with configurable page sizes
- **Filtering**: Multiple filter options including status, office, date ranges, and custom SQL
- **Sorting**: Order results by various fields in ascending or descending order
- **Field Selection**: Choose specific fields to return in responses
- **External IDs**: Support for external system integration
- **Transaction Notes**: Add notes to all transaction operations

## API Documentation

For detailed information about the Fineract API, refer to the [official documentation](https://demo.mifos.io/api-docs/apiLive.htm).

### Fineract API Endpoints Used

- **Clients**: `/clients` - Client management operations
- **Loans**: `/loans` - Loan management operations
- **Transactions**: `/loans/{id}/transactions` - Loan transaction operations
- **Authentication**: Supports both username/password and OIDC token authentication

## Troubleshooting

### Common Issues

#### Authentication Errors

- **401 Unauthorized**: Check your credentials and tenant ID
- **403 Forbidden**: Verify your user has the necessary permissions
- **Invalid Token**: Ensure OIDC tokens are not expired

#### Operation Failures

- **Validation Errors**: Check required fields are provided
- **Business Rule Violations**: Ensure operations are performed in correct order (e.g., approve before disburse)
- **Resource Not Found**: Verify client/loan IDs exist and are accessible

#### Performance Issues

- **Large Datasets**: Use pagination and filtering to limit results
- **Timeout Errors**: Consider breaking large operations into smaller batches
- **Rate Limiting**: Implement delays between API calls if needed

### Getting Help

1. Check the [GitHub Issues](https://github.com/Yann-J/n8n-nodes-fineract/issues) for known problems
2. Review the [Fineract API documentation](https://demo.mifos.io/api-docs/apiLive.htm)
3. Create a new issue with detailed error information

## Contributing

We welcome contributions! Here's how you can help:

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/n8n-nodes-fineract.git`
3. Install dependencies: `npm install`
4. Make your changes
5. Run tests: `npm run test`
6. Create a pull request

### Code Standards

- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Ensure all linting checks pass

### Reporting Issues

- Use the GitHub issue tracker
- Include detailed reproduction steps
- Provide error messages and logs
- Specify your n8n and Fineract versions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
