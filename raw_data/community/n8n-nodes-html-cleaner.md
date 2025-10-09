![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-html-cleaner
This is a custom n8n node that cleans HTML content by removing unwanted tags and attributes, making it easier to work with clean HTML data in your workflows.

## Features
- Remove specific HTML tags and attributes.
- Clean HTML content to ensure it is free from unwanted elements.
- Supports custom configurations for tag and attribute removal.
- Converts cleaned HTML to Markdown format.
- Easy to integrate into n8n workflows.

## Installation

```bash
npm install n8n-nodes-html-cleaner
```

## Usage
1. Add the node to your n8n workflow.
2. Configure the node by specifying the HTML content you want to clean.
3. Set the tags and attributes you want to remove.
4. Optionally, enable Markdown conversion if you want the output in Markdown format.
5. Execute the workflow to see the cleaned HTML output.

## Configuration

The HTML Cleaner node allows you to configure various options to customize the cleaning process. Here are the available configuration options:
- **HTML Content**: The HTML input that you want to clean.
- **Excluded Attributes**: A list of attributes to be removed from the HTML tags.
- **Excluded Selectors**: A list of CSS selectors to target specific elements for removal.
- **Excluded Tags**: A list of HTML tags to be removed from the content.
- **Remove Attributes**: Option to remove all attributes from the HTML content.
- **Remove Comments**: Option to remove comments from the HTML content.
- **Remove Empty Tags**: Option to remove empty tags from the HTML content.
- **Remove Scripts**: Option to remove script tags from the HTML content.
- **Remove Styles**: Option to remove style tags from the HTML content.


Readability options:
- **Char Threshold**: The number of characters an article must have in order to return a result. Defaults to 500.
- **Classes To Preserve**: A list of classes to preserve on HTML elements when the keepClasses options is set to false.
- **Disable JSON-LD**: Whether to disable JSON-LD extraction. when extracting page metadata, Readability gives precedence to Schema.org fields specified in the JSON-LD format. Set this option to true to skip JSON-LD parsing. Defaults to `false`.
- **Keep Classes**: Whether to preserve all classes on HTML elements. When set to false only classes specified in the classesToPreserve array are kept. Defaults to `false`.
- **NB Top Candidates**: The number of top candidates to consider when analysing how tight the competition is among candidates. Defaults to `5`.

Markdown: 
- **Markdown Output**: Whether to convert the cleaned HTML content to Markdown format. Defaults to `false`.

## Contributing

## References

- [cheerio](https://github.com/cheeriojs/cheerio)
- [readability](https://github.com/mozilla/readability)
- [jsdom](https://github.com/jsdom/jsdom)
- [turndown](https://github.com/mixmark-io/turndown)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
