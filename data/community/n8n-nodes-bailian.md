# n8n-nodes-bailian

这是一个用于[n8n](https://n8n.io)的阿里云百炼API节点集合，提供了与阿里云AI大模型服务的集成。

## 功能概览

本节点包含以下功能：

### 文本生图
- 支持阿里云通义万相模型进行文本到图像的生成
- 支持WanXiang 2.1 Turbo和WanXiang 2.0模型
- 支持多种图片尺寸和参数控制

### 文本生视频
- 支持通义万相-文生视频模型，一句话生成视频
- 支持两种不同性能的模型：
  - `wanx2.1-t2v-turbo`：生成速度更快，表现均衡
  - `wanx2.1-t2v-plus`：生成细节更丰富，画面更具质感
- 支持多种视频分辨率：16:9、9:16、1:1、3:4、4:3比例
- 提供Prompt智能改写和随机种子设置

### 任务结果查询
- 支持查询异步任务的执行结果
- 支持单次查询和持续轮询模式
- 针对文生视频等长耗时任务提供优化的查询方式

## Prerequisites

You need the following installed on your development machine:

* [git](https://git-scm.com/downloads)
* Node.js and npm. Minimum version Node 20. You can find instructions on how to install both using nvm (Node Version Manager) for Linux, Mac, and WSL [here](https://github.com/nvm-sh/nvm). For Windows users, refer to Microsoft's guide to [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows).
* Install n8n with:
  ```
  npm install n8n -g
  ```
* Recommended: follow n8n's guide to [set up your development environment](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Using this starter

These are the basic steps for working with the starter. For detailed guidance on creating and publishing nodes, refer to the [documentation](https://docs.n8n.io/integrations/creating-nodes/).

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) from this template repository.
2. Clone your new repo:
   ```
   git clone https://github.com/<your organization>/<your-repo-name>.git
   ```
3. Run `npm i` to install dependencies.
4. Open the project in your editor.
5. Browse the examples in `/nodes` and `/credentials`. Modify the examples, or replace them with your own nodes.
6. Update the `package.json` to match your details.
7. Run `npm run lint` to check for errors or `npm run lintfix` to automatically fix errors when possible.
8. Test your node locally. Refer to [Run your node locally](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/) for guidance.
9. Replace this README with documentation for your node. Use the [README_TEMPLATE](README_TEMPLATE.md) to get started.
10. Update the LICENSE file to use your details.
11. [Publish](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) your package to npm.

## More information

Refer to our [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
