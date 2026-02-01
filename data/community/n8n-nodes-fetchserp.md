# n8n-nodes-fetchserp

FetchSERP Community Node for [n8n](https://n8n.io)
=================================================

This community node lets you access the full [FetchSERP](https://www.fetchserp.com/) API from your n8n workflows. FetchSERP provides SEO, SERP, scraping, and domain-intelligence endpoints that help you build automations around keyword research, backlink analysis, and on-page data gathering.

---
[Installation](#installation) · [Operations](#operations) · [Credentials](#credentials) · [Usage](#usage) · [Version History](#version-history)

## Installation

Follow the [community-node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/).

```bash
npm install n8n-nodes-fetchserp
```

Self-hosted n8n users: make sure the directory containing this package is referenced by the `N8N_CUSTOM_EXTENSIONS` environment variable (or use the in-app *Community Nodes ➞ Install* UI in recent n8n versions).

## Credentials

Create a new **FetchSERP API** credential in n8n and paste your API token.  
Optional: change the base URL if you use a custom FetchSERP domain.

## Operations

The node exposes 20 FetchSERP endpoints:

| Operation (internal value) | Description |
|---------------------------|-------------|
| Get Backlinks (`get_backlinks`) | Retrieve backlinks for a given domain |
| Get Domain Emails (`get_domain_emails`) | Find emails mentioned on pages of a domain |
| Get Domain Info (`get_domain_info`) | WHOIS, DNS, SSL, tech stack |
| Get Keywords Search Volume (`get_keywords_search_volume`) | Monthly volume for keywords |
| Get Keywords Suggestions (`get_keywords_suggestions`) | Autocomplete & related keywords |
| Get Long-Tail Keywords (`get_long_tail_keywords`) | AI-generated long-tails for a seed keyword |
| Get Moz Analysis (`get_moz_analysis`) | Domain Authority, Page Authority, etc. |
| Check Page Indexation (`check_page_indexation`) | Whether pages rank for a keyword |
| Get Domain Ranking (`get_domain_ranking`) | SERP positions for a domain & keyword |
| Scrape Webpage (`scrape_webpage`) | Raw HTML without JS |
| Scrape Domain (`scrape_domain`) | Crawl domain up to N pages |
| Scrape Webpage JS (`scrape_webpage_js`) | Execute custom JS on a page |
| Scrape Webpage JS & Proxy (`scrape_webpage_js_proxy`) | Same as above via geo-proxy |
| Get SERP Results (`get_serp_results`) | Structured SERP JSON (titles, links, etc.) |
| Get SERP HTML (`get_serp_html`) | Raw SERP HTML |
| Get SERP AI Mode (`get_serp_ai_mode`) | AI Overview & AI-generated answer |
| Get SERP Text (`get_serp_text`) | Extracted text-only SERP |
| Get User Info (`get_user_info`) | Remaining credits & plan info |
| Get Webpage AI Analysis (`get_webpage_ai_analysis`) | AI summary of page content |
| Get Webpage SEO Analysis (`get_webpage_seo_analysis`) | SEO checklist for a page |

## Usage

The node keeps the UI minimal so you can pass any existing or future parameters without updating the package.

1. **Select an operation** in the dropdown.
2. **Query Parameters (JSON)** – provide GET/querystring parameters as JSON.
3. For the two POST endpoints, also fill **Request Body (JSON)**.

### Examples

**Domain info of example.com**
```json
{
  "domain": "example.com"
}
```

**Scrape a page with JS**
```jsonc
// Query Parameters (JSON)
{
  "url": "https://example.com"
}
// Request Body (JSON)
{
  "url": "https://example.com",
  "js_script": "return document.title"
}
```

After execution the node returns the raw JSON from FetchSERP, so you can continue parsing it with Merge, Set, IF, etc.

## Version History

* 0.1.1 — initial public release

---
Made with ❤️ by Olivier — PRs & issues welcome.
