# n8n-nodes-gcp-pubsub

This is an n8n community node that provides integration with Google Cloud Pub/Sub messaging service. It allows you to publish and subscribe to messages using Pub/Sub topics and subscriptions in your n8n workflows.

Google Cloud Pub/Sub is a messaging service for exchanging event data among applications and services. It provides reliable, many-to-many, asynchronous messaging between applications.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of Contents

- [Installation](#installation)
- [Nodes](#nodes)
  - [GCP Pub/Sub Publisher](#gcp-pubsub-publisher)
  - [GCP Pub/Sub Subscriber](#gcp-pubsub-subscriber)
- [Credentials](#credentials)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
   ![step1](./docs/install-1.png)
3. Enter `n8n-nodes-gcp-pubsub` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.
   ![step2](./docs/install-2.png)

> **Note:** Feel free to inspect the source code of this package before installing it, ensuring greater transparency and security for your environment.

After installing the node, you can use it like any other node. n8n displays the node in search results in the **Nodes** panel.

## Nodes

This package contains two nodes for working with Google Cloud Pub/Sub:

### GCP Pub/Sub Publisher

The Publisher node allows you to publish messages to a Pub/Sub topic.

#### Parameters

- **Project ID** (required): The Google Cloud Project ID where your Pub/Sub topic exists
- **Topic Name** (required): The name of the Pub/Sub topic to publish messages to

#### Features

- Publishes the entire input data as JSON to the specified topic
- Returns the message ID upon successful publication
- Supports error handling with continue on fail option
- Can be used as a tool in AI workflows

#### Input/Output

- **Input**: Any JSON data that you want to publish to the topic
- **Output**: Original data plus a `result` object containing:
  - `success`: boolean indicating if the message was published successfully
  - `messageId`: the unique identifier of the published message

### GCP Pub/Sub Subscriber

The Subscriber node is a trigger node that listens for messages from a Pub/Sub subscription.

#### Parameters

- **Project ID** (required): The Google Cloud Project ID where your Pub/Sub subscription exists
- **Subscription Name** (required): The name of the Pub/Sub subscription to listen to

#### Features

- Continuously listens for messages from the specified subscription
- Automatically acknowledges messages after processing
- Handles both JSON and text message payloads
- Provides comprehensive message metadata

#### Output

Each received message outputs:
- **id**: The unique message ID
- **attributes**: Message attributes (key-value pairs)
- **data**: The message payload (parsed as JSON if possible, otherwise as string)
- **publishTime**: When the message was published
- **received**: Timestamp when the message was received by the node

## Credentials

Both nodes require Google Cloud Platform Service Account credentials to authenticate with the Pub/Sub service.

### Setting up GCP Service Account

1. **Create or select a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Select an existing project or create a new one

2. **Enable the Pub/Sub API**:
   - In the Cloud Console, go to **APIs & Services > Library**
   - Search for "Cloud Pub/Sub API" and enable it

3. **Create a Service Account**:
   - Go to **IAM & Admin > Service Accounts**
   - Click **Create Service Account**
   - Enter a descriptive name (e.g., "n8n-pubsub-service-account")
   - Add a description for clarity

4. **Grant necessary permissions**:
   Choose one of these permission sets based on your needs:
   - **Pub/Sub Admin** (for full access to all Pub/Sub resources)
   - **Pub/Sub Editor** (for read/write access)
   - Or create a custom role with specific permissions:
     - `pubsub.topics.publish` (for Publisher node)
     - `pubsub.subscriptions.consume` (for Subscriber node)
     - `pubsub.messages.ack` (for message acknowledgment)

5. **Generate and download the key**:
   - Select your service account
   - Go to the **Keys** tab
   - Click **Add Key > Create new key**
   - Select **JSON** format
   - Download the key file

6. **Configure credentials in n8n**:
   - In n8n, go to **Settings > Credentials**
   - Click **Create New Credential**
   - Select **Google Cloud Platform Service Account API**
   - Copy the entire contents of the downloaded JSON file
   - Paste it into the **Service Account JSON** field
   - Save the credential

### Example Service Account JSON Structure

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "service-account@your-project-id.iam.gserviceaccount.com",
  "client_id": "client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account%40your-project-id.iam.gserviceaccount.com"
}
```

### Security Best Practices

- Store the service account JSON securely and never commit it to version control
- Use the principle of least privilege (only grant necessary permissions)
- Regularly rotate service account keys
- Monitor service account usage in the Cloud Console
- Consider using Workload Identity in production environments

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Tested with**: n8n v1.0.0+
- **Node API version**: 1
- **Dependencies**: @google-cloud/pubsub v5.2.0+

## Usage

### Basic Publisher Example

1. Add a **Manual Trigger** or any input node
2. Add the **GCP Pub/Sub Publisher** node
3. Configure the Project ID and Topic Name
4. Select your GCP Service Account credentials
5. The node will publish whatever data flows into it

### Basic Subscriber Example

1. Add the **GCP Pub/Sub Subscriber** trigger node
2. Configure the Project ID and Subscription Name
3. Select your GCP Service Account credentials
4. The workflow will trigger whenever a message is received

### Advanced Usage

**Message Processing Pipeline**:
```
Subscriber → Process Data → Publisher
```

**Error Handling**:
Enable "Continue on Fail" in the Publisher node to handle publishing errors gracefully.

**Message Attributes**:
The Subscriber node provides access to message attributes, which can be used for routing or filtering logic.

### Prerequisites

Before using these nodes, ensure you have:
- A Google Cloud Platform account with billing enabled
- A project with the Pub/Sub API enabled
- At least one Pub/Sub topic and subscription created
- Proper IAM permissions configured

To create topics and subscriptions, you can use the [Google Cloud Console](https://console.cloud.google.com/cloudpubsub) or the `gcloud` CLI tool.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [Google Cloud Pub/Sub documentation](https://cloud.google.com/pubsub/docs)
- [Google Cloud Service Accounts](https://cloud.google.com/iam/docs/service-accounts)
- [Pub/Sub Node.js client library](https://googleapis.dev/nodejs/pubsub/latest/)
