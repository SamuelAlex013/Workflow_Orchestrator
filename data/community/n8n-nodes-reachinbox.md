![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-reachinbox

This custom node allows users to connect [ReachInbox.ai](https://reachinbox.ai) with n8n, enabling workflows to be triggered by email events (e.g. email sent, reply received) and perform powerful actions like adding leads, updating their statuses, starting campaigns, and more.

n8n is a fair-code licensed workflow automation platform.

---

## 📦 Installation

Follow the official [n8n custom nodes installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to install this package.

```bash
npm install n8n-nodes-reachinbox
```

Or for local development:

```bash
git clone https://github.com/<your-org>/n8n-nodes-reachinbox.git
cd n8n-nodes-reachinbox
npm install
npm run build
npm link
```

Then link it in your local `~/.n8n/custom/` folder:

```bash
cd ~/.n8n/custom
npm init -y
npm link n8n-nodes-reachinbox
```

---

## 🤖 ReachInbox Setup

To use this integration, you’ll need an **API Key** from ReachInbox:

1. Log in to [ReachInbox.ai](https://app.reachinbox.ai).
2. Go to **Settings** > **Integrations** > **n8n**.
3. Copy your API Key and Base URL (typically `https://api.reachinbox.ai`).

---

## 🔧 Credentials

This node requires the following credentials:

* **API Key**: Your ReachInbox API key.
* **Base URL**: API base URL (`https://api.reachinbox.ai`).

Set these up once in the **Credentials** section in n8n.

---

## ⚡ Operations

### 🟢 Triggers

You can use this node to trigger workflows on events like:

* Email Sent
* Email Opened
* Email Link Clicked
* Reply Received
* Email Bounced
* Lead Interested
* Lead Not Interested
* Campaign Completed
* Or trigger on **All Events**

These are dynamically fetched from ReachInbox’s API.
After setting up, a webhook URL will be generated which you must add in ReachInbox → **Integrations** → **Webhooks**.

### 🛠️ Actions

* **Add Lead to Campaign**
* **Update Lead to Campaign**
* **Remove Lead to Campaign**

All actions require selecting a campaign and passing necessary data (email, first name, last name, etc.), which can be mapped from previous steps.

---

## ✅ Usage

1. **Install the node** as described in the installation section.
2. **Drag the ReachInbox Trigger or Action node** into your workflow.
3. **Set up your credentials** by entering your API key and base URL.
4. **Choose a trigger event** or action.
5. **Map the required fields**, test the workflow, and activate.

You can now fully automate your cold outreach operations.

---

## 🧪 Testing Locally

To run locally:

```bash
n8n
```

Then open [http://localhost:5678](http://localhost:5678) and search for **ReachInbox** in the node list.

---

## 📎 Compatibility

* Tested on **n8n v1.75.2**
* Node.js **v20+**

---

## 🕓 Version History

| Version | Description                                          |
| ------- | ---------------------------------------------------- |
| 0.1.0   | Initial release with full trigger and action support |

---

## 🧩 Resources

* [ReachInbox API Docs](https://docs.reachinbox.ai)
* [n8n Community Nodes Guide](https://docs.n8n.io/integrations/community-nodes/)