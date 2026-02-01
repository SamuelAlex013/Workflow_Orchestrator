
# n8n-nodes-glideapps

This is an n8n community node for integrating with the Glide Big Tables API. It allows you to automate data operations in Glide using n8n workflows.

## Installation

Follow these steps to install this node in your n8n instance:


```sh
npm install n8n-nodes-glideapps
```


## Credentials

To use this node, you'll need a Glide API key. You can obtain one by:

1. Creating an account at [Glide](https://www.glideapps.com/)
2. Navigating to your team settings
3. Generating an API key for your team

Configure your credentials in n8n:
- **API Key**: Your Glide API key



## Features

This node supports various Glide Big Tables API operations including:

- List, create, and import Big Tables
- Add, update, and delete rows in Big Tables
- Replace table schema or data
- Manage stashes for bulk data operations

### Glide Tables Helper Module (for n8n GUI)

This package includes a helper module for the official `@glideapps/tables` package, focused on dynamic dropdowns and safe UX for n8n nodes.

#### GUI Operations (for n8n dropdowns and user-facing actions)

- **getApps(apiKey)**: Returns a list of available apps/teams (placeholder, implement as needed for your Glide setup).
- **getTables(token, appId)**: Returns a list of tables for a given app (token and appId required).
- **getColumns(client, tableName)**: Returns a list of columns for a table (for dropdowns).
- **getRows(client, tableName, limit)**: Returns a preview of rows for dropdowns (with limit).
- **getRowPreview(client, tableName, limit)**: Returns a preview of rows for dropdowns (with limit).
- **getRowsWithConfirmation(client, tableName, limit, confirmed)**: Returns rows only if user has confirmed (for large data fetches).
- **getRowFetchWarning(limit)**: Returns a warning string for the UI before fetching rows.
- **getRowById(client, tableName, rowId)**: Fetch a single row by ID for previewing.

Use these helpers in your node's `loadOptionsMethod` for dynamic dropdowns, and in property descriptions to provide warnings or confirmations before large data fetches.

##### Example: Dynamic Dropdown for Table Columns

```ts
{
  displayName: 'Column',
  name: 'column',
  type: 'options',
  typeOptions: {
    loadOptionsMethod: 'getColumns',
    loadOptionsDependsOn: ['table'],
  },
  required: true,
  description: 'Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>'
}
```

##### Example: Row Fetch with Confirmation

```ts
{
  displayName: 'Row',
  name: 'row',
  type: 'options',
  typeOptions: {
    loadOptionsMethod: 'getRowsWithConfirmation',
    loadOptionsDependsOn: ['table', 'confirmed'],
  },
  required: true,
  description: 'Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>'
}
```

#### Node Execution Helpers (for use in node logic)

- **addRowToTable(client, { tableName, columnValues })**: Add a row to a table.
- **setColumnsInRow(client, { tableName, rowID?, rowIndex?, columnValues })**: Set columns in a row.
- **deleteRow(client, { tableName, rowID?, rowIndex? })**: Delete a row.
- **batchMutateTables(client, mutations)**: Run multiple mutations in a batch.
- **runMutations(client, mutations)**: Run any array of mutation objects.
- **queryTableSql(client, { appID, sql, params? })**: Run a SQL query (for Big Tables).
- **getAllRowsPaginated(client, tableName, pageSize?, maxPages?)**: Fetch all rows from a table using pagination (use with caution for large tables).

These helpers are intended for use in your node's main execution logic, not in the GUI.

**Note:** Internal utilities (such as error extraction and client instantiation) are not intended for direct use in n8n GUI dropdowns.

Below is a full example of using the node execution helpers in your own scripts:

```ts
// Example usage of node execution helpers:
const client = getGlideTablesClient('YOUR_API_KEY', 'YOUR_APP_ID'); // For row/column operations

// Add a row
await addRowToTable(client, { tableName: 'MyTable', columnValues: { Name: 'Test' } });

// Update a row
await setColumnsInRow(client, { tableName: 'MyTable', rowID: 'row123', columnValues: { Name: 'Updated' } });

// Delete a row
await deleteRow(client, { tableName: 'MyTable', rowID: 'row123' });

// Batch mutations
await batchMutateTables(client, [
  { kind: 'add-row-to-table', tableName: 'MyTable', columnValues: { Name: 'Batch' } },
  { kind: 'delete-row', tableName: 'MyTable', rowID: 'row456' }
]);

// Query rows
await queryTable(client, { appID: 'YOUR_APP_ID', tableName: 'MyTable' });

// SQL query (Big Tables)
await queryTableSql(client, { appID: 'YOUR_APP_ID', sql: 'SELECT * FROM "MyTable" LIMIT 10' });

// Extract errors from mutation results
const errors = extractMutationErrors(results);

// Dynamic dropdowns for n8n
const tables: DropdownOption[] = await getTables('YOUR_API_KEY', 'YOUR_APP_ID');
const columns: DropdownOption[] = await getColumns(client, 'MyTable');
const rows: DropdownOption[] = await getRows(client, 'MyTable', 50);

// Row preview and confirmation
const preview: DropdownOption[] = await getRowPreview(client, 'MyTable', 10);
const warning = getRowFetchWarning(100);
const safeRows: DropdownOption[] = await getRowsWithConfirmation(client, 'MyTable', 100, true);


// Fetch a single row by ID
const row = await getRowById(client, 'MyTable', 'row123');
```



---

## 🚀 Usage

**To get started:**

- Add the **Glide** node to your workflow
- Configure your **Glide credentials**
- Select the desired **operation** (e.g., list tables, add rows)
- Set the **operation parameters**
- Connect to other nodes in your workflow

---



## 💬 Support & Resources

- 📚 [Glide Big Tables API Documentation](https://www.glideapps.com/docs/api/big-tables)
- 🐞 Issues: Please report any issues in the [GitHub repository](https://github.com/KTheMan/n8n-nodes-glideapps)
- 👤 Maintainer: Kenneth Gordon

---



## 📝 License

[MIT](LICENSE.md)