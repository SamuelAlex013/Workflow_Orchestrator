# n8n-nodes-simplybook

This is an n8n community node. It lets you use SimplyBook.me in your n8n workflows.

SimplyBook.me is an online booking system for service businesses.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## How to install

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-simplybook` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Manual installation

To get started install the package in your n8n root directory:

`npm install n8n-nodes-simplybook`

For Docker-based deployments, add the following line before the font installation command in your [n8n Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile):

`RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-simplybook`

## Operations

- **Get Services**: Retrieve services with filter search.
- **Get Providers**: Retrieve providers with filter search.
- **Get Locations**: Retrieve locations with filter search.
- **Get Categories**: Retrieve categories with filter search.
- **Get Clients**: Retrieve clients list.
- **Create Client**: Create new client and return it.
- **Edit Client**: Edit client and return it.
- **Delete Client**: Delete client.
- **Get Slots**: Return array of available slots to book as admin.
- **Get Available Slots**: Return array of available slots to book.
- **Get First Available Slot**: Return first available slot for selected service/provider/date.
- **Get Slots Timeline**: Return data for slots timeline per date.
- **Get Bookings**: Return bookings list.
- **Create Booking**: Create new booking and return it.
- **Edit Booking**: Edit booking and return it.

## Triggers

- **Cancelled Booking**: Triggers when a booking is canceled.
- **New Booking**: Triggers when a new booking is created.
- **New Invoice**: Triggers when a new invoice is created.
- **Updated Booking Details**: Triggers when the following booking details are updated: date, time, service, or provider.
- **New Client**: Triggers when a new client is created.
- **New Offer**: Triggers when a new offer is created.

## Credentials

To use this node, you need to authenticate with the SimplyBook.me API. Follow these steps:

1. Sign up for a SimplyBook.me account.
2. Enter your credentials in the n8n SimplyBook node.

## Compatibility

This node is compatible with n8n version 1.81 and above. It hasn't been tested on other versions yet.

## Usage

Refer to the [SimplyBook.me API documentation](https://help.simplybook.me/index.php/User_API_guide) for detailed information on how to use the API.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [SimplyBook.me API documentation](https://help.simplybook.me/index.php/User_API_guide)
* [SimplyBook.me Developers API](https://simplybook.me/en/api/developer-api)
## Version history

* 0.3.4 - Update dependencies related to security (a security vulnerability found in xml-crypto)
* 0.3.0 - Minor fixes
* 0.2.0 - Minor fixes
* 0.1.0 - Initial release
