# n8n-nodes-yup-data-validator

This is an n8n community node. It lets you use [Yup](https://github.com/jquense/yup) for data validation in your n8n workflows by providing a JSON schema.

This node uses [schema-to-yup](https://www.npmjs.com/package/schema-to-yup) to convert a JSON schema into a Yup schema for powerful validation.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node provides a `validate` operation that allows you to define a set of validation rules against your input data using JSON schema.

## Compatibility

This node was developed against n8n version 1.x.

## Usage

This node is designed to validate incoming data against a JSON schema. You can configure multiple validation rules.

For each validation rule, you need to provide:

*   **Field Value**: The value from your input data that you want to validate. You can use n8n expressions here. To validate the entire JSON object of an item, you can use `{{$json}}`.
*   **Validation Schema**: A JSON schema object that defines the validation rules.

**Example:**

If you have an input item with the following JSON:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30
}
```

You could set up a validation rule to validate the entire object:

*   **Field Value**: `{{$json}}`
*   **Validation Schema**:
    ```json
    {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "minLength": 3
        },
        "email": {
          "type": "string",
          "format": "email"
        },
        "age": {
          "type": "number",
          "minimum": 18
        }
      },
      "required": ["name", "email", "age"]
    }
    ```

If the validation fails for an item, the node will either stop the workflow and throw an error, or if "Continue on Fail" is enabled, it will output an item with an `error` property containing the validation error message.

## Resources

*   [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
*   [Yup Documentation](https://github.com/jquense/yup)
*   [schema-to-yup Documentation](https://www.npmjs.com/package/schema-to-yup)
