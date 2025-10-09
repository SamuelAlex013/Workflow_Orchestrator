<p align="center">
  <img width="180" height="180" src="/nodes/ApaleoAPI/apaleo.svg">
</p>


# n8n Nodes for Apaleo

This repository provides custom nodes for [n8n](https://n8n.io), enabling integration with Apaleo, a property management platform tailored for the hospitality industry. Use these nodes to automate workflows that interact with Apaleo's data and services.

To contribute and make this custom node available to the community, create it as an npm package and publish it to the npm registry.

## install

![Settings Animation](install.gif)

## Setup

### Get Apaleo API Credentials

1. Log in to your [Apaleo account](https://app.apaleo.com/apps/connected-apps/create) to create and retrieve a new App and get your client id and secret id.
2. Go to **APPS** > **connected Apps** in the n8n dashboard
3. Click **create new** and select **Aindividual App**
4. Enter your **Client Code** and **Client Name** and save them and get your **Credentials**


### Add Credentials to n8n

1. Go to ***Settings*** > ***Credentials*** in the n8n dashboard
2. Click ***New*** and select Apaleo API
3. Enter your Apaleo API credentials and save them

## Implemented Endpoints

The following Apaleo endpoints are currently supported:

- ⬜ Inventory V1 0/33
- ⬜ Rate Plan V1 0/43
- ✅ Booking V1 53/53
- 🔄 Finance V1 7/60

## Features

- **Comprehensive API Coverage**: Implements a wide range of Apaleo API endpoints for bookings, reservations, blocks, and more.
- **Type Safety**: Full TypeScript implementation with proper type definitions.
- **Error Handling**: Robust error handling with descriptive error messages.
- **Parameter Validation**: Validates input parameters including dates, required fields, and formats.
- **Flexible Filtering**: Supports extensive filtering options for listing operations.
- **Data Expansion**: Allows expanding related data in responses where supported.
- **Pagination Support**: Implements proper pagination for list operations.
- **OAuth Authentication**: Secure authentication using OAuth 2.0.

## Parameter Options

### Common Filter Parameters

- **Property IDs**: Filter by specific properties
- **Unit Groups**: Filter by unit group types or IDs
- **Date Range**: Filter by various date types (arrival, departure, stay, etc.)
- **Status**: Filter by reservation or booking status
- **Channel**: Filter by booking channel (Direct, BookingCom, Expedia, etc.)
- **Market Segments**: Filter by market segments
- **Text Search**: Search across relevant fields

### Expansion Options

- Property details
- Unit group information
- Rate plan details
- Service information
- Company data
- Block details

## Usage

After setting up the credentials, you can add Apaleo nodes to your workflows by selecting **Apaleo** in the node selection menu. Configure each node by choosing the relevant actions and fields provided by Apaleo.

## Usage Examples

Create workflows that automatically retrieve and manage bookings, cancellations, and customer data from Apaleo. Integrate this data with other applications such as CRMs, email systems, and more.

### Example Workflows

1. **Automated Booking Confirmation**
   - Trigger on new booking
   - Send confirmation email
   - Update CRM system

2. **No-Show Management**
   - Monitor check-in status
   - Process no-show charges
   - Update availability

3. **Group Booking Handling**
   - Create group blocks
   - Manage group reservations
   - Send group-specific communications

## Test Locally

Test your node locally to ensure everything works as expected. For more information, refer to the [documentation on running nodes locally](https://docs.n8n.io/nodes/creating-nodes/testing/).

## Support

If you encounter any issues or have feature requests, please open an issue in this repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
