# n8n-nodes-mattermost-trigger

This is an n8n community trigger node. It lets you receive mattermost events.



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
pnpm link n8n-nodes-mattermost-trigger
```


Run:
```
export N8N_CUSTOM_EXTENSIONS="[path_to_folder_with_node]"
n8n
```

## Resources

- Team
- Other
- Channel
- SystemEvent
- Role
- User
- Plugin
- Post
- UserPreference
- Reaction
- Thread

## Events

- Added to team
- Authentication challenge
- Channel converted
- Channel created
- Channel deleted
- Channel member updated
- Channel updated
- Channel viewed
- Config changed
- Delete team
- Direct added
- Emoji added
- Ephemeral message
- Group added
- Hello
- Leave team
- License changed
- Memberrole updated
- New user
- Plugin disabled
- Plugin enabled
- Plugin statuses changed
- Post deleted
- Post edited
- Post unread
- Posted
- Preference changed
- Preferences changed
- Preferences deleted
- Reaction added
- Reaction removed
- Response
- Role updated
- Status change
- Typing
- Update team
- User added
- User removed
- User role updated
- User updated
- Dialog opened
- Thread updated
- Thread follow changed
- Thread read changed

## Credentials

Provide [Bot Token](https://developers.mattermost.com/integrate/reference/bot-accounts/) or [Personal access tokens](https://developers.mattermost.com/integrate/reference/personal-access-token/)

## Compatibility

This node created for N8N Version 1.89.2, tested on Version 1.64.3 and 1.89.2

## Usage

- Add trigger node to your workflow
- Set up events:
    - Standard:
        - Choose resources
        - Choose events 
    - Custom
        - Fill Custom Events in Settings tab, example:
            ```
            hello,authentication_challenge,config_changed
            ```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [mattermost event list](https://developers.mattermost.com/api-documentation/#/#websocket-events)
* [Personal access tokens](https://developers.mattermost.com/integrate/reference/personal-access-token/)

## Version history

**v0.1.0** - Initial version