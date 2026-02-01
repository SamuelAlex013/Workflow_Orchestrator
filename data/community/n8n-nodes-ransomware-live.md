# n8n Ransomware.live Nodes

Custom n8n node for exploring the [ransomware.live](https://www.ransomware.live) intelligence API. The node wraps the public PRO endpoints and exposes friendly parameters so you can query victims, negotiations, indicators of compromise, press coverage, and more without hand-crafting HTTP requests.

## Features

- Authenticates with the ransomware.live X-API-KEY header via a dedicated credential.
- Supports all documented resources: victims, groups, negotiations, IOCs, YARA rules, press, ransomnotes, sectors, 8-K filings, CSIRT directory, platform statistics, and key validation.
- Maps Swagger parameters to n8n fields (tickers, CIK, dates, countries, chat IDs, IOC types, etc.) and converts responses to JSON items ready for downstream nodes.
- Gracefully handles both array and object responses and surfaces raw payloads when the API returns non-JSON data.

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```
2. Build or watch the project while developing:
   ```bash
   npm run build
   # or
   npm run dev
   ```
3. Link the package into your n8n instance (or copy the compiled files) following the [n8n community nodes guide](https://docs.n8n.io/integrations/community-nodes/publish/installation/).

## Credentials

Create a new credential of type `Ransomware.live API` inside n8n and paste the API key obtained from [my.ransomware.live](https://my.ransomware.live). The credential defaults to https://api-pro.ransomware.live; override the base URL only if you run a self-hosted mirror.

The credential test hits the `/validate` endpoint to confirm the key is active.

## Supported Operations

- **Victims**: list, recent, search, get (filters for group, sector, country, dates, query, victim ID).
- **Groups**: list all groups or fetch detailed information for one group.
- **IOCs**: list IOC-enabled groups or fetch IOCs for a specific group with optional type filtering.
- **Negotiations**: list groups with chats, list negotiation metadata for a group, or fetch full chat transcripts.
- **Press**: retrieve the entire enriched press feed or just the most recent entries, optionally filtered by country.
- **Ransomnotes**: discover groups with ransom notes, list note filenames for a group, or load an individual note.
- **8-K Filings**: pull Item 1.05 / 8.01 cybersecurity filings with ticker, CIK, and date filters.
- **CSIRT Directory**: fetch national CSIRT/CERT contacts by country code.
- **Sectors**: list victim sectors with incident counts.
- **YARA Rules**: list YARA-enabled groups or fetch rules for a group.
- **Statistics**: retrieve global stats for victims, groups, press entries, and last update time.
- **Validate**: confirm the configured API key is still valid.

## Usage Tips

- Enable "Continue On Fail" in the node options when you want the workflow to proceed even if the API returns errors; the node will emit an item with the error message.
- Combine the node with `Split In Batches` or `Function` nodes to iterate victims and enrich data in parallel workflows.
- Respect ransomware.live fair-use guidelines: avoid unnecessary polling or extremely broad queries in tight loops.

## License

MIT


