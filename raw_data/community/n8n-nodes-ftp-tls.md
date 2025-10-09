# n8n-nodes-ftp-tls

[![npm version](https://badge.fury.io/js/n8n-nodes-ftp-tls.svg)](https://badge.fury.io/js/n8n-nodes-ftp-tls)

This is an n8n community node that extends the native FTP node with TLS/FTPS support. It provides secure file transfer capabilities using:

- **FTP** - Standard File Transfer Protocol
- **FTPS (Explicit)** - FTP with explicit TLS encryption
- **FTPS (Implicit)** - FTP with implicit TLS encryption  
- **SFTP** - SSH File Transfer Protocol

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-ftp-tls` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in n8n.

### npm

```bash
npm install n8n-nodes-ftp-tls
```

## Features

### Supported Protocols

- **FTP**: Standard unencrypted FTP
- **FTPS (Explicit)**: FTP with explicit TLS (starts unencrypted, then upgrades to TLS)
- **FTPS (Implicit)**: FTP with implicit TLS (encrypted from the start)
- **SFTP**: SSH File Transfer Protocol

### Supported Operations

- **List**: List files and folders in a directory
- **Download**: Download files from the server
- **Upload**: Upload files to the server  
- **Delete**: Delete files or folders
- **Rename**: Rename or move files and folders

### TLS/SSL Configuration

- **Security Mode**: Choose between strict and legacy SSL/TLS handling
- **SSL Certificate Validation**: Option to ignore SSL certificate errors
- **Custom Ports**: Support for custom ports (FTP: 21, FTPS Implicit: 990, SFTP: 22)

## Configuration

### Credentials

Create a new credential of type **FTP/FTPS with TLS**:

#### Basic Settings
- **Host**: FTP server hostname or IP address
- **Port**: Connection port (defaults: FTP=21, FTPS Implicit=990, SFTP=22)
- **Username**: FTP username
- **Password**: FTP password

#### Protocol Settings
- **Protocol**: Choose from:
  - FTP (standard, unencrypted)
  - FTPS (Explicit) - recommended for secure connections
  - FTPS (Implicit) - for servers requiring implicit TLS
  - SFTP - for SSH-based file transfer

#### Security Settings (FTPS only)
- **Security**: 
  - Strict (recommended) - uses modern TLS protocols
  - Legacy - for compatibility with older servers
- **Ignore SSL Issues**: Enable to bypass SSL certificate validation

#### SFTP Settings
- **Private Key**: SSH private key for key-based authentication
- **Passphrase**: Passphrase for encrypted private keys

#### Advanced Settings
- **Timeout**: Connection timeout in milliseconds (default: 10000)

### Node Configuration

#### Operations

**List Operation**
- **Path**: Directory path to list
- **Recursive**: Enable to list subdirectories recursively

**Download Operation**
- **Path**: Remote file path to download
- **Property Name**: Name of the binary property to store the file

**Upload Operation**
- **Path**: Remote path where the file will be uploaded
- **Binary File**: Toggle for binary vs text content
- **File Content**: Text content (if not binary)
- **Property Name**: Binary property name (if binary)

**Delete Operation**
- **Path**: Path to file or folder to delete
- **Recursive**: Enable to delete folders recursively

**Rename Operation**
- **Path**: Current path of the file/folder
- **New Path**: New path for the file/folder

## Examples

### Basic FTP Connection

```json
{
  "host": "ftp.example.com",
  "port": 21,
  "username": "user",
  "password": "password",
  "protocol": "ftp"
}
```

### FTPS (Explicit) Connection

```json
{
  "host": "secure.example.com",
  "port": 21,
  "username": "user",
  "password": "password",
  "protocol": "ftps-explicit",
  "security": "strict",
  "ignoreSSLIssues": false
}
```

### SFTP Connection with Key Authentication

```json
{
  "host": "sftp.example.com",
  "port": 22,
  "username": "user",
  "protocol": "sftp",
  "privateKey": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----",
  "passphrase": "key-passphrase"
}
```

## Troubleshooting

### Common Issues

1. **SSL Certificate Errors**: Enable "Ignore SSL Issues" in credentials for testing
2. **Connection Timeout**: Increase timeout value in credentials
3. **Port Issues**: Ensure correct ports (FTP: 21, FTPS Implicit: 990, SFTP: 22)
4. **Authentication Failures**: Verify username/password or private key setup

### Debug Tips

- Test with FTP first, then upgrade to FTPS
- Check server logs for connection attempts
- Verify firewall settings allow the connection
- Use explicit FTPS before trying implicit FTPS

## Development

### Requirements

- Node.js 18+
- npm 8+
- n8n installed

### Setup

```bash
# Clone the repository
git clone https://github.com/techbrainpt/n8n-nodes-ftp-tls.git
cd n8n-nodes-ftp-tls

# Install dependencies
npm install

# Build the project
npm run build

# Lint the code
npm run lint

# Format the code
npm run format
```

### Testing

To test the node locally:

1. Link the package: `npm link`
2. In your n8n installation: `npm link n8n-nodes-ftp-tls`
3. Restart n8n

## Dependencies

- [basic-ftp](https://www.npmjs.com/package/basic-ftp) - FTP/FTPS client
- [ssh2-sftp-client](https://www.npmjs.com/package/ssh2-sftp-client) - SFTP client

## License

[MIT](LICENSE.md)

## Support

For issues and questions:
- GitHub Issues: https://github.com/techbrainpt/n8n-nodes-ftp-tls/issues
- n8n Community: https://community.n8n.io/

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests.

## Changelog

### 1.0.0
- Initial release
- Support for FTP, FTPS (Explicit/Implicit), and SFTP
- All basic operations (list, download, upload, delete, rename)
- TLS/SSL configuration options
- Private key authentication for SFTP
