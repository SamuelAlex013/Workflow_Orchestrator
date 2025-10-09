# 🤖 AI Search API n8n Node

**Custom [n8n](https://n8n.io) node** to integrate the [AI Search API](https://aisearchapi.io?utm_source=npm) into your automation workflows.  
Bring **semantic search**, **context awareness**, **summarization**, and **balance monitoring** directly into your n8n pipelines.

[![npm version](https://img.shields.io/npm/v/n8n-nodes-aisearchapi.svg)](https://www.npmjs.com/package/n8n-nodes-aisearchapi)
[![TypeScript](https://img.shields.io/badge/TypeScript-ready-blue.svg)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-brightgreen.svg)](https://nodejs.org/)

---

## ✨ Features

- 🔍 **Semantic Search (AI Search API)** – Natural language search with embeddings  
- 🌐 **Web Search API** – Search across the web with intelligent filtering  
- 📝 **Summarization API / Summary API** – Condense long text into clear summaries  
- 💬 **Context Management** – Add previous messages for richer answers  
- 📊 **Balance Monitoring** – Track credits and usage in real time  
- ⚡ **TypeScript Support** – Strong typings and IDE hints  
- 🧩 **Seamless n8n Integration** – Drag-and-drop node inside your n8n editor  

---

## 🚀 Quick Start

### 1) Sign Up & Get Your API Key
- [🆕 Create Account](https://app.aisearchapi.io/join?utm_source=npm)  
- [🔑 Log In](https://app.aisearchapi.io/login?utm_source=npm)  
- [📊 Dashboard](https://app.aisearchapi.io/dashboard?utm_source=npm) – manage your API key  

### 2) Install the Package

From npm (recommended):

```bash
npm install n8n-nodes-aisearchapi
```

From source:

```bash
git clone https://github.com/aisearchapi/aisearchapi-n8n.git
cd aisearchapi-n8n
npm install
npm run build
```

### 3) Run n8n with the Extension

**Windows PowerShell (edit the path):**
```powershell
docker run -it --rm -p 5678:5678 `
  -e N8N_CUSTOM_EXTENSIONS=/extensions `
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true `
  -e DB_SQLITE_POOL_SIZE=5 `
  -e N8N_RUNNERS_ENABLED=true `
  -v "C:\n8n-extensions\aisearchapi-n8n:/extensions" `
  -v n8n_data:/home/node/.n8n `
  n8nio/n8n:latest
```

**macOS / Linux / WSL (edit the path):**
```bash
docker run -it --rm -p 5678:5678   -e N8N_CUSTOM_EXTENSIONS=/extensions   -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true   -e DB_SQLITE_POOL_SIZE=5   -e N8N_RUNNERS_ENABLED=true   -v "$HOME/n8n-extensions/aisearchapi-n8n:/extensions"   -v n8n_data:/home/node/.n8n   n8nio/n8n:latest
```

Then open: **http://localhost:5678**

You should see:  
`Loaded extensions from /extensions`.

---

## 🔧 Configuration in n8n

1. Go to **Credentials → New → AI Search API**  
2. Paste your **API Key** (without the `Bearer` prefix)  
3. Save  

---

## 📖 Usage

### Search API
- Resource: **Search**  
- Operation: **Search**  
- Parameters:  
  - `query` → your question (required)  
  - `responseType` → `markdown | text`  
  - `context` → optional array of messages  
  - `timeout` → ms (default `30000`)  

### Web Search API
- Resource: **Web Search**  
- Operation: **Search the web**  
- Parameters:  
  - `query` → keywords or question  
  - `maxResults` → limit number of results  
  - `filters` → optional filters  

### Summarization API / Summary API
- Resource: **Summarize**  
- Operation: **Summarize Text**  
- Parameters:  
  - `text` → input text or content  
  - `ratio` → compression ratio (0–1)  
  - `length` → target length of summary  

### Balance
- Resource: **Account**  
- Operation: **Get Balance**  

---

## ⚠️ Error Codes

| Code | Meaning | Fix |
|------|---------|-----|
| 401  | Unauthorized | Invalid key → [Get key](https://app.aisearchapi.io/join?utm_source=npm) |
| 429  | Too Many Requests | Slow down / add retry logic |
| 433  | Quota Exceeded | Buy credits / upgrade |
| 500  | Server Error | Try again later |
| 503  | Service Unavailable | Temporary downtime |

---

## 🛡️ Best Practices

- Keep your API key secret → store it in n8n **Credentials**  
- Use **Markdown** output for rich UI when possible  
- Reset **context** when you change topics  
- Monitor your **credits** via the balance endpoint  

---

## 🧰 Troubleshooting

- **Node not visible in n8n**  
  - Check `dist/...` files exist after build  
  - Verify `package.json` has `"n8n"` block  
  - Restart the Docker container after changes  
  - Run `docker exec -it <ID> sh -c "ls -R /extensions"`  

- **Cannot find package 'n8n-workflow'**  
  - Install it: `npm i n8n-workflow@1.108.2`  
  - Build as **CommonJS** (see `tsconfig.json`)  
  - Keep `node_modules` mounted into the container  

- **Windows copy errors (cp not found)**  
  - Use `shx` (already included) or PowerShell `Copy-Item`

---

## 📚 Resources

- [🌐 AI Search API Homepage](https://app.aisearchapi.io?utm_source=npm)  
- [📘 Documentation](https://docs.aisearchapi.io?utm_source=npm)  
- [🐙 GitHub Issues](https://github.com/aisearchapi/aisearchapi-n8n/issues)  
- [📦 npm Package](https://www.npmjs.com/package/n8n-nodes-aisearchapi)  
- [Blog](https://aisearchapi.io/blog/)  

---

## 🎉 Start Now

```bash
npm install n8n-nodes-aisearchapi
```

Connect your API key in n8n and build **AI-powered workflows** in minutes.

---

## 🔍 SEO Keywords

AI Search API n8n node, web search api, summary api, summarization api, search api, semantic search automation, context-aware AI n8n, AI Search API workflow automation, AI Search API key integration, n8n extension AI Search API, AI search node for n8n, n8n semantic search plugin
