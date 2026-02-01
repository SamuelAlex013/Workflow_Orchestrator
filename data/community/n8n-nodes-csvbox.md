![CSVBox for n8n](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-csvbox
## Overview

This is an n8n community node. It lets you use [CSVBox](https://csvbox.io/) in your n8n workflows.

CSVBox is a platform for importing CSV data into your applications with ease. This node allows you to trigger n8n workflows when new rows are imported into a CSVBox Importer.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

---

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)
- [License](#license)

---

## Installation

You can install this node as a community package in your n8n instance.

### Steps

1. Go to **Settings → Community Nodes** in your n8n instance.
2. Click **Install a community node** and enter:
   ```
   n8n-nodes-csvbox
   ```
3. Check the warning button.
4. Click on the **Install** and wait for the installation to complete.
4. Restart n8n if prompted.

After installation, you’ll find the **CSVBox Trigger** node available in your n8n workflow editor.

---

## Operations

This package provides the following node:

- **CSVBox Trigger**: Starts a workflow when a new row is imported to a CSVBox Sheet.

---

## Credentials

Create an API Key and Secret Key from the CSVBox API Key Page, then add them as a credential in n8n using the following fields:

- **API Key:** Your CSVBox API Key.
- **API Secret Key:** Your CSVBox Secret Key.

---

## Compatibility

- **Minimum n8n version:** 1.x
- **Node.js version:** >= 20.15
- Tested on latest n8n and Node.js LTS.

---

## Usage

1. In your n8n workflow editor, add the **CSVBox Trigger** node.
2. Choose your CSVBox credential from the dropdown (set up your API Key and Secret in n8n Credentials first).
3. Select the Sheet name you want to monitor for new imports.
4. Click **Fetch and execute** to test the trigger and preview sample data from your sheet.
5. Once you see the sample data, connect and map it to the next node in your workflow.
6. Activate your workflow. Now, whenever new rows are imported into your selected CSVBox sheet, your workflow will run automatically.

---

## Resources

- [CSVBox Documentation](https://help.csvbox.io/destinations/n8n)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)

---

## License

[MIT](LICENSE.md)