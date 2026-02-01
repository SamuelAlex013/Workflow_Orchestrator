# n8n-nodes-variables-store

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

A community node package for n8n that provides global variables functionality - an alternative to the paid Variables feature.

一个为n8n提供全局变量功能的社区节点包 - n8n付费Variables功能的免费替代方案。

[English](#english) | [中文](#中文)

## English

## Features

- **Variables Get**: Retrieve global variables across workflows
- **Variables Set**: Store and manage global variables
- **Variables Manager**: Import/export and manage variable collections
- **Persistent Storage**: Variables are stored persistently in JSON files
- **Type Support**: String, Number, Boolean, and JSON data types
- **Cross-workflow Access**: Variables accessible across all workflows

## Installation

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter `n8n-nodes-variables-store`
4. Click **Install**

### Manual Installation

```bash
# In your n8n root directory
npm install n8n-nodes-variables-store
```

## Usage

### Variables Set Node

Use this node to create and update global variables:

**Operations:**
- **Set Variable**: Store a single variable with specified type
- **Set Multiple Variables**: Store multiple variables from a JSON object
- **Delete Variable**: Remove a specific variable
- **Clear All Variables**: Remove all stored variables

**Example - Set a Variable:**
```json
{
  "operation": "set",
  "variableName": "apiUrl",
  "variableValue": "https://api.example.com",
  "valueType": "string"
}
```

### Variables Get Node

Use this node to retrieve stored variables:

**Operations:**
- **Get Variable**: Retrieve a single variable value
- **Get All Variables**: Get all variables as an object
- **List Variable Names**: Get array of all variable names

**Example - Get a Variable:**
```json
{
  "operation": "get",
  "variableName": "apiUrl",
  "defaultValue": "https://default.api.com",
  "failOnMissing": false
}
```

### Variables Manager Node

Use this node for advanced variable management:

**Operations:**
- **Export Variables**: Export all variables as JSON
- **Import Variables**: Import variables from JSON data
- **Get Info**: Get storage information and statistics
- **Backup Variables**: Create a backup of current variables

## Variable Access

Unlike n8n's paid Variables feature that uses `$vars.variableName`, this community solution requires using the nodes to access variables. However, you can create a workflow pattern to simulate the `$vars` behavior:

1. Use **Variables Get** node at the start of workflows
2. Reference the output in subsequent nodes
3. Use expressions like `{{$node["Variables Get"].json["value"]}}`

## Storage

Variables are stored in JSON files in your n8n user directory:
- Location: `~/.n8n/variables/variables.json`
- Format: JSON key-value pairs
- Persistent across n8n restarts

## Data Types

Supported variable types:
- **String**: Text values
- **Number**: Numeric values (integers and floats)
- **Boolean**: true/false values
- **JSON**: Complex objects and arrays

## Examples

### Basic Variable Management

```javascript
// Set a configuration variable
{
  "operation": "set",
  "variableName": "environment",
  "variableValue": "production",
  "valueType": "string"
}

// Get the variable in another workflow
{
  "operation": "get",
  "variableName": "environment",
  "defaultValue": "development"
}
```

### Bulk Variable Operations

```javascript
// Set multiple variables at once
{
  "operation": "setMultiple",
  "variablesObject": {
    "apiUrl": "https://api.example.com",
    "timeout": 5000,
    "retryCount": 3,
    "debugMode": true
  }
}

// Export all variables for backup
{
  "operation": "export"
}
```

## Error Handling

- **Missing Variables**: Use `defaultValue` or `failOnMissing` options
- **Type Conversion**: Automatic type conversion based on `valueType`
- **Storage Errors**: Graceful error handling with detailed messages
- **Continue on Fail**: Supported for all operations

## Comparison with n8n Variables

| Feature | n8n Variables (Paid) | n8n-nodes-variables-store (Free) |
|---------|---------------------|---------------------------|
| Global Access | `$vars.name` | Node-based access |
| Persistence | ✅ | ✅ |
| Type Support | ✅ | ✅ |
| Cross-workflow | ✅ | ✅ |
| Import/Export | ❌ | ✅ |
| Backup/Restore | ❌ | ✅ |
| Cost | Paid feature | Free |

## Troubleshooting

### Variables Not Persisting
- Check n8n user directory permissions
- Ensure `~/.n8n/variables/` directory exists
- Verify JSON file is not corrupted

### Performance Considerations
- Variables are loaded from disk on each access
- Consider caching for high-frequency access
- Large JSON objects may impact performance

### Migration from n8n Variables
1. Export existing variables (if possible)
2. Use Variables Manager to import
3. Update workflows to use new nodes
4. Test thoroughly before production use

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

- GitHub Issues: Report bugs and feature requests
- n8n Community: Discuss usage and get help
- Documentation: Check this README and inline help

## Changelog

### v1.1.2
- **Repository Update**: Updated GitHub repository URL to correct owner (yingcaihuang)
- **Package Configuration**: Updated homepage and repository URLs in package.json
- **Documentation**: Updated all references to use correct GitHub repository

### v1.1.1
- **Critical Fix**: Fixed package.json node paths to match actual build output structure
- **npm Package Fix**: Resolved issue where n8n couldn't find node files in published package
- **Path Correction**: Updated node paths from `dist/nodes/` to `dist/` to match TypeScript build output

### v1.1.0
- **Bilingual Documentation**: Added comprehensive Chinese documentation alongside English
- **Improved Accessibility**: Better support for Chinese-speaking developers
- **Package Name Update**: Updated all references to `n8n-nodes-variables-store`
- **Enhanced Examples**: Updated example workflows with correct node types
- **Documentation Structure**: Reorganized README with language navigation

### v1.0.0
- Initial release
- Variables Get, Set, and Manager nodes
- Persistent JSON storage
- Type support for string, number, boolean, JSON
- Import/export functionality
- Comprehensive error handling

---

## 中文

## 功能特性

- **Variables Get** - 获取全局变量
- **Variables Set** - 设置和管理全局变量
- **Variables Manager** - 导入/导出和高级管理
- **持久化存储** - 变量在n8n重启后保持
- **跨工作流访问** - 在所有工作流中使用相同变量
- **多种数据类型** - 支持字符串、数字、布尔值、JSON

## 安装

### 社区节点安装（推荐）

1. 在n8n实例中进入 **设置 > 社区节点**
2. 点击 **安装社区节点**
3. 输入 `n8n-nodes-variables-store`
4. 点击 **安装**

### 手动安装

```bash
# 在n8n根目录中
npm install n8n-nodes-variables-store
```

## 使用方法

### Variables Set 节点

用于创建和更新全局变量：

**操作类型：**
- **设置变量** - 存储单个变量并指定类型
- **批量设置变量** - 从JSON对象设置多个变量
- **删除变量** - 删除指定变量
- **清除所有变量** - 删除所有存储的变量

**示例 - 设置变量：**
```json
{
  "operation": "set",
  "variableName": "apiUrl",
  "variableValue": "https://api.example.com",
  "valueType": "string"
}
```

### Variables Get 节点

用于获取存储的变量：

**操作类型：**
- **获取变量** - 获取单个变量值
- **获取所有变量** - 获取所有变量作为对象
- **列出变量名** - 获取所有变量名数组

**示例 - 获取变量：**
```json
{
  "operation": "get",
  "variableName": "apiUrl",
  "defaultValue": "https://default.api.com",
  "failOnMissing": false
}
```

### Variables Manager 节点

用于高级变量管理：

**操作类型：**
- **导出变量** - 将所有变量导出为JSON
- **导入变量** - 从JSON数据导入变量
- **获取信息** - 获取存储信息和统计数据
- **备份变量** - 创建当前变量的备份

## 变量访问

与n8n付费Variables功能使用 `$vars.variableName` 不同，这个社区解决方案需要使用节点来访问变量。但是，你可以创建工作流模式来模拟 `$vars` 行为：

1. 在工作流开始时使用 **Variables Get** 节点
2. 在后续节点中引用输出
3. 使用表达式如 `{{$node["Variables Get"].json["value"]}}`

## 存储

变量存储在n8n用户目录的JSON文件中：
- 位置：`~/.n8n/variables/variables.json`
- 格式：JSON键值对
- 持久性：n8n重启后保持

## 数据类型

支持的变量类型：
- **字符串** - 文本值
- **数字** - 数值（整数和浮点数）
- **布尔值** - true/false值
- **JSON** - 复杂对象和数组

## 使用示例

### 基本变量管理

```javascript
// 设置配置变量
{
  "operation": "set",
  "variableName": "environment",
  "variableValue": "production",
  "valueType": "string"
}

// 在另一个工作流中获取变量
{
  "operation": "get",
  "variableName": "environment",
  "defaultValue": "development"
}
```

### 批量变量操作

```javascript
// 一次设置多个变量
{
  "operation": "setMultiple",
  "variablesObject": {
    "apiUrl": "https://api.example.com",
    "timeout": 5000,
    "retryCount": 3,
    "debugMode": true
  }
}

// 导出所有变量进行备份
{
  "operation": "export"
}
```

## 与n8n Variables对比

| 功能 | n8n Variables (付费) | n8n-nodes-variables-store (免费) |
|---------|---------------------|---------------------------|
| 全局访问 | `$vars.name` | 基于节点的访问 |
| 持久化 | ✅ | ✅ |
| 类型支持 | ✅ | ✅ |
| 跨工作流 | ✅ | ✅ |
| 导入/导出 | ❌ | ✅ |
| 备份/恢复 | ❌ | ✅ |
| 成本 | 付费功能 | 免费 |

## 错误处理

- **缺失变量** - 使用 `defaultValue` 或 `failOnMissing` 选项
- **类型转换** - 基于 `valueType` 自动类型转换
- **存储错误** - 优雅的错误处理和详细消息
- **继续执行** - 所有操作都支持失败时继续

## 故障排除

### 变量不持久化
- 检查n8n用户目录权限
- 确保 `~/.n8n/variables/` 目录存在
- 验证JSON文件未损坏

### 性能考虑
- 变量在每次访问时从磁盘加载
- 考虑为高频访问进行缓存
- 大型JSON对象可能影响性能

## 项目亮点

### 方案优势
- **完全免费** - 替代n8n付费Variables功能
- **功能增强** - 提供额外的导入/导出、备份功能
- **开源** - 社区可以贡献和扩展
- **专业品质** - 完整的TypeScript实现和测试

### 技术特性
- **持久化存储** - 基于JSON文件的可靠存储
- **类型安全** - 完整的TypeScript支持
- **测试覆盖** - 11个单元测试确保质量
- **错误处理** - 完善的错误处理机制

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 添加测试
5. 提交拉取请求

## 许可证

MIT许可证 - 查看LICENSE文件了解详情

## 支持

- GitHub Issues：报告错误和功能请求
- n8n社区：讨论使用和获取帮助
- 文档：查看此README和内联帮助

## 更新日志

### v1.1.2
- **仓库更新**: 更新GitHub仓库URL为正确的所有者 (yingcaihuang)
- **包配置**: 更新package.json中的主页和仓库URL
- **文档**: 更新所有引用以使用正确的GitHub仓库

### v1.1.1
- **关键修复**: 修复package.json中的节点路径以匹配实际构建输出结构
- **npm包修复**: 解决了n8n无法在已发布包中找到节点文件的问题
- **路径纠正**: 将节点路径从 `dist/nodes/` 更新为 `dist/` 以匹配TypeScript构建输出

### v1.1.0
- **双语文档**: 添加完整的中文文档和英文文档
- **提升可访问性**: 更好地支持中文开发者
- **包名更新**: 更新所有引用为 `n8n-nodes-variables-store`
- **增强示例**: 更新示例工作流的正确节点类型
- **文档结构**: 重新组织README并添加语言导航

### v1.0.0
- 初始发布
- Variables Get、Set和Manager节点
- 持久化JSON存储
- 支持字符串、数字、布尔值、JSON类型
- 导入/导出功能
- 完善的错误处理
