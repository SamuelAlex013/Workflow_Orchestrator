"""RAG-based document search endpoints."""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import sys
from pathlib import Path
from sentence_transformers import SentenceTransformer

sys.path.append(str(Path(__file__).parent.parent / "services" / "RAG" / "scripts"))

from rag_retriever import RAGRetriever
from ..api.schemas import (
    DocumentSearchRequest, DocumentSearchResponse,
    DocumentChunk, ChunkMetadata, HealthCheckResponse
)

router = APIRouter(prefix="/api/docs", tags=["Document Search"])
_retriever = None
_embedding_model = None


async def initialize_retriever():
    """Initialize the RAG retriever at startup."""
    global _retriever, _embedding_model
    try:
        _embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
            cache_folder=".cache/models"
        )
        _retriever = RAGRetriever(model=_embedding_model)
        print("✅ RAG retriever ready")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize retriever: {e}")
        return False


def get_retriever() -> RAGRetriever:
    if _retriever is None:
        raise HTTPException(status_code=503, detail="Vector store not initialized")
    return _retriever


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Check if document search service is healthy."""
    try:
        retriever = get_retriever()
        return HealthCheckResponse(
            status="healthy",
            vector_store_loaded=True,
            total_chunks=retriever.index.ntotal,
            embedding_model="all-MiniLM-L6-v2"
        )
    except HTTPException:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "vector_store_loaded": False, "total_chunks": 0, "embedding_model": "none"}
        )


@router.post("/search", response_model=DocumentSearchResponse)
async def search_documents(request: DocumentSearchRequest):
    """Search n8n documentation using semantic search."""
    try:
        retriever = get_retriever()
        results = retriever.retrieve(query=request.query, top_k=request.top_k, filters=request.filters)
        
        chunks = [
            DocumentChunk(
                text=r['text'],
                metadata=ChunkMetadata(**r['metadata']),
                distance=r['distance'],
                relevance_score=max(0.0, min(1.0, 1.0 - (r['distance'] / 2.0)))
            )
            for r in results
        ]
        
        formatted_context = retriever.format_context(results, max_tokens=request.max_context_tokens) if request.format_context else None
        
        return DocumentSearchResponse(
            query=request.query, results=chunks,
            total_results=len(chunks), formatted_context=formatted_context
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@router.get("/search", response_model=DocumentSearchResponse)
async def search_documents_get(query: str, top_k: int = 5, section_type: str | None = None, doc_category: str | None = None, format_context: bool = False):
    """Search using GET request."""
    filters = {}
    if section_type: filters['section_type'] = section_type
    if doc_category: filters['doc_category'] = doc_category
    
    return await search_documents(DocumentSearchRequest(
        query=query, top_k=top_k,
        filters=filters if filters else None, format_context=format_context
    ))
