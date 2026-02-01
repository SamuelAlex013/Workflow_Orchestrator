## n8n WPForms Trigger node

NPM package name: `n8n-nodes-wpforms`

This repository contains custom n8n nodes for WPForms integration, providing triggers and actions to automate workflows with WPForms data.

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Build and Install the Node Package

### 1. Install Dependencies
```bash
npm install
```

### 2. Build the Project
```bash
npm run build
```
This command will:
- Clean the `dist` directory
- Compile TypeScript files
- Build icons using gulp
- Generate the distributable files

### 3. Link the Package Locally
```bash
npm link
```

### 4. Set Up Custom Nodes Directory
```bash
# Create custom directory in n8n home
mkdir -p ~/.n8n/custom
cd ~/.n8n/custom

# Initialize npm in the custom directory
npm init -y
```

### 5. Link Node to n8n Instance
```bash
# Link your custom node to n8n (run from ~/.n8n/custom)
npm link n8n-nodes-wpforms
```

### 6. Configure n8n Environment
Set the environment variable to tell n8n where to find custom nodes:

**For Linux/Mac:**
```bash
export N8N_CUSTOM_EXTENSIONS="$HOME/.n8n/custom"
```

**For Windows (PowerShell):**
```powershell
$env:N8N_CUSTOM_EXTENSIONS="$HOME\.n8n\custom"
```

### 7. Start n8n
```bash
n8n start
```

### 8. Verify Installation
1. Open n8n in your browser (usually `http://localhost:5678`)
2. Look for your custom nodes in the node palette
3. You should see "WPForms" nodes available

## Setup and Usage Instructions for WPForms Trigger Node

### Prerequisites

- A WordPress site with the WPForms plugin + WPForms n8n addon installed and activated.
- An n8n instance.

### Installation

1.  Go to your n8n instance.
2.  Go to **Settings > Community Nodes**.
3.  Click **Install a community node**.
4.  Enter `n8n-nodes-wpforms` in the **npm package name** field.
5.  Click **Install**.

### Configuration

1.  In your n8n workflow, add the **WPForms Trigger** node.
2.  Configure the node settings:
    *   **Secret Key**: Enter a secret key. This key must match the secret key configured in your WPForms n8n addon settings. It is used to verify the integrity of the data received.
    *   **Timestamp Skew**: Set the allowed time difference in seconds between your server and the WPForms server. The default is 300 seconds.
    *   **Output Schema**: Choose the output format. 'Default' provides a structured JSON object, while 'Raw' provides the raw request body and headers.
3.  The node will display a webhook URL. Copy this URL.
4.  In the Form Builder, go to the Marketing > n8n tab.
5.  Enable n8n integration.
6.  Paste the webhook URL from n8n.
7.  Copy Secret Key and paste it to the WPForms Trigger node.
8.  Save your form settings.

### Usage

Now, whenever the selected form is submitted, it will trigger your n8n workflow. The form data will be available in the node's output.

## Development Workflow 

In Linux/MacOS or Windows using PS 7 shell:

```bash
cd /path/to/wpforms-n8n-nodes/

# Build and link after changes
npm run build && npm link

# Watch for changes during development
npm run dev
```

In your n8n instance, re-link the node and restart n8n:
```bash
cd ~/.n8n/custom

# Re-link node and restart n8n:
npm link n8n-nodes-wpforms && n8n start
```

## Testing Your Node 

```bash
# Check for linting errors
npm run lint

# Auto-fix linting errors when possible
npm run lintfix
```

## Publishing  

First you need to bump the version. This needs to be reflected both in the package.json & the package-lock.json.  

You can also do that using `npm version` - this will also create the new tag:  

```bash
npm version patch  # for bug fixes (0.1.2 → 0.1.3)
npm version minor  # for new features (0.1.2 → 0.2.0)
npm version major  # for breaking changes (0.1.2 → 1.0.0)
```

Next, you need to push the change in the main branch and also create/push a tag starting with `v`, e.g. v0.1.3

We are publishing automatically to npm each time a tag is pushed in the repo.  
Alongside that, a GitHub Release is also created.  

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
