# n8n-nodes-zalo-bot

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

Một community node cho n8n cho phép tích hợp với Zalo Bot Platform - nền tảng chatbot hàng đầu tại Việt Nam.

## Mục lục

- [Cài đặt](#cài-đặt)
- [Credentials](#credentials)
- [Operations](#operations)
- [Ví dụ sử dụng](#ví-dụ-sử-dụng)
- [Tương thích](#tương-thích)
- [Tài nguyên](#tài-nguyên)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

## Giới thiệu

Zalo Bot Platform là nền tảng cho phép các doanh nghiệp và nhà phát triển xây dựng chatbot tự động trên hệ sinh thái Zalo - ứng dụng nhắn tin phổ biến nhất tại Việt Nam với hơn 75 triệu người dùng. Node này cung cấp khả năng tích hợp đầy đủ với Zalo Bot API, cho phép bạn:

- Gửi và nhận tin nhắn tự động
- Quản lý webhook để xử lý tin nhắn real-time
- Gửi media (ảnh, sticker) và thông báo trạng thái
- Tích hợp với các hệ thống ERP, CRM, CDP
- Tự động hóa quy trình chăm sóc khách hàng

## Cài đặt

### Cài đặt từ n8n Community Nodes

1. Mở n8n instance của bạn
2. Vào **Settings** > **Community Nodes**
3. Chọn **Install a community node**
4. Nhập: `n8n-nodes-zalo-bot`
5. Nhấn **Install**

### Cài đặt thủ công

```bash
# Trong thư mục n8n của bạn
npm install n8n-nodes-zalo-bot
```

Sau khi cài đặt, khởi động lại n8n để node xuất hiện trong danh sách.

## Credentials

### Zalo Bot Credentials API

Để sử dụng node này, bạn cần tạo credentials với thông tin sau:

| Trường | Mô tả | Bắt buộc |
|--------|-------|----------|
| Bot Token | Token của bot được cấp từ Zalo Bot Platform | ✅ |

#### Cách lấy Bot Token

1. Truy cập [Zalo Bot Platform](https://bot.zapps.me/)
2. Đăng nhập và tạo bot mới
3. Sau khi tạo thành công, copy Bot Token từ dashboard
4. Dán token vào trường **Bot Token** trong n8n credentials

> **Lưu ý**: Bot Token được mã hóa và lưu trữ an toàn trong n8n. Node sẽ tự động test credentials khi bạn lưu.

## Operations

Node hỗ trợ các operations sau:

### 🔍 Bot Management

#### Get Me
Lấy thông tin cơ bản về bot.

**Tham số**: Không có

**Kết quả**: Thông tin bot bao gồm ID, tên, username

#### Get Updates
Lấy danh sách tin nhắn mới gửi đến bot.

**Tham số**:
- `timeout` (number): Thời gian chờ tối đa (giây), mặc định 30

**Kết quả**: Mảng các tin nhắn mới

### 🔗 Webhook Management

#### Set Webhook
Thiết lập webhook URL để nhận tin nhắn real-time.

**Tham số**:
- `webhookUrl` (string): URL endpoint để nhận webhook
- `secretToken` (string): Token bảo mật để xác thực webhook

#### Get Webhook Info
Lấy thông tin về webhook hiện tại.

**Tham số**: Không có

#### Delete Webhook
Xóa webhook đã thiết lập.

**Tham số**: Không có

### 💬 Messaging

#### Send Message
Gửi tin nhắn text đến người dùng.

**Tham số**:
- `chatId` (string): ID của cuộc trò chuyện
- `text` (string): Nội dung tin nhắn

#### Send Photo
Gửi ảnh đến người dùng.

**Tham số**:
- `chatId` (string): ID của cuộc trò chuyện  
- `photo` (string): URL của ảnh
- `caption` (string, tùy chọn): Mô tả ảnh

#### Send Sticker
Gửi sticker đến người dùng.

**Tham số**:
- `chatId` (string): ID của cuộc trò chuyện
- `sticker` (string): ID của sticker

#### Send Chat Action
Gửi trạng thái hoạt động (typing, uploading, etc.).

**Tham số**:
- `chatId` (string): ID của cuộc trò chuyện
- `action` (string): Loại hành động
  - `typing`: Đang gõ
  - `upload_photo`: Đang tải ảnh lên
  - `upload_video`: Đang tải video lên
  - `upload_voice`: Đang tải voice lên
  - `upload_document`: Đang tải tài liệu lên
  - `find_location`: Đang tìm vị trí
  - `record_video`: Đang quay video
  - `record_voice`: Đang ghi âm
  - `choose_sticker`: Đang chọn sticker

## Ví dụ sử dụng

### Workflow cơ bản: Auto-reply

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300],
      "webhookId": "zalo-webhook"
    },
    {
      "name": "Zalo Bot",
      "type": "n8n-nodes-zalo-bot.zaloBotNode", 
      "position": [450, 300],
      "parameters": {
        "operation": "sendMessage",
        "chatId": "={{$json.message.from.id}}",
        "text": "Xin chào! Cảm ơn bạn đã nhắn tin."
      },
      "credentials": {
        "zaloBotCredentialsApi": "zalo-bot-creds"
      }
    }
  ]
}
```

### Workflow nâng cao: Customer Support

```json
{
  "nodes": [
    {
      "name": "Zalo Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Check Message Type", 
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.message.text}}",
              "operation": "contains",
              "value2": "hỗ trợ"
            }
          ]
        }
      }
    },
    {
      "name": "Send Typing Status",
      "type": "n8n-nodes-zalo-bot.zaloBotNode",
      "parameters": {
        "operation": "sendChatAction", 
        "chatId": "={{$json.message.from.id}}",
        "action": "typing"
      }
    },
    {
      "name": "Query Database",
      "type": "n8n-nodes-base.mysql"
    },
    {
      "name": "Send Support Info",
      "type": "n8n-nodes-zalo-bot.zaloBotNode",
      "parameters": {
        "operation": "sendMessage",
        "chatId": "={{$json.message.from.id}}",
        "text": "Đây là thông tin hỗ trợ: {{$json.support_info}}"
      }
    }
  ]
}
```

### Tích hợp với CRM

```json
{
  "nodes": [
    {
      "name": "Daily CRM Sync",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "triggerTimes": {
          "hour": 9,
          "minute": 0
        }
      }
    },
    {
      "name": "Get Customer Data",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.yourcrm.com/customers",
        "method": "GET"
      }
    },
    {
      "name": "Send Daily Report",
      "type": "n8n-nodes-zalo-bot.zaloBotNode",
      "parameters": {
        "operation": "sendMessage",
        "chatId": "admin-chat-id",
        "text": "📊 Báo cáo khách hàng hôm nay:\n- Khách hàng mới: {{$json.new_customers}}\n- Đơn hàng: {{$json.orders}}\n- Doanh thu: {{$json.revenue}}"
      }
    }
  ]
}
```

## Tương thích

- **n8n version**: 0.190.0 trở lên
- **Node.js**: 16.x trở lên
- **Zalo Bot API**: v1.0

## Tài nguyên

- [Tài liệu Zalo Bot Platform](https://bot.zapps.me/docs/)
- [Hướng dẫn tạo Bot](https://bot.zapps.me/docs/create-bot)
- [API Reference](https://bot.zapps.me/docs/api-reference)
- [n8n Community](https://community.n8n.io/)

## Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Mở Pull Request

### Báo lỗi

Nếu bạn gặp lỗi, vui lòng tạo issue với thông tin:
- Phiên bản n8n
- Phiên bản node
- Mô tả lỗi chi tiết
- Workflow example (nếu có)

## Giấy phép

MIT License - xem file [LICENSE](LICENSE) để biết chi tiết.

## Tác giả

Được phát triển bởi cộng đồng n8n Việt Nam.

---

**Lưu ý**: Node này không phải là sản phẩm chính thức của Zalo hoặc n8n. Đây là community node được phát triển độc lập.

