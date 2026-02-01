# n8n-nodes-fill-docx

This is an n8n community node. It lets you fill a docx file with data using placeholders.

This node is based on [n8n-nodes-generate-report](https://github.com/bramkn/n8n-nodes-generate-report), but with several improvements:

- Updated the easy-template-x dependency to a current version
- Added support for complex objects as input to easy-template-x
- Added support for image insertion into templates
- Removed PDF generation functionality to reduce complexity

For this node, the [easy-template-x](https://www.npmjs.com/package/easy-template-x) package is used.
For more info on its usage, please check the package documentation.
The start and end tag for normal data are {{ }} instead of the standard { }
The tags for lists/containers are the same as default.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Developer

Hi,

My name is Leon Chemnitz and I am the developer of this fork.
The original node was developed by Bram (bram@knitco.nl).

For questions or issues with this node, please open an issue on Github.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

- Fill in placeholders of a DocX file with data, supporting complex objects.
- Insert images into templates using binary data references.

## Image Support

To insert images into your template, use the following format in your input data:

```json
{
	"myImage": {
		"_type": "image",
		"source": "binaryPropertyName",
		"format": "png",
		"width": 200,
		"height": 200,
		"altText": "Image Description",
		"transparencyPercent": 80
	}
}
```

Where:

- `_type`: Must be "image" to identify this as an image object
- `source`: The binary property name containing the image data
- `format`: The image format, either "png" or "jpg"
- `width`: Width of the image in pixels
- `height`: Height of the image in pixels
- `altText`: Alternative text description for the image
- `transparencyPercent`: (optional) Transparency level of the image (0-100)

Then in your template, use the placeholder `{{myImage}}` where you want the image to appear.

## Compatibility

Tested on n8n version 1.69.2 and above.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [easy-template-x documentation](https://www.npmjs.com/package/easy-template-x)

## Version history

v1.1 - Added image support

- Added ability to insert images into templates using binary data references

v1.0 - Initial release of the fork

- Updated easy-template-x dependency
- Added support for complex objects
- Removed PDF conversion functionality
