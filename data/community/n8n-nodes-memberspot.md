
# n8n-nodes-memberspot

  

[![n8n](https://img.shields.io/badge/n8n-1.107.3%2B-brightgreen)](https://n8n.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Memberspot Node](https://img.shields.io/badge/n8n-community--node-FF6D5A)
  

An n8n Community Node for the **Memberspot API**, allowing you to seamlessly integrate your Memberspot instance into n8n workflows.

  

## What is n8n?

  

n8n is an easy-to-use workflow automation tool that connects different apps and services, like Memberspot.

By creating "workflows" between apps, you can automate many manual tasks – saving you and your team valuable time.

  

## ⚖️ Legal Notice

  

This Community Node uses the public Memberspot API and is **not affiliated with, endorsed, or sponsored by Memberspot**.

All trademarks are the property of their respective owners.

  

**Note**: This is a community-developed Node for the Memberspot API. For official support, please contact Memberspot directly.

  

## 🚀 Features

  

-  **5 resources** fully supported (User, Offer, Chapter, Exam, Custom Property)

-  **11+ operations** for maximum flexibility

-  **Dropdown selection** for Offers with live data from `/v1/offers`

-  **TypeScript** implementation for the best developer experience

-  **Simple authentication** via API Key

  

## 📋 Supported Operations

  

### 👤 **User**

  

- List Users

- Find by Email

- Grant Offer by Email (with `firstname`, `lastname`, `email`, `offerId`, `orderId`)

- Set Offer State (active/inactive)

- Set Order State (active/inactive)

- Set Custom Properties

- Delete Users

- List Course Progress

- Get Course Progress (for a specific course)

- Get Login Token

  

### 🎁 **Offer**

  

- Get All Offers

  

### 📚 **Chapter**

  

- Enable Chapter Access

  

### 🛠 **Custom Property**

  

- List Custom User Properties

  

### 📝 **Exam**

  

- List Exam Results

  

## 💡 Example Use Cases

  

### Automated User Management

  

Automatically create new users and assign them offers – without manual work in the Memberspot backend.

  

### E-Commerce Integration

  

Connect Copecart, Digistore, or Stripe via webhook and automatically grant course access in Memberspot after a purchase.

  

### Progress Monitoring

  

Track your users’ learning progress automatically and send personalized reminders or congratulations.

  

### Single-Sign-On Links

  

Generate login links for users via workflow and deliver them by email or messenger.

  

## 🛠️ Installation

  

> You can install **unscoped** or **scoped**. Scoped is recommended.

  

### A) Unscoped (Community Nodes UI)

1. Open **Settings → Community Nodes** in n8n

2. Install: `n8n-nodes-memberspot`

3. Restart n8n

  

### B) Unscoped (manual)

```bash

# inside your n8n data dir (e.g. /home/node/.n8n or a bind-mounted /data)

npm  i  n8n-nodes-memberspot
```

  

### C) Scoped (recommended)

```bash

npm  i  @rjsebening/n8n-nodes-memberspot 

```

  

### D) Docker quickstart

  

```bash

docker  run  -it  --rm  \

--name n8n \

-p  5678:5678  \

-e N8N_CUSTOM_EXTENSIONS="/data/custom" \

-v  ~/.n8n:/data  \

docker.n8n.io/n8nio/n8n

#  Then  inside  the  mounted  /data/custom  dir:

# npm i n8n-nodes-memberspot (or @rjsebening/n8n-nodes-memberspot)

``` 

Restart n8n after installation.

## 🔐 Authentication Setup

  

### Generate an API Key

  

1. Log into your **Memberspot instance**: [https://app.memberspot.de](https://app.memberspot.de/)

2. Go to **Settings → Integrations**

3. Under **API Keys**, click **"Create API Key"**

4. Copy the generated API Key (the secret is only shown **once**)

  

### Configure Credentials in n8n

  

1. Open n8n and go to **Credentials**

2. Click **"New Credential"**

3. Search for **"Memberspot API"**

4. Fill in the fields:

-  **API Key**: your generated secret key

-  **Base URL**: `https://api.memberspot.de` (default)

  

5. Test the connection and save

  

## 📖 Usage

  

### Basic User Operation

1. Add a "Memberspot" Node

2. Select Resource: "User"

3. Select Operation: "Find by Email"

4. Enter the email address

5. Execute the workflow


### Using the Offer Dropdown

  
1. Add a "Memberspot" Node

2. Select Resource: "User"

3. Select Operation: "Grant Offer by Email"

4. Choose the desired offer from the dropdown

5. Fill in firstname, lastname, and email
 

## 🔧 API Reference

  

This Node is based on the **Memberspot API v1.0** and supports all publicly available endpoints.

  

**Base URL**: `https://api.memberspot.de/v1`

**Authentication**: API Key via `X-API-KEY` header

  

Full API documentation available at: [Memberspot API Docs](https://api.memberspot.de/api)

  

## 🤝 Contributing

  

Contributions are welcome! Please follow these guidelines:

  

### Development Setup

  

```bash

# Clone the repository

git  clone  https://github.com/rjsebening/n8n-nodes-memberspot.git

cd  n8n-nodes-memberspot

  

# Install dependencies

npm  install

  

# Compile TypeScript

npm  run  build

  

# Run tests

npm  test  

```

  

### Pull Request Guidelines

  

1.  **Fork** the repository

2. Create a **feature branch** (`git checkout -b feature/amazing-feature`)

3.  **Commit** your changes (`git commit -m 'Add amazing feature'`)

4.  **Push** to the branch (`git push origin feature/amazing-feature`)

5. Open a **Pull Request**

  

### Code Style

  

- Use TypeScript for all new features

- Follow the ESLint configuration

- Add tests for new functionality

- Update documentation

  

## 📝 Changelog

  

### Version 1.0.0 (2025-08-24)

  

#### 🎉 Initial Release

  

- ✅ Full Memberspot API integration

- ✅ 5 resources with 11+ operations

- ✅ Offer dropdown via `/v1/offers`

- ✅ TypeScript implementation

- ✅ Comprehensive error handling

  

## 🛠️ Compatibility

  

-  **n8n Version**: 1.107.3+ (tested with latest)

-  **Node Version**: 14+

-  **TypeScript**: 4.0+

  

## ❓ Support

  

### Reporting Issues

  

For bugs or feature requests, please open a [GitHub Issue](https://github.com/rjsebening/n8n-nodes-memberspot/issues).

  

### FAQ

  

**Q: Can I use multiple Memberspot instances?**

A: Yes, just create multiple credentials with different API keys and base URLs.

  

**Q: Are all API endpoints supported?**

A: This Node covers all public API v1.0 endpoints.

  

**Q: How do I find my Memberspot API base URL?**

A: The default base URL is `https://api.memberspot.de/v1`.

  

⭐ **Like this Node?** Give us a star on GitHub!

  

💡 **Feature request?** Open an issue – we’re always open to improvements!

  

## 📬 About the Author

  

I’m [Rezk Jörg Sebening](https://github.com/rjsebening) – Business Automation Expert (DACH).

I build automation systems & n8n nodes that free agencies, coaches, and consultants from manual work.

  

👉 Follow me on GitHub to stay updated with new DACH-focused integrations.

  
  

## 📋 Disclaimer

  

This unofficial community Node is **not affiliated with, supported, or sponsored by Memberspot**.

It only provides an interface to the publicly available Memberspot API under its terms of use.

  

**Important Notes:**

  

- This Node is developed and maintained by the community

- For issues with the Memberspot API itself, please contact official Memberspot support

- All Memberspot trademarks and logos belong to Memberspot

- This Node only acts as a connector to the public API