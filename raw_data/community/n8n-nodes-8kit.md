<div align="center">
<img src="https://8kit.io/logo.svg" alt="8kit Logo" width="120" height="120">

**Essential n8n Node for Reliable Workflows**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://8kit.io/community)
[![GitHub](https://img.shields.io/badge/GitHub-8kit--community-181717?logo=github&logoColor=white)](https://github.com/8kit-io/n8n-node-8kit-community)

*The n8n node that makes your workflows bulletproof*

</div>

---

Part of the 8kit⁠ n8n integration framework. See [8kit.io](https://8kit.io)⁠ for full details.

---

## 🚀 What is the 8kit n8n Node?

The 8kit n8n node brings 8kit capabilities directly into your n8n workflows. Easily access the powerful capabilities of the 8kit suite directly from within n8n (Uniq, Lookup, Lock, App).

### What is 8kit?

8kit is a comprehensive automation toolkit with three core components: an n8n node for workflow integration, a lightweight service for data synchronization, and an admin dashboard for management — making your automations faster, safer, and smarter.

### Common Automation Problems 8kit Solves

Running into these frustrating automation challenges?

- **Duplicate Processing** – The same data gets processed multiple times across different runs
- **ID Mapping Chaos** – Customer #123 in one system becomes Customer #456 in another one - now what?
- **Race Conditions** – Multiple processes trying to update the same record simultaneously
- **No Audit Trail** – When something breaks, you have no idea what happened

### How the 8kit n8n Node Helps

Add the 8kit node to your n8n workflows and get:

✅ **Persistent storage** – Your workflows remember everything between runs  
✅ **Smart Deduplication** – Built-in checks prevent duplicate processing  
✅ **Cross-System ID Mapping** – Seamlessly connect data between different platforms  
✅ **Distributed Transactions** – Prevent conflicts in multi-process environments

## 🔧 Getting Started with 8kit in n8n

### Step 0: Prerequisites

You need access to a running 8kit service before the node can do useful work. Configure your own instance by following the [8kit documentation](https://8kit.io/docs).

### Step 1: Install the 8kit n8n Node

1. **Search for 8kit in the n8n sidebar**
   - Open your n8n instance
   - Look for "8kit" in the node sidebar on the right
   - If you can't find the 8kit node, see the step below.
  
   ![Install 8kit Node](docs/images/8kit-node-side.png)

2. **Install via Community Nodes (if not found)**
   - Go to **Settings** → **Community Nodes**
   - Click **Install a community node**
   - Enter the package name: `n8n-nodes-8kit`
   - Click **Install**

   ![Install 8kit Node](docs/images/install-8kit-node.png)

### Step 2: Create the 8kit API credentials

 1. **Create new credentials**

- Go to the credentials section in n8n
- Select **8kit API** as the credential type
- Fill in the required fields:

   | Field | Description |
   | --- | --- |
   | `Host URL` | Base URL of the service API, such as `http://localhost:4000`. |
   | `API Key` | Application key generated in the 8kit admin dashboard. (See more [8kit.io](https://8kit.io)⁠) |

   ![Create 8kit Credentials](docs/images/create-8kit-credentials.png)
   (Example of an 8kit service running locally on port 4000) 


2. **Test the connection**
   - Click **Test** to verify your credentials work

The credential is reused across every 8kit node in a workflow.

## Actions

When using 8kit nodes, each operation returns structured items on distinct outputs (for example existing vs non-existing Uniq values) so you can branch logic without manual parsing.

<img src="docs/images/setvalues-check.png" alt="Operation" height="300">

Available operations include:

🔄 **Uniq Collections & Uniq Values**

- Track processed items, user preferences, or configuration data
- Operations: Create Uniq Collection, List Uniq Collections, Get Uniq Collection Info, Get Uniq Values, Add to Uniq, Check Uniq Values, Remove from Uniq

🔗 **Lookup Collections & Lookups**

- Map identifiers across different platforms seamlessly
- Operations: Create Lookup Collection, List Lookup Collections, Get Lookup Values, Add to Lookup, Complete Lookup + Uniq, Remove from Lookup

🔒 **Locks**

- Manage distributed transactions for resource coordination
- Prevent race conditions
- Operations: Acquire Lock, Check Lock, Release Lock

⏰ **Last Updated**

- Track when workflow processed something
- Operations: Add New Last Updated, Get Last Updated

 ![Install 8kit Node](docs/images/8kit-actions.png)

## 📚 Resources

- **📖 [Complete Documentation](https://8kit.io/docs)** – Learn everything about 8kit deployment and APIs
- **💻 [GitHub Repository](https://github.com/8kit-io/n8n-node-8kit-community)** – Source code and community contributions
- **💬 [Discord Community](https://8kit.io/community)** – Get help and share experiences

## n8n Community

This community node is built by n8n users, for n8n users. Whether you're just getting started with n8n workflows or you're a seasoned automation expert, join our community to share experiences and get help!

---

<div align="center">

**Ready to supercharge your n8n workflows?**

[Get Started with 8kit](https://8kit.io/docs) | [View on GitHub](https://github.com/8kit-io/n8n-node-8kit-community)

</div>

Brought to you by [Stratagems](https://stratagens.com).
