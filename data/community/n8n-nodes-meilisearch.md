# n8n-nodes-meilisearch

This is an n8n community node. It lets you use the meilisearch REST API in your n8n workflows.

[Meilisearch](https://meilisearch.com) 
An open-source, lightning-fast, and hyper-relevant search engine that fits effortlessly into your apps, websites, and workflow.

[meilisearch API Docs](https://docs.meilisearch.com/reference/api/overview.html)

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

## Operations

-  Documents
   -  Add or replace documents
   -  Add or update documents
   -  Delete batch of documents by UID
   -  Delete all documents in an index
   -  Get documents
   -  Get one document by UID
-  General
   -  Create a dump
   -  Get all index stats
   -  Get health
   -  Get version information
-  Indexes
   -  Create an index
   -  Get stats of an index
   -  List indexes
   -  Search index
   -  Swap indexes
-  Keys
   -  Create a new key
   -  Delete a key by its uid or key
   -  Get a single key by its uid or key
   -  Get many api keys
   -  Update a key by its uid or key
-  Search
   -  Search an index (Also found in indexes section)
-  Settings
   -  Get the settings of an index
   -  Reset the settings of an index
   -  Update the settings of an index
-  Tasks
   -  Cancel tasks
   -  Delete tasks
   -  Get all tasks
   -  Get one task by UID

## Credentials

By [providing Meilisearch with a master key at launch](https://docs.meilisearch.com/learn/security/master_api_keys.html#protecting-a-meilisearch-instance), you protect your instance from unauthorized requests. The provided master key must be at least 16 bytes. From then on, you must include the `Authorization` header along with a valid API key to access protected routes (all routes except /health.)

The credentials type provided in this node send an `Authorization` header with the key you provide. e.g. `Authorization: Bearer YOURKEY`

## Compatibility

This is subject to change.

## Usage

Use as you would any node- I tried to include useful descriptions and hints for all fields.

## Updating

If you depend soley on the community nodes part of the GUI, you can update there.

If you use a dockerfile setup such as one of mine: [SimpleDockerfileExample](https://github.com/Bwilliamson55/n8n-custom-images/blob/master/bwill-nodes-simple/Dockerfile) , you can rebuild your container to get the updated node version.

---

### *If you're using `docker compose` or `docker-compose`, you can still use a dockerfile to persist custom nodes:*

Put the `DockerFile` and `docker-entrypoint` in the same directory as your docker-compose file, and swap the `image` property for `build: .`

 Then run `docker-compose down && docker-compose up --build -d`.

 Or if you want to have less down time, run `docker-compose build` to create the image, THEN do `docker-compose down && docker-compose up --force-recreate -d` - [Source Docs](https://docs.docker.com/compose/compose-file/build/#dockerfile)

 If you're on Digital Ocean or similar, "Force rebuild and redeploy".

`Dockerfile`:
    ***Note the `-g` - these nodes will not show in 'community nodes' but will work and show when searched for***
```yaml
FROM n8nio/n8n:latest
RUN npm install -g n8n-nodes-meilisearch
```
`docker-entrypoint.sh`:  (Default one from n8n repo)
```shell
#!/bin/sh

if [ -d /root/.n8n ] ; then
  chmod o+rx /root
  chown -R node /root/.n8n
  ln -s /root/.n8n /home/node/
fi

chown -R node /home/node

if [ "$#" -gt 0 ]; then
  # Got started with arguments
  exec su-exec node "$@"
else
  # Got started without arguments
  exec su-exec node n8n
fi
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [n8n-nodes-meilisearch repository](https://github.com/Bwilliamson55/n8n-nodes-meilisearch)
* [Official Meilisearch API Reference](https://www.meilisearch.com/docs/reference/api/overview)
* [Official Meilisearch Docs](https://www.meilisearch.com/docs/learn/what_is_meilisearch/overview)

## Version history

- 0.1.0 - Initial release
  - Almost all API endpoints accounted for in node operations
    - TODO: 
      - multi-search, 
      - index settings sub-routes, 
      - (Done in 0.1.1) auto-populating options where possible
        - Due to the very dynamic permissions, getting options has a high chance of failure. For MVP I opted to skip loading options dynamically, such as index names. 
    - Currently index settings can be interacted with, but as the entire settings object for each index
- 0.1.1 - QOL Updates
  - When adding or updating documents, the "Documents JSON" field is now far more forgiving. Very broken JSON will throw an error before sending as well.
  - Some array type input fields are now also validated and transformed as JSON
	- UID fields will be a dropdown when credentials have the proper permissions
