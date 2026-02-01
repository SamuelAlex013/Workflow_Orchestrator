# n8n-nodes-aqbanking

An n8n community node to interact with German banks using AqBanking.

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

## ⚠️ Development Version Notice

**This version has been implemented without the aqbanking-cli tool dependency and is intended for testing purposes only.** This is a development version primarily designed for developers working on German banking integrations and should not be used in production environments. It is specifically designed for German banking institutions only.

**Please do not install this version for production use. It is meant for testing and development purposes only.**

## Installation

**Important Note**: This development version has been implemented without the `aqbanking-tools` dependency using direct FinTS/HBCI protocol implementation. This version is for testing and development purposes only and should not be used in production environments.

### Community Nodes (Recommended)

For users on n8n v0.187+, your instance owner can install this node from **Community Nodes**.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-aqbanking` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node. n8n runs `npm install` in the background.

### Manual installation

To get started install the package in your n8n root directory:

```bash
npm install n8n-nodes-aqbanking
```

For Docker-based deployments, you need to ensure `aqbanking-tools` is installed within your container. You can do this by creating a custom Dockerfile based on the official n8n image:

**Dockerfile Example:**
```dockerfile
# Use the official n8n image as a base
FROM n8nio/n8n:latest

# Switch to root user to install system packages
USER root

# Install AqBanking tools
RUN apt-get update && apt-get install -y aqbanking-tools && rm -rf /var/lib/apt/lists/*

# Install the community node
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-aqbanking

# Switch back to the node user
USER node
```

Build and run this custom image instead of the standard one.

### Manual installation

To get started install the package in your n8n root directory:

```bash
npm install n8n-nodes-aqbanking
```

## Prerequisites

**Development Version**: This version does not require AqBanking to be installed as it uses a direct FinTS/HBCI implementation. However, it is intended for testing and development purposes only.

**Important**: This version is designed specifically for German banking institutions and should only be used by developers working on banking integrations for testing purposes.

## Configuration

### Development Version Setup

This version uses direct FinTS/HBCI protocol implementation and does not require AqBanking setup.

### Credentials

The node requires the following credentials:

- **Bank Code (BLZ)**: Your bank's routing number
- **User ID**: Your online banking user ID
- **PIN**: Your online banking PIN
- **FinTS URL**: Your bank's FinTS server URL (optional, will be auto-detected if not provided)

## Operations

### Get Balance

Retrieves the current balance of a specified bank account.

**Parameters:**
- **Account Number**: The bank account number to query

**Output:**
```json
{
  "balance": 1234.56,
  "currency": "EUR"
}
```

### Get Transactions

Retrieves the transaction history for a specified bank account within a given date range.

**Parameters:**
- **Account Number**: The bank account number to query
- **Start Date**: The start date for the transaction query (YYYY-MM-DD)
- **End Date**: The end date for the transaction query (YYYY-MM-DD)

**Output:**
```json
{
  "transactions": [
    {
      "date": "2023-10-27",
      "amount": -50.00,
      "currency": "EUR",
      "remoteName": "REWE",
      "purpose": "Einkauf"
    },
    {
      "date": "2023-10-26",
      "amount": 1200.00,
      "currency": "EUR",
      "remoteName": "Arbeitgeber",
      "purpose": "Gehalt"
    }
  ]
}
```

## Usage Example

1. Add the AqBanking node to your workflow
2. Configure your AqBanking credentials
3. Select the desired operation ("Get Balance" or "Get Transactions")
4. Enter the required parameters for the selected operation
5. Execute the workflow

The node will return the current balance and currency for the specified account.

## Compatibility

- **n8n version**: 0.187.0 or higher
- **Node.js**: 16.x or higher
- **AqBanking**: 6.x or higher

## Security Notes

- Your banking credentials are securely stored in n8n's credential system
- The PIN is encrypted and never logged
- All communication with AqBanking happens locally on your system
- No banking data is transmitted to external services

## Troubleshooting

### Common Issues

**"aqbanking-cli command not found"**
- Make sure AqBanking is installed on your system
- Verify `aqbanking-cli` is in your system PATH

**"Authentication failed"**
- Double-check your User ID and PIN
- Ensure your AqBanking setup is complete and working
- Test with `aqbanking-cli request --balance` first

**"Could not parse balance"**
- Your bank might return a different format
- Check the raw output with `aqbanking-cli request --balance`
- Open an issue with the output format for support

## Development

### Building

```bash
npm run build
```

### Development Mode

```bash
npm run dev
```

### Linting

```bash
npm run lint
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/CePeHH/n8n-nodes-aqbanking/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/CePeHH/n8n-nodes-aqbanking/discussions)
- 📖 **n8n Documentation**: [docs.n8n.io](https://docs.n8n.io)
- 🏦 **AqBanking Documentation**: [AqBanking Wiki](https://wiki.gnucash.org/wiki/AqBanking)

## Disclaimer

**This development version is provided for testing and development purposes only.** It should not be installed or used in production environments. This version is specifically designed for developers working on German banking integrations and is limited to German banking institutions only.

Always verify transactions and balances through your bank's official channels. The authors are not responsible for any financial losses or damages that may occur from using this development version.

---

**Keywords**: n8n, node, aqbanking, german banks, hbci, fintech, automation, workflow
