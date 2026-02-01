# entitys nodes for n8n (simple)

Two standalone nodes for n8n:

- **entitys Import** (Trigger): Receives HTTP **POST** webhooks. The node UI shows only the generated webhook URLs.
- **entitys Export** (Action): Sends an HTTP **POST** request. Requires a URL and supports optional headers, query parameters, and JSON body.

## Installation
```bash
npm install n8n-nodes-entitys-simple
```

## Usage

### Import (webhook trigger)
1. Add **entitys Import** to your workflow.
2. Copy the **Test URL** or **Production URL** from the node UI.
3. Send a POST request:
```bash
curl -X POST "$WEBHOOK_URL" -H "Content-Type: application/json" -d '{"hello":"world"}'
```
4. The node outputs the request body, headers, query, method, and url.

### Export (HTTP POST action)
1. Add **entitys Export** after any node.
2. Set **URL** (required).
3. Optionally add **Query Parameters**, **JSON Body**, and **Additional Headers**.
4. The node outputs `statusCode`, `headers`, and `body`.

## Notes
- No environment variables or filesystem access.
- English-only UI and docs.
- License: MIT

## Links
- npm: https://www.npmjs.com/package/n8n-nodes-entitys-simple
- repo: https://github.com/DCrainic/n8n-nodes-entitys-simple
