![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# Pin-Interest n8n Community Node
This community node integrates [Pinterest API v5](https://developers.pinterest.com/docs/api/v5/) with [n8n](https://n8n.io). It enables automation of creating, retrieving, and managing Pinterest boards and pins directly within your workflows.

## Features
- **Authentication**: OAuth2 (Authorization Code flow)
- **Boards**
- Create a new board
- Get a single board by ID
- List all boards (with bookmark-based pagination)
- **Pins**
- Create a pin (from Image URL, Base64 string, or binary data)
- Get a pin by ID
- Delete a pin
- List pins from a board (with pagination)

## Requirements
1. An active [Pinterest Developer Account](https://developers.pinterest.com/).
2. A registered Pinterest app with:
- OAuth redirect URI set to your n8n instance’s callback URL (e.g. `https://<your-n8n-host>/rest/oauth2-credential/callback`).
- Scopes enabled:
- `pins:read`
- `pins:write`
- `boards:read`
- `boards:write`
- `user_accounts:read`

## Authentication
1. Create credentials in n8n with type **Pin-Interest OAuth2 API**.
2. Provide your Pinterest app’s **Client ID** and **Client Secret**.
3. Authorize through the OAuth2 consent screen.

OAuth2 Settings:
- **Authorize URL**: `https://www.pinterest.com/oauth/`
- **Token URL**: `https://api.pinterest.com/v5/oauth/token`
- **Scopes**: `pins:read pins:write boards:read boards:write user_accounts:read`

## Operations

### Boards
- **Create Board**: Provide `Name` and optional `Description`.
- **Get Board**: Input the `Board ID`.
- **List Boards**: Returns all boards (or limited number with `Limit`).

### Pins
- **Create Pin**: Requires `Board ID`. Supports three media sources:
- **Image URL**: Provide a publicly accessible image link.
- **Base64 String**: Paste a base64-encoded image string.
- **Binary Property**: Pass binary data from a previous node (e.g. HTTP Request download).
- **Get Pin**: Input the `Pin ID`.
- **Delete Pin**: Input the `Pin ID`.
- **List Pins by Board**: Provide `Board ID` and set `Return All` or `Limit`.

## Example Workflow
1. **HTTP Request Node** → Download image (binary).
2. **Pin-Interest Node** → Create Pin on a target board using binary property.
3. **Google Sheets Node** → Log created Pin IDs.

## Notes
- The base URL for production is `https://api.pinterest.com/v5`.
- For testing, Pinterest provides a sandbox endpoint: `https://api-sandbox.pinterest.com/v5`.
- Image uploads larger than standard limits or video uploads require the `/media` endpoint (not currently implemented).
- Ensure your Pinterest app has production access to create pins/boards outside sandbox mode.

## Development
- Place files in:
- `nodes/PinInterest/PinInterest.node.ts`
- `credentials/PinInterestOAuth2Api.credentials.ts`
- Run `pnpm build` to compile.
- Restart n8n and the node should appear in the UI.

## License
MIT © 2025 n8n Community Contributors
