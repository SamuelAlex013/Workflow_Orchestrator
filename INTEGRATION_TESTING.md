# Integration Testing Guide

This document provides a step-by-step verification plan to test the frontend-backend integration.

---

## Prerequisites

- Python 3.9+ installed
- Node.js 18+ installed
- Both `backend/` and `frontend/` dependencies installed

---

## 🚀 Quick Start

### Step 1: Start the Backend

```bash
# From project root
cd f:\college\projects\Workflow_Orchestrator

# Activate virtual environment (if using one)
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Start the FastAPI server
python run_server.py
```

**Expected output:**
```
🚀 Starting Workflow Orchestrator...
✅ RAG retriever ready
✅ Workflow retriever ready
✅ LLM service ready
✅ Ready
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Verify Backend is Running

Open a new terminal and run:

```bash
curl http://localhost:8000/
```

**Expected:** `{"status":"ok","version":"0.1.0"}`

```bash
curl http://localhost:8000/api/workflows/health
```

**Expected:** `{"status":"healthy","rag_retriever":true,"llm_service":true,"llm_backend":"openai"}`

### Step 3: Start the Frontend

```bash
# New terminal window
cd f:\college\projects\Workflow_Orchestrator\frontend

# Install dependencies (if not done)
npm install

# Start Next.js dev server
npm run dev
```

**Expected output:**
```
▲ Next.js 15.x.x
- Local: http://localhost:3000
✓ Ready
```

### Step 4: Open the Application

1. Open **http://localhost:3000** in your browser
2. Sign in (if Clerk authentication is required)
3. Navigate to the chat interface

---

## ✅ Test Checklist

### Basic Connectivity
- [ ] Frontend loads without errors at `http://localhost:3000`
- [ ] No CORS errors in browser console
- [ ] Backend responds to health check

### Chat Functionality

| Test Case | Input | Expected Behavior |
|-----------|-------|-------------------|
| **Basic question** | "What is n8n?" | Should return AI-generated answer with sources |
| **Workflow question** | "How do I use the HTTP Request node?" | Detailed response with n8n documentation |
| **Workflow planning mode** | Type `@` → select "Workflow Planning" → "Build a Slack notification bot" | Returns structured workflow design |
| **Empty message** | Click send with no text | Button should be disabled |
| **Long message** | 1000+ character message | Should truncate or show validation error |

### Loading States
- [ ] Typing dots animation appears while waiting for response
- [ ] Send button is disabled during loading
- [ ] Input field is disabled during loading

### Error Handling

| Scenario | How to Test | Expected UI |
|----------|-------------|-------------|
| **Backend offline** | Stop backend server, send message | "🔌 Connection Failed" error message |
| **Service initializing** | Send message immediately after backend start | "⚠️ Service Unavailable" message |
| **No results found** | Ask about unrelated topic | "🔍 No Relevant Information Found" message |

### UI Features
- [ ] Sources accordion expands/collapses
- [ ] Confidence badge displays (high/medium/low)
- [ ] Model name displays in response
- [ ] Error messages have distinct red styling
- [ ] Messages auto-scroll to bottom

---

## 🔧 Troubleshooting

### CORS Errors
The backend has CORS fully open (`allow_origins=["*"]`). If you still see CORS errors:
1. Check if the backend URL is correct in `.env.local`
2. Ensure the backend is running
3. Try clearing browser cache

### "Cannot connect to backend"
1. Verify backend is running: `curl http://localhost:8000/`
2. Check firewall settings
3. Ensure port 8000 is not blocked

### "Service Unavailable (503)"
The RAG or LLM service may still be initializing. Wait 10-15 seconds and try again.

### LLM Errors
If you see LLM-related errors, ensure:
1. `OPENAI_API_KEY` or `GROQ_API_KEY` environment variable is set
2. API key is valid and has quota

---

## 🧪 API Testing with cURL

### Test the /ask endpoint directly:
```bash
curl -X POST http://localhost:8000/api/workflows/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is n8n?", "top_k": 5}'
```

### Test the /design endpoint:
```bash
curl -X POST http://localhost:8000/api/workflows/design \
  -H "Content-Type: application/json" \
  -d '{"description": "Send Slack message when new row added to Google Sheet"}'
```

---

## 📊 Expected Response Times

| Operation | Expected Time |
|-----------|---------------|
| Health check | < 100ms |
| Document search | 200-500ms |
| LLM response (ask) | 2-5 seconds |
| Workflow design | 3-8 seconds |

---

## ✨ Success Criteria

The integration is complete when:

1. ✅ User can send a message and receive a real AI response
2. ✅ Loading state shows while waiting
3. ✅ Error states display meaningful messages
4. ✅ Sources are shown for AI responses
5. ✅ Mode switching (General/Workflow Planning) works
6. ✅ Confidence indicators display correctly
