# n8n Community Node: HiBob

This is an n8n community node for interacting with the HiBob API. HiBob is a modern HR platform that helps fast-growing companies manage their people and culture.

This node allows you to automate HR workflows by connecting HiBob to other applications and services within your n8n workflows.

## Features

*   **Metadata Resource**:
    *   **Get All Employee Fields**: Retrieve metadata about all available employee fields.
*   **People Resource**:
    *   **Search for Employees**: Search and retrieve employee data.
        *   Optionally specify which employee fields to return.
        *   Control the format of human-readable values in the response (append to or replace machine-readable values).
        *   Optionally include inactive employees in the search results.
        *   Filter employees based on specific field values and conditions using a JSON filter.

## Prerequisites

*   An active HiBob account.
*   A Service User ID and Token from your HiBob account with the necessary permissions for the API actions you intend to perform. (Refer to [HiBob API Service Users Documentation](https://apidocs.hibob.com/docs/api-service-users) for more details on permissions).

## Installation

Follow the [n8n community node installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) to install this node.

1.  Go to **Settings > Community Nodes**.
2.  Select **Install**.
3.  Enter `n8n-nodes-hibob` in the **Enter npm package name** field.
4.  Agree to the risks of using community nodes.
5.  Click **Install**.

After installing the node, you can use it in your n8n workflows.

## Configuration

To use this node, you need to configure HiBob API credentials in n8n:

1.  In your n8n workflow, add the "HiBob" node.
2.  In the node's properties panel, click on the "Credential" dropdown.
3.  Select "Create New".
4.  Enter a **Credential Name**.
5.  Fill in the **Service User ID** and **Service User Token** obtained from your HiBob account.
6.  Click **Save**.

## Usage

Once the node is configured, you can use it in your workflows:

1.  Add the HiBob node to your workflow.
2.  Select the desired **Resource** (e.g., "People").
3.  Select the **Operation** you want to perform (e.g., "Search for Employees").
4.  Configure any additional parameters for the operation.
5.  Connect other nodes to process the data returned by the HiBob API.

### Example: Get All Employee Fields

*   **Resource**: `Metadata`
*   **Operation**: `Get all employee fields`

This operation will retrieve a list of all available employee fields in your HiBob instance.

### Example: Search for Employees

*   **Resource**: `People`
*   **Operation**: `Search for Employees`
*   **Fields**: (Optional) Select specific fields like `root.id`, `root.displayName`, `work.department`. If left empty, a default set of fields is returned.
*   **Additional Settings**:
    *   **Human Readable**: `Append` (default) or `Replace`.
    *   **Show Inactive**: `false` (default) or `true`.
    *   **Filter**: (Optional) Provide a JSON filter, e.g.:
        ```json
        {
            "fieldPath": "root.email",
            "operator": "equals",
            "values": [
                "tom@n8n.io"
            ]
        }
        ```
This operation will search for employees, potentially filtered by department, and return the specified fields.

## Resources

*   [n8n Community Support Forum](https://community.n8n.io/)
*   [HiBob API Documentation](https://apidocs.hibob.com/) (Refer to the HiBob documentation for details on API endpoints, filters, and permissions)

## Compatibility

This node has been tested with n8n version `1.94.1`, but should also work with later versions.

## Contributing

Contributions to this node are welcome! Please refer to the n8n [community node development guide](https://docs.n8n.io/integrations/creating-nodes/) for more information on how to contribute.

If you find any bugs or have a feature request, please open an issue on the GitHub repository.

## License

This n8n community node is [MIT Licensed](LICENSE.md).