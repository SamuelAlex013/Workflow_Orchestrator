# n8n-nodes-html-validation

This is an n8n community node. It lets you use HTML validation in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  


## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Validate HTML

## Credentials

The node doesn't require credentials

## Compatibility
Tested with n8n version 1.99.1

## Usage
- Input the HTML content for verification into the field labeled as `Html` - **required**
- Specify if empty string needs to be rejected using the field labeled as `Reject empty string` in the `Additional Fields` collection - optional, default: `false`
- Specify if at least one tag needs to be present in order to the validator to accept the input using the field labeled as `Require At Least One Tag` in the `Additional Fields` collection - optional, default: `false`
- Specify custom rules using the `Custom Rules` field in the 'Additional Fields' collection - optional, default:
```json
{
	"extends": [
		"html-validate:recommended"
	],
	"rules": {
		"close-order": "error",
		"void-style": "off"
	}
}
```
For example to allow self-closing tags, you can set `Custom Rules` to:
```json
{
  "extends": [
    "html-validate:recommended"
  ],

  "rules": {
    "close-order": "error",
    "no-self-closing": "off",
    "void-style": "off"
  }
}
```
Note: The `Custom Rules` field needs to be **a valid JSON** if set.
## Resources
* [html-validate rules reference](https://html-validate.org/rules/)


