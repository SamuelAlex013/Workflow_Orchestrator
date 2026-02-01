![Banner image](https://github.com/BuildForCare/n8n-nodes-ksaar/blob/main/baniere_bfc_ksaar_n8n.png?raw=true)

# n8n-nodes-ksaar

## Features

### API

<!-- <style>
    .method-get {
        border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;
    }
    .method-patch {
        border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #20807D; color: #FFFFFF; font-weight: bold;
    }
    .method-post {
        border-radius: 20px;
        display: inline-block;
        padding-left: 8px;
        padding-right: 8px;
        text-align: center;
        background-color: #20807D;
        color: #FFFFFF;
        font-weight: bold;
    }
    .method-delete {
        border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #F04419; color: #FFFFFF; font-weight: bold;
    }
</style> -->
<table style="width: 100%">
    <caption>:white_check_mark: Done&nbsp;&nbsp;&nbsp;&nbsp;:x: Not planned&nbsp;&nbsp;&nbsp;&nbsp;:first_quarter_moon: Planned</caption>
    <header>
        <tr>
            <td><b>Name</b></td>
            <td style="text-align: center;"><b>Method</b></td>
            <td><b>API</b></td>
            <td style="width: 5%;">&nbsp;</td>
        </tr>
    </header>
    <tbody>
        <tr>
            <td colspan="4">Users</td>
        </tr>
        <tr>
            <td>Get user information</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/users/<span style="color: #20807d;">{id}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Update user information</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #20807D; color: #FFFFFF; font-weight: bold;">PATCH</span></td>
            <td>/v1/users/<span style="color: #20807d;">{id}</span></td>
            <td>:first_quarter_moon:</td>
        </tr>
        <tr>
            <td colspan="4">Applications</td>
        </tr>
        <tr>
            <td>Get applications</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/applications</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get application workflows</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/applications/<span style="color: #20807d;">{id}</span>/workflows</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get application users</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/applications/<span style="color: #20807d;">{id}</span>/users</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get application user by email</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/applications/<span style="color: #20807d;">{id}</span>/users/email/<span style="color: #20807d;">{email}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get application user fields</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/applications/<span style="color: #20807d;">{id}</span>/users/fields</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td colspan="4">Worflows</td>
        </tr>
        <tr>
            <td>Get workflow records</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/workflows/<span style="color: #20807d;">{id}</span>/records</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get workflow fields</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/workflows/<span style="color: #20807d;">{id}</span>/fields</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td colspan="4">Records</td>
        </tr>
        <tr>
            <td>Get record</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Create record</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #20807D; color: #FFFFFF; font-weight: bold;">POST</span></td>
            <td>/v1/workflows/<span style="color: #20807d;">{id}</span>/records</td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Update record</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #20807D; color: #FFFFFF; font-weight: bold;">PATCH</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Delete record</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #F04419; color: #FFFFFF; font-weight: bold;">DELETE</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Get record file</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #6ad0dd; color: #383838;  font-weight: bold;">GET</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span>/file/<span style="color: #20807d;">{fieldId}</span></td>
            <td>:x:</td>
        </tr>
        <tr>
            <td>Upload record file</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #20807D; color: #FFFFFF; font-weight: bold;">POST</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span>/file/<span style="color: #20807d;">{fieldId}</span></td>
            <td>:white_check_mark:</td>
        </tr>
        <tr>
            <td>Delete record'file</td>
            <td style="text-align: center;"><span style="border-radius: 20px; display: inline-block; padding-left: 8px; padding-right: 8px; text-align: center; background-color: #F04419; color: #FFFFFF; font-weight: bold;">DELETE</span></td>
            <td>/v1/records/<span style="color: #20807d;">{id}</span>/file/<span style="color: #20807d;">{fieldId}</span>/<span style="color: #20807d;">{fileId}</span></td>
            <td>:first_quarter_moon:</td>
        </tr>
    </tbody>
</table>

## Test the node
You can test your node as you build it by running it in a local n8n instance.

### Install n8n using npm
```bash
npm install n8n -g
```

### Clone git repository
```bash
git clone https://github.com/BuildForCare/n8n-nodes-ksaar.git
cd n8n-nodes-ksaar/
```

### Publish it locally
```bash
# In the node directory
npm run build
npm link
```

### Install the node into your local n8n instance
```bash
# In the nodes directory within your n8n installation
npm link n8n-nodes-ksaar
```
> Make sure you run <b>npm link n8n-nodes-ksaar</b> in the nodes directory within your n8n installation. This is probably something like <b>~/.n8n/nodes/</b>

## More information

Refer to N8N's [documentation on creating nodes](https://docs.n8n.io/integrations/creating-nodes/) for detailed information on building your own nodes.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)
