# n8n-nodes-crypttools

一个强大的 n8n 社区节点，提供全面的加密工具功能，包括加解密、哈希、HMAC、密钥派生和编码/解码等操作。

## 功能特性

### 🔐 支持的操作

- **加密 (Encrypt)**: 使用多种算法加密数据
- **解密 (Decrypt)**: 解密已加密的数据
- **哈希 (Hash)**: 生成数据的哈希值
- **HMAC**: 生成基于哈希的消息认证码
- **密钥派生 (Key Derivation)**: 使用 PBKDF2 或 Scrypt 派生密钥
- **Base64 编码/解码**: 转换 Base64 格式数据
- **Hex 编码/解码**: 转换十六进制格式数据

### 🛡️ 支持的加密算法

- **AES**: AES-128-CBC, AES-192-CBC, AES-256-CBC, AES-256-GCM
- **ChaCha20**: ChaCha20-Poly1305
- **DES**: DES-EDE3-CBC (3DES)

### 🔑 支持的哈希算法

- **MD5**: md5
- **SHA**: sha1, sha256, sha384, sha512
- **Blake2**: blake2b512, blake2s256

### 📁 支持的输入输出格式

- **UTF-8 字符串**: 普通文本
- **Base64**: Base64 编码数据
- **Hex**: 十六进制编码数据
- **JSON**: 自动解析 JSON 格式（仅解密输出）

### ⚙️ 密钥处理方式

- **原始密钥 (raw)**: 直接使用提供的密钥
- **SHA256 哈希**: 对密钥进行 SHA256 哈希处理
- **PBKDF2 派生**: 使用 PBKDF2 派生密钥

## 使用示例

### AES-256-CBC 加密解密

**加密:**
```
Operation: Encrypt
Algorithm: AES-256-CBC
Key: mySecretKey
Input Data: Hello, World!
Key Processing: SHA256 hash
Input Format: UTF-8 string
Output Format: Base64
```

**解密:**
```
Operation: Decrypt
Algorithm: AES-256-CBC
Key: mySecretKey
Input Data: [加密后的Base64数据]
Key Processing: SHA256 hash
Input Format: Base64
Output Format: UTF-8 string
```

### SHA256 哈希

```
Operation: Hash
Hash Algorithm: sha256
Input Data: Hello, World!
Input Format: UTF-8 string
Output Format: Hex
```

### HMAC 签名

```
Operation: HMAC
Hash Algorithm: sha256
Key: mySecretKey
Input Data: Hello, World!
Input Format: UTF-8 string
Output Format: Hex
```

### 密钥派生

```
Operation: Key derivation
Key Derivation Method: PBKDF2
Key: password123
Key Length: 32
Iterations: 100000
Output Format: Hex
```

## 兼容原有代码

此节点可以完美替代原生 Node.js 中的 crypto 模块功能。例如，原来的这段代码：

```javascript
const crypto = require('crypto');

class AESCipher {
    constructor(key) {
        const hash = crypto.createHash('sha256');
        hash.update(key);
        this.key = hash.digest();
    }

    encrypt(content, ivKey) {
        ivKey = ivKey ? Buffer.from(ivKey) : crypto.randomBytes(16);
        const cipher = crypto.createCipheriv('aes-256-cbc', this.key, ivKey);
        let encrypted = cipher.update(content);
        encrypted = Buffer.concat([encrypted, cipher.final()]);
        return Buffer.concat([ivKey, encrypted]).toString('base64');
    }

    decrypt(encrypt) {
        const encryptBuffer = Buffer.from(encrypt, 'base64');
        const ivKey = encryptBuffer.slice(0, 16);
        const encrypted = encryptBuffer.slice(16);
        const decipher = crypto.createDecipheriv('aes-256-cbc', this.key, ivKey);
        let decrypted = decipher.update(encrypted);
        decrypted = Buffer.concat([decrypted, decipher.final()]);
        return decrypted.toString();
    }
}
```

现在可以通过配置 CryptoTools 节点来实现相同的功能：

- **Operation**: Encrypt 或 Decrypt
- **Algorithm**: AES-256-CBC
- **Key Processing**: SHA256 hash
- **Input Format**: UTF-8 string
- **Output Format**: Base64

## 安装

1. 在 n8n 中打开 "Settings" -> "Community Nodes"
2. 输入包名: `n8n-nodes-crypttools`
3. 点击 "Install"

## 开发

```bash
# 克隆仓库
git clone <repository-url>
cd n8n-nodes-crypttools

# 安装依赖
npm install

# 构建项目
npm run build

# 代码检查
npm run lint

# 自动修复lint问题
npm run lintfix
```

## 贡献

欢迎提交 Pull Requests 和 Issues！

## 许可证

MIT License

## 版本历史

### 0.1.0
- 初始版本
- 支持加密、解密、哈希、HMAC、密钥派生等基本功能
- 支持多种算法和格式
- 完整的错误处理和参数验证
