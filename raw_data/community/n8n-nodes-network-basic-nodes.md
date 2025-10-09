# Network Basic Nodes for n8n

A comprehensive n8n community node package that provides TCP and UDP network functionality with specialized client and server nodes.

**🌐 Languages:** [English](README.md) | [Español](README.es.md) | [Galego](README.gl.md)

[![npm version](https://badge.fury.io/js/n8n-nodes-network-basic-nodes.svg)](https://badge.fury.io/js/n8n-nodes-network-basic-nodes)
[![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-network-basic-nodes.svg)](https://www.npmjs.com/package/n8n-nodes-network-basic-nodes)

## 📦 Installation

Install this package from the n8n community nodes library:

### Option 1: Via n8n Interface (Recommended)
1. Go to **Settings** → **Community Nodes**
2. Click **Install a community node**
3. Enter: `n8n-nodes-network-basic-nodes`
4. Click **Install**

### Option 2: Via npm
```bash
npm install n8n-nodes-network-basic-nodes
```

### Option 3: Via Docker
Add this line to your n8n Docker environment:
```bash
-e N8N_COMMUNITY_PACKAGES="n8n-nodes-network-basic-nodes"
```

## 🚀 Included Nodes

### TCP Client & UDP Client
**📤 Send data via TCP/UDP protocols**
- **Category:** Actions
- **Icons:** TCP (📡), UDP (📻)

**Key Features:**
- Support for both TCP and UDP protocols
- Configurable connection and response timeouts
- Multiple text encodings (UTF-8, ASCII, Base64, Hex)
- Optional response waiting and connection persistence (TCP)
- Comprehensive error handling and status reporting

### TCP Server Trigger & UDP Server Trigger  
**🖥️ Listen for incoming TCP/UDP connections**
- **Category:** Triggers
- **Icons:** TCP Server (🖥️), UDP Server (📡)

**Key Features:**
- Automatic workflow triggering on data reception
- Configurable host binding (localhost or all interfaces)
- Connection limit control (TCP)
- Optional automatic response to clients
- Binary data support with base64 encoding

## 📋 Usage Examples

### Sending Data (Client Nodes)

**TCP Client:**
```json
{
  "host": "192.168.1.100",
  "port": 8080,
  "message": "Hello TCP Server!",
  "waitForResponse": true,
  "encoding": "utf8"
}
```

**UDP Client:**
```json
{
  "host": "192.168.1.100", 
  "port": 9090,
  "message": "Hello UDP Server!",
  "encoding": "utf8"
}
```

### Receiving Data (Server Triggers)

**Output Example:**
```json
{
  "protocol": "tcp",
  "server": { "host": "127.0.0.1", "port": 8080 },
  "client": { "remoteAddress": "192.168.1.50", "remotePort": 54321 },
  "data": "Received message",
  "encoding": "utf8",
  "bytes": 16,
  "timestamp": "2024-12-24T19:30:00.000Z"
}
```

## ⚙️ Default Settings

| Setting | TCP | UDP |
|---------|-----|-----|
| **Port** | 8080 | 9090 |
| **Host** | 127.0.0.1 | 127.0.0.1 |
| **Encoding** | UTF-8 | UTF-8 |
| **Connection Timeout** | 5000ms | N/A |
| **Response Timeout** | 3000ms | 3000ms |

## 🎯 Common Use Cases

### Client Nodes (Sending Data)
- **IoT Communication:** Send commands to smart devices
- **Legacy System Integration:** Communicate with older systems
- **Network Service Testing:** Test TCP/UDP services
- **Data Broadcasting:** Send data to multiple endpoints
- **Remote Monitoring:** Send status updates to monitoring systems

### Server Triggers (Receiving Data)
- **Webhook Alternatives:** Receive data from custom applications
- **Device Data Collection:** Collect data from IoT sensors
- **Network Monitoring:** Monitor network traffic and events
- **Custom API Endpoints:** Create simple TCP/UDP APIs
- **Real-time Notifications:** Receive instant notifications

## 🔧 Advanced Configuration

### Security Considerations
- **Bind to localhost (127.0.0.1)** for local testing only
- **Bind to specific IP** for controlled access
- **Use 0.0.0.0** only when needed for all interfaces
- **Implement proper firewall rules** for production use

### Performance Tips
- **TCP:** Use connection persistence for multiple messages
- **UDP:** Best for small, frequent messages
- **Encoding:** Use binary encodings for non-text data
- **Timeouts:** Adjust based on network conditions

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🐛 Issues & Support

Found a bug or need help? Please [open an issue](https://github.com/DiegoDVG/n8n-nodes-network-basic-nodes/issues).

## 📊 Related Projects

- [n8n](https://n8n.io/) - Workflow automation platform
- [n8n Community Nodes](https://docs.n8n.io/nodes/community-nodes/) - Community-built nodes
