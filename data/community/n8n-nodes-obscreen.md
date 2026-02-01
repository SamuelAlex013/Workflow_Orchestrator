![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-obscreen

This is an n8n community node. It lets you use Obscreen API in your n8n workflows.

Obscreen is a cloud-based/self-hosted digital signage platform that allows you to manage your digital signage content and playlists.

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

## Operations

> Content
- List all contents
- Add new content
- Update existing content
- Delete content
- Get content
- Get content location
- Get available content types

> Content Folder
- List all content folders
- Add new content folder
- Update a folder
- Delete a folder
- Move multiple contents to a folder

> Playlist
- List all playlists
- Add a playlist
- Update existing playlist
- Delete playlist
- Get playlist
- Get regular slides associated with playlist
- Get notifications slides associated with playlist

> Slide
- List all slides
- Add a regular slide
- Add a notification slide
- Update existing slide
- Delete slide
- Get slide

> Process
- Refresh player

## Credentials

To use this node, you need to authenticate with your Obscreen Instance. You will need:

1. An Obscreen Instance with the Core API plugin enabled (Premium feature)
1. Your Obscreen Instance URL
2. Your Obscreen API Key (you can get it from any user's security settings)

**Optional Security Note**: You can configure your instance to permit unauthenticated access to the API. If you do so, you can set a random value as the API Key.

## Compatibility

This node is compatible with n8n version 0.150.0 and above. It has been tested with the latest version of n8n.

## Usage

This node allows you to manage your Obscreen Instance using the Core API plugin. You can create, update, delete, get, get many, get types, get location contents, content folders, playlists, slides, and processes.

## Development

To develop this node, you can use the following commands:

```bash
npm install
npm link
npm run dev
```
In a separate terminal, run the following command to start the n8n server:

Locate the n8n directory and run the following 
( Note: to locate the .n8n directory - when starting the server `n8n start` look for the message: "User settings loaded from: ..." ) 

command:
```bash
cd .n8n
# ensure the custom folder is in the .n8n directory with npm initialised
mkdir custom    
cd custom 
npm init
npm link @n8n-nodes-obscreen
npm start
```


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Obscreen documentation](https://docs.obscreen.io/)

## Version history

### 1.0.0
- Initial release of the Obscreen node.
