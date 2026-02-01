# n8n-nodes-amazon-bedrock-knowledge-bases

This is an n8n community node. It lets you use Amazon Bedrock Knowledge Bases in your n8n workflows.

Amazon Bedrock Knowledge Bases is a service that allows you to build applications that can retrieve information from your knowledge base using natural language queries. This node provides essential functionality to query knowledge bases and retrieve relevant information.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Alternatively, you can install directly via npm:

```bash
npm install n8n-nodes-amazon-bedrock-knowledge-bases
```

## Operations

### Retrieve

Execute queries against Amazon Bedrock Knowledge Bases to retrieve relevant information based on natural language queries.

**Parameters:**
- **Knowledge Base Name or ID** (required): Select from the dynamically loaded list or specify an ID manually
- **Query** (required): Natural language query to search in the knowledge base
- **Max Results**: Maximum number of results to return (1-100, default: 10)

**Features:**
- Dynamic knowledge base selection
- Essential Retrieve command parameters only
- Automatic credential validation
- Support for both normal node and tool usage

## Credentials

To use this node, you need to authenticate with Amazon Bedrock using AWS credentials.

### Prerequisites

1. An AWS account with access to Amazon Bedrock
2. A knowledge base created in Amazon Bedrock
3. AWS IAM user with appropriate permissions

### Authentication Setup

Configure the following credentials in n8n:

1. **AWS Region**: Select the region where your knowledge base is available
2. **Access Key ID**: Your AWS access key
3. **Secret Access Key**: Your AWS secret access key
4. **Session Token** (optional): Session token for temporary credentials

### Obtaining AWS Credentials

1. Access the AWS IAM console
2. Create a user or use an existing one
3. Attach the `AmazonBedrockFullAccess` policy or create a custom policy
4. Generate access keys (Access Key ID and Secret Access Key)
5. Use these credentials in n8n

### Required IAM Permissions

Your AWS account must have the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:Retrieve",
                "bedrock:ListKnowledgeBases",
                "bedrock:ListFoundationModels"
            ],
            "Resource": "arn:aws:bedrock:*:*:knowledge-base/*"
        }
    ]
}
```

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with n8n versions**: 1.0.0+
- **Node.js version**: >= 20.15

## Usage

### Basic Usage

Add the "Amazon Bedrock Knowledge Base" node to your workflow and configure:

- **Knowledge Base Name or ID** (required): Select from the dynamically loaded list or enter the knowledge base ID manually
- **Query** (required): Natural language query to search in the knowledge base
- **Max Results**: Maximum number of results to return (1-100, default: 10)

### Knowledge Base Selection

The node automatically loads and lists all available knowledge bases in your AWS account. You can:
- **Select from list**: Choose a knowledge base from the dropdown list (loaded automatically)
- **Enter ID manually**: Use an expression to specify a specific ID

**Note**: The knowledge base list is loaded dynamically when you open the dropdown, using your configured AWS credentials.

### Using as a Tool

The node can also be used as a tool in n8n workflows, allowing more flexible integration with other nodes.

### Example Workflow

```javascript
{
  "nodes": [
    {
      "name": "Amazon Bedrock Knowledge Base",
      "type": "n8n-nodes-amazon-bedrock-knowledge-bases.amazonBedrockKnowledgeBase",
      "parameters": {
        "knowledgeBaseId": "YOUR_KNOWLEDGE_BASE_ID",
        "query": "How to configure authentication?",
        "maxResults": 5
      },
      "credentials": {
        "amazonBedrockCredentialsApi": "YOUR_CREDENTIALS_ID"
      }
    }
  ]
}
```

### Response Structure

The node returns a JSON object with the following structure:

```json
{
  "retrievalResults": [
    {
      "content": {
        "text": "Retrieved document content"
      },
      "location": {
        "type": "S3",
        "uri": "s3://bucket-name/path/to/document.pdf"
      },
      "score": 0.95,
      "metadata": {
        "source": "document.pdf",
        "page": "10"
      }
    }
  ],
  "nextToken": "token-for-next-page"
}
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
* [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
* [Creating Custom Nodes in n8n](https://docs.n8n.io/integrations/creating-nodes/)

## Version history

### 0.1.0

Initial release with essential Amazon Bedrock Knowledge Base functionality:

- **Retrieve operation**: Query knowledge bases with natural language
- **Dynamic knowledge base selection**: Automatically loads available knowledge bases
- **AWS credentials support**: Traditional AWS authentication (Access Key ID, Secret Access Key, Session Token)
- **Essential parameters only**: Simplified configuration with core Retrieve command parameters
- **Tool support**: Can be used as both normal node and tool in n8n workflows
- **Automatic validation**: Credentials are validated when loading knowledge bases

### Troubleshooting

#### Common Error Messages

The node provides detailed error messages to help with troubleshooting:

- **"Invalid AWS credentials"**: Verify that Access Key ID and Secret Access Key are correct
- **"Insufficient permissions"**: Ensure the IAM user has the necessary permissions
- **"Access denied (403)"**: Check IAM permissions for Amazon Bedrock
- **"Unauthorized (401)"**: Verify that credentials are correct
- **"IAM user not found"**: Check if Access Key ID is correct
- **"Invalid signature"**: Verify that Secret Access Key is correct
- **"Session token expired"**: Generate a new session token

#### Credential Validation

**Important**: Credential validation is done automatically when you load the knowledge base list. If you see "Invalid URL" when saving credentials, this is normal - the real validation happens when the knowledge base dropdown is loaded.

#### Dynamic Knowledge Base Loading

If the knowledge base list doesn't load in the dropdown:

1. **Check credentials**: Ensure AWS credentials are configured correctly
2. **Check permissions**: IAM user must have `bedrock:ListKnowledgeBases` permission
3. **Check region**: Ensure the selected region supports Amazon Bedrock Agent
4. **Fallback**: If the list doesn't load, you can manually enter the knowledge base ID

## License

MIT

## Author

Alex Ribeiro - [alexribeirodev.com](https://alexribeirodev.com)
