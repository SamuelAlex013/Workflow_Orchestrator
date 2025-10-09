# 🎮 Clash of Clans API Node for n8n

[![npm](https://img.shields.io/npm/v/n8n-nodes-clash-of-clans)](https://www.npmjs.com/package/n8n-nodes-clash-of-clans)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n](https://img.shields.io/badge/n8n-Community%20Node-brightgreen)](https://n8n.io/)

> **Comprehensive Clash of Clans API integration for n8n workflows**

This is an [n8n](https://n8n.io/) community node that provides comprehensive integration with the [Clash of Clans API](https://developer.clashofclans.com/#/documentation). Build powerful workflows to manage your Clash of Clans data, automate clan management, and create gaming analytics dashboards.

[<img src="https://cdn.jsdelivr.net/gh/n8n-io/n8n@a0f6c3a/assets/images/n8n-logo.png" alt="n8n" width="200"/>](https://n8n.io)

---

## 🚀 Quick Start

### Prerequisites
- [n8n](https://n8n.io/) installed and running
- Clash of Clans Developer Account
- API Token from [Clash of Clans Developer Portal](https://developer.clashofclans.com/#/account)

### Installation Methods

#### Method 1: Direct Installation (Recommended)
```bash
# Navigate to your n8n custom nodes directory
cd ~/.n8n/custom  # Linux/Mac
cd %USERPROFILE%\.n8n\custom  # Windows

# Install the node
npm install n8n-nodes-clash-of-clans

# Restart n8n
n8n start
```

#### Method 2: Manual Installation
```bash
# Clone the repository
git clone https://github.com/iamtahiralvi/n8n-nodes-clash-of-clans.git

# Navigate to the project
cd n8n-nodes-clash-of-clans

# Install dependencies
npm install

# Build the project
npm run build

# Link to n8n
npm link

# Navigate to n8n custom directory
cd ~/.n8n/custom  # Linux/Mac
cd %USERPROFILE%\.n8n\custom  # Windows

# Link the node
npm link n8n-nodes-clash-of-clans

# Restart n8n
n8n start
```

#### Method 3: Docker Installation
```bash
# Add to your docker-compose.yml
volumes:
  - ~/.n8n/custom:/home/node/.n8n/custom

# Then use Method 1 or 2 inside the container
```

---

## 🔑 Setup Credentials

1. **Get API Token**
   - Visit [Clash of Clans Developer Portal](https://developer.clashofclans.com/#/account)
   - Create a new application
   - Copy your API token

2. **Add Credentials in n8n**
   - Open n8n workflow editor
   - Go to **Credentials** → **Add Credential**
   - Select **Clash of Clans API**
   - Enter your API token
   - Save the credential

---

## 🎯 Available Operations

### 👤 Player Operations
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Get Player** | Retrieve player profile information | Player Tag |
| **Verify Player Token** | Verify a player's one-time API token | Player Tag, Verification Token |
| **Get Player Achievement Progress** | Get detailed achievement progress | Player Tag |
| **Get Player Battle Log** | Access player's recent battle history | Player Tag |
| **Get Player Upcoming Chests** | View upcoming chest rewards | Player Tag |
| **Get Player Rankings** | Get player rankings by location | Player Tag, Location ID |

### 🏰 Clan Operations
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Get Clan** | Retrieve detailed clan information | Clan Tag |
| **Get Clan Members** | Get list of clan members | Clan Tag, Pagination |
| **Get Clan War Log** | Access the complete war history | Clan Tag |
| **Get Current War** | Get current war information | Clan Tag |
| **Get Clan Capital Raid Log** | Access clan capital raid history | Clan Tag, Pagination |
| **Get Clan Capital Info** | Get detailed clan capital information | Clan Tag |
| **Get Clan Labels** | Retrieve available clan labels | None |
| **Get Clan Rankings** | Get clan rankings by location | Clan Tag, Location ID |

### ⚔️ War Operations
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Get War Leagues** | Retrieve list of available war leagues | Pagination |
| **Get CWL Group** | Get Clan War League group information | CWL Group ID |
| **Get CWL War** | Get specific CWL war details | CWL Group ID, CWL War ID |

### 🔍 Search & Discovery
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Search Clans** | Search for clans with advanced filters | Search Parameters, Pagination |
| **Get Locations** | Get list of available locations | Pagination |
| **Get Location Info** | Get specific location information | Location ID |
| **Get Location Rankings** | Get rankings for a specific location | Location ID, Ranking Type, Pagination |

### 🏆 League Operations
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Get Leagues** | Get list of all available leagues | None |
| **Get League Info** | Get specific league information | League ID |
| **Get League Seasons** | Access league season information | League ID, Pagination |
| **Get League Season Rankings** | Get rankings for specific seasons | League ID, Season ID, Pagination |

### 🎁 Additional Features
| Operation | Description | Parameters |
|-----------|-------------|------------|
| **Get Gold Pass Season** | Get current gold pass season | None |
| **Get Player Labels** | Retrieve available player labels | None |
| **Get Capital Districts** | Get list of capital districts | None |
| **Get Capital District Info** | Get specific district information | Capital District ID |

---

## 📊 Advanced Features

### 🔍 Enhanced Search & Filtering
- **Multi-parameter clan search** with location, member count, and level filters
- **Capital hall level filtering** for clan searches
- **Comprehensive pagination** support for all list operations
- **Location-based rankings** for players and clans

### 📈 Improved Data Processing
- **Enhanced metadata** with operation type categorization
- **Better error handling** with detailed error context
- **Structured response format** with timestamps and operation details
- **Operation type classification** (player, clan, war, discovery, league, general)

### 🌐 Extended API Coverage
- **Complete player operations** including achievements, battle logs, and chests
- **Comprehensive clan management** with capital and ranking features
- **Full war system support** including CWL operations
- **Location and ranking systems** for competitive play
- **Capital district operations** for clan capital features

---

## 💡 Usage Examples

### Basic Player Lookup
```json
{
  "operation": "getPlayer",
  "playerTag": "#ABC123"
}
```

### Advanced Clan Search
```json
{
  "operation": "searchClans",
  "searchParams": {
    "parameters": {
      "name": "Elite Warriors",
      "minMembers": 20,
      "maxMembers": 50,
      "minClanLevel": 10,
      "warFrequency": "always"
    }
  }
}
```

### Player Rankings by Location
```json
{
  "operation": "getPlayerRankings",
  "playerTag": "#ABC123",
  "locationId": "32000006"
}
```

### League Season Rankings
```json
{
  "operation": "getLeagueSeasonRankings",
  "leagueId": "29000022",
  "seasonId": "2024-01"
}
```

---

## 📋 Response Format

All operations return data in the following enhanced format:

```json
{
  "operation": "getPlayer",
  "url": "https://api.clashofclans.com/v1/players/%23ABC123",
  "data": {
    // Raw API response data
  },
  "timestamp": "2024-01-01T00:00:00.000Z",
  "metadata": {
    "operationType": "player",
    "apiVersion": "v1",
    "processedAt": "2024-01-01T00:00:00.000Z"
  }
}
```

---

## ⚠️ API Rate Limits

The Clash of Clans API has rate limits:
- **IP-based**: 100 requests per IP per minute
- **Token-based**: 1000 requests per token per day

The node handles rate limiting gracefully and will return appropriate error messages when limits are exceeded.

---

## 🛠️ Development

### Prerequisites
- Node.js >= 20.15
- npm or yarn

### Setup
```bash
# Clone the repository
git clone https://github.com/iamtahiralvi/n8n-nodes-clash-of-clans.git

# Install dependencies
npm install

# Build the project
npm run build

# Run linting
npm run lint

# Auto-fix linting issues
npm run lintfix
```

### Testing
Test your node locally by following the [n8n community nodes testing guide](https://docs.n8n.io/integrations/community-nodes/testing/).

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

### Getting Help
1. 📚 Check the [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
2. 💬 Visit the [n8n community forum](https://community.n8n.io/)
3. 🐛 Open an issue on this repository
4. 📧 Contact the author directly

### Common Issues
- **"Couldn't connect" errors**: Check your API token and internet connection
- **Rate limiting**: Wait for the rate limit to reset or use multiple tokens
- **Invalid tags**: Ensure player/clan tags start with `#` and are properly formatted

---

## 📝 Changelog

### [2.0.0] - 2025-01-27 - Major Feature Expansion
- **New Player Operations**: Achievement progress, battle logs, upcoming chests, rankings
- **Enhanced Clan Operations**: Member lists, capital raid logs, capital info, rankings
- **War System Expansion**: CWL group and war operations
- **Advanced Discovery**: Location info, location rankings, multiple ranking types
- **League System**: Complete league operations with season rankings
- **Capital Features**: Capital districts and district information
- **Gold Pass**: Current season information
- **Labels System**: Player and clan labels
- **Improved Search**: Capital hall level filtering, enhanced pagination
- **Better Metadata**: Operation type classification, enhanced response structure
- **Enhanced Error Handling**: Better context and error information

### [1.0.0] - 2024-01-01 - Initial Release
- Support for basic Clash of Clans API endpoints
- Player and clan operations
- Basic search and discovery features
- Error handling and pagination support

---

## 👨‍💻 Author

<div align="center">

### **Tahir Alvi**
**Full-Stack Developer & n8n Community Contributor**

[![Portfolio](https://img.shields.io/badge/Portfolio-Website-blue?style=for-the-badge&logo=globe)](https://tahiralvi.com)
[![Email](https://img.shields.io/badge/Email-hi@tahiralvi.com-red?style=for-the-badge&logo=gmail)](mailto:hi@tahiralvi.com)
[![GitHub](https://img.shields.io/badge/GitHub-tahiralvi-black?style=for-the-badge&logo=github)](https://github.com/iamtahiralvi)

**Specializing in:**
- 📱 FlutterFlow App Development
- 🔧 n8n Node Development
</div>

---

## 🙏 Acknowledgments

- [n8n](https://n8n.io/) for the amazing workflow automation platform
- [Supercell](https://supercell.com/) for the Clash of Clans game and API
- The n8n community for support and guidance
- All contributors and users of this node

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**Made with ❤️ by [Tahir Alvi](https://tahiralvi.com)**

</div>
