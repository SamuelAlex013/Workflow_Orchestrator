# HTTPS Over Proxy Node for n8n

> [繁體中文版說明文件](README.zh-TW.md)

This node solves the critical limitation of n8n's built-in HTTP Request node: **the inability to connect to HTTPS websites when using an HTTP proxy**.

## The Problem

n8n's standard HTTP Request node fails when trying to access HTTPS sites through HTTP proxies, which is a common requirement in enterprise environments with firewall restrictions.

## The Solution

HTTPS Over Proxy node provides specialized proxy handling while maintaining compatibility with n8n's workflow ecosystem.

## Unique Features (Not Available in Built-in HTTP Request)

### 🌍 Advanced Proxy Support
- **HTTPS over HTTP Proxy**: The core feature that solves the main limitation
- **Proxy Authentication**: Complete username/password authentication for proxy servers
- **Connection Pool Management**: Specialized proxy connection pooling for optimal performance
- **Proxy Error Diagnostics**: Detailed proxy-specific error messages and troubleshooting guides

### 🔧 Enhanced Connection Management
- **Custom Connection Pools**: HTTP/HTTPS/Proxy agent management with configurable settings:
  - `maxSockets`: Maximum concurrent connections per host (default: 50)
  - `maxFreeSockets`: Maximum idle connections per host (default: 10)
  - `keepAlive`: Connection reuse optimization
  - `timeout`: Per-connection timeout control
- **Agent Cleanup**: Automatic cleanup of unused connection agents

### 🛠️ Advanced Error Handling & Diagnostics
- **Proxy-Specific Error Messages**: Detailed error reporting for proxy connection issues
- **Troubleshooting Suggestions**: Built-in guidance for common proxy problems
- **Connection State Debugging**: Detailed logging of connection pool states
- **Smart Error Classification**: Distinguishes between proxy, network, and application errors

### 📊 Enhanced Response Processing
- **HTML Content Extraction**: Advanced HTML parsing with CSS selectors
- **Mozilla Readability Integration**: Clean article extraction from web pages
- **JSDOM Processing**: Full DOM manipulation capabilities
- **Text Content Optimization**: Intelligent text extraction and formatting

### 🔍 Development & Debugging Features
- **Comprehensive Logging**: Detailed request/response logging for debugging
- **cURL Command Parsing**: Advanced cURL import with proxy settings support
- **Request State Tracking**: Monitor connection states and performance metrics
- **Proxy Configuration Validation**: Automatic validation of proxy settings

## Installation

### Local Installation

1. Go to your n8n installation directory
2. Install the node package:
```bash
npm install n8n-nodes-httpsoverproxy
```

### Global Installation

If you installed n8n globally, you can install this node globally too:

```bash
npm install -g n8n-nodes-httpsoverproxy
```

## Usage

After installation, you can find the "HTTPS Over Proxy" node in the n8n nodes panel under the "Network" category.

### Basic Configuration

1. Add the HTTPS Over Proxy node to your workflow
2. Set the request method (GET, POST, etc.)
3. Enter the target URL
4. Configure authentication if needed
5. Configure proxy settings in the Options section:
   - Enable "Use Proxy"
   - Enter Proxy Host (without http:// or https:// prefix)
   - Enter Proxy Port
   - Configure proxy authentication if needed

### Advanced Features

#### Authentication
- Choose from None, Predefined Credential Type, or Custom Auth
- For predefined types, select from available n8n credentials
- For custom auth, configure JSON-based authentication logic

#### Batch Processing
- Configure batch size for processing multiple items
- Set intervals between batches
- Control maximum number of requests

#### Pagination
- Enable pagination for APIs that return paginated results
- Configure pagination parameters and completion conditions
- Set request intervals and maximum page limits

#### Response Optimization
- Enable response optimization for better data processing
- Configure HTML content extraction using CSS selectors
- Set up JSON data filtering and text content optimization

### Advanced Options

- **Allow Internal Network Access**: Enable to allow requests to internal network addresses (disabled by default for security)
- **Connection Pool Settings**: Configure connection pooling for better performance
- **SSL Certificate Validation**: Control SSL certificate verification
- **Request Timeout**: Set custom timeout values

## Comparison with n8n HTTP Request Node

This node provides feature parity with n8n's built-in HTTP Request node while adding:
- ✅ HTTPS over HTTP proxy support
- ✅ Enhanced error handling with detailed troubleshooting
- ✅ Advanced connection pool management
- ✅ Complete pagination system implementation
- ✅ Comprehensive authentication support
- ✅ Intelligent response optimization

## License

[MIT](LICENSE)
