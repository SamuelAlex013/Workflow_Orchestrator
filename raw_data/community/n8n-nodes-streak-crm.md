# n8n-nodes-streak-crm

This is an n8n community node that lets you use [Streak CRM](https://streak.com) in your n8n workflows.

Streak CRM is a powerful customer relationship management (CRM) tool integrated directly into Gmail that helps teams track leads, manage sales pipelines, and streamline customer communications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version History](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-streak-crm
```

Or if you use n8n Desktop, you can go to **Settings > Community nodes > Install** and provide the package name `n8n-nodes-streak-crm`.

## Operations

This node supports a comprehensive set of operations across various Streak CRM resources.

### Architecture Improvements

The node now features a dedicated `StreakApiService` class that centralizes all API interactions, providing:

- Consistent error handling across all operations
- Strong TypeScript typing for better code reliability
- Improved performance with optimized request handling
- Better developer experience for future enhancements

### User Operations
- **Get Current User** - Retrieve the details of the current authenticated user
- **Get User** - Retrieve details of a specific user by key

### Team Operations
- **Get My Teams** - Retrieve all teams the current user belongs to
- **Get Team** - Retrieve details of a specific team by key

### Pipeline Operations
- **List All Pipelines** - Get all available pipelines
- **Get Pipeline** - Retrieve a specific pipeline by key
- **Create Pipeline** - Create a new pipeline with customizable properties
- **Update Pipeline** - Update properties of an existing pipeline
- **Delete Pipeline** - Remove a pipeline
- **Move Boxes Between Pipelines** - Move multiple boxes (deals) between pipelines in batch

### Box Operations
- **List Boxes in Pipeline** - Get all boxes (deals) in a specific pipeline
- **Get Box** - Retrieve a specific box by key
- **Get Multiple Boxes** - Retrieve multiple boxes at once
- **Create Box** - Create a new box in a pipeline
- **Update Box** - Update properties of an existing box
- **Delete Box** - Remove a box
- **Get Box Timeline** - Retrieve the timeline of events for a box

### Stage Operations
- **List Stages** - Get all stages in a pipeline
- **Get Stage** - Retrieve a specific stage by key
- **Create Stage** - Create a new stage in a pipeline
- **Update Stage** - Update properties of an existing stage
- **Delete Stage** - Remove a stage from a pipeline

### Field Operations
- **List Fields** - Get all fields in a pipeline
- **Get Field** - Retrieve a specific field by key
- **Create Field** - Create a new field in a pipeline
- **Update Field** - Update properties of an existing field
- **Delete Field** - Remove a field from a pipeline
- **List Field Values** - Get all field values for a box
- **Get Field Value** - Retrieve a specific field value
- **Update Field Value** - Update a field value for a box

### Contact Operations
- **Get Contact** - Retrieve a specific contact by key
- **Create Contact** - Create a new contact
- **Update Contact** - Update properties of an existing contact
- **Delete Contact** - Remove a contact

### Organization Operations
- **Get Organization** - Retrieve a specific organization by key
- **Create Organization** - Create a new organization
- **Check Existing Organizations** - Search for existing organizations by name or domain
- **Update Organization** - Update properties of an existing organization
- **Delete Organization** - Remove an organization

### Task Operations
- **Get Task** - Retrieve a specific task by key
- **Get Tasks in Box** - Get all tasks associated with a box
- **Create Task** - Create a new task for a box
- **Update Task** - Update properties of an existing task
- **Delete Task** - Remove a task

## Credentials

To use this node, you need an API key from Streak CRM.

### How to get your API key:

1. Log in to your Streak account at [streak.com](https://streak.com)
2. Go to **Settings** > **API** 
3. Copy your API key

In n8n, create a new credential of type **Streak CRM API** and enter your API key.

## Compatibility

This node was developed and tested with n8n version 1.0.0 and Streak API v1.

## Usage

### Example: Creating a new pipeline and adding a box (deal)

This is a simple workflow to create a pipeline and then add a box to it:

1. **Streak CRM node** with operation **Create Pipeline**
   - Set name: `New Sales Pipeline`
   - Optional: Add description, team key, and other properties

2. **Streak CRM node** with operation **Create Box**
   - Use the pipeline key from the previous node
   - Set name: `Potential Client`
   - Optional: Add stage key and other properties

### Example: Managing contacts and linking them to boxes

1. **Streak CRM node** with operation **Create Contact**
   - Set email: `client@example.com`
   - Add fields for name, organization, etc.

2. **Streak CRM node** with operation **Update Box**
   - Use an existing box key
   - Link the contact by updating field values

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Streak API Documentation](https://streak.readme.io/reference/about-the-streak-api)
* [Streak User Guide](https://streak.com/support/articles)

## Version History

### 1.0.3
- Added a comprehensive StreakApiService class to centralize API interactions
- Improved pipeline selection with dynamic dropdown loading
- Fixed Box Keys field handling in Move Boxes operation
- Enhanced error handling and API request consistency
- Added TypeScript interfaces for better type safety

### 1.0.2
- Initial release with comprehensive support for Users, Teams, Pipelines, Boxes, Stages, Fields, Contacts, Organizations, and Tasks
- Support for pagination in list operations
- Detailed error handling

## License

[MIT](LICENSE.md)
