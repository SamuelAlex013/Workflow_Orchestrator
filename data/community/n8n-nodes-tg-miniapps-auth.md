# n8n-nodes-tg-miniapps-auth

n8n node for Telegram Mini Apps authentication and user management

## Features

- **Telegram Mini Apps Authentication**: Verify init-data from Telegram Mini Apps
- **User Data Extraction**: Extract user information from verified init-data
- **Security**: Cryptographic verification using HMAC-SHA256
- **Configurable**: Customizable max age for init-data validation

## Installation

```bash
npm install n8n-nodes-tg-miniapps-auth
```

## Usage

### 1. Configure Telegram Credentials

1. Create a new Telegram Bot using [@BotFather](https://t.me/botfather)
2. Get your bot token
3. In n8n, go to Credentials and create a new "Telegram API" credential
4. Enter your bot token

### 2. Use the Telegram Mini Apps Auth Node

1. Add the "Telegram Mini Apps Auth" node to your workflow
2. Configure the node:
   - **Init Data**: The init-data string from your Telegram Mini App
   - **Max Age**: Maximum age of init-data in seconds (default: 86400 = 24 hours)
   - **Options**:
     - Include Raw Data: Whether to include the raw init-data string in output
     - Include Hash: Whether to include the hash in output

### 3. Input Data Format

The node expects init-data in the following format:
```
query_id=AAHdF6IQAAAAAN0XohDhrOrc&user=%7B%22id%22%3A279058397%2C%22first_name%22%3A%22Vladislav%22%2C%22last_name%22%3A%22Kibenko%22%2C%22username%22%3A%22vdkfrost%22%2C%22language_code%22%3A%22ru%22%7D&auth_date=1662771648&hash=c501b71e775f74ce10e377dea85a7ea24ecd640b223ea86dfe453e0eaed2e2b2
```

### 4. Output Data

The node returns verified user data:

```json
{
  "verified": true,
  "query_id": "AAHdF6IQAAAAAN0XohDhrOrc",
  "user": {
    "id": 279058397,
    "first_name": "Vladislav",
    "last_name": "Kibenko",
    "username": "vdkfrost",
    "language_code": "ru"
  },
  "auth_date": 1662771648,
  "user_id": 279058397,
  "user_name": "Vladislav Kibenko",
  "is_authenticated": true
}
```

## Security

The node implements the official Telegram Mini Apps authentication protocol:

1. **Hash Verification**: Uses HMAC-SHA256 to verify the integrity of init-data
2. **Time Validation**: Checks that init-data is not older than the specified max age
3. **Bot Token**: Uses your bot's secret token for cryptographic verification

## Error Handling

The node handles various error scenarios:
- Invalid or missing hash
- Expired init-data
- Malformed user data
- Missing required fields

When `Continue on Fail` is enabled, the node returns:
```json
{
  "verified": false,
  "error": "Error message",
  "is_authenticated": false
}
```

## Development

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run in development mode
npm run dev
```

## License

MIT