# Discord Signature Validator for n8n

This is a **community node for n8n** that validates Discord ED25519 request signatures.  
It is designed to work with Discord Webhooks and allows you to verify that incoming requests are authentic.

---

## Features

- Validates Discord webhook signatures using `x-signature-ed25519` and `x-signature-timestamp`.
- Simple Node interface: provide **Public Key**, **Signature**, **Timestamp**, and **Raw Body**.
- Returns `{ valid: true/false }` in the output JSON.

---

## How to Use

1. **Install the node** via npm:

   Access your Docker shell (if running with Docker):

   ```bash
   docker exec -it n8n sh
   ```

   Create the custom nodes folder if it doesn’t exist and navigate into it:

   ```bash
   mkdir -p ~/.n8n/nodes
   cd ~/.n8n/nodes
   ```

   Install the node:

   ```bash
   npm install n8n-nodes-discord-signature-validator
   ```

   > 🔁 Reinicia n8n después de instalar para que detecte el nuevo nodo.

   Alternatively, if you are self-hosting without Docker, you can copy this repository into `~/.n8n/custom/`.

2. **Add a Webhook Node** in your workflow to receive Discord events.

   - Make sure you have **Raw Body** enabled to pass the exact payload.

3. **Add the Discord Signature Validator Node**:

   - `Public Key (hex)`: Your Discord application's public key.
   - `Signature (hex)`: `{{$json["headers"]["x-signature-ed25519"]}}`
   - `Timestamp`: `{{$json["headers"]["x-signature-timestamp"]}}`
   - `Raw Body`: `{{$binary["data"].data.toString()}}` (or `{{ JSON.stringify($json) }}` if using JSON)

4. **Use an IF Node** to check `{{$json["valid"]}}` and route your workflow accordingly.

---

## Example Output

```json
{
	"valid": true,
	"signature": "60f1df1975c5771dcdc5bf55f9351f91c720f061541727c7bc8ebb058638f01eb261767d98259564a28f5699ebc3cfd0ad7d269825f01a012da20ebf21deaf0c",
	"timestamp": "1758306667",
	"messageSample": "{\"type\":1,...}"
}
```

---

## Dependencies

- [tweetnacl](https://www.npmjs.com/package/tweetnacl)

---

## License

MIT
