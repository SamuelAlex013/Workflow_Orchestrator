# 使用案例

## URL验证案例
```json
{
  "nodes": [
    {
      "parameters": {
        "path": "1d476f93-cc5b-431e-96a5-71111846e39d",
        "responseMode": "responseNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -620,
        -140
      ],
      "id": "21c66249-0213-4c84-9495-219b6fdcd41c",
      "name": "Webhook",
      "webhookId": "1d476f93-cc5b-431e-96a5-71111846e39d"
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $('Webhook').item.json.query.echostr }}",
        "options": {}
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.4,
      "position": [
        -260,
        -140
      ],
      "id": "013fc8c7-4261-4a4e-875c-e65305bd2167",
      "name": "Respond to Webhook1"
    },
    {
      "parameters": {
        "content": "## URL验证",
        "height": 240,
        "width": 940
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        -680,
        -220
      ],
      "id": "5d24d3e0-001c-4709-8932-ffb331f89e40",
      "name": "Sticky Note"
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Respond to Webhook1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "02b4f549b31e5afb7ac0434f27e8e1e51494096eb26622aff0d1c16686021c54"
  }
}
```

## 明文消息回复案例
```json
{
  "nodes": [
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "=<xml>\n  <ToUserName><![CDATA[{{ $('Webhook1').item.json.body.xml.fromusername }}]]></ToUserName>\n  <FromUserName><![CDATA[{{ $('Webhook1').item.json.body.xml.tousername }}]]></FromUserName>\n  <CreateTime>{{ $('Webhook1').item.json.body.xml.createtime }}</CreateTime>\n  <MsgType><![CDATA[text]]></MsgType>\n  <Content><![CDATA[用户发送：{{ $('Webhook1').item.json.body.xml.content }}]]></Content>\n</xml>\n",
        "options": {}
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.4,
      "position": [
        -140,
        100
      ],
      "id": "114d02ef-ec8d-4386-8e3c-824fba7883e1",
      "name": "Respond to Webhook"
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "1d476f93-cc5b-431e-96a5-71111846e39d",
        "responseMode": "responseNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -620,
        100
      ],
      "id": "32abe73e-bb72-4aaf-8ae1-df35c0847a19",
      "name": "Webhook1",
      "webhookId": "1d476f93-cc5b-431e-96a5-71111846e39d"
    }
  ],
  "connections": {
    "Webhook1": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "02b4f549b31e5afb7ac0434f27e8e1e51494096eb26622aff0d1c16686021c54"
  }
}
```

