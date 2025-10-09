<p align="center">
  <img src="nodes/Authentica/authentica.svg" alt="Authentica" width="120" />
</p>

<h1 align="center">Authentica for n8n</h1>

<p align="center">
  Saudi identity & communications APIs for OTP and balance — packaged as an n8n Community Node.
</p>

---

## ✨ What’s included in v0.1.0

This first release focuses on the essentials:

* **Account → Get Balance**
* **OTP → Send** (SMS / WhatsApp / Email)
* **OTP → Verify**


---

## 🧰 Requirements

* n8n **v1.x** (self‑hosted or desktop)
* Node.js **>= 20** (for local development)
* An **Authentica API key** (header: `X-Authorization`)

---

## 🚀 Install

### Install from the n8n editor (Community Nodes)

1. Open the n8n editor → **Settings → Community Nodes → Install**.
2. Search for **Authentica** (package **`n8n-nodes-authentica`**).
3. Click **Install** and confirm the warning screen.
4. n8n downloads the package from npm and reloads. You’ll now see **Authentica** in the Nodes panel.

### Update / Uninstall

* **Update:** Settings → Community Nodes → find *Authentica* → **Update**.
* **Uninstall:** Settings → Community Nodes → find *Authentica* → **Uninstall**.

### Offline / Self‑hosted without Community Nodes

If Community Nodes is disabled in your environment, install via npm on the host that runs n8n and point the extensions path:

```bash
npm i n8n-nodes-authentica
export N8N_CUSTOM_EXTENSIONS="/absolute/path/to/node_modules/n8n-nodes-authentica"
n8n start
```

---

## 🔐 Credentials — *Authentica API*

Create a new credential in **Credentials → New → Authentica API**.

**Fields**

* **API Key** *(required)*: your Authentica key (sent as `X-Authorization`) 
* **Base URL** *(optional)*: defaults to `https://api.authentica.sa`

**Test**

* Click **Test** to call `/api/v2/balance` — you should see **Success**.

---

## 🧩 Node usage

### 1) Account → Get Balance

* **Resource:** `Account`
* **Operation:** `Get Balance`
* **Output:** `{ balance: number }`

### 2) OTP → Send

* **Resource:** `OTP`
* **Operation:** `Send`
* **Channel:** `SMS` | `WhatsApp` | `Email`
* **Phone** *(required for SMS/WhatsApp)*: **E.164** format, e.g. `+9665XXXXXXX`
* **Email** *(required for Email)*: valid email
* **Optional:** message/template fields as supported by your Authentica app

**Output (example)**

```json
{
	"success": true,
	"data": null,
	"message": "OTP send successfully"
}
```

### 3) OTP → Verify

* **Resource:** `OTP`
* **Operation:** `Verify`
* **Verify With:** `Phone` or `Email`
* **Code:** the OTP the user received

**Output (example)**

```json
{
	"status": true,
	"message": "OTP verified successfully"
}
```

> **Validation built‑in:**
>
> * Phone must be E.164 (`+<country><number>`). Example KSA mobile: `+9665…`
> * Email must be a well‑formed address.

---

## 🐞 Troubleshooting

* **401 Unauthorized** → API key missing/invalid. Recheck the *Authentica API* credential, header `X-Authorization`.
* **422 Unprocessable Entity** → A required field is missing or invalid (e.g., non‑E.164 phone). Fix inputs and retry.
* **Rate limiting** → If you expect bursts, add a **Wait** or **Rate Limit** node before the Authentica node.
* **Large execution data** → Run with the top‑bar **Execute workflow** button, or enable on‑disk binaries.

---

## 📦 Build locally (contributors)

```bash
npm ci
npm run lint
npm run build
# local load
export N8N_CUSTOM_EXTENSIONS="$PWD"
n8n start
```


---

## 🔒 Security & privacy

* Keep API keys in **Credentials** (never hardcode in workflows).
* Use **E.164** phones and never log sensitive PII in plaintext nodes.

---


## 🙌 Thanks

Built by the **Authentica** team to help developers verify users and reduce fraud in Saudi Arabia.

* Website: [https://authentica.sa](https://authentica.sa)
* Issues / Feedback: [Support Email](mailto:support@authentica.sa)

---

## 📄 License (MIT)

```
MIT License

Copyright (c) 2025 Authentica

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

```

---

### File layout (what gets published)

```
.
├─ dist/                               # compiled node + credentials + svg
├─ README.md                           # this file
├─ LICENSE
├─ CHANGELOG.md
└─ package.json
```
