![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-searxng-request
This is a custom n8n node for making requests to a SearxNG instance.

## Features

- Make GET requests to a SearxNG instance.
- Supports custom parameters for search queries.
- Supports both `GET` and `POST` methods.
- Handles response data and errors gracefully.
- Supports authentication via API keys.


## Installation

```bash
npm install n8n-nodes-searxng-request
```

## Usage
1. Import the node into your n8n workflow.
2. Configure the node with your SearxNG instance URL.
3. Set the operation to `search` and the method to `GET` or `POST`.
	 - Enter your search query in the `Query` field.
	 - Specify the maximum number of results you want to retrieve in the `Max Results` field.
4. Add any custom parameters you want to include in the search query.
5. Execute the workflow to see the results.

## Configuration

- **SearxNG URL**: The base URL of your SearxNG instance (e.g., `https://your-searxng-instance.com`).
- **Authentication**: If your SearxNG instance requires authentication, provide the necessary API key or credentials.

- **Operation**: The operation to perform, which is `search` for this node.
- **Method**: The HTTP method to use, which can be either `GET` or `POST`. For search operations, `GET` is typically used.
- **Query**: The search query.
- **Max Results**: The maximum number of results to return (default is 10).

- **Custom Parameters**: Any additional parameters you want to include in the search request:
  - `categories`: The categories to search in (e.g., `general`, `images`, `news`).
  - `format`: The response format (e.g., `json`).
  - `language`: The language for the search results.
  - `llmMode`: The mode for LLM (Large Language Model) integration (e.g., `off`, `on`).
  - `pageno`: The page number for paginated results.
  - `safesearch`: The safe search mode (e.g., `off`, `moderate`, `strict`).
  - `time_range`: The time range for the search results (e.g., `day`, `month`, `year`).

## Contributing

## References

- [n8n](https://github.com/n8n-io/n8n)

## License

[MIT](LICENSE.md)
