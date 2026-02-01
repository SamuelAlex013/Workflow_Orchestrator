\# n8n-nodes-crowd-bf-explorer



\*\*Crowd BF Explorer\*\* is a custom \[n8n](https://n8n.io) node that lets you explore the Cardano blockchain and submit transactions via the \[Blockfrost API](https://blockfrost.io).



---



\## ✨ Features

\- 🔍 Get Cardano address info (balance, UTXOs, recent transactions)

\- 🔎 Fetch transaction details by hash

\- 📨 Submit signed transactions (CBOR hex format)

\- ⚙️ Options for validation-only mode and waiting for confirmation



---



\## 📦 Installation



Clone this repo into your n8n custom nodes folder:



```bash

git clone https://github.com/crowdtrendz/n8n-nodes-crowd-bf-explorer.git

cd n8n-nodes-crowd-bf-explorer

npm install

npm run build



