# n8n-nodes-instasent

This is an n8n community node. It lets you use Instasent in your n8n workflows.

Instasent is a customer data platform that allows you to collect, manage, and analyze customer data in real-time. This integration focuses on the data ingestion capabilities, allowing you to manage contacts and track events in Instasent.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Data Source Contact Operations

* **Add/Update Contact**
  * Create a new contact or update an existing one
  * Supports dynamic contact properties based on your Instasent configuration
  * Required field: User ID

* **Delete Contact**
  * Remove a contact from your Data Source
  * Required field: User ID

### Data Source Event Operations

* **Create Event**
  * Track customer events with custom parameters
  * Required fields:
    * User ID
    * Event ID
    * Event Type
  * Optional:
    * Event Date (defaults to current timestamp)
    * Event Parameters (dynamic based on event type)

## Credentials

You need the following credentials:

* **Project ID** - Your Instasent project identifier
* **Datasource ID** - The specific Data Source identifier within your project
* **API Token** - Your Data Source API authentication token

To get them, add a n8n Data Source to your Instasent project. You can find the credentials in the Setup tab.

## Compatibility

* Requires n8n version >= 1.0.0
* Node.js >= 18.10

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Instasent API Documentation](https://docs.instasent.com/)

