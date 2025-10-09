![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-emailvalidation

This package provides the EmailValidation community node for [n8n](https://n8n.io). It integrates the [emailvalidation.io API](https://emailvalidation.io) to validate and verify email addresses.

To make your custom node available to the community, you must create it as an npm package, and [submit it to the npm registry](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry).

If you would like your node to be available on n8n cloud you can also [submit your node for verification](https://docs.n8n.io/integrations/creating-nodes/deploy/submit-community-nodes/).

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this starter

These are the basic steps for working with the starter. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your new repo:
   ```
   git clone https://github.com/<your organization>/<your-repo-name>.git
   ```
3. Run `npm i` to install dependencies.
4. Open the project in your editor.
5. Browse the examples in `/nodes` and `/credentials`. Modify the examples, or replace them with your own nodes.
6. Update the `package.json` to match your details.
7. Run `npm run lint` to check for errors or `npm run lintfix` to automatically fix errors when possible.
8. Test your node locally. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) for guidance.
9. Replace this README with documentation for your node. Use the [README_TEMPLATE](README_TEMPLATE.md) to get started.
10. Update the LICENSE file to use your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## EmailValidation Node

Validate and verify email addresses using the `emailvalidation.io` API.

### Credentials

- Create credentials of type `EmailValidation API`.
- Fields:
  - API Key (stored securely)
  - Base URL: defaults to `https://api.emailvalidation.io/v1`

Authentication is sent via query parameter `apikey` (the API also supports header-based auth). See docs: [`https://emailvalidation.io/docs/`](https://emailvalidation.io/docs/).

### Operation

- Validate Email
  - Email (required) — the email address to validate
  - Catch All (optional) — when enabled, sets `catch_all=1` to perform catch-all detection (paid plans)

Per endpoint docs: [`https://emailvalidation.io/docs/info`](https://emailvalidation.io/docs/info)

The node performs a `GET /v1/info` with `email`, optional `catch_all`, and `apikey` query parameters. Example request:

```bash
curl -G "https://api.emailvalidation.io/v1/info" \
  --data-urlencode "email=support@emailvalidation.io" \
  --data-urlencode "apikey=YOUR-API-KEY"
```

### Example Output

```json
{
  "email": "[email protected]",
  "user": "support",
  "tag": "",
  "domain": "emailvalidation.io",
  "smtp_check": true,
  "mx_found": true,
  "did_you_mean": "",
  "role": true,
  "disposable": false,
  "score": 0.64,
  "state": "deliverable",
  "reason": "valid_mailbox",
  "free": false,
  "format_valid": true,
  "catch_all": null
}
```

See documentation for field meanings and state/reason descriptions: [`https://emailvalidation.io/docs/info`](https://emailvalidation.io/docs/info)

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
