# n8n-nodes-zalo-oa-refresh

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

An n8n community node for Zalo Official Account token refresh automation. This node helps you automatically refresh Zalo OA access tokens before they expire, ensuring your integrations stay connected.

## Features

- 🔄 **Automatic Token Refresh**: Refresh Zalo OA access tokens before they expire
- ✅ **Token Status Check**: Check if current tokens are still valid
- ⏰ **Smart Scheduling**: Only refresh when needed (< 2 hours until expiry)
- 🔐 **Multi-Layer Storage**: Workflow static data + database + environment variables
- 🛡️ **Robust Error Handling**: Graceful fallbacks when storage methods fail
- 📊 **Detailed Logging**: Comprehensive execution logs with ✅/❌ status indicators
- 🔧 **Production Ready**: Multiple backup storage methods ensure reliability

## Installation

### Via n8n Community Nodes

1. Go to your n8n instance
2. Navigate to **Settings** → **Community Nodes**
3. Click **Install a Community Node**
4. Enter: `n8n-nodes-zalo-oa-refresh`
5. Click **Install**

### Via npm

```bash
# Install globally
npm install -g n8n-nodes-zalo-oa-refresh

# Or install in your n8n project
npm install n8n-nodes-zalo-oa-refresh
```

## Credentials

### Zalo Official Account API

This node requires a **Zalo Official Account API** credential with the following fields:

| Field | Description | Required |
|-------|-------------|----------|
| App ID | Your Zalo OA App ID from Developer Console | ✅ |
| Secret Key | Your Zalo OA Secret Key | ✅ |
| Access Token | Current access token (auto-updated) | ❌ |
| Refresh Token | Token used to refresh access token | ✅ |
| Token Expires At | ISO date when token expires | ❌ |

### Getting Credentials

1. Go to [Zalo Developer Console](https://developers.zalo.me/)
2. Create or select your Official Account app
3. Get your **App ID** and **Secret Key**
4. Obtain initial **Refresh Token** through OAuth flow
5. Configure the credential in n8n

## Nodes

### Zalo OA Refresh Token

Main node for token management operations.

#### Operations

**Refresh Token**
- Calls Zalo API to refresh access token
- Returns new access token and refresh token
- Calculates new expiration time

**Check Token Status**  
- Checks if current token is still valid
- Returns time until expiry
- Indicates if refresh is needed

#### Example Workflow

```json
{
  "name": "Zalo OA Token Refresh Automation",
  "nodes": [
    {
      "name": "Schedule Every 23 Hours",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "rule": {
          "interval": [{"field": "hours", "hoursInterval": 23}]
        }
      }
    },
    {
      "name": "Check Token Status", 
      "type": "n8n-nodes-zalo-oa-refresh.zaloOaRefreshToken",
      "parameters": {
        "operation": "checkStatus"
      }
    },
    {
      "name": "Refresh if Needed",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "boolean": [{
            "value1": "={{$json.should_refresh}}",
            "value2": true
          }]
        }
      }
    },
    {
      "name": "Refresh Token",
      "type": "n8n-nodes-zalo-oa-refresh.zaloOaRefreshToken", 
      "parameters": {
        "operation": "refreshToken"
      }
    }
  ]
}
```

## API Reference

### Zalo OAuth Endpoint

The node calls this Zalo API endpoint:

```
POST https://oauth.zaloapp.com/v4/oa/access_token
Content-Type: application/x-www-form-urlencoded
secret_key: YOUR_SECRET_KEY

refresh_token=YOUR_REFRESH_TOKEN&
app_id=YOUR_APP_ID&
grant_type=refresh_token
```

### Response Format

```json
{
  "access_token": "new_access_token_here",
  "refresh_token": "new_refresh_token_here", 
  "expires_in": "90000"
}
```

## Scheduling Recommendations

- **Every 23 hours**: Safe interval to refresh before 25-hour expiry
- **Check before refresh**: Always check token status first
- **Handle failures**: Implement retry logic and alerts
- **Monitor logs**: Review execution history regularly

## Security Best Practices

- ✅ Store credentials securely in n8n credential manager
- ✅ Use environment variables for sensitive data
- ✅ Enable webhook authentication where possible
- ✅ Monitor token usage and refresh patterns
- ❌ Never log or expose tokens in plain text
- ❌ Don't commit credentials to version control

## Troubleshooting

### Common Issues

**Token refresh fails**
- Check if secret key is correct
- Verify refresh token hasn't expired
- Ensure network connectivity to Zalo API

**Node not found in n8n**
- Restart n8n after installation
- Check community nodes are enabled
- Verify installation completed successfully

**Credentials not working**
- Double-check App ID and Secret Key
- Test with Zalo API directly using curl
- Verify OAuth flow was completed correctly

### Debug Tips

1. Enable detailed logging in n8n
2. Test with "Check Token Status" first
3. Use n8n's execution logs to trace issues
4. Check Zalo Developer Console for API limits

## Development

### Local Development

```bash
# Clone repository
git clone https://github.com/yourusername/n8n-nodes-zalo-oa-refresh.git
cd n8n-nodes-zalo-oa-refresh

# Install dependencies
pnpm install

# Build
pnpm build

# Watch mode
pnpm dev
```

### Testing

```bash
# Run linter
pnpm lint

# Format code
pnpm format

# Run tests
pnpm test
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Changelog

### v1.5.2 (2025-08-22)

**🔧 Major Token Storage Improvements**
- ✅ **Multi-layer storage system**: Tokens now saved to workflow static data, database, AND environment variables
- ✅ **Robust error handling**: Graceful fallbacks when any storage method fails
- ✅ **Fixed database issues**: Proper SQLite syntax with UUID generation for n8n variables table
- ✅ **Enhanced logging**: Clear ✅/❌ status indicators for each storage method
- ✅ **Production reliability**: Never fails completely - always has backup storage
- ✅ **Priority retrieval**: Smart token fetching with fallback hierarchy

**Technical Fixes**
- Fixed SQL syntax from PostgreSQL to SQLite (`INSERT OR REPLACE` instead of `ON CONFLICT`)
- Added proper ID field handling for n8n variables table
- Improved database connection handling with fallback methods
- Enhanced TypeScript type safety for workflow static data
- Better error isolation - single storage failure doesn't break entire operation

### v1.5.1 and earlier
- Initial release with basic token refresh functionality
- Zalo OA API integration
- Basic credential management

## License

[MIT](LICENSE)

## Support

- 📖 [Documentation](https://github.com/yourusername/n8n-nodes-zalo-oa-refresh/wiki)
- 🐛 [Report Issues](https://github.com/yourusername/n8n-nodes-zalo-oa-refresh/issues)
- 💬 [Discussions](https://github.com/yourusername/n8n-nodes-zalo-oa-refresh/discussions)

---

Made with ❤️ for the n8n community
