# n8n-nodes-alicloud

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![中文文档](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)

This is an n8n community node that allows you to use various Alibaba Cloud services in n8n workflows, including Intelligent Speech Service, Object Storage Service (OSS), and Elastic Compute Service (ECS).

This node supports the following Alibaba Cloud services:
- **Intelligent Speech Service**: Provides speech recognition and speech synthesis capabilities, supporting file transcription for multiple audio formats and text-to-speech conversion
- **Speech Synthesis Service**: Convert text to natural speech with support for multiple voice types, audio formats and parameter adjustments
- **Object Storage Service (OSS)**: Supports file upload, download, list, delete and other operations
- **OSS Signed URL**: Generate temporary access links with support for multiple HTTP methods and custom parameters
- **Elastic Compute Service (ECS)**: Manage cloud server instances

Through this node, you can easily integrate various Alibaba Cloud services into your automated workflows.

[n8n](https://n8n.io/) is a workflow automation platform with [fair-code license](https://docs.n8n.io/reference/license/).

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)  
[Version History](#version-history)  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Alternatively, you can also refer to these [n8n workflow templates](https://github.com/crazyyanchao/n8n-workflow-template).

## Operations

This node supports the following resource types and operations:

### File Transcription Service
- **File Transcription (Complete Workflow)**: Complete process that automatically handles task submission and result polling
- **Submit Task Only**: Only submit transcription task without waiting for results
- **Query Results Only**: Query transcription results for already submitted tasks

### Speech Synthesis Service
- **Speech Synthesis**: Convert text to natural speech with support for multiple voice types and audio formats
  - Support for multiple audio formats: PCM, WAV, MP3
  - Multiple voice options (such as Xiaoyun)
  - Adjustable parameters: volume, speech rate, pitch, etc.
  - Support for subtitle timestamp functionality
  - Multiple output formats: binary data, Base64 encoding, audio files, etc.

### Object Storage Service (OSS)
- **Upload File**: Upload files to OSS storage bucket
- **Download File**: Download files from OSS storage bucket
- **List Objects**: List objects in the storage bucket
- **Delete Object**: Delete specified objects from the bucket

### OSS Signed URL
- **Generate Signed URL**: Generate temporary access links for OSS objects

### Elastic Compute Service (ECS)
- **Query Instances**: Query ECS instance information

## Credentials

To use this node, you need:

1. **Register Alibaba Cloud Account**: Visit [Alibaba Cloud official website](https://www.aliyun.com/) to register an account
2. **Enable Related Services**: Enable the following services based on your usage needs:
   - **Intelligent Speech Service**: For file transcription and speech synthesis functionality
   - **Object Storage Service (OSS)**: For file storage and management
   - **Elastic Compute Service (ECS)**: For cloud server management
3. **Obtain Access Keys**: Create AccessKey ID and AccessKey Secret in the RAM console
4. **Obtain AppKey**: Get the project AppKey in the Intelligent Speech Service console (required for file transcription and speech synthesis)
5. **Configure Permissions**: Ensure the AccessKey has operation permissions for the corresponding services
6. **Configure Credentials**: Configure Alibaba Cloud credentials in n8n

### Authentication Methods
- **AccessKey Authentication**: Use Alibaba Cloud AccessKey ID and Secret for API calls (OSS, ECS, file transcription, speech synthesis)
- **AppKey Authentication**: Use the Intelligent Speech Service project AppKey (required for file transcription and speech synthesis)

## Compatibility

- **Minimum n8n Version**: 1.0.0
- **Node.js Version**: >=22.16
- **Tested Versions**: n8n 1.0.0+

## Resources

* [n8n Community Nodes Documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Alibaba Cloud Intelligent Speech Service Documentation](https://help.aliyun.com/product/30413.html)
* [Alibaba Cloud File Transcription API Reference](https://help.aliyun.com/document_detail/90727.html)
* [Alibaba Cloud Object Storage Service (OSS) Documentation](https://help.aliyun.com/product/31815.html)
* [Alibaba Cloud OSS API Reference](https://help.aliyun.com/document_detail/31947.html)
* [Alibaba Cloud Elastic Compute Service (ECS) Documentation](https://help.aliyun.com/product/25365.html)
* [Alibaba Cloud ECS API Reference](https://help.aliyun.com/document_detail/25484.html)

## Version History

### v0.2.18 (Current Version)
- **Added Speech Synthesis Service Support**
  - Text-to-speech functionality with multiple voice options
  - Support for multiple audio formats: PCM, WAV, MP3
  - Rich parameter adjustments: volume, speech rate, pitch control
  - Support for subtitle timestamp functionality
  - Multiple output formats: binary data, Base64 encoding, audio files, etc.
  - Automatic access token generation and management
  - Complete error handling and logging

### v0.2.0
- **Added OSS Object Storage Service Support**
  - File upload functionality
  - File download functionality
  - Object list query functionality
  - Object deletion functionality
- **Added OSS Signed URL Generation Functionality**
  - Support for multiple HTTP methods (GET, POST, PUT, DELETE)
  - Configurable expiration time
  - Support for custom request headers and query parameters
  - Generate internal and external access URLs
- **Added ECS Elastic Compute Service Support**
  - Instance information query functionality
- **Optimized Node Architecture**
  - Adopted modular resource management
  - Unified error handling mechanism
  - Better code organization structure

### v0.1.0
- Initial version release
- Support for complete file transcription workflow
- Support for separate task submission and result query
- Implementation based on official Alibaba Cloud SDK
- Automatic polling mechanism
- Complete error handling

---

**Note**: Using this node requires a valid Alibaba Cloud account and permissions for the corresponding services. Please ensure compliance with Alibaba Cloud's terms of use and API call limits. Different features require different service permissions, please configure the appropriate access permissions based on actual usage.
