# n8n Node - ViaCep

This is a custom n8n node for interacting with the ViaCep API, which provides information about Brazilian postal codes (CEP). It allows you to fetch data like street names, neighborhoods, cities, states, and other relevant postal information.

## Installation

To use this node in your n8n setup, follow these steps:

### 1. Install via n8n

You can install the ViaCep node directly from the n8n community nodes repository. Follow the instructions in the [n8n documentation](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/#install-a-community-node) to add custom nodes to your n8n instance.

### 2. Add Custom Node to Your n8n Workflow

Once installed, you can add the ViaCep node to your workflow by searching for Via Cep in the nodes menu inside n8n.

Configuration
Properties
The ViaCep node accepts the following properties:

Cep (cep): (required) The Brazilian postal code (CEP) to search for. You can use either the full format (xxxxx-xxx) or the non-hyphenated format (xxxxxxxx).

Additional Fields (additionalFields): These additional fields allow you to specify extra options for the response format.

Format Response (formatResponse): Choose the format of the response. Available options are:

JSON: Return the response in JSON format.

XML: Return the response in XML format.

Example:
To query a postal code, for example 01001-000 (São Paulo), you need to specify the postal code as follows:

```json
{
	"cep": "58052-070",
	"additionalFields": {
		"formatResponse": "json"
	}
}
```

### Example Usage
Drag and Drop the Via Cep node into your workflow.

Set the Cep field with the postal code you want to query (e.g., 01001-000).

Optionally, specify the response format (JSON or XML).

Connect the node to other nodes in your workflow to process the data returned by ViaCep API.

### Authentication
No authentication is required for using this node as ViaCep API is publicly accessible.

Response Format
Depending on the value of the Format Response field, the node will return either JSON or XML formatted data. Here's an example of the JSON response for the postal code 01001-000:

```json
{
	"cep": "58052-070",
	"logradouro": "Rua das Castanholas",
	"complemento": "",
	"unidade": "",
	"bairro": "Anatólia",
	"localidade": "João Pessoa",
	"uf": "PB",
	"estado": "Paraíba",
	"regiao": "Nordeste",
	"ibge": "2507507",
	"gia": "",
	"ddd": "83",
	"siafi": "2051"
}
```
