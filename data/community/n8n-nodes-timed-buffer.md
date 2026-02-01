![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)


# n8n-nodes-timed-buffer

A custom n8n node that collects incoming messages into a time‑based buffer and emits them all at once. It uses Redis to maintain buffer state and requires a Redis credential to operate.

---

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

---

## Usage

1. **Session Key** (String)
   Unique identifier (e.g. `conversation-123`) to group executions into the same buffer.
2. **Content** (String)
   Data to buffer (e.g. `Hello`).
3. **Wait Amount** (Number)
   Numeric delay before emitting the buffer (e.g. `30`).
4. **Wait Unit** (Dropdown)
   Time unit for the delay: `seconds`, `minutes`, `hours`, or `days`.
5. **Redis Credential** (Credential, required)
   Create a [Redis credential](https://docs.n8n.io/integrations/builtin/credentials/redis/#using-database-connection) in n8n and select it here. The node will not function without it.

---

## Node Parameters

| Parameter            | Type        | Description                                          |
| -------------------- | ----------- | ---------------------------------------------------- |
| **Session Key**      | String      | Unique key to group messages                       |
| **Content**          | String | Data to accumulate                                   |
| **Wait Amount**      | Number      | Numeric value for delay                              |
| **Wait Unit**        | Dropdown    | `seconds`, `minutes`, `hours`, or `days`             |
| **Redis Credential** | Credential  | **Required**: Use Redis for cross-instance buffering |

---

## Outputs

1. **Resume**
   Fires once after the wait interval, returning all buffered content:

   ```json
   [
     {
       "data": [ … ]
     }
   ]
   ```
2. **Skipped**
   Fires on any execution arriving during an active interval (returns `{}`).

---

## Example: Chat Message Buffering

![Screenshot of example workflow](./images/example.png)

1. Five WhatsApp messages arrive.
2. Four are routed to **Skipped**.
3. After 10 seconds from the last message, the node sends all five messages in **Resume**.

   ```json
   [
     {
       "data": [
         "Hi!",
         "How are you?",
         "What’s up?",
         "Let’s meet.",
         "Bye!"
       ]
     }
   ]
   ```

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
