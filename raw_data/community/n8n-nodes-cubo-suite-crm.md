🧩 n8n-nodes-cubo-suite-crm
Integration node for Cubo Suite CRM to automate business workflows in n8n
📌 Overview
Full integration with the Cubo Suite CRM API for managing deals directly within n8n.
🚀 Features

✅ Create new deals
🔄 Update existing deals
🔐 Authentication via API Key
🏷️ Support for custom fields
⚡ Real-time synchronization

📦 Installation
Via Command Line:
npm install n8n-nodes-cubo-suite-crm

Via n8n Interface:

Go to Settings > Community Nodes
Click Install community node
Search for n8n-nodes-cubo-suite-crm
Click Install

🔑 Authentication

In Credentials, select Cubo CRM API
Enter your API Key (found in the Cubo Suite CRM dashboard)
Configure the required parameters:

Example Payload
{
  "title": "string",
  "price": "string",
  "userId": 0,
  "peopleName": "string",
  "peoplePhone": "string",
  "organizationName": "string",
  "stageId": 0,
  "pipeId": 0,
  "rating": 0,
  "products": [
    {
      "productId": 0,
      "quantity": 0,
      "price": "string"
    }
  ],
  "customfields": [
    {
      "customfieldId": 0,
      "value": "string"
    }
  ]
}

📄 License
MIT - https://cubosuite.com.br/