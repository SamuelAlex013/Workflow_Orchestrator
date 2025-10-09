# n8n-nodes-kafka-wait-event

![n8n-nodes-kafka-wait-event](https://img.shields.io/npm/v/n8n-nodes-kafka-wait-event.svg)
![License](https://img.shields.io/npm/l/n8n-nodes-kafka-wait-event.svg)

A custom n8n node that waits for specific Kafka events with configurable timeout. This node allows you to pause workflow execution until a matching Kafka message is received or a timeout occurs.

## Features

- 🕐 **Configurable Timeout**: Set custom timeout in seconds
- 🔍 **Message Filtering**: Filter by message key or JSON path expressions
- 🎯 **Offset Management**: Consistent consumer group for proper offset tracking
- 🔄 **Auto Retry**: Built-in connection retry logic with exponential backoff
- 🛡️ **Error Handling**: Graceful timeout and error handling
- 📊 **Full Message Context**: Returns complete message metadata (topic, partition, offset, timestamp, headers)

## Installation

### Via npm (Recommended)

```bash
npm install n8n-nodes-kafka-wait-event
```

### Self-hosted n8n

If you're running n8n in a Docker container or self-hosted environment:

1. Install the package in your n8n installation:
   ```bash
   npm install n8n-nodes-kafka-wait-event
   ```

2. Set the `N8N_CUSTOM_EXTENSIONS` environment variable:
   ```bash
   export N8N_CUSTOM_EXTENSIONS="/path/to/node_modules/n8n-nodes-kafka-wait-event"
   ```

3. Restart n8n

## Prerequisites

- n8n version 1.0.0 or higher
- Kafka cluster accessible from n8n
- Kafka credentials configured in n8n (uses built-in Kafka credentials)

## Usage

### Basic Configuration

1. **Kafka Credentials**: Use the built-in n8n Kafka credentials
2. **Topic Name**: Specify the Kafka topic to listen to
3. **Group ID**: Set a consumer group ID (default: `n8n-kafka-wait-event`)
4. **Timeout**: Maximum time to wait for a message (default: 30 seconds)

### Advanced Filtering

#### Message Key Filter
Filter messages by exact key match:
```
Key Filter: "user-123"
```

#### JSON Path Value Filter
Filter messages by JSON content using JSONPath expressions:
```
Value Filter: $.eventType
Expected Value: "user_created"
```

### Advanced Options

- **Heartbeat Interval**: Consumer heartbeat frequency (default: 3000ms)
- **Session Timeout**: Consumer session timeout (default: 30000ms)
- **Max Wait Time**: Maximum fetch request wait time (default: 5000ms)

## Example Workflow

```json
{
  "nodes": [
    {
      "name": "Wait for User Event",
      "type": "n8n-nodes-kafka-wait-event.kafkaWaitEvent",
      "parameters": {
        "topicName": "user-events",
        "groupId": "user-workflow-handler",
        "timeoutSeconds": 60,
        "filterOptions": {
          "valueFilter": "$.eventType",
          "expectedValue": "user_created"
        }
      },
      "credentials": {
        "kafka": "kafka-prod"
      }
    }
  ]
}
```

## Output Format

When a matching message is received, the node outputs:

```json
{
  "topic": "user-events",
  "partition": 0,
  "offset": "1234567",
  "key": "user-123",
  "value": {
    "eventType": "user_created",
    "userId": "123",
    "timestamp": "2024-01-01T12:00:00Z"
  },
  "timestamp": "1704110400000",
  "headers": {}
}
```

## Error Handling

- **Timeout**: If no matching message is received within the timeout period, the node throws a `NodeOperationError`
- **Connection Issues**: Built-in retry logic attempts connection up to 3 times with exponential backoff
- **Filter Errors**: Invalid JSONPath expressions or parsing errors are handled gracefully

## Comparison with Kafka Trigger

| Feature | Kafka Wait Event | Kafka Trigger |
|---------|------------------|---------------|
| Node Type | Execution | Trigger |
| Usage | Wait for specific events in workflow | Start workflow on any message |
| Timeout | Configurable timeout | Continuous listening |
| Consumer Groups | Consistent for offset tracking | New group per execution |
| Filtering | Key + JSONPath filtering | No built-in filtering |
| Workflow Integration | Pauses workflow execution | Initiates workflow |

## Development

### Building

```bash
npm run build
```

### Linting

```bash
npm run lint
npm run lintfix  # Auto-fix issues
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/halimtuhu/n8n-kafka-wait-event/issues)
- 📧 **Email**: halimtuhuprasetyo@gmail.com

## Related

- [n8n Documentation](https://docs.n8n.io/)
- [KafkaJS Documentation](https://kafka.js.org/)
- [Creating n8n Nodes](https://docs.n8n.io/integrations/creating-nodes/)