# n8n-nodes-edifact-to-json

This is an n8n community node. It lets you convert EDIFACT (Electronic Data Interchange For Administration, Commerce and Transport) messages in your n8n workflows.

EDIFACT is a global standard for electronic data interchange, facilitating the exchange of business documents like invoices and purchase orders.

## Installation
Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations
* **Convert EDIFACT to JSON:** Converts a raw EDIFACT string or binary data into a structured JSON object.

## Credentials
This node does not require any external authentication or credentials.

## Compatibility
This node requires n8n version 1.0.0 or higher.

## Usage

### Node Parameters:
* **Input Type:**
    * `String`: For direct EDIFACT string input.
    * `Binary`: For EDIFACT data coming from a binary property.
* **EDIFACT Input (visible when Input Type is String):**
    * Provide the EDIFACT message as a string.
* **Binary Property Name (visible when Input Type is Binary):**
    * Specify the name of the binary property (e.g., `data`, `file`) that contains the EDIFACT data.

### Example Workflow:
1.  **Start Node:** Use a "Manual Trigger" or "Webhook" node.
2.  **EDIFACT to JSON Node:**
    * Connect it to the start node.
    * Configure `EDIFACT Input` (or `Binary Property Name`) and delimiter settings as appropriate.
3.  **Set Node (Optional):** Add a "Set" node to view the output JSON.

After execution, the node outputs an item with a `json` property containing the parsed EDIFACT data.

## Resources
* [n8n community nodes documentation](https://docs.n8n.io/integrations/#community-nodes)
* [ts-edifact GitHub Repository](https://github.com/RovoMe/ts-edifact)