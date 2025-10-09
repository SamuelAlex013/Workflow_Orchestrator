# SSH Nexus for n8n

**The Ultimate SSH Automation Hub - Advanced SSH operations with intelligent TextFSM template parsing**

> ⚠️ **BETA VERSION** - This package is currently in beta. Please report any bugs or issues you encounter to help us improve SSH Nexus!

SSH Nexus is a comprehensive n8n package that combines two powerful nodes into one unified solution for network device automation and SSH operations. Built for network engineers, DevOps teams, and automation specialists who need to manage network devices and extract structured data from command outputs.

## 🏗️ Project Architecture

SSH Nexus consists of two specialized nodes that work together seamlessly:

### **Core Components**

1. **SuperSSH Node** - Advanced SSH Operations & Device Management
2. **SSH Template Parser Node** - TextFSM Template Engine for Output Parsing

These nodes are designed to work independently or together in workflows, providing a complete solution for network automation tasks.

## 🚀 What SSH Nexus Delivers

### **SuperSSH Node** - Your SSH Powerhouse
- **Multi-device management** with intelligent connection pooling
- **Advanced credential management** with secure storage
- **Network device optimization** for Cisco, Aruba, Juniper, and generic devices
- **Batch operations** across multiple devices simultaneously
- **Connection health monitoring** and performance testing
- **Security auditing** and configuration management
- **AI agent compatibility** for automated workflows

### **SSH Template Parser Node** - Intelligent Output Processing
- **TextFSM template engine** for parsing structured command outputs
- **Pre-built templates** for Aruba, Cisco, and other vendor commands
- **Custom template creation** via user-friendly forms or JSON upload
- **Structured data extraction** with automatic type conversion
- **Template management** and sharing capabilities
- **Debug mode** for troubleshooting parsing issues

## 📦 Installation

```bash
npm install n8n-nodes-ssh-nexus
```

After installation, you'll find both nodes in your n8n palette:
- **"SSH Nexus"** (SuperSSH node)
- **"SSH Template Parser"** (TextFSM parser node)

## 🔑 Quick Start Guide

### **Step 1: Set Up SSH Credentials**
1. Add **SuperSSH Credentials** to your n8n instance
2. Configure your SSH connection details (host, username, password/key)

### **Step 2: Execute Commands with SuperSSH**
1. Drag the **"SSH Nexus"** node into your workflow
2. Select your credentials
3. Choose an operation (Execute Command, Upload File, etc.)
4. Configure your target devices and commands

### **Step 3: Parse Output with TextFSM Templates**
1. Connect the **"SSH Template Parser"** node after SuperSSH
2. Select a pre-built template (e.g., "Aruba AOS-CX - Show ARP")
3. The parser automatically converts raw SSH output into structured JSON

## 🔄 Workflow Patterns

### **Pattern 1: Basic Device Information**
```
SSH Nexus (Execute: "show version") 
  → SSH Template Parser (Parse with "show version" template)
  → HTTP Request (Send to inventory system)
```

### **Pattern 2: Network Monitoring**
```
SSH Nexus (Execute: "show interface brief" on multiple devices)
  → SSH Template Parser (Parse each device output)
  → Filter (Status = "down")
  → Slack (Send alert notification)
```

### **Pattern 3: Configuration Management**
```
SSH Nexus (Backup running config)
  → SSH Template Parser (Parse config sections)
  → Code Node (Validate configuration)
  → HTTP Request (Update documentation)
```

## 📋 Understanding TextFSM Templates

### **What is TextFSM?**
TextFSM (Text Finite State Machine) is a template language that defines how to parse structured text output. Think of it as a "smart pattern matcher" that extracts specific data from command outputs and converts them into structured JSON.

### **How TextFSM Works in SSH Nexus**
1. **Raw Output**: SSH command returns unstructured text
2. **Template**: TextFSM template defines patterns to match
3. **Parsed Result**: Structured JSON with extracted data

