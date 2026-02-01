# PDF Merger Node for n8n

A custom node to merge two PDF files in your n8n workflows. Overlay the **first page** of a house-style PDF behind **all pages** of a content PDF, with fallback handling for missing or single-page PDFs.

---

## 📖 Overview

The **PDF Merger Node** allows you to:

- Overlay a "house style" PDF onto a "content" PDF by **using only the first page** of the house style as a background for all content pages.
- Always draw the **content on top** of the house style.
- Handle differences in page counts gracefully, defaulting to A4-size if no pages exist in either PDF.
- Output a single merged PDF file.

---

## 🛠️ Node Configuration

### Inputs
- **House Style PDF**: Binary property for the house style file (default: `binaryData1`).
- **Content PDF**: Binary property for the content file (default: `binaryData2`).

### Additional Options
- **Output File Name**: Name used when storing the merged PDF (default: `merged.pdf`).
- **Output Binary Property**: Binary property name where the merged PDF is saved (default: `mergedPdf`).

### Output
- **Merged PDF**: The combined PDF file as a binary property in the item.

---

## 🚀 Installation

### Step-by-Step Guide

1. **Clone the repository**:
	  ```bash
		git clone https://github.com/silverkey-it/n8n-nodes-pdf-merger.git
		```
2. **Navigate to the directory**:
	  ```bash
		cd n8n-nodes-pdf-merger
		```
3. **Install dependencies and build**:
	  ```bash
		pnpm install && pnpm run build
		```
4. **Copy the build to your n8n custom nodes folder**:
	  ```bash
		cp -r dist/ ~/.n8n/custom/
		```
5. **Restart your n8n instance**:
	  ```bash
		# If n8n is currently running, stop it first, then start.
		n8n stop && n8n start
		```
	 or just start it if it was not running:
	  ```bash
		n8n start
		```

---

## 🏗️ Example Workflow

1. **Provide two PDFs** to your workflow:
	- One as **house style** (binary property `binaryData1`).
	- One as **content** (binary property `binaryData2`).
2. **Add the PDF Merger Node** and configure the property names if needed.
3. **Execute the workflow**, and the node will produce:
	- A single merged PDF in the binary property you specify (default: `mergedPdf`).

---

## ⚙️ How It Works Under the Hood

1. **Load PDFs**: The node uses [pdf-lib](https://github.com/Hopding/pdf-lib) to load the house style and content PDFs.
2. **Embed Only the First Page of the House Style**: Even if your house style has multiple pages, **only page 1** is used as the background.
3. **Iterate Over Content Pages**: For each content PDF page, the node:
	- Creates a new page in the output PDF.
	- Draws the background (house style) **first**.
	- Draws the content page **on top**.
4. **Fallback Sizes**: If a PDF has no pages, the node defaults to an A4-ish size (`595 × 842`).

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

Happy merging! 🎉
