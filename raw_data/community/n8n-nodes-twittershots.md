![n8n TwitterShots node image](./n8n-TwitterShots-node.png)

# n8n-nodes-twittershots

A n8n node lets you easily screenshot X (Twitter) posts in your workflows with TwitterShots API.

- [TwitterShots](https://twittershots.com/) is professional X/Tweet screenshot generator.
- [n8n](https://n8n.io/) is a fair-code licensed workflow automation platform.

## Features

- Multiple output formats (SVG, PNG, HTML)
- Light/Dark theme support
- Customizable logo options (X, bluebird, or none)
- Configurable display options (full text, timestamp, view count, statistics)
- Simple API integration

## Authentication

Before using the node, you need to set up TwitterShots API credentials:

1. Visit [TwitterShots account](https://twittershots.com/account/settings) to get your API key
2. Add your API key to n8n credentials

For detailed information about API credentials and parameters, please refer to the [API Documentation](https://twittershots.com/docs/api).

## Usage

1. Search TwitterShots and add TwitterShots node to your workflow
2. Select "Tweet Screenshot" resource
3. Select "Get a tweet screenshot" action
4. Create TwitterShots API credentials
5. Select Tweet Screenshot Resource
6. Enter the tweet ID and configure output format and display options
7. Run the workflow to get your screenshot

## Dev and test node local

### Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

1.Clone your new repo

  ```
  git clone https://github.com/0xinhua/n8n-nodes-twittershots
  ```

2.When you are ready to test your node, publish it locally

```
# In your n8n-nodes-twittershots directory
npm i
npm run build
npm link
```

3. Install the node into your local n8n instance:

```
# In the nodes directory within your n8n installation
npm link n8n-nodes-twittershots
```

4.Start n8n:

```
n8n start
```

5.Open n8n in your browser. You should see TwitterShots nodes when you search for them in the nodes panel.

Checkout full docs [test n8n node](https://docs.n8n.io/integrations/creating-nodes/build/declarative-style-node/#test-your-node).

### Issues

If you need help or have any questions:

- Check the [API Documentation](https://twittershots.com/docs/api)
- Email us at support@twittershots.com
- Create an issue on [GitHub Issues](https://github.com/0xinhua/n8n-nodes-twittershots/issues)

## License

[MIT](LICENSE.md)
