# n8n-nodes-pirate-weather

This is an n8n community node that provides access to the [Pirate Weather API](https://pirateweather.net/), a free and open-source weather API that serves as an alternative to the Dark Sky API.

## Features

- **Weather Forecast**: Get current conditions and forecasts up to 7 days
- **Time Machine**: Access historical weather data
- **Multiple Units**: Support for US, UK, CA, and SI units
- **50+ Languages**: Weather summaries in multiple languages
- **Flexible Data**: Choose which data blocks to include or exclude
- **Extended Forecasts**: Get hourly forecasts up to 168 hours

## Installation

### Community Node (Recommended)

1. Go to **Settings > Community Nodes**
2. Search for `n8n-nodes-pirate-weather`
3. Click **Install**

### Manual Installation

1. Navigate to your n8n installation directory
2. Run:
   ```bash
   npm install n8n-nodes-pirate-weather
   ```
3. Restart n8n

## Authentication

This node requires a Pirate Weather API key:

1. Sign up for a free API key at [pirate-weather.apiable.io](https://pirate-weather.apiable.io/)
2. In n8n, create new Pirate Weather API credentials
3. Enter your API key

## Usage

### Weather Forecast

Get current weather conditions and forecasts:

- **Latitude & Longitude**: Location coordinates
- **Units**: Choose between auto, CA, UK, US, or SI
- **Exclude**: Remove unwanted data blocks (currently, minutely, hourly, daily, alerts)
- **Extend**: Get hourly forecasts for 168 hours instead of 48
- **Language**: Get summaries in your preferred language

### Time Machine

Query historical weather data:

- **Time**: Specify the date/time for historical data
- Supports UNIX timestamps and ISO 8601 formats
- Limited to available historical data

## Example Workflows

### Basic Weather Forecast
```
1. Pirate Weather node
2. Set coordinates (e.g., 37.8267, -122.4233)
3. Execute to get current weather
```

### Daily Weather Alert
```
1. Schedule Trigger (daily at 7 AM)
2. Pirate Weather node (get forecast)
3. IF node (check for rain)
4. Send notification if rain expected
```

## Development

To test this node locally during development:

1. **Clone and install dependencies**
   ```bash
   git clone https://github.com/ChadMoran/n8n-nodes-pirate-weather.git
   cd n8n-nodes-pirate-weather
   npm install
   ```

2. **Link the node locally**
   ```bash
   npm run link:local
   ```
   Then in your n8n installation directory:
   ```bash
   npm link n8n-nodes-pirate-weather
   ```

3. **Start development mode**
   ```bash
   npm run dev
   ```
   This will watch for code changes and run n8n.

4. **Remove the local link when done**
   ```bash
   npm run link:remove
   ```

### Available Scripts

- `npm run build` - Build the node for production
- `npm run dev` - Run TypeScript compiler and n8n in watch mode
- `npm run lint` - Check code style
- `npm run lintfix` - Fix code style issues
- `npm run link:local` - Create local npm link for testing
- `npm run link:remove` - Remove local npm link

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## Resources

- [Pirate Weather API Documentation](https://docs.pirateweather.net/en/latest/)
- [n8n Community Forum](https://community.n8n.io/)
- [Report Issues](https://github.com/ChadMoran/n8n-nodes-pirate-weather/issues)

## License

MIT