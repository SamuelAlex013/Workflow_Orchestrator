# n8n-nodes-browserai

**BrowserAI** – a powerful, serverless platform for AI-driven browser automation, web scraping, and data extraction at scale.

Whether you're a developer, data scientist, or growth hacker, BrowserAI is designed to make your life easier when dealing with complex websites and anti-bot systems.

---

## 🔍 What is BrowserAI?

BrowserAI is a next-gen browser automation platform that:

✅ Uses AI to automate web tasks via natural language or API  
✅ Handles CAPTCHAs, IP blocks, browser fingerprinting & anti-bot detection  
✅ Supports Puppeteer, Playwright, and Selenium  
✅ Scales effortlessly – no server setup needed  
✅ Lets you build scrapers, bots, and workflows in minutes  
✅ Watch the action live  

---

## 🚀 Features

### 🛡️ Stealth-mode browsing for unstoppable AI agents

Your AI agent browses like a real user – handling cookies, solving CAPTCHAs, and blending in naturally for smooth, uninterrupted access.

- 🍪 Handle cookies  
- 🧠 Browser fingerprinting  
- 🔐 CAPTCHA solving  
- 🔁 Set referral headers  
- 🕵️ Manage specific user agents  

---

### 🤖 Smarter scraping with adaptive intelligence

Dynamic content? No problem. Failed requests? We've got automatic retries. Need fresh IPs? Consider it done.

- ⚙️ JavaScript rendering  
- 🔄 Automatic retries and IP rotation  
- ✅ Data integrity validations  

---

### 🌍 Borderless data access for limitless insights

Your AI agent can access region-specific content anywhere. From local pricing to market trends, get the data you need—no matter where it's hiding.

- 🌐 Worldwide geo-coverage  

---

## 📡 API Endpoints

| Method | Endpoint Description           |
|--------|--------------------------------|
| `POST` | Create a new task              |
| `POST` | Force stop a task              |
| `GET`  | Get task metadata              |
| `GET`  | Get task results               |
| `POST` | Create saved task              |
| `GET`  | Get list of saved tasks        |
| `GET`  | Get saved task by name         |

---

## 💡 A Few Ideas to Get You Started

- 🛒 Open amazon.com, search for **AirPods Pro 2**, find the three best prices available and extract as a JSON file  
- 🏠 Open airbnb.com, search for **apartments in London**, find the five closest spots to the city center  
- 💼 Open google.com, search for **software engineering jobs in Seattle, Washington**, and return all results in JSON format  

---

## 📦 Installation

To install this node in your custom n8n instance:

```bash
npm install n8n-nodes-browserai