# n8n-nodes-biteship

![Biteship Custom Node Banner](https://biteship.com/assets/images/logo.png)

Custom node n8n untuk integrasi dengan [Biteship API](https://biteship.com/id/docs/api), platform pengiriman Indonesia.

## Fitur

- **Courier Management**: Dapatkan daftar kurir yang tersedia
- **Rate Checking**: Cek tarif pengiriman untuk berbagai kurir
- **Order Management**: Buat dan kelola pesanan pengiriman
- **Tracking**: Lacak status pengiriman real-time

## Instalasi

### Prasyarat

- Node.js (v16 atau lebih tinggi)
- npm atau yarn
- n8n (v0.190.0 atau lebih tinggi)

### Install via npm

```bash
npm install n8n-nodes-biteship
```

### Install dari source

```bash
git clone https://github.com/biteship/n8n-nodes-biteship.git
cd n8n-nodes-biteship
npm install
npm run build
```

## Konfigurasi

1. **API Key**: Dapatkan API key dari [Biteship Dashboard](https://biteship.com/dashboard)
2. **Environment**: Pilih antara Production atau Sandbox
3. **Credentials**: Tambahkan credentials di n8n dengan informasi:
   - API Key dari Biteship
   - Environment (production/sandbox)

## Penggunaan

### 1. Courier Operations

#### Get All Couriers
Dapatkan daftar semua kurir yang tersedia di Biteship.

**Output:**
```json
{
  "courier_code": "jne",
  "courier_name": "JNE",
  "courier_service_name": "REG",
  "description": "Layanan Reguler",
  "service_type": "standard",
  "shipping_type": "parcel",
  "shipment_duration_range": "1-2",
  "shipment_duration_unit": "days"
}
```

### 2. Rate Operations

#### Check Rates
Cek tarif pengiriman untuk berbagai kurir.

**Input Parameters:**
- Origin Postal Code (required)
- Destination Postal Code (required)
- Couriers (multiselect)
- Items (collection)

**Output:**
```json
{
  "courier_code": "jne",
  "courier_service_code": "REG",
  "courier_service_name": "Layanan Reguler",
  "price": 15000,
  "type": "parcel"
}
```

### 3. Tracking Operations

#### Track Shipment
Lacak status pengiriman menggunakan waybill ID.

**Input Parameters:**
- Waybill ID (required)
- Courier Code (required)

**Output:**
```json
{
  "status": "delivered",
  "waybill_id": "12345678901234567890",
  "courier": {
    "code": "jne",
    "name": "JNE"
  },
  "history": [
    {
      "note": "Paket telah diterima",
      "updated_at": "2023-12-01T10:00:00Z",
      "status": "delivered"
    }
  ]
}
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/biteship/n8n-nodes-biteship.git
cd n8n-nodes-biteship

# Install dependencies
npm install

# Build project
npm run build

# Run in development mode
npm run dev
```

### Project Structure

```
├── credentials/
│   └── BiteshipApi.credentials.ts    # API credentials
├── nodes/
│   └── Biteship/
│       ├── Biteship.node.ts         # Main node implementation
│       └── biteship.svg             # Node icon
├── package.json                     # Package configuration
├── tsconfig.json                   # TypeScript configuration
└── README.md                       # Documentation
```

### Build Commands

```bash
npm run build      # Build TypeScript and copy assets
npm run dev        # Watch mode for development
npm run lint       # Run ESLint
npm run format     # Format code with Prettier
```

## Testing

### Manual Testing

1. Import node ke n8n instance
2. Buat workflow baru
3. Tambahkan node Biteship
4. Konfigurasi credentials
5. Test berbagai operasi

### Unit Testing

```bash
npm test
```

## Troubleshooting

### Common Issues

1. **Authentication Error**
   - Pastikan API key valid
   - Cek environment setting (production vs sandbox)

2. **Rate Limit**
   - Biteship API memiliki rate limit
   - Tambahkan delay antar request jika diperlukan

3. **Invalid Postal Code**
   - Pastikan format kode pos benar (5 digit)
   - Cek ketersediaan layanan di area tersebut

## Contributing

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## License

MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## Support

- Email: support@biteship.com
- Documentation: https://biteship.com/id/docs/intro
- GitHub Issues: https://github.com/biteship/n8n-nodes-biteship/issues

## Changelog

### v1.0.0
- Initial release
- Support untuk courier, rate, order, dan tracking operations
- Dokumentasi lengkap
- Error handling yang robust
