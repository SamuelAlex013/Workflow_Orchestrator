![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-greenapi

The node allows integration with Green API for sending WhatsApp messages and listening to incoming webhooks.

It provides the following resources:

- **Messages**: send text messages, media messages, polls, and button messages  
- **Journals**: retrieve the history of incoming and outgoing messages, as well as chat history  
- **Contacts**: get the list of contacts, group participants, and check if a phone number is registered on WhatsApp  
- **Trigger**: listen to incoming webhooks with advanced filters  

## More information

- Please refer to the GREEN-API documentation at [https://green-api.com/en/docs/](https://green-api.com/en/docs/)

- To connect an instance, it must be authorized. You can authorize the instance in your Green-API console

- To enable triggers, specify *WEBHOOK_URL* in the .env file

- If you notice any issues with the integration, please report them to Green-API support

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
