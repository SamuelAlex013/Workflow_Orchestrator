# n8n-nodes-aws-sqs

[![npm version](https://badge.fury.io/js/@nooma-tech%2Fn8n-nodes-aws-sqs.svg)](https://www.npmjs.com/package/@nooma-tech/n8n-nodes-aws-sqs)
[![Test Coverage](https://img.shields.io/badge/coverage-97.29%25-brightgreen)](https://github.com/Nooma-Tech/n8n-nodes-aws-sqs)
[![AWS SDK](https://img.shields.io/badge/AWS%20SDK-v3-orange)](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/)

This is a high-performance n8n community node for AWS SQS integration. Built with AWS SDK v3 for optimal performance and modern JavaScript features.

AWS SQS (Simple Queue Service) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

## Table of Contents

- [Installation](#installation)
- [Operations](#operations)
- [Credentials](#credentials)
- [Usage](#usage)
- [Examples](#examples)
- [Resources](#resources)
- [Version History](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

Install directly from n8n:

1. Go to **Settings** > **Community Nodes**
2. Select **Install** and enter `@nooma-tech/n8n-nodes-aws-sqs`

### Manual Installation

```bash
npm install @nooma-tech/n8n-nodes-aws-sqs
```

The package is published to the public npm registry for easy installation.

## Operations

This package provides 1 node for AWS SQS integration:

### Trigger Nodes

**AWS SQS Trigger**

- 🚀 **High Performance**: Built with AWS SDK v3 for optimal speed and efficiency
- 📊 **Smart Polling**: Configurable intervals (seconds/minutes/hours) with long-polling support
- 🔄 **Batch Processing**: Handle multiple messages efficiently with batch delete operations
- 🎯 **Auto Message Management**: Automatically process and optionally delete messages
- 🏷️ **Rich Metadata**: Full support for message attributes and queue attributes
- 🛡️ **Robust Error Handling**: Comprehensive error handling with detailed logging
- 📈 **High Reliability**: 97.29% test coverage with 34 comprehensive test cases

## Credentials

You need to authenticate with AWS using standard AWS credentials. Prerequisites and setup:

### Prerequisites

1. AWS Account with SQS access
2. IAM user with appropriate SQS permissions

### Credential Setup

1. In n8n, create new credentials of type "AWS"
2. Fill in the required fields:
   - **Region**: Your AWS region (e.g., us-east-1)
   - **Access Key ID**: Your AWS access key
   - **Secret Access Key**: Your AWS secret key
   - **Session Token** (optional): For temporary credentials

### Required IAM Permissions

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"sqs:ListQueues",
				"sqs:ReceiveMessage", 
				"sqs:DeleteMessage",
				"sqs:DeleteMessageBatch",
				"sqs:GetQueueAttributes"
			],
			"Resource": "arn:aws:sqs:*:*:*"
		}
	]
}
```

## Usage

### AWS SQS Trigger

The trigger node polls SQS queues at regular intervals and processes new messages with high performance and reliability.

**✨ Key Features:**
- **Dynamic Queue Selection**: Choose from a dropdown of your AWS SQS queues
- **Smart Polling**: Configurable intervals with units (seconds/minutes/hours)
- **Batch Processing**: Handle 1-10 messages per poll with optimized batch operations
- **Long Polling**: Reduce costs with wait times up to 20 seconds
- **Auto JSON Parsing**: Automatic JSON parsing with fallback to raw text

**⚙️ Configuration Options:**

- **Queue**: Select from your AWS SQS queues (dynamically loaded)
- **Interval**: Polling frequency (1+ with units: seconds/minutes/hours)
- **Delete Messages**: Auto-delete processed messages (default: true)
- **Max Number Of Messages**: Messages per poll (1-10, default: 1)
- **Visibility Timeout**: Hide duration for other consumers (default: 30s)
- **Wait Time Seconds**: Long polling duration (0-20s, default: 0)
- **Message Attribute Names**: Specific attributes to retrieve (default: "All")
- **Attribute Names**: Queue attributes to retrieve (default: "All")

**📤 Output Structure:**
Each message becomes a separate workflow execution with:

- `messageId`: Unique message identifier
- `receiptHandle`: Handle for message deletion/visibility control
- `body`: Raw message body (string)
- `parsedBody`: Automatically parsed JSON (if valid JSON, otherwise same as body)
- `attributes`: Standard SQS message attributes
- `messageAttributes`: Custom message attributes with typed values
- `md5OfBody`: MD5 hash of message body
- `md5OfMessageAttributes`: MD5 hash of message attributes

## Examples

### Basic Message Processing

```json
{
	"nodes": [
		{
			"parameters": {
				"queue": "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue",
				"interval": 5,
				"unit": "seconds",
				"options": {
					"maxNumberOfMessages": 10,
					"deleteMessages": true
				}
			},
			"type": "awsSqsTrigger",
			"position": [200, 300]
		}
	]
}
```

### Advanced Configuration with Long Polling

```json
{
	"nodes": [
		{
			"parameters": {
				"queue": "https://sqs.us-east-1.amazonaws.com/123456789012/my-priority-queue",
				"interval": 30,
				"unit": "seconds",
				"options": {
					"maxNumberOfMessages": 5,
					"visibilityTimeout": 60,
					"waitTimeSeconds": 20,
					"deleteMessages": false,
					"messageAttributeNames": "priority,source,timestamp",
					"attributeNames": "ApproximateReceiveCount,MessageGroupId"
				}
			},
			"type": "awsSqsTrigger",
			"position": [200, 300]
		}
	]
}
```

### High-Frequency Processing with Batch Delete

```json
{
	"nodes": [
		{
			"parameters": {
				"queue": "https://sqs.us-east-1.amazonaws.com/123456789012/high-volume-queue",
				"interval": 1,
				"unit": "seconds",
				"options": {
					"maxNumberOfMessages": 10,
					"visibilityTimeout": 30,
					"waitTimeSeconds": 10,
					"deleteMessages": true,
					"messageAttributeNames": "All",
					"attributeNames": "All"
				}
			},
			"type": "awsSqsTrigger",
			"position": [200, 300]
		}
	]
}
```

## Resources

- [AWS SQS Documentation](https://docs.aws.amazon.com/sqs/)
- [n8n Documentation](https://docs.n8n.io/)
- [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/)

## Version History

### 2.0.0 (2024-12-19) - 🚀 Major Release

#### ⚡ Breaking Changes
- **AWS SDK v3 Migration**: Upgraded from legacy SDK to modern v3 architecture
- **Enhanced Performance**: Reduced bundle size and improved tree-shaking
- **Security Improvements**: Latest AWS SDK with enhanced security features

#### ✨ New Features
- **Complete AWS SDK v3 Integration**: Using `@aws-sdk/client-sqs` v3.705.0
- **Dynamic Queue Loading**: Dropdown selection of AWS SQS queues
- **Enhanced Message Processing**: Improved JSON parsing with intelligent fallback
- **Batch Delete Optimization**: Efficient handling of multiple messages
- **Advanced Configuration**: Granular control over all SQS parameters
- **Better Error Handling**: More descriptive error messages and handling

#### 🧪 Quality Improvements
- **97.29% Test Coverage**: Comprehensive test suite with 34 test cases
- **100% Function Coverage**: All functions thoroughly tested
- **Advanced Testing**: Fake timer testing for async trigger functionality
- **TypeScript Excellence**: Enhanced type safety and definitions
- **Zero Linting Errors**: Strict code quality standards

#### 🔧 Technical Enhancements
- **Memory Leak Prevention**: Proper cleanup of timers and resources
- **Improved Timer Management**: Better handling of polling intervals
- **Resource Cleanup**: Automatic SQS client destruction
- **Modern JavaScript**: ES2022+ features and optimizations
- **Jest Integration**: Professional testing setup without `--forceExit`

### 1.0.0 (2024-12-19) - Initial Release

#### Core Features
- AWS SQS Trigger with polling functionality
- Message processing with JSON parsing
- Configurable polling intervals and timeouts
- Basic error handling and logging
