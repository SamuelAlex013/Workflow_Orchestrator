# n8n-nodes-wechat-enterprise-bot

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

企业微信群机器人节点for n8n，支持发送文本和Markdown消息到企业微信群。

[View on GitHub](https://github.com/maple412/n8n-nodes-wechat-enterprise-bot) | [npm Package](https://www.npmjs.com/package/n8n-nodes-wechat-enterprise-bot)

## 安装

### 社区节点安装

1. 在n8n中，进入 **Settings** → **Community Nodes**
2. 选择 **Install**
3. 输入包名：`n8n-nodes-wechat-enterprise-bot`
4. 点击 **Install**

### npm安装

```bash
npm install n8n-nodes-wechat-enterprise-bot
```

### Docker安装

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_CUSTOM_EXTENSIONS="n8n-nodes-wechat-enterprise-bot" \
  n8nio/n8n
```

## 使用方法

### 获取企业微信机器人Webhook

1. 在企业微信群中添加机器人
2. 选择"自定义机器人"
3. 复制Webhook地址中的key值

### 配置节点

1. 在n8n工作流中添加"企业微信机器人"节点
2. 填写机器人Webhook Key
3. 选择消息类型（文本或Markdown）
4. 输入消息内容
5. 可选择@用户设置

## 功能特点

- ✅ 支持文本消息
- ✅ 支持Markdown消息
- ✅ 支持@所有人
- ✅ 支持@指定用户ID
- ✅ 支持@指定手机号
- ✅ 完整的错误处理
- ✅ 支持批量处理

## 节点参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 机器人Webhook Key | string | ✓ | 企业微信机器人的Key值 |
| 消息类型 | options | ✓ | text或markdown |
| 消息内容 | string | ✓ | 要发送的消息内容 |
| @所有人 | boolean | - | 是否@群内所有人 |
| @指定用户 | string | - | 用户ID列表，逗号分隔 |
| @指定手机号 | string | - | 手机号列表，逗号分隔 |

## 示例

### 发送文本消息

```json
{
  "webhookKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "messageType": "text",
  "content": "Hello, 这是来自n8n的消息！",
  "mentionedAll": true
}
```

### 发送Markdown消息

```json
{
  "webhookKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "messageType": "markdown",
  "content": "## 重要通知\n**系统状态**：正常\n- 服务器响应时间：100ms\n- 错误率：0%"
}
```

## 版本历史

- **1.0.0**: 初始版本，支持文本和Markdown消息发送

## 许可证

MIT

## 贡献

欢迎提交Issue和Pull Request！

## 支持

如有问题请提交Issue或发邮件至：your.email@example.com