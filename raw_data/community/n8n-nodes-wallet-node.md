# Wallet Node

A custom n8n node to interact with blockchain wallets using [ethers.js](https://docs.ethers.org/).

## Features

- 🔍 **Get Balance**: Check the ETH balance of any wallet address.
- 💸 **Send Transaction**: Send ETH to another address using a private key from credentials.

## Operations

### 1. Get Balance

- **Inputs**

  - `RPC URL` (e.g., Infura or Alchemy endpoint)
  - `Wallet Address` to query

- **Outputs**

  - `balanceWei`: Balance in wei
  - `balanceEther`: Balance in ETH

- **Credentials**
  - ❌ Not required

---

### 2. Send Transaction

- **Inputs**

  - `RPC URL`
  - `To Address`
  - `Amount` in ETH

- **Credentials**

  - ✅ `walletCredentialsApi` (must contain `privateKey`)

- **Outputs**
  - `txHash`: The transaction hash of the sent transaction

---

## Credentials

Create a new credential of type `walletCredentialsApi` with the following structure:

```json
{
	"privateKey": "your-wallet-private-key"
}
```

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
