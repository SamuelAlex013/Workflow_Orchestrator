# n8n-nodes-fractalforge

An n8n custom node for integrating with the Fractal Forge platform. This node enables you to perform commands and queries on your Fractal Forge entities directly within your n8n workflows.

## Features

- **Query Operations**: List objects, get specific objects, and execute custom queries
- **Command Operations**: Create, update, delete objects, and execute custom commands
- **Dynamic Entity Loading**: Automatically loads available entity collections from your Fractal Forge instance
- **Flexible Authentication**: Supports API key authentication with configurable endpoints

## Prerequisites

- n8n installation
- Access to a Fractal Forge platform instance
- Valid Fractal Forge API credentials

## Installation

Install the package in your n8n instance:

```bash
npm install n8n-nodes-fractalforge
```

## Configuration

### Credentials

You'll need to configure the `fractalForgeApi` credentials with:
- **API Endpoint**: Your Fractal Forge API base URL (required)
- **API Key**: Your Fractal Forge application API key (stored securely as a password field)

The node uses Bearer token authentication, automatically adding the `Authorization: Bearer <your-api-key>` header to all requests.

### Node Configuration

The node supports two main resource types:

#### Query Operations
- **List**: Retrieve multiple objects from a collection
- **Get**: Retrieve a specific object by ID
- **Custom Collection Query**: Execute custom queries on collections
- **Custom Object Query**: Execute custom queries on specific objects

#### Command Operations
- **Create**: Create new objects (with optional ID specification)
- **Update**: Modify existing objects
- **Delete**: Remove objects
- **Custom Collection Command**: Execute custom commands on collections
- **Custom Object Command**: Execute custom commands on specific objects

## Usage Examples

### Listing Objects
1. Select "Query" as the resource
2. Choose "List" operation
3. Select your entity collection
4. Execute to retrieve all objects

### Creating Objects
1. Select "Command" as the resource
2. Choose "Create" operation
3. Select your entity collection
4. Provide JSON data in the JSON Body field
5. Optionally specify an Object ID

### Custom Operations
The node supports custom commands and queries for advanced operations specific to your Fractal Forge implementation.

## Documentation

For more information about Fractal Forge, visit: https://fractalforge.dev

## License

[MIT](LICENSE.md)
