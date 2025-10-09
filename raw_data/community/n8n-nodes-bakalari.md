# n8n-nodes-bakalari

n8n community node for integrating with Bakalari school system API v3.

## Features

- **Messages (Komens)**: Get noticeboard, received, and sent messages
- **Secure authentication** with username/password
- **Docker-ready** deployment

## Quick Start

### Docker (Recommended)
```bash
git clone https://github.com/czmathew/n8n-nodes-bakalari.git
cd n8n-nodes-bakalari
cp .env.example .env  # Edit with your values
docker-compose up -d
```

Access n8n at `http://localhost:5678` (admin/password)

### Manual Installation
```bash
npm install && npm run build
npm link
cd ~/.n8n/custom && npm link n8n-nodes-bakalari
```

## Usage

1. **Add Credentials**: Settings → Credentials → Bakalari API
   - School URL: `https://yourschool.bakalari.cz`
   - Username & Password
2. **Add Node**: Select Bakalari → Messages → Choose operation

## API Endpoints

- `POST /api/3/komens/messages/noticeboard` - Noticeboard messages
- `POST /api/3/komens/messages/received` - Received messages
- `POST /api/3/komens/messages/sent` - Sent messages

## Development

```bash
npm install
npm run build    # Compile TypeScript
npm run lint     # Check code style
npm run dev      # Test with n8n
```

## Troubleshooting

- **Authentication Failed**: Check school URL format includes `https://`
- **Node Missing**: Restart n8n after installation
- **Debug**: Set `N8N_LOG_LEVEL=debug` in environment

## Roadmap

**v0.2.0**: Token caching, mark as read, attachments
**v1.0.0**: Full API coverage (timetable, grades, absence, homework)

## Contributing

1. Fork and create feature branch
2. Make changes and run `npm run lint`
3. Submit pull request

## Links

- [Bakalari API v3 Docs](https://github.com/bakalari-api/bakalari-api-v3)
- [n8n Documentation](https://docs.n8n.io)
- [Issues](https://github.com/czmathew/n8n-nodes-bakalari/issues)

MIT License