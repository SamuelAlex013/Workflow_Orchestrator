# n8n-nodes-zalo-oa-integration

Bộ node tích hợp Zalo Official Account (OA) vào n8n, cho phép tự động hóa tương tác với người dùng Zalo thông qua Zalo OA API v3.0.

[n8n](https://n8n.io/) là nền tảng tự động hóa quy trình làm việc được cấp phép [fair-code](https://docs.n8n.io/reference/license/).

## Tính năng

Bộ node này bao gồm:

### 1. Node Zalo OA

Node chính để tương tác với Zalo OA API, hỗ trợ các chức năng:

- **Gửi tin nhắn**: văn bản, hình ảnh, file, danh sách
- **Quản lý media**: upload hình ảnh, file
- **Quản lý người theo dõi**: lấy thông tin, gán tag
- **Quản lý tag**: lấy danh sách tag

### 2. Node Zalo OA Webhook

Node webhook để nhận và xử lý các sự kiện từ Zalo OA:

- **Người dùng follow/unfollow OA**
- **Người dùng gửi tin nhắn**: văn bản, hình ảnh, file, vị trí, sticker, GIF
- **Người dùng tương tác**: nhấp vào nút, liên kết
- **Xác thực MAC**: đảm bảo an toàn cho webhook

## Mua cho tôi 1 ly cafe

Nếu bạn thấy dự án này hữu ích và muốn hỗ trợ phát triển, bạn có thể mua cho tôi một ly cafe:
![Phạm Sỹ Cang](image.png)

- Momo: 0973781781
- Zalo: 0973781781

Mỗi đóng góp đều rất có ý nghĩa và giúp duy trì dự án này!

## Tác giả
- Phạm Sỹ Cang - ChickenAI Team

## Cài đặt

### Cài đặt n8n Community Node

Có nhiều cách để cài đặt n8n community node, tùy thuộc vào cách bạn đã cài đặt n8n:

#### 1. Cài đặt trong n8n website

Các bước cài đặt:

- Mở n8n website
- Vào **Settings** > **Community Nodes**
- Nhấp vào **Install** và nhập tên package: `n8n-nodes-zalo-oa-integration`
- Nhấp vào **Install** và khởi động lại n8n khi được nhắc

#### 2. Cài đặt trong n8n Docker

Các bước cài đặt:

- Tạo thư mục custom cho n8n:

```bash
mkdir -p /path-to-n8n-data/custom
```

- Thêm volume vào docker-compose.yml:

```yaml
volumes:
  - /path-to-n8n-data/custom:/home/node/.n8n/custom
```

- Cài đặt node trong container:

```bash
docker-compose exec n8n npm install n8n-nodes-zalo-oa-integration
```

- Khởi động lại container:

```bash
docker-compose restart n8n
```

#### 3. Cài đặt từ npm (cài đặt toàn cục)

```bash
npm install -g n8n-nodes-zalo-oa-integration
```

#### 4. Cài đặt từ npm (cài đặt cục bộ)

```bash
npm install n8n-nodes-zalo-oa-integration
```

#### 5. Cài đặt thủ công

Các bước cài đặt thủ công:

- Clone repository:

```bash
git clone https://github.com/ChickenAI/zalo-node-oa.git
```

- Build node:

```bash
cd zalo-node-oa
npm install
npm run build
```

- Copy thư mục `dist` vào thư mục custom của n8n:

```bash
# Linux/macOS
cp -r dist/* ~/.n8n/custom/

# Windows
xcopy /E dist\* %APPDATA%\n8n\custom\
```

4. Kiểm tra cấu trúc thư mục của node:

```
/path-to-n8n/custom/
├── credentials/
│   └── ZaloOAApi.credentials.js
├── nodes/
│   ├── ZaloOA/
│   │   └── ZaloOA.node.js
│   └── ZaloOAWebhook/
│       └── ZaloOAWebhook.node.js
```

5. Khởi động lại n8n với cờ chế debug:

```bash
DEBUG=* n8n start
```

## Hướng dẫn sử dụng

### Thiết lập xác thực

Các bước thiết lập:

- Tạo Zalo OA tại [Zalo Business](https://business.zalo.me/)
- Đăng ký ứng dụng tại [Zalo Developers](https://developers.zalo.me/)
- Lấy App ID, Secret Key, Access Token và OA ID
- Trong n8n, tạo credential mới cho Zalo OA API

### Sử dụng Node Zalo OA

#### Gửi tin nhắn văn bản

Các bước thực hiện:

- Thêm node Zalo OA vào workflow
- Chọn operation "Gửi Tin Nhắn Văn Bản"
- Nhập User ID và nội dung tin nhắn
- Chạy workflow

#### Upload hình ảnh

Các bước thực hiện:

- Thêm node Zalo OA vào workflow
- Chọn operation "Upload Hình Ảnh"
- Chọn nguồn hình ảnh (URL hoặc Binary Data)
- Chạy workflow để lấy ID hình ảnh

### Sử dụng Node Zalo OA Webhook

Các bước thiết lập webhook:

- Thêm node Zalo OA Webhook vào workflow
- Nhập OA Secret Key
- Chọn các loại sự kiện muốn nhận
- Kích hoạt workflow để lấy URL webhook
- Cấu hình URL webhook trong trang quản lý Zalo OA

## Ví dụ workflow

### Gửi tin nhắn chào mừng khi có người theo dõi mới

Các bước thực hiện:

- Thêm node Zalo OA Webhook (lọc sự kiện "follow")
- Thêm node Zalo OA để gửi tin nhắn chào mừng
- Kết nối các node và kích hoạt workflow

### Trả lời tự động tin nhắn của người dùng

Các bước thực hiện:

- Thêm node Zalo OA Webhook (lọc sự kiện "user_send_text")
- Thêm node Function để xử lý nội dung tin nhắn
- Thêm node Zalo OA để gửi tin nhắn trả lời
- Kết nối các node và kích hoạt workflow

## Lưu ý quan trọng

Một số lưu ý khi sử dụng Zalo OA API:

- **API v3.0 với MessageV3**: Bộ node này sử dụng Zalo OA API v3.0 với MessageV3 API, hỗ trợ các loại tin nhắn khác nhau (Tư vấn, Giao dịch, Truyền thông cá nhân)
- **Rate Limit**: Zalo OA API có giới hạn số lượng request, thường là 10 requests/giây
- **Access Token**: Access Token có thời hạn sử dụng, cần cập nhật khi hết hạn
- **HTTPS**: Zalo OA yêu cầu webhook phải sử dụng HTTPS
- **Xác thực MAC**: Nên bật tính năng này để đảm bảo an toàn cho webhook

## Danh sách API và tham số

Dưới đây là danh sách các API được sử dụng trong node Zalo OA:

### Tham số xác thực và cấu hình

#### Tham số xác thực

- **App ID**: ID ứng dụng Zalo OA
- **Secret Key**: Khóa bí mật của ứng dụng
- **Access Token**: Token truy cập Zalo OA API
- **Refresh Token**: Token làm mới Access Token khi hết hạn

#### Header chung cho các API

- `access_token`: Token truy cập Zalo OA API
- `Content-Type`: application/json hoặc multipart/form-data (tùy API)

### 1. API Gửi tin nhắn

#### Gửi tin nhắn văn bản

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/message/{messageType}`
- **Method**: POST
- **Tham số**:
  - `messageType`: Loại tin nhắn (cs, transaction, promotion)
  - `recipient.user_id`: ID người nhận
  - `message.text`: Nội dung tin nhắn

#### Gửi tin nhắn hình ảnh

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/message/{messageType}`
- **Method**: POST
- **Tham số**:
  - `messageType`: Loại tin nhắn (cs, transaction, promotion)
  - `recipient.user_id`: ID người nhận
  - `message.attachment.type`: Loại đính kèm (image)
  - `message.attachment.payload.token`: Token hình ảnh đã upload
  - `message.attachment.payload.url`: URL hình ảnh (tùy chọn thay cho token)

#### Gửi tin nhắn file

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/message/{messageType}`
- **Method**: POST
- **Tham số**:
  - `messageType`: Loại tin nhắn (cs, transaction, promotion)
  - `recipient.user_id`: ID người nhận
  - `message.attachment.type`: Loại đính kèm (file)
  - `message.attachment.payload.token`: Token file đã upload

#### Gửi tin nhắn danh sách

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/message/{messageType}`
- **Method**: POST
- **Tham số**:
  - `messageType`: Loại tin nhắn (cs, transaction, promotion)
  - `recipient.user_id`: ID người nhận
  - `message.attachment.type`: Loại đính kèm (template)
  - `message.attachment.payload.template_type`: Loại template (list)
  - `message.attachment.payload.elements`: Mảng các phần tử danh sách
    - `title`: Tiêu đề mục
    - `subtitle`: Mô tả mục
    - `image_url`: URL hình ảnh mục
    - `default_action.url`: URL khi nhấp vào mục
  - `message.attachment.payload.buttons`: Mảng các nút tương tác
    - `title`: Tiêu đề nút
    - `type`: Loại nút (oa.open.url)
    - `payload.url`: URL khi nhấp vào nút

### 2. API Quản lý người dùng

#### Lấy thông tin Official Account

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/getoa`
- **Method**: GET
- **Tham số**: Không có

#### Lấy thông tin người theo dõi

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/getprofile`
- **Method**: GET
- **Tham số**:
  - `user_id`: ID người dùng

#### Lấy danh sách người theo dõi

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/getfollowers`
- **Method**: GET
- **Tham số**:
  - `offset`: Vị trí bắt đầu
  - `count`: Số lượng người dùng cần lấy

#### Cập nhật thông tin người theo dõi

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/updatefollowerinfo`
- **Method**: POST
- **Tham số**:
  - `user_id`: ID người dùng
  - `info_type`: Loại thông tin (name, phone, email, address, city, birthday)
  - `info_value`: Giá trị thông tin

### 3. API Quản lý hội thoại

#### Lấy danh sách cuộc trò chuyện gần đây

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/listrecentchat`
- **Method**: GET
- **Tham số**:
  - `offset`: Vị trí bắt đầu
  - `count`: Số lượng cuộc trò chuyện cần lấy

#### Lấy lịch sử hội thoại

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/conversation`
- **Method**: GET
- **Tham số**:
  - `user_id`: ID người dùng
  - `offset`: Vị trí bắt đầu
  - `count`: Số lượng tin nhắn cần lấy

### 4. API Quản lý media

#### Upload hình ảnh

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/upload/image`
- **Method**: POST
- **Tham số**:
  - `file`: File hình ảnh (multipart/form-data)
  - `image_url`: URL hình ảnh (thay thế cho file)

#### Upload file

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/upload/file`
- **Method**: POST
- **Tham số**:
  - `file`: File cần upload (multipart/form-data)
  - `file_url`: URL file (thay thế cho file)

#### Upload hình ảnh GIF

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/upload/gif`
- **Method**: POST
- **Tham số**:
  - `file`: File GIF (multipart/form-data)
  - `gif_url`: URL hình ảnh GIF (thay thế cho file)

### 5. API Quản lý tag

#### Lấy danh sách tag

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/tag/gettagsofoa`
- **Method**: GET
- **Tham số**:
  - `offset`: Vị trí bắt đầu
  - `count`: Số lượng tag cần lấy

#### Gán tag cho người dùng

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/tag/tagfollower`
- **Method**: POST
- **Tham số**:
  - `user_id`: ID người dùng
  - `tag_id`: ID tag

#### Xóa tag của người dùng

- **Endpoint**: `https://openapi.zalo.me/v3.0/oa/tag/rmfollowerfromtag`
- **Method**: POST
- **Tham số**:
  - `user_id`: ID người dùng
  - `tag_id`: ID tag

### 6. API Quản lý bài viết

#### Tạo bài viết

- **Endpoint**: `https://openapi.zalo.me/v3.0/article/create`
- **Method**: POST
- **Tham số**:
  - `title`: Tiêu đề bài viết
  - `description`: Mô tả bài viết
  - `author`: Tác giả bài viết
  - `cover.photo_url`: URL ảnh bìa
  - `cover.status`: Trạng thái ảnh bìa (show/hide)
  - `body`: Nội dung bài viết
  - `status`: Trạng thái bài viết (show/hide)
  - `comment`: Cho phép bình luận (show/hide)

#### Chuẩn bị upload video

- **Endpoint**: `https://openapi.zalo.me/v3.0/article/upload_video/preparevideo`
- **Method**: POST
- **Tham số**:
  - `video_name`: Tên video
  - `video_size`: Kích thước video (byte)

#### Xác thực video

- **Endpoint**: `https://openapi.zalo.me/v3.0/article/upload_video/verify`
- **Method**: POST
- **Tham số**:
  - `upload_id`: ID upload

#### Lấy chi tiết bài viết

- **Endpoint**: `https://openapi.zalo.me/v3.0/article/verify`
- **Method**: GET
- **Tham số**:
  - `token`: Token bài viết

### 7. API Quản lý cửa hàng

#### Tạo sản phẩm

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/product/create`
- **Method**: POST
- **Tham số**:
  - `name`: Tên sản phẩm
  - `price`: Giá sản phẩm
  - `description`: Mô tả sản phẩm
  - `code`: Mã sản phẩm
  - `photos`: Mảng URL hình ảnh sản phẩm
  - `status`: Trạng thái sản phẩm (show/hide)

#### Cập nhật sản phẩm

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/product/update`
- **Method**: POST
- **Tham số**:
  - `id`: ID sản phẩm
  - `name`: Tên sản phẩm
  - `price`: Giá sản phẩm
  - `description`: Mô tả sản phẩm
  - `code`: Mã sản phẩm
  - `photos`: Mảng URL hình ảnh sản phẩm
  - `status`: Trạng thái sản phẩm (show/hide)

#### Tạo đơn hàng

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/order/create`
- **Method**: POST
- **Tham số**:
  - `user_id`: ID người dùng
  - `shipping.name`: Tên người nhận
  - `shipping.phone`: Số điện thoại người nhận
  - `shipping.address`: Địa chỉ giao hàng
  - `shipping.city`: Thành phố
  - `items`: Mảng sản phẩm trong đơn hàng
  - `shipping_fee`: Phí vận chuyển
  - `discount`: Giảm giá
  - `total`: Tổng tiền

#### Cập nhật đơn hàng

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/order/update`
- **Method**: POST
- **Tham số**:
  - `id`: ID đơn hàng
  - `status`: Trạng thái đơn hàng
  - `reason`: Lý do cập nhật

#### Lấy thông tin đơn hàng

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/order/getorder`
- **Method**: GET
- **Tham số**:
  - `id`: ID đơn hàng

#### Lấy danh sách đơn hàng

- **Endpoint**: `https://openapi.zalo.me/v3.0/store/order/getorderofoa`
- **Method**: GET
- **Tham số**:
  - `offset`: Vị trí bắt đầu
  - `count`: Số lượng đơn hàng cần lấy
  - `status`: Trạng thái đơn hàng

### 8. API Webhook

#### Webhook nhận sự kiện

- **Endpoint**: URL webhook của bạn
- **Method**: POST
- **Tham số nhận được**:
  - `app_id`: ID ứng dụng
  - `sender.id`: ID người gửi
  - `recipient.id`: ID người nhận (OA ID)
  - `event_name`: Tên sự kiện
  - `timestamp`: Thời gian sự kiện
  - `message`: Thông tin tin nhắn (nếu có)
  - `mac`: Mã xác thực MAC

#### Các loại sự kiện webhook

- **Sự kiện người dùng**:
  - `follow`: Người dùng theo dõi OA
  - `unfollow`: Người dùng hủy theo dõi OA

- **Sự kiện tin nhắn**:
  - `user_send_text`: Người dùng gửi tin nhắn văn bản
  - `user_send_image`: Người dùng gửi hình ảnh
  - `user_send_file`: Người dùng gửi file
  - `user_send_sticker`: Người dùng gửi sticker
  - `user_send_gif`: Người dùng gửi GIF
  - `user_send_location`: Người dùng gửi vị trí

- **Sự kiện tương tác**:
  - `user_click_link`: Người dùng nhấp vào liên kết
  - `user_click_button`: Người dùng nhấp vào nút
  - `user_received_message`: Người dùng đã nhận tin nhắn
  - `user_seen_message`: Người dùng đã xem tin nhắn

## Mã lỗi phổ biến

Dưới đây là một số mã lỗi phổ biến khi sử dụng Zalo OA API:

- **-201**: Thiếu tham số bắt buộc
- **-202**: Tham số không hợp lệ
- **-204**: Access Token không hợp lệ hoặc đã hết hạn
- **-205**: Không có quyền truy cập API
- **-210**: Rate limit vượt quá giới hạn
- **-211**: OA chưa được xác thực
- **-213**: Người dùng không theo dõi OA
- **-214**: OA đã gửi tin nhắn cho người dùng trong 24h gần đây
- **-215**: Nội dung tin nhắn vi phạm chính sách
- **-216**: Tin nhắn đã được gửi trước đó
- **-240**: API v2.0 đã bị tắt, cần sử dụng API v3.0

## Tài liệu tham khảo

- [Tài liệu Zalo OA API](https://developers.zalo.me/docs/api/official-account-api-230)
- [Tài liệu n8n Community Nodes](https://docs.n8n.io/integrations/creating-nodes/)
- [Zalo OA API Changelog](https://developers.zalo.me/changelog)

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request trên GitHub.

## Giấy phép

[MIT](LICENSE.md)
