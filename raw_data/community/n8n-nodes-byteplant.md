# n8n-nodes-byteplant

This is an n8n community node. It lets you use Byteplant validation services in your n8n workflows.

Byteplant provides comprehensive validation services for addresses, email addresses, and phone numbers with unparalleled precision in 240+ countries worldwide.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Byteplant Address Validator
- **Validate Address**: Validates and standardizes addresses with geocoding support

### Byteplant Email Validator  
- **Validate Email**: Validates email addresses and checks for deliverability

### Byteplant Phone Validator
- **Validate Phone Number**: Validates phone numbers with extensive or express mode options

## Credentials

To use these nodes, you need to obtain API keys from Byteplant services:

### Prerequisites
1. Sign up for the respective Byteplant service:
   - [Address Validator](https://www.address-validator.net/api.html) - for address validation
   - [Email Validator](https://www.email-validator.net/api.html) - for email validation  
   - [Phone Validator](https://www.phone-validator.net/api.html) - for phone validation

### Authentication Setup
Each node requires its own API key credential:
- **Byteplant Address Validator API**: Enter your address-validator API key
- **Byteplant Email Validator API**: Enter your email-validator API key
- **Byteplant Phone Validator API**: Enter your phone-validator API key

The API keys are passed as query parameters in the requests to the respective Byteplant services.

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: >=20.15
- **Tested with**: Latest n8n versions

## Usage

### Address Validator
The Address Validator node validates and standardizes addresses with the following features:
- **Required fields**: Country Code, Street Address
- **Optional fields**: City, Additional Address Info, Postal Code, State, Street Number, Locale
- **Features**: Geocoding support, output charset selection (UTF-8 or US-ASCII)
- **Timeout**: Configurable between 5-300 seconds (default: 10s)

### Email Validator
The Email Validator node validates email addresses with comprehensive checks:
- **Required fields**: Email Address
- **Features**: Deliverability checking, freemail detection, detailed status codes
- **Timeout**: Configurable between 5-300 seconds (default: 10s)

### Phone Validator
The Phone Validator node validates phone numbers with two validation modes:
- **Required fields**: Phone Number
- **Optional fields**: Country Code, Locale
- **Modes**: 
  - **Extensive**: Comprehensive validation with detailed results
  - **Express**: Fast validation for basic checks
- **Timeout**: Configurable between 5-300 seconds (default: 10s)

All nodes support batch processing and can be used as tools in n8n workflows.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Byteplant Address Validator API](https://www.address-validator.net/api.html)
* [Byteplant Email Validator API](https://www.email-validator.net/api.html)
* [Byteplant Phone Validator API](https://www.phone-validator.net/api.html)
* [Byteplant Website](https://www.byteplant.com/)