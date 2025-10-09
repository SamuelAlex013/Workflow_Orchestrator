# n8n-nodes-ytube-transcript-wlang

[![npm version](https://badge.fury.io/js/n8n-nodes-ytube-transcript-wlang-v2.svg)](https://www.npmjs.com/package/n8n-nodes-ytube-transcript-wlang-v2)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![n8n](https://img.shields.io/badge/n8n-custom%20node-orange)](https://n8n.io/)
[![Build](https://img.shields.io/badge/status-stable-blue)](https://github.com/minproducer/n8n-nodes-ytube-transcript-wlang-v2)

> 🔧 A powerful n8n custom node to extract and parse YouTube subtitles using `yt-dlp`, with multi-language support and structured JSON output.

---

## 🇻🇳 Mô tả

Node tùy chỉnh cho [n8n](https://n8n.io), giúp **trích xuất phụ đề video YouTube** bằng công cụ `yt-dlp`. Hỗ trợ lựa chọn **ngôn ngữ phụ đề** (ví dụ: `vi`, `en`, `ja`, ...), **xác thực bằng cookie**, và **chuyển phụ đề định dạng `.vtt` sang JSON có cấu trúc**, sẵn sàng để xử lý hoặc lưu trữ.

---

## ✨ Tính năng

- 📼 Nhận cả URL YouTube và video ID
- 🌐 Lựa chọn ngôn ngữ phụ đề (`lang`: vi, en, ja,...)
- 🔐 Hỗ trợ xác thực bằng `cookie` (dạng chuỗi hoặc file `.txt`)
- 📄 Phân tích `.vtt` thành JSON chi tiết (`text`, `start`, `duration`)
- 🧹 Tự động dọn dẹp file tạm sau xử lý

---

## 📦 Cài đặt

### 1. Cài qua npm

```bash
npm install n8n-nodes-ytube-transcript-wlang-v2
```

### 2. Đặt vào thư mục custom node:

```bash
~/.n8n/nodes/
```

### 3. Hoặc mount vào Docker:

```yaml
volumes:
  - ./nodes:/home/node/.n8n/nodes
```

---

## 🧪 Ví dụ input

```json
{
	"videoId": "5rJbGqNyPn4",
	"lang": "vi"
}
```

## 📤 Ví dụ output

```json
{
	"youtubeId": "5rJbGqNyPn4",
	"transcript": [
		{
			"text": "Xin chào các bạn",
			"start": 0,
			"duration": 2.5
		}
	],
	"metadata": {
		"title": "Mỹ phát ‘cảnh báo thép’...",
		"duration": 499,
		"uploader": "VIETNAM NEWS AGENCY MEDIA...",
		"uploadDate": "20250622",
		"view_count": 15000,
		"description": "..."
	}
}
```

## 🇬🇧 English

Custom node for [n8n](https://n8n.io) to **extract YouTube subtitles** via `yt-dlp`, with support for **subtitle language selection** (`vi`, `en`, `ja`, etc.), **cookie authentication**, and full `.vtt` parsing into **structured JSON**.

---

### ✨ Features

- 📼 Accepts both YouTube URL and video ID
- 🌍 Select subtitle language (`lang`: vi, en, ja,...)
- 🔐 Supports cookie-based authentication (string or file)
- 📄 Parses `.vtt` subtitle files into structured JSON (`text`, `start`, `duration`)
- 🧹 Auto-cleans temp files after use

---

### 📦 Installation

```bash
npm install @minproducer/n8n-nodes-ytube-transcript-wlang
```

Place inside custom node folder:

```bash
~/.n8n/nodes/
```

Or mount in Docker:

```yaml
volumes:
  - ./nodes:/home/node/.n8n/nodes
```

---

### 📝 License

MIT © [minproducer](https://github.com/minproducer)
