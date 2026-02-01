# n8n-nodes-zohopeople

<br />
<p align="center">
    <a href="https://zohopeople.io" target="_blank"><img width="260" height="" src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" alt="zohopeople Logo"></a>
    <br />
    <br />
    <b>Free and open fair-code licensed node based Workflow Automation Tool.</b>
    <br />
    <br />
</p>

<br />
<p align="center">
    <a href="https://zohopeople.io" target="_blank"><img width="150" height="" src="/nodes/ZohoPeople/zohopeople.svg" alt="zohopeople Logo"></a>
    <br />
    <br />
    <b>Zoho People is a cloud-based HR software crafted to nurture employees, quickly adapt to changes, and make HR management agile and effective</b>
    <br />
    <br />
</p>

<p align="center">
    <a href="https://n8n.io" target="_blank"><img width="600" height="" src="/n8n-zohopeople-node.png" alt="zohopeople-node"></a>
    <br />
    <br />
</p>

## How to install

To install a community node in your n8n instance :

- Go to `Settings > Community Nodes` :
- Select `Install a community node`
- Type in `n8n-nodes-zohopeople` and hit `Install`

OR

To get started install the package in your n8n root directory with

`npm install n8n-nodes-zohopeople`

OR

For docker add the following line before the font installation command in your [n8n Docker file](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile)


`RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-zohopeople`

## Features
- Forms
	- Fetch Forms
	- Get Bulk Records
	- Get Record Count
- Attendance
	- Fetch Last Attendnce Entries
	- Shift Details of Employee
- Cases
	- View List of Categories
	- View Case Details
- Leaves
	- Get Leave Types
	- Get Holidays
- Views
	- Default and Custom View
	Fetch View of Specific Form

## Coming Soon
All APIs defined on https://www.zoho.com/people/api/overview.html
For the node-athon it's been READ operations for most of the Resources, later more CRUD operations will be added
## 🔗 Connect with me

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/saad-mujeeb-b730a860)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/SaadMMujeeb)

## License

[Apache 2.0 with Commons Clause](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/LICENSE.md)
