# n8n-nodes-dty-erpnext-cn

这是一个n8n社区节点包，为DTY ERPNext中国版本提供集成功能。

## 功能特性

- 与ERPNext中国版本的无缝集成
- 支持多种ERPNext操作
- 简化的认证流程
- 中文友好的界面

## 安装

```bash
npm install n8n-nodes-dty-erpnext-cn
```

## GitHub 仓库

项目地址：[https://github.com/guinanlin/n8n-nodes-dty-erpnext-cn](https://github.com/guinanlin/n8n-nodes-dty-erpnext-cn)

## 使用方法

1. 在n8n中安装此节点包
2. 配置ERPNext连接凭据
3. 使用提供的节点进行ERPNext操作

## 节点列表

- **erpNextcn**: ERPNext中国版本集成节点

## 开发

### 前置要求

- Node.js 20+
- pnpm

### 安装依赖

```bash
pnpm install
```

### 构建

```bash
pnpm run build
```

### 本地测试

```bash
pnpm run dev
```

### 代码检查

```bash
pnpm run lint
pnpm run lintfix
```

## 发布到npm

1. 确保已登录npm：
   ```bash
   npm login
   ```
   $ npm version patch

2. 构建项目：
   ```bash
   pnpm run build
   ```

3. 发布到npm：
   ```bash
   npm publish
   ```

## 许可证

[MIT](LICENSE.md)
