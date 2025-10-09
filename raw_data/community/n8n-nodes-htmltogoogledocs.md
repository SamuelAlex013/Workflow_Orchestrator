![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# HTML to Google Docs Node for n8n

This is an n8n community node that allows you to upload HTML content directly to Google Docs. With this node, you can automate the creation of Google Docs documents from HTML content in your n8n workflows.

## Features

- Convert HTML content to Google Docs format
- Create new Google Docs documents programmatically
- Support for rich HTML formatting (headings, lists, links, etc.)
- Authentication via Google OAuth2

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Alternatively, you can install the node directly from npm:

```bash
npm install n8n-nodes-htmltogoogledocs
```

## Operations

This node allows you to:

- Upload HTML content to Google Docs
- Create new Google Docs documents with HTML content

## Credentials

To use this node, you need to authenticate with Google Drive using OAuth2.

### Prerequisites

1. You need a Google account
2. Enable the Google Drive API in your Google Cloud Console
3. Create OAuth2 credentials (Client ID and Client Secret)

### Setup

1. In n8n, go to Settings > Credentials
2. Click on "Add Credential"
3. Select "Google Drive OAuth2 API" (predefined credential)
4. Click on "Connect my account" and follow the OAuth flow

## Compatibility

This node is compatible with n8n version 0.1.0 and above.

## Usage

1. Add the HTML to Google Docs node to your workflow
2. Configure the credentials by selecting your Google Drive OAuth2 account
3. Enter the document name for your new Google Doc
4. Provide the HTML content you want to upload
5. Execute the workflow

The node will create a new Google Doc with your HTML content converted to Google Docs format.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Google Drive API documentation](https://developers.google.com/drive/api)

## Release Process

This project uses semantic-release to automate the release process. All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

#### Types

- `feat`: A new feature
- `fix`: A bug fix
- `perf`: A code change that improves performance
- `revert`: Reverts a previous commit
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to our CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files

### Release Automation

Releases are automatically created when changes are merged to the `master` branch. The semantic-release tool analyzes commits and determines the next version number based on the commit types:

- `feat` commits will trigger a minor version bump
- `fix` commits will trigger a patch version bump
- `BREAKING CHANGE` in the commit body will trigger a major version bump

## License

[MIT](https://github.com/WalkingStatue/n8n-nodes-htmltogoogledocs/blob/master/LICENSE.md)
