![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-dfir-iris

This is an n8n community node. It allows to use the API for [IRIS](https://docs.dfir-iris.org/latest/) IRP system.

## Installation

Follow the [official guide](https://docs.n8n.io/integrations/community-nodes/installation/) for community nodes installation.

## Features

Supported IRIS Versions:

- Currenly supported the API [v2.0.4](https://docs.dfir-iris.org/latest/operations/api/#references) for IRIS v2.4.x

Supported operations:
|Endpoint|Status|
|--|--|
|Alerts|Fully supported|
|Case Assets|Fully supported|
|Case General|**Get/Update Summary, Export case**|
|Case Evidence|**Not supported yet**|
|Case IOCs|Fully supported|
|Case Modules|**Call Module, List Tasks**|
|Case Notes|Fully supported|
|Case Note Groups|Fully supported|
|Case Tasks|Fully supported|
|Case Timeline|**Not supported yet**|
|Comments|Fully supported|
|Datastore File|Fully supported|
|Datastore Folder|Fully supported|

For other endpoints there is no plans to add anything

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)


## Issues

For any kind of issues please let me know on [GitHub](https://github.com/barn4k/n8n-nodes-dfir-iris.git)
