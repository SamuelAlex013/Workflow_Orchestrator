# @winth03/n8n-nodes-minio

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/winth03/n8n-nodes-minio/npm-publish.yml)](https://github.com/winth03/n8n-nodes-minio/actions)
[![NPM Version](https://img.shields.io/npm/v/%40winth03%2Fn8n-nodes-minio)](https://www.npmjs.com/package/@winth03/n8n-nodes-minio)
[![NPM Downloads](https://img.shields.io/npm/dm/%40winth03%2Fn8n-nodes-minio)](https://www.npmjs.com/package/@winth03/n8n-nodes-minio)
[![NPM License](https://img.shields.io/npm/l/%40winth03%2Fn8n-nodes-minio)](https://github.com/winth03/n8n-nodes-minio/blob/master/LICENSE.md)
[![NPM Last Update](https://img.shields.io/npm/last-update/%40winth03%2Fn8n-nodes-minio)](https://www.npmjs.com/package/@winth03/n8n-nodes-minio)
[![MinIO Dependency](https://img.shields.io/npm/dependency-version/%40winth03%2Fn8n-nodes-minio/minio)](https://www.npmjs.com/package/@winth03/n8n-nodes-minio)

This is an n8n community node. It lets you use MinIO in your n8n workflows.

[MinIO](https://github.com/minio/minio) is a high-performance, S3-compatible object storage system designed for large scale AI/ML, data lake and database workloads.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Or install it manually:

```bash
npm install @winth03/n8n-nodes-minio
```

## Operations

The MinIO node supports the following operations:

### Bucket Operations
- **List** - List all buckets owned by the authenticated user
- **Make** - Create a new bucket with the specified name
- **Remove** - Remove an empty bucket
- **Exists** - Check if a bucket exists and is accessible

### Object Operations
- **List** - List all objects in a bucket
- **Get** - Download an object from a bucket as binary data
- **Put** - Upload an object to a bucket from binary data
- **Remove** - Remove an object from a bucket
- **Stat** - Retrieves metadata about an object in the specified bucket

### Presigned URL Operations
- **Get** - Generate a presigned URL for downloading an object (7-day expiry)
- **Put** - Generate a presigned URL for uploading an object (7-day expiry)

## Credentials

To use this node, you need to set up MinIO API credentials with the following information:

### Prerequisites
- Access to a MinIO server (self-hosted or cloud service)
- Valid access key and secret key with appropriate permissions

### Required Credential Fields
- **Endpoint** - The MinIO server endpoint (e.g., `localhost` or `play.min.io`)
- **Port** - The port number (typically `9000` for MinIO)
- **Use SSL** - Whether to use HTTPS/SSL connection
- **Access Key** - Your MinIO access key
- **Secret Key** - Your MinIO secret key

### Setting Up Credentials
1. In n8n, go to **Credentials** and click **Add Credential**
2. Search for "MinIO API" and select it
3. Fill in your MinIO server details
4. Test the connection to ensure it works
5. Save the credential

## Compatibility

- **Minimum n8n version**: 0.174.0
- **Node.js version**: >= 20.15.0
- **Tested with n8n versions**: 1.0.0+

This node uses the official MinIO JavaScript SDK and is compatible with:
- MinIO servers (any version)
- Amazon S3 (due to S3 compatibility)
- Any S3-compatible storage service

## Usage

### Basic Workflow Examples

#### Listing Buckets
1. Add the MinIO node to your workflow
2. Select **Bucket** as the resource
3. Select **List** as the operation
4. Configure your MinIO credentials
5. Execute to get a list of all buckets

#### Uploading a File
1. Use an input node to provide binary file data
2. Add the MinIO node
3. Select **Object** as the resource
4. Select **Put** as the operation
5. Specify the bucket name and object name
6. Configure the field name containing your binary data

#### Downloading a File
1. Add the MinIO node
2. Select **Object** as the resource
3. Select **Get** as the operation
4. Specify the bucket name and object name
5. The file content will be available as binary data in the specified field

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [MinIO Documentation](https://min.io/docs/)
* [MinIO JavaScript SDK](https://github.com/minio/minio-js/blob/master/docs/API.md)
* [GitHub Repository](https://github.com/winth03/n8n-nodes-minio)
