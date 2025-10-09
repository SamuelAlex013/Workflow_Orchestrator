# n8n-nodes-lmstudio-embeddings

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A community n8n node for generating embeddings through LM Studio API with encoding format selection.

## Description

This package provides an n8n node for integration with LM Studio - a local system for running large language models. The node allows generating vector representations (embeddings) of text that can be used for semantic search, recommendation systems, and other machine learning tasks.

## Features

- 🤖 Generate embeddings through LM Studio API
- 🎯 Automatic loading of available models
- 📊 Support for different encoding formats (float, base64)
- 🔧 Simple configuration via n8n credentials
- 🚀 Support for local and remote LM Studio server

## Installation

### Through n8n Community Package Manager

1. Open n8n
2. Go to settings
3. Select "Community Nodes"
4. Install package: `n8n-nodes-lmstudio-embeddings`

## Usage

### Node Parameters

- **Model**: Model for generating embeddings (automatically loaded from LM Studio)
- **Encoding Format**: Format of returned embeddings
  - `float`: Floating point numbers (default)
  - `base64`: Base64 encoding
