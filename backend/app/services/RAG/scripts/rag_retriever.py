"""
Helper module for loading and querying the FAISS vector store.
Use this in your RAG application to retrieve relevant documentation chunks.
"""

import numpy as np
import faiss
import pickle
import re
from pathlib import Path
from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer

# Paths
VECTOR_STORE_DIR = Path(__file__).parent.parent / "data" / "vector_store"
INDEX_FILE = VECTOR_STORE_DIR / "faiss.index"
METADATA_FILE = VECTOR_STORE_DIR / "metadata.pkl"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Query expansion mappings
QUERY_EXPANSIONS = {
    # Action verbs
    'send': ['send', 'transmit', 'dispatch', 'deliver'],
    'receive': ['receive', 'get', 'retrieve', 'fetch', 'listen'],
    'store': ['store', 'save', 'write', 'insert', 'persist'],
    'update': ['update', 'modify', 'change', 'edit'],
    'delete': ['delete', 'remove', 'clear', 'drop'],
    'create': ['create', 'make', 'generate', 'build'],
    
    # Integration names
    'telegram': ['telegram', 'telegram trigger', 'telegram message', 'telegram bot'],
    'database': ['database', 'db', 'storage', 'data store', 'mysql', 'postgres', 'mongodb'],
    'google drive': ['google drive', 'gdrive', 'drive api', 'google storage'],
    'slack': ['slack', 'slack message', 'slack channel'],
    'discord': ['discord', 'discord message', 'discord webhook'],
    'email': ['email', 'mail', 'smtp', 'gmail', 'send email'],
    
    # Common patterns
    'authentication': ['authentication', 'auth', 'credentials', 'oauth', 'api key'],
    'webhook': ['webhook', 'trigger', 'http request', 'incoming webhook'],
    'api': ['api', 'http', 'rest api', 'endpoint'],
}

# Workflow pattern keywords
WORKFLOW_TRIGGERS = ['receive', 'listen', 'trigger', 'when', 'on', 'watch']
WORKFLOW_ACTIONS = ['send', 'store', 'save', 'update', 'create', 'delete', 'process']


