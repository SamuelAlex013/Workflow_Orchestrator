# Teamleader n8n Node Integration

## Overview
This project is an n8n custom node integration for Teamleader, a popular online CRM platform. The purpose of this integration is to provide a seamless way to connect your workflows in n8n with the various resources offered by Teamleader, including users, contacts, companies, deals, invoices, projects, and more.

Currently, this project is **under active development**, meaning features are being continuously added and refined. Please note that there are still many aspects that are not yet complete or that may be subject to change.

## Features
- OAuth2 authentication with Teamleader.
- Support for CRUD operations across a variety of Teamleader resources, such as Users, Contacts, Companies, Deals, Tickets, and more.
- All types of triggers (Webhooks) are supported.
- Flexible parameter handling to allow customization for each resource operation.

## Unsupported Resources
The following functions from the Teamleader API were not yet implemented:

1. **Quotations**:
   - `quotations.list` - List quotations
   - `quotations.info` - Get a specific quotation
   - `quotations.delete` - Remove a quotation

2. **Work Types**:
   - `workTypes.list` - List all work types

3. **Document Templates**:
   - `documentTemplates.list` - List document templates

4. **Currencies**:
   - `currencies.exchangeRates` - Get exchange rates

5. **Notes**:
   - `notes.list` - List notes
   - `notes.update` - Update a note

6. **Email Tracking**:
   - `emailTracking.create` - Create new email tracking
   - `emailTracking.list` - List email tracking records

7. **Closing Days**:
   - `closingDays.list` - List account closing days
   - `closingDays.add` - Add a closing day
   - `closingDays.delete` - Remove a closing day

8. **Day Off Types**:
   - `dayOffTypes.list` - List day-off types

9. **Activity Types**:
   - `activityTypes.list` - List all activity types

10. **Level Two Areas (for Addresses)**:
    - `levelTwoAreas.list` - List address areas

11. **Payment Terms**:
    - `paymentTerms.list` - List available payment terms

12. **Commercial Discounts**:
    - `commercialDiscounts.list` - List discounts

13. **Payment Methods**:
    - `paymentMethods.list` - List payment methods

14. **Projects**:
    - `projects.create` - Creating projects
    - `projects.update` - Creating projects
    - 
15. **Invoices**:
    - `invoices.list` - List invoices
    - `invoices.create` - Creating invoices
    - `invoices.update` - Creating invoices

16. **Deals**:
    - `deals.create` - Creating deals

### Why?
The omitted functions from the `n8n` implementation generally require complex data structures and intricate handling of resource relationships. At this stage, the focus remains on simpler operations and trigger-based functionality. Further development may include these features as data structures and dependencies are refined.

## Disclaimer
**This project is still in development**, and many functionalities are expected to evolve over time. Please use it with caution in production environments as some features might not be fully stable.

If you have ideas for improvements, feature requests, or encounter issues, please check out the GitHub Issues tab to see what's currently planned or in progress. Feel free to contribute by opening an issue or submitting a pull request.

## Getting Started
To use this n8n node:
1. Clone the repository and install dependencies.
2. Build the project and link it to your local n8n instance.
3. Configure the node by providing the necessary credentials (OAuth2 via Teamleader).

Detailed installation instructions are coming soon!

### Requirements
- Node.js
- n8n v1.66.0 or later
- Teamleader API access

## Usage
- **Authentication**: This node uses OAuth2 authentication to connect with Teamleader. You need to set up a new integration via Teamleader's Marketplace to obtain your Client ID and Client Secret.
- **Resources and Operations**: You can add this node to your workflow and use any of the supported resources with the appropriate operations. Parameters are automatically adjusted based on the selected resource.

## Development
This project is open-source and contributions are highly appreciated. Please ensure that all changes are well-tested and consistent with the existing codebase.

### Running Locally
- Clone the repository.
- Run `npm install` to install all required dependencies.
- Use `npm run build` to build the project.
- Start an n8n instance linked with this node.

### Contribution Guidelines
- Please follow the coding standards used throughout the project.
- Open an issue before submitting large changes to discuss your approach.
- Pull requests are reviewed and merged as time permits.

## Roadmap
- [x] Add support for webhooks and triggers for real-time updates.
- [x] Improve error handling and logging throughout the node.
- [ ] Integrate all ressources, actions and parameters from the API

## Issues
Please report any issues or bugs using the GitHub Issues page. Contributions to resolve these issues are highly welcome.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this code, provided the original author is credited.

---

Thank you for using and contributing to the Teamleader n8n node integration!