### **Example: Parsing "show arp" Output**

**Raw SSH Output:**
```
IPv4 Address      MAC Address       Port  Physical Port  State  VRF
192.168.1.1      00:11:22:33:44:55 1/1/1 1/1/1         active default
192.168.1.2      00:11:22:33:44:66 1/1/2 1/1/2         active default
```

**TextFSM Template Definition:**
```json
{
  "name": "aruba_aoscx_show_arp_all_vrfs",
  "vendor": "aruba",
  "deviceOs": "aruba_aoscx",
  "command": "show arp all-vrfs",
  "variables": [
    {"name": "IP_ADDRESS", "pattern": "(\\d+\\.\\d+\\.\\d+\\.\\d+)", "type": "ip"},
    {"name": "MAC_ADDRESS", "pattern": "([0-9a-fA-F:]+)", "type": "mac"},
    {"name": "PORT_ID", "pattern": "(\\S+)"},
    {"name": "PHYSICAL_PORT", "pattern": "(\\S+)"},
    {"name": "STATE", "pattern": "([a-z]+)"},
    {"name": "VRF", "pattern": "(\\S+)"}
  ],
  "states": [
    {
      "name": "Start",
      "patterns": [
        {
          "regex": "^IPv4 Address\\s+MAC\\s+Port\\s+Physical\\s+Port\\s+State",
          "actions": ["Next"]
        },
        {
          "regex": "^${IP_ADDRESS}\\s+${MAC_ADDRESS}\\s+${PORT_ID}\\s+${PHYSICAL_PORT}\\s+${STATE}\\s+${VRF}",
          "actions": ["Record", "Next"]
        }
      ]
    }
  ]
}
```

**Parsed Result (Structured JSON):**
```json
[
  {
    "IP_ADDRESS": "192.168.1.1",
    "MAC_ADDRESS": "00:11:22:33:44:55",
    "PORT_ID": "1/1/1",
    "PHYSICAL_PORT": "1/1/1",
    "STATE": "active",
    "VRF": "default"
  },
  {
    "IP_ADDRESS": "192.168.1.2",
    "MAC_ADDRESS": "00:11:22:33:44:66",
    "PORT_ID": "1/1/2",
    "PHYSICAL_PORT": "1/1/2",
    "STATE": "active",
    "VRF": "default"
  }
]
```

## 🛠️ Creating Custom TextFSM Templates

### **Method 1: Form-Based Creation (Beginner Friendly)**
1. Use the **SSH Template Parser** node
2. Select **"Create Template"** operation
3. Choose **"Form"** as template source
4. Fill out the fields:
   - **Template Name**: Descriptive name (e.g., `my_device_show_status`)
   - **Vendor**: Device vendor (Aruba, Cisco, Juniper, Generic)
   - **Device OS**: Operating system version
   - **Command**: The command this template parses
   - **Variables**: Define what data to extract
   - **Patterns**: Define how to match and extract data

### **Method 2: JSON Upload (Advanced Users)**
1. Create a JSON file following the template structure above
2. Use the **"Upload Template"** operation
3. Upload your JSON file
4. The template becomes available immediately

### **Template Components Explained**

#### **Variables Section**
```json
"variables": [
  {
    "name": "INTERFACE",           // Variable name in results
    "pattern": "(\\S+)",           // Regex pattern to match
    "type": "string",              // Data type (string, number, ip, mac, list)
    "description": "Interface name", // Optional description
    "required": true               // Whether this field is required
  }
]
```

#### **States Section**
```json
"states": [
  {
    "name": "Start",               // State name
    "patterns": [
      {
        "regex": "^${INTERFACE}\\s+${STATUS}",  // Pattern to match
        "actions": ["Record", "Next"]           // Actions to take
      }
    ]
  }
]
```

