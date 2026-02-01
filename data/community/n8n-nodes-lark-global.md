### Credits
Original node created by [zhgqthomas](https://github.com/zhgqthomas/n8n-nodes-feishu-lark).  
Optimized and internationalized by [ariesho2903](https://github.com/ariesho2903).  
Contact: [Telegram](https://t.me/ariesho205)  
# n8n Nodes Lark Global

Custom n8n community nodes for interacting with Lark Open Platform, including action nodes, triggers, and MCP helpers.

## Highlights
- Full CRUD coverage for Lark Bitable, Documents, Calendar, Space, Contacts, Messages, and Wiki APIs.
- Webhook and WebSocket triggers for receiving Lark events inside n8n.
- MCP tooling support so AI agents can call Lark Open APIs through the MCP protocol.
- Typed parameter descriptions and rich list-search helpers for faster workflow building.

## Credentials

The nodes rely on two credential types that point at the Lark global platform (`https://open.larksuite.com`). Create both credentials under *Settings -> API integrations* in n8n.

### Lark Tenant Token API
1. Open the Lark developer console and create or select a classic custom app.
2. Copy the **App ID** and **App Secret** from *Credentials -> App credentials*.
3. In n8n choose **Lark Tenant Token API**, keep the base URL as `https://open.larksuite.com`, and paste the App ID/Secret.
4. Save. The credential automatically refreshes `tenant_access_token` values when required.

### Lark OAuth2 API
1. In the same Lark app enable OAuth 2.0 and add `https://api.n8n.io/oauth2/callback` (or your own n8n callback URL) as the redirect URL.
2. Copy the Client ID/Secret and configure scopes such as `offline_access`, `bitable:app`, `calendar:calendar` as needed by your workflow.
3. In n8n choose **Lark OAuth2 API**, keep the base URL as `https://open.larksuite.com`, enter the Client ID/Secret, scopes, and save. The credential uses PKCE and stores refresh tokens automatically.

## Usage Notes
- WebSocket triggers require the bot to have *Event Subscription* permissions and only one live connection per bot is supported.
- Webhook triggers use the `parse webhook` operation together with the core `Webhook` + `Respond to Webhook` nodes for validation and response handling.
- Many operations expose list-search helpers (Bitable apps, tables, roles, calendars, etc.) - use the dropdown to avoid guessing IDs.
- Most operations accept raw JSON bodies; enable *JSON Parameters* to send data exactly as required by the Lark API reference.

## Development
```
npm install
npm run build
npm run lint
```
Install the compiled package inside your n8n instance (Community Nodes -> Install) and restart n8n.

## Resources
- [Lark Open Platform documentation](https://open.larksuite.com/document/)
- [n8n Community Nodes guide](https://docs.n8n.io/integrations/community-nodes/)
- [Issue tracker](https://github.com/ariesho2903/n8n-nodes-lark-global/issues)

MIT License.


## Acknowledgment
> This package is based on the open-source work [n8n-nodes-feishu-lark](https://github.com/zhgqthomas/n8n-nodes-feishu-lark) by zhgqthomas.  
> This fork has been optimized to remove Feishu dependencies and provide smoother performance for Lark-only use cases, rebranded as **n8n Lark Global**.  
> Maintained by [ariesho2903](https://github.com/ariesho2903).








