![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-modbus-fccomplete

## Description

n8n community node package for industrial automation with complete Modbus protocol support. Provides three nodes for reading, writing, and converting Modbus data with an intuitive interface.

## Features

### Nodes

1. **Modbus Trigger** - Triggers workflows based on Modbus events
2. **Modbus** - Read/write operations for function codes FC1-FC4
3. **Modbus Data Converter** - Quick and custom data conversion with scaling

### Modbus Support

- **Function codes**: FC1 (Read Coils), FC2 (Read Discrete Inputs), FC3 (Read Holding Registers), FC4 (Read Input Registers)
- **Data types**: INT16, UINT16, INT32, UINT32, FLOAT32, Double, BCD, Bitfields
- **Byte ordering**: Big Endian and Little Endian
- **Connection types**: TCP/IP with configurable timeout and retry

### Data Converter Features

#### Quick Convert Mode
- **Single Value** - Basic INT16 conversion with scaling
- **Float (2 Registers)** - IEEE 754 32-bit floating point
- **Long Integer (2 Registers)** - 32-bit signed/unsigned with value selection
- **Double (4 Registers)** - 64-bit double precision
- **BCD** - Binary Coded Decimal conversion
- **Bitfield** - Individual bit extraction for status flags
- **All Common Types** - Shows all possible conversions

#### Custom Mode
- Multiple conversion rules per execution
- Named output fields
- Full data type support
- Configurable scaling and offsets

#### Output Organization
- **Configurable field names** for clean output structure
- **Optional metadata** with conversion details
- **Timestamp support** for time-series data
- **Scaling options** with direct factor input

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

```bash
npm install n8n-nodes-modbus-fccomplete
```

## Quick Start

### Power Meter Example (replaces Node-RED function)

1. **Modbus Node**:
   - Function Code: FC3 (Read Holding Registers)
   - Memory Address: Power register address
   - Quantity: 2 (for 32-bit values)

2. **Modbus Data Converter**:
   - Conversion Mode: Quick Convert
   - Quick Convert Type: Long Integer (2 Registers)
   - Long Integer Value: Signed (for negative power)
   - Scale: ✅ Enabled
   - Scale Factor: 0.001 (divides by 1000)
   - Add Timestamp: ✅ Enabled

**Output:**
```json
{
  "output": {
    "value": 1.234
  },
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

Access your power value with: `{{ $json.output.value }}`

### Temperature Sensor Example

1. **Modbus Node**:
   - Function Code: FC3 (Read Holding Registers)
   - Memory Address: Temperature register
   - Quantity: 2

2. **Modbus Data Converter**:
   - Conversion Mode: Quick Convert
   - Quick Convert Type: Float (2 Registers)
   - Byte Order: Big Endian
   - Output Field Name: "temperature"

**Output:**
```json
{
  "temperature": {
    "value": 23.5
  }
}
```

## Configuration

### Modbus Connection

Configure connection credentials in n8n:
- **Host**: Modbus server IP address
- **Port**: Default 502 for Modbus TCP
- **Unit ID**: Modbus slave/unit identifier
- **Timeout**: Connection timeout in milliseconds

### Data Converter Scaling

Common scaling examples:
- **Temperature sensors**: Often need scaling (e.g., 0.1 for tenths of degrees)
- **Power meters**: Typically 0.001 for kW conversion
- **Pressure sensors**: Various factors depending on units

## Troubleshooting

### Common Issues

1. **"No register data found"**
   - Ensure Modbus node output contains `data` array
   - Check connection to Modbus device

2. **Incorrect values**
   - Verify byte order (Big Endian vs Little Endian)
   - Check data type selection (signed vs unsigned)
   - Confirm scaling factor

3. **Connection timeouts**
   - Increase timeout in credentials
   - Verify network connectivity
   - Check Modbus device configuration

## Version History

- **v0.10.0** - Initial release with simplified Quick Convert and Custom modes, improved UI with always-visible output options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License