# n8n-nodes-ibm-db2

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

An n8n community node for connecting to and querying IBM DB2 databases via REST API.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

### Simple Installation

```bash
npm install @mehrdafon/n8n-nodes-ibm-db2
```

**No build tools required!** This package uses HTTP/REST APIs instead of native database drivers, making installation simple and reliable across all platforms.

### Docker Setup

```Dockerfile
FROM n8nio/n8n:1.95.2
ENV N8N_ENABLE_COMMUNITY_NODES=true
```

No additional dependencies or build tools needed!

### n8n UI Installation

1. Go to **Settings → Community Nodes → Install Node**
2. Enter: `@mehrdafon/n8n-nodes-ibm-db2`
3. Click **Install**
4. Restart n8n if prompted

## Configuration

### Connection Types

This node supports three connection methods:

#### 1. Database Connection Parameters (REST) - Recommended
- Use traditional database connection parameters via REST API
- Perfect for IBM Cloud DB2 instances
- Automatically constructs REST API endpoints
- **No build tools required**

#### 2. ODBC Direct Connection - For servers without REST services
- Direct ODBC connection to DB2 using native drivers
- Use when your DB2 server doesn't have REST services enabled
- **Requires `ibm_db` package installation and build tools**
- Best performance for direct database access

#### 3. REST API Endpoint - For custom implementations
- Use if you have a custom REST API endpoint
- For environments with pre-configured REST services

### Installation Options

#### For REST API connections (Recommended):
```bash
npm install @mehrdafon/n8n-nodes-ibm-db2
```
**No additional setup required!**

#### For ODBC Direct connections:
You need to install the `ibm_db` package separately:

```bash
# Install build tools first (Alpine/Docker)
apk update && apk add --no-cache build-base python3 python3-dev linux-pam-dev libc6-compat libstdc++ libgcc musl-dev gcompat

# Install the n8n node
npm install @mehrdafon/n8n-nodes-ibm-db2

# Install ODBC driver
npm install ibm_db
```

