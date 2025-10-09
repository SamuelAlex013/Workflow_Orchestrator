# n8n-nodes-extended-gitlab

This package provides an extended GitLab node for [n8n](https://n8n.io). It expands the built-in GitLab integration with many additional API operations.

## Installation

Follow the [community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to install the package from npm:

```bash
npm install n8n-nodes-extended-gitlab
```

## Usage

1. Install the package through **Community Nodes** in the n8n settings or run `npm install n8n-nodes-extended-gitlab` in your n8n directory.
2. Create **Gitlab Extended API** credentials providing your server URL, personal access token and default project ID.
3. Drop the **Gitlab Extended** node into a workflow and select your credentials.
4. Pick a resource and operation, then fill in the required fields.

For example, choose `pipeline` and `getAll` to list all pipelines in your project.

## Operations

Operations are grouped by resource. Select the desired `resource` and then pick
one of its operations.

### Branch

- `create` – Create a branch
- `get` – Get a branch
- `getAll` – List branches
- `delete` – Delete a branch
- `rename` – Rename a branch
- `protect` – Protect a branch
- `unprotect` – Unprotect a branch
- `merge` – Merge a branch

### Pipeline

- `create` – Trigger a pipeline
- `retry` – Retry a pipeline
- `cancel` – Cancel a pipeline
- `get` – Get a pipeline by ID
- `getAll` – List pipelines
- `getJobs` – List jobs for a pipeline
- `delete` – Delete a pipeline
- `downloadArtifacts` – Download artifacts from a pipeline

### Tag

- `create` – Create a tag
- `get` – Get a tag
- `getAll` – List tags
- `delete` – Delete a tag

### Release

- `create` – Create a release
- `update` – Update a release
- `get` – Get a release
- `getAll` – List releases
- `delete` – Delete a release

### Group

- `create` – Create a group
- `get` – Get a group
- `delete` – Delete a group
- `getMembers` – List group members

### Project

- `create` – Create a project
- `get` – Get a project
- `getAll` – List projects
- `search` – Search projects

### File

- `create` – Create a file
- `update` – Update a file
- `delete` – Delete a file
- `get` – Retrieve a file
- `list` – List repository files

### Issue

- `create` – Create an issue
- `update` – Update an issue
- `close` – Close an issue
- `reopen` – Reopen an issue
- `get` – Get an issue by number
- `getAll` – List issues

### Merge request

- `create` – Create a merge request
- `get` – Get a merge request
- `getAll` – List merge requests
- `createNote` – Add a note
- `postDiscussionNote` – Reply or start a discussion
- `updateNote` – Update a note by ID
- `updateDiscussionNote` – Update a note in a discussion
- `deleteNote` – Delete a note
- `getNote` – Get a note
- `getChanges` – Get merge request changes
- `getDiscussions` – List discussions
- `getDiscussion` – Get a discussion
- `updateDiscussion` – Update a discussion
- `deleteDiscussion` – Delete a discussion
- `resolveDiscussion` – Resolve or unresolve a discussion
- `merge` – Merge (accept) a merge request
- `rebase` – Rebase a merge request
- `close` – Close a merge request
- `reopen` – Reopen a merge request
- `labels` – Add or remove labels based on `labelAction`

### Raw API

- `request` – Call any GitLab endpoint

### Example: Managing Labels on a Merge Request

To add labels to a merge request, use the `labels` operation with the following parameters:

- `mergeRequestIid`: The IID of the merge request.
- `labelAction`: Set to `add` or `remove`.
- `labels`: Comma-separated label names.

Example:

```json
{
	"operation": "labels",
	"mergeRequestIid": 123,
	"labelAction": "add",
	"labels": "bug,urgent"
}
```

## Parameters

Below is a concise list of parameter names used by the node. Provide only those
required for your chosen operation.

| Name                 | Description                                        |
| -------------------- | -------------------------------------------------- |
| `branch`             | Name of a branch                                   |
| `ref`                | Source branch or commit                            |
| `newBranch`          | New name when renaming                             |
| `targetBranch`       | Target branch for merges                           |
| `developersCanPush`  | Allow developers to push                           |
| `developersCanMerge` | Allow developers to merge                          |
| `pipelineId`         | Numeric pipeline ID (positive)                     |
| `pipelineRef`        | Branch or tag for pipelines and artifact downloads |
| `path`               | File or directory path                             |
| `fileRef`            | Branch, tag or commit for file operations          |
| `title`              | Title for issues and merge requests                |
| `description`        | Description text                                   |
| `issueIid`           | Issue IID (positive)                               |
| `issueLabels`        | Issue labels, comma-separated                      |
| `issueState`         | Desired issue state (`reopen` or `close`)          |
| `mergeRequestIid`    | Merge request IID (positive)                       |
| `labels`             | Comma-separated label list                         |
| `labelAction`        | `add` or `remove`                                  |
| `body`               | Body of a note                                     |
| `startDiscussion`    | Start a new discussion                             |
| `discussionId`       | Discussion ID                                      |
| `resolved`           | Whether a discussion is resolved                   |
| `noteId`             | ID of a note (positive)                            |
| `positionType`       | `text` or `image` position                         |
| `newPath`/`oldPath`  | File paths for note position                       |
| `newLine`/`oldLine`  | Optional line numbers for note position           |
| `lineRangeStartLineCode` | Line code for the start line of a multiline note |
| `lineRangeStartType` | `new` or `old` start line type |
| `lineRangeStartOldLine`/`lineRangeStartNewLine` | Optional line numbers for the start line |
| `lineRangeEndLineCode` | Line code for the end line of a multiline note |
| `lineRangeEndType` | `new` or `old` end line type |
| `lineRangeEndOldLine`/`lineRangeEndNewLine` | Optional line numbers for the end line |
| `baseSha`            | Base commit SHA                                    |
| `headSha`            | Head commit SHA                                    |
| `startSha`           | Start commit SHA                                   |
| `mergeCommitMessage` | Commit message when merging                        |
| `mergeStrategy`      | `merge` or `squash`                                |
| `skipCi`             | Skip CI when rebasing                              |
| `httpMethod`         | Method for raw requests                            |
| `endpoint`           | Endpoint path                                      |
| `content`            | JSON body payload                                  |
| `queryParameters`    | JSON query parameters                              |
| `returnAll`          | Return every result when listing                   |
| `limit`              | Maximum number of results                          |

Optional parameters set to `null` are omitted from requests. Use this to avoid
sending the `resolved` flag when updating a note body with `updateDiscussionNote`.
| `groupId`            | Numeric group ID                                   |
| `groupName`          | Name when creating a group                         |
| `groupPath`          | Path when creating a group                         |
| `parentId`           | Parent group ID when creating a subgroup          |
| `projectId`          | Numeric project ID                                 |
| `projectName`        | Name when creating a project                       |
| `projectPath`        | Path when creating a project                       |
| `namespaceId`        | Namespace for the new project                      |
| `searchTerm`         | Term to search projects                            |

## Credentials

Authentication can use the saved <code>Gitlab Extended API</code> credentials or custom values entered directly in the node. When selecting <strong>Custom</strong> authentication you provide the server URL, token and project details on the node itself.

The credentials' or custom <code>server</code> field specifies your GitLab instance host (e.g. <code>https://gitlab.your-company.com</code>). Requests automatically use the <code>/api/v4</code> path.

## Compatibility

This package requires n8n version 1.0.0 or later and is tested on Node.js 20.

## Development

Install dependencies with `npm install` and ensure the `n8n-workflow` peer is installed:

```bash
npm install
npm install n8n-workflow
```

Run the tests with:

```bash
npm test
```

## Tool usage for AI

The node is marked with `usableAsTool: true`, so it can be invoked by n8n's AI
features. After installing the package and creating the **Gitlab Extended API**
credentials, the node appears in the list of available tools when building
generative AI workflows. An AI agent can call any of the supported operations—
such as fetching files or creating issues—by providing the necessary
parameters in natural language. The node runs using the credentials you
configured, enabling automated access to your GitLab projects from AI-driven
flows.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [GitLab API documentation](https://docs.gitlab.com/ee/api/)

## License

[MIT](LICENSE.md)
