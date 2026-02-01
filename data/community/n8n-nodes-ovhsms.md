# n8n-nodes-ovhsms

## 📦 Installation

### Community Nodes Installation

1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install** and enter: `n8n-nodes-ovhsms`
3. Click **Install** and restart n8n

### Manual Installation

```bash
# Install in your n8n root directory
npm install n8n-nodes-ovhsms
```

### Docker Installation

```dockerfile
# Add to your n8n Dockerfile
RUN cd /data && npm install n8n-nodes-ovhsms
```

## 🔑 Authentication

### API Credentials Setup

1. **Create OVH API Credentials**
   - Visit: [OVH API Console](https://api.ovh.com/createToken/)
   - Choose your region endpoint
   - Set required permissions (see below)
   - Generate your credentials

2. **Configure in n8n**
   - Create new **OVH API** credential
   - Enter your **Application Key**, **Application Secret**, and **Consumer Key**
   - Select your **Endpoint** region

### Required API Permissions

#### Core Services
```bash
# Account Management
GET /me*
PUT /me*
POST /me*
DELETE /me*

# Sms Services
GET /sms*
PUT /sms*
POST /sms*
DELETE /sms*

```
