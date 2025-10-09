# n8n 阿里云 OSS 节点

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
  <a href="https://github.com/felix-liuyj/n8n-nodes-alicloud-oss">
    <img src="./nodes/AlicloudOss/alicloud-oss.logo.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">n8n 阿里云 OSS 节点</h3>
<p align="center">
    为 n8n 工作流提供阿里云对象存储服务集成
    <br />
    <a href="https://github.com/felix-liuyj/n8n-nodes-alicloud-oss"><strong>查看详细文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/felix-liuyj/n8n-nodes-alicloud-oss">演示</a>
    ·
    <a href="https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/issues">报告Bug</a>
    ·
    <a href="https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/issues">功能请求</a>
</p>

## 目录

- [n8n 阿里云 OSS 节点](#n8n-阿里云-oss-节点)
  - [目录](#目录)
  - [关于项目](#关于项目)
    - [核心功能](#核心功能)
    - [技术栈](#技术栈)
  - [快速开始](#快速开始)
    - [环境要求](#环境要求)
    - [安装步骤](#安装步骤)
  - [项目结构](#项目结构)
  - [使用指南](#使用指南)
    - [配置凭据](#配置凭据)
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
    - [凭据配置](#凭据配置)
    - [节点参数](#节点参数)
  - [兼容性](#兼容性)
  - [开发贡献](#开发贡献)
  - [许可证](#许可证)
  - [联系方式](#联系方式)

## 关于项目

这是一个专为 [n8n](https://n8n.io/) 工作流自动化平台开发的社区节点，提供了完整的阿里云 OSS（对象存储服务）集成功能。

阿里云 OSS 是一种安全、经济高效且高度可靠的云存储服务，支持存储和访问任意数量的数据。通过此节点，你可以在 n8n 工作流中无缝集成文件上传、下载、管理等功能。

### 核心功能

- **🚀 高性能文件操作**：基于官方 ali-oss SDK，提供稳定可靠的文件操作
- **📁 完整的 CRUD 支持**：支持文件上传、下载、列表查询和删除操作
- **🔐 安全认证**：支持 Access Key 和自定义终端节点配置
- **📊 批量操作**：支持前缀过滤的批量对象管理
- **🎯 易于集成**：符合 n8n 标准，开箱即用
- **🌐 多区域支持**：支持阿里云所有 OSS 区域

### 技术栈

- **n8n 框架**：[n8n-workflow](https://n8n.io/)
- **阿里云 SDK**：[ali-oss](https://github.com/ali-sdk/ali-oss)
- **开发语言**：TypeScript
- **构建工具**：Gulp + TypeScript
- **代码规范**：ESLint + Prettier

## 快速开始

### 环境要求

- **n8n 版本**：>= 1.0.0
- **Node.js 版本**：>= 20.15
- **阿里云账户**：需要有效的 Access Key 和 OSS 存储桶

### 安装步骤

1. **通过 n8n 社区节点安装**

   按照 [n8n 社区节点安装指南](https://docs.n8n.io/integrations/community-nodes/installation/) 进行操作。

2. **通过 npm 安装**

   ```bash
   npm install n8n-nodes-alicloud-oss
   ```

3. **重启 n8n 服务**

   ```bash
   # 如果使用 npm 安装的 n8n
   n8n start
   
   # 如果使用 Docker
   docker restart n8n
   ```

4. **验证安装**

   在 n8n 编辑器中搜索 "Alicloud OSS" 节点，应该能看到新增的节点。

## 项目结构

```
├── /nodes/                    # n8n 节点实现
│  └── /AlicloudOss/          # 阿里云 OSS 节点
│     ├── AlicloudOss.node.ts # 主节点实现
│     └── alicloud-oss.logo.svg # 节点图标
├── /credentials/              # 凭据定义
│  └── AlicloudOssCredentialsApi.credentials.ts # 凭据配置
├── /dist/                     # 编译输出目录
├── .eslintrc.js              # ESLint 配置
├── .prettierrc.js            # Prettier 配置
├── gulpfile.js               # Gulp 构建配置
├── package.json              # 项目依赖和脚本
├── tsconfig.json             # TypeScript 配置
└── README.md                 # 项目文档
```

## 使用指南

### 配置凭据

在使用节点之前，需要配置阿里云 OSS 凭据：

1. **获取阿里云凭据**：
   - 登录 [阿里云控制台](https://ecs.console.aliyun.com/)
   - 创建或获取 Access Key ID 和 Access Key Secret
   - 创建 OSS 存储桶并记录区域信息

2. **在 n8n 中配置凭据**：

| 字段名           | 描述                                    | 必填 | 示例值                     |
|------------------|----------------------------------------|------|---------------------------|
| Access Key ID    | 阿里云 Access Key ID                   | ✅   | LTAI4G***************    |
| Access Key Secret| 阿里云 Access Key Secret               | ✅   | 3yX9***************      |
| 区域             | OSS 服务区域                           | ✅   | oss-cn-hangzhou          |
| 存储桶           | OSS 存储桶名称                         | ✅   | my-bucket                |
| 终端节点         | 自定义 OSS 终端节点（可选）              | ❌   | oss-cn-hangzhou.aliyuncs.com |

### 支持的操作

| 操作       | 描述                               | 用途场景                    |
|------------|------------------------------------|-----------------------------|
| **上传**   | 将文件上传到 OSS 存储桶             | 文件备份、数据存储            |
| **下载**   | 从 OSS 存储桶下载文件               | 文件获取、数据处理            |
| **列出对象** | 列出存储桶中的对象（支持前缀过滤）     | 文件管理、批量处理            |
| **删除**   | 从 OSS 存储桶删除指定对象           | 文件清理、存储空间管理        |

### 操作详细说明

#### 📤 上传操作

- **对象键**：文件在 OSS 中的完整路径（如：`documents/report.pdf`）
- **二进制属性**：包含文件数据的属性名称（默认：`data`）

```typescript
// 输入示例
{
  "data": {
    "filename": "report.pdf",
    "data": "binary file data"
  }
}
```

#### 📥 下载操作

- **对象键**：要下载文件的完整路径
- **二进制属性**：下载数据的属性名称（默认：`data`）

```typescript
// 输出示例
{
  "data": {
    "filename": "report.pdf",
    "data": "binary file data",
    "mimeType": "application/pdf"
  }
}
```

#### 📋 列出对象操作

- **前缀**（可选）：过滤对象的前缀（如：`images/` 列出 images 文件夹下的文件）
- **返回数量**：最多返回 1000 个对象

```typescript
// 输出示例
{
  "objects": [
    {
      "name": "documents/report.pdf",
      "size": 1024,
      "lastModified": "2023-12-01T10:00:00.000Z"
    }
  ]
}
```

#### 🗑️ 删除操作

- **对象键**：要删除文件的完整路径

```typescript
// 输出示例
{
  "deleted": true,
  "objectKey": "documents/report.pdf"
}
```

### 使用示例

**场景一：文档自动备份**
```
HTTP请求节点 → 文件处理 → Alicloud OSS上传 → 通知发送
```

**场景二：批量文件处理**
```
Alicloud OSS列出对象 → 循环处理 → Alicloud OSS下载 → 数据处理 → Alicloud OSS上传
```

**场景三：定时清理任务**
```
定时触发 → Alicloud OSS列出对象 → 条件判断 → Alicloud OSS删除
```

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
   git clone https://github.com/felix-liuyj/n8n-nodes-alicloud-oss.git
   cd n8n-nodes-alicloud-oss
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
   npm link n8n-nodes-alicloud-oss
   ```

### 生产环境部署

1. **通过 npm 安装**
   ```bash
   npm install n8n-nodes-alicloud-oss
   ```

2. **Docker 环境中安装**
   ```dockerfile
   FROM n8nio/n8n:latest
   RUN npm install n8n-nodes-alicloud-oss
   ```

3. **通过 n8n 社区节点管理器**
   - 在 n8n 界面中安装社区节点
   - 搜索 "n8n-nodes-alicloud-oss"
   - 点击安装并重启 n8n

## 配置参数

### 凭据配置

| 参数名           | 类型     | 必填 | 描述                      | 示例值                        |
|-----------------|---------|------|---------------------------|-------------------------------|
| accessKeyId     | string  | ✅   | 阿里云 Access Key ID       | LTAI4G***************        |
| accessKeySecret | string  | ✅   | 阿里云 Access Key Secret   | 3yX9***************          |
| region          | string  | ✅   | OSS 服务区域                | oss-cn-hangzhou              |
| bucket          | string  | ✅   | OSS 存储桶名称              | my-bucket                    |
| endpoint        | string  | ❌   | 自定义 OSS 终端节点         | oss-cn-hangzhou.aliyuncs.com |

### 节点参数

#### 上传操作
| 参数名         | 类型     | 必填 | 描述                    | 默认值 |
|---------------|---------|------|-------------------------|--------|
| objectKey     | string  | ✅   | 对象键（文件路径）        | -      |
| binaryProperty| string  | ❌   | 二进制数据属性名          | data   |

#### 下载操作
| 参数名         | 类型     | 必填 | 描述                    | 默认值 |
|---------------|---------|------|-------------------------|--------|
| objectKey     | string  | ✅   | 对象键（文件路径）        | -      |
| binaryProperty| string  | ❌   | 输出二进制数据属性名      | data   |

#### 列出对象操作
| 参数名     | 类型     | 必填 | 描述                        | 默认值 |
|----------|---------|------|-----------------------------|--------|
| prefix   | string  | ❌   | 对象前缀过滤器                | -      |

#### 删除操作
| 参数名     | 类型     | 必填 | 描述                    | 默认值 |
|----------|---------|------|-------------------------|--------|
| objectKey| string  | ✅   | 要删除的对象键（文件路径） | -      |

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
git clone https://github.com/felix-liuyj/n8n-nodes-alicloud-oss.git
cd n8n-nodes-alicloud-oss

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
**项目链接**：[https://github.com/felix-liuyj/n8n-nodes-alicloud-oss](https://github.com/felix-liuyj/n8n-nodes-alicloud-oss)

---

**相关资源**：
- [n8n 官方文档](https://docs.n8n.io/)
- [阿里云 OSS 文档](https://www.alibabacloud.com/help/zh/oss/)
- [ali-oss SDK 文档](https://github.com/ali-sdk/ali-oss)
- [n8n 社区节点开发指南](https://docs.n8n.io/integrations/creating-nodes/)

<!-- 链接定义 -->
[contributors-shield]: https://img.shields.io/github/contributors/felix-liuyj/n8n-nodes-alicloud-oss.svg?style=flat-square
[contributors-url]: https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/felix-liuyj/n8n-nodes-alicloud-oss.svg?style=flat-square
[forks-url]: https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/network/members
[stars-shield]: https://img.shields.io/github/stars/felix-liuyj/n8n-nodes-alicloud-oss.svg?style=flat-square
[stars-url]: https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/stargazers
[issues-shield]: https://img.shields.io/github/issues/felix-liuyj/n8n-nodes-alicloud-oss.svg?style=flat-square
[issues-url]: https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/issues
[license-shield]: https://img.shields.io/github/license/felix-liuyj/n8n-nodes-alicloud-oss.svg?style=flat-square
[license-url]: https://github.com/felix-liuyj/n8n-nodes-alicloud-oss/blob/master/LICENSE.md
