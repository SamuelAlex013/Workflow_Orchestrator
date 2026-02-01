# n8n-nodes-defang

![](https://raw.githubusercontent.com/pemontto/n8n-nodes-defang/main/images/workflow.png)

n8n node to defang and refang IOCs like IPs, Domains, and URLs.

Based on the amazing work of [ninoseki](https://github.com/ninoseki) with [fanger](https://www.npmjs.com/package/fanger).

## How to install

To get started install the package in your n8n root directory:

`npm install n8n-nodes-defang`

For Docker-based deployments, add the following line before the font installation command in your [n8n Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile):

`RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-defang`

## License

[MIT](https://github.com/pemontto/n8n-nodes-defang/blob/master/LICENSE.md)
