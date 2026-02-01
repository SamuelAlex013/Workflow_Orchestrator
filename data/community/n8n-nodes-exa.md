![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-exa

This is an n8n community node for interacting with the [Exa API](https://docs.exa.ai/). It provides functionality to search, find similar content, get content, and get answers using Exa's powerful AI capabilities.

## Installation

Follow these steps to install this node in your n8n instance:

1. Go to **Settings > Community Nodes**
2. Select **Install Another Node**
3. Enter `n8n-nodes-exa`
4. Click **Install**

Alternatively, you can install it using npm:

```bash
npm install n8n-nodes-exa
```

## Operations

The Exa node supports the following operations:

### Search

- **Search**: Search for content across the web
- **Search and Get Contents**: Search and retrieve the content of the results

Additional options:
- Use autoprompt
- Number of results
- Date filters
- Domain filters

### Find Similar

- **Find Similar**: Find content similar to a given URL
- **Find Similar and Get Contents**: Find similar content and retrieve it

Additional options:
- Exclude source domain
- Number of results

### Get Content

- **Get Contents**: Get the content of specified URLs

### Answer

- **Get Answer**: Get an AI-generated answer to a question

Additional options:
- Include source text
- Choose model (Default or Exa Pro)

## Credentials

To use this node, you need an Exa API key. You can get one by:

1. Going to [Exa's website](https://exa.ai)
2. Creating an account
3. Getting your API key from the dashboard

## Example Usage

1. **Simple Search**
   - Add the Exa node
   - Select "Search" as the resource
   - Enter your search query
   - Run the workflow

2. **Find Similar Content**
   - Add the Exa node
   - Select "Find Similar" as the resource
   - Enter the URL you want to find similar content for
   - Run the workflow

3. **Get Answer with Sources**
   - Add the Exa node
   - Select "Answer" as the resource
   - Enter your question
   - Enable "Include Text" in additional fields to get source information
   - Run the workflow

## Resources

- [Exa API Documentation](https://docs.exa.ai/)
- [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/community-nodes/)

## License

[MIT](LICENSE.md)
