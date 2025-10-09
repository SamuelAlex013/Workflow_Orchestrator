# n8n-nodes-douyin-transcript

[English](README_EN.md) | 简体中文

这是一个用于 [n8n](https://n8n.io/) 的自定义节点包，可以帮助您从抖音视频中提取文字内容。该节点利用阿里云语音大模型进行视频内容转写。

## 功能特点

- 支持从抖音分享链接中提取视频信息
- 使用阿里云语音大模型进行视频内容转写
- 支持长视频内容处理
- 提供详细的转写结果，包括时间戳信息

## 安装说明

### 方法一：通过 n8n 安装

1. 打开 n8n 设置面板
2. 进入 `社区节点` 页面
3. 搜索 "n8n-nodes-douyin-transcript"
4. 点击安装

### 方法二：手动安装

在您的 n8n 安装目录下运行：

```bash
npm install n8n-nodes-douyin-transcript
```

## 配置说明

使用本节点前，您需要：

1. 注册阿里云账号并开通大力云百炼的模型服务
2. 获取以下认证信息：
   - API Key

## 使用方法

1. 在 n8n 工作流中添加 "douyinTranscript" 节点
2. 配置阿里云认证信息
3. 输入抖音视频分享链接
4. 运行工作流，等待转写完成

### 输入格式

1. 节点接受以下格式的抖音分享链接或者分享的完整文本内容：

```
https://v.douyin.com/xxxxx/
```

2. 文本提取默认使用 `Paraformer-V2`大模型, 您也可以选择 `Paraformer-V1`, 但 `Paraformer-V1` 可能在长视频处理上有性能问题。同时也可选择 `Fun-ASR` 模型。

### 输出格式

节点将输出 JSON 格式的转写结果：

```json
{
  "download_url": "视频下载地址",
  "title": "视频标题",
  "fullText": "视频完整的文本信息，选择提取文本时返回",
  "subtitleEntries": [
    {
      "startTime": 0,
      "endTime": 7994,
      "text": "识别的句子数组，大模型返回的原始信息，可供二次加工处理，选择提取文本时返回"
    }
  ],
  "srtSubtitle": "srt字幕格式文本信息，选择提取文本时返回"
}
```

## 使用示例

1. **简单的视频转写流程**
   - 添加 "抖音转写" 节点
   - 配置视频链接
   - 连接到文本处理节点或保存结果

## 常见问题

1. **Q: 支持多长的视频？**
   A: 目前支持最长 2 小时的视频转写。

2. **Q: 转写准确率如何？**
   A: 使用大力云百炼的模型服务，准确率可达 95% 以上。

3. **Q: 处理速度多快？**
   A: 通常 1 分钟视频需要 10-20 秒处理时间。

## 更新日志

请查看 [CHANGELOG.md](CHANGELOG.md) 了解详细的更新历史。

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

本项目采用 [MIT](LICENSE) 许可证。

## 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件至 [feiguan@foxmail.com]

## 致谢

感谢以下项目和服务：

- [n8n](https://n8n.io/)
- [大力云百炼的模型服务](https://www.aliyun.com/product/bailian)
