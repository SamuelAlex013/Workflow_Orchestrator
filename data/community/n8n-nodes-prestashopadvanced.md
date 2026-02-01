# n8n-nodes-prestashopadvanced

This is an n8n community node. It lets you integrate [PrestaShop](https://www.prestashop.com/) Webservice/API in your n8n workflows.

It supports both **actions** (managing main resources) and **triggers** (listening for new entities created in PrestaShop).

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources) 

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

npm Package Name: **n8n-nodes-prestashopadvanced**

## Operations

#### Cart Rule (Voucher)
- Create a cart rule
- Delete a cart rule
- Get a cart rule
- Get all specific prices (allowing filtering and sorting by multiple fields)

#### Customers
- Create a customer
- Update a customer (only the specified attributes)
- Delete a customer
- Get a customer
- Get all customers (allowing filtering and sorting by multiple fields)

#### Orders
- Get an order
- Get all orders (allowing filtering and sorting by multiple fields)
- Delete an order
- Change order state
- Set order internal note
- Set order shipping number

#### Products
- Create a product
- Update a product (only the specified attributes)
- Update a product stock (set quantity)
- Delete a product
- Get a product
- Get all products (allowing filtering and sorting by multiple fields)

#### Specific Prices
- Create a specific price
- Update a specific price (only the specified attributes)
- Delete a specific price
- Get a specific price
- Get all specific prices (allowing filtering and sorting by multiple fields)

### Trigger Events
- Address created
- Carrier created
- Cart Rule created
- Cart created
- Category created
- Combination created
- Customer Message created
- Customer Thread created
- Customer created
- Employee created
- Manufacturer created
- Message created
- Order Carrier created
- Order Detail created
- Order History created
- Order Payment created
- Order created
- Product created
- Specific Price Rule created
- Specific Price created
- Stock Available created
- Store created
- Supplier created
- Tag created

## Credentials

You need a **PrestaShop API Key** and the **base URL** of your store.

1. In your PrestaShop back office, go to **Advanced Parameters → Webservice**.
2. Enable the webservice and generate a key.
3. Use this key and your store URL in the node credentials in n8n.

## Compatibility

- Minimum n8n version: **1.0.0**
- Tested with:
  - PrestaShop **1.7.x**
  - PrestaShop **8.x**
  - PrestaShop **9.x**

## Usage

1. Add the **PrestaShop** node to your workflow.
2. Configure credentials.
3. Choose a resource and operation:
   - `Customer`, `Order`, `Product`, `Cart Rules`, `Specific Prices`
   - For triggers, select one of the available events.
4. Connect the node with other nodes in your automation.

**For ready-to-use workflow examples, [CHECK THIS FOLDER](/examples/).**

## Resources

* [PrestaShop + n8n workflow examples](/examples/)
* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [PrestaShop webservice documentation](https://devdocs.prestashop-project.org/9/webservice/)

