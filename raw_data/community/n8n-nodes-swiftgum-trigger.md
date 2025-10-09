![Swiftgum n8n Node](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-swiftgum-trigger

A custom [n8n](https://n8n.io) trigger node built by Swiftgum.

This node allows you to trigger workflows from Swiftgum-related events or integrations.

---

## 🚀 Features

- Custom trigger node for Swiftgum-specific events
- Built for compatibility with the latest n8n versions
- Ready to use in your local or cloud-hosted n8n instance

---

## 📚 How to Use the Swiftgum Trigger Node

### 1. Add the Swiftgum Trigger to Your Workflow
- Search for `Swiftgum Trigger` in the n8n node selector.
- Add it as the starting node of your workflow.

### 2. Set Up Credentials  
- Go to **Credentials** in n8n and create new credentials with your Swiftgum API Key.  
- Click **Test Credentials** to ensure your API key is valid (it performs a call to `/schemas`).

### 3. (Optional) Filter by Schemas  
- In the node configuration, select one or more **Schema Names or IDs** to only trigger on events matching these schemas.
- Leave it blank to receive all events (`job.processed`).

### 4. Trigger Events
- Upload a PDF document in your Swiftgum workspace.
- Once the document is processed, the node will emit structured data extracted from the document.

---

### 📦 Example Event Payload

```json
{
  "id": "file-123",
  "name": "document.pdf",
  "createdAt": "2024-06-01T12:00:00.000Z",
  "receivedAt": "2024-06-01T12:00:00.000Z",
  "updatedAt": "2024-06-01T12:05:00.000Z",
  "job": {
    "id": "job-123",
    "status": "completed",
    "schema": {
      "type": "object",
      "properties": {
        "fieldA": { "type": "number", "title": "Surface" }
      }
    },
    "result": { "fieldA": 350 }
  }
}
```

---

### 🔐 Webhook Security

- Each webhook subscription generates a **signing secret** (`secret`) when created.
- Verify the authenticity of incoming events using the `X-Swiftgum-Signature` header.
- The signature is an HMAC-SHA256 hash of the raw body using your secret.

Example verification (in Node.js):

```ts
const crypto = require('crypto');
const expectedSignature = crypto
  .createHmac('sha256', secret)
  .update(rawBody)
  .digest('hex');

if (receivedSignature !== expectedSignature) {
  throw new Error('Invalid signature');
}
```

---

## 🧰 Installation

You can install this package directly via the n8n UI or CLI.

### Via n8n UI

Paste this URL into the **Install from npm** input:

```
https://www.npmjs.com/package/n8n-nodes-swiftgum-trigger
```

### Via CLI (inside your custom n8n setup)

```bash
pnpm add n8n-nodes-swiftgum-trigger
```

---

## 🧪 Local Development

To test this node locally:

```bash
pnpm install
pnpm build
```

You can also use our internal dev environment with Docker:

```bash
./fetch-node.sh
docker compose up --build
```

---

## 🗂 File Structure

```
n8n-nodes-swiftgum-trigger/
├── credentials/           # Custom credential classes
├── nodes/                 # Swiftgum Trigger node definition
├── dist/                  # Compiled output
├── gulpfile.js            # Icon handling
├── tsconfig.json
├── package.json
└── README.md
```

---

## 🧑‍💻 Contributing

Pull requests and contributions are welcome! Please:
- Follow the code structure in `nodes/` and `credentials/`
- Run `pnpm lint` before submitting
- Build locally and test in a running n8n instance

---

## 🚀 Publishing

If you're making changes to this node and want to publish them to npm:

1. Bump the version:
   ```bash
   pnpm version patch   # or minor / major
   ```

2. Publish to npm:
   ```bash
   pnpm publish --access public
   ```

> 📦 npm does not allow publishing the same version twice. Always increment the version before running `pnpm publish`.

---

## 📄 License

[MIT](LICENSE.md)
