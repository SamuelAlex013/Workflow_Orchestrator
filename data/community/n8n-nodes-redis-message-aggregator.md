![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-redis-message-aggregator

🚀 **n8n custom node để gom tin nhắn từ nhiều trigger với Redis và intelligent delay**

Giải quyết vấn đề tin nhắn rời rạc trong chatbot/webhook bằng cách gom nhiều tin nhắn thành một với chiến lược chờ thông minh.

## 📦 Cài đặt

```bash
npm install n8n-nodes-redis-message-aggregator
```

Sau khi cài đặt, restart n8n để load nodes mới.

## ⚡ Tính năng chính

- ✅ **Gom tin nhắn thông minh**: Tự động gom nhiều tin nhắn rời rạc thành một
- ✅ **2 chiến lược xử lý**: Smart Wait và Immediate on Complete
- ✅ **Real-time waiting**: Node thật sự chờ, không cần external scheduler
- ✅ **Redis support**: Hỗ trợ Redis local và cloud (Upstash, Redis Cloud)
- ✅ **Connection testing**: Node test kết nối Redis riêng biệt
- ✅ **Flexible keys**: Hỗ trợ user ID, group ID, hoặc kết hợp

## 🎯 Vấn đề giải quyết

**Trước khi sử dụng:**

```
Trigger 1: "Xin"     → Xử lý ngay → Response "?"
Trigger 2: "chào"    → Xử lý ngay → Response "?"
Trigger 3: "bạn!"    → Xử lý ngay → Response "?"
```

**Sau khi sử dụng:**

```
Trigger 1: "Xin"     → Lưu & chờ
Trigger 2: "chào"    → Lưu & chờ
Trigger 3: "bạn!"    → Lưu & chờ 5s → Gom: "Xin chào bạn!" → Response
```

## 🚀 Bắt đầu nhanh

### Bước 1: Setup Redis

**Option A - Upstash Redis (Khuyến nghị cho người mới):**

1. Đăng ký tại [upstash.com](https://upstash.com) (free tier)
2. Tạo Redis database mới
3. Copy connection string dạng: `redis://default:xxx@xxx.upstash.io:6379`

**Option B - Redis local:**

```bash
# Docker
docker run -d -p 6379:6379 redis:alpine

# macOS
brew install redis && redis-server

# Ubuntu
sudo apt install redis-server
```

### Bước 2: Tạo Credentials

1. Trong n8n, vào **Credentials** → **New** → **Redis API**
2. Chọn connection type:
   - **Connection String**: Paste connection string từ Upstash
   - **Host & Port**: Nhập localhost:6379 cho Redis local

### Bước 3: Test Connection

1. Thêm node **Redis Connection Test**
2. Chọn credentials vừa tạo
3. Chọn **Complete Test** và execute
4. Xem kết quả: ✅ Connection successful!

### Bước 4: Basic Workflow

```
[Manual Trigger] → [Redis Message Aggregator] → [Set] (để xem kết quả)
```

**Cấu hình Redis Message Aggregator:**

- **Key**: `user123` (hoặc bất kỳ string nào)
- **Message Content**: `Xin chào!`
- **Wait Time**: `5` (giây)
- **Strategy**: `Smart Wait`

## 📚 Chi tiết Nodes

### Redis Message Aggregator

Node chính để gom tin nhắn với 2 chiến lược đơn giản:

#### 🧠 Smart Wait (Khuyến nghị)

Chờ thông minh - chỉ output khi chắc chắn không có tin nhắn mới.

**Khi nào dùng:** Chatbot, webhook nhận tin nhắn liên tiếp

**Ví dụ:**

```javascript
// Input: 3 tin nhắn với key "user123"
// - "Xin" (10:00:00)
// - "chào" (10:00:03)
// - "bạn!" (10:00:06)

// Output sau 5 giây không có tin mới (10:00:11):
{
  "status": "messages_aggregated",
  "key": "user123",
  "aggregatedMessage": "Xin chào bạn!",
  "messageCount": 3,
  "trigger": "smart_timeout"
}
```

#### 🎯 Immediate on Complete

Trả về ngay khi phát hiện tin nhắn kết thúc bằng từ được định nghĩa.

**Khi nào dùng:** Khi muốn response nhanh với những từ kết thúc cụ thể

**Cấu hình:**

- **End Words**: `xong, rồi, nhé, ok, done` (ngăn cách bởi dấu phẩy)

**Ví dụ:**

```javascript
// End Words: "xong, rồi, nhé"
"Xin chào"     → Chưa hoàn chỉnh → Lưu & chờ
"bạn nhé"      → Hoàn chỉnh (kết thúc bằng "nhé") → Output ngay: "Xin chào bạn nhé"
```

### Redis Connection Test

Node để test và troubleshoot Redis connection.

**Test Types:**

- **Basic Connection**: Chỉ test PING
- **Read/Write Test**: Test SET/GET/DEL
- **Server Info**: Lấy thông tin Redis server
- **Complete Test**: Chạy tất cả tests above

## 🔧 Cấu hình nâng cao

### Key Patterns

Sử dụng key linh hoạt cho các tình huống khác nhau:

```javascript
// Chat 1-1
key = 'user_123';

// Group chat
key = 'group_456';

// User trong group cụ thể
key = 'user_123_group_456';

// Session based
key = 'session_abc123';

// Multi-tenant
key = 'tenant_A_user_123';
```

### Redis Options

Tùy chỉnh connection cho performance tốt hơn:

- **Connection Timeout**: 5000ms (mặc định)
- **Command Timeout**: 3000ms (mặc định)
- **Max Retries**: 1 (mặc định)

### Strategy Selection Guide

| Strategy              | Use Case          | Output Timing             | Best For          |
| --------------------- | ----------------- | ------------------------- | ----------------- |
| Smart Wait            | Chatbot responses | Sau X giây no new message | Real-time chat    |
| Immediate on Complete | Quick responses   | Khi detect end words      | Fast interactions |

## 💡 Workflow Examples

### Example 1: Chatbot với Smart Wait

```
[Webhook] → [Redis Message Aggregator] → [OpenAI/ChatGPT] → [Response]
```

**Cấu hình:**

- Key: `{{$json.userId}}` (từ webhook payload)
- Message: `{{$json.message}}`
- Strategy: Smart Wait
- Wait Time: 3 giây

### Example 2: Quick Response với End Words

```
[Webhook] → [Redis Message Aggregator] → [Filter: Complete Messages] → [Processing]
```

**Cấu hình:**

- Key: `{{$json.groupId}}_{{$json.userId}}`
- Strategy: Immediate on Complete
- End Words: `xong, rồi, nhé, ok, done`

## 🔍 Troubleshooting

### ❌ "Connection failed"

1. Dùng **Redis Connection Test** node để kiểm tra
2. Verify credentials và connection string
3. Check firewall/network access

### ❌ "Key và Message Content là bắt buộc"

- Đảm bảo cả 2 fields đều có giá trị
- Kiểm tra expressions nếu dùng dynamic values

### ❌ Không có output

- Cả 2 strategies đều output khi có kết quả
- Check Redis có tin nhắn không bằng Redis Connection Test
- Verify end words có match không (cho Immediate strategy)

### ❌ Tin nhắn không gom được

- Verify cùng Key được sử dụng
- Check Wait Time có phù hợp không
- Ensure Redis connection stable

## 📝 API Reference

### Input Parameters

| Parameter      | Type   | Required | Description                                                     |
| -------------- | ------ | -------- | --------------------------------------------------------------- |
| key            | string | ✅       | Key để gom tin nhắn                                             |
| messageContent | string | ✅       | Nội dung tin nhắn                                               |
| waitTime       | number | ✅       | Thời gian chờ (giây)                                            |
| strategy       | string | ✅       | Chiến lược xử lý                                                |
| endWords       | string | ❌       | Từ kết thúc ngăn cách bởi dấu phẩy (chỉ cho Immediate strategy) |

### Output (khi status = 'messages_aggregated')

```javascript
{
  "status": "messages_aggregated",
  "key": "user123",
  "aggregatedMessage": "Xin chào bạn!",
  "messageCount": 3,
  "originalMessages": [
    {"content": "Xin", "timestamp": 1234567890},
    {"content": "chào", "timestamp": 1234567893},
    {"content": "bạn!", "timestamp": 1234567896}
  ],
  "trigger": "smart_timeout",
  "aggregatedAt": "2024-01-01T10:00:11.000Z"
}
```

## 🛡️ Security & Performance

- ✅ **TTL automatic**: Tin nhắn tự động expire
- ✅ **Lock mechanism**: Tránh race conditions
- ✅ **Connection pooling**: Efficient Redis usage
- ✅ **Error handling**: Comprehensive error messages

## 🤝 Support

- 📖 **Documentation**: [GitHub Wiki](https://github.com/nhh0718/n8n-nodes-gom-tin/wiki)
- 🐛 **Issues**: [GitHub Issues](https://github.com/nhh0718/n8n-nodes-gom-tin/issues)
- 💬 **Community**: [n8n Community](https://community.n8n.io)

## 📄 License

MIT © Hoang Thanh Nga

---

**⭐ Nếu package này hữu ích, đừng quên star trên GitHub!**
