# n8n-nodes-kdrive

This is an n8n community node. It lets you use kDrive API from infomaniaks in your n8n workflows.

Infomaniak is an independant cloud provider. kDrive is their cloud storage solution. kDrive makes focus on privacy and security. 15Go of storage are free.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Operations Parameters](#operations-parameters)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history) 

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

⚠️ **WARNING: This node is currently under development. Some features might be missing or incomplete. Use with caution in a production environment.**


### Profile Operations
- **Get**: Get user profile information

### Drive Operations
- **List**: Get list of accessible drives

### File Operations
- **Upload**: Upload a file to kDrive
- **Download**: Download a file from kDrive
- **Delete**: Delete a file
- **List**: List files in a folder
- **Info**: Get file information

### Folder Operations
- **Create**: Create a new folder
- **Delete**: Delete a folder

## Operation Parameters

### Common Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Drive ID | String | Yes* | ID of the drive (*required for File and Folder operations) |
| Account ID | String | Yes** | ID of the account (**required for Drive operations, can be found in profile information) |

### Profile Operations
#### Get
*No additional parameters required*

### Drive Operations
#### List
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Account ID | String | Yes | ID of the account |

### File Operations
#### Upload
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Parent Folder ID | String | Yes | ID of the parent folder (1 for root) |
| Binary Data | Boolean | Yes | Whether to take data from binary field |
| Binary Property | String | Yes* | Name of the binary property containing file data (*required if Binary Data is true) |
| File Name | String | Yes* | Name of the file to upload (*required if Binary Data is false) |

#### Download
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| File ID | String | Yes | ID of the file to download |
| File Name | String | Yes | Name of the file |

#### Delete
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| File ID | String | Yes | ID of the file to delete |

#### List
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Parent Folder ID | String | Yes | ID of the folder to list files from (1 for root) |

#### Info
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| File ID | String | Yes | ID of the file to get information about |

### Folder Operations
#### Create
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Parent Folder ID | String | Yes | ID of the parent folder |

#### Delete
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Folder ID | String | Yes | ID of the folder to delete |


## Credentials

When you have a kDrive account, you can get your credentials from the [Token list page](https://manager.infomaniak.com/v3/ng/accounts/token/list).
You need to create a token with the following permissions:
- `drive`
- `user_info`
- `user_email`

## Compatibility

Tested with n8n 1.17.3._

## Usage

Almost all operations needs a `Drive ID` and an `Account ID`.
The `Drive ID` is the ID of the drive you want to use. You can get it from the `Drive/List` operation.
The `Account ID` is the ID of the account you want to use. You can get it from the `Profile/Get` operation.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [kDrive API documentation](https://developer.infomaniak.com/getting-started)

## Version history

First release

