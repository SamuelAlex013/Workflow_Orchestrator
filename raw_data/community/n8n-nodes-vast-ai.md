# n8n Vast.ai Custom Node

Đây là một custom node cho n8n, cho phép bạn tương tác với API của Vast.ai để quản lý các phiên bản máy ảo (instances), tìm kiếm ưu đãi (offers), và truy vấn thông tin tài khoản.

## Tính năng

Node này hỗ trợ các tài nguyên và hoạt động sau:

### Instances (Phiên bản máy ảo)

- **Create Instance**: Tạo một phiên bản máy ảo mới dựa trên các thông số được cung cấp.
- **Destroy Instance**: Hủy bỏ một phiên bản máy ảo hiện có.
- **Show Instance**: Hiển thị thông tin chi tiết của một phiên bản máy ảo cụ thể.
- **Show Instances**: Hiển thị danh sách tất cả các phiên bản máy ảo của bạn.

### Search (Tìm kiếm)

- **Search Offers**: Tìm kiếm các ưu đãi máy ảo có sẵn trên Vast.ai dựa trên các tiêu chí lọc khác nhau.

### Accounts (Tài khoản)

- **Show API Keys**: Hiển thị danh sách các khóa API của tài khoản.
- **Show Connections**: Hiển thị thông tin kết nối đám mây của tài khoản.
- **Show Env Vars**: Hiển thị các biến môi trường đã lưu.
- **Show Subaccounts**: Hiển thị danh sách các tài khoản phụ.
- **Show User**: Hiển thị thông tin chi tiết về người dùng hiện tại.

### Serverless

- **Show Autogroup**: Hiển thị thông tin về một autogroup.
- **Show Endpoints**: Hiển thị danh sách các endpoint serverless.

### Volumes

- **List Volumes**: Liệt kê tất cả các volume lưu trữ.

## Cài đặt

Để cài đặt custom node này trong n8n, bạn cần làm theo các bước sau:

1.  **Sao chép thư mục node**: Sao chép toàn bộ thư mục `n8n-nodes-vast.ai-main` vào thư mục `.n8n/custom` trong thư mục người dùng của bạn (ví dụ: `~/.n8n/custom/n8n-nodes-vast.ai-main`). Nếu thư mục `custom` không tồn tại, hãy tạo nó.

2.  **Cài đặt dependencies**: Mở terminal trong thư mục `n8n-nodes-vast.ai-main` và chạy lệnh sau để cài đặt các dependencies:

    ```bash
    npm install
    # hoặc
    yarn install
    # hoặc
    pnpm install
    ```

3.  **Khởi động lại n8n**: Sau khi cài đặt xong, khởi động lại n8n để node mới được tải.

## Cấu hình Vast.ai Credentials

Để sử dụng node Vast.ai, bạn cần cấu hình Vast.ai API Key của mình trong n8n. Thực hiện theo các bước sau:

1.  Trong n8n, nhấp vào **Credentials** ở thanh điều hướng bên trái.
2.  Nhấp vào **New Credential**.
3.  Tìm kiếm và chọn **Vast.ai API**.
4.  Nhập **API Key** của bạn vào trường tương ứng. Bạn có thể tìm thấy API Key của mình trên trang Vast.ai console.
5.  Lưu thông tin xác thực.

## Cách sử dụng

Node Vast.ai cho phép bạn chọn một tài nguyên (Resource) và một hoạt động (API Group Name or ID) để thực hiện các tác vụ khác nhau. Dưới đây là hướng dẫn chi tiết cho từng tài nguyên và hoạt động được hỗ trợ.

### 1. Resource: Instances

Khi bạn chọn `Instances` làm tài nguyên, bạn có thể thực hiện các hoạt động sau:

#### 1.1. Create Instance

Hoạt động này cho phép bạn tạo một phiên bản máy ảo mới. Các tham số cần thiết bao gồm:

#### 1.2. Destroy Instance

Hoạt động này dùng để hủy bỏ một phiên bản máy ảo. Tham số cần thiết:

#### 1.3. Show Instance

Hoạt động này hiển thị thông tin chi tiết của một phiên bản máy ảo cụ thể. Tham số cần thiết:

#### 1.4. Show Instances

Hoạt động này hiển thị danh sách tất cả các phiên bản máy ảo của bạn. Không yêu cầu tham số.

### 2. Resource: Search

Khi bạn chọn `Search` làm tài nguyên, bạn có thể thực hiện hoạt động sau:

#### 2.1. Search Offers

Hoạt động này cho phép bạn tìm kiếm các ưu đãi máy ảo có sẵn trên Vast.ai. Các tham số có thể được sử dụng để lọc kết quả tìm kiếm bao gồm:

### 3. Resource: Accounts

Khi bạn chọn `Accounts` làm tài nguyên, bạn có thể thực hiện các hoạt động sau:

#### 3.1. Show API Keys

Hoạt động này hiển thị danh sách các khóa API liên quan đến tài khoản của bạn. Không yêu cầu tham số.

#### 3.2. Show Connections

Hoạt động này hiển thị thông tin về các kết nối đám mây của tài khoản. Không yêu cầu tham số.

#### 3.3. Show Env Vars

Hoạt động này hiển thị các biến môi trường đã được lưu trữ cho tài khoản của bạn. Không yêu cầu tham số.

#### 3.4. Show Subaccounts

Hoạt động này hiển thị danh sách các tài khoản phụ được liên kết với tài khoản chính của bạn. Không yêu cầu tham số.

#### 3.5. Show User

Hoạt động này hiển thị thông tin chi tiết về người dùng hiện tại. Không yêu cầu tham số.

### 4. Resource: Serverless

Khi bạn chọn `Serverless` làm tài nguyên, bạn có thể thực hiện các hoạt động sau:

#### 4.1. Show Autogroup

Hoạt động này hiển thị thông tin về một autogroup. Không yêu cầu tham số.

#### 4.2. Show Endpoints

Hoạt động này hiển thị danh sách các endpoint serverless. Không yêu cầu tham số.

### 5. Resource: Volumes

Khi bạn chọn `Volumes` làm tài nguyên, bạn có thể thực hiện hoạt động sau:

#### 5.1. List Volumes

Hoạt động này liệt kê tất cả các volume lưu trữ của bạn. Không yêu cầu tham số.

## Đóng góp

Nếu bạn muốn đóng góp vào custom node này, vui lòng làm theo các bước sau:

1.  Fork repository.
2.  Tạo một nhánh mới (`git checkout -b feature/your-feature-name`).
3.  Thực hiện các thay đổi của bạn.
4.  Cam kết các thay đổi của bạn (`git commit -m 'Add some feature'`).
5.  Push lên nhánh (`git push origin feature/your-feature-name`).
6.  Mở một Pull Request.

## Giấy phép

Node này được phát hành dưới Giấy phép MIT. Xem file `LICENSE.md` để biết thêm chi tiết.

---

**Tác giả:** TRƯƠNG HẢI ĐĂNG

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [MyService API documentation](https://docs.myservice.com/api)

## License

[MIT](https://github.com/yourusername/n8n-nodes-myservice/blob/master/LICENSE.md)
