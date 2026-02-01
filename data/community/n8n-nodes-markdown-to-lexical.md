# n8n-nodes-markdown-to-lexical

一个用于将 Markdown 转换为 Lexical 格式的 n8n 社区节点包。

## 功能特性

- 🔄 将 Markdown 文本转换为 Lexical 编辑器格式
- 📝 支持丰富的 Markdown 语法元素
- 🔗 完全集成到 n8n 工作流中
- ⚡ 基于 Lexical 无头编辑器的高性能转换

## 支持的 Markdown 元素

该节点支持以下 Markdown 语法元素的转换：

- **标题** (H1-H6)
- **引用块** (Blockquotes)
- **列表** (有序和无序列表)
- **代码块** 和行内代码
- **链接**
- **文本标记** (粗体、斜体等)
- **自定义Block标签** (支持任意属性的自定义块元素)

### 自定义Block标签

该节点支持自定义的 `<block>` 标签，可以包含任意属性：

```markdown
<block type="note" name="重要提示" title="标题" content="内容" custom="自定义值"/>
```

**属性映射规则：**
- `type` → `blockType`
- `name` → `blockName`
- 其他属性保持原名
- 支持任意自定义属性

**导出时的属性映射：**
- `blockType` → `type`
- `blockName` → `name`
- 其他属性保持原名

## 安装

### 通过 n8n 社区节点安装

1. 在 n8n 实例中，转到 **设置 > 社区节点**
2. 选择 **安装**
3. 输入 `n8n-nodes-markdown-to-lexical`
4. 点击 **安装**

### 手动安装

要手动安装该节点包，请在 n8n 根文件夹中运行以下命令：

```bash
npm install n8n-nodes-markdown-to-lexical
```

## 使用方法

1. 在 n8n 工作流中添加 **Markdown to Lexical** 节点
2. 在节点配置中输入要转换的 Markdown 文本
3. 执行节点，转换后的 Lexical 格式数据将在 `lexical` 字段中输出

### 输入

- **Markdown**: 要转换的 Markdown 文本（支持多行输入）

### 输出

节点将在输出数据的 `lexical` 字段中返回转换后的 Lexical 编辑器状态对象。

## 示例

### 输入 Markdown:
```markdown
# 标题

这是一个 **粗体** 文本和一个 [链接](https://example.com)。

- 列表项 1
- 列表项 2

> 这是一个引用块

<block type="note" name="重要提示" title="注意事项" content="这是一个自定义块元素" priority="high"/>
```

### 输出:
转换后的数据将包含一个 `lexical` 字段，其中包含 Lexical 编辑器的 JSON 状态。

## 技术实现

该节点基于以下技术构建：

- **Lexical**: Meta 开发的现代富文本编辑器框架
- **@lexical/headless**: 用于服务器端转换的无头编辑器
- **@lexical/markdown**: Markdown 转换器
- **n8n-workflow**: n8n 工作流集成

## 开发

### 环境要求

- Node.js >= 20.15
- npm 或 pnpm

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/hubo502/n8n-markdown-to-lexical.git
cd n8n-markdown-to-lexical

# 安装依赖
npm install

# 开发模式（监听文件变化）
npm run dev

# 构建
npm run build

# 代码格式化
npm run format

# 代码检查
npm run lint

# 修复代码问题
npm run lintfix
```

### 项目结构

```
├── nodes/
│   └── MarkdownToLexical/
│       ├── MarkdownToLexical.node.ts    # 主节点实现
│       └── MarkdownToLexical.node.json  # 节点配置
├── utilities/
│   ├── convertMarkdownToLexical.ts      # 核心转换逻辑
│   └── nodes/
│       └── block/
│           ├── BlockNode.ts             # 自定义Block节点实现
│           └── BlockTransformer.ts      # Block标签转换器
├── package.json                         # 项目配置
└── tsconfig.json                        # TypeScript 配置
```

## 许可证

MIT License

## 作者

**Boris Hu**
- Email: hubo502@gmail.com
- GitHub: [hubo502](https://github.com/hubo502)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 版本历史

### 0.2.0
- 新增自定义Block标签支持
- 支持任意属性的自定义块元素
- 完善属性映射和导出功能
- 增强Markdown到Lexical的转换能力

### 0.1.0
- 初始版本
- 基本的 Markdown 到 Lexical 转换功能
- 支持标题、列表、链接、代码块等常用元素

---

如果您觉得这个项目有用，请给它一个 ⭐️！