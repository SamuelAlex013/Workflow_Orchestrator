# n8n Instagram Scraper Node

![n8n Logo Placeholder](https://via.placeholder.com/150/0000FF/FFFFFF?text=n8n+Logo) ![Instagram Logo Placeholder](https://via.placeholder.com/150/FF00FF/FFFFFF?text=Instagram+Logo)

This custom n8n node allows you to scrape public Instagram profiles to extract post information, primarily focusing on the text content (captions). It's built using the `@aduptive/instagram-scraper` library and is designed for easy integration into your n8n workflows.

**Disclaimer**: Scraping Instagram is against their terms of service. This tool should be used for educational purposes only. Be aware that Instagram frequently updates its website, which can break scrapers like this one.

## Features

*   **Scrape Public Profiles**: Extract data from any public Instagram profile.
*   **Get Post Captions**: Focuses on retrieving the text content of posts.
*   **Configurable Limit**: Specify the number of recent posts to retrieve.
*   **Easy to Use**: Simple interface within n8n.

## Installation

To install this node in your local n8n instance:

1.  **Clone this repository**:
    ```bash
    git clone git@github.com:pinedamg/n8n-nodes-instagram-scraper.git
    cd n8n-nodes-instagram-scraper
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Build the node**:
    ```bash
    npm run build
    ```

4.  **Link the package locally**:
    ```bash
    npm link
    ```

5.  **Install the node into your n8n instance**:
    Navigate to your n8n custom nodes directory (e.g., `~/.n8n/custom/` or as configured by `N8N_CUSTOM_EXTENSIONS`) and link the package:
    ```bash
    npm link n8n-nodes-instagram-scraper
    ```

6.  **Start n8n**:
    ```bash
    n8n start
    ```

Once n8n starts, you should be able to find "Instagram Scraper" in the nodes panel.

## Usage

1.  Drag and drop the "Instagram Scraper" node into your workflow.
2.  Configure the node:
    *   **Username**: Enter the username of the public Instagram profile you want to scrape (e.g., `buenosairesparachicos`).
    *   **Limit**: (Optional) Specify the maximum number of posts to retrieve. Default is 20.
3.  Run the workflow. The node will output a JSON array containing the scraped post data, including the `caption` for each post.

## Development

If you want to contribute or modify this node:

*   **`npm run dev`**: Watch for changes and recompile automatically.
*   **`npm run lint`**: Check code for linting errors.
*   **`npm run lintfix`**: Automatically fix linting errors.

## License

This project is licensed under the MIT License.