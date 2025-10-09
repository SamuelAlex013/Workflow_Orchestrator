# n8n-nodes-simla

This is a n8n community node. It lets you use Simla API in your n8n workflows.

Simla is a customer relationship management (CRM) platform that helps businesses manage sales, customer interactions, and messaging.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following resources and operations:

### Customer
- **Get**: Get customers by filter
- **Create**: Create customer
- **Edit**: Edit customer

### Order
- **Get**: Get orders by filter
- **Create**: Create order
- **Edit**: Edit order

### Message
- **Send**: Send a message to chat

### Dialog
- **Assign**: Assign a dialog to a user or bot
- **Unassign**: Unassign a dialog
- **Close**: Close a dialog

## Credentials

To use the Simla node, you need to authenticate with the Simla API:

1. You need a Simla account
2. Create a Simla API key - [documentation](https://docs.simla.com/Users/Integration/APIEditing). Minimal required permissions:
	- **Orders**: Read and write
	- **Customers**: Read and write
	- **Integration**: Read and write
3. Provide:
	- **Simla URL**: Your Simla instance URL
	- **Simla API key**: Your API key for authentication

The node uses API key authentication with the key sent in the X-Api-Key header.

## Compatibility

This node has been tested with n8n version 1.109.1.

## Usage

### Customer and order operations:
Fill in the necessary fields in the filter to search for a customer or order.

#### Saving an order with a customer
Select Simla Trigger with Trigger On: _Customer Message_.
![img.png](docs/customerOrderCreate.png)
You can search for a customer by _customerMgId_:
![img.png](docs/customerGet.png)
When creating an order, specify Customer -> ID:
![img.png](docs/orderWithCustomer.png)

Choose the necessary fields from fixedCollection for creating and editing a customer or order.
#### Order creation example:
![img.png](docs/orderCreate.png)

#### Customer edition example:
![img.png](docs/customerEdit.png)

### Illustrative example of chat interactions:
Select Simla Trigger with Trigger On: _Customer Message_.
When a message is received in Simla, the message is passed to $json.body.payload[0].content. Depending on the message written by the client:
- a greeting is sent to the client;
- the dialog is assigned to the appropriate manager;
- the dialog is unassigned from the responsible person;
- the dialog is closed.

![img.png](docs/chatManipulation.png)

To send a message, specify the Chat ID from INPUT. To manage the dialog, select dialogId in the corresponding field.

![img.png](docs/chatSendMessage.png)


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Simla API Documentation](https://docs.simla.com/Developers/API/APIVersions/APIv5)
