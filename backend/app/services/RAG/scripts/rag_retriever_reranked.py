"""
Enhanced RAG Retriever with Cross-Encoder Re-ranking.
Fixes the poor semantic search results by re-ranking with a more powerful model.
"""

import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder
from typing import List, Dict, Optional


class RAGRetrieverWithReranking:
    """RAG retriever with two-stage retrieval: FAISS + Cross-Encoder re-ranking."""
    
    def __init__(
        self,
        vector_store_path: str = None,
        metadata_path: str = None,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):
        """
        Initialize retriever with re-ranking capability.
        
        Args:
            vector_store_path: Path to FAISS index
            metadata_path: Path to metadata pickle
            embedding_model: Sentence transformer for initial retrieval
            reranker_model: Cross-encoder for re-ranking
        """
        # Default paths
        if vector_store_path is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            vector_store_path = os.path.join(script_dir, "..", "data", "vector_store", "faiss.index")
        
        if metadata_path is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            metadata_path = os.path.join(script_dir, "..", "data", "vector_store", "metadata.pkl")
        
        self.vector_store_path = vector_store_path
        self.metadata_path = metadata_path
        
        # Load models
        print(f"Loading embedding model: {embedding_model}...")
        self.embedding_model = SentenceTransformer(embedding_model)
        
        print(f"Loading re-ranker model: {reranker_model}...")
        self.reranker = CrossEncoder(reranker_model)
        
        # Load FAISS index and metadata
        print(f"Loading FAISS index from {vector_store_path}...")
        self.index = faiss.read_index(vector_store_path)
        
        print(f"Loading metadata from {metadata_path}...")
        with open(metadata_path, 'rb') as f:
            data = pickle.load(f)
            self.metadata_list = data['metadata']
            self.text_list = data['texts']
        
        print(f"✅ Loaded {self.index.ntotal} vectors with {len(self.metadata_list)} metadata entries")
        
        # Query expansion synonyms (same as before)
        self.synonym_map = {
            # Messaging services
            "telegram": ["telegram", "telegram trigger", "telegram bot"],
            "slack": ["slack", "slack trigger", "slack message"],
            "discord": ["discord", "discord webhook"],
            "whatsapp": ["whatsapp", "whatsapp business"],
            
            # Databases
            "database": ["database", "db", "storage", "data store"],
            "mongodb": ["mongodb", "mongo", "nosql"],
            "postgres": ["postgres", "postgresql", "sql"],
            "mysql": ["mysql", "sql"],
            "redis": ["redis", "cache"],
            
            # Actions
            "store": ["store", "save", "insert", "write", "persist"],
            "send": ["send", "post", "publish", "push"],
            "get": ["get", "fetch", "retrieve", "read"],
            "update": ["update", "modify", "change"],
            "delete": ["delete", "remove", "drop"],
            
            # Workflow concepts
            "message": ["message", "msg", "text", "content"],
            "trigger": ["trigger", "listener", "webhook", "event"],
            "workflow": ["workflow", "automation", "flow"],
        }
    
    def expand_query(self, query: str) -> str:
        """Expand query with synonyms (same as before)."""
        query_lower = query.lower()
        expanded_terms = [query_lower]
        
        for keyword, synonyms in self.synonym_map.items():
            if keyword in query_lower:
                expanded_terms.extend(synonyms)
        
        # Remove duplicates while preserving some order
        expanded_terms = list(dict.fromkeys(expanded_terms))
        return " ".join(expanded_terms)
    
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        expand_query: bool = True,
        use_reranking: bool = True,
        initial_candidates: int = 20
    ) -> List[Dict]:
        """
        Retrieve relevant chunks with two-stage process:
        1. FAISS retrieval (fast, get top 20)
        2. Cross-encoder re-ranking (slow but accurate, get top 5)
        
        Args:
            query: User query
            top_k: Final number of results to return
            expand_query: Whether to expand query with synonyms
            use_reranking: Whether to use cross-encoder re-ranking
            initial_candidates: Number of candidates to retrieve before re-ranking
        
        Returns:
            List of dicts with text, metadata, distance, and rerank_score
        """
        # Step 1: Query expansion (optional)
        search_query = self.expand_query(query) if expand_query else query
        
        print(f"Original query: {query}")
        if expand_query:
            print(f"Expanded query: {search_query}")
        
        # Step 2: Initial FAISS retrieval (get more candidates for re-ranking)
        retrieve_count = initial_candidates if use_reranking else top_k
        query_embedding = self.embedding_model.encode([search_query])
        
        distances, indices = self.index.search(
            np.array(query_embedding).astype('float32'),
            retrieve_count
        )
        
        # Build initial results
        candidates = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.metadata_list):
                chunk_meta = self.metadata_list[idx]
                chunk_text = self.text_list[idx]
                candidates.append({
                    'text': chunk_text,
                    'metadata': chunk_meta,
                    'distance': float(dist),
                    'relevance_score': 1 / (1 + dist)  # Lower distance = higher score
                })
        
        # Step 3: Cross-encoder re-ranking (if enabled)
        if use_reranking and len(candidates) > 0:
            print(f"\n🔍 Re-ranking {len(candidates)} candidates with cross-encoder...")
            
            # Prepare pairs for re-ranking
            pairs = [[query, candidate['text'][:1000]] for candidate in candidates]
            
            # Get re-ranking scores
            rerank_scores = self.reranker.predict(pairs)
            
            # Add rerank scores to candidates
            for candidate, score in zip(candidates, rerank_scores):
                candidate['rerank_score'] = float(score)
            
            # Sort by rerank score (higher is better)
            candidates.sort(key=lambda x: x['rerank_score'], reverse=True)
            
            print(f"✅ Re-ranking complete")
            print("\nTop 5 after re-ranking:")
            for i, c in enumerate(candidates[:5], 1):
                header = c['metadata'].get('header_path', 'Unknown')
                node_type = c['metadata'].get('node_type', 'unknown')
                integrations = c['metadata'].get('integrations', [])
                print(f"  {i}. {header[:60]}")
                print(f"     Original distance: {c['distance']:.3f} | Rerank score: {c['rerank_score']:.3f}")
                print(f"     Node type: {node_type} | Integrations: {integrations}")
        
        # Return top k results
        return candidates[:top_k]
    
    def search_by_metadata(
        self,
        query: str,
        node_type: Optional[str] = None,
        integrations: Optional[List[str]] = None,
        workflow_patterns: Optional[List[str]] = None,
        top_k: int = 5
    ) -> List[Dict]:
        """
        Search with metadata filters.
        
        Args:
            query: User query
            node_type: Filter by node type (trigger, action, core)
            integrations: Filter by integrations (telegram, mongodb, etc.)
            workflow_patterns: Filter by patterns (message_to_storage, etc.)
            top_k: Number of results
        
        Returns:
            Filtered and ranked results
        """
        # Get more candidates for filtering
        candidates = self.retrieve(
            query=query,
            top_k=50,
            use_reranking=True,
            initial_candidates=100
        )
        
        # Apply filters
        filtered = []
        for candidate in candidates:
            meta = candidate['metadata']
            
            # Node type filter
            if node_type and meta.get('node_type') != node_type:
                continue
            
            # Integration filter
            if integrations:
                candidate_integrations = meta.get('integrations', [])
                if not any(integration in candidate_integrations for integration in integrations):
                    continue
            
            # Workflow pattern filter
            if workflow_patterns:
                candidate_patterns = meta.get('workflow_patterns', [])
                if not any(pattern in candidate_patterns for pattern in workflow_patterns):
                    continue
            
            filtered.append(candidate)
            
            if len(filtered) >= top_k:
                break
        
        return filtered


