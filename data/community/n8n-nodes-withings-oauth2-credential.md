# n8n-nodes-withings-oauth2-credential

A community node package for n8n that provides OAuth2 authentication for the Withings API.

## Features

- **Custom OAuth2 Credential**: Handles Withings' non-standard OAuth2 implementation that requires `action=requesttoken` during token exchange
- **Automatic Token Management**: n8n handles authorization, token exchange, storage, and refresh automatically
- **Clean Integration**: Use with HTTP Request nodes or any custom Withings nodes
- **Dummy Node Included**: Contains a minimal dummy node to satisfy n8n package requirements (use HTTP Request nodes instead)

## Installation

### Community Nodes (Recommended)

1. Go to **Settings** → **Community Nodes** in your n8n instance
2. Click **Install a community node**
3. Enter: `n8n-nodes-withings-oauth2-credential`
4. Click **Install**

### Manual Installation

```bash
npm install n8n-nodes-withings-oauth2-credential
```

## Setup

### 1. Create Withings Developer App

1. Go to [Withings Developer Portal](https://developer.withings.com/)
2. Create a new application
3. Set the **Callback URL** to: `https://your-n8n-instance.com/rest/oauth2-credential/callback`
4. Note your **Client ID** and **Client Secret**

### 2. Configure Credential in n8n

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for "Withings OAuth2 API"
3. Fill in:
   - **Client ID**: From your Withings app
   - **Client Secret**: From your Withings app
   - **Scope**: `user.info,user.metrics,user.activity` (or customize as needed)
4. Click **Connect my account**
5. Complete the OAuth2 authorization flow

## Usage

### With HTTP Request Node (Recommended)

1. Add an **HTTP Request** node to your workflow
2. Set **Authentication** to "Predefined Credential Type"
3. Select **Credential Type**: "Withings OAuth2 API"
4. Choose your configured credential
5. Configure your request:
   - **Method**: POST
   - **URL**: `https://wbsapi.withings.net/v2/user`
   - **Body**: `action=getbyuserid` (or other Withings API actions)

### Dummy Node

This package includes a "Withings Dummy" node to satisfy n8n's package requirements, but it's recommended to use HTTP Request nodes instead for actual API calls.

### Example API Calls

**Get User Info:**
```
POST https://wbsapi.withings.net/v2/user
Body: action=getbyuserid
```

**Get Measurements:**
```
POST https://wbsapi.withings.net/v2/measure
Body: action=getmeas&startdate=1609459200&enddate=1640995200
```

## How It Works

Withings uses a non-standard OAuth2 implementation that requires an additional `action=requesttoken` parameter during token exchange. This credential:

1. **Extends n8n's genericAuth**: Provides full control over the token exchange process
2. **Injects Required Parameter**: Automatically adds `action=requesttoken` to token requests
3. **Handles Standard Flow**: Authorization URL, redirect, and token storage work normally

## Technical Details

- **Credential Type**: `genericAuth` with custom `authenticate()` method
- **Authorization URL**: `https://account.withings.com/oauth2_user/authorize2`
- **Token URL**: `https://wbsapi.withings.net/v2/oauth2`
- **Required Parameter**: `action=requesttoken` (automatically injected)

## Troubleshooting

### "Invalid Grant" Error
- Ensure your redirect URI in Withings matches exactly: `https://your-n8n-instance.com/rest/oauth2-credential/callback`
- Check that your Client ID and Client Secret are correct

### "Scope Error"
- Verify the scopes in your credential match what's configured in your Withings app
- Common scopes: `user.info`, `user.metrics`, `user.activity`, `user.sleepevents`

### Token Refresh Issues
- n8n handles token refresh automatically
- If issues persist, re-authorize the credential

## Development

```bash
# Clone the repository
git clone https://github.com/mrowrpurr/n8n-nodes-withings-oauth2-credential.git
cd n8n-nodes-withings-oauth2-credential

# Install dependencies
npm install

# Build
npm run build

# Lint
npm run lint
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
