# 📟 n8n-nodes-vatfix-plus

Custom n8n community node for **VATFix Plus** — Real-time EU VAT validation with VIES fallback.

---

## 🚀 Features

* Validate EU VAT numbers via VATFix Plus API
* Works when official VIES service is down
* Headers + rate limits identical to public API
* Full support for `/vat/lookup` and `/reset` endpoints

---

## 🔑 Prerequisites

1. [Sign up at VATFix Plus](https://plus.vatfix.eu/buy)
2. Copy your **API Key**.
3. Install this node in your n8n instance.

---

## 📦 Installation

From your n8n root:

```bash
npm install n8n-nodes-vatfix-plus
```

Restart n8n. Node appears as **VATFix Plus** inside the Editor.

---

## ⚙️ Usage

### Credentials

* **API Key** → `x-api-key`
* **Customer Email** → `x-customer-email`

### Example Workflow

1. Add **VATFix Plus** node.
2. Set `countryCode = DE`, `vatNumber = 12345678901`.
3. Connect to downstream nodes (CRM, database, etc.).

Output:

```json
{
  "valid": true,
  "countryCode": "DE",
  "vatNumber": "12345678901",
  "traderName": "Example GmbH",
  "traderAddress": "Berlin"
}
```

---

## 💳 Plans

* Starter — €29/mo (10k req)
* Growth — €79/mo (50k req)
* Scale — €199/mo (250k req)

👉 [Manage subscription](https://billing.stripe.com/p/login/14A14o2Kk69F6Ei2hQ5wI00)

---

## 🛡️ Notes

* Rate limit: 120 requests/min per key
* Rotate key anytime: `POST /reset`
* Responses cached 12h in S3

---

## 📬 Support

* Docs: [plus.vatfix.eu/plus](https://plus.vatfix.eu/plus)
* Email: [support@vatfix.eu](mailto:support@vatfix.eu)

---

## 📜 License

[MIT](./LICENSE)
