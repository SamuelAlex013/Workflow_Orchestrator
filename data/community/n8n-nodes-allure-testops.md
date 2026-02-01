![Banner image](./docs/imgs/banner.png)

# n8n-nodes-allure-testops

This is an n8n community node. It lets you use [Allure TestOps](https://qameta.io/) in your n8n workflows.

[Allure TestOps](https://qameta.io/) is a test management platform that integrates the processes of test case development, execution, and result analysis into a single system, providing transparency and control throughout all testing phases. It enables teams to centrally track quality metrics, automate reporting through integration with [Allure Framework](https://github.com/allure-framework), and accelerate decision-making via data visualization and collaboration tools.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Table of contents
- [Installation](#installation)  
- [Operations](#operations)  
- [Credentials](#credentials)  <!-- delete if no auth needed -->  
- [Compatibility](#compatibility)  
- [Usage](#usage)  <!-- delete if not using this section -->  
- [Resources](#resources)  
- [Version history](#version-history)  <!-- delete if not using this section -->
- [License](#license)
- [Contributors](#contributors)

## Installation

### NPM
```shell
npm i n8n-nodes-allure-testops
```

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

| Resource | Action | Description| Status |
| -- | -- | -- | -- |
| Project | Create | Create project | ✅ |
|  | Delete | Delete project | ✅ |
|  | Get | Get project details | ✅ |
|  | GetList | Get list of projects | ✅ |
|  | Update | Update project | ✅ |
| Test Case | Create | Create test case | ❌ |
|  | Delete | Delete test case | ❌ |
|  | Get | Get test case details | ❌ |
|  | GetList | Get list of test cases | ❌ |
|  | Update | Update test case | ❌ |
| Launch | Create | Create launch | ❌ |
|  | Delete | Delete launch | ❌ |
|  | Get | Get launch details | ❌ |
|  | GetList | Get list of launches | ❌ |
|  | Update | Update launch | ❌ |
|  | Results | Get launch test results | ❌ |
| Test Result | GetList | Get list of test results | ❌ |
|  | Get | Get test result details | ❌ |
|  | Export | Export test results | ❌ |
| Defect | GetList | Get list of defects | ❌ |
|  | Get | Get defect details | ❌ |
|  | Create | Create defect | ❌ |
|  | Update | Update defect | ❌ |
|  | Delete | Delete defect | ❌ |
| Account | GetList | Get list of users | ❌ |
|  | Get | Get user details | ❌ |
|  | GetGroupList | Get access groups | ❌ |
|  | AddToGroup | Add user from group | ❌ |
|  | DeleteFromGroup | Remove user from group | ❌ |
| Environment | GetList | Get list of environments | ❌ |
|  | Create | Create environment variables | ❌ |
|  | Update | Update environment variables | ❌ |
|  | Delete | Delete environment variables | ❌ |
| Analytic | DashboardList | Get dashboards | ❌ |
|  | Trends | Get automation trends | ❌ |
|  | GroupByStatus | Get grouping by status | ❌ |


## Credentials

- [Allure TestOps API](./docs/credentials.md)

## Compatibility

This integration was tested on versions `N8N 1.104.2` and `Allure TestOps API version 25.3.1`.

> The project structure initially included the ability to expand the list of supported versions. Therefore, if you need a specific version of Allure, you are welcome to [issue](https://github.com/GAKiknadze/n8n-nodes-allure-testops/issues ).

## Usage

<!-- _This is an optional section. Use it to help users with any difficult or confusing aspects of the node._

_By the time users are looking for community nodes, they probably already know n8n basics. But if you expect new users, you can link to the [Try it out](https://docs.n8n.io/try-it-out/) documentation to help them get started._ -->

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [Allure TestOps](https://docs.qameta.io/allure-testops)

## Version history

<!-- _This is another optional section. If your node has multiple versions, include a short description of available versions and what changed, as well as any compatibility impact._ -->

## License
- [Source code](./LICENSE)
- [N8N](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
- [Allure TestOps](https://qameta.io/license-terms/)

## Contributors
![[Contributors](https://github.com/GAKiknadze/n8n-nodes-allure-testops/graphs/contributors)](https://contrib.rocks/image?repo=GAKiknadze/n8n-nodes-allure-testops)
