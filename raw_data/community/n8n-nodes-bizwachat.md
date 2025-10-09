<p align="center">
  <img src="https://bizwachat.com/media/public/6SdyZBP5DKcS7U7WZaM5xZuIBh0deEoXvtHk13q3.png" alt="Bizwachat Logo" width="160"/>
</p>

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)


## 📝 Release Notes & Functionality Overview

### 🚀 Latest Changes

- **API Alignment:**  
  All node operations and payloads now strictly follow the latest Bizwachat API reference:
  - **Send Text Message:** Uses `POST /api/send` with support for `phone`, `message`, `header`, `footer`, and `buttons`.
  - **Send Media Message:** Uses `POST /api/send/media` with `phone`, `media_type`, `media_url`, `caption`, and `file_name`.
  - **Send Template Message:** Uses `POST /api/send/template` with a `template` object (`name`, `language`, `components`) as per API docs.
- **Legacy Logic Removed:**  
  All deprecated endpoints and legacy payloads have been removed for clarity and reliability.
- **UI & Parameter Improvements:**  
  Node properties and UI fields have been updated for clarity, validation, and to match the latest API requirements.
- **Media Upload:**  
  Supports uploading media files and using the returned URL in media messages.
- **Template Variable Mapping:**  
  Dynamic mapping for template variables, including support for body, header, and button parameters.
- **Error Handling:**  
  Robust error handling and input validation for all API calls.
- **Documentation & Comments:**  
  Inline comments and descriptions updated for easier usage and maintenance.

### 💡 Functionality

- **Send WhatsApp Text Messages:**  
  With optional headers, footers, and interactive buttons.
- **Send WhatsApp Media Messages:**  
  Supports images, videos, documents, and audio with captions and filenames.
- **Send WhatsApp Template Messages:**  
  Full support for template structure, language, and dynamic parameters.
- **Media Upload:**  
  Upload files to Bizwachat and use them in outgoing messages.
- **Dynamic Template & Label Loading:**  
  Fetch templates and labels directly from your Bizwachat account.
- **Scheduling & Labels:**  
  (If supported by your API) Schedule messages and assign labels.

---

**For full API details, see the Bizwachat API Reference.**

---
