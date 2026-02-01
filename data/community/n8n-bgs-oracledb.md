# n8n-bgs-oracledb

This is an n8n community node that lets you use Oracle Database in your n8n workflows.

Oracle Database is a multi-model database management system produced and marketed by Oracle Corporation. It is one of the most popular enterprise databases in the world.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Operations](#operations)
- [Credentials](#credentials)
- [Usage](#usage)
- [Resources](#resources)
- [License](#license)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Local Installation

1. Clone this repository:
```bash
git clone https://github.com/askbgs/n8n-bgs-oracledb.git
cd n8n-bgs-oracledb
```

2. Install dependencies:
```bash
npm install
```

3. Build the node:
```bash
npm run build
```

4. Link the node to n8n:
```bash
npm link
cd /path/to/n8n
npm link n8n-bgs-oracledb
```

5. Start n8n:
```bash
n8n start
```

## Prerequisites

### Oracle Instant Client

This node requires Oracle Instant Client to be installed on your system.

#### Linux/Mac Installation:

1. Download Oracle Instant Client from [Oracle's website](https://www.oracle.com/database/technologies/instant-client/downloads.html)
2. Extract the files to a directory (e.g., `/opt/oracle/instantclient`)
3. Set the library path:
```bash
export LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
```

#### Windows Installation:

1. Download Oracle Instant Client from [Oracle's website](https://www.oracle.com/database/technologies/instant-client/downloads.html)
2. Extract the files to a directory (e.g., `C:\oracle\instantclient`)
3. Add the directory to your PATH environment variable

## Operations

- **Execute Query**: Execute any SQL query with parameter binding support
- **Insert**: Insert rows into a table
- **Update**: Update existing rows in a table
- **Delete**: Delete rows from a table
- **Execute Stored Procedure**: Execute stored procedures with parameters

## Credentials

To connect to your Oracle database, you'll need to configure the following credentials:

- **Host**: The hostname or IP address of your Oracle server
- **Port**: The port number (default: 1521)
- **Service Name**: The Oracle service name (e.g., ORCL)
- **User**: Your database username
- **Password**: Your database password
- **Connection String** (Optional): A full Oracle connection string that overrides host, port, and service name

### Connection String Format:
```
(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=ORCL)))
```

## Usage

### Execute Query

Execute a SELECT query with parameter binding:

**Query:**
```sql
SELECT * FROM employees WHERE department_id = :deptId AND salary > :minSalary
```

**Query Parameters:**
```json
{
  "deptId": 10,
  "minSalary": 50000
}
```

### Insert

Insert data into a table:

- **Table**: `employees`
- **Columns**: `employee_id,first_name,last_name,email,hire_date`

Input data from previous node:
```json
{
  "employee_id": 1001,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "hire_date": "2024-01-15"
}
```

### Update

Update existing records:

- **Table**: `employees`
- **Update Key**: `employee_id`

Input data:
```json
{
  "employee_id": 1001,
  "salary": 75000,
  "department_id": 20
}
```

### Delete

Delete records from a table:

- **Table**: `employees`
- **Delete Key**: `employee_id`

Input data:
```json
{
  "employee_id": 1001
}
```

### Execute Stored Procedure

Execute a stored procedure:

- **Procedure Name**: `UPDATE_EMPLOYEE_SALARY`
- **Procedure Parameters**:
```json
{
  "emp_id": 1001,
  "new_salary": 80000
}
```

## Features

- ✅ Full CRUD operations support
- ✅ Parameter binding to prevent SQL injection
- ✅ Stored procedure execution
- ✅ Transaction control (auto-commit option)
- ✅ Configurable fetch size for large result sets
- ✅ Type conversion for boolean values (converts to 0/1)
- ✅ Proper null handling
- ✅ JSON serialization for complex objects
- ✅ Error handling with continue on fail support

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Oracle Database Documentation](https://docs.oracle.com/en/database/)
* [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html)
* [node-oracledb Documentation](https://oracle.github.io/node-oracledb/)

## Development

To contribute to this node:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Commands

```bash
# Install dependencies
npm install

# Build the node
npm run build

# Build in watch mode for development
npm run dev

# Run tests (when implemented)
npm test
```

## Troubleshooting

### NJS-045: Cannot load the oracledb add-on binary

This error indicates that Oracle Instant Client is not properly installed or configured. Make sure:

1. Oracle Instant Client is installed
2. The library path is correctly set
3. The architecture (32-bit vs 64-bit) matches your Node.js installation

### NJS-005: Invalid value for parameter

This error occurs when parameter types don't match. The node automatically converts:
- Booleans to numbers (true → 1, false → 0)
- Objects to JSON strings
- Null/undefined to Oracle NULL

### Connection Issues

1. Verify your connection details (host, port, service name)
2. Check if the Oracle listener is running
3. Ensure firewall rules allow the connection
4. Test the connection using SQL*Plus or another Oracle client

## Version History

### 0.1.0
- Initial release
- Basic CRUD operations
- Stored procedure support
- Parameter binding
- Type conversion

## License

[MIT](LICENSE.md)

## Author

BGS- askfrombgs@gmail.com

## Acknowledgments

- Thanks to the n8n team for creating an amazing workflow automation platform
- Oracle node-oracledb team for the excellent Node.js driver