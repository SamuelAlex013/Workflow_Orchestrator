![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-straker-verify

This is an n8n community node. It lets you use the Straker Verify API in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Quick Installation

1. Open your n8n instance
2. Go to **Settings > Community Nodes**
3. Select **Install**
4. Enter `n8n-nodes-straker-verify` in **Enter npm package name**
5. Agree to the risks of using community nodes: select **I understand the risks of installing unverified code from a third party**
6. Select **Install**

## Operations

### Language Resource

* **Get Many**: Retrieve all supported languages

### File Resource

* **Get**: Download a file by ID returning binary data

### Key Resource

* **Create**: Create a new API key
* **Delete**: Delete an API key
* **Get**: Get all API keys

### Project Resource

* **Confirm**: Confirm a project
* **Create**: Create a new project
* **Get**: Get a specific project
* **Get Many**: Get all projects
* **Get Segments**: Retrieve segments of a specific project

### User Resource

* **Get Current User**: Get the currently authenticated user information

### Workflow Resource

* **Get**: Get a specific workflow
* **Get Many**: Get all available workflows

## Credentials

To use this node, you'll need to create an API key from the Straker Verify platform.

1. Log in to your Straker Verify account
2. Navigate to API Keys section
3. Create a new API key
4. Use the generated key in your n8n credentials for this node

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Straker Verify API Documentation](https://api-verify.straker.ai/docs#/)

## Example Workflow

For an example of how to use this node in a complete workflow, you can refer to the following template:

* [Simple Workflow Template](https://raw.githubusercontent.com/strakergroup/int-n8n-verify/refs/heads/master/workflows/Simple_Workflow.json)

This template demonstrates a basic flow for submitting a file for translation and retrieving the translated version.

## Binary Data Handling

This node supports proper binary data handling for files.

### File Download (File > Get)

The **File > Get** operation returns binary data that can be used directly with other n8n nodes that handle files, such as Google Drive or AWS S3. When using the output of this operation, you can refer to the binary property (by default, `data`) in the subsequent node's configuration.

### File Upload (Project > Create)

When creating a project, the node uploads files to Straker Verify. For this to work correctly:

* Each file you want to upload must be a separate n8n item.
* Each item must contain binary data under a specific property name.
* You must specify this property name in the **Binary Property** field of the **Project > Create** operation. The default is `data`.

For example, if you have two files to upload, your workflow should provide two items to the Straker Verify node. If the first item has its file in `binary.myFile` and the second in `binary.anotherFile`, you would need to process these items so that both files are under the same binary property name (e.g., `data`) before they reach the Straker Verify node. The **Set** node can be useful for this transformation.
