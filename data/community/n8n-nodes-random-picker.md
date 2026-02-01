# n8n-nodes-random-picker

This is an n8n community node that lets you randomly select items from a list in your n8n workflows.

The Random Picker node allows you to randomly select one or multiple items from an input array, with options to control the selection process and handle duplicates.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

* **Pick Random Item**: Selects a single random item from the input array
* **Pick Multiple Random Items**: Selects multiple random items from the input array
* **Shuffle Array**: Randomly shuffles the order of items in the input array

## Compatibility

This node is compatible with n8n version 1.0.0 and above.

## Usage

1. Add the Random Picker node to your workflow
2. Connect an input node that provides an array of items
3. Configure the node settings:
   - Choose the operation (Pick Random Item, Pick Multiple Random Items, or Shuffle Array)
   - For multiple items selection, specify the number of items to pick
   - Optionally enable/disable duplicate items in the selection
4. The node will output the randomly selected item(s) or shuffled array

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [n8n documentation](https://docs.n8n.io/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
