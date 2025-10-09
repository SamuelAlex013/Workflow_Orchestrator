# n8n-nodes-octoparse

**n8n-nodes-octoparse** is a community node for [n8n](https://n8n.io/) that allows you to automate and orchestrate your [Octoparse](https://www.octoparse.com/) web scraping workflows directly from n8n. This node provides full access to the Octoparse API, including task management, cloud extraction, and data retrieval.

---

## Features

- **Task Management**: List, copy, move, and search Octoparse tasks and task groups.
- **Cloud Extraction**: Start/stop tasks, manage subtasks, and check extraction status.
- **Data Access**: Retrieve scraped data by offset or batch, mark data as exported, and remove data.
- **Authentication**: Securely connect to Octoparse using your credentials and automatic token handling.
- **n8n UX**: Clean, grouped UI with resource/operation dropdowns and context-sensitive fields.

---

## Installation

### Via npm

```bash
npm install n8n-nodes-octoparse
```

### Manual (for development)

```bash
git clone https://github.com/LPilic/n8n-nodes-octoparse.git
cd n8n-nodes-octoparse
npm install
npm run build
npm link
```

Then, in your n8n custom nodes directory:

```bash
cd ~/.n8n/custom
npm init # if you haven't already
npm link n8n-nodes-octoparse
```

Restart n8n and search for "Octoparse" in the node list.

---

## Usage

1. **Add the Octoparse node** to your n8n workflow.
2. **Configure authentication**: Enter your Octoparse username and password in the credentials section.
3. **Select a resource**: Choose between Tasks, Cloud Extraction, or Data.
4. **Choose an operation**: The available operations will update based on the selected resource.
5. **Fill in required fields**: Only relevant fields for your chosen operation will be shown.
6. **Execute the workflow**: The node will interact with the Octoparse API and return the results in a structured format.

### Example: Get Data by Offset

- Resource: `Data`
- Operation: `Get Data by Offset`
- Fill in Task ID, Offset, and Size.
- The response will include the data array, offset, total, and requestId as returned by Octoparse.

---

## Development

1. Clone the repo and install dependencies:
```bash
    git clone https://github.com/LPilic/n8n-nodes-octoparse.git
    cd n8n-nodes-octoparse
    npm install
    ```
2. Run tests and build:
```bash
npm run test
npm run build
    ```
3. Link the node into your n8n custom directory as shown above.

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check [issues page](https://github.com/LPilic/n8n-nodes-octoparse/issues) or submit a pull request.

---

## License

[MIT](LICENSE.md)

---

## Links

- [Octoparse API Documentation](https://openapi.octoparse.com/)
- [n8n Documentation](https://docs.n8n.io/)
- [GitHub Repository](https://github.com/LPilic/n8n-nodes-octoparse)
