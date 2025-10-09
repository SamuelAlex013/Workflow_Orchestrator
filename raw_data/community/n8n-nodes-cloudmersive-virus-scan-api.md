# n8n-nodes-cloudmersive-virus-scan-api

This is an n8n community node. It lets you use Cloudmersive Virus Scan API in your n8n workflows.

Cloudmersive Virus Scan API enables you to scan files and content for viruses and leverage continuously updated signatures for millions of threats, and advanced high-performance scanning capabilities.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.  Once installed, search for **Cloudmersive Virus Scan** in the node picker.

## Operations

This node currently supports the following resources and operations:

### File

* **Scan** — Scan a binary file from the incoming item.
* **Advanced Scan** — Scan a binary file with 360° content protection controls (block macros, scripts, restrict file types, etc.).

  * Optional: **Override File Name** header for content-aware scanning.

**Required input**

* *Binary Property Name* — defaults to `data`.

**Advanced controls** (Advanced Scan):

* Booleans: `allowExecutables`, `allowHtml`, `allowInsecureDeserialization`, `allowInvalidFiles`, `allowMacros`, `allowOleEmbeddedObject`, `allowPasswordProtectedFiles`, `allowScripts`, `allowUnsafeArchives`, `allowXmlExternalEntities`
* Multi-select **Options** (sent as a comma-separated `options` header):

  * `blockInvalidUris`, `blockOfficeXmlOleEmbeddedFile`, `permitAuthenticodeSignedExecutables`, `permitJavascriptAndHtmlInPDFs`, `scanMultipartFile`
* **Restrict File Types** — comma-separated extensions to permit (e.g., `.pdf,.docx,.png`).

### Website

* **Scan** — Scan a website URL for malicious content and threats.
  **Input**: `URL` (http/https)


## Credentials

The Cloudmersive Virus Scan API is free to use.  You can get a free API key that does not expire by going to [Cloudmersive](https://portal.cloudmersive.com/signup) and signing up.  You can use Cloudmersive SaaS or your own Cloudmersive Private Cloud.

## Compatibility

* **n8n**: built and tested on n8n v1.x
* **Runtime**: standard n8n Docker and desktop builds
* If you run an older n8n version and encounter issues, please update to a recent 1.x build.

## Usage

To use the service, simply drop the node into your flow and pass in a file as the data parameter.  Look at the CleanResult attribute returned as part of the output to confirm if your file passed the scan.

### Common patterns

**A) Scan an uploaded file (Webhook → Virus Scan)**

1. **Webhook** node receives a file (ensure *Binary Data* is enabled).
2. **Cloudmersive Virus Scan → File → Scan**

   * *Binary Property Name*: `data` (or your property name)
3. Use an **IF** node to branch on the scan result (the node returns the Cloudmersive response JSON; check the “clean/dirty” flags or threat details relevant to your policy).

**B) Advanced scan with restrictions**

* Choose **File → Advanced Scan** and set **Advanced Controls**:

  * For example, disable scripts/macros, and set **Restrict File Types** to `.pdf,.docx`.
* Optional: set **Override File Name** for better content handling.

**C) Scan a website**

* Choose **Website → Scan** and provide the URL (http/https).

### Output

* The node returns the **raw Cloudmersive API JSON** response on `items[0].json`.
* Use standard n8n nodes (**IF**, **Set**, **Switch**) to branch, extract fields, and handle positives/negatives per your workflow.

### Tips

* For large files, ensure your n8n instance has sufficient upload limits and memory.
* If you run Cloudmersive Private Cloud, set the **Base URL** in credentials so traffic never leaves your network.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Cloudmersive Virus Scan API Documentation](https://api.cloudmersive.com/docs/virus.asp)

