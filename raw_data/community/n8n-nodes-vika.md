# n8n-nodes-vika

这是一个 n8n 社区节点包，让你可以在 n8n 工作流中使用维格表格(Vika)。

维格表格是一个强大的在线协作表格平台，提供了丰富的数据管理和协作功能。

[n8n](https://n8n.io/) 是一个[公平代码许可](https://docs.n8n.io/reference/license/)的工作流自动化平台。

## 目录

- [安装](#安装)
- [操作](#操作)
- [凭据配置](#凭据配置)
- [兼容性](#兼容性)
- [使用示例](#使用示例)
- [资源链接](#资源链接)
- [版本历史](#版本历史)

## 安装

按照 n8n 社区节点文档中的[安装指南](https://docs.n8n.io/integrations/community-nodes/installation/)进行安装。

### 通过 n8n 界面安装

1. 在 n8n 中，转到 **设置 > 社区节点**
2. 选择 **安装**
3. 输入 `n8n-nodes-vika`
4. 同意风险并安装

### 通过 npm 安装

如果你是自托管的 n8n 实例：

```bash
npm install n8n-nodes-vika
```

然后重启 n8n 实例。

## 操作

维格表格节点支持以下操作：

### 记录 (Record)

- **获取记录**: 通过记录ID获取单个记录的详细信息
- **获取所有记录**: 获取数据表中的所有记录，支持筛选、排序和分页
- **创建记录**: 在数据表中创建新记录
- **更新记录**: 更新现有记录的字段值
- **删除记录**: 删除指定的记录

### 支持的功能

- ✅ 字段筛选 - 指定返回的字段
- ✅ 视图支持 - 基于特定视图获取记录
- ✅ 排序功能 - 多字段排序支持
- ✅ 分页控制 - 控制返回的记录数量
- ✅ 错误处理 - 完善的错误处理机制
- ✅ 批量操作 - 支持批量处理多个输入项

## 凭据配置

使用维格表格节点需要配置 API 凭据：

### 维格表格 API 凭据

| 字段 | 类型 | 必填 | 描述 |
|------|------|------|------|
| API Token | string | 是 | 维格表格的 API Token |
| Base URL | string | 否 | API 基础 URL (默认: https://api.vika.cn) |

### 获取 API Token

1. 登录[维格表格工作台](https://vika.cn/)
2. 进入"开发者配置"页面
3. 创建或查看现有的 API Token
4. 复制 Token 并在 n8n 中配置凭据

### 权限要求

确保你的 API Token 具有以下权限：
- 读取数据表记录
- 创建数据表记录（如需创建操作）
- 更新数据表记录（如需更新操作）
- 删除数据表记录（如需删除操作）

## 兼容性

- **最低 n8n 版本**: 0.190.0
- **推荐 n8n 版本**: 1.0.0+
- **测试版本**: 1.0.0, 1.1.0, 1.2.0
- **Node.js 版本**: 20.15+

### 已知兼容性问题

目前没有已知的兼容性问题。

## 使用示例

### 示例 1: 获取数据表中的所有记录

```json
{
  "nodes": [
    {
      "name": "获取维格表格记录",
      "type": "n8n-nodes-vika.vika",
      "parameters": {
        "resource": "record",
        "operation": "getAll",
        "datasheetId": "dst1234567890",
        "options": {
          "maxRecords": 100,
          "fields": "姓名,邮箱,电话"
        }
      }
    }
  ]
}
```

### 示例 2: 创建新记录

```json
{
  "nodes": [
    {
      "name": "创建维格表格记录",
      "type": "n8n-nodes-vika.vika",
      "parameters": {
        "resource": "record",
        "operation": "create",
        "datasheetId": "dst1234567890",
        "fields": {
          "field": [
            {
              "name": "姓名",
              "value": "张三"
            },
            {
              "name": "邮箱",
              "value": "zhangsan@example.com"
            }
          ]
        }
      }
    }
  ]
}
```

### 示例 3: 更新记录状态

```json
{
  "nodes": [
    {
      "name": "更新记录状态",
      "type": "n8n-nodes-vika.vika",
      "parameters": {
        "resource": "record",
        "operation": "update",
        "datasheetId": "dst1234567890",
        "recordId": "rec1234567890",
        "fields": {
          "field": [
            {
              "name": "状态",
              "value": "已完成"
            }
          ]
        }
      }
    }
  ]
}
```

### 示例工作流: 表单数据同步

这个工作流演示如何将表单提交的数据同步到维格表格：

1. **Webhook 节点** - 接收表单提交
2. **维格表格节点** - 创建新记录
3. **邮件节点** - 发送确认邮件

## 常见问题

### Q: 如何获取数据表ID？
A: 数据表ID可以在维格表格的URL中找到，格式为 `dst` 开头的字符串。

### Q: 支持哪些字段类型？
A: 支持维格表格的所有字段类型，包括文本、数字、日期、选择、附件等。

### Q: 如何处理大量数据？
A: 使用分页功能，设置合适的 `pageSize` 和 `maxRecords` 参数。

### Q: API 有频率限制吗？
A: 是的，维格表格 API 有频率限制。建议在工作流中添加适当的延迟。

## 资源链接

- [n8n 社区节点文档](https://docs.n8n.io/integrations/community-nodes/)
- [维格表格官方文档](https://developers.vika.cn/)
- [维格表格 API 参考](https://developers.vika.cn/api/introduction)
- [项目 GitHub 仓库](https://github.com/your-username/n8n-nodes-vika)
- [问题反馈](https://github.com/your-username/n8n-nodes-vika/issues)

## 贡献

欢迎贡献代码！请查看 [贡献指南](CONTRIBUTING.md) 了解详细信息。

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/your-username/n8n-nodes-vika.git
cd n8n-nodes-vika

# 安装依赖
pnpm install

# 构建项目
pnpm run build

# 运行测试
pnpm run test

# 代码格式化
pnpm run format

# 代码检查
pnpm run lint
```

## 版本历史

### v0.1.0 (2024-01-01)

**首次发布**

- ✨ 支持维格表格记录的增删改查操作
- ✨ 完整的 API Token 认证支持
- ✨ 丰富的查询选项（筛选、排序、分页）
- ✨ 完善的错误处理机制
- ✨ 中文界面支持
- 📚 完整的文档和使用示例

**支持的操作:**
- 获取记录
- 获取所有记录
- 创建记录
- 更新记录
- 删除记录

## 许可证

[MIT](LICENSE.md)

## 支持

如果你觉得这个项目有用，请给它一个 ⭐️！

如果你遇到问题或有功能建议，请[创建一个 issue](https://github.com/your-username/n8n-nodes-vika/issues)。
