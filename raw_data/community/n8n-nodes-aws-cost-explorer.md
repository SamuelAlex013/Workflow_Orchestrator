# n8n-nodes-aws-cost-explorer

This is an n8n community node that lets you retrieve cost and usage data from AWS Cost Explorer in your n8n workflows.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

To install via n8n settings:
1. Go to Settings > Community Nodes
2. Click "Install Community Node"
3. Enter `n8n-nodes-aws-cost-explorer`
4. Click Install

## Prerequisites

You need:
- AWS account with Cost Explorer enabled
- AWS IAM user/role with Cost Explorer permissions
- AWS Access Key ID and Secret Access Key

## Credentials

This node requires AWS Cost Explorer API credentials:
- **AWS Access Key ID**: Your AWS access key
- **AWS Secret Access Key**: Your AWS secret key
- **Region**: AWS region (usually us-east-1 for Cost Explorer)

Required IAM permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ce:GetCostAndUsage",
                "ce:GetDimensionValues"
            ],
            "Resource": "*"
        }
    ]
}
```

## Operations

### Cost and Usage
- **Get**: Retrieve cost and usage data for a specified time period

### Dimension Values  
- **Get**: Get available values for AWS cost dimensions (Service, Account, Instance Type, Region)

## Usage Example

1. Add AWS Cost Explorer node to your workflow
2. Configure credentials
3. Select "Cost and Usage" > "Get"
4. Set start/end dates (YYYY-MM-DD format)
5. Choose granularity (Daily/Monthly/Hourly)
6. Select metrics (Blended Cost, Unblended Cost, Usage Quantity)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md) 