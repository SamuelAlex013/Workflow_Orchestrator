![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

### n8n-nodes-yandex-embeddings
This is an n8n community node. It lets you use app/service name in your n8n workflows. Node for using Yandex model embeddings.

Installation
Follow the installation [guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Also pay attention to Environment Variables for using tools in AI Agents. It's mandatory to set the N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE environment variable to true if you want to use the Yandex Embeddings node as a tool in AI Agents.
Operations
### Credentials
To use, you need to get authentication data, follow the auth [guide](https://yandex.cloud/ru/docs/foundation-models/api-ref/authentication):

```bash
folderId
apiKey
```

## License

You can find the license information [here](https://github.com/mkremnev/n8n-nodes-yandex-embeddings/blob/master/LICENSE.md)
