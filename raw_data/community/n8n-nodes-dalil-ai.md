# n8n-nodes-dalil-ai

This is an n8n community node. It lets you use Dalil AI in your n8n workflows.

Dalil AI is a CRM platform that helps you manage your customer relationships and sales pipeline.

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

**People:**
- Create, Update, Delete, Get, Get Many

**Company:**
- Create, Update, Delete, Get, Get Many

**Opportunity:**
- Create, Update, Delete, Get, Get Many

**Task:**
- Create, Update, Delete, Get, Get Many

**Note:**
- Create, Update, Delete, Get, Get Many

**Task Target (Relations):**
- Create, Update, Delete, Get, Get Many

**Note Target (Relations):**
- Create, Update, Delete, Get, Get Many

**Pipeline:**
- Create, Update, Delete, Get, Get Many

## Credentials

You'll need to create Dalil AI API credentials. You can find these in your Dalil AI account settings.

## Compatibility

This was tested against n8n version 1.0+.

## Usage

This node allows you to interact with Dalil AI's CRM system to manage contacts, companies, opportunities, tasks, and notes.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Dalil AI](https://dalil.ai)

---

# Dalil AI n8n Node - Complete User Guide

Welcome to the comprehensive guide for using the Dalil AI n8n node. This documentation will help users of all experience levels - from beginners to advanced developers - understand and effectively use the DalilAI n8n node.

## Table of Contents

