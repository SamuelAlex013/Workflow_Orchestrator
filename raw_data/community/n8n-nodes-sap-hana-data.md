# n8n-nodes-sap-hana-data

This is an n8n community node for reading data from SAP HANA databases and HDI containers.

## Features

- Connect to SAP HANA Cloud HDI containers
- Connect to regular SAP HANA databases
- Read all records from tables
- Filter records with WHERE conditions
- Specify columns to retrieve
- Sort and limit results
- Flexible output formats

## Installation

**⚠️ Important**: This node is designed for **self-hosted n8n** installations only. It cannot be used with n8n Cloud due to dependency requirements.

### Option 1: npm Installation (Recommended)

1. Navigate to your n8n installation directory
2. Install the package:
   ```bash
   npm install n8n-nodes-sap-hana-data
   ```
3. Restart your n8n instance

### Option 2: Development Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/pondev1/n8n-nodes-sap-hana-data.git
   cd n8n-nodes-sap-hana-data
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the node:
   ```bash
   npm run build
   ```

4. Link the package locally:
   ```bash
   npm pack
   cd ~/.n8n
   npm install "C:\path\to\n8n-nodes-sap-ai-core\n8n-nodes-sap-hana-data-1.0.0.tgz"
   ```

5. Restart your n8n instance

After installing the node, you can use it like any other node in n8n.

## Configuration

### Credentials

1. Create new credentials of type "SAP HANA API"
2. Choose connection type:
   - **HDI Container**: Use service key credentials from SAP BTP
   - **Database**: Use direct database connection details
3. Fill in the connection details:
   - **Host**: Database hostname (from service key "host" field)
   - **Port**: Database port (from service key "port" field, typically 443 for HANA Cloud)
   - **Username**: Database username (from service key "user" field)
     - Use **_DT** suffix user for design-time operations (creating/modifying database objects)
     - Use **_RT** suffix user for runtime operations (reading data, SELECT queries) - **Recommended for this node**
   - **Password**: Database password (from service key "password" field)
   - **Database**: Database name (from service key "database" field, optional)
   - **Schema**: Schema name (from service key "schema" field or your specific schema) 

### Node Usage

1. Add "SAP HANA Data" node to your workflow
2. Select your credentials
3. Choose operation:
   - **Get All Records**: Retrieve all records from a table
   - **Get Records with Filter**: Retrieve records with WHERE conditions
4. Configure table name and options
5. Execute the node

## Operations

### Get All Records
- Retrieves all records from specified table
- Optional column selection
- Optional sorting and limiting

### Get Records with Filter
- Retrieves records matching WHERE condition
- All features from "Get All Records"
- Flexible WHERE clause support

## Examples

### Basic Usage
```
Table Name: CUSTOMERS
Limit: 100
```

### With Filtering
```
Table Name: ORDERS
WHERE Condition: STATUS = 'COMPLETED' AND ORDER_DATE > '2024-01-01'
Limit: 50
```

### Custom Columns
```
Table Name: PRODUCTS
Columns: ID, NAME, PRICE, CATEGORY
Order By: PRICE DESC
```

## Requirements

- n8n version 0.87.0 or later
- Access to SAP HANA database or HDI container
- Appropriate database permissions for SELECT operations

## Sample Workflows

Ready-to-use n8n workflow examples are available in the `workflows/` directory:

### 1. Get Data from SAP HANA DB Tables Workflow
**File**: [`workflows/Get Data from SAP Hana DB tables.json`](./workflows/Get%20Data%20from%20SAP%20Hana%20DB%20tables.json)

Comprehensive workflow demonstrating data retrieval from SAP HANA database tables with various query options and data processing capabilities.

**Features**:
- Table data retrieval with filtering
- Column selection and sorting
- Result limiting and pagination
- Data transformation and processing
- Error handling and validation

### How to Use Sample Workflows

1. Download the desired workflow JSON file
2. In n8n, go to **Workflows** > **Import from File**
3. Select the downloaded JSON file
4. Configure your SAP HANA credentials (use _RT user for read operations)
5. Update table names to match your database schema
6. Customize WHERE conditions and column names as needed
7. Activate and test the workflow

## Support

For issues and feature requests, please create an issue in the GitHub repository.

## License

MIT License