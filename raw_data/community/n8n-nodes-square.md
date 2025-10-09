![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-square

This is a Square integration node for [n8n](n8n.io) that allows you to interact with the Square API. With this node, you can automate your Square-related workflows and integrate Square's functionality into your n8n automations.

## Features

- Connect to Square API securely
- Manage Square transactions and payments
- Integrate Square functionality into your n8n workflows
- Built with TypeScript for better type safety and developer experience

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js (version 18 or later) and pnpm
* n8n installed globally:
  ```bash
  pnpm install n8n -g
  ```
* A Square developer account and API credentials

## Installation

To install this node in your n8n instance:

```bash
pnpm install n8n-nodes-square
```

## Usage

1. Create a Square developer account if you haven't already
2. Obtain your Square API credentials
3. Add the Square credentials in n8n
4. Use the Square node in your workflows

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/RostamMahabadi/n8n-nodes-square.git
   ```
2. Install dependencies:
   ```bash
   pnpm install
   ```
3. Build the project:
   ```bash
   pnpm build
   ```
4. Link to your n8n installation for testing

## Available Scripts

- `pnpm build`: Build the project
- `pnpm dev`: Watch for changes and rebuild
- `pnpm format`: Format the code
- `pnpm lint`: Check for code issues
- `pnpm lintfix`: Automatically fix code issues when possible

## Support

If you encounter any issues or have questions, please file them in the [issues section](https://github.com/RostamMahabadi/n8n-nodes-square/issues) of this repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](LICENSE.md)

## Author

Rostam Mahabadi (RostamMahabadi@gmail.com)
