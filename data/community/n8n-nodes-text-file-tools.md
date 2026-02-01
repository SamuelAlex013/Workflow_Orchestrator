# n8n-nodes-text-file-tools

This is an n8n community node. It lets you use Text File Tools in your n8n workflows.

Text File Tools is a module designed to process text-based files, offering functionalities like removing the UTF-8 Byte Order Mark (BOM), converting line endings, and skipping lines. It integrates seamlessly with n8n workflows to enhance text file processing capabilities.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Remove UTF-8 BOM from text files
- Convert line endings between LF and CRLF
- Skip specified number of lines from the start of text files

## Credentials

_No authentication is required for this node._

## Compatibility

This node is compatible with n8n version 0.150.0 and above. It has been tested with the latest versions of n8n.

## Usage

_This node is straightforward to use for users familiar with n8n. For new users, refer to the [Try it out](https://docs.n8n.io/try-it-out/) documentation to get started._

## TextFileTools Module

The `TextFileTools` module is designed to process text-based files with functionalities such as removing the UTF-8 Byte Order Mark (BOM), converting line endings, and skipping lines. This module is part of the n8n workflow automation tool and provides the following features:

### Properties

- **Binary Property Name**: The name of the binary property containing the text file. Default is 'data'.
- **Strip UTF-8 BOM**: A boolean option to remove the UTF-8 BOM if present.
- **Convert Line Endings**: A boolean option to enable conversion of line endings between LF and CRLF.
- **Line Ending Conversion**: Options to convert line endings from LF to CRLF or vice versa.
- **Skip First N Lines**: A boolean option to enable skipping the first N lines of the text file.
- **Number of Lines to Skip**: Specifies how many lines to skip from the start of the file.

### Execution Logic

The `TextFileTools` node processes each input item by:
1. Checking if the specified binary data exists.
2. Optionally removing the UTF-8 BOM.
3. Converting line endings if enabled.
4. Skipping the first N lines if enabled.
5. Converting the processed content back to binary format.

This node is useful for preparing text files for further processing in workflows, ensuring consistent file formats and contents.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)


## License

MIT. See [LICENSE](LICENSE.md) for more details.
