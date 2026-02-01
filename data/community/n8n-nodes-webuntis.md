# n8n-nodes-WebUntis

This is an n8n community node. It lets you use WebUntis in your n8n workflows.

WebUntis is a popular service for school timetables and schedule management used by educational institutions worldwide.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

To install this community node, use the following package name:
```
n8n-nodes-webuntis
```

## Operations

The WebUntis node supports the following operations:

### Timetable
- **Get Week**: Retrieve timetable data for a specific week
- **Get Timeframe**: Retrieve timetable data for multiple weeks (with configurable lookback period)

### Teachers
- **Get All**: Retrieve a list of all teachers with their IDs and names

### Rooms
- **Get All**: Retrieve a list of all rooms with their IDs, names, and long names

### Subjects
- **Get All**: Retrieve a list of all subjects with their IDs, names, and long names

## Credentials

To use this node, you need to create WebUntis API credentials in n8n with the following information:

### Prerequisites
- You must have a valid WebUntis account with access to your school's timetable system
- Your account must have appropriate permissions to access timetable data

### Setting up credentials
1. In n8n, go to **Credentials** and create a new **WebUntis API** credential
2. Enter your WebUntis login credentials:
   - **Username**: Your WebUntis username
   - **Password**: Your WebUntis password

### Important Notes
- The node is currently configured for the "st-bernhard-gym" school. For other schools, you may need to modify the school parameter in the code
- Credentials are securely stored and encrypted by n8n

## Compatibility

- **Minimum n8n version**: 0.198.0
- **Tested with n8n versions**: 0.198.0+
- **Node.js compatibility**: Node.js 16+

### Known Limitations
- Currently hardcoded for "st-bernhard-gym" school - customization needed for other schools
- Requires WebUntis server to support the specific API endpoints used
- Some WebUntis installations may have different API structures

## Usage

### Basic Timetable Retrieval
1. Add the WebUntis node to your workflow
2. Select **Timetable** as the resource
3. Choose **Get Week** operation
4. Set the date parameter (leave empty for current week)
5. Configure your WebUntis credentials

### Getting Multiple Weeks
1. Select **Timetable** resource and **Get Timeframe** operation
2. Set the **Look Back Weeks** parameter to specify how many weeks to retrieve
3. The node will return combined data from multiple weeks

### Teacher/Room/Subject Information
1. Select the appropriate resource (Teachers, Rooms, or Subjects)
2. The operation will automatically be set to **Get All**
3. The node will return all available items of the selected type

### Advanced Options
- **User ID**: Leave empty to use the authenticated user's timetable, or specify a different user ID
- **Date**: Use YYYY-MM-DD format or n8n's date picker

### Output Data Structure

**Timetable data includes:**
- Lesson details (start time, end time, date)
- Teacher information (including substitution teachers)
- Subject and room assignments
- Special flags (substitution, cancellation, free periods, etc.)

**Teachers/Rooms/Subjects include:**
- ID numbers for API references
- Display names
- Long names (where applicable)

### Error Handling
The node handles common errors such as:
- Authentication failures (403 errors)
- No data available (204 errors)
- Network connectivity issues

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [WebUntis Official Website](https://webuntis.com/)
- [WebUntis API Documentation](https://help.untis.at/hc/en-us/articles/360016560358-WebUntis-API-documentation)
- [n8n workflow automation platform](https://n8n.io/)

## Version history

### 1.0.0
- Initial release
- Support for timetable retrieval (single week and multiple weeks)
- Support for teachers, rooms, and subjects data
- Authentication via WebUntis credentials
- Error handling for common API issues
- Compatible with n8n 0.198.0+

### Known Issues
- School parameter is currently hardcoded - future versions will support multiple schools
- Limited to specific WebUntis server configurations
- Some advanced WebUntis features not yet supported

### Planned Features
- Multi-school support with configurable school parameters
- Support for additional WebUntis data types (classes, holidays, etc.)
- Enhanced filtering and search capabilities
- Caching support for improved performance