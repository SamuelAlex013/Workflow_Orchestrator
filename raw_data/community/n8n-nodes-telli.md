# n8n-nodes-telli

This is an n8n community node. It lets you use telli AI phone call platform in your n8n workflows.

telli is an AI phone calling platform that lets you automate phone call operations and perform custom tasks.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

- [Installation](#installation)  
- [Actions](#actions)  
- [Credentials](#credentials)  
- [Compatibility](#compatibility)  
- [Usage](#usage)  
- [Resources](#resources)  
- [Development](#development)  

## Repository Structure

- `credentials/`: Contains credential definitions
  - `TelliApi.credentials.ts`: Defines the API key authentication for telli API

- `nodes/`: Contains the actual node implementations
  - `Telli/`: The telli node folder
    - `Telli.node.ts`: Main implementation of the telli node with operations for adding contacts and scheduling calls
    - `telli.svg`: Icon for the node in n8n

<!-- Adding a node would mean creating a new folder in the nodes/ directory, and adding a new file with the node implementation. -->

- `dist/`: Generated folder containing compiled JavaScript code (created after running `npm run build`)

- `package.json`: Defines package dependencies and n8n node registration information

## Installation

### Option 1: Install from npm

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-telli
```

### Option 2: Manual installation

1. Clone this repository to your local machine
2. Install dependencies: `npm install`
3. Build the code: `npm run build`
4. Create a custom directory in your n8n installation: `mkdir -p ~/.n8n/custom`
5. Create a package.json file in the custom directory:
```json
{
  "name": "n8n-custom-nodes",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "n8n-nodes-telli": "file:///path/to/cloned/n8n-nodes-telli"
  }
}
```
6. Install the dependency: `cd ~/.n8n/custom && npm install`
7. Restart n8n

## Actions

The telli node provides the following operations:

### Add Contact
- Add a new contact to telli with first name, last name, email, phone number, and optional attributes
- See more info [here](https://docs.telli.com/endpoint/add-contact)

### Update Contact
- Update an existing contact in telli. Only provided fields will be updated, others remain unchanged
- Supports updating first name, last name, phone number, email, external contact ID, external URL, salutation, timezone, and contact details
- See more info [here](https://docs.telli.com/endpoint/update-contact)

### Delete Contact
- Permanently delete a contact and any PII data associated with it from the system
- This action cannot be undone. If you want to stop calling a contact, use the `v1/remove-from-auto-dialer` endpoint instead
- See more info [here](https://docs.telli.com/endpoint/delete-contact)

### Remove from Auto Dialer
- Remove a contact from the auto dialer queue
- This stops the contact from receiving automated calls without deleting their data
- See more info [here](https://docs.telli.com/endpoint/remove-from-auto-dialer)

### Schedule Call
- Schedule an AI phone call with a telli contact, with customizable message and questions
- See more info [here](https://docs.telli.com/endpoint/schedule-call)

## Credentials

To use the telli nodes, you need to authenticate with the telli API:

1. Sign up for an account at [telli.com](https://telli.com/)
2. Navigate to your account settings
3. Create an API key with the necessary permissions
4. Use this API key in the telli API credentials in n8n

## Compatibility

This node has been tested with n8n version 0.171.0 and higher.

## Usage

### Add Contact Example

1. Add the telli node to your workflow
2. Select the "Add Contact" operation
3. Fill in the required fields (First Name, Last Name, Phone Number, External Contact ID)
4. Optionally add Email, Salutation, etc.
5. Connect the node to a trigger or another node

### Update Contact Example

1. Add the telli node to your workflow
2. Select the "Update Contact" operation
3. Enter the Contact ID (obtained from a previous Add Contact operation or from telli dashboard)
4. Fill in only the fields you want to update (leave others empty to keep existing values)
5. Connect the node to a trigger or another node

### Delete Contact Example

1. Add the telli node to your workflow
2. Select the "Delete Contact" operation
3. Enter the Contact ID (obtained from a previous Add Contact operation or from telli dashboard)
4. Connect the node to a trigger or another node
5. **Warning**: This action permanently deletes the contact and cannot be undone

### Remove from Auto Dialer Example

1. Add the telli node to your workflow
2. Select the "Remove from Auto Dialer" operation
3. Enter the Contact ID (obtained from a previous Add Contact operation or from telli dashboard)
4. Connect the node to a trigger or another node
5. This will stop the contact from receiving automated calls without deleting their data

### Schedule Call Example

1. Add the telli node to your workflow  
2. Select the "Schedule Call" operation
3. Enter the Contact ID (obtained from a previous Add Contact operation or from telli dashboard)
4. Configure call details including message and questions
5. Connect to a trigger or other nodes to start the workflow

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [telli API documentation](https://docs.telli.com/)
* [telli website](https://telli.com/)

## Development

### Making Changes and Rebuilding Locally

Refer to the n8n docs on how to run nodes locally: [docs](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/)

1. Make your changes to the code (e.g., in `nodes/Telli/Telli.node.ts`)

2. Build the project:
```bash
npm run build
```

3. Copy the built files to your n8n custom directory:
```bash
cp -r dist/* ~/.n8n/custom/n8n-nodes-telli/ # or wherever your custom directory is
```

4. Restart n8n to see your changes:
```bash
# First kill the current n8n process (Ctrl+C), then run:
n8n start
```

### Development Workflow Tips

- Use `npm run dev` to continuously build the code as you make changes
- Check for linting errors with `npm run lint`
- Format code with `npm run format`

### Troubleshooting

If you don't see your changes after rebuilding and restarting n8n:

1. Check if there are any errors in the n8n logs
2. Verify that the files were correctly copied to the custom directory
3. Make sure n8n was properly restarted
4. Clear your browser cache or open n8n in an incognito window