if __name__ == "__main__":
    print("Testing RAG Retriever with Re-ranking")
    print("=" * 80)
    print()
    
    # Initialize retriever
    retriever = RAGRetrieverWithReranking()
    print()
    
    # Test queries
    test_queries = [
        "i want to take the message from telegram and store it at a database",
        "How many auth parameters for Google Drive?",
        "Send notifications to Slack when error occurs"
    ]
    
    for query in test_queries:
        print("\n" + "=" * 80)
        print(f"Query: {query}")
        print("=" * 80)
        
        # Compare with and without re-ranking
        print("\n--- Without Re-ranking (baseline) ---")
        results_no_rerank = retriever.retrieve(query, top_k=5, use_reranking=False)
        for i, result in enumerate(results_no_rerank, 1):
            header = result['metadata'].get('header_path', 'Unknown')
            print(f"{i}. {header[:70]} (distance: {result['distance']:.3f})")
        
        print("\n--- With Re-ranking (enhanced) ---")
        results_rerank = retriever.retrieve(query, top_k=5, use_reranking=True)
        
        print("\n📊 Improvement Analysis:")
        print(f"  - Top result changed: {results_no_rerank[0]['metadata'].get('header_path') != results_rerank[0]['metadata'].get('header_path')}")
        print(f"  - Telegram mentioned in top 3 (no rerank): {any('telegram' in r['metadata'].get('integrations', []) for r in results_no_rerank[:3])}")
        print(f"  - Telegram mentioned in top 3 (rerank): {any('telegram' in r['metadata'].get('integrations', []) for r in results_rerank[:3])}")
