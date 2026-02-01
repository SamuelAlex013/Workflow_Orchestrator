![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-pdf-extractor
This is a custom n8n node that extracts content from `PDF` files and converts them into various formats such as `Text` or `Markdown`. It is built using the `unpdf` library and is designed to be easily integrated into n8n workflows.

## Features

- Convert `PDF` files to `Text` or `Markdown` format.
- Support binary data input.
- Easy integration into n8n workflows.

## Installation

```bash
npm install n8n-nodes-pdf-extractor
```

## Usage
1. Add the node to your n8n workflow.
2. Connect the node to a previous node that outputs a `PDF` file, ensuring that the input data is in binary format.
3. Configure the node by selecting the desired output format (`Text`, `Markdown`, or `All`).

## Configuration
- **Output Format**: Choose the desired output format for the conversion:
	- `Text`: Converts the `PDF` file to plain text format.
	- `Markdown`: Converts the `PDF` file to Markdown format.
  - `All`: Converts the `PDF` file to all formats (`Text` and `Markdown`).

## Contributing

## References

- [pdfjs](https://github.com/mozilla/pdf.js)
- [unpdf](https://github.com/unjs/unpdf)
- [pdf-to-markdown](https://github.com/jzillmann/pdf-to-markdown)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
