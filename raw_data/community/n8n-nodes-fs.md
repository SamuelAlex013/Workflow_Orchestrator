# n8n File System Nodes

A collection of n8n community nodes for comprehensive file system operations. This package provides multiple specialized nodes for handling files and directories efficiently within your n8n workflows.

## Features

This package includes the following nodes:

### 📁 **ReadFile Node**
- Read file contents as text or binary
- Support for various encodings (UTF-8, ASCII, Base64, etc.)
- Error handling for non-existent files

### ✏️ **WriteFile Node**
- Write text or binary content to files
- Create parent directories automatically
- Append or overwrite modes
- Multiple encoding support

### 📋 **ListFiles Node**
- List files and directories in a specified path
- Recursive directory traversal option
- File filtering by extension or pattern
- Include/exclude hidden files

### ℹ️ **FileInfo Node**
- Get detailed file/directory information
- File size, creation/modification dates
- File permissions and ownership
- MIME type detection

### 🗑️ **DeleteFile Node**
- Delete files or directories
- Recursive directory deletion
- Safe deletion with confirmation options

### 📁 **CreateDirectory Node**
- Create single or nested directories
- Set directory permissions
- Skip if directory already exists

### 📋 **CopyFile Node**
- Copy files or directories
- Preserve file metadata and permissions
- Recursive directory copying

### 🔄 **MoveFile Node**
- Move/rename files and directories
- Cross-filesystem move support
- Automatic directory creation

### 🔍 **FileExists Node**
- Check if files or directories exist
- Support for different path types (file, directory, any)
- Access permission checking (read, write, execute)
- Detailed file information retrieval
- Symbolic link resolution

## Installation

### In n8n
1. Go to **Settings > Community Nodes**
2. Install `n8n-nodes-fs`

### Manual Installation
```bash
# In your n8n installation directory
cd ~/.n8n/custom
npm install n8n-nodes-fs
```

### Development Setup

For development and testing, you can use the provided registration scripts to link the package locally with n8n:

#### Windows (PowerShell)
```powershell
.\local_n8n_register.ps1
```

#### macOS/Linux (Bash)
```bash
# Make the script executable
chmod +x local_n8n_register.sh

# Run the script
./local_n8n_register.sh
```

These scripts will:
1. Clean the build directory
2. Install dependencies
3. Build the project
4. Link the package to your local n8n installation
5. Set up development environment variables
6. Start n8n with debug logging

## Usage

After installation, you'll find all the file system nodes in your n8n editor under the "File System" category. Each node provides intuitive configuration options and comprehensive error handling.

## Security Considerations

⚠️ **Important**: These nodes have direct access to the file system where n8n is running. Ensure you:

- Run n8n with appropriate user permissions
- Validate file paths to prevent directory traversal attacks
- Use absolute paths when possible
- Be cautious with user-provided file paths in production

## Examples

### Basic File Reading
```json
{
  "filePath": "/path/to/your/file.txt",
  "encoding": "utf8"
}
```

### Directory Listing with Filtering
```json
{
  "directoryPath": "/path/to/directory",
  "recursive": true,
  "filter": "*.js",
  "includeHidden": false
}
```

### File Information Retrieval
```json
{
  "path": "/path/to/file",
  "includeStats": true,
  "detectMimeType": true
}
```

### Check File Existence
```json
{
  "filePath": "/path/to/file.txt",
  "checkOptions": {
    "checkType": "file",
    "includeDetails": true,
    "checkAccess": ["readable", "writable"]
  }
}
```

## Example Workflow

The package includes a complete example workflow (`example-workflow.json`) that demonstrates all file system operations:

1. **Initialize Variables**: Set up test directory path
2. **Create Directory**: Create a test directory
3. **Write File**: Create a text file with content
4. **Get File Info**: Retrieve detailed file information
5. **Move File**: Move the file to a new location
6. **Read File**: Read the moved file content
7. **Delete File**: Remove the file
8. **Check File Exists**: Verify file deletion
9. **List Files**: Show remaining directory contents

### Using the Example Workflow

1. Import `example-workflow.json` into your n8n instance
2. Update the test directory path in the "Vars" node
3. Execute the workflow to see all nodes in action

The workflow uses expressions to pass data between nodes, demonstrating real-world usage patterns.

## Error Handling

All nodes include comprehensive error handling:
- File not found errors
- Permission denied errors
- Invalid path errors
- Disk space errors

## Compatibility

- n8n version: 1.0.0+
- Node.js version: 18+
- Supports: Windows, macOS, Linux

## Project Files

This project includes several helpful scripts and configuration files:

- `local_n8n_register.ps1` - Windows PowerShell script for development setup
- `local_n8n_register.sh` - macOS/Linux Bash script for development setup
- `example-workflow.json` - Complete workflow example demonstrating all nodes
- `package.json` - Node.js package configuration
- `tsconfig.json` - TypeScript configuration

## Contributing

This package is part of the Mira project. Contributions are welcome!

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- GitHub Issues: [Project Repository](https://github.com/hunmer/mira-dashboard)
- n8n Community: [n8n Community Forum](https://community.n8n.io/)

---

**Note**: Always test file operations in a safe environment before using in production workflows.
