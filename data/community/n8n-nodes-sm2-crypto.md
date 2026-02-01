# n8n SM2 密码学节点

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<p align="center">
<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/felix-liuyj/n8n-nodes-sm2-crypto">
    <img src="./nodes/Sm2Crypto/sm2.logo.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">n8n SM2 密码学节点</h3>
<p align="center">
    为 n8n 工作流提供国密 SM2 加密解密功能
    <br />
    <a href="https://github.com/felix-liuyj/n8n-nodes-sm2-crypto"><strong>查看详细文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/felix-liuyj/n8n-nodes-sm2-crypto">演示</a>
    ·
    <a href="https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/issues">报告Bug</a>
    ·
    <a href="https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/issues">功能请求</a>
</p>

## 目录

- [n8n SM2 密码学节点](#n8n-sm2-密码学节点)
  - [目录](#目录)
  - [关于项目](#关于项目)
    - [核心功能](#核心功能)
    - [技术栈](#技术栈)
  - [快速开始](#快速开始)
    - [环境要求](#环境要求)
    - [安装步骤](#安装步骤)
  - [项目结构](#项目结构)
  - [使用指南](#使用指南)
    - [支持的操作](#支持的操作)
    - [操作详细说明](#操作详细说明)
    - [使用示例](#使用示例)
  - [开发命令](#开发命令)
    - [构建和开发](#构建和开发)
    - [代码质量](#代码质量)
    - [发布](#发布)
  - [部署选项](#部署选项)
    - [本地开发环境](#本地开发环境)
    - [生产环境部署](#生产环境部署)
  - [配置参数](#配置参数)
    - [节点参数](#节点参数)
  - [兼容性](#兼容性)
  - [开发贡献](#开发贡献)
  - [许可证](#许可证)
  - [联系方式](#联系方式)

## 关于项目

这是一个专为 [n8n](https://n8n.io/) 工作流自动化平台开发的社区节点，提供了完整的 SM2 密码学功能集成。

SM2 是基于椭圆曲线的公钥密码算法，是中国国家密码标准（GM/T 0003-2012）的一部分。通过此节点，你可以在 n8n 工作流中无缝集成 SM2 加密和解密功能，确保数据传输的安全性。

### 核心功能

- **🔐 国密 SM2 算法**：基于官方 sm-crypto 库，提供标准的 SM2 加密解密
- **🚀 高性能处理**：支持大文本和二进制数据的快速加密解密
- **📊 灵活配置**：支持自定义字段名称和数据格式
- **🎯 易于集成**：符合 n8n 标准，开箱即用
- **🛡️ 安全可靠**：严格遵循国密标准，确保加密安全性
- **💡 智能错误处理**：友好的错误提示和异常处理

### 技术栈

- **n8n 框架**：[n8n-workflow](https://n8n.io/)
- **密码学库**：[sm-crypto](https://github.com/JuneAndGreen/sm-crypto)
- **开发语言**：TypeScript
- **构建工具**：Gulp + TypeScript
- **代码规范**：ESLint + Prettier

## 快速开始

### 环境要求

- **n8n 版本**：>= 1.0.0
- **Node.js 版本**：>= 20.15
- **已测试版本**：n8n 1.x

### 安装步骤

1. **通过 n8n 社区节点安装**

   按照 [n8n 社区节点安装指南](https://docs.n8n.io/integrations/community-nodes/installation/) 进行操作。

2. **通过 npm 安装**

   ```bash
   npm install n8n-nodes-sm2-crypto
   ```

3. **重启 n8n 服务**

   ```bash
   # 如果使用 npm 安装的 n8n
   n8n start
   
   # 如果使用 Docker
   docker restart n8n
   ```

4. **验证安装**

   在 n8n 编辑器中搜索 "SM2 Crypto" 节点，应该能看到新增的节点。

## 项目结构

```
├── /nodes/                    # n8n 节点实现
│  └── /Sm2Crypto/            # SM2 密码学节点
│     ├── Sm2Crypto.node.ts   # 主节点实现
│     └── sm2-crypto.svg      # 节点图标
├── /dist/                     # 编译输出目录
├── .eslintrc.js              # ESLint 配置
├── .prettierrc.js            # Prettier 配置
├── gulpfile.js               # Gulp 构建配置
├── package.json              # 项目依赖和脚本
├── tsconfig.json             # TypeScript 配置
└── README.md                 # 项目文档
```

## 使用指南

### 支持的操作

| 操作       | 描述                               | 用途场景                    |
|------------|------------------------------------|------------------------------|
| **加密**   | 使用 SM2 公钥加密明文数据           | 数据保护、安全传输            |
| **解密**   | 使用 SM2 私钥解密密文              | 数据解密、信息恢复            |

### 操作详细说明

#### 🔒 加密操作

- **令牌（密钥）**：SM2 公钥（64位十六进制格式，不含 '04' 前缀）
- **输入字段名称**：包含待加密数据的属性名称（默认：`data`）

```typescript
// 输入示例
{
  "data": "Hello, World!",
  "publicKey": "7b93a5e9d8c4f2a1b6e3c7d9f4a2b8e1c5d6f9a2b4e7c1d8f3a6b9c2e5d7f8a1"
}
```

#### 🔓 解密操作

- **令牌（密钥）**：SM2 私钥（64位十六进制格式）
- **输入字段名称**：包含待解密数据的属性名称（默认：`data`）

```typescript
// 输入示例  
{
  "data": "04a1b2c3d4e5f6...",
  "privateKey": "3f2a1b4c5e6d7f8a9b2c3d4e5f6a7b8c9d2e3f4a5b6c7d8e9f1a2b3c4d5e6f7"
}
```

### 使用示例

**场景一：敏感数据加密**
```
HTTP请求节点 → 数据处理 → SM2加密 → 数据库存储
```

**场景二：数据解密处理**
```
数据库查询 → SM2解密 → 数据处理 → API响应
```

**场景三：文件安全传输**
```
文件读取 → SM2加密 → 文件传输 → SM2解密 → 文件处理
```

### 输出格式

**加密输出：**
```json
{
  "data": "Hello, World!",
  "ciphertext": "04a1b2c3d4e5f6..."
}
```

**解密输出：**
```json
{
  "data": "04a1b2c3d4e5f6...",
  "plaintext": "Hello, World!"
}
```

**错误输出：**
```json
{
  "data": "invalid data",
  "error": "Invalid key format"
}
```

### 密钥格式要求

- **公钥**：64字符十六进制字符串（未压缩格式，不含 '04' 前缀）
- **私钥**：64字符十六进制字符串

## 开发命令

### 构建和开发

- `npm run build` - 完整构建（TypeScript 编译 + 图标复制）
- `npm run dev` - 开发模式，TypeScript 监听模式
- `npm run format` - 使用 Prettier 格式化代码
- `npm run lint` - 运行 ESLint 检查
- `npm run lintfix` - 自动修复 ESLint 问题

### 代码质量

- `npm run prepublishOnly` - 发布前检查（构建 + lint）
- `npm run publicPublish` - 发布到 npm（公开访问）

### 发布

```bash
# 发布新版本
npm version patch|minor|major
npm run publicPublish
```

## 部署选项

### 本地开发环境

1. **克隆项目**
   ```bash
   git clone https://github.com/felix-liuyj/n8n-nodes-sm2-crypto.git
   cd n8n-nodes-sm2-crypto
   ```

2. **安装依赖**
   ```bash
   npm install
   ```

3. **开发模式**
   ```bash
   npm run dev
   ```

4. **链接到本地 n8n**
   ```bash
   # 创建全局链接
   npm link
   
   # 在 n8n 项目中链接
   cd /path/to/n8n
   npm link n8n-nodes-sm2-crypto
   ```

### 生产环境部署

1. **通过 npm 安装**
   ```bash
   npm install n8n-nodes-sm2-crypto
   ```

2. **Docker 环境中安装**
   ```dockerfile
   FROM n8nio/n8n:latest
   RUN npm install n8n-nodes-sm2-crypto
   ```

3. **通过 n8n 社区节点管理器**
   - 在 n8n 界面中安装社区节点
   - 搜索 "n8n-nodes-sm2-crypto"
   - 点击安装并重启 n8n

## 配置参数

### 节点参数

#### 加密操作
| 参数名         | 类型     | 必填 | 描述                    | 默认值 |
|---------------|---------|------|-------------------------|--------|
| token         | string  | ✅   | SM2 公钥（十六进制）      | -      |
| inputFieldName| string  | ❌   | 输入数据字段名           | data   |

#### 解密操作
| 参数名         | 类型     | 必填 | 描述                    | 默认值 |
|---------------|---------|------|-------------------------|--------|
| token         | string  | ✅   | SM2 私钥（十六进制）      | -      |
| inputFieldName| string  | ❌   | 输入数据字段名           | data   |

## 兼容性

| 环境要求        | 最低版本    | 推荐版本    | 测试版本     |
|---------------|------------|------------|-------------|
| n8n           | 1.0.0      | 最新版本    | 1.x         |
| Node.js       | 20.15      | 20.x LTS   | 20.15+      |
| TypeScript    | 5.0        | 5.8+       | 5.8.2       |

## 开发贡献

欢迎参与项目开发！请遵循以下步骤：

1. **Fork 项目**
2. **创建功能分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送到分支** (`git push origin feature/AmazingFeature`)
5. **创建 Pull Request**

**开发环境搭建**：

```bash
# 克隆项目
git clone https://github.com/felix-liuyj/n8n-nodes-sm2-crypto.git
cd n8n-nodes-sm2-crypto

# 安装依赖
npm install

# 开发模式
npm run dev

# 构建项目
npm run build

# 代码检查
npm run lint
```

## 许可证

本项目基于 MIT 许可证开源。详细信息请查看 [LICENSE.md](LICENSE.md) 文件。

## 联系方式

**作者**：Felix Liu (Cambria Tech)  
**邮箱**：felixliuyj@gmail.com  
**项目链接**：[https://github.com/felix-liuyj/n8n-nodes-sm2-crypto](https://github.com/felix-liuyj/n8n-nodes-sm2-crypto)

---

**相关资源**：
- [n8n 官方文档](https://docs.n8n.io/)
- [SM2 密码算法规范](https://tools.ietf.org/html/draft-shen-sm2-ecdsa-02)
- [sm-crypto 库文档](https://github.com/JuneAndGreen/sm-crypto)
- [n8n 社区节点开发指南](https://docs.n8n.io/integrations/creating-nodes/)

<!-- 链接定义 -->
[contributors-shield]: https://img.shields.io/github/contributors/felix-liuyj/n8n-nodes-sm2-crypto.svg?style=flat-square
[contributors-url]: https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/felix-liuyj/n8n-nodes-sm2-crypto.svg?style=flat-square
[forks-url]: https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/network/members
[stars-shield]: https://img.shields.io/github/stars/felix-liuyj/n8n-nodes-sm2-crypto.svg?style=flat-square
[stars-url]: https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/stargazers
[issues-shield]: https://img.shields.io/github/issues/felix-liuyj/n8n-nodes-sm2-crypto.svg?style=flat-square
[issues-url]: https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/issues
[license-shield]: https://img.shields.io/github/license/felix-liuyj/n8n-nodes-sm2-crypto.svg?style=flat-square
[license-url]: https://github.com/felix-liuyj/n8n-nodes-sm2-crypto/blob/master/LICENSE.md