#### **Available Actions**
- **`Record`**: Save current variables and start new record
- **`Next`**: Move to next line
- **`Continue`**: Keep current variables for next line
- **`Error`**: Handle parsing errors gracefully

## 📚 Pre-Built TextFSM Templates

SSH Nexus comes with ready-to-use templates for common network commands:

### **Aruba AOS-CX Templates**
- **`show arp`** - ARP table parsing
- **`show interface brief`** - Interface status summary
- **`show mac-address-table`** - MAC address table
- **`show lldp neighbor-info`** - LLDP neighbor information
- **`show clock`** - System time and date
- **`show aaa authentication port-access`** - Port access authentication status

### **Aruba OS Templates**
- **`show ap database`** - Access point database
- **`show system`** - System information
- **`show version`** - Version information
- **`show interface status`** - Interface status

## 🔧 Advanced Features

### **SuperSSH Node Features**
- **Multi-device operations** with connection pooling
- **Device-specific optimizations** for Cisco, Aruba, and generic devices
- **Advanced security options** with cipher selection and compatibility modes
- **Connection health monitoring** with performance metrics
- **Batch command execution** across device groups
- **File operations** (upload, download, backup, restore)

### **SSH Template Parser Features**
- **Output modes**: Single item (all records) or split items (one per record)
- **Text source options**: Input field, JSON path, or direct string
- **Debug mode**: Detailed parsing trace for troubleshooting
- **Type coercion**: Automatic data type conversion based on template definitions
- **Filldown control**: Manage variable persistence across lines
- **Template management**: Create, update, delete, and share templates

### **Integration Features**
- **Seamless workflow chaining** between SuperSSH and Template Parser
- **Dynamic template loading** with vendor and command filtering
- **Error handling** with graceful fallbacks
- **Performance optimization** for large outputs

## 🚨 Troubleshooting

### **Common Issues & Solutions**

**"No templates found"**
- Check if templates are properly loaded
- Verify template vendor and command filters
- Use "Manage Templates" to see available templates

**"Parsing failed"**
- Enable debug mode to see parsing trace
- Check if output format matches template patterns
- Verify regex patterns in template

**"Template not working"**
- Test with sample output first
- Check variable names and patterns
- Use template validation tools

### **Debug Mode**
Enable debug mode in the SSH Template Parser node to get detailed information about:
- Which patterns matched
- Variable extraction process
- State transitions
- Parsing errors

## 🐛 Bug Reports & Beta Feedback

**SSH Nexus is currently in beta** - your feedback is crucial for making it production-ready!

### **How to Report Bugs**
1. **Check existing issues** first to avoid duplicates
2. **Provide detailed information**:
   - n8n version
   - Node.js version
   - Exact error messages
   - Steps to reproduce
   - Sample data (if applicable)
3. **Include workflow examples** when possible
4. **Use the GitHub issues page** for formal bug reports

### **What to Report**
- **Connection issues** with specific devices
- **Template parsing errors** with sample output
- **Performance problems** with large outputs
- **UI/UX issues** in the node configuration
- **Integration problems** with other n8n nodes

### **Beta Testing Tips**
- Test with different device types and vendors
- Try various command outputs and template combinations
- Report any unexpected behavior or edge cases
- Share successful workflows for the community

## 🤝 Contributing to SSH Nexus

We welcome contributions to make SSH Nexus even better:

1. **Add new TextFSM templates** for different devices and commands
2. **Improve existing templates** with better patterns
3. **Report bugs** and suggest new features
4. **Share workflows** that others might find useful

### **Adding New Templates**
1. Create a template following the structure above
2. Test with real device output
3. Submit a pull request or share the template

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and feature requests on GitHub
- **Discussions**: Ask questions and share workflows
- **Documentation**: Check this README and inline help

---

**SSH Nexus: Where SSH Operations Meet Intelligent Parsing**

*Made with ❤️ for the n8n community*

---

Repository: https://github.com/Sarryaz/SSH-Nexus
