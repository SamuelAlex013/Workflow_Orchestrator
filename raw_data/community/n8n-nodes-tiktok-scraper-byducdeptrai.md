![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-tiktok-scraper

An **n8n community node** that scrapes TikTok profile posts using **Puppeteer**.
Supports **Video / Photo / All**, profile counters (**followers, following, likes**), **cookies**, **proxy**, concurrency and anti-CAPTCHA friendly pacing.

> ⚠️ Heads-up: Puppeteer may not run on **n8n Cloud**. Self-hosting is recommended.

---

## Features

* Scrape profile grid (supports both **video** and **photo** posts)
* Per-item details: `type_post`, `video_id`, counts (views/likes/comments/shares/saves), caption, hashtags, music, duration
* Fallback timestamp from **video ID** (works even when DOM metadata isn’t available)
* Profile counters (followers / following / total likes) appended to each item
* Cookies, proxy, custom UA, extra headers, viewports, retries
* Performance switch: **Block Media** (images/media/css/fonts) while scrolling

---

## Installation

### A) Install from n8n UI (Community Nodes)

1. `Settings → Community Nodes → Install`
2. Enter package name: **`n8n-nodes-tiktok-scraper`**
3. After install, search for **TikTok Scraper** in the node list.

> If you don’t see “Community Nodes”, enable the env var:
> `N8N_COMMUNITY_PACKAGES_ENABLED=true`

### B) Self-host via custom extensions folder

```bash
export N8N_CUSTOM_EXTENSIONS=/path/to/extensions
cd $N8N_CUSTOM_EXTENSIONS
npm i n8n-nodes-tiktok-scraper
# restart n8n (or docker restart) and the node will appear
```

---

## Requirements

* Node.js **>= 18**
* A runtime that can launch **Chromium/Chrome** for Puppeteer
* For Docker: increase shared memory (`shm_size: "1gb"`) to avoid Chrome crashes

---

## Usage

Add **TikTok Scraper** node to your workflow and configure:

### Required

* **Username**: TikTok handle without `@` (e.g., `tiktok`)

### Core options

* **Max Videos**: `0 = unlimited` (default: 100)
* **Post Type**: `All | Video | Photo`
* **Concurrency**: parallel tabs (default: 4)
* **Per-Video Delay (MS)**: base delay per item (default: 500)
* **Headless**: `True | New | False` (default: True)
* **Timeout (MS)**: navigation/selector wait (default: 45000)
* **Hard Scroll Timeout (MS)**: max time to scroll profile (default: 600000)
* **User Agent**: override if needed

### Additional Options (collection)

* **Block Media (Faster)**: boolean (default: **true**)
* **Cookies (JSON Array)**: paste an **array** of cookies from your browser session
  Example:

  ```json
  [
    { "name": "ttwid", "value": "…", "domain": ".tiktok.com", "path": "/", "httpOnly": true, "secure": true },
    { "name": "sid_tt", "value": "…", "domain": ".tiktok.com", "path": "/", "httpOnly": true, "secure": true }
  ]
  ```
* **Proxy URL**: e.g., `http://user:pass@host:port`
* **Executable Path**: custom Chrome/Chromium path (optional)
* **Extra Headers**: key/value list (e.g., `Accept-Language`)
* **Retries**: per-item retry attempts (default: 2)
* **Viewport Width / Height**: default `1366 × 768`
* **Emit Profile Summary**: prepend one summary item with counters

---

## Output (example)

```json
{
  "video_id": "7345678901234567890",
  "type_post": "video",
  "url": "https://www.tiktok.com/@user/video/7345678901234567890",
  "caption": "Sample caption #tag",
  "created_at": "2024-05-01T12:34:56.000Z",
  "created_at_ts": 1714566896,
  "views": 1200,
  "views_grid": 1200,
  "likes": 150,
  "comments": 12,
  "shares": 3,
  "saves": 0,
  "author_username": "user",
  "music_title": "Track",
  "music_author": "Artist",
  "duration": 17,
  "hashtags": ["tag"],
  "profile_following": 827,
  "profile_followers": 70700,
  "profile_likes": 321600
}
```

> Numeric fields default to **0** when the source value is missing/`null`.

---

## Anti-CAPTCHA Tips

To reduce verification prompts:

* Use **valid cookies** from a real Chrome session (logged in, CAPTCHA solved)
* Prefer **residential proxy** from the same country as your cookies
* **Headless**: True, **Concurrency**: 1, **Per-Video Delay**: 1200–2000 ms
* Keep **Block Media (Faster)** enabled
* Set **Accept-Language** to match your region, e.g. `vi-VN,vi;q=0.9,en-US,en;q=0.8`
* Use a realistic, consistent **User Agent**

---

## Docker (example)

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    environment:
      N8N_CUSTOM_EXTENSIONS: /custom
      PUPPETEER_EXECUTABLE_PATH: /usr/bin/chromium
      TZ: Asia/Ho_Chi_Minh
    volumes:
      - ./custom:/custom
      - ./n8n_data:/home/node/.n8n
    shm_size: "1gb"
```

If your base image doesn’t include Chromium, extend the image and install it (Debian/Ubuntu packages), then set `PUPPETEER_EXECUTABLE_PATH`.

---

## Troubleshooting

* **CAPTCHA detected** → provide cookies, use residential proxy, reduce concurrency and increase delays.
* **Navigation timeout exceeded** → increase `Timeout (MS)`; ensure proxy/cookies/headers are valid.
* **Chromium not found** → install Chromium or set `Executable Path`.
* **n8n Cloud** → Puppeteer may not be supported; self-host or use a remote browser service.

---

## Development

```bash
npm run lint
npm run build
npm publish --access public
```

Ensure `dist/**`, `index.js`, `icon.svg` are included in the npm package (via `files` + a copy script if needed).

---

## Disclaimer

This project is for educational/integration purposes. Use responsibly and respect TikTok’s Terms of Service and local laws.

---

## License

MIT

---

