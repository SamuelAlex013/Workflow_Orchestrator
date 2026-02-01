# n8n-nodes-TacticalRMMAPI

Custom n8n nodes for interacting with the Tactical RMM API, including support for Agents and Alerts.

## ⚠️ Disclaimer
This project is **still under development**. The nodes currently support the basic functionalities for Agents and Alerts, but **require further refinement and testing**. Use at your own risk, and feel free to contribute to the improvement of this repository!

---

## Features

### Tactical RMM Agents Node
- **Fetch Agents**:
  - Get all agents
  - Get an agent by ID
- **Manage Agents**:
  - Update agent details
  - Delete agents
  - Reboot agents
  - Run scripts on agents
- **Additional Operations**:
  - Fetch agent event logs
  - Post tasks, commands, or checks to agents
  - Retrieve agent history

### Tactical RMM Alerts Node
- **Manage Alerts**:
  - Create, update, delete alerts
  - Fetch alerts by ID
  - Bulk alerts management
- **Alert Templates**:
  - Create, update, delete templates
  - Fetch templates and related templates

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/n8n-nodes-TacticalRMMAPI.git
