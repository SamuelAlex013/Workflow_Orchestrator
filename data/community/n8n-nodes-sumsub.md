# n8n-nodes-sumsub

This is an **unofficial** n8n community node that provides integration with the Sumsub identity verification API. This node allows you to automate identity verification workflows by connecting n8n to Sumsub's KYC/AML platform.

[Sumsub](https://sumsub.com/) is a comprehensive identity verification platform that helps businesses verify their users' identities and comply with KYC/AML regulations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## ⚠️ Disclaimer

**This project is not affiliated with, endorsed by, or sponsored by Sumsub.** This is an independent community-developed integration. Use this project at your own risk. The author is not responsible for any issues, data loss, or problems that may arise from using this node.

## ⚠️ Fork Notice

This is a fork of [https://github.com/nkt/n8n-nodes-sumsub](https://github.com/nkt/n8n-nodes-sumsub) and is **not backward compatible** with the original repository. The API structure and operations have been reorganized and enhanced.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This node provides two main resources:

### Applicant Resource

- **Create**: Create a new applicant in Sumsub with external user ID, verification level, and optional information (email, phone, sourceKey)
- **Get**: Retrieve complete applicant information including verification status and documents
- **Get Status**: Get current verification status of an applicant (pending, approved, rejected, etc.)
- **Update**: Update applicant information such as email, phone, firstName, or lastName

### SDK Integrations Resource

- **Generate WebSDK Link**: Generate an external WebSDK link for applicant verification with customizable TTL and identifiers

## Credentials

To use this node, you need to configure the following credentials in n8n:

- **App Token**: Your Sumsub application token
- **App Secret**: Your Sumsub application secret key
- **API URL**: The Sumsub API base URL (default: <https://api.sumsub.com>)

You can obtain the App Token and App Secret from your Sumsub dashboard under the API settings.

### Authentication

This node automatically handles Sumsub's required HMAC-SHA256 signature authentication. Each request is signed with your app secret using the proper timestamp and request data, ensuring secure communication with the Sumsub API.

## Compatibility

- **Minimum n8n version**: Compatible with n8n community nodes
- **Node.js version**: Requires Node.js >=20.15
- **n8n API version**: Uses n8n-workflow API version 1

## Usage

### Example Workflows

#### Automated User Onboarding

1. **Trigger**: New user registration webhook
2. **Sumsub Node**: Create applicant with user's email and external ID
3. **Conditional Logic**: Check if applicant was created successfully
4. **Email Node**: Send verification link to user
5. **Wait Node**: Wait for verification completion
6. **Sumsub Node**: Check verification status
7. **Database Node**: Update user status based on verification result

#### Verification Status Monitoring

1. **Schedule Trigger**: Run every hour
2. **Database Node**: Get list of pending applicants
3. **Sumsub Node**: Check status for each applicant
4. **Switch Node**: Route based on verification status
5. **Email/Slack Node**: Notify team of status changes

#### WebSDK Link Generation

1. **HTTP Request Trigger**: User requests verification link
2. **Sumsub Node**: Generate WebSDK link with user ID and level
3. **Return Response**: Send link back to user for verification

### Key Features

- **Comprehensive API Coverage**: Supports all major Sumsub applicant operations
- **Secure Authentication**: Built-in HMAC-SHA256 signature handling
- **Type Safety**: Full TypeScript implementation with proper interfaces
- **Error Handling**: Robust error handling with detailed error messages
- **Flexible Configuration**: Optional parameters for customized workflows

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
- [Sumsub API Documentation](https://developers.sumsub.com/api-reference/)
- [Sumsub Official Website](https://sumsub.com/)
- [n8n Official Website](https://n8n.io/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](LICENSE.md)
