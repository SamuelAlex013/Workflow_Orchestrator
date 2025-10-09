# Amazon PA-API Enhanced Node for n8n

An enhanced n8n community node for Amazon Product Advertising API (PA-API 5.0) with full Resources support, better security, and comprehensive product data retrieval.

[![npm version](https://badge.fury.io/js/n8n-nodes-amazon-paapi-enhanced.svg)](https://badge.fury.io/js/n8n-nodes-amazon-paapi-enhanced)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

### ✅ Complete PA-API 5.0 Resources Support
Unlike the original `n8n-nodes-amazon-paapi` node, our enhanced version supports **ALL** PA-API 5.0 Resources with proper specifications:

- **ItemInfo.Title** - Product title
- **ItemInfo.Features** - Product features and bullet points  
- **ItemInfo.ContentInfo** - Content information (pages, languages, etc.)
- **ItemInfo.TechnicalInfo** - Technical specifications (brand, model, etc.)
- **ItemInfo.ProductInfo** - Product information (color, size, etc.)
- **Images.Primary.Small/Medium/Large** - Primary product images in all sizes
- **Images.Variants** - Additional product images
- **Offers.Listings.Price** - Price and availability information
- **Offers.Listings.Availability.Message** - Stock status
- **Offers.Listings.Condition** - Item condition (New, Used, etc.)
- **Offers.Summaries.HighestPrice** - Price summaries
- **ParentASIN** - Parent ASIN for product variations
- **BrowseNodeInfo.BrowseNodes** - Category information
- **CustomerReviews.Count** - Customer review count
- **CustomerReviews.StarRating** - Customer review ratings

### 🔒 Enhanced Security
- Secure credential storage with password masking
- Input validation and sanitization
- Better error handling with detailed debugging
- No hardcoded credentials in source code

### 🌍 Extended Marketplace Support
- **Complete marketplace coverage** including Netherlands (amazon.nl)
- Support for all major Amazon marketplaces worldwide
- Proper locale and currency handling

### 🎯 Advanced Features
- **Structured output processing** - Clean, organized product data
- **Batch processing** - Retrieve multiple ASINs simultaneously (up to 10)
- **Flexible configuration** - Choose exactly which data you need
- **Advanced filtering** - Condition, merchant, currency, language preferences
- **Comprehensive error handling** - Detailed error messages for debugging

## 🆚 Comparison with Original Node

| Feature | Original Node | Enhanced Node |
|---------|---------------|---------------|
| Resources Support | ❌ Limited (title only) | ✅ Complete (all PA-API resources) |
| Price Information | ❌ Missing | ✅ Full (Offers.Listings + Summaries) |
| Product Images | ❌ Missing | ✅ Complete (Primary + Variants, all sizes) |
| Netherlands Marketplace | ❌ Missing | ✅ Supported (amazon.nl) |
| Structured Output | ❌ Raw API response | ✅ Clean, organized data |
| Error Handling | ❌ Basic | ✅ Comprehensive with validation |
| Security | ❌ Basic | ✅ Password masking + validation |
| Resource Specification | ❌ Incorrect format | ✅ Proper PA-API 5.0 format |

## 🔒 Security

### ⚠️ **IMPORTANT: Credential Security**

**NEVER** commit your real Amazon PA-API credentials to Git!

- Always use placeholder values in examples
- Rotate your credentials regularly  
- Use environment variables for production
- Monitor your API usage in Amazon Partner Central

### 🔐 **Secure Credential Management**

```bash
# Example .env file (DO NOT commit!)
AMAZON_ACCESS_KEY=your-access-key-here
AMAZON_SECRET_KEY=your-secret-key-here  
AMAZON_PARTNER_TAG=your-partner-tag-here
```

## 📦 Installation

### Via n8n Community Nodes
1. Go to **Settings** > **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter: `n8n-nodes-amazon-paapi-enhanced`
4. Click **Install**

### Manual Installation
```bash
# For n8n running locally
npm install n8n-nodes-amazon-paapi-enhanced

# For Docker installations
docker exec n8n npm install n8n-nodes-amazon-paapi-enhanced
docker restart n8n
```

### Development Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/n8n-nodes-amazon-paapi-enhanced.git
cd n8n-nodes-amazon-paapi-enhanced

# Install dependencies
npm install

# Build the node
npm run build

# Install in your n8n environment
npm install /path/to/n8n-amazon-paapi-enhanced
```

## 🔧 Configuration

### 1. Create Credentials
Create new credentials in n8n:
- **Type**: Amazon PA-API Enhanced
- **Access Key ID**: Your Amazon PA-API Access Key
- **Secret Access Key**: Your Amazon PA-API Secret Key  
- **Partner Tag**: Your Amazon Associate ID
- **Marketplace**: Choose your marketplace (e.g., www.amazon.nl)

### 2. Node Configuration
1. Add the "Amazon PA-API Enhanced" node to your workflow
2. Select your credentials
3. Choose the desired operation:
   - **Get Items**: Retrieve product info by ASIN(s)
   - **Search Items**: Search products with keywords
   - **Get Browse Nodes**: Retrieve category information

### 3. Select Resources
Choose which product information to retrieve:
- For **prices**: Select "Offers - Listings Price" and "Offers - Summaries"
- For **images**: Select "Images - Primary Medium/Large" and "Images - Variants"
- For **product details**: Select "Item Info - Features" and "Item Info - Technical Info"

## 📊 Output Structure

The node returns structured, clean data:

```json
{
  "operation": "getItems",
  "itemCount": 1,
  "items": [
    {
      "asin": "B08N5WRWNW",
      "title": "Product Title",
      "features": ["Feature 1", "Feature 2"],
      "primaryImage": {
        "small": "https://...",
        "medium": "https://...",
        "large": "https://..."
      },
      "offers": [
        {
          "price": "€29.99",
          "currency": "EUR",
          "availability": "In Stock",
          "condition": "New",
          "merchant": "Amazon.nl",
          "isPrime": true
        }
      ],
      "priceSummary": [
        {
          "condition": "New",
          "lowestPrice": "€29.99",
          "highestPrice": "€39.99",
          "offerCount": 5
        }
      ]
    }
  ]
}
```

## 🔍 Usage Examples

### Example 1: Get Product Details
```
Operation: Get Items
Item IDs: B08N5WRWNW
Resources: 
- ItemInfo.Title
- ItemInfo.Features  
- Images.Primary.Medium
- Offers.Listings.Price
```

### Example 2: Search Products
```
Operation: Search Items
Keywords: wireless headphones
Search Index: Electronics
Item Count: 10
Resources:
- ItemInfo.Title
- Images.Primary.Medium
- Offers.Summaries.HighestPrice
```

### Example 3: Batch Processing
```
Operation: Get Items
Item IDs: B08N5WRWNW,B07XJ8C8F5,B09KMVNY87
Resources:
- ItemInfo.Title
- Offers.Listings.Price
- Images.Primary.Large
```

## 🛠️ Development

### Project Structure
```
n8n-amazon-paapi-enhanced/
├── credentials/
│   └── AmazonPaApiEnhanced.credentials.ts
├── nodes/
│   └── AmazonPAEnhanced/
│       ├── AmazonPAEnhanced.node.ts
│       └── amazon.svg
├── dist/                 # Compiled output
├── package.json
├── tsconfig.json
└── README.md
```

### Build Commands
```bash
npm run build          # Compile TypeScript + copy icons
npm run dev            # Watch mode for development
npm run lint           # ESLint checking
npm run format         # Prettier formatting
```

### Testing
```bash
# Run tests
npm test

# Test specific functionality
npm run test:api
```

## 🚨 Troubleshooting

### Common Issues

**"Bad Request" Error**
- Ensure you're using the correct Resource specifications (e.g., `Images.Primary.Medium` not `Images.Primary`)
- Verify your credentials are valid and have PA-API access
- Check that your Partner Tag is active and approved

**Missing Product Data**
- Select appropriate Resources for the data you need
- Some products may not have all data available (e.g., prices, reviews)
- Verify the ASIN exists in your selected marketplace

**Rate Limiting**
- Amazon PA-API has rate limits (1 request per second for new associates)
- Implement proper delays between requests
- Use batch processing to retrieve multiple items efficiently

## 📋 Requirements

- n8n version 0.190.0 or higher
- Valid Amazon PA-API credentials
- Active Amazon Associates account
- Node.js 16+ (for development)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow TypeScript best practices
- Add tests for new functionality
- Update documentation for new features
- Ensure security best practices
- Test with multiple marketplaces

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/n8n-nodes-amazon-paapi-enhanced/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/n8n-nodes-amazon-paapi-enhanced/discussions)
- **n8n Community**: [n8n Community Forum](https://community.n8n.io/)

## 🙏 Acknowledgments

- Built on top of the [amazon-paapi](https://www.npmjs.com/package/amazon-paapi) library
- Inspired by the original n8n-nodes-amazon-paapi community node
- Thanks to the n8n community for feedback and testing

## 🔗 Related Links

- [Amazon PA-API 5.0 Documentation](https://webservices.amazon.com/paapi5/documentation/)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [Amazon Associates Program](https://affiliate-program.amazon.com/)

---

**Made with ❤️ for the n8n community**
