# n8n-nodes-nvidia-nim

![n8n.io - Workflow Automation](https://img.shields.io/badge/n8n-workflow%20automation-FF6D5A.svg)
![npm version](https://img.shields.io/npm/v/n8n-nodes-nvidia-nim.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

n8n community node for **NVIDIA NIM** - Chat completions and image analysis with NVIDIA AI models.

## 📋 Requirements

- **n8n** version 1.0.0 or higher
- **Node.js** v18.17.0 or higher
- **NVIDIA NGC API Key** - Get yours at [ngc.nvidia.com](https://ngc.nvidia.com)

## 📦 Installation

### Via n8n Community Nodes (Recommended):

1. Go to **Settings** → **Community Nodes**
2. Click **Install**
3. Enter: `n8n-nodes-nvidia-nim`
4. Restart n8n after installation

### Via npm:

```bash
npm install n8n-nodes-nvidia-nim
```

## ⚙️ Setup

1. **Get NVIDIA API Key**: [ngc.nvidia.com](https://ngc.nvidia.com)
2. **Add Credentials** in n8n:
   - Go to **Credentials** → **New**
   - Select **NVIDIA NIM API**
   - Enter API Key and Base URL: `https://integrate.api.nvidia.com/v1`

## 🎯 Basic Usage

### Text Chat

1. Add "NVIDIA NIM" node → Configure model (e.g., `meta/llama3-8b-instruct`)
2. Connect: Trigger → NVIDIA NIM (main)
3. Execute workflow

### Image Analysis

1. Add "NVIDIA NIM Image Analysis" node → Configure vision model (e.g., `meta/llama-3.2-11b-vision-instruct`)
2. Provide image data (URL, base64, or data URL) and analysis prompt
3. Connect: Trigger → NVIDIA NIM Image Analysis (main)
4. Execute workflow

## 🤖 Available Models

### Text Models

- `meta/llama3-8b-instruct` ⭐ (recommended)
- `meta/llama3-70b-instruct`
- `meta/llama3-405b-instruct`
- `mistralai/mixtral-8x7b-instruct-v0.1`

[View all models →](https://docs.nvidia.com/nim/)

### Vision Models

- `meta/llama-3.2-11b-vision-instruct` ⭐ (recommended)
- `meta/llama-3.2-90b-vision-instruct`

[View all vision models →](https://docs.nvidia.com/nim/)

## ⚙️ Configuration

**Key Parameters**:
- **Model**: Choose from NVIDIA models
- **Temperature**: 0.0-2.0 (default: 0.7)
- **Max Tokens**: Response length (default: 1024)
- **Top P**: Nucleus sampling (default: 1.0)

## 📚 Resources

- [CHANGELOG](./CHANGELOG.md) - Version history
- [GitHub Repository](https://github.com/Akash9078/n8n-nodes-nvidia-nim)
- [npm Package](https://www.npmjs.com/package/n8n-nodes-nvidia-nim)
- [NVIDIA NIM Docs](https://docs.nvidia.com/nim/)

## 🤝 Contributing

Issues and PRs welcome on [GitHub](https://github.com/Akash9078/n8n-nodes-nvidia-nim)

---

Made by [Akash Kumar Naik](https://github.com/Akash9078)
