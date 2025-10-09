# n8n-nodes-telegram-forum

> A specialized collection of n8n nodes that lets you create Telegram forum topics (message threads) without manually configuring HTTP requests or exposing your Bot Token in each workflow.

---

## Contents

- [Why This Module Exists](#why-this-module-exists)  
- [Installation](#installation)  
- [Prerequisites](#prerequisites)  
- [Quick Start](#quick-start)  
- [Example Workflow](#example-workflow)  
- [Benefits and Security](#benefits-and-security)  
- [Frequently Asked Questions](#frequently-asked-questions)  
  - [Why does my node return `BOT_NO_RIGHTS_TO_MANAGE_TOPICS`?](#why-does-my-node-return-bot_no_rights_to_manage_topics)  
  - [How do I find the correct Chat ID?](#how-do-i-find-the-correct-chat-id)  
  - [Can I specify a custom emoji icon for the topic?](#can-i-specify-a-custom-emoji-icon-for-the-topic)  
- [Compatibility](#compatibility)  
- [License](#license)  
- [Author](#author)  

---

## Why This Module Exists

By default, the built-in Telegram nodes in n8n do **not** support creating forum topics in Telegram supergroups with “Topics” enabled. To work around this, you’d typically add an **HTTP Request** node, paste in a URL like:



[https://api.telegram.org/bot](https://api.telegram.org/bot)\<YOUR\_BOT\_TOKEN>/createForumTopic


and manually construct a JSON body every time. This approach has several drawbacks:

1. **Risk of Token Leakage**  
   Embedding your Bot Token in an HTTP Request node increases the chance it could be inadvertently shared when exporting or sharing workflows.

2. **Cumbersome Workflow Sharing**  
   Anyone importing your workflow must remember to replace the hard-coded token themselves.

3. **Extra Setup Overhead**  
   You have to remember the correct endpoint, format JSON payloads, and set headers manually.

**n8n-nodes-telegram-forum** solves all these problems by providing a dedicated node:

- Uses n8n’s **Credentials** mechanism, so your Bot Token is never hard-coded in the workflow.  
- Requires only **Chat ID** and **Topic Title** fields—nobody needs to hand-craft HTTP requests or copy/paste tokens.  
- Makes workflows fully shareable: anyone who imports your workflow simply chooses their own Telegram API Credential and it works out of the box.

---

## Installation

In your n8n project directory (or globally), run:

```bash
npm install --save n8n-nodes-telegram-forum
````

After installation, **restart n8n** (or close and re-open the Desktop app). You will see a new node in the list:

* **Telegram: Create Forum Topic**

---

## Prerequisites

1. **Telegram Bot**

   * Create a bot via [@BotFather](https://t.me/BotFather) if you haven’t already.
   * Obtain the Bot Token (a string like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
   * Add the bot as an **administrator** in your target supergroup and grant it the `manage_topics` permission.

2. **Supergroup with Topics Enabled**

   * The group must be a **Supergroup** (not a regular group) and have **“Topics” (Forum)** enabled. Only in that context can you create forum topics via API.

3. **Telegram API Credential in n8n**

   * In n8n, navigate to **Settings → Credentials → New Credential**.
   * Select **Telegram API**, paste your Bot Token, and save.
   * When you add the node, choose this credential—no need to embed the token manually.

---

## Quick Start

1. Open your workflow in n8n.

2. Drag and drop the **Telegram: Create Forum Topic** node onto the canvas.

3. Configure the node:

   * **Telegram API (Credential):** Select the Telegram API Credential you created.
   * **Chat ID:** Enter the numeric ID of your supergroup (e.g., `-1001234567890`).
   * **Title (Topic Title):** Provide a short, clear title (e.g., `📣 Announcements`).
   * **Icon Custom Emoji ID (Optional):** If you have a custom emoji sticker set up for your bot, paste its ID here; otherwise leave blank.

4. Save and **Execute** the workflow. The node will send the `createForumTopic` request to Telegram and output a JSON response containing fields such as:

   ```jsonc
   {
     "ok": true,
     "result": {
       "message_thread_id": 12345,
       "is_forum_topic": true,
       "name": "Announcements",
       …
     }
   }
   ```

5. If you need to post a message into the newly created topic, add a **Telegram: Send Message** node next. In that node’s settings, choose:

   * Same **Telegram API Credential**
   * **Chat ID:** The same group ID
   * **Message Thread ID:** Use the expression `{{ $json["result"]["message_thread_id"] }}` to grab it from the Create Forum Topic node
   * **Text:** Your message content

---

## Example Workflow

Below is a simple example where a scheduled trigger creates a new topic “❓ Product Questions” and immediately posts a welcome message inside it.

```jsonc
[
  {
    "nodes": [
      {
        "parameters": {
          "event": "week",
          "weekDays": ["mon"],
          "time": "08:00"
        },
        "name": "Weekly Trigger",
        "type": "n8n-nodes-base.scheduleTrigger",
        "typeVersion": 1,
        "position": [200, 200]
      },
      {
        "parameters": {
          "chatId": "-1001234567890",
          "title": "❓ Product Questions",
          "iconCustomEmojiId": ""
        },
        "name": "Create Forum Topic",
        "type": "telegramForumTopic",
        "typeVersion": 1,
        "position": [400, 200],
        "credentials": {
          "telegramApi": "Telegram API"
        }
      },
      {
        "parameters": {
          "chatId": "-1001234567890",
          "text": "Hello everyone! Feel free to ask your product-related questions here.",
          "messageThreadId": "={{ $json["result"]["message_thread_id"] }}"
        },
        "name": "Send Welcome Message",
        "type": "telegram",
        "typeVersion": 1,
        "position": [650, 200],
        "credentials": {
          "telegramApi": "Telegram API"
        }
      }
    ],
    "connections": {
      "Weekly Trigger": {
        "main": [
          [
            {
              "node": "Create Forum Topic",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Create Forum Topic": {
        "main": [
          [
            {
              "node": "Send Welcome Message",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    ]
  }
]
```

1. **Weekly Trigger** fires every Monday at 08:00.
2. **Create Forum Topic** creates a “❓ Product Questions” topic in the specified supergroup.
3. **Send Welcome Message** posts a greeting inside that new topic.

---

## Benefits and Security

* **No Hard-Coded Bot Token**
  Your Bot Token is stored securely in n8n Credentials. When you share or export workflows, recipients see a pointer to your Credential, not the actual token string. This drastically reduces the risk of accidental credential leaks.

* **Shareable Workflows**
  Colleagues or community members can import your workflow, create their own Telegram API Credential once, and everything “just works” without extra editing.

* **Minimal Configuration Overhead**
  Rather than memorizing the `createForumTopic` endpoint or building JSON payloads manually, you simply fill in Chat ID and Topic Title. The node constructs the request payload automatically, ensuring correct parameter formatting.

* **Centralized Updates**
  If Telegram updates the API or introduces new parameters for `createForumTopic`, you only need to update this module in one place. All workflows that use the node instantly benefit from the new functionality—no need to hunt down and fix multiple HTTP Request nodes.

---

## Frequently Asked Questions

### Why does my node return `BOT_NO_RIGHTS_TO_MANAGE_TOPICS`?

1. **Bot Permissions**
   Ensure your bot is an **administrator** in the target supergroup.
2. **“Topics” Enabled**
   The group must have **Forum/Topics** turned on. You cannot create a forum topic otherwise.
3. **Manage Topics Right**
   Verify that your bot has the specific `manage_topics` permission. Without it, Telegram will reject the request.

---

### How do I find the correct Chat ID?

* **Existing Telegram Nodes**
  If you already use other Telegram nodes (e.g., “Send Message”), run a test and check the output; the response includes the numeric `chat.id`.
* **Utility Bots**
  Use a helper bot such as [@getidsbot](https://t.me/getidsbot) or similar—simply add it to your group and it will report the Chat ID.
* **HTTPS Request Debugging**
  Temporarily configure a plain **Telegram: Send Message** node to send a dummy message. The node’s output JSON shows `"chat": { "id": … }`.

---

### Can I specify a custom emoji icon for the topic?

Yes. If you maintain custom emoji/sticker sets for your bot, you can use the `getForumIconStickers` method in the Telegram Bot API to retrieve valid emoji IDs. Simply paste the retrieved emoji ID into the **Icon Custom Emoji ID** field. If you leave this blank, Telegram will apply a default icon.

---

## Compatibility

* **n8n Version:** ≥ 1.82.0 (tested against `n8n-core@^1.14.1` and `n8n-workflow@^1.82.0`)
* **Node.js:** ≥ 14.x (LTS recommended)
* **Telegram Bot API:** The bot must be an administrator with `manage_topics` permission in a Supergroup that has Forum enabled.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](./LICENCE) for details.

---

## Author

**GigantPro**
✉️ [pochtagigantpro@gmail.com](mailto:pochtagigantpro@gmail.com)
GitHub: [github.com/GigantPro](https://github.com/GigantPro)

> Automate Telegram forum topic creation effortlessly! 🚀
