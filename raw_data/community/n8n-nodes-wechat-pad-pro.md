# n8n-nodes-wechat-pad-pro

---

这是一个 n8n 社区节点，允许您在 n8n 工作流中连接 [WeChatPadPro](https://github.com/WeChatPadPro/WeChatPadPro)。当前分支支持的版本为`0859`.

WeChatPadPro 是基于微信Pad协议的微信管理工具，可以用于实现微信消息的自动化收发和联系人、账号管理等功能。

[n8n](https://n8n.io/) 是一个 [fair-code licensed](https://docs.n8n.io/reference/license/) 的工作流自动化平台。

## 安装

有两种安装此社区节点的方法：

1.  **[通过 n8n 图形界面安装](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/)**：在 n8n 的 "Community Nodes" 界面中搜索 `n8n-nodes-wechat-pad-pro` 并安装。
2.  **[通过命令行手动安装](https://docs.n8n.io/integrations/community-nodes/installation/manual-install/)**：如果您的 n8n 实例不支持图形界面安装，可以手动安装。

## 凭证

要使用此节点，您需要配置 WeChatPadPro API 凭证。

1.  **BaseUrl**: 您的 WeChatPadPro 服务的 URL 地址。
2.  **AuthKey**: 您的 WeChatPadPro 服务的授权密钥。

您需要自行搭建 WeChatPadPro 服务来获取这些凭证。

## 操作

本节点支持以下操作：

### 用户 (User)
* 获取个人资料信息

### 消息 (Message)
* 发送文本消息
* 发送图片消息

## 触发器 (Trigger)

### 接收新消息

当收到新消息时触发工作流。

* `接收文本消息`: 仅在收到文本消息 (msg_type == 1) 时触发。
* `接收图片消息`: 仅在收到图片消息 (msg_type == 3) 时触发。
* `接收音频消息`: 仅在收到音频消息 (msg_type == 34) 时触发。
* `接收表情消息`: 仅在收到表情消息 (msg_type ==  47) 时触发。
* `接收视频消息`: 仅在收到视频消息 (msg_type ==  47) 时触发。

## 兼容性

* **最低 n8n 版本**: 此节点遵循 n8n 的 `n8nNodesApiVersion: 1`，建议在最新的 n8n 版本上使用。
* **Node.js 版本**: 需要 `>=20.15` 版本。

## 资源

* [n8n 社区节点文档](https://docs.n8n.io/integrations/#community-nodes)
* [WeChatPadPro 项目地址](https://github.com/WeChatPadPro/WeChatPadPro)
* [本项目 GitHub 仓库](https://github.com/LegendLeo/n8n-nodes-wechat-pad-pro)
