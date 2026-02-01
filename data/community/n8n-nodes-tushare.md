# n8n-nodes-tushare

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![中文文档](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)

This is an n8n community node that allows you to use the Tushare API in your n8n workflows.

Tushare is a professional financial data platform that provides API services for financial data such as stocks, funds, futures, and foreign exchange. Through this node, you can easily obtain financial data such as stock quotes, company information, and financial data, and integrate it into your automated workflows.

[n8n](https://n8n.io/) is a workflow automation platform with a [fair-code license](https://docs.n8n.io/reference/license/).

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage Instructions](#usage-instructions)  
[Resources](#resources)  
[Version History](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Additionally, you can also refer to these [n8n workflow templates](https://github.com/crazyyanchao/n8n-workflow-template).

## Operations

This node supports the following operations:

- **API Calls**: Call Tushare API to obtain financial data
- **Parameter Configuration**: Supports both JSON format and individual parameter input methods
- **Data Transformation**: Automatically processes API response data

## Credentials

To use this node, you need:

1. **Register a Tushare Account**: Visit [Tushare official website](https://tushare.pro/) to register an account
2. **Get API Token**: Log in and obtain your API Token in the personal center
3. **Configure Credentials**: Configure Tushare API credentials in n8n, enter your Token

### Authentication Method
- **API Token Authentication**: Use the Token you obtained from the Tushare platform for API calls

## Compatibility

- **Minimum n8n version**: 1.0.0
- **Node.js version**: >=22.16
- **Tested versions**: n8n 1.0.0+

## Usage Instructions

### Basic Configuration

1. **Add Tushare node** to your workflow
2. **Configure Credentials**: Select or create Tushare API credentials
3. **Set API Name**: Enter the Tushare API name to call (such as: stock_company, daily, etc.)
4. **Configure Parameters**: Choose parameter input method (JSON or individual parameters)

### Parameter Configuration

**JSON Mode**:
```json
{
  "offset": 0,
  "limit": 10,
  "ts_code": "000001.SZ"
}
```

**Individual Parameter Mode**:
- Add parameter key-value pairs one by one
- Supports dynamic value input

### Common API Examples

- **Stock Basic Information**: `stock_company`
- **Daily Quotes**: `daily`
- **Financial Indicators**: `income`
- **Company Announcements**: `anns`

### Data Output

The node will return the original response data from the Tushare API, which you can further process in subsequent nodes.

## Resources

* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Tushare Official Documentation](https://tushare.pro/document/1)
* [Tushare API Reference](https://tushare.pro/document/2)

## Version History

### v0.1.x (Current Version)
- Initial version release
- Support for basic Tushare API calls
- Support for both JSON and individual parameter input modes
- Complete credential authentication system

### Planned Features
- Support for more Tushare API endpoints
- Add data caching functionality
- Optimize error handling mechanisms
- Increase batch data processing capabilities

---

**Note**: Using this node requires a valid Tushare account and API Token. Please ensure compliance with Tushare's terms of use and API call limits.
