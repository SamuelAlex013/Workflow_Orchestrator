"""Pydantic models for API schemas."""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict


# Document Search
class DocumentSearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500)
    top_k: int = Field(5, ge=1, le=20)
    filters: Optional[Dict[str, str]] = None
    format_context: bool = False
    max_context_tokens: int = Field(2000, ge=100, le=8000)


class ChunkMetadata(BaseModel):
    source: str
    header_path: str
    last_header: str
    chunk_index: int
    contains_code: bool
    token_count: int
    section_type: str
    doc_category: str
    char_count: int
    node_type: Optional[str] = None
    integrations: Optional[List[str]] = None
    workflow_patterns: Optional[List[str]] = None


class DocumentChunk(BaseModel):
    text: str
    metadata: ChunkMetadata
    distance: float
    relevance_score: float


class DocumentSearchResponse(BaseModel):
    query: str
    results: List[DocumentChunk]
    total_results: int
    formatted_context: Optional[str] = None


class HealthCheckResponse(BaseModel):
    status: str
    vector_store_loaded: bool
    total_chunks: int
    embedding_model: str


# Workflow Assistant
class WorkflowAskRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    top_k: int = Field(5, ge=1, le=10)
    temperature: float = Field(0.7, ge=0, le=1)
    max_answer_tokens: int = Field(2000, ge=100, le=4000)
    include_sources: bool = True


class WorkflowAskResponse(BaseModel):
    query: str
    answer: str
    sources: List[str]
    confidence: str
    model: str
    retrieved_chunks: int


class WorkflowDesignRequest(BaseModel):
    description: str = Field(..., min_length=10, max_length=500)
    top_k: int = Field(5, ge=1, le=10)


class WorkflowDesignResponse(BaseModel):
    workflow_description: str
    required_nodes: List[str]
    suggested_structure: str
    model: str
