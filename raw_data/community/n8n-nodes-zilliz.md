# n8n-nodes-zilliz

n8n社区节点包，用于连接Zilliz向量数据库云服务，专为AI Agent和RAG应用设计。

## 🚀 功能特性

### 基础向量操作
- **向量插入**: 将向量数据插入到Zilliz集合中
- **向量搜索**: 基于相似度搜索向量数据
- **向量查询**: 使用过滤条件查询向量数据
- **集合管理**: 创建、列出和管理向量集合

### 🎯 RAG 知识库构建
- **文档清洗**: 自动清理HTML标签、标准化文本格式
- **智能分块**: 支持可配置的文本分块策略，保持语义完整性
- **向量化存储**: 批量处理文档，保存向量和元数据
- **语义检索**: 高效的相似度搜索和结果过滤
- **AI Agent集成**: 为AI Agent优化的上下文格式化输出

### 技术特性
- **完全兼容**: 支持Zilliz Cloud的RESTful API
- **批量处理**: 支持大规模数据的高效处理
- **错误处理**: 完善的错误处理和重试机制
- **类型安全**: 完整的TypeScript类型定义

## 安装

```bash
npm install n8n-nodes-zilliz
```

## 配置

### 凭证设置

1. 在n8n中创建新的凭证
2. 选择 "Zilliz Cloud API"
3. 填入以下信息：
   - **API Key**: 您的Zilliz Cloud API密钥
   - **Cluster Endpoint**: 您的集群端点URL (例如: https://your-cluster-id.api.region.zillizcloud.com)

### 获取凭证信息

1. 登录 [Zilliz Cloud控制台](https://cloud.zilliz.com.cn/)
2. 创建或选择一个集群
3. 在API Keys页面生成API密钥
4. 从集群详情页面复制集群端点URL

## 节点说明

### 1. Zilliz Vector Store Insert

**用途**: 向Zilliz集合中插入向量数据

**配置参数**:
- **Database Name**: 数据库名称 (默认: default)
- **Collection Name**: 集合名称
- **Options**:
  - Clear Collection: 插入前是否清空集合
  - Text Field: 文本字段名称 (默认: text)
  - Vector Field: 向量字段名称 (默认: vector)
  - Metadata Fields: 额外的元数据字段

**输入数据格式**:
```json
{
  "vector": [0.1, 0.2, 0.3, 0.4, 0.5],
  "text": "示例文本内容",
  "category": "技术",
  "timestamp": "2024-01-01"
}
```

### 2. Zilliz Vector Store Load

**用途**: 从Zilliz集合中搜索和加载向量数据

**配置参数**:
- **Database Name**: 数据库名称
- **Collection Name**: 集合名称  
- **Query Vector**: 查询向量 (JSON数组或字段引用)
- **Top K**: 返回结果数量
- **Options**:
  - Filter Expression: 过滤表达式
  - Output Fields: 输出字段
  - Score Threshold: 相似度阈值

**查询向量格式**:
```json
[0.1, 0.2, 0.3, 0.4, 0.5]
```

或使用字段引用:
```
{{$json.embedding}}
```

### 3. Zilliz Vector Store

**用途**: 综合向量数据库操作节点

**支持操作**:
- Insert Vectors: 插入向量
- Search Vectors: 搜索向量
- Query Vectors: 查询向量
- Delete Vectors: 删除向量
- Create Collection: 创建集合
- List Collections: 列出集合

### 4. Zilliz Vector Store RAG 🎯

**用途**: 专为RAG（检索增强生成）应用设计的综合节点，支持完整的知识库构建和检索流程

**主要操作**:

#### createKnowledgeBase - 创建知识库
创建优化的向量集合用于存储文档知识库
```json
{
  "operation": "createKnowledgeBase",
  "embeddingSettings": {
    "dimension": 1536,
    "metricType": "COSINE"
  }
}
```

#### processAndStore - 文档处理和存储
对文档进行清洗、分块、向量化并存储到知识库
```json
{
  "operation": "processAndStore",
  "contentField": "content",
  "titleField": "title",
  "textProcessing": {
    "cleanText": true,
    "removeHtml": true,
    "chunkSize": 1000,
    "chunkOverlap": 200,
    "minChunkSize": 50
  }
}
```

#### semanticSearch - 语义搜索
基于向量相似度进行语义搜索
```json
{
  "operation": "semanticSearch",
  "queryText": "用户问题",
  "queryVector": "[0.1, 0.2, ...]",
  "searchOptions": {
    "maxResults": 5,
    "similarityThreshold": 0.7,
    "includeMetadata": true
  }
}
```

#### queryWithContext - AI Agent上下文查询
为AI Agent优化的上下文格式化输出
```json
{
  "operation": "queryWithContext",
  "queryText": "AI Agent查询",
  "searchOptions": {
    "maxResults": 3,
    "similarityThreshold": 0.8
  }
}
```

**RAG工作流示例**:
1. **文档** → **Embedding节点** → **RAG processAndStore**
2. **用户查询** → **Embedding节点** → **RAG queryWithContext** → **AI Agent**

详细使用指南请参考: [RAG_GUIDE.md](./RAG_GUIDE.md)

## 使用示例

### 示例1: 文档向量化存储

1. **Document → Text Splitter → Embeddings → Zilliz Insert**
   - 文档分割成块
   - 生成向量嵌入
   - 存储到Zilliz

### 示例2: 语义搜索

1. **HTTP Request → Embeddings → Zilliz Load**
   - 接收用户查询
   - 生成查询向量
   - 搜索相似内容

### 示例3: RAG应用

1. **User Input → Embeddings → Zilliz Load → LLM**
   - 用户输入
   - 向量搜索相关文档
   - 结合上下文生成回答

## 过滤表达式

支持Zilliz的过滤语法:

```javascript
// 数值过滤
"id > 100 and id < 1000"

// 字符串过滤
"category == 'technology'"

// 组合过滤
"score > 0.8 and category in ['tech', 'science']"

// 元数据过滤
"$meta['custom_field'] == 'value'"
```

## 故障排除

### 常见错误

1. **连接错误**: 检查API密钥和端点URL是否正确
2. **集合不存在**: 确保集合已创建或使用Create Collection操作
3. **向量维度不匹配**: 确保输入向量维度与集合定义一致
4. **权限错误**: 确保API密钥有足够权限

### 调试技巧

1. 启用节点的"Continue on Fail"选项查看详细错误
2. 使用List Collections操作验证连接
3. 检查向量数据格式是否正确

## 版本历史

### v0.2.5
- 初始版本发布
- 支持基本的CRUD操作
- 集成Zilliz Cloud RESTful API

## 贡献

欢迎提交Issue和Pull Request到项目仓库。

## 许可证

MIT License

## 相关链接

- [Zilliz Cloud官网](https://zilliz.com.cn/cloud)
- [Zilliz API文档](https://docs.zilliz.com.cn/reference/restful)
- [n8n社区节点文档](https://docs.n8n.io/integrations/community-nodes/)
