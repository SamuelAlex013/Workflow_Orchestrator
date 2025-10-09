# n8n-nodes-cigotracker

This is an n8n community node that allows you to interact with the [CigoTracker API](https://app.cigotracker.com/api/documentation) in your n8n workflows.

CigoTracker is a logistics and delivery management platform that helps businesses manage their delivery operations, routes, and field service teams.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node supports the following resources and operations:

### Jobs
- **Create** - Create a new delivery/service job
- **Get** - Retrieve a specific job by ID
- **Update** - Update job details
- **Delete** - Delete a job
- **Search** - Search for jobs by date range
- **Cancel** - Cancel a job

### Actions
- **Create** - Add actions to a job
- **Get** - Get a specific action
- **Get All** - Get all actions for a job
- **Update** - Update action details
- **Delete** - Delete an action

### Itineraries
- **Create** - Create a new route/itinerary
- **Get** - Get itinerary by ID
- **Get by Date** - Get itineraries for a specific date
- **Get by Operator** - Get itineraries assigned to an operator
- **Get by Vehicle** - Get itineraries assigned to a vehicle
- **Update** - Update itinerary details
- **Delete** - Delete an itinerary
- **Preview Route** - Preview a potential route
- **Add Job** - Add a job to an itinerary
- **Remove Job** - Remove a job from an itinerary
- **Update Job Position** - Change job order in itinerary

### Locations
- **Get** - Get a specific location
- **Get All** - Get all locations

### Vehicles
- **Get** - Get a specific vehicle
- **Get All** - Get all vehicles

### Operators
- **Get** - Get a specific operator
- **Get All** - Get all operators

## Credentials

To use this node, you need to configure CigoTracker API credentials:

1. Log in to your CigoTracker account as an administrator
2. Navigate to Integrations → API settings
3. Enable API access to obtain your API Account ID and API Auth Key
4. In n8n, create new CigoTracker credentials with:
   - Environment: Production or Sandbox
   - API Account ID
   - API Auth Key

## Usage Examples

### Create a Job

```json
{
  "resource": "job",
  "operation": "create",
  "skipStaging": true,
  "firstName": "John",
  "lastName": "Doe",
  "address": "123 Main St",
  "date": "2024-01-15",
  "additionalFields": {
    "email": "john.doe@example.com",
    "phone_number": "+1234567890",
    "time_frame": {
      "timeFrame": [{
        "start": "09:00",
        "end": "17:00"
      }]
    }
  }
}
```

### Add Action to Job

```json
{
  "resource": "action",
  "operation": "create",
  "jobId": "job_123",
  "type": "delivery",
  "additionalFields": {
    "name": "Deliver Package",
    "quantity": 1,
    "handle_time": 15
  }
}
```

### Create Itinerary

```json
{
  "resource": "itinerary",
  "operation": "create",
  "name": "Monday Route",
  "date": "2024-01-15",
  "additionalFields": {
    "vehicle_id": "vehicle_123",
    "operator_ids": "operator_1,operator_2",
    "jobs": "[\"job_123\", \"job_456\"]"
  }
}
```

## Important Notes

- Jobs created with `skip_staging: false` (default) will need to be reviewed in the CigoTracker Import Tool before they can be routed
- Date format should be YYYY-MM-DD
- Time format should be HH:MM (24-hour format)
- Coordinates should be provided as "latitude,longitude"
- The API has a 30-day limit for date range searches
- Sub-users must provide `branch_id` and `distribution_center_id` when creating jobs

## Resources

- [CigoTracker API Documentation](https://app.cigotracker.com/api/documentation)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[Apache 2.0](https://github.com/streamlinedstartup/n8n-nodes-cigotracker/blob/master/LICENSE)
