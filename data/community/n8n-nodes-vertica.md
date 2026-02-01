# n8n-nodes-vertica

This is a node for n8n that is used to execute SQL queries against Vertica database.

It also supports executing multiple queries in a single request by splitting the query with `--split--`.

## Development

1. Clone the repository
2. Run `npm install`
3. Run `npm run build`
4. Run `npm link`
5. Navigate to your local n8n nodes directory (e.g. `~/.n8n/nodes`) and run `npm link n8n-nodes-vertica`
6. Start n8n (`n8n start`) and you should see the Vertica node in the list of available nodes.
