
# n8n-nodes-suitecrm

A generic n8n node to operate with any SuiteCRM (SuiteCRM 8.x+) module via the official JSON API.

Supports CRUD operations, dynamic module and field discovery (including custom fields), advanced filtering, pagination, and relationship retrieval.

---

## Features

- **Full CRUD**: Create, read, update, and delete any SuiteCRM module.
- **Dynamic discovery**: Lists modules and fields automatically, including custom fields.
- **Advanced filtering**: Filter records with multiple operators, use custom fields, and paginate.
- **Relationship handling**: Retrieve related records for any entity.
- **OAuth2 authentication**: Secure, SuiteCRM-native using client credentials.
- **Robust error handling**: Clear, actionable errors and in-code comments for maintainability.

---

## Installation

```sh
npm install n8n-nodes-suitecrm-community
```

or

```sh
pnpm add n8n-nodes-suitecrm-community
```

Add to your n8n instance as a custom node following [n8n documentation on custom nodes](https://docs.n8n.io/integrations/creating-nodes/code/create-node/).

---

## Usage

### 1. Credentials

- Create credentials in n8n of type **SuiteCRM API**.
- Enter your SuiteCRM API URL, Client ID, and Client Secret  
  (see SuiteCRM > Admin > OAuth2 Clients).

### 2. Node configuration

- **Module:** Select any available module (dynamic, from API).
- **Operation:** Get All, Get One, Create, Update, Delete, or Get Relationships.
- **Options:** Add filters, paging, or relationship parameters as needed.

### 3. Input/Output Examples

#### Create Contact  
Data (JSON):

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email1": "john.doe@example.com"
}
```

#### Get Relationships  
Select a record and relationship type (auto-discovered by the node).

---

## Supported Operations

| Operation           | Description                                   |
|---------------------|-----------------------------------------------|
| Get All             | Fetch multiple records (with filters, paging) |
| Get One             | Fetch a single record by ID                   |
| Create              | Create a record (fields as JSON)              |
| Update              | Update a record (fields as JSON, PATCH method)|
| Delete              | Delete a record by ID                         |
| Get Relationships   | Get related records for a specific entity     |

---

## Requirements & Limitations

- SuiteCRM 8.x+ with API and OAuth2 enabled.
- Uses only official SuiteCRM API endpoints.
- Relationships must be managed as per SuiteCRM API capabilities.
- For 1:N relationships, set the "parent" ID on the child record (SuiteCRM logic).
- All modules and fields (including custom fields) are auto-discovered via API.

---

## Example Workflow

1. Create a Contact
2. Get Relationships (e.g., Opportunities related to that Contact)
3. Update, delete, or link related records as needed

---

## Troubleshooting

- **No access_token:** Check credentials and OAuth2 client config in SuiteCRM.
- **405 Method Not Allowed:** Use PATCH for updates; verify your SuiteCRM supports it.
- All API errors are relayed in node output with detail.

---

## Contributing

Contributions are welcome!  
Open an issue or PR in this repository.

---

## License

MIT

---

**Maintainer:** Javier Quilez Cabello / tecnologiasolidaria.org
**Support:** [SuiteCRM Community Forums](https://community.suitecrm.com/)
**Source:** [GitHub](https://github.com/tecnologiasolidaria/n8n-nodes-suitecrm)
**Docs:** [SuiteCRM JSON API Documentation](https://docs.suitecrm.com/developer/api/developer-setup-guide/json-api/)
