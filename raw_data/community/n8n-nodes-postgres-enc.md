
![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-postgres-encryption

This repo contains [n8n](n8n.io) node and credentials for a custom Postgres integration. It adds support for ssmode=verify* (similarly to [SSL support for MySQL](https://github.com/n8n-io/n8n/pull/1644/files)). Includes the node linter and other dependencies.
Credentials testing for non API-based credentials does not work properly in n8n, so do not focus on errors related to "Couldn’t connect with these settings. No testing function found for this credential."

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 16. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
	```
	npm install n8n -g
	```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).


## Using this repo

These are the basic steps for working with the repo. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your repo:
    ```
    git clone git@github.com:hycomsa/n8n-postgres-encryption.git
    ```
3. Run `npm i` to install dependencies.
4. Update the `package.json` to match your details.
5. Run `npm run build` to compile the codes.
6. To install the node on an n8n:
6.1. Follow instructions from [Install your node in a docker n8n instance](https://docs.n8n.io/integrations/creating-nodes/deploy/install-private-nodes/#install-your-node-in-a-docker-n8n-instance)
6.2. For the approach with docker-compose from this repo, create directory `custom` in `/home/node/.n8n` and then inside this directory call `npm i n8n-nodes-postgres-enc`

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
