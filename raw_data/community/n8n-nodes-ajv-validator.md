![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-ajv-validator

This is a custom n8n node that validates JSON data against a schema. It can be used in n8n workflows to ensure that the data being processed meets specific requirements.

## Features
- Validate JSON data against a schema
- Ajv validation library for schema validation

* Install node with:
  ```
  npm install n8n-nodes-ajv-validator
  ```
## Usage
1. Add the node to your n8n workflow.
2. Configure the node with the JSON data you want to validate and the schema against which you want to validate it.
3. Run the workflow to see if the JSON data is valid according to the schema.
4. If the data is valid, the node will output the data. If it is invalid, it will throw an error with details about the validation failure.
5. You can use the output of this node in subsequent nodes in your workflow to process only valid data.

## Example json schema
```json
{
	"type": "object",
	"properties": {
		"name": {
			"type": "string"
		},
		"age": {
			"type": "integer",
			"minimum": 0
		}
	},
	"required": ["name", "age"]
}
```

## References
- [JSON Schema](https://json-schema.org/)
- [Ajv Documentation](https://ajv.js.org/)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
