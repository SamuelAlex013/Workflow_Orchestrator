# n8n-nodes-get-chapter-royalroad-in-epub

This project contains custom nodes for n8n to download chapters from RoyalRoad and convert them into EPUB files.

## Features

- **RoyalRoadNode**: Downloads multiple chapters from RoyalRoad and generates a combined HTML file.
- **HtmlToEpubNode**: Converts an HTML file (binary or string) into an EPUB file.

## Node Previews

### RoyalRoadNode

![RoyalRoadNode](./doc/RoyalRoadNode.png)

### HtmlToEpubNode

![HtmlToEpubNode](./doc/HtmlToEpubNode.png)

## Import Workflow

### Pre-configured Workflow

You can use the pre-configured workflow provided in this project. Simply copy the content of the [`n8n-template.json`](https://github.com/JamesDAdams/n8n-nodes-download-chapter-royalroad-in-epub/blob/master/doc/n8n-template.json) file and paste it into n8n to get a fully functional workflow.

![Workflow Preview](./doc/n8n-template.png)

This workflow includes the following steps:

1. **RSS Feed Primal Hunter**: Fetches updates from the RoyalRoad RSS feed.
2. **Send notif Discord1**: Sends a notification to Discord.
3. **RoyalRoad: Fetch Chapters**: Downloads chapters from RoyalRoad.
4. **HTML → EPUB**: Converts the downloaded HTML chapters into an EPUB file.
5. **Write Binary File**: Saves the EPUB file locally (for me on komga).

## Usage

### RoyalRoadNode

- **Description**: Downloads sequential chapters from RoyalRoad starting from a given URL.
- **Properties**:
  - `Start Chapter URL`: URL of the first chapter.
  - `Number of Chapters`: Number of chapters to download.
  - `Start Chapter Index`: Index of the starting chapter (default is 1).
  - `Output`: Output format (binary or JSON).
  - `File Name`: Name of the generated file (if binary).

### HtmlToEpubNode

- **Description**: Converts an HTML file into an EPUB file.
- **Properties**:
  - `Input Mode`: Input mode (binary or string).
  - `Title`: Title of the book.
  - `Author`: Author of the book.
  - `Language`: Language of the book.
  - `File Name`: Name of the generated EPUB file.


## Scripts

- `npm run build`: Compiles the project.
- `npm run dev`: Starts the development mode with file watching.
- `npm run format`: Formats the code using Prettier.
- `npm run lint`: Lints the code using ESLint.
- `npm run lintfix`: Automatically fixes ESLint errors.

## Dependencies

- `cheerio`: HTML parsing and manipulation.
- `typescript`: Programming language used for this project.

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or problems.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Author**: JamesDAdams

**Contact**: contact@jamestech.fr

---