class RAGRetriever:
    """Simple RAG retriever using FAISS vector store."""
    
    def __init__(self, model=None):
        """Load the FAISS index, metadata, and embedding model.
        
        Args:
            model: Optional pre-loaded embedding model. If None, will load from local cache.
        """
        if not INDEX_FILE.exists() or not METADATA_FILE.exists():
            raise FileNotFoundError(
                f"Vector store not found. Please run 4_build_vector_store.py first."
            )
        
        print("Loading vector store...")
        self.index = faiss.read_index(str(INDEX_FILE))
        
        with METADATA_FILE.open('rb') as f:
            data = pickle.load(f)
            self.metadata_list = data['metadata']
            self.text_list = data['texts']
        
        if model is not None:
            print("Using pre-loaded embedding model...")
            self.model = model
        else:
            print("Loading embedding model from cache...")
            try:
                self.model = SentenceTransformer(EMBEDDING_MODEL, cache_folder=".cache/models")
            except Exception as e:
                print(f"Warning: Failed to load model with cache: {e}")
                print("Trying without cache...")
                self.model = SentenceTransformer(EMBEDDING_MODEL)
        
        print(f"✓ Loaded {self.index.ntotal} chunks")
    
    def expand_query(self, query: str) -> str:
        """
        Expand query with synonyms and related terms for better retrieval.
        
        Args:
            query: Original user query
        
        Returns:
            Expanded query with additional search terms
        """
        expanded_terms = [query]  # Always keep original
        query_lower = query.lower()
        
        # Check for workflow patterns (trigger -> action)
        has_trigger = any(word in query_lower for word in WORKFLOW_TRIGGERS)
        has_action = any(word in query_lower for word in WORKFLOW_ACTIONS)
        
        if has_trigger and has_action:
            # This is a workflow query - add pattern terms
            expanded_terms.append("workflow template example")
        
        # Expand known terms
        for key, synonyms in QUERY_EXPANSIONS.items():
            if key in query_lower:
                # Add the most relevant synonyms (not all to avoid noise)
                expanded_terms.extend(synonyms[:2])
        
        # Detect multi-concept queries (e.g., "telegram" AND "database")
        concepts = []
        for integration in ['telegram', 'slack', 'discord', 'google drive', 'database', 'email']:
            if integration in query_lower:
                concepts.append(integration)
        
        if len(concepts) >= 2:
            # Multi-integration query - add integration-specific terms
            for concept in concepts:
                if concept in QUERY_EXPANSIONS:
                    expanded_terms.append(QUERY_EXPANSIONS[concept][0])
        
        # Join and deduplicate
        expanded = " ".join(expanded_terms)
        return expanded
    
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filters: Dict[str, str] = None,
        expand_query: bool = True
    ) -> List[Dict]:
        """
        Retrieve top-k most relevant chunks for a query.
        
        Args:
            query: User's natural language question
            top_k: Number of chunks to retrieve
            filters: Optional filters (e.g., {'section_type': 'example'})
            expand_query: Whether to expand query with synonyms (default: True)
        
        Returns:
            List of dictionaries with 'text', 'metadata', and 'distance'
        """
        # Optionally expand query for better retrieval
        if expand_query:
            expanded = self.expand_query(query)
            print(f"Expanded query: {query} -> {expanded}")
            search_query = expanded
        else:
            search_query = query
        
        # Generate query embedding
        query_embedding = self.model.encode([search_query])[0].astype('float32').reshape(1, -1)
        
        # Search in FAISS index (retrieve more if filtering)
        search_k = top_k * 3 if filters else top_k
        distances, indices = self.index.search(query_embedding, search_k)
        
        # Build results
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.text_list):
                metadata = self.metadata_list[idx]
                
                # Apply filters if provided
                if filters:
                    match = all(
                        metadata.get(key) == value
                        for key, value in filters.items()
                    )
                    if not match:
                        continue
                
                results.append({
                    'text': self.text_list[idx],
                    'metadata': metadata,
                    'distance': float(distance)
                })
                
                if len(results) >= top_k:
                    break
        
        return results
    
    def format_context(self, results: List[Dict], max_tokens: int = 2000) -> str:
        """
        Format retrieved chunks into a context string for LLM.
        
        Args:
            results: Retrieved chunks from retrieve()
            max_tokens: Maximum tokens to include (approximate)
        
        Returns:
            Formatted context string
        """
        context_parts = []
        total_tokens = 0
        
        for i, result in enumerate(results):
            metadata = result['metadata']
            text = result['text']
            
            # Estimate tokens (rough approximation: 1 token ≈ 4 chars)
            chunk_tokens = len(text) // 4
            
            if total_tokens + chunk_tokens > max_tokens:
                break
            
            # Format with metadata for better LLM understanding
            formatted = f"""
[Source {i+1}] {metadata['header_path']}
{text}
"""
            context_parts.append(formatted.strip())
            total_tokens += chunk_tokens
        
        return "\n\n".join(context_parts)


# Example usage
if __name__ == "__main__":
    # Initialize retriever
    retriever = RAGRetriever()
    
    # Test queries
    test_queries = [
        "How do I send an SMS in n8n?",
        "How to use Python in Code node?",
        "What are the breaking changes in n8n v1.0?",
        "How to configure AWS Secrets Manager?"
    ]
    
    for query in test_queries:
        print("\n" + "=" * 70)
        print(f"Query: {query}")
        print("=" * 70)
        
        results = retriever.retrieve(query, top_k=3)
        
        for i, result in enumerate(results):
            print(f"\nResult #{i+1} (distance: {result['distance']:.4f}):")
            print(f"  Header: {result['metadata']['header_path']}")
            print(f"  Section: {result['metadata']['section_type']}")
            print(f"  Preview: {result['text'][:100]}...")
        
        # Show formatted context
        print("\n--- Formatted Context for LLM ---")
        context = retriever.format_context(results, max_tokens=500)
        print(context[:300] + "...")
