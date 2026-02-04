# Workflow Orchestrator API Reference

> **Framework:** FastAPI  
> **Base URL:** `http://localhost:8000`  
> **Version:** 0.1.0  
> **Interactive Docs:** [Swagger UI](http://localhost:8000/docs) | [ReDoc](http://localhost:8000/redoc)

---

## CORS Configuration

The backend has CORS fully enabled:
```python
allow_origins=["*"]
allow_methods=["*"]
allow_headers=["*"]
```
No CORS issues expected for local development.

---

## Table of Contents

1. [Health & Root](#1-health--root-endpoints)
2. [Document Search API](#2-document-search-api)
3. [Workflow Assistant API](#3-workflow-assistant-api)
4. [Error Handling](#4-error-handling)
5. [Data Models Reference](#5-data-models-reference)

---

## 1. Health & Root Endpoints

### `GET /`
Root endpoint to verify API is running.

**Response:**
```json
{
  "status": "ok",
  "version": "0.1.0"
}
```

**curl:**
```bash
curl http://localhost:8000/
```

---

### `GET /api/docs/health`
Check document search service health.

**Response (200):**
```json
{
  "status": "healthy",
  "vector_store_loaded": true,
  "total_chunks": 1523,
  "embedding_model": "all-MiniLM-L6-v2"
}
```

**Response (503 - Unhealthy):**
```json
{
  "status": "unhealthy",
  "vector_store_loaded": false,
  "total_chunks": 0,
  "embedding_model": "none"
}
```

**curl:**
```bash
curl http://localhost:8000/api/docs/health
```

---

### `GET /api/workflows/health`
Check workflow assistant services health (RAG + LLM).

**Response:**
```json
{
  "status": "healthy",
  "rag_retriever": true,
  "llm_service": true,
  "llm_backend": "openai"
}
```

**curl:**
```bash
curl http://localhost:8000/api/workflows/health
```

---

## 2. Document Search API

### `POST /api/docs/search`
Semantic search through n8n documentation using RAG.

**Request Body:**
| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `query` | string | ✅ Yes | - | 1-500 chars | Search query |
| `top_k` | integer | No | 5 | 1-20 | Number of results |
| `filters` | object | No | null | - | Filter by section_type, doc_category |
| `format_context` | boolean | No | false | - | Return formatted context string |
| `max_context_tokens` | integer | No | 2000 | 100-8000 | Max tokens in formatted context |

**Request Example:**
```json
{
  "query": "How do I use the HTTP Request node?",
  "top_k": 5,
  "filters": {
    "section_type": "node"
  },
  "format_context": true,
  "max_context_tokens": 2000
}
```

**Response (200):**
```json
{
  "query": "How do I use the HTTP Request node?",
  "results": [
    {
      "text": "The HTTP Request node is used to make HTTP requests...",
      "metadata": {
        "source": "n8n_docs.md",
        "header_path": "Nodes > HTTP Request",
        "last_header": "HTTP Request",
        "chunk_index": 42,
        "contains_code": true,
        "token_count": 256,
        "section_type": "node",
        "doc_category": "integrations",
        "char_count": 1024,
        "node_type": "action",
        "integrations": ["http"],
        "workflow_patterns": ["api-call"]
      },
      "distance": 0.234,
      "relevance_score": 0.883
    }
  ],
  "total_results": 5,
  "formatted_context": "## Context from Documentation\n\n..."
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/docs/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How do I use the HTTP Request node?",
    "top_k": 5,
    "format_context": true
  }'
```

---

### `GET /api/docs/search`
Same as POST but via query parameters.

**Query Parameters:**
| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `query` | string | ✅ Yes | - |
| `top_k` | integer | No | 5 |
| `section_type` | string | No | - |
| `doc_category` | string | No | - |
| `format_context` | boolean | No | false |

**curl:**
```bash
curl "http://localhost:8000/api/docs/search?query=webhook%20trigger&top_k=3"
```

---

## 3. Workflow Assistant API

### `POST /api/workflows/ask`
**Primary chat endpoint** - Ask questions and get AI-generated answers using RAG context.

**Request Body:**
| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `query` | string | ✅ Yes | - | 1-1000 chars | User question |
| `top_k` | integer | No | 5 | 1-10 | Context chunks to retrieve |
| `temperature` | float | No | 0.7 | 0.0-1.0 | LLM creativity |
| `max_answer_tokens` | integer | No | 1000 | 100-2000 | Max response length |
| `include_sources` | boolean | No | true | - | Include source references |

**Request Example:**
```json
{
  "query": "How do I connect Slack to a webhook trigger?",
  "top_k": 5,
  "temperature": 0.7,
  "max_answer_tokens": 1000,
  "include_sources": true
}
```

**Response (200):**
```json
{
  "query": "How do I connect Slack to a webhook trigger?",
  "answer": "To connect Slack to a webhook trigger in n8n, follow these steps:\n\n1. Create a new workflow...",
  "sources": [
    "Nodes > Webhook",
    "Integrations > Slack",
    "Getting Started > Triggers"
  ],
  "confidence": "high",
  "model": "gpt-4o-mini",
  "retrieved_chunks": 5
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/workflows/ask \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How do I connect Slack to a webhook trigger?",
    "top_k": 5,
    "temperature": 0.7,
    "include_sources": true
  }'
```

---

### `POST /api/workflows/design`
Generate structured workflow designs from natural language descriptions.

**Request Body:**
| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | ✅ Yes | - | 10-500 chars | Workflow description |
| `top_k` | integer | No | 5 | 1-10 | Context chunks |

**Request Example:**
```json
{
  "description": "Create a workflow that monitors a Google Sheet for new rows and sends a Slack message for each new entry",
  "top_k": 5
}
```

**Response (200):**
```json
{
  "workflow_description": "This workflow monitors a Google Sheet for new rows using a scheduled trigger...",
  "required_nodes": [
    "Schedule Trigger",
    "Google Sheets",
    "Slack"
  ],
  "suggested_structure": "1. Schedule Trigger (runs every 5 minutes)\n2. Google Sheets node (Get Rows)\n3. IF node (check for new rows)\n4. Slack node (Send Message)",
  "model": "gpt-4o-mini"
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/workflows/design \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Monitor Google Sheet and send Slack notifications",
    "top_k": 5
  }'
```

---

## 4. Error Handling

### Standard Error Response
```json
{
  "detail": "Error message describing the issue"
}
```

### HTTP Status Codes

| Code | Meaning | When |
|------|---------|------|
| 200 | Success | Request processed successfully |
| 404 | Not Found | No relevant documentation found |
| 422 | Validation Error | Invalid request body/parameters |
| 500 | Server Error | Unexpected server failure |
| 503 | Service Unavailable | RAG/LLM service not initialized |

### Validation Error Example (422)
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "query"],
      "msg": "String should have at least 1 character",
      "input": "",
      "ctx": {"min_length": 1}
    }
  ]
}
```

---

## 5. Data Models Reference

### DocumentChunk
```typescript
interface DocumentChunk {
  text: string;
  metadata: {
    source: string;
    header_path: string;
    last_header: string;
    chunk_index: number;
    contains_code: boolean;
    token_count: number;
    section_type: string;
    doc_category: string;
    char_count: number;
    node_type?: string;
    integrations?: string[];
    workflow_patterns?: string[];
  };
  distance: number;
  relevance_score: number;  // 0.0 - 1.0
}
```

### WorkflowAskResponse
```typescript
interface WorkflowAskResponse {
  query: string;
  answer: string;
  sources: string[];
  confidence: "high" | "medium" | "low";
  model: string;
  retrieved_chunks: number;
}
```

### WorkflowDesignResponse
```typescript
interface WorkflowDesignResponse {
  workflow_description: string;
  required_nodes: string[];
  suggested_structure: string;
  model: string;
}
```

---

## Quick Start

1. **Start the backend:**
   ```bash
   python run_server.py
   ```
   Server runs on `http://localhost:8000`

2. **Verify it's running:**
   ```bash
   curl http://localhost:8000/
   # Expected: {"status":"ok","version":"0.1.0"}
   ```

3. **Check services health:**
   ```bash
   curl http://localhost:8000/api/workflows/health
   ```

4. **Ask your first question:**
   ```bash
   curl -X POST http://localhost:8000/api/workflows/ask \
     -H "Content-Type: application/json" \
     -d '{"query": "What is n8n?"}'
   ```
