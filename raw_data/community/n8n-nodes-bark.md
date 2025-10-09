![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-bark

This project is about a community node for n8n, which allows notifications to be pushed to your iOS device using [Finb/bark-server](https://github.com/Finb/bark-server). 

For more information about Bark, please refer to the [Bark documentation](https://bark.day.app/#/tutorial).

> **Note: The documentation above is in Chinese.**

> If you encountered any issue, feel free to open an issue at [IcedMango/n8n-nodes-bark](https://github.com/IcedMango/n8n-nodes-bark/issues/new)



**简体中文文档**  [👉点击这里打开](https://github.com/IcedMango/n8n-nodes-bark/blob/master/README.zh-CN.md)





[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Parameters](#Parameters)  
[Resources](#resources)  
[License](#license) 


## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.


## Operations

You can send a notification to your iOS device using the `Send Notification` operation.

## Credentials

**Before you start, you should go to the Bark app on your iOS device to get the server address and the token.**


1. Open the Bark app on your iOS device.
2. Copy the server address and the token.
3. Create a new credential in n8n (Go search for `Bark Api`).
4. Enter the server address and the token in the credential.
5. Enjoy :)


## Compatibility

Dev & Test using n8n v1.67.0

## Parameters

| Parameter   | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| title       | The title of the notification.                                              |
| body        | The content of the notification.                                            |
| level       | The interruption level of the notification.                                  |
|             | - `active`: Default value, the system will immediately display the notification on the screen. |
|             | - `timeSensitive`: Time-sensitive notification, which can display notifications even in focus mode. |
|             | - `passive`: Only adds the notification to the notification list without waking the screen. |
| badge       | The badge number for the notification, which can be any number.            |
| autoCopy    | Automatically copies the notification content on iOS 14.5 and below. On iOS 14.5 and above, long-press or pull down the notification to manually copy. |
| sound       | Allows setting different ringtones for the notification.                    |
| icon        | Sets a custom icon for the notification, which will replace the default Bark icon. The icon is automatically cached on the device, and the same icon URL is only downloaded once. |
| group       | Groups messages. Notifications will be displayed in the notification center by group. You can also view different groups in the history message list. |
| isArchive   | Pass `1` to save the notification, pass anything else to not save the notification. If not provided, the decision to save is based on the app's settings. |
| url         | The URL to redirect to when the notification is clicked. Supports URL Scheme and Universal Link. |



## Resources

* [IcedMango/n8n-nodes-bark](https://github.com/IcedMango/n8n-nodes-bark)
* [Finb/bark-server](https://github.com/Finb/bark-server)

## License

Distribute under [MIT](https://github.com/IcedMango/n8n-nodes-bark/blob/master/LICENSE.md) License. 

## CLA Agreement

If you contribute code to this repository, you are implicitly allowing your code to be distributed under the MIT license. 
