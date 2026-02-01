
# MetisAi Node for n8n

This is a custom node for [n8n](https://n8n.io/) that integrates the **MetisAi API**, providing seamless access to advanced conversational AI capabilities directly within your automation workflows in https://metisai.ir.

---

## 🚀 Overview

The **MetisAi Node** allows users to:
- Initiate conversational sessions with Metis AI bots.
- Send messages and receive responses within workflows.
- Simplify and automate interactions with AI-powered conversational services.

---

## 🔑 Requirements

Before using this node, you need to have:
- An active API Key from [MetisAi](https://docs.metisai.ir).
- The **Bot ID** of your Metis AI conversational bot.

---

## ⚙️ Installation

1. Clone or download this repository into your n8n custom nodes folder.
2. Ensure dependencies like `axios` are installed:
   ```bash
   npm install axios
   ```
3. Restart your n8n instance to load the custom node.

---

## 📝 Node Parameters

| Parameter              | Type     | Description                             | Example           |
|------------------------|----------|-----------------------------------------|-------------------|
| **BOT ID**             | `string` | Unique identifier of your Metis AI bot  | `abc123botid`     |
| **Initial Message Type**| `option` | Type of initial message (`USER` or `SYSTEM`) | `USER`            |
| **Initial Message**    | `string` | Content of the initial message          | `Hello MetisAI!`  |
| **Prompt**             | `string` | Message prompt to send to the bot       | `How's the weather?` |

---

## 🔐 Authentication

The node securely utilizes the `MetisAiApi` credential. Simply create a credential in your n8n instance with your MetisAi API key.

---

## 📖 Documentation

Complete API documentation for MetisAi can be found here:
- [MetisAi API Documentation](https://docs.metisai.ir)

---

## 🧑‍💻 Developer

This node was developed by **Hossein Khoshraftar** ([hkhoshraftar2](https://github.com/hkhoshraftar2))

---

## 🌟 Contributing

Feel free to submit issues, feature requests, and contributions via GitHub.

---

**Happy automating! 🎉**
