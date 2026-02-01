# n8n-nodes-twakedrive

This is an n8n community node. It lets you use Twake Drive in your n8n workflows.

[Twake Drive](https://twake-drive.com/) is an open source file sharing and storage platform focused on privacy and security. It’s built for efficient team collaboration with shared spaces, real-time editing, and seamless file organization. The Twake Drive app relies ont the [Cozy stack API](https://github.com/cozy/cozy-stack/tree/master/docs) for permissions management and files operations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

- Go to **Settings > Community Nodes**
- Click **Install a community node**
- Enter `n8n-nodes-twakedrive` in the "Enter npm package name" field
- Acknowledge the risk: check **"I understand the risks..."**
- Click **Install**

Once installed, you can find it like any other node. Just search for **"Twake Drive"** in the node panel.

Or follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

List of all available operations in this node.

### Files operations

- List files
  - List all files in the specified folder
  - Get a single file with it's binary (download is now possible)
- Upload files
  - Possibility to overwrite an already existing file
- Copy files
- Create file from text
- Delete files
- Update files
- Move files
- Rename files

### Folders operations

- Create Folder
- Delete Folder
- Move Folder
- Rename Folder

### Shares operations

- Delete Share (by Permissions ID)
  - Dynamic dropdown to select a permission ID
  - Dynamic dropdown depending on the selected ID to select a specific label(s) to revoke share link from.
- Share by Link (File or Folder)
  - With multi-label handling, expiration possibility and password protection.

_Different improvements (like dynamic lists when relevant on files and folders operations or Triggers operations) are planned for future updates._

## Credentials

This node uses an OAuth 2.0 authentication.

> **Note:**
> For now, client creation is only possible via a cURL or HTTP request. See the tutorial below.

In both cases, the first step is to create a new credential in your n8n app. Select `Twake Drive OAuth2 API` in the list.
You must do this first, because you’ll need the `OAuth Redirect URL` shown in the credential setup window.

```curl
curl -X POST "https://<INSTANCE_URL>/auth/register" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --data-raw '{
    "redirect_uris": ["<N8N_REDIRECT_URL>"],
    "client_name": "n8n Twake Drive",
    "software_id": "github.com/cozy/n8n-nodes-twakedrive",
    "client_kind": "web"
  }'
```

#### CURL method

- Replace `INSTANCE_URL` with your instance domain (e.g `https://example.mycozy.cloud` or `https://example.twake.linagora.com`)
- Replace `N8N_REDIRECT_URL` with the `OAuth Redirect URL` you copied from the credentials setup window
- Send the modified cURL request in your terminal
- Copy both the `client_id` and the `client_secret` from the response
- Paste those values into the appropriate fields in the credentials setup window
- Fill the remaining fields as shown in the examples under each field
- Connect to your instance

#### N8N node method

Doing it all in n8n is possible. Follow these steps:

- Replace `INSTANCE_URL` by your instance domain (e.g `https://example.mycozy.cloud` or `https://example.twake.linagora.com`)
- Replace `N8N_REDIRECT_URL` with the `OAuth Redirect URL` you copied from the credentials setup window
- Create a new workflow and add an `HTTP Request` node from n8n node search panel.
- Click Import cURL (currently located in the upper-right of the node panel).
- Paste the modified cURL request
- Execute the node
- Copy both the `client_id` and the `client_secret` from the response
- Paste those values into the appropriate fields in the credentials setup window
- Fill the remaining fields as shown in the examples under each field
- Connect to your instance

Ta-da 🎉, you are now connected via OAuth2.

_Client registration via the instance's settings is planned for future updates_

## Compatibility

Tested with:

- Cozy Stack v1.6.39+
- n8n v1.0+

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)

This is a community node. If you encounter issues or have feature requests, feel free to open an issue or PR on the [GitHub repository](https://github.com/cozy/n8n-nodes-twakedrive).

## Version history

### 1.3.2

- Ensure `uploadFile` operation return all input binaries

### 1.3.1

#### 🚨 Breaking changes

- `getFileFolder` return data structure has been changed. If you are using this operation in your workflow, you will need to make modifications accordingly

It was not meant to be pushed already, but this kind of changes will come in the future for every operations to harmonize returned items

- Little patch to fix the binary's return on `getFileFolder` operation

### 1.3.0

#### 🚨 Breaking changes

- Finally getting the actual OAuth2 authentication for the node

You will no longer be able to run your workflow from v1.2.0 and under, authentication method has changed, all operation have been rebuilt accordingly

- Use `requestWithAuthentication` for all operations and load-options
- Standardize outputs: each operation returns a single top-level object named after the operation
- Add Rename File operation
- Files, Folder and Share operations: refactor, more robust JSON parsing and binary handling; clearer errors
- Load-options: permissions list fetched via authenticated requests with
- Add overwrite possibility in uploadFile if file with same name already exists

### 1.2.0

- Rename `listFiles` operation to `getFileFolder` and improve it
  - Remove `listAllFiles` option as it was not revelant
  - Remake the function to use two mode only : `File` and `Folder`. `File` mode will return a single file with it's metadata and it's binary. `Folder` will return the content of the specified folder, no binaries
- Remove `getOneFile` operation, as it is now handle by `getFileFolder`
- Sanitize `instanceUrl` input from credential to avoid trailing slashes
- Only one item return by operation, for UI clarity and usage
- Little modifications such as renaming some files or actions and descriptions for clearer UI

### 1.1.1

- Transfer repo ownership to [Cozy](https://github.com/cozy/) Github organisation

### 1.1.0

- Using manual OAuth to get an app token instead of an admin token
- Folders operations (as listed above)
- Shares operations (as listed above)
- Add "byDirectory" option on `listFiles` operation
- Move `ezlog` (Little function to save an item during execution) in `/utils` folder for clarity
- Split operations in ressource categories in the n8n UI

### 1.0.0 - First release 🎉

- Connect via a locally generated token
- Files operations (as listed above)

## Useful links

- [Twake Drive website](https://twake-drive.com/)
- [Twake Drive on GitHub](https://github.com/cozy/cozy-drive)
- [Cozy Stack documentation](https://docs.cozy.io/en/cozy-stack/)
- [Cozy stack on Github](https://github.com/cozy/cozy-stack/)
- [Twake Drive node on GitHub](https://github.com/cozy/n8n-nodes-twakedrive)
