# n8n-nodes-infranodus

This is an n8n community node from [InfraNodus](https://infranodus.com). It lets you use [InfraNodus GraphRAG API](https://infranodus.com/docs/graph-rag-knowledge-graph) in your n8n workflows.

You can create and use knowledge graphs as experts in your LLM workflows (no OpenAI keys required). InfraNodus can provide information about the main topics and content gaps in any text, so you can use it in your marketing and research workflows.

![InfraNodus graph](https://infranodus.com/images/front/infranodus-overview.jpg)

Video demo: [https://www.youtube.com/watch?v=kS0QTUvcH6E](https://www.youtube.com/watch?v=kS0QTUvcH6E)

You can also use the knowledge graphs to augment and improve your RAG flows with graph-based AI advice about the structure of the knowledge and better quality retrieval without the need to set up complex vector store infrastructures.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### For automatic installation

1. Open the nodes panel at the top right of your n8n editor (+ button)
2. Search for "InfraNodus"
3. Click on the "Install" button

### For manual installation:

You can install this node manually if you're running a local version of n8n.

0. Install the local version of n8n

If you don't have n8n installed yet, you can install it using

- [n8n Docker installer](https://docs.n8n.io/hosting/installation/npm/) (in this case you'll need Docker installed)

```bash
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

- through the command line in your terminal using the [n8n NPX installer](https://docs.n8n.io/hosting/installation/npm/) — for temporarily launching n8n without installing it (in this case, you'll need node version 20 or 22 installed).

```bash
npx n8n
```

- through `npm` [n8n node package](https://docs.n8n.io/hosting/installation/npm/) manager (in this case you install it globally and can launch it from your termainal)

```bash
npm install n8n -g
```

In all cases, your configuration settings will be saved even if you quit at this folder, where you can also install the InfraNodus node:

```bash
cd ~/.n8n
```

1. Launch the local version of n8n

- If it's installed globally:

```bash
n8n start
```

- If it's installed through Docker:

Start the Docker n8n instsance:

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

Then access the Docker shell (terminal entry into your Docker n8n instance):

```bash
docker exec -it n8n sh
```

1. Install the node

Change to the nodes folder:

```bash
cd ~/.n8n/nodes
```

If it doesn't exist, create it first:

```bash
mkdir -p ~/.n8n/nodes
```

2. Install the node into this folder:

```bash
npm install n8n-nodes-infranodus
```

3. Then restart n8n

## Operations

The node supports the following operations:

- Create a knowledge graph
- Get a knowledge graph
- Generate a question based on the content gaps in a knowledge graph
- Prompt a knowledge graph expert

## Credentials

The node requires an API token from InfraNodus. You can get it from [your InfraNodus account](https://infranodus.com/api-access).

We use Bearer authentication in case you want to build your own node using InfraNodus.

## Compatibility

The node is compatible with n8n v0.225.0 and above.

## Usage

To learn more about using InfraNodus with n8n, see our tutorials and videos on the Nodus Labs support portal: [https://support.noduslabs.com/hc/en-us/search?utf8=%E2%9C%93&query=n8n](https://support.noduslabs.com/hc/en-us/search?utf8=%E2%9C%93&query=n8n)

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Nodus Labs support portal](https://support.noduslabs.com/hc/en-us/search?utf8=%E2%9C%93&query=n8n)
- [InfraNodus API endpoints](https://support.noduslabs.com/hc/en-us/articles/13605983537692-InfraNodus-API-Access-Points)

## Version history

v 0.1.0 (2025-09-11)

- Initial release
