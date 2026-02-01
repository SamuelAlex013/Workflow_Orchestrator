# n8n-nodes-volcengine

![n8n.io - Workflow Automation](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

This is an n8n community node package that provides integration with VolcEngine services.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Community Nodes (Recommended)

1. Go to **Settings > Community Nodes**.
2. Select **Install**.
3. Enter `n8n-nodes-volcengine` in **Enter npm package name**.
4. Agree to the [risks](https://docs.n8n.io/integrations/community-nodes/risks/) of using community nodes: select **I understand the risks of installing unverified code from a public source**.
5. Select **Install**.

After installing the node, you can use it like any other node in n8n.

### Manual Installation

To get started install the package in your n8n root directory:

```bash
npm install n8n-nodes-volcengine
```

For Docker-based deployments add the following line before the font installation command in your [n8n Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/n8n.Dockerfile):

```dockerfile
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-volcengine
```

## Supported Services

### ✅ ECS (Elastic Compute Service)
- **Copy Image**: Cross-region image replication with full parameter support
- **Describe Tasks**: Query progress of asynchronous tasks (copy, export, import operations)
  - Support querying by Task IDs or Resource IDs
  - Pagination support for large result sets
  - Real-time task status and progress monitoring

### 🚧 Coming Soon
- **RDS**: Database management
- **CDN**: Content delivery network
- **VPC**: Virtual private cloud
- **CLB**: Cloud load balancer

## Credentials

You need to create VolcEngine API credentials to use this package:

1. Log in to the [VolcEngine Console](https://console.volcengine.com/)
2. Go to **Access Control** > **Access Keys**
3. Create or obtain your AccessKeyId and SecretAccessKey
4. In n8n, create new credentials of type **VolcEngine API**
5. Enter your AccessKeyId, SecretAccessKey, and default Region

## Usage

### Copy Image Example

1. Add the **VolcEngine ECS** node to your workflow
2. Select **Image** as the resource
3. Select **Copy** as the operation
4. Configure the parameters:
   - **Source Image ID**: The ID of the image to copy (e.g., `image-abc123def456789`)
   - **Destination Region**: Target region for the copied image
   - **Target Image Name**: Name for the new image
   - **Description** (optional): Description for the new image
   - **Copy Image Tags** (optional): Whether to copy source image tags
   - **Project Name** (optional): Project name for the image

## Supported Regions

- 华北2（北京）- cn-beijing
- 华东2（上海）- cn-shanghai
- 华南1（广州）- cn-guangzhou
- 西南1（成都）- cn-chengdu
- 华东1（杭州）- cn-hangzhou
- 华东3（南京）- cn-nanjing
- 亚太东南1（新加坡）- ap-singapore
- 亚太东北1（东京）- ap-tokyo
- 美国东部1（弗吉尼亚）- us-east-1
- 美国西部2（俄勒冈）- us-west-2

## API Documentation

For detailed API documentation, please refer to:
- [VolcEngine ECS API Documentation](https://www.volcengine.com/docs/6261/64965)
- [VolcEngine API Authentication](https://www.volcengine.com/docs/6291/65568)

## Development

### Prerequisites

- Node.js 18+
- npm or pnpm
- n8n development environment

### Setup

```bash
# Clone the repository
git clone https://github.com/caiwenhao/n8n-nodes-volcengine.git
cd n8n-nodes-volcengine

# Install dependencies
npm install

# Build the package
npm run build

# Run linting
npm run lint

# Run tests
npm test
```

### Project Structure

```
n8n-nodes-volcengine/
├── credentials/
│   └── VolcEngineApi.credentials.ts
├── nodes/
│   └── VolcEngine/
│       ├── types.ts
│       ├── GenericFunctions.ts
│       ├── volcengine.svg
│       └── ECS/
│           ├── VolcEngineEcs.node.ts
│           ├── ImageDescription.ts
│           ├── VolcEngineEcs.node.json
│           └── ecs.svg
├── dist/                 # Compiled output
├── package.json
├── tsconfig.json
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Guidelines

1. Follow the existing code style
2. Add tests for new features
3. Update documentation as needed
4. Ensure all tests pass before submitting

## License

[MIT](LICENSE.md)

## Support

- [n8n Community Forum](https://community.n8n.io/)
- [VolcEngine Documentation](https://www.volcengine.com/docs/)
- [GitHub Issues](https://github.com/caiwenhao/n8n-nodes-volcengine/issues)

## Changelog

### 1.0.0
- Initial release
- ECS Copy Image functionality
- VolcEngine API authentication
- Support for 10 regions
- Comprehensive error handling

---

**Note**: This is a community-maintained package and is not officially supported by VolcEngine or n8n.io.
