# n8n-nodes-llmlayer

An n8n **Community Node** for [LLMLayer](https://llmlayer.ai) — a Search & Answer API that combines web search with AI-generated, source-grounded responses.

---

## Features

* **AI‑Powered Answers**: Generate comprehensive answers using popular models (GPT‑4o, Claude 3.5, Gemini, etc.).
* **Web Search**: General, news, shopping, videos, images, and scholar search types.
* **Content Extraction**: Scrape public pages and return Markdown/HTML, or request PDFs/screenshots.
* **YouTube Transcripts**: Retrieve transcripts from YouTube videos.
* **PDF Text**: Extract text and metadata from PDFs.

> Availability of specific models/features depends on your LLMLayer account and current API support.

---

## Compatibility

* **n8n**: 1.68+ recommended
* **Node.js**: 20+ recommended (align with n8n’s LTS baseline)

---

## Installation

### A) n8n Cloud / In‑Editor Browse

If/when this package is **verified by n8n**, you can install it directly from the editor:

1. **Settings → Community Nodes → Browse**
2. Search for `LLMLayer` or `n8n-nodes-llmlayer`
3. Click **Install**

> If it’s not yet verified, use the self‑hosted options below.

### B) Self‑Hosted n8n

**From the UI**

1. **Settings → Community Nodes → Install**
2. Enter `n8n-nodes-llmlayer`
3. Install and restart n8n if prompted

**Using npm inside your instance**

```bash
npm install n8n-nodes-llmlayer
```

**Using Docker (inside the container)**

```bash
docker exec -it <n8n-container> npm install n8n-nodes-llmlayer
```

Then restart your container.

**Via environment variable (install at startup)**

```bash
# Add to your n8n environment
N8N_COMMUNITY_PACKAGES=n8n-nodes-llmlayer
```

---

## Authentication

1. Sign up at **[https://app.llmlayer.ai](https://app.llmlayer.ai)** and create an API key.
2. In n8n, go to **Credentials → New → LLMLayer**.
3. Paste your API key and **Save**.

> This node sends your queries/URLs to LLMLayer; review your privacy and data‑handling requirements before production use.

---

## Node Overview

The node exposes the following **resources**:

### 1) Answer

Generate AI answers grounded in real‑time search.

* **Query** — Question/prompt
* **Model** — Pick from supported models
* **Answer Type** — `markdown` | `html` | `json`
* **Search Type** — `general` | `news`
* **System Prompt** — Optional instructions
* **Location / Date Filter / Recency** — Tune search context
* **Citations / Return Sources** — Include sources and documents
* **Temperature / Max Tokens** — Output control

### 2) Web Search

Perform targeted searches.

* **Search Type** — `general`, `news`, `shopping`, `videos`, `images`, `scholar`
* **Query**, **Location**, **Recency**
* **Domain Filters** — Include/exclude specific domains

### 3) Scrape

Extract content from public web pages.

* **URL**
* **Format** — `markdown`, `html`, `pdf`, `screenshot`
* **Include Images / Links**

### 4) YouTube

Fetch video transcripts.

* **URL**
* **Language** (optional)

### 5) PDF

Extract text from a PDF URL.

* **URL**

---

## Usage Examples

### Answer (Markdown)

```json
{
  "resource": "answer",
  "query": "What are the latest developments in AI?",
  "model": "openai/gpt-4o-mini",
  "answer_type": "markdown",
  "citations": true,
  "return_sources": true
}
```

### News Search (Past Week, US)

```json
{
  "resource": "webSearch",
  "query": "artificial intelligence breakthroughs",
  "search_type": "news",
  "recency": "week",
  "location": "us"
}
```

### Structured JSON Answer

```json
{
  "resource": "answer",
  "query": "List top 5 programming languages",
  "model": "anthropic/claude-3-5-sonnet-latest",
  "answer_type": "json",
  "json_schema": {
    "type": "object",
    "properties": {
      "languages": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "rank": {"type": "number"},
            "use_cases": {"type": "array"}
          },
          "required": ["name", "rank"]
        }
      }
    },
    "required": ["languages"]
  }
}
```

---

## Error Handling & Tips

* Enable **Continue On Fail** to keep workflows running on non‑critical errors.
* Common issues:

    * **401/403** → Invalid/expired API key
    * **429** → Rate limit exceeded (add a Wait node or retry)
    * **Network timeouts** → Increase node timeout or add retries
    * **Access‑restricted pages** (Scrape) → Paywalls/blocks/dynamic content may limit extraction

---

## Support

* **Docs**: [https://docs.llmlayer.ai](https://docs.llmlayer.ai)
* **Issues**: [https://github.com/YassKhazzan/n8n-nodes-llmlayer/issues](https://github.com/YassKhazzan/n8n-nodes-llmlayer/issues)
* **Email**: [support@llmlayer.ai](mailto:support@llmlayer.ai)

---

## License

MIT

---

## Author

Yassine Khazzan — [LLMLayer](https://llmlayer.ai)

---

## Changelog

### 1.0.2

* Polish: README, metadata, minor fixes

### 1.0.1

* Passed security scan

### 1.0.0

* Initial release with Answer, Web Search, Scrape, YouTube, PDF
