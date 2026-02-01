![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-arcblock

This repo contains nodes to help you automate apps run on the ArcBlock Blocklet platform.

- [Blocklet Server](nodes/BlockletServer/BlockletServer.node.ts)
- [Blocklet Service](nodes/BlockletService/BlockletService.node.ts)
- [Discuss Kit](nodes/DiscussKit/DiscussKit.node.ts)
- [Payment Kit](nodes/PaymentKit/PaymentKit.node.ts)
- [Snap Kit](nodes/SnapKit/SnapKit.node.ts)
- [Media Kit](nodes/MediaKit/MediaKit.node.ts)
- [Vote Kit](nodes/VoteKit/VoteKit.node.ts)

And some util nodes:

- [MarkdownToLexical](nodes/MarkdownToLexical/MarkdownToLexical.node.ts)

## Prerequisites

You need the following installed on your development machine:

- [git](https://git-scm.com/downloads)
- Node.js and pnpm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
- Install n8n with:
  ```
  npm install n8n -g
  ```
- Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
