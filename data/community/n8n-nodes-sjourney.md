![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-automatic1111

This [n8n](https://n8n.io) integration was create for the [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) project. It provides a way to automate generation of images from text (Text to Image) and images (Image to Image). It also provides a way to easily set which model to use from what is available (automatically creates a list of available models). More functionality will be added as needed. 

# Installation and Development
You can install this npm package through the [GUI](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/) or [manually](https://docs.n8n.io/integrations/community-nodes/installation/manual-install/) using `@xzcutable/n8n-nodes-automatic1111` in the GUI or run the command `npm install @xzcutable/n8n-nodes-automatic1111` manually.

### If installed correctly, the node should show up as any other node. You will need to create a credential like any other node and point to an instance of Automatic1111.
![alt text](<previews/setup credential.png>)

### Generated images are returned in Base64 strings and can be previewed with `Convert to File` node. Note: `Convert to File` doesn't support expressions and the fixed expression needs to be the name of the base64 string key.
![alt text](<previews/c2f example.png>)

### Multiple images output is supported, but you'll need to attach it to a `Split` node. With the fields to split being `images`.
![alt text](previews/Usage.png)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
