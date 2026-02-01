## How to Use

To use the Pickaxe n8n node, you first need to set up your environment on [pickaxe.co](https://pickaxe.co). This involves creating an account, setting up a Studio, and creating your Pickaxes (your AI tools). Once your Pickaxes are ready, you can integrate them with your n8n workflows.

### 1. Create a Pickaxe Account

First, you'll need to create an account on Pickaxe. You can sign up on their website to get started.

### 2. Create a Studio

After creating your account, you'll need to set up a Studio. A Studio acts as a container for your AI tools (Pickaxes). To create a new Studio, navigate to the "Studio" section in the Pickaxe navigation bar. Give your Studio a name and a description. You can also configure settings for your Studio, such as making it public or invite-only.

### 3. Create Pickaxes

Once you have a Studio, you can start creating Pickaxes. A Pickaxe is an AI tool, which can be a chatbot or a form, that you build using prompts. You can create new Pickaxes within your Studio. In the Pickaxe builder, you can write prompts, select the AI model you want to use, and configure other settings for your tool.

### 4. Using n8n Actions

To connect your Pickaxes to n8n, you will use Pickaxe's "Actions" feature. Actions allow you to connect your Pickaxe to external software and APIs.

While Pickaxe offers pre-built Actions, for n8n you will likely use a generic webhook or a custom action to send data from your Pickaxe to your n8n workflow. You can also trigger your Pickaxes from other platforms via the Pickaxe API.

### Credentials and API Usage

To connect Pickaxe with n8n, you will need to create Pickaxe OAuth2 API credentials by connecting your Pickaxe account. 

If you need to know more about Pickaxe API please refer to this [documentation](https://pickaxe.co/user/documentation)

***


## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