## AES加密消息回复案例
```json
{
  "nodes": [
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $json.body }}",
        "options": {}
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.4,
      "position": [
        300,
        340
      ],
      "id": "cf53af1f-c5db-42d6-9cbb-702cab656739",
      "name": "Respond to Webhook2"
    },
    {
      "parameters": {
        "content": "## 收到加密消息",
        "height": 220,
        "width": 940
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        -680,
        280
      ],
      "id": "e92f2655-f801-4e67-888f-5a89ce3de0b2",
      "name": "Sticky Note2"
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "1d476f93-cc5b-431e-96a5-71111846e39d",
        "responseMode": "responseNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -620,
        340
      ],
      "id": "bdf2bfef-4770-4972-a7b8-9051005800fa",
      "name": "Webhook2",
      "webhookId": "1d476f93-cc5b-431e-96a5-71111846e39d"
    },
    {
      "parameters": {
        "resource": "sign",
        "operation": "sign:decrypt",
        "signature": "={{ $json.query.signature }}",
        "timestamp": "={{ $json.query.timestamp }}",
        "nonce": "={{ $json.query.nonce }}",
        "encrypt_type": "={{ $json.query.encrypt_type }}",
        "encrypt_str": "={{ $json.body.xml.encrypt }}",
        "token": "xxxxxxxxx",
        "aesKey": "xxxxxxxx"
      },
      "type": "CUSTOM.wechatOfficialAccountNode",
      "typeVersion": 1,
      "position": [
        -360,
        340
      ],
      "id": "6ea59c79-c04e-4500-91cc-5b63ea8e10a6",
      "name": "消息解密",
      "credentials": {
        "wechatOfficialAccountCredentialsApi": {
          "id": "POmYAAOAHjQ4kTJG",
          "name": "BL公众号"
        }
      }
    },
    {
      "parameters": {
        "resource": "sign",
        "operation": "sign:encrypt",
        "content": "=<xml>\n  <ToUserName><![CDATA[{{ $json.fromusername }}]]></ToUserName>\n  <FromUserName><![CDATA[{{ $json.tousername }}]]></FromUserName>\n  <CreateTime>{{ $json.createtime }}</CreateTime>\n  <MsgType><![CDATA[text]]></MsgType>\n  <Content><![CDATA[用户发送：{{ $json.content }}]]></Content>\n</xml> ",
        "token": "xxxxxxxx",
        "aesKey": "xxxxxxxx"
      },
      "type": "CUSTOM.wechatOfficialAccountNode",
      "typeVersion": 1,
      "position": [
        -40,
        340
      ],
      "id": "c58d7a58-6ea1-47da-a3d0-0293ce28b25a",
      "name": "消息加密",
      "credentials": {
        "wechatOfficialAccountCredentialsApi": {
          "id": "POmYAAOAHjQ4kTJG",
          "name": "BL公众号"
        }
      }
    }
  ],
  "connections": {
    "Webhook2": {
      "main": [
        [
          {
            "node": "消息解密",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "消息解密": {
      "main": [
        [
          {
            "node": "消息加密",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "消息加密": {
      "main": [
        [
          {
            "node": "Respond to Webhook2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "02b4f549b31e5afb7ac0434f27e8e1e51494096eb26622aff0d1c16686021c54"
  }
}
```

## request 节点引用凭证
> 注意：请提前调用该凭证下的其他节点，直接使用request可能凭证是过期的
```json
{
  "nodes": [
    {
      "parameters": {
        "url": "https://api.weixin.qq.com/cgi-bin/material/get_materialcount",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "wechatOfficialAccountCredentialsApi",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        440,
        340
      ],
      "id": "1b23baa1-64ea-49eb-a7a0-611240bd6d43",
      "name": "HTTP Request",
      "credentials": {
        "wechatOfficialAccountCredentialsApi": {
          "id": "POmYAAOAHjQ4kTJG",
          "name": "BL公众号"
        }
      }
    }
  ],
  "connections": {
    "HTTP Request": {
      "main": [
        []
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "02b4f549b31e5afb7ac0434f27e8e1e51494096eb26622aff0d1c16686021c54"
  }
}
```

# 功能
## 用户标签
- 编辑标签
- 获取标签下粉丝列表
- 获取标签列表
- 获取用户身上的标签列表
- 删除标签
- 创建标签
- 批量为用户取消标签
- 批量为用户打标签
## 用户
- 设置用户备注名
- 获取用户列表
- 获取用户信息
- 获取黑名单列表
- 取消拉黑用户
- 拉黑用户
## 模板
- 发送模板消息
- 获取模板列表
- 删除模板
## 发布
- 发布草稿
- 发布状态轮询
- 获取成功发布列表
- 获取已发布文章
- 删除发布
## 其他
- 生成短Key
- 获取长信息
- 生成带参数的二维码
## 菜单
- 查询
- 获取当前菜单配置
- 删除
- 创建
## 素材
- 上传临时素材
- 上传永久素材
- 获取素材列表
- 获取临时素材
- 获取永久素材
- 删除永久素材
- 获取素材总数
## 草稿
- 修改草稿
- 获取草稿列表
- 获取草稿
- 删除草稿
- 获取草稿总数
- 新建草稿
## 评论
- 取消精选
- 删除回复
- 回复评论
- 打开评论
- 标记精选
- 查看评论
- 删除评论
- 关闭评论




