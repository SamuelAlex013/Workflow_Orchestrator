# n8n-nodes-mfr

This is an n8n community node. It lets you use mfr – Field Service Management in your n8n workflows.

mfr – Field Service Management is a cloud platform for creating, scheduling and tracking service requests, assets, appointments, technicians, reports and related documents.


[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations


- Get a Company
- Create a Company
- List Companies
- Create a Service Request
- Get a Service Request
- List Service Requests
- Delete a Service Request
- Generate Report
- Add Tags to Service Request
- Remove Tag from Service Request
- Upload Document
- Appointment
- Create an Appointment
- Create an Item Type
- Get an Item Type
- List Item Types
- Create a Service Object
- Get a Service Object
- List Service Objects
- List Users
- Watch Events Trigger – subscribe to real‑time change events from mfr

## Credentials

The basic auth method is used for the requests.

## Compatibility

1.98.0

## Usage

Add the mfr Field Service node to your workflow and choose a Resource and Operation from the dropdown. Map the required fields using n8n data‑pinning or expressions.

Example ideas:

Create a Service Request when a support ticket is opened

Trigger: Zendesk, Freshdesk, etc.

Node: Create a Company (if customer doesn’t exist)

Node: Create a Service Request

Node: Slack / Email → notify dispatcher.

Generate a PDF report nightly for completed service requests

Trigger: Cron (daily 02:00)

Node: List Service Requests (filter status = completed, updatedYesterday)

Loop: Generate Report → store in S3 / email to customer.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [mfr API Documentation and Auth](https://documenter.getpostman.com/view/3999268/TVYCAzpK#intro)