1. [Overview](#overview)
2. [Authentication Setup](#authentication-setup)
3. [Understanding Resources](#understanding-resources)
4. [Core Concepts](#core-concepts)
5. [Operations Guide](#operations-guide)
6. [Understanding Field Types and Values](#understanding-field-types-and-values)
7. [Query Parameters](#query-parameters)
8. [Triggers and Webhooks](#triggers-and-webhooks)
9. [Advanced Features](#advanced-features)
10. [Troubleshooting](#troubleshooting)

## Overview

The Dalil AI n8n node allows you to seamlessly integrate with the Dalil AI CRM system, enabling automation of customer relationship management tasks. The node supports comprehensive CRUD (Create, Read, Update, Delete) operations across multiple resources and provides real-time webhook notifications for data changes.

### Supported Resources
- **People**: Individual contacts and customers
- **Company**: Organizations and businesses
- **Opportunity**: Sales deals and prospects
- **Task**: To-do items and assignments
- **Note**: Documentation and comments
- **Task Relations**: Link tasks to multiple records
- **Note Relations**: Link notes to multiple records
- **Pipeline**: Workflow stages and processes

## Authentication Setup

Before using the Dalil AI node, you need to configure your API credentials:

1. **Create Credentials**: In your n8n instance, go to Settings > Credentials
2. **Add New Credential**: Select "Dalil AI API"
3. **Configure**:
   - **API Key**: Your authentication token from Dalil AI settings

## Understanding Resources

### Core Resources

#### People
Represents individual contacts in your CRM.
- **Use Case**: Store customer information, contacts, leads
- **Key Fields**: First Name, Last Name, Email, Phone, Company ID
- **Relationships**: Belongs to Company, has Tasks/Notes

#### Company  
Represents businesses and organizations.
- **Use Case**: Manage client companies, prospects, vendors
- **Key Fields**: Name, Domain URL, Industry, Employees, Address
- **Relationships**: Has People, Opportunities, Tasks/Notes

#### Opportunity
Represents sales deals and revenue opportunities.
- **Use Case**: Track sales pipeline, deals, revenue forecasts
- **Key Fields**: Name, Amount, Stage, Close Date, Company ID
- **Relationships**: Belongs to Company and people, has Tasks/Notes

#### Task
Represents actionable items and assignments.
- **Use Case**: Track work items, follow-ups, assignments
- **Key Fields**: Title, Body, Status, Due Date, Assignee ID
- **Relationships**: Can be linked to any record via Task Relations

#### Note
Represents documentation and comments.
- **Use Case**: Store meeting notes, customer interactions, documentation
- **Key Fields**: Title, Body, Visibility Level
- **Relationships**: Can be linked to any record via Note Relations

### Relationship Resources

#### Task Relations (taskTarget)
Creates many-to-many relationships between tasks and other records.
- **Purpose**: One task can be related to multiple People, Companies, or Opportunities
- **Use Case**: Project tasks affecting multiple contacts or deals
- **Key Fields**: Task ID, Person ID, Company ID, Opportunity ID

#### Note Relations (noteTarget)  
Creates many-to-many relationships between notes and other records.
- **Purpose**: One note can be related to multiple People, Companies, or Opportunities
- **Use Case**: Meeting notes involving multiple participants or deals
- **Key Fields**: Note ID, Person ID, Company ID, Opportunity ID

#### Pipeline
Defines workflow stages and custom processes.
- **Purpose**: Create custom workflows beyond standard opportunity stages
- **Use Case**: Support tickets, hiring processes, custom workflows
- **Key Fields**: Name, Status, Custom Fields

## Core Concepts

### Operations
Each resource supports standard CRUD operations:

- **Create**: Add new records
- **Get**: Retrieve a single record by ID
- **Get Many**: Retrieve multiple records with filtering
- **Update**: Modify existing records
- **Delete**: Remove records

### Field Types
Understanding field types is crucial for proper data entry:

#### Standard Field Types
- **TEXT**: Plain text strings (e.g., "John Smith")
- **NUMBER**: Numeric values (e.g., 100, 3.14)
- **BOOLEAN**: True/false values
- **DATE_TIME**: ISO 8601 format dates (e.g., "2024-01-15T10:30:00Z")
- **SELECT**: Single choice from predefined options
- **MULTI_SELECT**: Multiple choices from predefined options
- **RATING**: Scale of 1-5 (represented as "RATING_1" through "RATING_5")

#### Complex Field Types
- **EMAILS**: Email addresses with primary and additional emails
- **PHONES**: Phone numbers with country codes and calling codes
- **LINKS**: URLs with labels and secondary links
- **ADDRESS**: Complete address information
- **FULL_NAME**: First and last name components
- **MONEY**: Amount with currency code (stored in micros)

### Select Values Format
**IMPORTANT**: Select field values must be in uppercase with underscores, not the display labels.

**Frontend Display** → **API Value Required**
- "Lead" → "LEAD"
- "New Customer" → "NEW_CUSTOMER"  
- "In Progress" → "IN_PROGRESS"
- "On Site" → "ON_SITE"
- "Remote Work" → "REMOTE_WORK"

**Example for Opportunity Stage:**
- Display: "Discovery" → Value: "DISCOVERY"
- Display: "Proposal" → Value: "PROPOSAL"
- Display: "Negotiation" → Value: "NEGOTIATION"

## Operations Guide

### Creating Records

#### People - Create
**Required Fields:**
- First Name

**Example:**
```javascript
{
  "firstName": "John",
  "additionalFields": {
    "lastName": "Smith",
    "primaryEmail": "john.smith@company.com",
    "jobTitle": "Software Engineer",
    "companyId": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

#### Company - Create
**Required Fields:**
- Company Name

**Example:**
```javascript
{
  "name": "Acme Corp",
  "additionalFields": {
    "domainUrl": "https://acmecorp.com",
    "industry": "Technology",
    "employees": 50,
    "addressStreet1": "123 Main St",
    "addressCity": "San Francisco",
    "addressState": "CA",
    "addressCountry": "United States"
  }
}
```

#### Opportunity - Create
**Required Fields:**
- Name

**Example:**
```javascript
{
  "name": "Q1 Software License Deal",
  "additionalFields": {
    "amount": 50000,
    "currencyCode": "USD",
    "stage": "DISCOVERY",
    "closeDate": "2024-03-31",
    "companyId": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

#### Task - Create
**Required Fields:**
- Title

**Example:**
```javascript
{
  "title": "Follow up with client",
  "additionalFields": {
    "body": "Call to discuss proposal feedback",
    "status": "TODO",
    "dueAt": "2024-01-20T15:00:00Z",
    "assigneeId": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

#### Note - Create
**Required Fields:**
- Title

**Example:**
```javascript
{
  "title": "Client Meeting Notes",
  "additionalFields": {
    "body": "Discussed project requirements and timeline",
    "visibilityLevel": 1
  }
}
```

### Creating Relationships

#### Task Relations (taskTarget) - Create
Links a task to multiple records.

**⚠️ Important Constraint: Single Relation Per Record**
Each taskTarget record can only link to **ONE** relation ID at a time. You cannot add both `personId` and `companyId` in the same taskTarget record.

**❌ Incorrect - Multiple Relations in One Record:**
```javascript
{
  "taskId": "task-uuid-here",
  "personId": "person-uuid-here",      // ❌ Cannot combine
  "companyId": "company-uuid-here"     // ❌ Cannot combine
}
```

**✅ Correct - Separate Records for Each Relation:**

**First Record (Person Relation):**
```javascript
{
  "taskId": "task-uuid-here",
  "personId": "person-uuid-here"
}
```

**Second Record (Company Relation):**
```javascript
{
  "taskId": "task-uuid-here",
  "companyId": "company-uuid-here"
}
```

**Third Record (Opportunity Relation):**
```javascript
{
  "taskId": "task-uuid-here",
  "opportunityId": "opportunity-uuid-here"
}
```

#### Note Relations (noteTarget) - Create
Links a note to multiple records.

**⚠️ Important Constraint: Single Relation Per Record**
Each noteTarget record can only link to **ONE** relation ID at a time. You cannot add both `personId` and `companyId` in the same noteTarget record.

**❌ Incorrect - Multiple Relations in One Record:**
```javascript
{
  "noteId": "note-uuid-here",
  "personId": "person-uuid-here",      // ❌ Cannot combine
  "companyId": "company-uuid-here"     // ❌ Cannot combine
}
```

**✅ Correct - Separate Records for Each Relation:**

**First Record (Person Relation):**
```javascript
{
  "noteId": "note-uuid-here",
  "personId": "person-uuid-here"
}
```

**Second Record (Company Relation):**
```javascript
{
  "noteId": "note-uuid-here",
  "companyId": "company-uuid-here"
}
```

**Workflow Example:**
To link a single note to both a person and a company, create two separate n8n node executions:

1. **First Node Execution:**
   - Operation: Create noteTarget
   - noteId: "your-note-uuid"
   - personId: "your-person-uuid"

2. **Second Node Execution:**
   - Operation: Create noteTarget  
   - noteId: "your-note-uuid"
   - companyId: "your-company-uuid"


### Updating Records

Updates require the record ID and any fields you want to modify:

**Example - Update Person:**
```javascript
{
  "personId": "123e4567-e89b-12d3-a456-426614174000",
  "updateFields": {
    "jobTitle": "Senior Software Engineer",
    "primaryEmail": "john.smith.senior@company.com"
  }
}
```

### Getting Records

#### Get Single Record
Requires only the record ID:
- **Person ID**: UUID of the person to retrieve
- **Depth**: Level of related data to include (0, 1, or 2)

#### Get Many Records
Supports filtering, sorting, and pagination:
- **Return All**: Whether to fetch all results or limit
- **Limit**: Maximum records to return (1-60)
- **Filter**: Conditions to filter results
- **Order By**: Sorting criteria
- **Depth**: Level of related data to include

## Understanding Field Types and Values

### Custom Properties
Each resource can have custom fields specific to your workspace. The node dynamically loads available custom properties and shows the expected format.

**Custom Property Types:**
- **Text Fields**: Accept plain strings
- **Select Fields**: Accept predefined values (use API format, not display labels)
- **Multi-Select Fields**: Accept arrays of predefined values
- **Date Fields**: Accept ISO 8601 formatted dates
- **Boolean Fields**: Accept true/false
- **Rating Fields**: Accept "RATING_1" through "RATING_5"


## Query Parameters

### Filtering
Filter results using field conditions with comparators:

**Format:** `field[comparator]:value,field2[comparator]:value2`

**Available Comparators:**
- `eq`: Equal to
- `neq`: Not equal to  
- `gt`: Greater than
- `gte`: Greater than or equal
- `lt`: Less than
- `lte`: Less than or equal
- `in`: In list (comma-separated values)
- `startsWith`: Starts with text
- `like`: Contains text (case-sensitive)
- `ilike`: Contains text (case-insensitive)
- `is`: For NULL/NOT_NULL values
- `containsAny`: For array fields

**Simple Field Examples:**
```
score[gt]:5
employees[gte]:50
stage[in]:[DISCOVERY,PROPOSAL]
createdAt[gte]:2024-01-01
city[is]:NOT_NULL
```

**Nested Field Examples:**
For composite fields, use dot notation to access subfields:

**People/Person Fields:**
```
name.firstName[eq]:John
name.lastName[eq]:Smith
emails.primaryEmail[like]:@company.com
emails.primaryEmail[is]:NOT_NULL
phones.primaryPhoneNumber[startsWith]:+1
phones.primaryPhoneCountryCode[eq]:US
linkedinLink.primaryLinkUrl[like]:linkedin.com
whatsapp.primaryPhoneNumber[startsWith]:+1
```

**Company Fields:**
```
name[eq]:Acme Corp
domainName.primaryLinkUrl[eq]:acme.com
address.addressCity[eq]:New York
address.addressCountry[eq]:USA
annualRecurringRevenue.amountMicros[gt]:1000000
linkedinLink.primaryLinkUrl[like]:linkedin.com
```

**Opportunity Fields:**
```
name[eq]:Big Deal
amount.amountMicros[gt]:500000
amount.currencyCode[eq]:USD
```

**Complex Filters with Conjunctions:**
Use `and`, `or`, `not` to combine conditions:
```
and(name.firstName[eq]:John,name.lastName[eq]:Smith)
or(emails.primaryEmail[like]:@company.com,phones.primaryPhoneNumber[startsWith]:+1)
not(emails.primaryEmail[is]:NULL)
and(score[gt]:5,or(name.firstName[eq]:John,name.firstName[eq]:Jane))
```

### Sorting (Order By)
Sort results by one or more fields:

**Format:** `field1,field2[DIRECTION]`

**Available Directions:**
- `AscNullsFirst`: Ascending, nulls first (default)
- `AscNullsLast`: Ascending, nulls last
- `DescNullsFirst`: Descending, nulls first  
- `DescNullsLast`: Descending, nulls last

**Simple Field Examples:**
```
createdAt[DescNullsLast]
score[DescNullsFirst]
position[AscNullsLast]
```

**Nested Field Examples:**
For composite fields, use dot notation to access subfields:

**People/Person Sorting:**
```
name.firstName[AscNullsFirst]
name.lastName[DescNullsLast]
emails.primaryEmail[AscNullsLast]
phones.primaryPhoneNumber[DescNullsFirst]
```

**Company Sorting:**
```
name[AscNullsFirst]
domainName.primaryLinkUrl[AscNullsLast]
address.addressCity[DescNullsFirst]
annualRecurringRevenue.amountMicros[DescNullsLast]
```

**Multiple Field Sorting:**
```
name.firstName,name.lastName[DescNullsFirst]
score[DescNullsLast],name.firstName[AscNullsLast]
createdAt[DescNullsFirst],name.firstName[AscNullsFirst]
```

### Depth Levels
Control how much related data to include:

- **Depth 0**: Only the primary object
- **Depth 1**: Primary object + direct relationships (default)
- **Depth 2**: Primary object + relationships + their relationships

**Example:**
- Depth 0: Just the person record
- Depth 1: Person + their company info
- Depth 2: Person + company + company's opportunities

## Triggers and Webhooks

The Dalil AI Trigger node allows you to react to real-time changes in your Dalil AI workspace.

### Setting Up Triggers

1. **Add Trigger Node**: Drag "Dalil AI Trigger" to your workflow
2. **Configure Entity**: Choose which resource to monitor (Company, People, Opportunity, Task)
3. **Configure Action**: Choose which events to listen for (Create, Update, Delete, All)
4. **Save and Activate**: The webhook will be automatically registered

### Trigger Configuration

**Entity Options:**
- **Company**: Monitor company record changes
- **People**: Monitor person record changes  
- **Opportunity**: Monitor opportunity changes
- **Task**: Monitor task changes

**Action Options:**
- **All (*)**: Any change to the entity
- **Create**: New records created
- **Update**: Existing records modified
- **Delete**: Records removed

### Webhook Response Structure

When a trigger fires, you receive a structured webhook payload:

```javascript
[
  {
    "targetUrl": "https://your-n8n-instance.com/webhook/...",
    "eventName": "company.updated",
    "objectMetadata": {
      "id": "8913832e-825b-4374-a527-f9e3524ef3a9",
      "nameSingular": "company"
    },
    "workspaceId": "20202020-1c25-4d02-bf25-6aeccf7ea419",
    "webhookId": "85124f96-2698-4368-8805-c2755070c1c1",
    "eventDate": "2025-06-26T04:51:21.005Z",
    "record": {
      // Complete record data with all fields
      "id": "2f51e0c3-6ed4-4ec7-8ecf-05f0282154fe",
      "name": "Acme Corp",
      "industry": "Technology",
      // ... all other fields
    },
    "updatedFields": [
      "address",
      "industry"
    ]
  }
]
```

### Key Webhook Fields

#### eventName
Identifies the specific event that occurred:
- Format: `{entity}.{action}`
- Examples: `company.created`, `people.updated`, `opportunity.deleted`
- **Use Case**: Filter webhook processing based on event type

#### updatedFields  
Array of field names that were changed (only for update events):
- **Use Case**: Process only specific field changes, ignore others
- **Example**: Only send email notifications when contact info changes

#### record
Complete record data after the change:
- **Create Events**: The newly created record
- **Update Events**: Record with latest values  
- **Delete Events**: The record before deletion

#### eventDate
ISO timestamp of when the event occurred:
- **Use Case**: Order events, detect delayed processing

### Using Webhook Data

**Example - Process Only Email Changes:**
```javascript
// In your workflow's JavaScript code
if (items[0].json.eventName === 'people.updated' && 
    items[0].json.updatedFields.includes('primaryEmail')) {
  // Send notification about email change
  return items;
} else {
  // Skip processing
  return [];
}
```

**Example - Route by Event Type:**
```javascript
const eventName = items[0].json.eventName;
const [entity, action] = eventName.split('.');

if (entity === 'company' && action === 'created') {
  // Handle new company
} else if (entity === 'opportunity' && action === 'updated') {
  // Handle opportunity changes
}
```

## Troubleshooting

### Common Issues

#### Authentication Errors
- **Symptom**: "Unauthorized" or credential errors
- **Solution**: Verify API key

#### Field Value Errors  
- **Symptom**: "Invalid value" errors for select fields
- **Solution**: Use API format values, not display labels
- **Example**: Use "IN_PROGRESS" not "In Progress"

#### Date Format Errors
- **Symptom**: Date validation failures  
- **Solution**: Use ISO 8601 format: "2024-01-15T10:30:00Z"
- **Tools**: Use JavaScript `new Date().toISOString()`

#### Relationship Errors
- **Symptom**: "Record not found" when creating relations
- **Solution**: Ensure referenced IDs exist and are valid UUIDs
- **Check**: Verify record existence before creating relations

#### Filter Syntax Errors
- **Symptom**: No results or filter errors
- **Solution**: Check comparator syntax and field names
- **Example**: `name[eq]:value` not `name=value`


---

This guide provides comprehensive coverage of the Dalil AI n8n node. For specific use cases or advanced configurations, refer to the API documentation or reach out to the support team.
