# n8n-nodes-nwc

Custom n8n nodes for Nostr Wallet Connect (NWC) protocol integration.

## Features

- **Send Satoshis**: Send Bitcoin Lightning payments to addresses or invoices
- **Make invoice**: Create Lightning invoices to receive payments
- **List Transactions**: View recent transaction history
- **Lookup Invoice**: Look up invoice details from a BOLT-11 invoice or payment hash
- **Get Info**: Get wallet information and capabilities
- **Get Balance**: Get current wallet balance
- **Make Keysend Payment**: Send payment using keysend (no invoice required)
- **Sign Message**: Sign a message with the wallet

## Installation

1. Add community node in your n8n instance:
```
n8n-nodes-nwc
```

## Configuration

### NWC API Credentials

You'll need to configure the following credential:

1. **NWC URL**: Your NWC connection URL

### Getting NWC URL

1. **Using Alby hub**:
   - Go to https://albyhub.com
   - Create new NWC connection
   - Copy the NWC URL provided

2. **Using other wallets**:
   - Look for NWC connection settings in your wallet
   - Copy the NWC URL (format: `nostr+walletconnect://...`)

The NWC URL contains all the necessary connection information including relay, keys, and wallet details.

## Usage

### Send Satoshis

Configure the node with:
- **Operation**: Send Satoshis
- **Amount**: Amount in satoshis to send
- **Recipient**: Lightning address or invoice
- **Description**: Optional payment description

### Make invoice

Configure the node with:
- **Operation**: Make invoice
- **Amount**: Amount in satoshis to request
- **Description**: Description for the invoice

### List Transactions

Configure the node with:
- **Operation**: List Transactions
- **Limit**: Maximum number of transactions to return

### Lookup Invoice

Configure the node with:
- **Operation**: Lookup Invoice
- **Invoice or Payment Hash**: BOLT-11 invoice or payment hash to look up

### Get Info

Configure the node with:
- **Operation**: Get Info

### Get Balance

Configure the node with:
- **Operation**: Get Balance

### Make Keysend Payment

Configure the node with:
- **Operation**: Make Keysend Payment
- **Destination**: Destination node public key
- **Amount**: Amount in satoshis to send
- **Memo**: Optional memo for the payment

### Sign Message

Configure the node with:
- **Operation**: Sign Message
- **Message**: Message to sign

## Example Workflows

### Payment Processing

1. **Trigger**: Webhook or schedule
2. **NWC Node**: Send Satoshis
3. **Condition**: Check payment success
4. **Action**: Update database or send notification

### Invoice Generation

1. **Trigger**: Manual or API call
2. **NWC Node**: Make invoice
3. **Action**: Store invoice details
4. **Action**: Send invoice to customer

## Development

### Project Structure

```
n8n-nodes-nwc/
├── credentials/
│   └── NwcUrl.credentials.ts
├── nodes/
│   └── Nwc/
│       ├── Nwc.node.ts
│       └── nwc.svg
├── package.json
├── tsconfig.json
├── gulpfile.js
└── README.md
```

### Building

```bash
# Build the project
npm run build

# Watch for changes during development
npm run dev

# Format code
npm run format

# Lint code
npm run lint
```

## NWC Protocol

This node uses the [Alby NWC SDK](https://github.com/getAlby/alby-js-sdk) to implement the Nostr Wallet Connect (NWC) protocol as specified in the [official documentation](https://docs.nwc.dev/).

### Key Features

- **Alby SDK Integration**: Uses the official Alby NWC SDK for reliable wallet communication
- **Lightning Network**: Supports Bitcoin Lightning payments
- **Simplified Setup**: Single NWC URL credential for easy configuration
- **Automatic Connection Management**: SDK handles connection, encryption, and disconnection

### Supported Methods

- `pay_invoice`: Send payments to Lightning invoices
- `make_invoice`: Generate Lightning invoices
- `list_transactions`: Retrieve transaction history
- `lookup_invoice`: Look up invoice details from BOLT-11 invoice or payment hash
- `get_info`: Get wallet information and capabilities
- `get_balance`: Get current wallet balance
- `pay_keysend`: Send payments using keysend protocol
- `signMessage`: Sign messages with wallet

## Troubleshooting

### Common Issues

1. **Connection Timeout**: Check your NWC URL and network connection
2. **Authentication Error**: Verify your NWC URL is correct and not expired
3. **Wallet Not Found**: Ensure your wallet is online and the NWC URL is valid

### Debug Mode

Enable debug logging by setting the `NODE_ENV=development` environment variable.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Check the [NWC documentation](https://docs.nwc.dev/)
- Join the Nostr community

## Changelog

### v1.0.0
- Initial release
- Alby NWC SDK integration
