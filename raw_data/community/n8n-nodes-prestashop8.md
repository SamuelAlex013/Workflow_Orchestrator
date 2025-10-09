# n8n PrestaShop 8 Node

[![npm version](https://badge.fury.io/js/n8n-nodes-prestashop8.svg)](https://www.npmjs.com/package/n8n-nodes-prestashop8)
[![Downloads](https://img.shields.io/npm/dt/n8n-nodes-prestashop8.svg)](https://www.npmjs.com/package/n8n-nodes-prestashop8)
[![GitHub license](https://img.shields.io/github/license/PPCM/n8n-nodes-prestashop8)](https://github.com/PPCM/n8n-nodes-prestashop8/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/PPCM/n8n-nodes-prestashop8)](https://github.com/PPCM/n8n-nodes-prestashop8/issues)
[![GitHub stars](https://img.shields.io/github/stars/PPCM/n8n-nodes-prestashop8)](https://github.com/PPCM/n8n-nodes-prestashop8/stargazers)

A comprehensive n8n community node for PrestaShop 8 integration with automatic XML/JSON conversion and full CRUD support.

**🌍 Documentation Languages:**
- 🇬🇧 **English** (this file) - [Examples](./docs/EXAMPLES_EN.md) | [Installation](./docs/INSTALLATION_EN.md)
- 🇫🇷 [**Français**](./docs/README_FR.md) - [Exemples](./EXAMPLES.md) | [Installation](./INSTALLATION.md)
- 🇩🇪 [**Deutsch**](./docs/README_DE.md) - [Beispiele](./docs/EXAMPLES_DE.md) | [Installation](./docs/INSTALLATION_DE.md)
- 🇪🇸 [**Español**](./docs/README_ES.md) - [Ejemplos](./docs/EXAMPLES_ES.md) | [Instalación](./docs/INSTALLATION_ES.md)

**📚 [Complete Documentation Hub](./docs/README.md)**

[🚀 Quick Start](#quick-start) | [✨ Features](#features) | [📚 Documentation](#documentation) | [🎯 Examples](#examples) | [🤝 Contributing](#contributing)

---

## 🎯 Overview

**The first n8n node** that truly simplifies PrestaShop 8 integration:

- ✅ **Full CRUD operations** without writing a single line of XML
- ✅ **Intuitive graphical interface** with dynamic dropdown menus
- ✅ **Automatic XML/JSON conversion** - PrestaShop XML ↔ Simple JSON
- ✅ **25+ resources supported**: products, customers, orders, stocks...
- ✅ **Advanced filtering** with 10 search operators
- ✅ **Raw mode** for debugging and advanced use cases

## 🚀 Quick Start

### Installation
```bash
npm install n8n-nodes-prestashop8
```

### PrestaShop Configuration
1. **Enable Webservice**: Settings > Web Service > Enable
2. **Create API Key** with CRUD permissions  
3. **Note the URL**: `https://your-store.com/api`

### n8n Configuration
```javascript
// PrestaShop 8 API Credentials
{
  "baseUrl": "https://your-store.com/api",
  "apiKey": "YOUR_API_KEY"
}
```

### First Workflow
```javascript
// List active products
{
  "resource": "products",
  "operation": "search",
  "filters": {
    "filter": [
      { "field": "active", "operator": "=", "value": "1" }
    ]
  }
}
```

## ✨ Features

### 🔄 Complete CRUD Operations
| Operation | Description | Example |
|-----------|-------------|---------|
| **List** | Retrieve collections | All products |
| **Get by ID** | Individual retrieval | Product ID 123 |
| **Search** | Search with filters | Products > €20 |
| **Create** | Create new entities | New customer |
| **Update** | Modify existing | Update stock |
| **Delete** | Remove entities | Delete order |

### 📊 Supported Resources

<details>
<summary><strong>👥 CRM & Customers (6 resources)</strong></summary>

- `customers` - Store customers
- `addresses` - Shipping/billing addresses
- `groups` - Customer groups and pricing
- `customer_threads` - Customer service conversations
- `customer_messages` - Individual messages
- `guests` - Non-registered visitors
</details>

<details>
<summary><strong>📦 Product Catalog (9 resources)</strong></summary>

- `products` - Product catalog
- `combinations` - Product variations (size, color...)
- `stock_availables` - Stock management
- `categories` - Category tree
- `manufacturers` - Brands and manufacturers
- `suppliers` - Suppliers
- `tags` - Product tags
- `product_features` - Product characteristics
- `product_options` - Customization options
</details>

<details>
<summary><strong>🛒 Orders & Sales (8 resources)</strong></summary>

- `orders` - Store orders
- `order_details` - Order line items
- `order_histories` - Status change history
- `order_states` - Possible order states
- `order_carriers` - Carriers by order
- `order_invoices` - Invoices
- `carts` - Shopping carts
- `cart_rules` - Discount codes and promotions
</details>

### 🔍 Advanced Filtering

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal | `price = 19.99` |
| `!=` | Not equal | `active != 0` |
| `>` / `>=` | Greater than | `stock > 10` |
| `<` / `<=` | Less than | `price <= 50` |
| `LIKE` | Contains | `name LIKE %iPhone%` |
| `NOT LIKE` | Does not contain | `ref NOT LIKE %OLD%` |
| `BEGINS` | Starts with | `name BEGINS Apple` |
| `ENDS` | Ends with | `ref ENDS -2024` |

### 🎛️ Advanced Options

- **Pagination**: `limit=20` or `limit=10,30`
- **Sorting**: `[price_ASC]`, `[date_add_DESC]`
- **Fields**: `full`, `minimal`, or custom
- **Debug**: URL, headers, timeout

## 🎯 Usage Examples

### E-commerce Automation
```javascript
// Daily ERP → PrestaShop stock sync
Cron → ERP API → Transform → PrestaShop 8 Node → Slack Alert
```

### Marketing Automation
```javascript
// New customers → CRM + welcome email
PrestaShop Webhook → PrestaShop 8 Node → CRM → Mailchimp
```

### Business Intelligence
```javascript
// Daily sales report
Cron → PrestaShop 8 Node → Calculate KPIs → Email Report
```

## 📚 Documentation

- **[🎯 Practical Examples](./docs/EXAMPLES_EN.md)** - Detailed use cases
- **[🛠️ Installation Guide](./docs/INSTALLATION_EN.md)** - Step-by-step setup
- **[📝 Changelog](./CHANGELOG.md)** - Updates and fixes
- **[📋 Project Summaries](./summary/README.md)** - Executive summaries and presentations

## 🐛 Issues & Support

### Common Problems
- **401 Unauthorized** → Check API key and permissions
- **404 Not Found** → Verify base URL and Webservices enabled
- **Timeout** → Increase timeout in debug options

### Get Help
- 🐞 **[GitHub Issues](https://github.com/PPCM/n8n-nodes-prestashop8/issues)** - Bugs and questions
- 🌐 **[n8n Community](https://community.n8n.io)** - Forum discussions
- 📖 **[Documentation](./docs/INSTALLATION_EN.md)** - Detailed guides

## 🤝 Contributing

Contributions are welcome! Here's how to participate:

### Quick Start Development
```bash
git clone https://github.com/PPCM/n8n-nodes-prestashop8.git
cd n8n-nodes-prestashop8
npm install
npm run dev  # Watch mode
```

### Contribution Process
1. **Fork** the project
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Types of Contributions
- 🐞 **Bug fixes**
- ✨ **New features**
- 📚 **Documentation improvements**
- 🧪 **Additional tests**
- 🎨 **UI/UX improvements**

### Guidelines
- TypeScript code with strict typing
- Unit tests for new features
- Updated documentation
- Respect ESLint + Prettier

## 📊 Roadmap

### v1.1 (Q1 2024)
- [ ] Intelligent caching to optimize API calls
- [ ] Pre-configured workflow templates
- [ ] Bulk operations for batch processing
- [ ] Integrated PrestaShop webhooks

### v1.2 (Q2 2024)
- [ ] PrestaShop Cloud support
- [ ] Advanced multi-store
- [ ] Visual field mapping
- [ ] Performance metrics

### v2.0 (Q3 2024)
- [ ] GraphQL support (if available in PrestaShop)
- [ ] AI-powered data transformation
- [ ] Real-time synchronization
- [ ] Advanced analytics dashboard

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- **n8n Team** for the fantastic automation tool
- **PrestaShop Community** for API documentation
- **Contributors** who improve this project

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=PPCM/n8n-nodes-prestashop8&type=Date)](https://star-history.com/#PPCM/n8n-nodes-prestashop8&Date)

---

**Revolutionize your e-commerce with n8n and PrestaShop 8** 🚀

[⬆ Back to top](#n8n-prestashop-8-node)
