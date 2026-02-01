# n8n-nodes-lunar-calendar-vi

🌙 **n8n Community Node** để chuyển đổi giữa âm lịch và dương lịch Việt Nam

[![npm version](https://badge.fury.io/js/n8n-nodes-lunar-calendar-vi.svg)](https://badge.fury.io/js/n8n-nodes-lunar-calendar-vi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Giới thiệu

Đây là một n8n community node để chuyển đổi giữa âm lịch và dương lịch Việt Nam, sử dụng thư viện [@nghiavuive/lunar_date_vi](https://github.com/nacana22/lunar-date) được phát triển bởi cộng đồng Việt Nam.

### ✨ Tính năng chính

- 🔄 **Chuyển đổi Dương lịch sang Âm lịch** - Hỗ trợ ngày hiện tại, ngày cụ thể hoặc từ dữ liệu đầu vào
- 🔄 **Chuyển đổi Âm lịch sang Dương lịch** - Hỗ trợ tháng nhuận và các trường hợp đặc biệt
- 🌟 **Thông tin Can Chi** - Tên năm, tháng, ngày theo can chi (vd: Quý Mão, Giáp Thìn)
- ⏰ **Giờ hoàng đạo** - Danh sách các giờ tốt trong ngày
- 📅 **Tiết khí** - Thông tin 24 tiết khí trong năm
- 🗓️ **Thứ trong tuần** - Tên thứ bằng tiếng Việt
- 🏷️ **Interface tiếng Việt** - Dễ sử dụng cho người Việt

## 🚀 Cài đặt

### Cài đặt trong n8n

1. Vào **Settings** → **Community Nodes**
2. Chọn **Install**
3. Nhập `n8n-nodes-lunar-calendar-vi`
4. Chọn **Install**

### Cài đặt từ npm

```bash
npm install n8n-nodes-lunar-calendar-vi
```

## 🎯 Cách sử dụng

### Ví dụ 1: Chuyển ngày hiện tại sang âm lịch

1. Thêm node **Lunar Calendar VI** vào workflow
2. Chọn **Thao tác**: "Dương lịch sang Âm lịch"
3. Chọn **Nguồn ngày tháng**: "Ngày hiện tại"
4. Trong **Thông tin bổ sung**, chọn các thông tin bạn muốn:
   - ✅ Tên năm Can Chi
   - ✅ Giờ hoàng đạo
   - ✅ Tiết khí
5. Chạy workflow

**Kết quả:**
```json
{
  "solar": {
    "day": 19,
    "month": 6,
    "year": 2023,
    "leap_year": false
  },
  "lunar": {
    "day": 2,
    "month": 5,
    "year": 2023,
    "leap_year": true,
    "leap_month": false,
    "year_name": "Quý Mão",
    "lucky_hours": [
      { "name": "Tý", "time": [23, 1] },
      { "name": "Sửu", "time": [1, 3] }
    ]
  },
  "julian": 2460115,
  "solar_term": "Hạ chí"
}
```

### Ví dụ 2: Chuyển ngày cụ thể sang âm lịch

1. Thêm node **Lunar Calendar VI**
2. Chọn **Thao tác**: "Dương lịch sang Âm lịch"  
3. Chọn **Nguồn ngày tháng**: "Ngày cụ thể"
4. Nhập:
   - **Ngày**: 1
   - **Tháng**: 1
   - **Năm**: 2024
5. Chạy workflow

### Ví dụ 3: Chuyển từ dữ liệu đầu vào

**Dữ liệu đầu vào:**
```json
{
  "birth_date": "1990-05-15",
  "name": "Nguyễn Văn A"
}
```

**Cấu hình node:**
1. **Thao tác**: "Dương lịch sang Âm lịch"
2. **Nguồn ngày tháng**: "Từ dữ liệu đầu vào"
3. **Trường chứa ngày dương lịch**: `birth_date`

### Ví dụ 4: Chuyển âm lịch sang dương lịch

1. Thêm node **Lunar Calendar VI**
2. Chọn **Thao tác**: "Âm lịch sang Dương lịch"
3. Nhập thông tin âm lịch:
   - **Ngày âm lịch**: 15
   - **Tháng âm lịch**: 8
   - **Năm âm lịch**: 2023
   - **Tháng nhuận**: false
4. Chạy workflow

## 📋 Dữ liệu đầu ra

### Cấu trúc dữ liệu trả về

```typescript
{
  // Thông tin dương lịch
  solar: {
    day: number,           // Ngày (1-31)
    month: number,         // Tháng (1-12)
    year: number,          // Năm
    leap_year: boolean,    // Có phải năm nhuận không
    date?: Date           // Date object (chỉ có khi chuyển từ âm lịch)
  },
  
  // Thông tin âm lịch
  lunar: {
    day: number,           // Ngày âm lịch (1-30)
    month: number,         // Tháng âm lịch (1-12)
    year: number,          // Năm âm lịch
    leap_year: boolean,    // Có phải năm nhuận không
    leap_month: boolean,   // Có phải tháng nhuận không
    
    // Thông tin bổ sung (nếu được chọn)
    year_name?: string,    // Tên năm Can Chi (vd: "Quý Mão")
    month_name?: string,   // Tên tháng Can Chi
    day_name?: string,     // Tên ngày Can Chi
    lucky_hours?: Array<{  // Giờ hoàng đạo
      name: string,        // Tên giờ (vd: "Tý", "Sửu")
      time: [number, number] // Khoảng thời gian [bắt đầu, kết thúc]
    }>
  },
  
  // Thông tin chung
  julian: number,          // Số ngày Julian
  day_of_week?: string,    // Thứ trong tuần (vd: "Thứ hai")
  solar_term?: string      // Tiết khí (vd: "Hạ chí", "Đông chí")
}
```

## 🛠️ Phát triển

### Yêu cầu hệ thống

- Node.js 18.x hoặc cao hơn
- npm 8.x hoặc cao hơn
- n8n 0.190.0 hoặc cao hơn

### Cài đặt môi trường phát triển

```bash
# Clone repository
git clone https://github.com/hophamlam/n8n-lunar-calendar-vi.git
cd n8n-lunar-calendar-vi

# Cài đặt dependencies
npm install

# Build project
npm run build

# Kiểm tra linting
npm run lint

# Format code
npm run format
```

### Test local với n8n

```bash
# Build và link package
npm run build
npm link

# Trong thư mục n8n (~/.n8n)
npm link n8n-nodes-lunar-calendar-vi

# Khởi động n8n
n8n start
```

### Cấu trúc project

```
n8n-lunar-calendar-vi/
├── nodes/
│   └── LunarCalendarVi/
│       ├── LunarCalendarVi.node.ts    # Node chính
│       ├── LunarCalendarVi.node.json  # Metadata
│       └── lunarCalendar.svg          # Icon
├── dist/                              # Build output
├── package.json                       # Package config
├── tsconfig.json                      # TypeScript config
├── .eslintrc.js                       # ESLint config
├── gulpfile.js                        # Build scripts
└── README.md                          # Documentation
```

## 🌏 Ngôn ngữ và địa phương hóa

Node này được thiết kế đặc biệt cho thị trường Việt Nam:

- ✅ Interface hoàn toàn bằng tiếng Việt
- ✅ Hỗ trợ lịch âm Việt Nam chính xác
- ✅ Can Chi theo truyền thống Việt Nam
- ✅ Tiết khí theo lịch Việt Nam
- ✅ Giờ hoàng đạo theo phong tục Việt Nam

## 📚 Tài liệu tham khảo

- [Thư viện lunar-date gốc](https://github.com/nacana22/lunar-date)
- [Tài liệu n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [Hướng dẫn tạo n8n nodes](https://docs.n8n.io/integrations/creating-nodes/)

## 🤝 Đóng góp

Chúng tôi chào đón mọi đóng góp từ cộng đồng!

### Cách đóng góp

1. **Fork** repository này
2. Tạo **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** thay đổi (`git commit -m 'Add some amazing feature'`)
4. **Push** lên branch (`git push origin feature/amazing-feature`)
5. Mở **Pull Request**

### Báo lỗi

Nếu bạn phát hiện lỗi, vui lòng tạo issue với thông tin:

- Phiên bản n8n
- Phiên bản node
- Mô tả lỗi chi tiết
- Bước tái hiện lỗi
- Kết quả mong đợi vs thực tế

## 📄 Giấy phép

Dự án này được phát hành dưới giấy phép [MIT License](LICENSE).

## 👥 Tác giả

- **Hoang Pham** - *Initial work* - [@hophamlam](https://github.com/hophamlam)

## 🙏 Cảm ơn

- [nacana22](https://github.com/nacana22) - Tác giả thư viện lunar-date gốc
- [n8n.io](https://n8n.io) - Platform workflow automation tuyệt vời
- Cộng đồng lập trình viên Việt Nam

## 📈 Changelog

### v0.1.0 (2024-01-01)
- ✅ Chức năng chuyển đổi dương lịch sang âm lịch
- ✅ Chức năng chuyển đổi âm lịch sang dương lịch  
- ✅ Hỗ trợ thông tin Can Chi
- ✅ Hỗ trợ giờ hoàng đạo
- ✅ Hỗ trợ tiết khí
- ✅ Interface tiếng Việt

---

**⭐ Nếu project này hữu ích, đừng quên cho chúng tôi một star trên GitHub!** 