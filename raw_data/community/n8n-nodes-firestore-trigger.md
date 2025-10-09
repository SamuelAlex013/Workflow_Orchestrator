# n8n-nodes-firestore-trigger

[![Build Status](https://github.com/mrcodepanda/n8n-nodes-firestore-trigger/actions/workflows/main.yml/badge.svg)](https://github.com/mrcodepanda/n8n-nodes-firestore-trigger/actions/workflows/main.yml)
[![npm version](https://img.shields.io/npm/v/n8n-nodes-firestore-trigger.svg)](https://www.npmjs.com/package/n8n-nodes-firestore-trigger)
[![License](https://img.shields.io/npm/l/n8n-nodes-firestore-trigger.svg)](https://github.com/mrcodepanda/n8n-nodes-firestore-trigger/blob/master/LICENSE.md)

This is an n8n community node. It lets you use Firebase Firestore in your n8n workflows as a trigger source.

Firebase Firestore is a flexible, scalable NoSQL cloud database that lets you store and sync data between your users in real-time. This node allows you to listen for changes in your Firestore database and automatically trigger workflows when data is added, modified, or removed.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Self-hosted n8n:

- Go to `Settings` by clicking on 3-dots at the bottom left.
- Navigate to `Community Nodes` section on the left.
- Click on `Install` or `Add Community Nodes` button.
- Type `n8n-nodes-firestore-trigger`, accept the disclaimer and click `Install`.

The trigger node will now be available in your n8n instance by searching for `Firestore`.

### Locally hosted n8n instance:

```bash
# Install from npm
pnpm add n8n-nodes-firestore-trigger

# Alternatively, for local development:
cd ~/.n8n/custom/
pnpm link /path/to/n8n-nodes-firestore-trigger
```

Restart n8n after installation.

## Operations

The Firestore Trigger node supports the following operations:

| Operation | Description |
|-----------|-------------|
| Listen to Collection | Listen for changes to documents in a collection |
| Listen to Document | Listen for changes to a specific document |

### Collection Listeners
When listening to a collection, you can:

- Monitor all documents in a collection or subcollection
- Filter which events trigger the workflow (Added, Modified, Removed)
- Use query filters to only trigger on specific document changes
- Monitor nested subcollections using path patterns (e.g., "users/:userId/orders")
- Use dynamic expressions in path segments for flexible data access

### Document Listeners
When listening to a specific document, you can:

- Monitor a single document for any changes
- Include metadata changes if needed
- Get the complete document data when it changes

## Credentials

To use this node, you need Firebase Admin SDK credentials:

### Prerequisites:
1. A Firebase project with Firestore enabled
2. A service account with appropriate permissions

### Steps to obtain credentials:
1. Go to your [Firebase Console](https://console.firebase.google.com/)
2. Navigate to Project Settings > Service Accounts
3. Click "Generate new private key"
4. Download the JSON file containing your service account credentials

### Setting up in n8n:
1. In your n8n instance, go to the Credentials tab
2. Click "Create New Credentials"
3. Select "Firebase Admin API"
4. Choose Authentication Method:
   - Service Account JSON: Paste the contents of your JSON credentials file
   - Application Default Credentials: For testing with emulator or environment-based auth
5. Enter your Firebase Project ID
6. Optionally specify a Database ID (leave as "(default)" for standard setup)
7. Save your credentials

## Compatibility

- Requires n8n version 0.209.0 or later
- Compatible with Firebase Admin SDK v13.0.0 and later
- Tested with Firestore database in Native mode

## Usage

### Basic Collection Monitoring

To monitor all changes to a collection:

1. Add the Firestore Trigger node to your workflow (Note: The node appears as "Firestore" in the UI rather than "Firestore Trigger")
2. Select "Listen to Collection" operation
3. Enter the collection path (e.g., "users")
4. Select which events to trigger on (Added, Modified, Removed)
5. Save and activate the workflow

The workflow will execute whenever documents in the collection are added, modified, or removed.

### Monitoring a Specific Document

To monitor a specific document:

1. Add the Firestore Trigger node to your workflow
2. Select "Listen to Document" operation
3. Enter the collection path (e.g., "orders")
4. Enter the document ID (e.g., "order-123")
5. Save and activate the workflow

The workflow will execute whenever the specified document changes.

### Using Query Filters

To only trigger the workflow for specific documents:

1. Add the Firestore Trigger node to your workflow
2. Select "Listen to Collection" operation
3. Enter the collection path
4. Under "Options" > "Query Filters", add one or more filters:
   - Field: The document field to filter on
   - Operator: Comparison operator (==, !=, >, >=, <, <=, array-contains)
   - Value: The value to compare against
5. Save and activate the workflow

The workflow will only execute for documents that match the filter criteria.

### Monitoring Subcollections

To monitor a subcollection:

1. Add the Firestore Trigger node to your workflow
2. Select "Listen to Collection" operation
3. Enter the path including the subcollection (e.g., "users/user-123/orders")
4. Select which events to trigger on
5. Save and activate the workflow

### Using Path Patterns

To dynamically monitor subcollections across multiple documents:

1. Add the Firestore Trigger node to your workflow
2. Select "Listen to Collection" operation
3. Enter a path with a parameter (e.g., "users/:userId/orders")
   - The `:userId` parameter will match any document ID in the users collection
4. Select which events to trigger on
5. Save and activate the workflow

This creates a dynamic listener that will monitor the "orders" subcollection under any document in the "users" collection.

### Node Output

When a document change triggers the workflow, the node outputs the following data:

```json
{
  "id": "document-id",
  "data": {
    // Document fields and values
  },
  "changeType": "added | modified | removed",
  "path": "collection/document-id",
  "metadata": {
    "hasPendingWrites": false,
    "fromCache": false
  },
  "timestamp": 1715501234567
}
```

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Firebase Firestore documentation](https://firebase.google.com/docs/firestore)
* [Firebase Admin SDK documentation](https://firebase.google.com/docs/admin/setup)
* Testing documentation can be found in the `tests/docs/` folder

## Version history

### Version 1.0.0
- Initial release
- Support for collection and document listeners
- Support for event filtering (added, modified, removed)
- Support for query filters
- Support for subcollection monitoring
- Support for path patterns with parameters
- Support for metadata changes

### Known Issues

1. **Node Display Name**: When installed in n8n, the node may appear as "Firestore" rather than "Firestore Trigger" in the node selection menu. This is a known issue and doesn't affect functionality.
2. **Delete Events**: Delete events may not be consistently triggered during testing, especially in the emulator environment. This primarily affects document deletion notifications in nested collection patterns.
