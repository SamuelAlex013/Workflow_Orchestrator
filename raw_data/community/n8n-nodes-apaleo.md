# n8n-nodes-apaleo

![Apaleo Logo](nodes/Apaleo/apaleo.svg)

This package provides n8n nodes to interact with the [Apaleo API](https://docs.apaleo.com/), allowing you to automate workflows with Apaleo's property management system.

## Features

This integration provides two nodes:

- **Apaleo**: Perform operations on over 40 Apaleo resources including accounts, reservations, properties, and more
- **Apaleo Trigger**: Receive webhook events from Apaleo to trigger workflows

## Prerequisites

- [n8n](https://n8n.io/) (version 1.0.0 or later)
- Apaleo account with API credentials (Client ID and Client Secret)
- Node.js (version 20.15 or later)

## Installation

### In n8n Desktop / Self-hosted

1. Go to **Settings > Community Nodes**
2. Click on **Install**
3. Enter `n8n-nodes-apaleo` in the **Enter npm package name** field
4. Click on **Install**

### Manual Installation

1. Clone this repository:
   ```
   git clone https://github.com/apaleo/n8n-nodes-apaleo.git
   ```
2. Navigate to the project directory:
   ```
   cd n8n-nodes-apaleo
   ```
3. Install dependencies:
   ```
   npm install
   ```
4. Build the package:
   ```
   npm run build
   ```
5. Link to your n8n installation:
   ```
   npm link
   ```
6. In your n8n installation directory:
   ```
   npm link n8n-nodes-apaleo
   ```

## Credentials

To use the Apaleo nodes, you need to set up credentials:

1. In n8n, go to **Credentials**
2. Click on **Create New**
3. Search for "Apaleo OAuth2 API"
4. Enter your Apaleo Client ID and Client Secret
5. Save the credentials

## Usage

### Apaleo Node

The Apaleo node allows you to interact with the following resources:

#### Property Management
- **Property**: Manage hotel properties, including details, settings, and configurations
- **Unit**: Handle individual room/unit operations and information
- **UnitGroup**: Manage groups of units with similar characteristics
- **UnitAttribute**: Work with attributes that define unit features and amenities
- **PropertySettings**: Configure property-specific settings and preferences
- **PropertyActions**: Perform specific actions on properties

#### Reservation Management
- **Reservation**: Create, retrieve, and manage guest reservations
- **ReservationActions**: Execute specific actions on reservations (check-in, check-out, etc.)
- **ReservationAvailability**: Check availability for specific reservation scenarios
- **Block**: Manage room blocks for groups and events
- **BlockActions**: Perform actions on blocks (create, modify, cancel)
- **Booking**: Handle booking operations across the system
- **Group**: Manage group reservations and associated data

#### Financial Operations
- **Folio**: Access and manage guest folios containing charges and payments
- **FolioActions**: Perform specific actions on folios
- **FolioPayments**: Handle payment operations within folios
- **Invoice**: Create, retrieve, and manage invoices
- **InvoiceAction**: Execute specific actions on invoices
- **SubLedger**: Access financial sub-ledger information
- **CapturePolicies**: Manage payment capture policies
- **CustomSubAccounts**: Work with custom financial sub-accounts

#### Rate and Pricing
- **Rate**: Manage rate information and pricing
- **RatePlan**: Configure and manage rate plans
- **Offer**: Handle special offers and promotions
- **PromoCodes**: Manage promotional codes for special rates
- **CorporateCodes**: Handle corporate rate codes and agreements
- **CancellationPolicy**: Configure and manage cancellation policies
- **NoShowPolicy**: Set up and manage no-show policies

#### Account Management
- **Account**: Manage account information and settings
- **AccountActions**: Perform specific actions on accounts
- **Company**: Handle company account information and relationships

#### Reporting and Logs
- **Reports**: Access various system reports
- **BookingLogs**: View logs of booking-related activities
- **FinanceLogs**: Access logs of financial transactions and changes
- **Operations**: Perform operational tasks and reporting

#### Additional Resources
- **Availability**: Check general availability across properties
- **Types**: Access system type definitions
- **UiIntegrations**: Manage UI integration settings
- **Maintenance**: Handle maintenance-related operations
- **AgeCategory**: Manage age categories for guests
- **CityTax**: Configure and manage city tax settings
- **FeatureSettings**: Adjust feature-specific settings
- **InvoiceAddress**: Manage invoice address information
- **Languages**: Configure language settings
- **MarketSegment**: Manage market segment definitions
- **TimeSliceDefinitions**: Configure time slice settings
- **HealthCheck**: Verify system health and connectivity
- **Subscriptions**: Manage API event subscriptions

For each resource, you can select from available operations like GET, POST, PUT, DELETE, etc. based on the Apaleo API capabilities.

### Apaleo Trigger Node

Use this node to start workflows when specific events occur in Apaleo, such as:

- Reservation created, modified, or canceled
- Check-in or check-out completed
- Payment processed or refunded
- Folio or invoice created or updated
- Property settings changed
- Rate plan or availability updates
- And many more events from the Apaleo system

The trigger node works by subscribing to Apaleo's webhook events, allowing your n8n workflows to react in real-time to changes in your Apaleo environment.

## Development

If you want to contribute or modify the nodes:

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```
3. Start development mode:
   ```
   npm run dev
   ```
4. Make your changes
5. Build the package:
   ```
   npm run build
   ```
6. Test your changes locally

## License

[MIT](LICENSE.md)

## About Apaleo

[Apaleo](https://apaleo.com/) is a cloud-based property management system (PMS) that provides APIs for the hospitality industry, allowing seamless integration with various hotel systems and services.
