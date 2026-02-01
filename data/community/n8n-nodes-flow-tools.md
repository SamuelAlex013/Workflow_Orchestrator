# n8n-nodes-flow-tools

This is an n8n community node collection. It provides utility nodes for manipulating data flows in your n8n workflows.

n8n-nodes-flow-tools is a collection of nodes that help you transform and manipulate data streams within your n8n workflows, making it easier to handle complex data operations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This package includes the following nodes:

### Join Streams Node

The Join Streams node allows you to merge multiple input streams into a single output. Features include:
- Combine up to 10 different input streams
- Merges all properties from input items into a single output item
- Preserves binary data from all inputs
- Waits for all connected inputs to be executed before processing

### Lookup Node

The Lookup node enables you to search for values in a reference dataset. Features include:
- Match values between two data streams using configurable keys
- Output either the entire matched item or specific properties
- Efficient caching of lookup values for better performance
- Support for string and number type matching
- Flexible output configuration

## Compatibility

This package is compatible with n8n version 1.0.0 and above.

## Usage

### Join Streams Node

1. Add the Join Streams node to your workflow
2. Configure the number of inputs you want to merge (1-10)
3. Connect your input nodes to the Join Streams node
4. The node will combine all properties from the input items into a single output item

### Lookup Node

1. Connect your main data stream to the first input
2. Connect your reference data to the second input
3. Configure the following settings:
   - Input Search Key: The property to search for in your main data
   - Reference Input Search Key: The matching property in your reference data
   - Output Key: Where to store the lookup results
   - Choose whether to output the entire matched item or specific properties

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [n8n official website](https://n8n.io)



