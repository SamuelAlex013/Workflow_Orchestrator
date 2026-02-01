# n8n-nodes-tally

This is an n8n community node that lets you interact with [Tally.so](https://tally.so) forms and submissions in your n8n workflows.

[Tally.so](https://tally.so) is a form builder that allows you to create beautiful forms and collect responses. This node enables you to:

- 📋 Retrieve forms and questions, and manage fields safely
- ✏️ Add/Update/Delete fields, Copy questions between forms, and Rollback
- 🆕 Create a new form from JSON (Draft/Published)
- 📊 Access submissions

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes** in your n8n instance
2. Select **Install**
3. Enter `n8n-nodes-tally` as the npm package name
4. Click **Install**

Alternatively, you can install it via npm in your n8n installation:

```bash
npm install n8n-nodes-tally
```

## Prerequisites

You need a Tally.so account and API token to use this node.

### Getting Your API Token

1. Log into your [Tally.so account](https://tally.so)
2. Go to **Settings > Integrations**
3. Find the **API** section and generate a new API token
4. Copy the token for use in n8n

> **Note:** Free tier Tally.so accounts have API access with reasonable rate limits.

## Configuration

1. In n8n, create a new **Tally.so API Token** credential
2. Paste your API token from Tally.so
3. Test the connection to verify it works

## Supported Operations

### Form Resource

#### Get All Forms
- **Purpose**: Retrieve a list of all your forms
- **Output**: Array of form objects with basic information (id, name, dates)
- **Use case**: Discover available forms for further processing

#### Get Form
- **Purpose**: Get detailed information about a specific form
- **Input**: Form ID (selected from dropdown)
- **Output**: Complete form data including fields, configuration, and metadata
- **Use case**: Inspect form structure before processing submissions

#### List Questions (v1.2)
- Purpose: List question metadata for a form (includes block UUIDs, labels, and types)
- Input: Form ID
- Output: Array of question objects

#### Add Field (v1.2)
- Purpose: Add a new question to a form without editing raw JSON
- Inputs: Form, Type, Label, Placeholder (for input types), Options (JSON) for option-based types, Payload (JSON) for non-option types, insert position (end/index/before/after)
- Behavior:
  - Option-based types (Dropdown, Multiple Choice, Checkboxes, Multi-select): Provide Options (JSON) like ["Option 1","Option 2"]. The node generates one block per option and hides Payload (JSON) to avoid confusion.
  - Input types (Short/Long Text, Email, URL, Phone, Number, Date, Time): Placeholder is merged into payload; if Placeholder is empty, Label is used as the placeholder. Payload (JSON) is merged on top; Required toggle sets payload.isRequired.
- Safety: Fetch → merge → PATCH full blocks; supports Dry‑Run, Backup, and Optimistic Concurrency

#### Update Field (v1.2)
- Purpose: Update a field’s payload or label by UUID or by label resolution
- Inputs: Form, target (UUID/Label), payloadPatch (JSON), merge strategy (merge/replace)
- Safety: Dry‑Run preview with diff; Backup and Optimistic Concurrency supported

#### Delete Field (v1.2)
- Purpose: Remove one or more fields by UUID(s) or by label(s)
- Inputs: Form, target selection (UUID/Label), one or more values
- Safety: Full blocks PATCH with Dry‑Run/Backup/Optimistic

<!-- Sync Select Options was removed in favor of higher-level field ops in this release. -->

#### Copy Questions (v1.2)
- Purpose: Copy questions from a source form to a destination form
- Inputs: Source Form, Destination Form, question UUIDs, insert position
- Notes: UUIDs are regenerated; complex logic/dependencies may not port 1:1 (API errors are surfaced)
- Safety: Dry‑Run + diff; Backup + Optimistic for destination form

Title handling when copying:

- Selective copy: If a question group is copied and it has an immediately preceding TITLE block (groupType=QUESTION), the node will automatically include that TITLE to preserve context.
- Copy All: The node skips auto‑inserting preceding TITLEs when their own title groups are already included by the “Copy All” selection, avoiding duplicate TITLEs in the destination.
- Tip: Use Dry‑Run first to preview the proposed blocks and confirm titles appear as expected without duplication.

#### Rollback Form (v1.2)
- Purpose: Restore or copy forms from JSON
- Inputs: Form (destination form to overwrite), Backup Form JSON (or leave empty to consume incoming `$json.backup`, `$json.form`, or `$json`)
- Modes:
  1) Save JSON and restore later: keep the `previousForm` JSON from write ops and use it here to roll back.
  2) Copy an existing form: wire Tally “Get Form” → “Rollback Form” and leave JSON empty; the node uses `$json.form`. This works across accounts/instances.
- Safety: Dry‑Run/Preview shows proposed blocks and a diff for overwrite flows; Optimistic Concurrency applies to overwrite (PATCH) only.

#### Create Form (v1.2)
- Purpose: Create a brand new form from JSON
- Inputs: Form JSON (or leave empty to consume incoming `$json.form` or `$json`), optional Workspace, Final Status (Draft/Published/Blank)
- Behavior:
  - POST /forms with `{ workspaceId, status: 'BLANK', blocks, settings }` (FORM_TITLE ensured)
  - Immediately PATCH /forms/{id} with full `blocks` (and name/settings) to persist content
  - Optionally PATCH `status` to Draft or Published so it appears in the UI
  - Dry‑Run emits `{ preview: true, createBody, patchBody, targetStatus }` without any changes
- Tip: For cross‑account cloning, fetch with Account A, create with Account B (select B’s workspace).

### Submission Resource

#### Get All Submissions
- **Purpose**: Retrieve all form responses for a specific form
- **Input**: Form ID (selected from dropdown)
- **Output**: Array of submission objects
- **Features**:
  - Automatic pagination handling
  - Defensive response parsing for various API response formats
  - Error handling for forms with no submissions

**Response Handling**: The node automatically handles different response formats from the Tally API:
```json
{
  "submissionId": "sub_123",
  "createdAt": "2025-01-01T00:00:00Z",
  "formId": "form_456",
  "data": { /* submission fields */ }
}
```

## Example Workflows

### 1. Form Submissions to Google Sheets

```
Tally.so (Get All Submissions) → Google Sheets (Append Row)
```

1. **Tally.so Node**: 
   - Resource: Submission
   - Operation: Get All
   - Form: Select your form

2. **Google Sheets Node**:
   - Operation: Append
   - Map submission data to sheet columns

### 2. Daily Form Analysis

```
Schedule Trigger → Tally.so (Get All Submissions) → Process Data → Send Report
```

Perfect for daily/weekly form analytics and reporting.

### 3. Form Data to Database

```
Tally.so (Get All Forms) → Tally.so (Get All Submissions) → Database (Insert)
```

1. Get all forms to discover available forms
2. For each form, retrieve submissions
3. Store in your database for analysis

### 4. Clone a form into a new one (v1.2)

```
Tally.so (Get Form - source) → Tally.so (Create Form - select target Workspace, Final Status: Draft/Published)
```

1. Get the source form JSON
2. Create Form with that JSON, optionally to a different account/workspace
3. Choose Draft or Published so it shows up immediately

### 5. Copy Fields Between Forms (v1.2)
### 6. Add Field examples (v1.2)

- Add Multiple Choice with options:

  - Type: Multiple Choice
  - Title: Favorite Color
  - Options (JSON): ["Red","Green","Blue"]
  - Required: true
  - Dry‑Run first to preview per-option blocks

- Add Phone input with placeholder via Label fallback:

  - Type: Phone
  - Title: Contact Number
  - Label: (XXX) XXX-XXXX
  - Placeholder: (leave empty to use Label)
  - Required: true
  - Dry‑Run to verify payload includes placeholder and internationalFormat

```
Tally.so (List Questions - source) → Select IDs → Tally.so (Copy Questions) → Tally.so (List Questions - dest)
```

1. List questions on the source form and pick the UUIDs to copy
2. Run Copy Questions into the destination form at the desired position
3. Verify with List Questions on the destination form
  - Note on titles: In selective copies, the preceding TITLE is included automatically when present; in Copy All mode, title duplication is avoided by design.

## Safety, Concurrency, and Rollback (v1.2)

Updating a form uses Tally’s PATCH and rewrites the form’s blocks. This node always fetches, merges, and patches the full array to avoid destructive edits.

- Dry‑Run/Preview: Outputs proposed blocks and a diff; does not modify the form
- Backup: Outputs the pre‑patch form JSON so you can Rollback later
- Optimistic Concurrency: Compares updatedAt to prevent hidden overwrites

If a form changed during your workflow, the node will abort with a clear message—re-run the node to avoid conflicts.

## API Information

This node uses the Tally.so REST API endpoints:
- `GET /forms` - List forms
- `GET /forms/{id}` - Get specific form details  
- `GET /forms/{id}/submissions` - Get form submissions
- `GET /forms/{id}/questions` - List questions for a form
- `POST /forms` - Create a form
- `PATCH /forms/{id}` - Update a form (full blocks array is provided by this node)

The node automatically handles:
- Authentication via Bearer token
- Different response formats from the API
- Error handling and user-friendly error messages
- Continue-on-fail functionality for workflow resilience

## Rate Limits

Tally.so implements rate limiting on their API. If you encounter rate limit errors:

- Reduce the frequency of your requests
- Implement retry logic with exponential backoff
- Contact Tally.so support if you need higher limits

## Error Handling

The node provides detailed error messages for common issues:

- **Invalid API token**: Check your credential configuration
- **Form not found**: Verify the form ID exists and you have access
- **Submission not found**: Check the submission ID is correct
- **Rate limit exceeded**: Implement delays between requests

## Troubleshooting

### Empty Submission Data

1. Verify the form has actual submissions
2. Check that you have the correct form ID
3. Ensure your API token has access to the form

### Connection Issues

1. Test your API credential in n8n
2. Verify your API token is valid in Tally.so
3. Check your network connectivity

### Form Not Loading

1. Ensure your API token has the correct permissions
2. Check that the form exists and hasn't been deleted
3. Verify you're using the correct form ID

## Limitations

Known limitations:

- No webhook management (webhooks not available via Tally.so public API)
- Complex dependencies/logic/groups may not fully port when copying questions
- No analytics data retrieval
- No file upload handling for form attachments

## Version History

- v1.2.0
  - New field ops: List Questions, Add/Update/Delete Field, Copy Questions, Rollback
  - Create Form: POST + PATCH blocks; Final Status to Draft/Published
  - Safety: Dry‑Run preview, Backup JSON, Optimistic Concurrency
  - PATCH flow: fetch → modify → patch full `blocks`

- v1.0.0
  - Initial release with forms and submissions
  - REST API integration
  - Robust error handling and response parsing
  - Defensive handling of various API response formats

## Development

This repo uses the official n8n Node CLI with pnpm and Node.js >= 20.19.

Prerequisites:
- Node.js >= 20.19 (an `.nvmrc` is provided)
- pnpm (via corepack)

Setup:

```bash
pnpm install
```

Run dev server with hot reload:

```bash
pnpm dev
```

This launches n8n at http://localhost:5678 and watches this node for changes (TypeScript rebuild + live reload).

Build distributable:

```bash
pnpm build
```

Lint and autofix:

```bash
pnpm lint
pnpm lint:fix
```

Optional: Use your own n8n instance (Docker/remote):

```bash
# In this repo (build + watch only)
pnpm exec n8n-node dev --external-n8n

# In your n8n environment
# ensure the env var is set so n8n reloads extensions on changes
export N8N_DEV_RELOAD=true
```

## Contributing

This is a community node. Issues, suggestions, and contributions are welcome!

## License

[MIT](LICENSE)

## Support

- **n8n Community**: [n8n Community Forum](https://community.n8n.io)
- **Tally.so API Docs**: [Tally Developer Documentation](https://developers.tally.so)
- **Issues**: [GitHub Issues](https://github.com/brianmoney/n8n-nodes-tally/issues)

---

**Built with ❤️ for the n8n community**
