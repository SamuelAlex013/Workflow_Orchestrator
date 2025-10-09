# n8n-nodes-moodle

This is an n8n community node that provides comprehensive integration with [Moodle LMS](https://moodle.org/) through its Web Services API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Installation

1. In n8n, go to **Settings** > **Community Nodes**
2. Select **Install**
3. Enter `n8n-nodes-moodle`
4. Click **Install**

### Manual Installation (CLI)

```bash
npm install n8n-nodes-moodle
```

## Credentials

To use this node, you need to configure your Moodle instance to allow Web Service access:

### Setting up Moodle Web Services

1. **Enable Web Services**
   - Go to **Site administration** → **Advanced features**
   - Enable "Enable web services"
   - Save changes

2. **Enable REST Protocol**
   - Go to **Site administration** → **Server** → **Web services** → **Manage protocols**
   - Enable "REST protocol"

3. **Create a Web Service**
   - Go to **Site administration** → **Server** → **Web services** → **External services**
   - Click "Add"
   - Give it a name (e.g., "n8n Integration")
   - Enable "Enabled"
   - Enable "Authorised users only"

4. **Add Functions**
   - Click "Functions" for your service
   - Add the required functions (see list below)

5. **Create a Token**
   - Go to **Site administration** → **Server** → **Web services** → **Manage tokens**
   - Click "Create token"
   - Select your user and the service you created
   - Save the generated token

### Required Moodle Functions

Add these functions to your web service:

**User Operations:**
- `core_user_create_users`
- `core_user_get_users`
- `core_user_get_users_by_field`
- `core_user_update_users`
- `core_user_delete_users`

**Course Operations:**
- `core_course_create_courses`
- `core_course_get_courses`
- `core_course_get_courses_by_field`
- `core_course_update_courses`
- `core_course_delete_courses`
- `core_course_get_categories`

**Enrollment Operations:**
- `core_enrol_get_enrolled_users`
- `core_enrol_get_users_courses`
- `enrol_manual_enrol_users`
- `enrol_manual_unenrol_users`

**Grade Operations:**
- `gradereport_overview_get_course_grades`
- `gradereport_overview_view_grade_report`

**Message Operations:**
- `core_message_send_instant_messages`
- `core_message_get_messages`
- `core_message_get_conversations`
- `core_message_get_conversation_messages`

**System Operations:**
- `core_webservice_get_site_info`

### Configuring Credentials in n8n

1. In n8n, create new Moodle API credentials
2. Enter your Moodle URL (e.g., `https://your-moodle-site.com`)
3. Enter the Web Service token you created

## Operations

This node supports the following operations:

### Users
- **Create** - Create a new user
- **Get** - Get a user by ID
- **Get All** - Get multiple users with search options
- **Update** - Update user information
- **Delete** - Delete a user

### Courses
- **Create** - Create a new course
- **Get** - Get a course by ID
- **Get All** - Get all courses
- **Update** - Update course information
- **Delete** - Delete a course
- **Get Enrolled Users** - Get users enrolled in a course
- **Get Categories** - Get course categories

### Enrollments
- **Enroll User** - Enroll a user in a course
- **Unenroll User** - Remove a user from a course
- **Get User Courses** - Get courses a user is enrolled in
- **Get Course Users** - Get users enrolled in a course

### Grades
- **Get User Course Grades** - Get all course grades for a user
- **View Grade Report** - Mark that a user viewed their grade report

### Messages
- **Send Message** - Send a message to a user
- **Get Messages** - Get user messages (legacy)
- **Get Conversations** - Get user conversations (recommended)
- **Get Conversation Messages** - Get messages from a conversation

### System
- **Get Site Info** - Get Moodle site information

## Example Workflows

### 1. Bulk User Creation

Create multiple users from a spreadsheet:

```json
{
  "nodes": [
    {
      "name": "Spreadsheet File",
      "type": "n8n-nodes-base.spreadsheetFile",
      "position": [250, 300]
    },
    {
      "name": "Moodle",
      "type": "n8n-nodes-moodle.moodle",
      "position": [450, 300],
      "parameters": {
        "resource": "user",
        "operation": "create"
      }
    }
  ]
}
```

### 2. Course Enrollment Automation

Automatically enroll users in courses based on criteria:

```json
{
  "nodes": [
    {
      "name": "Get Users",
      "type": "n8n-nodes-moodle.moodle",
      "parameters": {
        "resource": "user",
        "operation": "getAll"
      }
    },
    {
      "name": "Filter Users",
      "type": "n8n-nodes-base.filter"
    },
    {
      "name": "Enroll in Course",
      "type": "n8n-nodes-moodle.moodle",
      "parameters": {
        "resource": "enrollment",
        "operation": "enroll"
      }
    }
  ]
}
```

## Version History

### 0.1.0
- Initial release
- Complete Moodle LMS integration
- Support for Users, Courses, Enrollments, Grades, Messages, and System operations

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Moodle Web Services documentation](https://docs.moodle.org/en/Web_services)
* [Moodle API documentation](https://docs.moodle.org/dev/Web_service_API_functions)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](https://github.com/threatroute66/n8n-nodes-moodle/blob/main/LICENSE)

## Author

**Murat Cakir**
- Email: muratc@tr66.net
- GitHub: [@threatroute66](https://github.com/threatroute66)

## Acknowledgments

This project was developed collaboratively with assistance from Claude (Anthropic's AI assistant) for:
- API integration architecture and HTTP request formatting
- Comprehensive workflow design and use case implementation
- Docker networking solutions and debugging approaches
- Moodle API parameter formatting and error handling