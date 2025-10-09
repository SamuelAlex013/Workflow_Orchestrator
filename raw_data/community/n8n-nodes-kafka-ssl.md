# n8n-nodes-kafka-ssl

This repo adds support for connecting to a Kafka Cluster with SSL certificates. The code is based on the work of https://github.com/cylabr on this https://github.com/n8n-io/n8n/pull/6398, plus some additional configuration. 

## Setup

Use visual studio code for best experience.

1. Clone this repository.
2. Install node and npm. https://nodejs.org/en/download
3. Install pnpm
```bash
npm i -g pnpm
```
4. Install local package
```bash
pnpm install
```
5. Build n8n
```bash
pnpm run build
```
6. Run n8n in docker mode
7. Configure n8n docker container to use this custom node. Add the following volume for n8n-main service
```yaml
  volumes:
    - ~/n8n-nodes-kafka-ssl/dist:/home/node/.n8n/custom/node_modules/n8n-nodes-kafka-ssl
```

## Development
1. Make changes to nodes or credentials
2. Delete compiled files
```bash
rm -rf dist
```
3. Build packages and n8n
```bash
pnpm run build
```
4. Restart n8n (make sure to be in n8n directory)
```bash
docker compose restart n8n-main
```

## Publishing Package on npm
1. Update version (patch / minor / major)
```bash
npm version patch
```

2. Push version update on git
```bash
git push
```

3. Publish version on npm
```bash
npm publish
```

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
