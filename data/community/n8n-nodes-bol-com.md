# n8n-nodes-bol-com

![Bol.com](https://img.shields.io/badge/Bol.com-Partner%20API-blue)
![n8n](https://img.shields.io/badge/n8n-Community%20Node-FF6D5A)
![License](https://img.shields.io/badge/license-MIT-green)

Een n8n community node voor integratie met de Bol.com Partner API, speciaal ontworpen voor affiliate marketing en productgegevens.

## Functies

- **Product Details**: Haal gedetailleerde productinformatie op via EAN of product ID
- **Product Zoeken**: Zoek naar producten met keywords en filters
- **Affiliate Marketing**: Volledig compatibel met Bol.com Partner programma
- **Nederlandse Marktplaats**: Geoptimaliseerd voor de Nederlandse e-commerce markt

## Installatie

### Via n8n Community Nodes

1. Ga naar **Settings** > **Community Nodes** in je n8n installatie
2. Klik op **Install a community node**
3. Voer `n8n-nodes-bol-com` in
4. Klik op **Install**

### Handmatige Installatie

```bash
# In je n8n installatie directory
npm install n8n-nodes-bol-com
```

## Configuratie

### Bol.com Partner API Credentials

Om deze node te gebruiken heb je Bol.com Partner API credentials nodig:

1. Registreer je bij het [Bol.com Partner Programma](https://partnerplatform.bol.com/)
2. Verkrijg je Client ID en Client Secret
3. Configureer de credentials in n8n:
   - **Client ID**: Je Bol.com Partner API Client ID
   - **Client Secret**: Je Bol.com Partner API Client Secret
   - **Environment**: Kies tussen Test en Production

## Gebruik

### Product Details Ophalen

```javascript
// Voorbeeld: Product details ophalen
{
  "resource": "product",
  "operation": "getProduct",
  "productId": "9200000123456789" // EAN of product ID
}
```

### Producten Zoeken

```javascript
// Voorbeeld: Zoeken naar producten
{
  "resource": "search",
  "operation": "searchProducts",
  "searchQuery": "laptop",
  "additionalFields": {
    "limit": 20,
    "offset": 0
  }
}
```

## Ondersteunde Operaties

### Product Resource
- **Get Product Details**: Haal gedetailleerde informatie op over een specifiek product
- **Get Product List**: Haal een lijst van producten op met filters

### Search Resource
- **Search Products**: Zoek naar producten met keywords

## API Endpoints

Deze node gebruikt de volgende Bol.com Partner API endpoints:

- `GET /catalog/v4/products/{productId}` - Product details
- `GET /catalog/v4/search` - Product zoeken
- `POST /login/token` - Authenticatie

## Foutafhandeling

De node bevat uitgebreide foutafhandeling voor:
- Authenticatie fouten
- API rate limiting
- Netwerk problemen
- Ongeldige parameters

## Ontwikkeling

### Lokaal Ontwikkelen

```bash
# Clone de repository
git clone https://github.com/yourusername/n8n-nodes-bol-com.git
cd n8n-nodes-bol-com

# Installeer dependencies
npm install

# Build de node
npm run build

# Link voor lokale ontwikkeling
npm link
```

### Project Structuur

```
n8n-nodes-bol-com/
├── credentials/
│   └── BolComApi.credentials.ts
├── nodes/
│   └── BolCom/
│       ├── BolCom.node.ts
│       └── bol-com.svg
├── dist/                 # Compiled output
├── package.json
├── tsconfig.json
└── README.md
```

## Bijdragen

Bijdragen zijn welkom! Zie [CONTRIBUTING.md](CONTRIBUTING.md) voor richtlijnen.

## Licentie

Dit project is gelicenseerd onder de MIT License - zie het [LICENSE](LICENSE) bestand voor details.

## Support

- 📧 Email: oscar@lijstjedelen.nl
- 🐛 Issues: [GitHub Issues](https://github.com/OscarWeijman/n8n-nodes-bol-com/issues)
- 📖 Documentatie: [Bol.com Partner API Docs](https://developers.bol.com/)

## Disclaimer

Deze node is niet officieel geassocieerd met Bol.com. Het is een community-ontwikkelde integratie voor de Bol.com Partner API.
