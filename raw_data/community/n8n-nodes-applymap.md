# n8n-nodes-applymap

This is an n8n community node. It lets you easily map data. For example an Id to a string value.
Normally this would be done by using a merge or function/code node. This community node makes it a lot simpler.

If you find any issues with the node please open an issue on Github.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Developer

Hi, 

My name is Bram and I am the developer of this node.
I am an independant consultant and expert partner of n8n.
My nodes are free to use for everyone, but please consider [donating](https://donate.stripe.com/3cs5oe7xM6L77Yc5ko) when you use my nodes.
This helps me to build and maintain nodes for everyone to use.

If you are looking for some outside help with n8n, I can of course also offer my services.
* Node Development
* Workflow Development
* Mentoring
* Support

Please contact me @ bram@knitco.nl if you want to make use of my services.

For questions or issues with nodes, please open an issue on Github.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

You can map data and also provide a default value for when there was no value found in the mapping table.
The first input is the data going through your n8n workflow. 
The second input is the mapping table.
This table consists of 3 fields:
* mapName
* input
* output

The mapName is used in the parameters of the mapping, this makes it so you can have multiple mappings done in one go.
For this it is important that every map has its unique name.

The input is the input value so for example an Id, to be mapped.

The output is the output value that has to replace the input value when it is found.

Each map is made by converting to string and then matching the values. This should make it easier to apply the maps in most cases. If there are any troubles with this please open an issue in github.

![mappingTable](https://github.com/bramkn/n8n-nodes-applymap/blob/master/images/mappingTable.png)

Keep in mind that this mapping table needs to be formatted exactly like this for it to work.

You can configure the node to do what you need it to do. An example is provided below.

![example](https://github.com/bramkn/n8n-nodes-applymap/blob/master/images/exampleConfig.png)

Keep in mind that you do not use expressions for setting these values unless you have a specific reason to do so.
Also keep in mind to use the correct Capitalization. 

## Compatibility

This node was developed and tested with n8n version 0.195.5


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [n8n ApplyMap](https://github.com/bramkn/n8n-nodes-applymap.git)

## Version history

Only 1 version
