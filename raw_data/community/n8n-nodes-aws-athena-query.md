# n8n-nodes-aws-athena-query

This is an n8n community node. It lets you execute SQL queries on AWS Athena in your n8n workflows.

AWS Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. With this node, you can run SQL queries against your data lake and incorporate the results into your n8n workflows.

**Key Features:**
- ✅ **Zero external dependencies** - Uses native HTTP requests with AWS Signature V4 authentication
- ✅ **Lightweight and fast** - No heavy SDK dependencies
- ✅ **Full Athena API support** - Direct integration with AWS Athena REST API
- ✅ **Handles large result sets** - Automatic pagination of results; optional configurable row limit

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install the package in your n8n root folder:

```bash
npm install n8n-nodes-aws-athena-query
```

## Operations

The AWS Athena Query node supports the following operations:

### Query Execution
- **Execute SQL Query**: Run SQL queries against your AWS Athena database
  - Supports SELECT statements for all table formats
  - Supports CREATE, INSERT, UPDATE, DELETE, MERGE INTO statements for Apache Iceberg tables only
  - Built-in SQL editor with syntax highlighting
  - Configurable query timeout
  - Results returned in structured JSON format

## Credentials

You need to authenticate with AWS to use this node. Set up AWS credentials with the following permissions:

### Prerequisites
1. An AWS account with access to Athena
2. An S3 bucket for query results storage
3. Proper IAM permissions

### Required AWS Permissions
Your AWS credentials need to contain at least the following IAM permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "glue:GetDatabase",
                "glue:GetTable",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}
```

### Setting up Credentials in n8n
1. Go to **Credentials** in your n8n instance
2. Click **Add Credential**
3. Select **AWS** from the list
4. Enter your AWS credentials:
   - **Access Key ID**: Your AWS access key
   - **Secret Access Key**: Your AWS secret key
   - **Session Token**: (Optional) For temporary credentials

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with n8n versions**: 1.0.0+
- **Implementation**: Native HTTP requests with AWS Signature V4 authentication (no external dependencies)

## Usage

### Basic Query Example
1. Add the **AWS Athena Query** node to your workflow
2. Configure the following parameters:
   - **Region**: Your AWS region (e.g., `us-east-1`)
   - **Database Name**: Your Athena database (optional)
   - **SQL Query**: Your SQL query
   - **S3 Output Location**: S3 path for results (e.g., `s3://my-bucket/athena-results/`)
   - **Query Timeout**: Maximum wait time in seconds (default: 300)

### Sample SQL Query
```sql
SELECT 
    customer_id,
    product_name,
    purchase_date,
    amount
FROM sales_data 
WHERE purchase_date >= '2024-01-01'
ORDER BY purchase_date DESC
LIMIT 100
```

### Important Note on Query Types
- **SELECT queries**: Work with all table formats (Parquet, CSV, JSON, ORC, etc.)
- **INSERT/UPDATE/DELETE/MERGE**: Only work with **Apache Iceberg tables**
- For regular tables, AWS Athena is primarily a read-only query service
- If you need to modify data, consider using Apache Iceberg table format

### Output Format
The node returns results in the following structure:
```json
{
  "queryExecutionId": "abc123-def456-ghi789",
  "rowCount": 25,
  "columns": ["customer_id", "product_name", "purchase_date", "amount"],
  "results": [
    {
      "customer_id": "12345",
      "product_name": "Widget A",
      "purchase_date": "2024-01-15",
      "amount": "29.99"
    }
  ]
}
```

### Advanced Usage Tips
- **Large Result Sets**: Results are paginated automatically (1000 rows per page, header on first page). Use the new
  **Max Rows Returned** option to cap total rows without changing your SQL.
- **Partitioned Tables**: Use partition predicates to improve query performance
- **Cost Optimization**: Monitor your query costs in AWS Cost Explorer
- **Data Types**: All values are returned as strings; use n8n's data transformation features to convert types as needed

### Error Handling
The node handles common errors gracefully:
- Query timeout errors
- AWS permission issues
- Invalid SQL syntax
- S3 access problems

Enable "Continue on Fail" in the node settings to handle errors in your workflow logic.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [AWS Athena Documentation](https://docs.aws.amazon.com/athena/)
* [AWS Athena API Reference](https://docs.aws.amazon.com/athena/latest/APIReference/)
* [AWS Athena SQL Reference](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html)