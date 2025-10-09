# Deezer Node for n8n

This is a custom node for [n8n](https://n8n.io/) that allows you to interact with the Deezer API. With this node, you can perform various actions such as searching for tracks, albums, artists, and playlists, retrieving track details, and more.

## Prerequisites

Before using this node, make sure you have the following:

- An active Deezer account
- Access to the Deezer API (you can obtain this by creating an application on the [Deezer for Developers](https://developers.deezer.com/) website)

## Installation
### User
https://docs.n8n.io/integrations/community-nodes/installation/gui-install/

### Developer
1. Install n8n by following the instructions in the [n8n documentation](https://docs.n8n.io/getting-started/installation).
2. Clone or download this repository.
3. Navigate to the repository folder and run the following command to install the dependencies:

```bash
npm install
```

4. Copy the entire folder `deezer` to your n8n custom nodes folder. The default location for the custom nodes folder is `~/.n8n/custom/`.

## Usage

1. Open n8n in your browser.
2. Create a new workflow or open an existing one.
3. Drag and drop the "Deezer" node from the nodes panel onto the canvas.
4. Double-click on the node to configure it.
5. Click on the credentials field and select "Add new Deezer API credentials".
6. Enter your Deezer API credentials (client ID and client secret) and click "Create".
7. Select the desired operation from the "Operation" dropdown list.
8. Configure the remaining fields based on the selected operation.
9. Click "Execute Node" to run the workflow.

## Credentials

To use the Deezer API node, you need to create Deezer API credentials. Here's how:

1. Open n8n in your browser.
2. Click on the "Credentials" tab in the top menu.
3. Click on the "Create New Credentials" button.
4. Select "Deezer API" from the dropdown list.
5. Enter a name for the credentials (e.g., "Deezer API").
6. Enter your Deezer API client ID and client secret.
7. Click "Create" to save the credentials.

## Node Reference

### Deezer

The Deezer node has the following operations:

- **Search**: Search for tracks, albums, artists, or playlists.
- **Get Track**: Retrieve details for a specific track.
- **Get Album**: Retrieve details for a specific album.
- **Get Artist**: Retrieve details for a specific artist.
- **Get Playlist**: Retrieve details for a specific playlist.
- **Get User**: Retrieve details for a specific user.
- And more...

For detailed information on each operation and their respective input/output parameters, refer to the [Deezer API documentation](https://developers.deezer.com/api).

## Limitations

Please note that this node currently supports a subset of the Deezer API functionality. If you require additional features, feel free to contribute to the project or submit a feature request.

## Support

If you encounter any issues or have any questions, please open an issue in the [GitHub repository](https://github.com/n8n-io/n8n).

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