For other platforms, see the [IBM DB2 installation guide](https://www.npmjs.com/package/ibm_db).

### Credentials Setup

#### For IBM Cloud DB2 Users (REST):

1. In n8n, create a new credential of type "IBM DB2 API"
2. Select **"Database Connection Parameters (REST)"** as Connection Type
3. Fill in your IBM Cloud connection details:
   - **Server**: Your DB2 server IP (e.g., `172.16.1.20`)
   - **Port**: Database port (usually `50000`)
   - **Database**: Your database name (e.g., `TFKDFG`)
   - **User**: Your database username (e.g., `T2000COCODMS`)
   - **Password**: Your database password

#### For ODBC Direct Connection:

1. In n8n, create a new credential of type "IBM DB2 API"
2. Select **"ODBC Direct Connection"** as Connection Type
3. Fill in your database connection details:
   - **Server**: Your DB2 server hostname or IP
   - **Port**: Database port (usually `50000`)
   - **Database**: Your database name
   - **User**: Your database username
   - **Password**: Your database password
4. Optionally configure ODBC Options:
   - **Connection Timeout**: Timeout in seconds (default: 30)
   - **Use SSL**: Enable SSL connection

#### For Custom REST API Users:

1. In n8n, create a new credential of type "IBM DB2 API"
2. Select **"REST API Endpoint"** as Connection Type  
3. Configure your endpoint:
   - **Base URL**: Your REST API endpoint
   - **User**: Your username
   - **Password**: Your password
   - **API Key**: If using API key authentication (optional)

## Usage

1. Add the "IBM DB2" node to your workflow
2. Select your IBM DB2 credentials
3. Choose your connection type
4. Write your SQL query in the Query field
5. Optionally add query parameters for prepared statements
6. Configure options like timeout and max rows
7. Execute the workflow

### Example Queries

```sql
-- Simple SELECT
SELECT * FROM EMPLOYEES WHERE DEPARTMENT = 'IT'

-- With parameters (use the Parameters section)
SELECT * FROM ORDERS WHERE ORDER_DATE > ? AND STATUS = ?

-- Complex query with joins
SELECT e.EMPLOYEE_ID, e.NAME, d.DEPARTMENT_NAME 
FROM EMPLOYEES e 
JOIN DEPARTMENTS d ON e.DEPT_ID = d.DEPT_ID
WHERE d.LOCATION = 'New York'
```

### Query Parameters

Use the Parameters section to add values for prepared statements:
- **Name**: Parameter placeholder (e.g., `param1`)
- **Value**: Actual value to substitute

## Features

- ✅ **Multiple connection types** - REST API (recommended) and ODBC Direct
- ✅ **Zero dependencies for REST** - Pure JavaScript implementation for REST connections
- ✅ **Native ODBC support** - Direct database access when REST services aren't available
- ✅ **IBM Cloud compatible** - Works seamlessly with IBM Cloud DB2 instances
- ✅ **Flexible authentication** - Basic Auth, API Key, database credentials
- ✅ **Query parameters** - Support for prepared statements
- ✅ **Configurable options** - Timeout, row limits, SSL settings
- ✅ **Error handling** - Comprehensive error reporting with helpful guidance
- ✅ **Cross-platform** - Works on any OS (REST mode) or with proper setup (ODBC mode)
- ✅ **Easy installation** - No build tools for REST, optional ODBC for maximum compatibility

## Compatibility

- ✅ n8n version 1.x
- ✅ IBM DB2 (all versions with REST API support)
- ✅ All platforms (Windows, macOS, Linux)
- ✅ Docker environments
- ✅ Cloud deployments (n8n Cloud compatible)
- ✅ n8n Community Node standards compliant

## Prerequisites

### For DB2 REST Services
- IBM DB2 with REST Services enabled
- REST Services configured and accessible
- Valid DB2 user credentials

### For Custom REST Endpoint
- REST API that provides DB2 access
- API documentation for endpoint structure
- Valid authentication credentials

### For JDBC Bridge
- HTTP-to-JDBC bridge service
- Bridge service configured for your DB2 instance
- Access to bridge service endpoints

## Troubleshooting

### REST API Connection Issues

- **Invalid URL**: Verify your base URL is correct and accessible
- **Authentication Failed**: Check your credentials and authentication method
- **SSL Errors**: Configure SSL options or use `ignoreSsl` for development
- **Timeout**: Increase timeout value in node options
- **REST Services Not Available**: Try "ODBC Direct Connection" instead

### ODBC Connection Issues

- **ibm_db not found**: Install the package with `npm install ibm_db`
- **Build tools missing**: Install build tools for your platform:
  - **Alpine/Docker**: `apk add build-base python3 python3-dev`
  - **Ubuntu/Debian**: `sudo apt-get install build-essential python3-dev`
  - **CentOS/RHEL**: `sudo yum groupinstall "Development Tools"`
- **Connection timeout**: Increase connection timeout in ODBC options
- **SSL issues**: Enable/disable SSL in ODBC options as needed
- **Permission denied**: Ensure your DB2 user has proper access permissions

### Query Issues

- **SQL Syntax**: Ensure your SQL syntax is compatible with DB2
- **Parameters**: Verify parameter names match your query placeholders
- **Permissions**: Ensure your user has appropriate database permissions

### Common Solutions

1. **For Connection Errors**:
   - Start with REST API connection (easier setup)
   - Fall back to ODBC if REST services aren't available
   - Test credentials with IBM DB2 client tools first

2. **For Installation Issues**:
   - Use REST mode if you don't need ODBC performance
   - Install build tools before attempting ODBC setup
   - Check the [IBM DB2 package documentation](https://www.npmjs.com/package/ibm_db) for platform-specific requirements

3. **For Performance**:
   - ODBC Direct provides better performance for heavy queries
   - REST API is better for simple queries and easier deployment

## Migration from v0.2.x

If you were using the previous version with native `ibm_db` dependency:

1. **Update your credentials** to use the new REST API format
2. **Configure your DB2 server** to expose REST Services (if not already done)
3. **Update your workflows** to use the new connection types
4. **Remove old Docker build dependencies** - no longer needed

## Development

### Building

   ```bash
npm run build
   ```

### Linting

   ```bash
npm run lint
   ```

### Testing

Test your REST endpoints before using in n8n:

   ```bash
# Test DB2 REST Services
curl -X POST "https://your-db2-server:8443/db2/rest/services/db" \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic base64(username:password)" \
  -d '{"sql": "SELECT 1 FROM SYSIBM.SYSDUMMY1"}'
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:

1. Check the troubleshooting section above
2. Test your REST endpoints independently
3. Review the [IBM DB2 REST Services documentation](https://www.ibm.com/docs/en/db2/11.5?topic=services-db2-rest)
4. Open an issue on the project repository

## Changelog

### v0.4.0
- ✅ **Major**: Added ODBC Direct Connection support for servers without REST services
- ✅ **Added**: Three connection types: REST (recommended), ODBC Direct, Custom REST
- ✅ **Added**: Optional `ibm_db` dependency for ODBC connections
- ✅ **Added**: ODBC-specific options (connection timeout, SSL support)
- ✅ **Added**: Comprehensive error handling with connection type guidance
- ✅ **Improved**: Documentation with installation options for different scenarios
- ✅ **Enhanced**: Troubleshooting guide for both REST and ODBC connections

### v0.3.x
- ✅ **Major**: Switched from native `ibm_db` to HTTP/REST API approach
- ✅ **Added**: Multiple connection types (DB2 REST, Custom, JDBC Bridge)
- ✅ **Added**: Flexible authentication methods
- ✅ **Added**: Query parameters support
- ✅ **Added**: SSL/TLS configuration options
- ✅ **Removed**: Native dependencies (no build tools required)
- ✅ **Improved**: Cross-platform compatibility
- ✅ **Improved**: Installation reliability

### v0.2.x
- Native `ibm_db` implementation (deprecated)

 
 