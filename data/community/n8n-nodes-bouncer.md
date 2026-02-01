# n8n-nodes-bouncer

[![npm version](https://img.shields.io/npm/v/n8n-nodes-bouncer.svg)](https://www.npmjs.com/package/n8n-nodes-bouncer)
[![n8n community node](https://img.shields.io/badge/n8n-community%20node-orange)](https://n8n.io/)

A custom n8n node for integrating with the [NeverBounce](https://neverbounce.com/) email verification API (or your own API).  
Easily verify emails and automate your workflows with n8n!

---

## Features

- **Email Verification:** Instantly verify email addresses using the NeverBounce API.
- **Easy Integration:** Plug-and-play with your n8n instance.
- **Customizable:** Supports additional fields and flexible API routing.
- **Open Source:** MIT licensed.

---

## Installation

### 1. Install in your n8n instance

```bash
npm install n8n-nodes-bouncer
```

Or, if you use a custom nodes folder:

```bash
cd ~/.n8n/custom
npm install n8n-nodes-bouncer
```

### 2. Restart n8n

```bash
n8n stop
n8n start
```
or just restart your n8n process/service.

---

## Usage

1. **Open n8n Editor.**
2. **Add the "The Never Bounce" node** to your workflow.
3. **Configure your API credentials** (see below).
4. **Set the email address** you want to verify.
5. **Run the workflow** to verify emails automatically!

---

## Credentials

This node requires an API key for the NeverBounce API (or your own API).  
Set up your credentials in n8n under **Credentials** > **BouncerApi**.

---

## Example Workflow

```json
{
  "nodes": [
    {
      "parameters": {
        "email": "test@example.com"
      },
      "name": "Bouncer",
      "type": "n8n-nodes-bouncer",
      "typeVersion": 1,
      "position": [450, 300]
    }
  ]
}
```

---

## Node Properties

| Property   | Type   | Description                       |
|------------|--------|-----------------------------------|
| email      | string | The email address to verify       |
<!-- | ...        | ...    | Add your other fields here        | -->

---

## Development

### Build

```bash
npm run build
```

### Lint

```bash
npm run lint
```

### Test

```bash
npm test
```

---

## Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Author

- [Neehal Ahmed Qureshi](https://github.com/NeehalAhmedQureshi)
- *Email Address*:m.nehalq125@gmail.com

---

## Support

If you have any questions or issues, please open an [issue](https://github.com/NeehalAhmedQureshi/n8n-nodes-bouncer/issues) on GitHub.

---

**Happy automating! 🚀**
