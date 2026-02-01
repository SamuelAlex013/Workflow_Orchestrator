# n8n-nodes-what3words

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

[n8n](https://www.n8n.io) "simple" state machine is storing your nodes/workflow state globally or workflow level

## What is the what3words?

What3words is a geocoding system that assigns a unique combination of three words to each 3-meter square area on the Earth's surface. It aims to provide a more human-friendly, easy-to-remember, and accurate way of sharing locations, especially in areas without clear addresses or where traditional navigation systems may be less effective

## How to install

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-what3words` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

### Manual installation

To get started install the package in your n8n root directory:

`npm install n8n-nodes-what3words`

For Docker-based deployments, add the following line before the font installation command in your [n8n Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile):

`RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-what3words`

### How to use

- You need to register a [what3words](https://what3words.com) account
- You need to go the [developer page](https://accounts.what3words.com/create-api-key?referrer=/public-api)
- You need to create an API key


## Demo
![Nodes](https://raw.githubusercontent.com/pigri/n8n-nodes-what3words/master/assets/nodes.png)

![Cordinates to What3words](https://raw.githubusercontent.com/pigri/n8n-nodes-what3words/master/assets/cordinates_to_what3words.png)

![What3words to Cordinates](https://raw.githubusercontent.com/pigri/n8n-nodes-what3words/master/assets/what3words_to_cordinates.png)

## Errors

If you have any error, please open an issue on [Github](https://github.com/pigri/n8n-nodes-what3words)
