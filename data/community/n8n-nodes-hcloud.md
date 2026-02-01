# n8n-nodes-hcloud

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is a fork of [n8n-nodes-hetznercloud](https://www.npmjs.com/package/n8n-nodes-hetznercloud), as the developer seems to have abandoned the project. I wanted to also be able to enable backup for Hetzner Cloud machines, therefore forked it - and here it is. :-)

The Node is available at [https://www.npmjs.com/package/n8n-nodes-hcloud](https://www.npmjs.com/package/n8n-nodes-hcloud)

## Additional Features
- Enable / Disable server backup
- Change server protection setting
- Get info about datacenters like available VM types and prices of VMs

## About this node

This node allows you to automate various tasks with the German infrastructure provider Hetzner. With this node, you can automatically start or stop servers, create or delete snapshots, and perform many other actions to manage your Hetzner Cloud infrastructure efficiently.

## How to use Hetzner in n8n

Currently, n8n is not shipped with this Hetzner Cloud API node. Therefore an installation of the community module is required.

### Installation of this community node

1. Open your n8n server.
1. Go to **Settings > Community Nodes**.
1. Select **Install**.
1. Enter `n8n-nodes-hcloud` in **Enter npm package name**.
1. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
1. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

## Local development

Read more at https://docs.n8n.io/integrations/creating-nodes/build/declarative-style-node/#test-your-node.

Here is the summary:

1. Install n8n globally on your PC with `npm install n8n -g`
2. Clone or download this repository and save it anywhere
3. In this downloaded folder run:

```bash
npm install
npm run build
npm link
```

4. Now install this node in your local n8n instance

```bash
cd ~/.n8n/nodes
npm link n8n-nodes-hcloud
```

5. Start the local development area. You need two consoles:

```bash
# in the node directory execute this, that after every change the dist directory is updated
npm run dev
n8n start
```
