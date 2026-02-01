# App Store Finance Node – Custom n8n Node for App Store Connect Financial Reports

This is a community node for [n8n](https://n8n.io/), designed to automate the retrieval and parsing of financial reports from [Apple App Store Connect](https://api.appstoreconnect.apple.com).

## ✨ Key Features

- 🔐 Authenticates with App Store Connect API using JWT
- 📥 Downloads financial and finance detail reports in TSV format
- 📊 Parses and outputs detailed transactions and per-country aggregates
- 🗃️ Supports both `FINANCIAL` and `FINANCE_DETAIL` report types
- 📦 Returns structured JSON or raw file in binary mode

## ⚙️ Node Operations

| Operation          | Description                                                  |
|--------------------|--------------------------------------------------------------|
| `Download & Parse` | Downloads and parses the financial report into JSON fields   |
| `Download`         | Downloads and decompresses the `.tsv` file as binary         |


## 📦 Installation

Install the node using:

```bash
npm install n8n-node-appstore-finance
```

Or follow the [official guide](https://docs.n8n.io/integrations/community-nodes/installation/) for installing community nodes.

## 🔐 Credentials

This node requires an Apple API key in the form of:

- **Issuer ID**
- **Key ID**
- **Private Key** (PEM format, can be Base64 encoded)

## ✅ Compatibility

Tested with:
- `n8n` version: `1.81.0`
- `Node.js`: `>=18.x`

## 📚 Resources

- [App Store Connect API Reference](https://developer.apple.com/documentation/appstoreconnectapi)
- [n8n Community Node Docs](https://docs.n8n.io/integrations/community-nodes/)

---

Pull requests welcome!
