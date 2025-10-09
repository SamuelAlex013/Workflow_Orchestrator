# n8n-nodes-signifycrm

This is an n8n community node. It lets you use [SignifyCRM](https://www.signifycrm.com/) in your n8n workflows.

SignifyCRM is a powerful CRM platform serving APAC businesses since 2006, helping teams automate sales pipelines, manage marketing campaigns, and streamline customer support.

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

```bash
npm install n8n-nodes-signifycrm
```

## Operations

The SignifyCRM node supports the following **resources** and **operations**:

### Account
- **create**: Create a new Account record  
- **get**: Retrieve an Account by ID  
- **getAll**: Retrieve multiple Accounts
- **update**: Update an existing Account  
- **delete**: Soft-delete an Account  

### Contact
- **create**: Create a new Contact record  
- **get**: Retrieve a Contact by ID  
- **getAll**: Retrieve multiple Contacts  
- **update**: Update an existing Contact  
- **delete**: Soft-delete a Contact  

### Lead
- **create**: Create a new Lead record  
- **get**: Retrieve a Lead by ID  
- **getAll**: Retrieve multiple Leads  
- **update**: Update an existing Lead  
- **delete**: Soft-delete a Lead  

### Opportunity
- **create**: Create a new Opportunity record  
- **get**: Retrieve an Opportunity by ID  
- **getAll**: Retrieve multiple Opportunities  
- **update**: Update an existing Opportunity  
- **delete**: Soft-delete an Opportunity  

### Case
- **create**: Create a new Case record  
- **get**: Retrieve a Case by ID  
- **getAll**: Retrieve multiple Cases  
- **update**: Update an existing Case  
- **delete**: Soft-delete a Case  

### Task
- **create**: Create a new Task record  
- **get**: Retrieve a Task by ID  
- **getAll**: Retrieve multiple Tasks  
- **update**: Update an existing Task  
- **delete**: Soft-delete a Task  

## Credentials

To connect your workflows to SignifyCRM, you must create a **SignifyCRM API** credential in n8n.

### Prerequisites
- An active SignifyCRM account (contact your administrator if you don’t have one).  
- Your SignifyCRM instance URL (e.g. `https://example.signifycrm.com`).  
- A valid **API Key** issued by your SignifyCRM administrator.  
- Your SignifyCRM **Username** and **Password**.

### Authentication Method
This node uses SignifyCRM’s REST-API login endpoint (`POST /rest_api/v1/rest/login`) to authenticate on every request. Your API key is sent in the request body along with your login credentials.

### How to set up in n8n
1. In n8n, go to **Settings → Credentials**.  
2. Click **New Credential** and choose **SignifyCRM API**.  
3. Enter the following fields:  
   - **Site URL**  
     - The full base URL of your SignifyCRM instance (e.g. `https://example.signifycrm.com`).  
   - **API Key**  
     - Your SignifyCRM API key.  
   - **Username**  
     - Your SignifyCRM username.  
   - **Password**  
     - Your SignifyCRM login password.  
4. Click **Save**.  
5. n8n will automatically send a test request to `/rest_api/v1/rest/login`. If the test succeeds, your credential is ready to use.

For more details on SignifyCRM authentication, refer to the [SignifyCRM API docs](https://support.signifycrm.net/service/api_v1/docs/).

## Compatibility

This node was developed and tested with latest stable n8n release and SignifyCRM API v1.

## Usage

If you’re new to n8n, check out the [Try it out guide](https://docs.n8n.io/try-it-out/) first.

1. **Add the node**  
   On your workflow canvas click the “+” button and search for **SignifyCRM**.

2. **Select your credential**  
   In the node’s **Credentials** dropdown, pick the **SignifyCRM API** you created.

3. **Choose a resource & operation**  
   - **Resource**: e.g. Account, Contact, Lead, Opportunity, Case, or Task  
   - **Operation**: e.g. create, get, getAll, update, delete  

4. **Fill in the parameters**  
   - Required fields will be marked in red  
   - You can expand **Additional Fields** to set any optional properties  

5. **Connect to other nodes**  
   - Use an **HTTP Request**, **Set**, or **Function** node before/after to pass data in or handle results  

6. **Execute the workflow**  
   - Click **Execute Node** (or run the whole workflow) to test  
   - Inspect the output in the node’s **Output** panel

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [SignifyCRM API v1 documentation](https://support.signifycrm.net/service/api_v1/docs/)  
* [GitHub repository & README](https://github.com/serveradmin-git/n8n-nodes-signifycrm#readme)  

## Version history

- **1.0.0**
  - Initial release  
  - Resources: Account, Contact, Lead, Opportunity, Case, Task  
  - Operations: create · get · getAll · update · delete  
  - Built and tested against n8n latest and SignifyCRM API v1

## License

This project is licensed under the [MIT License](LICENSE.md).