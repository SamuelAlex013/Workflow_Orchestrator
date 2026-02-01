"""Workflow Assistant API Router - LLM-powered endpoints with RAG."""
from fastapi import APIRouter, HTTPException
from typing import Optional
import os

from ..api.schemas import (
    WorkflowAskRequest, WorkflowAskResponse,
    WorkflowDesignRequest, WorkflowDesignResponse
)
from ..services.RAG.scripts.workflow_aware_retriever import WorkflowAwareRetriever
from ..services.llm_service_hybrid import get_llm_service

router = APIRouter(prefix="/api/workflows", tags=["Workflow Assistant"])
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
