# n8n-nodes-cosense

This is an n8n community node. It lets you integrate [Cosense](https://scrapbox.io/) (formerly Scrapbox) into your n8n workflows.

Cosense is a collaborative documentation platform that allows teams to create, share, and organize knowledge using a unique wiki-style interface with real-time collaboration features.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### npm

```bash
npm install n8n-nodes-cosense
```

### n8n UI

1. Open your n8n instance
2. Go to **Settings** > **Community Nodes**
3. Select **Install**
4. Enter `n8n-nodes-cosense` in the npm Package Name field
5. Agree to the risks of using community nodes
6. Select **Install**

## Authentication

This node supports two authentication methods:

### 1. Session Cookie Authentication (Default)

- Works for all operations (read and write)
- Requires a session ID from Cosense

**How to get your Session ID:**
1. Log in to your Cosense account in a web browser
2. Open Developer Tools (F12)
3. Go to the Application/Storage tab
4. Find Cookies for `scrapbox.io`
5. Copy the value of `connect.sid`

### 2. Service Account Authentication (Business Plan Only)

- Read-only access to Private Projects
- Available only for Business Plan users
- Limited to same-project API access

**How to get your Service Account Key:**
1. Go to your Project Settings
2. Navigate to the Service Accounts tab
3. Generate a new Service Account Access Key

## Operations

This node supports the following operations:

### Get Page
Retrieve a specific page by title.

**Parameters:**
- Project Name (required)
- Page Title (required)

### List Pages
Get a list of pages in a project.

**Parameters:**
- Project Name (required)
- Limit (optional, default: 100)
- Skip (optional, default: 0)

### Search Pages
Search for pages using keywords.

**Parameters:**
- Project Name (required)
- Search Query (required)
- Search Type: Title Search or Full-text Search
- Limit (optional, default: 50)

### Create Page
Create a new page in a project.

**Parameters:**
- Project Name (required)
- Page Title (required)
- Content (required)

**Note:** Requires Session Cookie authentication.

### Insert Lines
Insert text at a specific line in an existing page.

**Parameters:**
- Project Name (required)
- Page Title (required)
- Line Number (required)
- Text to Insert (required)

**Note:** Requires Session Cookie authentication.

## Example Usage

### Basic Page Retrieval

1. Add a Cosense node to your workflow
2. Select "Get Page" as the operation
3. Enter your project name and page title
4. Execute the node

### Batch Processing Pages

1. Use List Pages to get all pages
2. Connect to a Loop node
3. Process each page individually
4. Use Insert Lines to update pages with results

### Search and Update Workflow

1. Search Pages with specific keywords
2. Filter results based on criteria
3. Update matching pages with new content

## Error Handling

The node includes comprehensive error handling:

- **Authentication errors (401)**: Check your credentials
- **Not found errors (404)**: Verify project name and page title
- **Conflict errors (409)**: Page already exists (for Create Page)
- **Rate limiting (429)**: Automatic retry with exponential backoff
  - Maximum 3 retries
  - Delays: 1s, 2s, 4s (up to 60s max)
  - Transparent to workflow execution

Enable "Continue On Fail" in node settings to handle errors gracefully in your workflows.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Cosense (Scrapbox) Documentation](https://scrapbox.io/help/)
* [Cosense API Reference](https://scrapbox.io/scrapboxlab/Scrapbox_REST_API%E3%81%AE%E4%B8%80%E8%A6%A7)

## Development

```bash
# Install dependencies
npm install

# Build the node
npm run build

# Run tests
npm test

# Run integration tests (requires .env configuration)
npm run test:integration

# Lint the code
npm run lint
```

### Integration Tests

To run integration tests against the actual Cosense API:

1. Copy `.env.example` to `.env`
2. Fill in your Cosense credentials:
   - `COSENSE_PROJECT_NAME`: Your project name
   - `COSENSE_SID`: Your session ID (for full access)
   - `COSENSE_SERVICE_ACCOUNT_KEY`: Your service account key (optional, read-only)
3. Run `npm run test:integration`

**Note:** Integration tests will create test pages in your specified project. Make sure to use a test project.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
