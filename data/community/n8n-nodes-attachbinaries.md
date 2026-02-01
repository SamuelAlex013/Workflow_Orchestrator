## Attach Binaries (Files) Node

This node allows you to attach binary data (e.g., files) from another node’s output to the current item(s) in your workflow.

### Operation

- **Attach From Other Node**: Pulls binary fields from a specified node and attaches them to the current input item.

### Fields

| Field             | Type     | Description                                                                 |
|------------------|----------|-----------------------------------------------------------------------------|
| From Node        | String   | Name of the node containing the binaries you want to attach                |
| Attach           | Options  | Choose to attach `All Binaries` or `Selected Binaries`                     |
| Binary Fields    | String   | Comma-separated list of binary keys (only visible if "Selected Binaries")  |
| Item Mapping     | Options  | Determines which item to attach from: `Same`, `First`, or `Specify Index`  |
| Item Index       | Number   | (Visible if mapping is `Specify Index`) Index of the item in the source node |

### Behavior

- Binary data is copied from the specified node and merged into each incoming item.
- If a binary key already exists, a suffix (e.g., `_nodeName`) is added to prevent overwriting.

