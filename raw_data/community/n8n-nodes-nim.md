[n8n](https://n8n.io/) is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments. With __n8n-nodes-nim__, you can now  interact with NVIDIA NIM models in n8n.

### Example agent workflow using NIM Chat Model node

![NIM Chat Node](https://i.ibb.co/DDrnrfjz/nim-chat-demo.png)

## Prerequisite

You will need to get an API Key from https://build.nvidia.com.

## Installing NVIDIA NIM node

### From GUI
In n8n, go to Settings -> Community nodes -> Install community node

The package name is `n8n-nodes-nim`.

Read [how to install community nodes](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/#install-a-community-node).

### From source
You will need to install n8n following this guide from https://docs.n8n.io/hosting/installation/npm/. We will be using npm method.
Make sure npm and n8n is installed following the above guide. Clone this repository into a local directory. In your cloned directory, run this command to install the dependencies:

```
npm i
npm run build
npm link
```

Then create a ~/.n8n/custom directory. In ~/.n8n/custom, run:

```
npm link <node_name>
```

`<node_name>` is the name of the package in package.json.

Finally, start n8n by running the command below:

```
n8n start
```

Open n8n in your browser. Search for 'NIM' in the nodes panel and you should see the NIM node.

See [n8n documentation](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) on how to run node locally.
