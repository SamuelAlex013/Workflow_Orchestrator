# 🇬🇧 n8n-nodes-companies-house

An n8n community node for querying the [UK Companies House API](https://developer.company-information.service.gov.uk/).

> 🔐 Uses Basic Auth with your Companies House API key.

---

## ✨ Features

- 🔍 Search for companies by name
- 🧎 Get company profile details
- 👤 List company officers
- 📄 Fetch filing history
- 🏢 Get registered office address
- 👑 View persons with significant control (PSC)

---

## 📦 Installation

```bash
n8n install n8n-nodes-companies-house
```

Or via the n8n UI: **Settings → Community Nodes → Install**.

---

## 🔐 Credentials

- Create a Companies House API key here:  
  👉 [https://developer.company-information.service.gov.uk/manage-applications](https://developer.company-information.service.gov.uk/manage-applications)

- In n8n, add a new credential of type **Companies House API**:
  - **Username** = your API key
  - **Password** = leave blank

---

## ⚙️ Operations

| Operation                        | Input                        | Example                                |
|----------------------------------|-------------------------------|----------------------------------------|
| Search Companies                | Company name                 | `Monzo`                                |
| Get Company Profile             | Company number               | `09446231`                             |
| Get Officers                    | Company number               | `11223344`                             |
| Get Filing History              | Company number               | `11223344`                             |
| Get Registered Office Address   | Company number               | `11223344`                             |
| Get Persons with Significant Control | Company number          | `11223344`                             |

---

## 🧪 Example usage

### Search for companies:

```json
{
  "operation": "search",
  "companyInput": "OpenAI"
}
```

---

### Get filing history:

```json
{
  "operation": "getFilingHistory",
  "companyInput": "12345678"
}
```

---

## 🚰 Notes

- Only one request is made per execution.

---

## 🙌 Contributing

PRs and ideas welcome. Originally built by [Ian Carroll](https://github.com/yandaq), enhanced and maintained by [Chris Gee](https://github.com/c1gee).

---

## 📄 License

MIT

