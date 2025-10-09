# n8n-nodes-opencnpj

This is an n8n community node that allows you to consult Brazilian company data by CNPJ using the OpenCNPJ API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Company
- **Get**: Retrieve Brazilian company data by CNPJ with automatic validation

## Credentials

This node doesn't require any credentials. The OpenCNPJ API is free and doesn't require authentication.

## Compatibility

- Minimum n8n version: 0.175.0
- Tested with n8n version: 1.113.3

## Usage

1. Add the OpenCNPJ node to your workflow
2. Select the "Company" resource
3. Choose the "Get" operation
4. Enter a valid Brazilian CNPJ (14 digits, with or without punctuation)
5. Optionally enable "Simplify" to get a cleaner output with the most important fields

### Features

- **CNPJ Validation**: Automatically validates CNPJ format and check digits before making API requests
- **Multiple Formats**: Accepts CNPJ with or without punctuation
- **Error Handling**: Clear error messages with guidance on how to fix issues
- **Simplified Output**: Option to return only the most important company information
- **Batch Processing**: Supports processing multiple CNPJs from previous nodes

### Example CNPJ
You can test with this example CNPJ: `11222333000181`

### Supported CNPJ formats
- Numbers only: `11222333000181`
- With full punctuation: `11.222.333/0001-81`
- Partial punctuation: `11.222.333/000181`

### Output Fields (Simplified Mode)
When "Simplify" is enabled, the node returns only the most relevant fields:
- Company name (razao_social)
- Trade name (nome_fantasia)
- Registration status (situacao_cadastral)
- Company size (porte)
- Legal nature (natureza_juridica)
- Share capital (capital_social)
- Complete address
- Phone and email
- Main activity
- Start date

### Error Handling
The node provides clear error messages for common issues:
- Invalid CNPJ format or check digits
- Company not found (404)
- API rate limiting (429)
- Network or API errors

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [OpenCNPJ API documentation](https://api.opencnpj.org/)
* [OpenCNPJ website](https://opencnpj.org/)

## License

[MIT](LICENSE.md)
