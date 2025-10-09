![Banner image](http://lisvn.net/qr.jpg)
# n8n-nodes-zola-fake
Node dành riêng cho n8n này được thiết kế hoạt động hoàn toàn bên trong instance n8n của bạn. Không cần sử dụng API của bên thứ ba hay phụ thuộc ngoại vi nào — chỉ có sự tự động hóa quy trình thuần túy, đảm bảo dữ liệu của bạn luôn được giữ riêng tư và an toàn.

Node này mô phỏng trình duyệt để tương tác trực tiếp với Zalo Web, cho phép tự động hóa liền mạch ngay trong n8n. Đây là dự án mã nguồn mở, mở rộng cơ hội cho cộng đồng cùng đóng góp ý kiến và phát triển thêm các tính năng mới, nhằm xây dựng hệ thống tự động hóa Zalo tiên tiến, hiệu quả và an toàn hơn.

**Cập nhật mới nhất:**
- Đã mở rộng node ZaloUser với nhiều chức năng mới từ Zalo SDK như quản lý avatar, cài đặt người dùng, quản lý cuộc trò chuyện (ghim, ẩn, tắt thông báo), và nhiều tính năng khác
- Cải thiện cấu trúc và tổ chức các chức năng giữa các node để dễ sử dụng hơn
- Thêm các node tiện ích như ZaloGetSecretKey và ZaloDecrypt để hỗ trợ việc giải mã dữ liệu từ Zalo API

## Buy me a coffee
Nếu **node** này giúp bạn tiết kiệm thời gian hoặc giải quyết được vấn đề khó nhằn, hãy cân nhắc ủng hộ tôi một ☕ (Buy me a coffee) hoặc đơn giản là nhấn **★ Star** cho dự án.  
Sự động viên nhỏ ấy sẽ tiếp thêm năng lượng để mình tiếp tục duy trì, cập nhật và phát triển thêm nhiều tính năng hữu ích hơn nữa.  
Cám ơn bạn rất nhiều! 💛


## Tác giả
- Lấy nguồn từ Dương Đình Trung - ChickenAI Team
- Trần Hoàng Thông phát triển và sửa lỗi!

## Hướng dẫn cài đặt node này:

**Community Nodes (Khuyến nghị)**

Đối với người dùng n8n v0.187+, bạn có thể cài đặt node này trực tiếp từ bảng Community Nodes trong trình soạn thảo n8n.

1.  Mở trình soạn thảo n8n của bạn.
2.  Vào Settings > Community Nodes.
3.  Tìm kiếm "n8n-nodes-zola-fake".
4.  Nhấp vào Install.
5.  Tải lại trình soạn thảo.

**Cài đặt thủ công**

Bạn cũng có thể cài đặt node này theo cách thủ công:

```
cd YOUR_N8N_INSTALLATION_DIRECTORY
npm install n8n-nodes-zola-fake
```

## Available Nodes

### 1. Zalo Login By QR
- **Description**: Node cho phép đăng nhập vào Zalo thông qua mã QR.

### 2. Zalo Group
- **Description**: Node quản lý các hoạt động nhóm và bình chọn (poll).
- **Operations**:
  - **Quản lý nhóm cơ bản**:
    - `createGroup`: Tạo nhóm mới
    - `getGroupInfo`: Lấy thông tin nhóm
    - `getAllGroups`: Lấy tất cả nhóm
    - `changeGroupName`: Đổi tên nhóm
    - `changeGroupAvatar`: Đổi avatar nhóm
    - `leaveGroup`: Rời khỏi nhóm
  
  - **Quản lý thành viên**:
    - `getGroupMembers`: Lấy danh sách thành viên
    - `addUserToGroup`: Thêm thành viên
    - `removeUserFromGroup`: Xóa thành viên
    - `addGroupDeputy`: Thêm phó nhóm
    - `removeGroupDeputy`: Xóa phó nhóm
    - `getGroupDeputies`: Lấy danh sách phó nhóm
    - `inviteToGroup`: Mời người dùng vào nhóm
  
  - **Cài đặt nhóm**:
    - `updateGroupSetting`: Cập nhật cài đặt nhóm
    - `getAutoDeleteChat`: Lấy cài đặt tự động xóa tin nhắn
    - `updateAutoDeleteChat`: Cập nhật cài đặt tự động xóa
  
  - **Bình chọn và nhắc nhở**:
    - `createPoll`: Tạo bình chọn mới trong nhóm
    - `getPoll`: Lấy thông tin chi tiết của bình chọn
    - `lockPoll`: Khóa bình chọn
    - `createReminder`: Tạo nhắc nhở trong nhóm
    - `getReminder`: Lấy thông tin nhắc nhở

### 3. Zalo User
- **Description**: Node quản lý người dùng, bạn bè, cài đặt và tương tác.
- **Operations**:
  - **Quản lý bạn bè**:
    - `acceptFriendRequest`: Chấp nhận lời mời kết bạn
    - `sendFriendRequest`: Gửi lời mời kết bạn
    - `undoFriendRequest`: Hủy lời mời kết bạn đã gửi
    - `getReceivedFriendRequests`: Lấy danh sách lời mời kết bạn nhận được
    - `getSentFriendRequest`: Lấy danh sách lời mời kết bạn đã gửi
    - `getAllFriends`: Lấy danh sách bạn bè
    - `changeAliasName`: Đổi tên gợi nhớ của bạn bè
    - `blockUser`: Chặn người dùng
    - `unblockUser`: Bỏ chặn người dùng
    - `blockViewFeed`: Chặn/bỏ chặn xem bài viết
  
  - **Quản lý avatar**:
    - `changeAccountAvatar`: Thay đổi avatar từ URL
    - `getAvatarList`: Lấy danh sách avatar đã sử dụng
    - `deleteAvatar`: Xóa avatar
    - `reuseAvatar`: Sử dụng lại avatar cũ
  
  - **Quản lý cài đặt người dùng**:
    - `updateSettings`: Cập nhật các cài đặt người dùng
    - `updateProfile`: Cập nhật thông tin cá nhân
    - `updateLang`: Thay đổi ngôn ngữ
    - `changeAccountSetting`: Thay đổi cài đặt tài khoản
    - `fetchAccountInfo`: Lấy thông tin tài khoản hiện tại
  
  - **Quản lý cuộc trò chuyện**:
    - `setMute`: Tắt thông báo cho cuộc trò chuyện
    - `getMute`: Lấy danh sách cuộc trò chuyện đã tắt thông báo
    - `setPinnedConversations`: Ghim/bỏ ghim cuộc trò chuyện
    - `getPinConversations`: Lấy danh sách cuộc trò chuyện đã ghim
    - `setHiddenConversations`: Ẩn/hiện cuộc trò chuyện
    - `getHiddenConversations`: Lấy danh sách cuộc trò chuyện đã ẩn
    - `updateHiddenConversPin`: Cập nhật mã PIN cho cuộc trò chuyện ẩn
    - `resetHiddenConversPin`: Đặt lại mã PIN cho cuộc trò chuyện ẩn
  
  - **Quản lý tin nhắn**:
    - `undoMessage`: Thu hồi tin nhắn đã gửi
    - `deleteMessage`: Xóa tin nhắn
  
  - **Quản lý nhãn**:
    - `getLabels`: Lấy danh sách nhãn
    - `updateLabels`: Cập nhật nhãn
  
  - **Thông tin và báo cáo**:
    - `getUserInfo`: Lấy thông tin người dùng
    - `findUser`: Tìm kiếm người dùng qua số điện thoại
    - `lastOnline`: Kiểm tra thời gian trực tuyến cuối cùng
    - `sendReport`: Gửi báo cáo vi phạm

### 4. Zalo Send Message
- **Description**: Node đa chức năng để tương tác với các cuộc trò chuyện.
- **Operations**:
  - **Gửi tin nhắn**:
    - `sendMessage`: Gửi tin nhắn văn bản với các tùy chọn nâng cao (đính kèm ảnh, trích dẫn, đề cập người dùng)
    - `sendSticker`: Gửi sticker vào cuộc trò chuyện
    - `sendVoice`: Gửi tin nhắn thoại từ file âm thanh (.m4a)
    - `sendCard`: Gửi danh thiếp (contact card) của người dùng
    - `sendVideo`: Gửi video vào cuộc trò chuyện
    - `sendLink`: Gửi link với xem trước
    - `forwardMessage`: Chuyển tiếp tin nhắn
  
  - **Quản lý tin nhắn**:
    - `sendMessageStatus`: Gửi trạng thái "đang nhập..."
    - `addReaction`: Thả biểu cảm (reaction) vào tin nhắn
    - `sendDeliveredEvent`: Gửi sự kiện đã nhận tin nhắn
    - `addUnreadMark`: Đánh dấu chưa đọc
    - `removeUnreadMark`: Bỏ đánh dấu chưa đọc
  
  - **Sticker và tiện ích**:
    - `getStickers`: Lấy danh sách các bộ sticker
    - `getStickersDetail`: Lấy thông tin chi tiết của bộ sticker
    - `addQuickMessage`: Thêm tin nhắn nhanh
    - `getQuickMessage`: Lấy danh sách tin nhắn nhanh
    - `updateQuickMessage`: Cập nhật tin nhắn nhanh
    - `removeQuickMessage`: Xóa tin nhắn nhanh

### 5. Zalo TTS (Text-to-Speech)
- **Description**: Node chuyển đổi văn bản thành giọng nói và gửi dưới dạng tin nhắn thoại.
- **Operations**:
  - `convertTTS`: Chuyển đổi văn bản thành giọng nói và trả về URL của file âm thanh.
  - `sendTTSMessage`: Chuyển đổi văn bản thành giọng nói và gửi trực tiếp vào cuộc trò chuyện.

### 6. Zalo Message Trigger
- **Description**: Node lắng nghe và xử lý các sự kiện tin nhắn.
- **Events**:
  - Tin nhắn mới
  - Tin nhắn nhóm
  - Thay đổi trạng thái tin nhắn

### 7. Zalo Decrypt
- **Description**: Node giải mã các chuỗi được mã hóa bằng AES trong Zalo API.
- **Operations**:
  - `decryptAES`: Giải mã chuỗi đã mã hóa bằng khóa bí mật (secretKey).

### 8. Zalo Get Secret Key
- **Description**: Node trích xuất secretKey (zpw_enk) từ phiên đăng nhập Zalo hiện tại.
- **Operations**:
  - `getSecretKey`: Lấy secretKey và uid từ phiên đăng nhập Zalo, có thể sử dụng trực tiếp với node ZaloDecrypt.

## Warning and Thanks

**Please read this carefully before using the Zalo nodes:**

Lưu ý: việc sử dụng thư viện này đồng nghĩa với việc bạn đang làm trái với chính sách của Zalo và nó có thể khiến cho tài khoản của bạn bị vô hiệu hóa. Chúng tôi sẽ không chịu trách nhiệm nếu điều đó xảy ra, vậy nên hãy cân nhắc trước khi sử dụng.

We would like to thank ZCA-JS for their work on this library.


## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
