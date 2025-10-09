# N8N HashiCorp Vault Node
![npm version](https://img.shields.io/npm/v/n8n-nodes-hashi-vault)
![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-hashi-vault)
![license](https://img.shields.io/npm/l/n8n-nodes-hashi-vault)
![GitHub last commit](https://img.shields.io/github/last-commit/luisra51/n8n-nodes-hashi-vault)

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is a **security-hardened version** of the N8N HashiCorp Vault integration node. Created after discovering security vulnerabilities in the original `n8n-nodes-hashicorp-vault` package.

## ⚠️ Security Notice

This package was created as a secure alternative after identifying:
- **Critical vulnerabilities** in dependencies (form-data CVE)
- **Missing source repository** for original package
- **Potential supply chain attack** indicators

## 🚀 Features

- **AppRole Authentication**: Secure authentication using HashiCorp Vault's AppRole method
- **Token Authentication**: Direct token-based authentication
- **KV v1 & v2 Support**: Works with both Key-Value secret engines
- **Namespace Support**: Enterprise Vault namespace functionality
- **SSL Configuration**: Flexible SSL certificate validation options
- **Security Hardened**: Updated dependencies to resolve CVE vulnerabilities

## 📦 Installation

```bash
# Install from local package (recommended)
npm install file:./path/to/this/package

# Or from npm
npm install n8n-nodes-hashi-vault
```

## 🔧 Configuration

### Credentials Setup

1. **Vault URL**: Your Vault instance URL (e.g., `https://vault.example.com:8200`)
2. **Authentication Method**: Choose between `AppRole` or `Token`
3. **AppRole Configuration** (if selected):
   - **Role ID**: Your AppRole Role ID
   - **Secret ID**: Your AppRole Secret ID
4. **Token Configuration** (if selected):
   - **Token**: Your Vault token
5. **Optional Settings**:
   - **Namespace**: Vault namespace (Enterprise feature)
   - **API Version**: KV engine version (v1 or v2)
   - **Ignore SSL Issues**: Skip SSL certificate validation

## ⚙️ Vault Configuration Examples

### Token Authentication
**Best for**: Development, testing, or when you need simple setup.
**Advantages**: Quick setup, no additional Vault configuration needed.

```bash
# Create a token with KV access policy
vault policy write n8n-kv-policy - <<EOF
path "secret/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
path "secret/metadata/*" {
  capabilities = ["list"]
}
EOF

# Generate token (expires in 24h)
vault token create -policy=n8n-kv-policy -ttl=24h
```

### AppRole Authentication
**Best for**: Production, automated workflows, enhanced security.
**Advantages**: Token rotation, audit trails, granular permissions, no long-lived tokens in N8N.

```bash
# Enable AppRole auth method
vault auth enable approle

# Create policy
vault policy write n8n-kv-policy - <<EOF
path "secret/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
path "secret/metadata/*" {
  capabilities = ["list"]
}
EOF

# Create AppRole
vault write auth/approle/role/n8n-role \
    token_policies="n8n-kv-policy" \
    token_ttl=1h \
    token_max_ttl=4h

# Get Role ID and Secret ID for N8N configuration
vault read auth/approle/role/n8n-role/role-id
vault write -f auth/approle/role/n8n-role/secret-id
```

### Node Operations

#### Read Secret
```json
{
  "secretEngine": "secret",
  "secretPath": "myapp/database",
  "version": 0
}
```

#### Write Secret
```json
{
  "secretEngine": "secret",
  "secretPath": "myapp/database",
  "secretData": "{\"username\": \"myuser\", \"password\": \"mypassword\"}"
}
```

#### Delete Secret
```json
{
  "secretEngine": "secret",
  "secretPath": "myapp/database"
}
```

#### List Secrets
```json
{
  "secretEngine": "secret",
  "listPath": "myapp/"
}
```

## 🔒 Security Changes Made

### Dependency Updates
- ✅ **axios**: Updated to `^1.7.9` (fixes form-data CVE)
- ✅ **form-data**: Resolved critical vulnerability (CWE-330)
- ✅ **Development dependencies**: Updated to latest secure versions

### Code Integrity
- ✅ **Source verification**: Full code review completed
- ✅ **No external endpoints**: Confirmed communication only with configured Vault
- ✅ **TypeScript conversion**: Improved type safety
- ✅ **Clean package**: No suspicious dependencies or scripts

## 🧪 Testing

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test

# Security audit
npm audit
```

## 📋 Development

```bash
# Development mode
npm run dev

# Format code
npm run format

# Lint code
npm run lint
```

## 🚨 Security Audit Results

```bash
npm audit
# Expected: 0 vulnerabilities found
```

## 🤝 Contributing

This is a security-focused fork. When contributing:

1. **Security first**: All changes must maintain or improve security posture
2. **Dependency management**: Keep dependencies minimal and up-to-date
3. **Code review**: All changes require security review
4. **Testing**: Include security tests for new features

## 📋 TODO - Performance Optimizations

### 🚀 Token Management
- [ ] **Token Caching**: Implement AppRole token caching with TTL to reduce authentication requests
- [ ] **Token Renewal**: Add automatic token renewal before expiration
- [ ] **Connection Pooling**: Reuse HTTP connections to Vault

### 🗄️ Secret Caching
- [ ] **Secure Secret Caching**: Implement encrypted in-memory or Redis-based secret caching
- [ ] **TTL Management**: Configurable TTL for cached secrets with automatic expiration
- [ ] **Cache Invalidation**: Manual and automatic cache clearing mechanisms
- [ ] **Memory Security**: Implement secure memory handling and cleanup for cached secrets

### ⚡ Performance Monitoring
- [ ] **Metrics Collection**: Track response times, cache hit ratios, and authentication frequency
- [ ] **Memory Usage**: Monitor cache memory consumption and implement LRU eviction

## 📜 License

MIT License - See LICENSE file for details

## 🛡️ Security

- **Report vulnerabilities**: Create an issue with `[SECURITY]` prefix
- **Response time**: Security issues will be addressed within 24 hours
- **Disclosure**: Coordinated disclosure preferred

## 🙏 Acknowledgments

- Original concept from the `n8n-nodes-hashicorp-vault` package
- Security improvements by @luisra51
- N8N community for the excellent automation platform

---

**⚠️ Always verify package integrity and run security audits before deployment in production environments.**