# n8n-nodes-sapo

Đây là một node cộng đồng n8n cho Nền tảng Thương mại Điện tử Sapo. Node này cung cấp các tính năng để tương tác với các API của Sapo.

[n8n](https://n8n.io/) là một nền tảng tự động hóa quy trình làm việc được [cấp phép fair-code](https://docs.n8n.io/reference/license/).

[Cài đặt](#installation)  
[Các Thao Tác](#operations)  
[Thông Tin Xác Thực](#credentials)  
[Tài Nguyên](#resources)  
[Lịch Sử Phiên Bản](#version-history)  

## Cài đặt

Làm theo [hướng dẫn cài đặt](https://docs.n8n.io/integrations/community-nodes/installation/) trong tài liệu node cộng đồng n8n.

## Ủng hộ 1 cốc cà phê 
Nếu bạn thấy gói tích hợp này hữu ích, hãy ủng hộ tác giả 1 cốc cà phê nhé!
Cám ơn các bạn đã ủng hộ!
```
BIEN NGO HUY PHONG
TECHCOMBANK
```
<img src="bank.jpg" height="350" />


## Các Thao Tác

Các thao tác sau được hỗ trợ cho mỗi tài nguyên:

### Sản Phẩm
- Tạo sản phẩm
- Lấy chi tiết sản phẩm
- Lấy danh sách sản phẩm
- Cập nhật sản phẩm
- Xóa sản phẩm

### Đơn Hàng
- Tạo đơn hàng
- Lấy chi tiết đơn hàng
- Lấy danh sách đơn hàng
- Cập nhật đơn hàng
- Xóa đơn hàng
- Hủy đơn hàng
- Đánh dấu đã thanh toán
- Đánh dấu đã thực hiện

### Khách Hàng
- Tạo khách hàng
- Lấy chi tiết khách hàng
- Lấy danh sách khách hàng
- Cập nhật khách hàng
- Xóa khách hàng

### Bộ Sưu Tập
- Tạo bộ sưu tập tùy chỉnh
- Tạo bộ sưu tập thông minh
- Lấy chi tiết bộ sưu tập
- Lấy danh sách bộ sưu tập
- Cập nhật bộ sưu tập
- Xóa bộ sưu tập
- Thêm/xóa sản phẩm
- Sắp xếp sản phẩm

### Kho Hàng
- Điều chỉnh số lượng
- Lấy mức tồn kho
- Lấy danh sách tồn kho
- Đặt mức tồn kho
- Chuyển kho
- Lấy/hủy chuyển kho

### Quy Tắc Giá
- Tạo quy tắc giá
- Lấy chi tiết quy tắc giá
- Lấy danh sách quy tắc giá
- Cập nhật quy tắc giá
- Xóa quy tắc giá

### Thực Hiện Đơn Hàng
- Tạo thực hiện đơn hàng
- Lấy chi tiết thực hiện
- Lấy danh sách thực hiện
- Cập nhật tracking
- Hủy thực hiện
- Hoàn tất thực hiện

### Trường Tùy Chỉnh
- Tạo trường tùy chỉnh
- Lấy chi tiết trường tùy chỉnh
- Lấy danh sách trường tùy chỉnh
- Cập nhật trường tùy chỉnh
- Xóa trường tùy chỉnh
- Xóa hàng loạt trường tùy chỉnh
- Xác thực trường tùy chỉnh

### Trang
- Tạo trang
- Lấy chi tiết trang
- Lấy danh sách trang
- Cập nhật trang
- Xóa trang

### Blog & Bài Viết
- Tạo blog/bài viết
- Lấy chi tiết blog/bài viết
- Lấy danh sách blog/bài viết
- Cập nhật blog/bài viết
- Xóa blog/bài viết
- Quản lý bình luận

### Webhook
- Tạo webhook
- Lấy chi tiết webhook
- Lấy danh sách webhook
- Cập nhật webhook
- Xóa webhook

## Thông Tin Xác Thực

Để sử dụng các node này, bạn cần:
1. Tạo một ứng dụng riêng Sapo trong trang quản trị cửa hàng của bạn
2. Lấy API Key, Secret Key và URL cửa hàng
3. Thêm các thông tin xác thực vào phần credentials của n8n

## Tài Nguyên

* [Tài liệu node cộng đồng n8n](https://docs.n8n.io/integrations/community-nodes/)
* [Tài liệu API Sapo](https://developers.sapo.vn/)
