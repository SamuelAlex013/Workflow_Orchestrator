# n8n Node: ZeroMQ

This is an n8n community node to interact with [ZeroMQ](https://zeromq.org/) sockets. It allows you to send and receive messages using various ZeroMQ patterns.

## Supported Patterns

This node supports the following ZeroMQ socket types:

*   **Send Operations**: `PUSH`, `PUB` (Publish), `REQ` (Request)
*   **Receive Operations (Triggers)**: `PULL`, `SUB` (Subscribe), `REP` (Reply)

## Installation

To install this node, follow these steps for your n8n instance:

### Docker / Docker Compose

1.  Add the following line to your `docker-compose.yml` file under the `environment` section of your n8n service:
    ```yml
    - NODE_FUNCTION_ALLOW_EXTERNAL=n8n-nodes-zeromq
    ```
2.  Restart your n8n container.
3.  Navigate to **Settings > Community Nodes** in your n8n instance.
4.  Click **Install** and enter `n8n-nodes-zeromq`.
5.  Click **Install** again.

### npm / pnpm

If you are running n8n locally via npm or pnpm:

1.  Navigate to your n8n installation directory (e.g., `~/.n8n/`).
2.  Run the installation command:
    ```bash
    npm install n8n-nodes-zeromq
    ```
3.  Restart your n8n instance.

## Usage

Once installed, you can find the ZeroMQ node in your node panel.

1.  Add the ZeroMQ node to your workflow.
2.  Select an **Operation**: `Send` for regular nodes or `Receive` for trigger nodes.
3.  Choose the **Socket Type** (`PUSH`, `SUB`, etc.).
4.  Configure the **Socket Address** and other properties as needed.

---

Developed by Jucade Solutions.