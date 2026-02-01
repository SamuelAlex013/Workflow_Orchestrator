# n8n-nodes-docsautomator

This is an n8n community node for DocsAutomator, a powerful document automation tool. It allows you to create documents automatically using your existing DocsAutomator automations.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

### Create Document

The DocsAutomator node focuses on one primary operation: **Create Document**. This action uses a selected DocsAutomator automation to generate a document, populating it with data you provide for main placeholders and line items.

## Credentials

This node requires DocsAutomator API credentials:

1. Log in to your DocsAutomator account.
2. Navigate to your workspace settings > API Key.
3. Copy the API key.
4. In n8n, create new "DocsAutomator API" credentials and paste your API key into the provided field.

## Usage

### How to Use the Node

1.  **Add the DocsAutomator node** to your n8n workflow.
2.  **Set up Credentials**: Select your configured DocsAutomator API credentials from the dropdown.
3.  **Select an Automation**:
    - Choose the desired DocsAutomator automation from the "Automation" dropdown. This list is automatically populated with your available API-triggered automations from DocsAutomator.
4.  **Map Placeholder Values**:
    - Once an automation is selected, the "Placeholder Values" section will appear.
    - This section lists all main (non-line item) placeholders available in your selected DocsAutomator template.
    - Map data from previous nodes or enter static values for each placeholder. You can use n8n expressions here.
5.  **Configure Line Items (Optional)**:
    - If your selected automation template contains line items (dynamic tables), you can configure them in the "Line Items" section.
    - Click "Add Line Item" to add a set of line items. You can add multiple sets if your automation supports multiple line item types (e.g., `line_items_1`, `line_items_2`).
    - **Line Item Type**: Select the specific line item type (e.g., "Line Items 1") from the dropdown. This list is populated based on the selected automation.
    - **Items (JSON)**: Provide a JSON array of objects for the selected line item type. Each object in the array represents one row in your table, and its keys should match the placeholder names defined within that line item type in your DocsAutomator template.
      - _Example_: `[{"product_name": "Item A", "quantity": 2, "price": 10.00}, {"product_name": "Item B", "quantity": 1, "price": 25.50}]`
6.  **Set Processing Options**:
    - **Preview Mode**: Toggle this on if you want DocsAutomator to generate a preview document (e.g., a watermarked PDF or an image) instead of the final document.
    - **Async Processing**: Toggle this on if you want DocsAutomator to process the document creation asynchronously. This is useful for long-running document generation tasks. Your workflow will receive an immediate response, and DocsAutomator will process the document in the background, notifying a registered webhook (can be a webhook trigger in n8n) once finished.

### Example Workflow: Creating an Invoice with Line Items

1.  **Add and configure the DocsAutomator node** as described above.
2.  **Select Automation**: Choose your "Invoice Generation" automation from the dropdown.
3.  **Map Placeholder Values**:
    - `customer_name`: `{{ $json.customer.fullName }}`
    - `invoice_number`: `{{ $json.invoiceDetails.id }}`
    - `invoice_date`: `{{ $now.toFormat('yyyy-MM-dd') }}`
    - `due_date`: `{{ $now.plus({days: 30}).toFormat('yyyy-MM-dd') }}`
4.  **Configure Line Items**:
    - Click "Add Line Item".
    - **Line Item Type**: Select "Line Items 1" (assuming your invoice template uses `line_items_1` for its main product table).
    - **Items (JSON)**:
      ```json
      [
        {
          "item_description": "{{ $json.products[0].name }}",
          "item_quantity": "{{ $json.products[0].qty }}",
          "item_unit_price": "{{ $json.products[0].unitPrice }}",
          "item_total": "{{ $json.products[0].qty * $json.products[0].unitPrice }}"
        },
        {
          "item_description": "{{ $json.products[1].name }}",
          "item_quantity": "{{ $json.products[1].qty }}",
          "item_unit_price": "{{ $json.products[1].unitPrice }}",
          "item_total": "{{ $json.products[1].qty * $json.products[1].unitPrice }}"
        }
      ]
      ```
      _(Note: The actual placeholder names like `item_description`, `item_quantity` depend on how you've defined them in your DocsAutomator line item template)._
5.  **Set Options**:
    - Leave "Preview Mode" off for the final invoice.
    - Leave "Async Processing" off if you want the workflow to wait for the document.
6.  **Execute the workflow**. The node will send the data to DocsAutomator, which will generate the invoice. The result from DocsAutomator (e.g., a link to the document or document data) will be available in the output of the node.

### Tips for Success

- **JSON Structure for Line Items**: Ensure the JSON provided for "Items (JSON)" is a valid array of objects. Each object should contain key-value pairs corresponding to the placeholders in your line item template.
- **Use n8n Expressions**: Leverage n8n's powerful expression editor to dynamically map data from previous nodes or perform transformations.
- **Error Handling**: Use n8n's "Continue On Fail" setting (under node Settings) or error workflows to manage potential issues during document creation.

## Resources

- [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
- [DocsAutomator API documentation](https://docs.docsautomator.co/) (if available, or link to general help)
- [DocsAutomator website](https://docsautomator.co/)
