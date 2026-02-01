# n8n-nodes-webdav-ntml

This is an n8n community node. 
It lets you use WebDav with NTLM or Basic auth in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Local [installation](https://docs.n8n.io/integrations/creating-nodes/build/programmatic-style-node/#test-your-node)
Install N8N:
```
npm install n8n -g
```

Then in node folder:
```
npm install -g pnpm
pnpm install
pnpm run build
pnpm link --global
```

Then in n8n folder:
```
pnpm link n8n-nodes-webdav-ntml
```


Run:
```
export N8N_CUSTOM_EXTENSIONS="[path_to_folder_with_node]"
n8n
```

## Operations

Files:
- Download
- Write
- Delete

Folders:
- Get (files and subfolders list)
- Create
- Delete

## Credentials

Provide
- webdav server url
- username
- password
- domain
- ntlm option (checked by defualt)
    - if unchecked use basic auth

## Compatibility

This node created for N8N Version 1.89.2, tested on Version 1.64.3 and 1.89.2

## Usage

Operations are performed through passing the full path to a file or folder relative to the webdav root folder.
- Add node to your workflow
- Select resource
- Input path
- Provide optional data

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

## Version history

**v0.1.*** - initail version