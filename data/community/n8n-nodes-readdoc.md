# n8n-nodes-readdoc

![n8n-nodes-readdoc](https://img.shields.io/badge/n8n-community--node-blue)

这是一个用于读取doc/docx文档内容的n8n社区节点。

## 功能特性

- 支持读取 .doc 和 .docx 文件
- 多种输出格式：纯文本、HTML、Markdown
- 提取文档元数据（字数统计、字符数等）
- 保持原始二进制数据（可选）
- 错误处理和继续执行选项

## 安装

```bash
# 在你的n8n实例中安装
npm install n8n-nodes-readdoc
```

## 使用方法

1. 将包含doc/docx文件的二进制数据传递给节点
2. 选择输出格式（纯文本、HTML或Markdown）
3. 配置其他选项（如是否包含样式信息）
4. 节点将输出提取的文档内容和元数据

## 输入数据格式

节点需要包含二进制数据的输入，二进制数据应该是doc或docx文件。

## 输出数据格式

```json
{
  "content": "提取的文档内容",
  "fileName": "document.docx",
  "fileType": "docx",
  "format": "text",
  "metadata": {},
  "wordCount": 150,
  "characterCount": 1200
}
```

## 支持的文件格式

- `.doc` - Microsoft Word 97-2003文档
- `.docx` - Microsoft Word 2007+文档

## 开发

本项目使用TypeScript开发，基于n8n节点开发框架。

### 构建

```bash
pnpm run build
```

### 开发模式

```bash
pnpm run dev
```

### 代码格式化

```bash
pnpm run format
```

### 代码检查

```bash
pnpm run lint
```

## 依赖

- `mammoth` - 用于处理.docx文件
- `textract` - 用于处理.doc文件

## 许可证

MIT

## 贡献

欢迎提交Pull Request和Issue！
