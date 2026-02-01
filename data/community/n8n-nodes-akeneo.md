![Banner image](https://github.com/pixelinfinito/akeneo-node-n8n/blob/main/nodes/Akeneo/akeneo.svg)

# Akeneo n8n node

This version is modified to provide pagination on the products. This pagination is presented as N8N items. Or the response error.

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Check n8n first for best node version to use.
* Install n8n with:
	```
	npm install n8n -g
	```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

> Consider using NVM to manage node versions and use the `reinstall-packages` feature

## Using on N8N

1. go to N8N settings
2. go to communities nodes
3. install the node with the name of `@flagbit/n8n-nodes-akeneo`
4. example ![Banner image](https://github.com/flagbit/akeneo-node-n8n/blob/main/images/flagbit-install.png)

## Using locally

These are the basic steps for working locally without using the NPM version.

1. Clone the repo:
    ```
    git clone https://github.com/flagbit/akeneo-node-n8n.git
    ```
3. Run `npm i` to install dependencies.
4. in the other terminal navigate to: C:\Users\{user}\AppData\Roaming\npm\node_modules\n8n. Or, wherever your global `node_modules` are (use `npm -t` to find out)
5. Run
			```
				npm link @flagbit/n8n-nodes-akeneo
			```
6. To start n8n Run
			```
				n8n start
			```

## Develop locally

You will need pm2 (`npm i pm2 -g`)

We use pm2 as it makes stopping n8n easier, otherwise you need to look up process ids etc. Also, it is cool.

Start n8n using pm2: `pm2 start n8n`

When you need to rebuild use: `npm run exp`

This will trigger the akeneo node compilation, then restart the local n8n instance.

When you have finished, you can use pm to stop n8n: `pm2 stop n8n`

> You can use `pm2 log n8n` to see your local port number. Knowing this makes it easier to find the local site, or find out why it doesn't work

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

