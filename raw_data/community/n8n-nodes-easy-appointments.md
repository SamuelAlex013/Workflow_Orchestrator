# n8n-nodes-easy-appointments

![Thumbnail](https://raw.githubusercontent.com/jannikhst/n8n-nodes-easy-appointments/main/screenshot-2025-08-08-000276.png)

This package contains n8n nodes to interact with the [Easy!Appointments](https://easyappointments.org/) API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Easy!Appointments](https://easyappointments.org/) is a highly customizable web application that allows customers to book appointments with you via a sophisticated web interface.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-easy-appointments
```

## Nodes

### Easy!Appointments

This node allows you to interact with the Easy!Appointments API. It provides access to all resources in a single node.

**Resources:**
- **Appointment**: Manage appointments
- **Availability**: Check provider availability
- **Customer**: Manage customer records
- **Service**: Manage service offerings

**Operations:**
- **Appointment, Customer, Service**:
  - Create
  - Delete
  - Get
  - Get All
  - Update
- **Availability**:
  - Get

### Easy!Appointments Trigger

This trigger node allows you to listen for webhook events from Easy!Appointments.

**Events:**
- Appointment Created/Updated/Deleted
- Customer Created/Updated/Deleted
- Service Created/Updated/Deleted
- Provider Created/Updated/Deleted

The node automatically registers a webhook with Easy!Appointments when activated and removes it when deactivated.

## Credentials

### Easy!Appointments API

To use these nodes, you need to authenticate with the Easy!Appointments API. The following authentication methods are supported:

- **Bearer Token**: Generate an API key from the Easy!Appointments settings page.
- **Basic Auth**: Use the credentials of an admin user.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Easy!Appointments API documentation](https://easyappointments.org/docs.html)

## License

[MIT](LICENSE.md)

## Local Development and Testing

To test this node package locally:

1. Build the package:
   ```bash
   pnpm build
   ```

2. Create a symbolic link to your n8n custom extensions directory:
   ```bash
   mkdir -p ~/.n8n/custom
   ln -s "$(pwd)" ~/.n8n/custom/n8n-nodes-easy-appointments
   ```

3. Start n8n with custom extensions:
   ```bash
   export N8N_CUSTOM_EXTENSIONS=~/.n8n/custom
   n8n start
   ```

   Alternatively, use the provided script:
   ```bash
   ./start-n8n-with-custom-nodes.sh
   ```

4. Open n8n in your browser (usually at http://localhost:5678)

5. Create a new workflow and search for "Easy!Appointments" in the nodes panel

6. Set up the Easy!Appointments API credentials and start using the nodes

When you make changes to the code:

1. Rebuild the package:
   ```bash
   pnpm build
   ```

2. Restart n8n to load the updated nodes
