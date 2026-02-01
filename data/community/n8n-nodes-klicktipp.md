# n8n-nodes-klicktipp

## KlickTipp API Integration for n8n

What is the KlickTipp Marketing Suite?

<a href="https://www.klicktipp.com/de?source=n8n" title="E-Mail-Marketing" target="_blank" rel="noopener noreferrer">KlickTipp Marketing Suite</a> is a digital marketing platform that empowers creators and small businesses to generate leads and turn them into passionate customers. It boosts growth with GDPR-compliant tools for email and SMS marketing, marketing automation, landing pages, and conversion rate optimization.

This package provides a set of nodes for interacting with the KlickTipp API, allowing you to manage contacts, tags, subscription processes, and more directly from n8n.
For more detailed information on the KlickTipp API—covering functions for managing contacts, tags, fields, and more—please refer to the <a href="https://www.klicktipp.com/de/support/wissensdatenbank/application-programming-interface-api?source=n8n" target="_blank" rel="noopener" title="E-Mail-Marketing API">official KlickTipp API client documentation</a> and the <a href="https://www.klicktipp.com/support/knowledge-base/install-klicktipp-node-n8n?source=n8n" target="_blank" rel="noopener" title="Install KlickTipp Node for n8n">installation guide for the KlickTipp node in n8n</a>.

---

## Table of Contents

- [Installation](#installation)
- [Nodes Overview](#nodes-overview)
  - [Contact](#contact)
  - [Contact Tagging](#contact-tagging)
  - [Data Field](#data-field)
  - [Opt-In Process](#opt-in-process)
  - [Tag](#tag)
  - [Triggers](#triggers)
- [Credentials](#credentials)
- [Error Handling](#error-handling)
- [License](#license)
- [Example Workflows](#example-workflows)

---

## Installation

To install the package, run the following command in your n8n directory:

```bash
npm install n8n-nodes-klicktipp
```

## Nodes Overview

This package includes nodes to interact with various aspects of the KlickTipp API:

### Contact

- **Nodes**:
  - `Add or update contact`
  - `Delete contact`
  - `Get contact`
  - `Search contact id`
  - `List contacts`
  - `Search tagged contacts`
  - `Unsubscribe contact`
  - `Update contact`
- **Description**: Provides management capabilities for contacts, such as searching, updating, and deleting contact data.

### Contact Tagging

- **Nodes**:
  - `Tag contact`
  - `Untag contact`
- **Description**: Provides management capabilities for contacts tagging.

### Data Field

- **Nodes**: 
  - `Get data field`
	- `List data fields`
- **Description**: Manages data fields, including retrieving all available data fields for contacts, and obtaining data field information.

### Opt-in Process

- **Nodes**:
  - `Get opt-in process`
  - `Search redirect url`
  - `list opt in process`
- **Description**: Manages opt-in processes, including listing all processes, retrieving details of a specific process, and obtaining redirect URLs.

### Tag

- **Nodes**:
  - `Create tag`
	- `Delete tag`
  - `Get tag`
  - `List tags`
  - `Update tag`
- **Description**: Manages tags within KlickTipp, enabling operations to list, create, update, and delete tags.

### Triggers

- **Node**: `On new KlickTipp event`
- **Description**: Triggers when a webhook event occurs in KlickTipp, such as a tag being added, an email being opened or sent, a link clicked, an SMS sent, and more.

---

## Credentials

To authenticate with the KlickTipp API, configure your API credentials:

- **Username**
- **Password**

Once set up, these credentials will be used across all KlickTipp nodes in the package.

---

## License

This package is licensed under the MIT License. For details, see the `LICENSE` file.

---

## Example Workflows

Refer to the `examples/n8n-nodes-klicktipp.json` file for sample workflows showcasing the integration.
