# n8n-nodes-postgres-context

This is an n8n community node package that provides nodes for AI context management with PostgreSQL persistence.

## Overview

This package contains two nodes for managing AI context in n8n workflows:

1. **Context Manager Node**: Used within AI agent flows to retrieve contexts by type, with filtering and limits.
2. **External Context Node**: Used to save or retrieve external contexts from any type and scope.

## PostgreSQL Setup

Before using these nodes, you need to set up a PostgreSQL database with the following table:

```sql
CREATE TABLE IF NOT EXISTS ai_contexts (
  id SERIAL PRIMARY KEY,
  chat_id TEXT NOT NULL,
  user_id TEXT,
  agent_id TEXT,
  session_key TEXT NOT NULL,
  context_key TEXT NOT NULL,
  context_type TEXT DEFAULT 'session',
  context_value JSONB NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE (chat_id, context_key, context_type)
);

CREATE INDEX IF NOT EXISTS idx_context_chat_type ON ai_contexts (chat_id, context_type, updated_at DESC);
```

The nodes will automatically create this table if it doesn't exist, but it's recommended to set it up manually for better control.

## Node Usage

### Context Manager Node

This node allows AI agents to retrieve contexts by type with filtering and limits.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| chatId | string | Unique identifier for the conversation |
| alwaysInclude | multiOptions | Context types that should always be included |
| limitsPerType | fixedCollection | List of types with maximum number of records |
| connectionString | string | PostgreSQL connection string |

#### Example

```json
{
  "chatId": "chat-123",
  "alwaysInclude": ["api"],
  "limitsPerType": [
    {"type": "user", "limit": 20},
    {"type": "agent", "limit": 10}
  ]
}
```

### External Context Node

This node allows saving or retrieving external contexts of any type and scope.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| mode | options | 'save' or 'get' |
| chatId | string | Unique identifier for the conversation |
| contextKey | string | Name of the context key |
| contextType | string | Type of the context (api, user, etc.) |
| contextValue | json | (save mode) JSON object to be saved as context |
| userId | string | (save mode) Optional user identifier |
| agentId | string | (save mode) Optional agent identifier |
| sessionKey | string | (save mode) Session identifier |
| connectionString | string | PostgreSQL connection string |

#### Example: Saving Context

```json
{
  "mode": "save",
  "chatId": "chat-123",
  "contextKey": "weather-forecast",
  "contextType": "api",
  "contextValue": {
    "city": "Arraial do Cabo",
    "temperature": "27°C",
    "status": "Ensolarado"
  }
}
```

#### Example: Getting Context

```json
{
  "mode": "get",
  "chatId": "chat-123",
  "contextKey": "weather-forecast",
  "contextType": "api"
}
```

## Context Types

The following context types are supported:

- user
- agent
- api
- memory
- short_term
- long_term
- system
- custom

## Best Practices

- Use context_type as a way to group logics: user, api, memory, etc.
- Use ExternalContextNode for programmatic populations (via Webhook, Workers, etc).
- Add TTL with periodic cleaning by updated_at.
- Index by chat_id and context_type for performance.

## Examples

This package includes example workflows in the `examples` directory that demonstrate how to use the nodes in n8n. See the [examples README](examples/README.md) for more information.

## License

MIT
