# n8n-nodes-binkai

A powerful n8n module that integrates BinkAI functionality for blockchain and Web3 operations. This module enables seamless interaction with various blockchain networks and DeFi protocols through n8n workflows.

## Features

- **Blockchain Operations**

  - Wallet balance checking
  - Token transfers
  - Token swaps
  - Cross-chain bridging
  - Staking operations

- **DeFi Protocol Integration**

  - Jupiter (Solana)
  - PancakeSwap
  - Kyber
  - Thena
  - Venus
  - And more...

- **Additional Capabilities**
  - Image processing
  - Knowledge base integration
  - RPC provider support
  - Multi-chain support

## Installation

Follow the installation guide in the n8n community nodes documentation.

Also pay attention to Environment Variables for using tools in AI Agents. It's mandatory to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true` if you want to use the BinkAI nodes as tools in AI Agents.

## Credentials

The BinkAI nodes support the following types of credentials:

### API Key Based Authentication

- **API Key**: Your BinkAI API key
- **Environment**: The environment to use (mainnet/testnet)
- **Network**: The blockchain network to connect to

### Wallet Based Authentication

- **Private Key**: Your wallet's private key (encrypted)
- **Network**: The blockchain network to connect to
- **RPC URL**: Optional custom RPC endpoint

## Environment Variables

The BinkAI nodes support passing environment variables in two ways:

### 1. Using the Credentials UI

You can add environment variables directly in the credentials configuration:

- API Keys
- Network Settings
- RPC URLs
- Other configuration parameters

This method is useful for individual setups and testing. The values are stored securely as credentials in n8n.

### 2. Using Docker Environment Variables

For Docker deployments, you can pass environment variables directly by prefixing them with `BINKAI_`:

```yaml
version: '3'
services:
  n8n:
    image: n8nio/n8n
    environment:
      - BINKAI_API_KEY=your-api-key-here
      - BINKAI_NETWORK=mainnet
      - BINKAI_RPC_URL=your-rpc-url
    # other configuration...
```

## Operations

The BinkAI nodes support the following operations:

### Wallet Operations

- **Get Balance** - Get wallet balance
- **Transfer Tokens** - Send tokens to another address
- **Get Transaction History** - View past transactions

### DeFi Operations

- **Swap Tokens** - Exchange tokens on supported DEXes
- **Bridge Assets** - Transfer assets between chains
- **Stake Tokens** - Stake tokens in supported protocols

### Token Operations

- **Get Token Info** - Get token details and metadata
- **Get Token Balance** - Check token balance
- **Approve Token** - Approve token spending

## Using as a Tool

This node can be used as a tool in n8n AI Agents. To enable community nodes as tools, you need to set the `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE` environment variable to `true`.

### Setting the Environment Variable

**If you're using a bash/zsh shell:**

```bash
export N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
n8n start
```

**If you're using Docker:**
Add to your docker-compose.yml file:

```yaml
environment:
  - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

**If you're using the desktop app:**
Create a `.env` file in the n8n directory:

```
N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
```

## Examples

### Example: Token Swap Workflow

1. Add a BinkAI node to your workflow
2. Configure credentials with your API key
3. Select "Swap Tokens" operation
4. Set parameters:
   - Input Token: ETH
   - Output Token: USDC
   - Amount: 1
   - Slippage: 0.5%
5. Execute the workflow

### Example: Multi-Chain Bridge Workflow

1. Add a BinkAI node
2. Configure bridge credentials
3. Select "Bridge Assets" operation
4. Set parameters:
   - Source Chain: Ethereum
   - Destination Chain: BSC
   - Token: USDT
   - Amount: 100
5. Execute the workflow

## Compatibility

- Requires n8n version 1.0.0 or later
- Compatible with Node.js >= 18.10
- Supports multiple blockchain networks
- Works with major DeFi protocols

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [BinkAI Documentation](https://docs.binkai.com)
- [Blockchain API Reference](https://api.binkai.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Contributing

Contributions are welcome! Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
