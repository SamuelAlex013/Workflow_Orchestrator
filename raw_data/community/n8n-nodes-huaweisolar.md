# n8n-nodes-huaweisolar

N8N community nodes for reading data from Huawei SmartLogger 3000 and SUN2000 inverters via Modbus TCP protocol.

## Features

- 🔌 **Direct Modbus TCP communication** with Huawei SmartLogger 3000
- ⚡ **Fast parallel device discovery** with configurable timeouts
- 📊 **Comprehensive data reading** including power, environmental, system, and alarm data
- 🔧 **Critical Huawei-specific fixes** applied (little-endian byte order, correct unit IDs)
- 🚀 **Optimized performance** with connection management and retry logic

## Installation

Install this node in your N8N instance:

```bash
npm install n8n-nodes-huaweisolar
```

Or if using the N8N desktop app, install through the Community Nodes section.

## Available Nodes

### SmartLogger

Reads data from Huawei SmartLogger 3000 devices.

#### Operations

1. **Read Data** - Read selected data categories (system, power, environmental, alarms)
2. **Discover Devices** - Scan for all connected devices on the Modbus network

### SUN2000 Inverter

Reads data from individual Huawei SUN2000 inverters.

#### Operations

1. **Read Inverter Data** - Read data from manually specified inverter addresses
2. **Read From Discovery** - Read data from inverters discovered by SmartLogger node

#### SmartLogger Configuration

- **Host**: IP address of the SmartLogger (e.g., `192.168.1.10`)
- **Port**: Modbus TCP port (default: `502`)
- **Unit ID**: SmartLogger Modbus unit ID (default: `3` - not 0 as documented!)
- **Connection Timeout**: Timeout in milliseconds (default: `5000`)
- **Retry Attempts**: Number of retry attempts on failure (default: `3`)

#### SmartLogger Discovery Options

- **Discovery Range**: Unit IDs to scan (default: `1-247`)
- **Discovery Timeout**: Shorter timeout for discovery operations (default: `2000ms`)
- **Parallel Scan Count**: Number of simultaneous scans (default: `10`)

#### SUN2000 Configuration

- **Data Categories**: Select power, status, and/or fault data
- **Discovery Input Source**: Use SmartLogger discovery output or manual configuration
- **Filter Inverters Only**: Whether to only read SUN2000 devices from discovery
- **Inverter Addresses**: Manual list of inverter addresses (when not using discovery)

## Example Output

### SmartLogger Power Data
```json
{
  "power": {
    "dcCurrentTotal": 125.6,
    "inputPowerTotal": 87.3,
    "co2Reduction": 45234.5,
    "activePowerTotal": 85.2,
    "reactivePowerTotal": 12.5,
    "powerFactor": 0.985,
    "plantStatus": "Unlimited",
    "totalEnergy": 524312.5,
    "dailyEnergy": 312.7
  }
}
```

### SmartLogger Device Discovery
```json
{
  "allDevices": [
    {
      "unitId": 3,
      "deviceName": "SmartLogger 3000A",
      "connectionStatus": "Online",
      "portNumber": 1,
      "deviceAddress": 3
    },
    {
      "unitId": 12,
      "deviceName": "100KTL-M2(COM3-12)",
      "connectionStatus": "Online",
      "portNumber": 3,
      "deviceAddress": 12
    }
  ]
}
```

### SUN2000 Inverter Data
```json
{
  "inverters": [
    {
      "unitId": 12,
      "deviceName": "100KTL-M2(COM3-12)",
      "activePower": 85.2,
      "reactivePower": 12.1,
      "dcCurrent": 125.6,
      "inputPower": 87.3,
      "powerFactor": 0.985,
      "status": 49152,
      "connectionStatus": "Status: 0xC000",
      "cabinetTemperature": 45.2,
      "insulationResistance": 1250.5
    }
  ]
}
```

## Important Notes

### Critical Huawei-Specific Fixes Applied

1. **Little-Endian Byte Order**: Despite documentation claiming big-endian, Huawei devices use little-endian
2. **SmartLogger Unit ID**: Use unit ID `3` (not `0` as documented)
3. **Gain Factors**: All proper gain factors are applied automatically

### Known Compatible Devices

- Huawei SmartLogger 3000/3000A
- Huawei SUN2000 series inverters (100KTL-M2, etc.)
- Environmental monitoring devices connected to SmartLogger

## Troubleshooting

### Discovery Taking Too Long?
- Reduce the discovery range (e.g., `3,12-15` instead of `1-247`)
- Increase parallel scan count (try `20` for faster scanning)
- Decrease discovery timeout (try `1000ms` if network is reliable)

### Getting Wrong Device Names?
- Update to version 0.0.3 or later which fixes unit ID conflicts
- Ensure only one N8N instance is accessing the device at a time

### Connection Failed?
- Verify SmartLogger IP address is correct
- Check firewall allows port 502
- Try unit ID `3` (not `0` or `1`)
- Increase connection timeout if network is slow

## Version History

- **0.0.5** - Added SUN2000 Inverter node with discovery integration
- **0.0.4** - Simplified SmartLogger UI with checkbox data selection, added CO2 reduction and Xinjiang status
- **0.0.3** - Fixed parallel discovery unit ID conflicts
- **0.0.2** - Added parallel discovery, removed redundant inverter section  
- **0.0.1** - Initial release with SmartLogger node

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/Edward-Tollemache/n8n-nodes-huaweisolar).

## License

[MIT](LICENSE.md)

## Credits

Based on working Python implementation with critical fixes for Huawei's non-standard Modbus implementation.