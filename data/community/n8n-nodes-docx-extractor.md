![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-docx-extractor
This is a custom n8n node that converts `DOCX` files to `HTML`, `Text` or `Markdown` format using the [mammoth](https://github.com/mwilliamson/mammoth.js) and [turndown](https://github.com/mixmark-io/turndown) libraries.
This node is designed to be used in n8n workflows to facilitate the conversion of `DOCX` documents into more web-friendly formats like `HTML`, `Text` or `Markdown`.

## Features

- Convert `DOCX` files to `HTML`, `Text` or `Markdown` format.
- Support binary data input.
- Easy integration into n8n workflows.

## Installation

```bash
npm install n8n-nodes-docx-extractor
```

## Usage
1. Add the node to your n8n workflow.
2. Connect the node to a previous node that outputs a `DOCX` file, ensuring that the input data is in binary format.
	 - The input should be a binary file with the MIME type `application/vnd.openxmlformats-officedocument.wordprocessingml.document`.
3. Configure the node by selecting the desired output format (`HTML`, `Text`, `Markdown`, or `All`).

## Configuration
- **Output Format**: Choose the desired output format for the conversion:
	- `HTML`: Converts the `DOCX` file to HTML format.
	- `Text`: Converts the `DOCX` file to plain text format.
	- `Markdown`: Converts the `DOCX` file to Markdown format.
  - `All`: Converts the `DOCX` file to all formats (`HTML`, `Text`, and `Markdown`).

## Contributing

## References

- [mammoth](https://github.com/mwilliamson/mammoth.js)
- [turndown](https://github.com/mixmark-io/turndown)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
