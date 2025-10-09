# n8n-nodes-tripadvisor

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

This is an n8n community node. It lets you use Tripadvisor in your n8n workflows.

TripAdvisor is a U.S.-based online travel company that operates a website and mobile app with user-generated content and a comparison shopping website. It also offers online hotel reservations and bookings for transportation, lodging, travel experiences, and restaurants. Its platform features reviews and opinions about accommodations, restaurants, experiences, airlines and cruises.

[Installation](#installation)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Resources](#resources)  
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings** > **Community Nodes.**
2. Select **Install.**
3. Find the node you want to install:

   a.) Select **Browse**. n8n takes you to an npm search results page, showing all npm packages tagged with the keyword `n8n-community-node-package`.

   b.) Browse the list of results. You can filter the results or add more keywords.

   c.) Once you find the package you want, make a note of the package name. If you want to install a specific version, make a note of the version number as well.

   d.) Return to n8n.

4. Enter the npm package name, and version number if required.
5. Agree to the risks of using community nodes: select I understand the risks of installing unverified code from a public source.
6. Select Install. n8n installs the node, and returns to the Community Nodes list in Settings.

## Credentials

The Content API uses API Keys to authenticate requests. All API requests must be made over https.

Follow these steps to obtain an API key:

1. Go to [www.tripadvisor.com/developers](www.tripadvisor.com/developers)
2. Sign up for a Tripadvisor account
3. Click [Create API key](https://www.tripadvisor.com/developers?screen=credentials)

### API Key Security

Please safeguard your access key. To include it with each request, set it as the value of the "key" query parameter. If you need to make API calls from client code, be aware this may expose your key to other scripts and browser extensions on the client.

Tripadvisor reserves the right to revoke an access key at any time and issue a new one if a key has leaked or is being misused.

## Compatibility

Tested successfully with:

- n8n Version: 1.32.2
- Node Version: 18.19.1
- npm Version: 10.5.0
- No extra packages required

## Resources

- [n8n Website](https://n8n.io/)
- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Tripadvisor Website](https://www.tripadvisor.com/)
- [Tripadvisor API documentation](https://tripadvisor-content-api.readme.io/reference/overview)

## Version history

- `1.0.0` Initial release
