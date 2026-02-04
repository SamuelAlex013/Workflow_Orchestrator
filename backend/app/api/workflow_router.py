"""Workflow Assistant API Router - LLM-powered endpoints with RAG."""
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from typing import Optional
import os
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
import queue
import threading

from ..api.schemas import (
    WorkflowAskRequest, WorkflowAskResponse,
    WorkflowDesignRequest, WorkflowDesignResponse
)
from ..services.RAG.scripts.workflow_aware_retriever import WorkflowAwareRetriever
from ..services.llm_service_hybrid import get_llm_service

router = APIRouter(prefix="/api/workflows", tags=["Workflow Assistant"])

# Thread pool for running sync generators
_executor = ThreadPoolExecutor(max_workers=4)
_retriever: Optional[WorkflowAwareRetriever] = None
_llm_service = None


def get_retriever() -> WorkflowAwareRetriever:
    if _retriever is None:
        raise HTTPException(status_code=503, detail="RAG retriever not initialized")
    return _retriever


def get_llm():
    if _llm_service is None:
        raise HTTPException(status_code=503, detail="LLM service not initialized")
    return _llm_service


async def initialize_services():
    """Initialize workflow-aware retriever and LLM service."""
    global _retriever, _llm_service
    
    try:
        _retriever = WorkflowAwareRetriever()
        print("✅ Workflow retriever ready")
    except Exception as e:
        print(f"❌ RAG retriever failed: {e}")
        raise
    
    try:
        backend = os.getenv("LLM_BACKEND", "auto")
        from ..services.llm_service_hybrid import get_llm_service as get_singleton
        _llm_service = get_singleton(backend=backend)
        print("✅ LLM service ready")
    except Exception as e:
        print(f"⚠️ LLM service failed: {e}")


@router.post("/ask", response_model=WorkflowAskResponse)
async def ask_workflow_question(request: WorkflowAskRequest):
    """Ask a question and get an intelligent answer from documentation."""
    retriever = get_retriever()
    llm = get_llm()
    
    chunks = retriever.retrieve_workflow_nodes(query=request.query, top_k=request.top_k, use_reranking=True)
    
    if not chunks:
        raise HTTPException(status_code=404, detail="No relevant documentation found")
    
    result = llm.synthesize_answer(
        query=request.query, context_chunks=chunks,
        max_tokens=request.max_answer_tokens, temperature=request.temperature
    )
    
    return WorkflowAskResponse(
        query=request.query, answer=result["answer"],
        sources=result["sources"] if request.include_sources else [],
        confidence=result["confidence"], model=result["model"],
        retrieved_chunks=len(chunks)
    )


@router.post("/ask/stream")
async def ask_workflow_question_stream(request: WorkflowAskRequest):
    """Ask a question and get a streaming response (SSE)."""
    retriever = get_retriever()
    llm = get_llm()
    
    chunks = retriever.retrieve_workflow_nodes(query=request.query, top_k=request.top_k, use_reranking=True)
    
    if not chunks:
        raise HTTPException(status_code=404, detail="No relevant documentation found")
    
    # Pre-compute metadata
    sources = [chunk.get('metadata', {}).get('header_path', 'Unknown') for chunk in chunks[:5]]
    avg_distance = sum(c.get('distance', 1.0) for c in chunks[:5]) / min(5, len(chunks))
    confidence = "high" if avg_distance < 0.5 else ("medium" if avg_distance < 0.8 else "low")
    
    async def async_generate():
        """Async generator that properly bridges sync LLM streaming."""
        try:
            # First, send metadata
            metadata = {
                "type": "metadata",
                "sources": sources,
                "confidence": confidence,
                "model": llm.active_backend,
                "retrieved_chunks": len(chunks)
            }
            yield f"data: {json.dumps(metadata)}\n\n"
            
            # Use a queue to bridge sync generator to async
            token_queue = queue.Queue()
            error_holder = [None]  # Use list to allow modification in thread
            
            def run_sync_generator():
                """Run the sync generator in a thread and put tokens in queue."""
                try:
                    for token in llm.synthesize_answer_stream(
                        query=request.query,
                        context_chunks=chunks,
                        max_tokens=request.max_answer_tokens,
                        temperature=request.temperature
                    ):
                        token_queue.put(("token", token))
                    token_queue.put(("done", None))
                except Exception as e:
                    error_holder[0] = e
                    token_queue.put(("error", str(e)))
            
            # Start the sync generator in a thread
            thread = threading.Thread(target=run_sync_generator, daemon=True)
            thread.start()
            
            # Consume tokens from queue asynchronously
            token_count = 0
            while True:
                # Non-blocking check with small timeout
                try:
                    msg_type, content = token_queue.get(timeout=0.1)
                except queue.Empty:
                    # Send keep-alive while waiting
                    yield ": keep-alive\n\n"
                    continue
                
                if msg_type == "token":
                    chunk_data = {"type": "token", "content": content}
                    yield f"data: {json.dumps(chunk_data)}\n\n"
                    token_count += 1
                    
                    # Yield control periodically
                    if token_count % 10 == 0:
                        await asyncio.sleep(0)
                        
                elif msg_type == "done":
                    break
                elif msg_type == "error":
                    error_data = {"type": "error", "message": content}
                    yield f"data: {json.dumps(error_data)}\n\n"
                    break
            
            # Wait for thread to complete
            thread.join(timeout=1.0)
            
            # Send completion signal
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            error_data = {"type": "error", "message": str(e)}
            yield f"data: {json.dumps(error_data)}\n\n"
    
    return StreamingResponse(
        async_generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
            "Content-Type": "text/event-stream",
            "Transfer-Encoding": "chunked",
        }
    )


@router.post("/design", response_model=WorkflowDesignResponse)
async def design_workflow(request: WorkflowDesignRequest):
    """Generate a structured workflow design from natural language."""
    retriever = get_retriever()
    llm = get_llm()
    
    chunks = retriever.retrieve_workflow_nodes(query=request.description, top_k=request.top_k, use_reranking=True)
    
    if not chunks:
        raise HTTPException(status_code=404, detail="No relevant documentation found")
    
    result = llm.generate_workflow_description(query=request.description, context_chunks=chunks)
    
    return WorkflowDesignResponse(
        workflow_description=result["workflow_description"],
        required_nodes=result["required_nodes"],
        suggested_structure=result["suggested_structure"],
        model=result["model"]
    )


@router.get("/health")
async def check_health():
    """Check if workflow assistant services are ready."""
    return {
        "status": "healthy" if (_retriever and _llm_service) else "degraded",
        "rag_retriever": _retriever is not None,
        "llm_service": _llm_service is not None,
        "llm_backend": _llm_service.active_backend if _llm_service else None
    }
