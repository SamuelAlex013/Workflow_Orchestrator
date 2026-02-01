# n8n-nodes-gainium

Integrate Gainium with n8n to manage bots, strategies, and deals directly in your workflows. This package lets you trigger actions, fetch data, and coordinate trading logic with the rest of your automation stack.

## ⚡ Gainium Overview

[Gainium](https://gainium.io) is a platform for building and running automated trading strategies. Key features include:

- Trading terminal
- Grid, DCA, and Combo bots
- Backtesting & paper trading
- Market screener
- Portfolio tracking
- Risk tools & auto-compounding
- Webhook-triggered actions

## 🤖 About n8n

[n8n](https://n8n.io) is a workflow automation tool that connects APIs and services. Use these nodes to tie trading logic to alerts, signals, data sources, or messaging tools—no custom backend required.

---

## 📚 API Documentation

📖 **Complete API Reference:** [https://api.gainium.io/api/docs/](https://api.gainium.io/api/docs/)

> 💡 **Tip:** The interactive API documentation includes detailed endpoint descriptions, request/response examples, and a built-in testing interface to help you understand and implement each feature.

---

## 🚀 What You Can Do

The nodes let you:

- Trigger bots on signals or events
- Monitor deals, positions, and PnL
- Pause, resume, close, or adjust bots and deals
- React to strategy alerts
- Retrieve account and performance data
- Combine with Telegram, Discord, TradingView, etc. for full workflows

---

## 🔧 Use Cases (Examples)

- Rebalance: Fetch balances + external prices, adjust allocations via bot actions.
- News / sentiment trigger: Pause or de-risk bots when negative sentiment spikes.
- Scheduled profit taking: Cron step-down of position size or bot aggressiveness.
- Volatility adaptation: Adjust grid/DCA parameters when volatility changes.
- Arbitrage alerting: Compare prices across exchanges and notify or trigger a deal.
- Chat control: Telegram command interface to pause, resume, or inspect deals.
- Risk rules: Auto close or scale down deals at configured drawdown levels.
- Template deployment: Create bots from stored presets (e.g. Airtable / Notion).
- PnL logging: Push periodic performance snapshots to Sheets or Notion.

---

## 📦 Installation

In your n8n instance or custom Docker setup:

    npm install n8n-nodes-gainium

Then restart your n8n server.

> This is a community node. You’ll need to enable community nodes in your `n8n` settings.

---

## 🔐 Authentication

Set your Gainium API Key in the credentials section of the node. You can create an API key in your Gainium account settings.

---

## **🧩 Nodes Included**

Each Gainium API endpoint has its own dedicated n8n node for maximum flexibility in your workflows.

### **Bots**

- Get Grid Bots — /api/bots/grid
- Get Combo Bots — /api/bots/combo
- Get DCA Bots — /api/bots/dca
- Update DCA Bot — /api/updateDCABot
- Update Combo Bot — /api/updateComboBot
- Change Bot Pairs — /api/changeBotPairs
- Start Bot — /api/startBot
- Clone DCA Bot — /api/cloneDCABot
- Clone Combo Bot — /api/cloneComboBot
- Restore Bot — /api/restoreBot
- Stop Bot — /api/stopBot
- Archive Bot — /api/archiveBot

### **Deals**

- Get Deals — /api/deals
- Update DCA Deal — /api/updateDCADel
- Update Combo Deal — /api/updateComboDeal
- Add Funds to Deal — /api/addFunds
- Reduce Funds from Deal — /api/reduceFunds
- Start Deal — /api/startDeal
- Close Deal — /api/closeDeal/{dealId}

### **User**

- Get User Exchanges — /api/user/exchanges
- Get User Balances — /api/user/balances

### **General**

- Get Supported Exchanges — /api/exchanges
- Get Crypto Screener — /api/screener

More coming soon.

---

## **🧠 Agent Tool**

Provides a unified action/data interface for AI or rule-driven agents (OpenAI, Anthropic, LangChain, etc.) so they can inspect state and invoke supported bot or deal operations dynamically.

---

## 💡 Example Workflows

1. TradingView signal → start bot via webhook
2. De-risk on BTC dominance spike
3. Profit alert when deal closes > X%
4. Screener match → create / notify
5. AI agent adjusts risk or pauses bots
6. Natural language command interface (Telegram / Slack)
7. Adaptive parameter tuning (volatility & volume)

---

## 🙋 Support

Need help or a feature? Open an issue or visit the [community forum](https://community.gainium.io).