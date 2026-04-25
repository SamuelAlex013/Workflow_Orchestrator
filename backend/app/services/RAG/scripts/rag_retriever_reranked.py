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
            
            # Databases - expanded to focus on NODES not internal config
            "database": ["database node", "db node", "mysql node", "postgres node", "mongodb node", "redis node", "sql node", "database integration"],
            "mongodb": ["mongodb node", "mongodb", "mongo", "nosql"],
            "postgres": ["postgres node", "postgresql node", "postgres", "postgresql", "sql"],
            "mysql": ["mysql node", "mysql", "sql", "mariadb node"],
            "redis": ["redis node", "redis", "cache"],
            "sql": ["sql", "mysql node", "postgres node", "mssql node", "sqlite node", "database node"],
            
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
            
            # Code/Programming - NEW
            "javascript": ["javascript", "js", "code node", "code", "script", "function"],
            "python": ["python", "code node", "code", "script", "pyodide"],
            "code": ["code node", "code", "javascript", "python", "script", "function", "custom code"],
            "script": ["script", "code node", "code", "javascript", "python"],
            "function": ["function", "code node", "code", "javascript"],
            
            # Expressions
            "expression": ["expression", "expressions", "javascript", "dynamic", "transform"],
            
            # Integration listing queries
            "list": ["list", "all", "available", "supported", "nodes", "integrations"],
            "integrations": ["integrations", "nodes", "connectors", "apps"],
        }
        
        # Terms that indicate user wants integration nodes, NOT internal config
        self.node_intent_keywords = ["use", "connect", "integrate", "node", "through", "with", "via", "from"]
        
        # Chunks to deprioritize (internal config, not integration nodes)
        self.config_doc_patterns = [
            "database considerations", "database structure", "supported databases",
            "database type by", "mysql and mariadb deprecation", "prerequisites",
            "installation", "configuration", "requirements", "hosting"
        ]
    
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
    
    def _extract_important_keywords(self, query: str) -> List[str]:
        """
        Extract important keywords from query for boosting.
        Focus on technical terms, node names, and specific concepts.
        """
        query_lower = query.lower()
        keywords = []
        
        # Technical terms to look for
        important_terms = [
            # Programming languages
            'javascript', 'python', 'js', 'code',
            # Node names
            'code node', 'function', 'webhook', 'http request',
            # Concepts
            'expression', 'expressions', 'transform', 'data',
            # Services
            'api', 'http', 'rest', 'graphql',
            # Common actions
            'send', 'receive', 'store', 'get', 'post',
        ]
        
        for term in important_terms:
            if term in query_lower:
                keywords.append(term)
        
        # Also extract potential node names (capitalized words)
        words = query.split()
        for word in words:
            word_clean = word.strip('.,!?').lower()
            # Keep technical terms that might be node-specific
            if len(word_clean) > 2 and word_clean not in ['the', 'and', 'how', 'use', 'can', 'what', 'for']:
                if word_clean in ['javascript', 'python', 'code', 'workflow', 'node', 'expression']:
                    keywords.append(word_clean)
        
        return list(set(keywords))  # Remove duplicates
    
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
        
        #print(f"Original query: {query}")
        # if expand_query:
        #     print(f"Expanded query: {search_query}")
        
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
           # print(f"\n🔍 Re-ranking {len(candidates)} candidates with cross-encoder...")
            
            # Prepare pairs for re-ranking
            pairs = [[query, candidate['text'][:1000]] for candidate in candidates]
            
            # Get re-ranking scores
            rerank_scores = self.reranker.predict(pairs)
            
            # Add rerank scores to candidates
            for candidate, score in zip(candidates, rerank_scores):
                candidate['rerank_score'] = float(score)
            
            # Step 3.4: Detect if user wants integration nodes (not internal config)
            query_lower = query.lower()
            wants_nodes = any(kw in query_lower for kw in self.node_intent_keywords)
            
            # Penalize config docs when user wants nodes
            if wants_nodes:
                for candidate in candidates:
                    header_lower = candidate['metadata'].get('header_path', '').lower()
                    text_lower = candidate['text'].lower()
                    
                    # Check if this is a config doc (not an integration node)
                    is_config_doc = any(pattern in header_lower for pattern in self.config_doc_patterns)
                    
                    # Check if chunk actually mentions node integrations (positive signal)
                    has_node_mentions = any(term in text_lower for term in [
                        'node', 'nodes', 'integration', 'credential', 'execute', 'operation'
                    ])
                    
                    # Check for actual database node patterns
                    has_db_node_ref = any(term in text_lower for term in [
                        'mongodb', 'mysql node', 'postgres node', 'redis node', 'airtable', 
                        'google sheets', 'supabase', 'notion', 'firebase', 'fauna',
                        'microsoft sql', 'mssql', 'questdb', 'timescaledb', 'cratedb',
                        'n8n-nodes-base', 'app-nodes'
                    ])
                    
                    if is_config_doc and not has_db_node_ref:
                        # Heavy penalty for pure config docs
                        candidate['rerank_score'] -= 8.0
                        candidate['config_penalty'] = -8.0
                       # print(f"   ⚠️ Config doc penalty: {header_lower[:60]}")
                    elif has_db_node_ref:
                        # Boost chunks that reference actual database nodes
                        candidate['rerank_score'] += 3.0
                        candidate['node_boost'] = 3.0
                       # print(f"   ✅ DB node boost: {header_lower[:60]}")
            
            # Step 3.5: Apply keyword boost - boost chunks that contain important query keywords
            query_keywords = self._extract_important_keywords(query)
            if query_keywords:
                #print(f"   Applying keyword boost for: {query_keywords}")
                for candidate in candidates:
                    text_lower = candidate['text'].lower()
                    header_lower = candidate['metadata'].get('header_path', '').lower()
                    
                    # Count keyword matches
                    keyword_matches = sum(1 for kw in query_keywords if kw in text_lower or kw in header_lower)
                    
                    # Boost score based on keyword matches (0.5 per match, max 2.0 boost)
                    boost = min(keyword_matches * 0.5, 2.0)
                    candidate['rerank_score'] += boost
                    candidate['keyword_boost'] = boost
            
            # Sort by rerank score (higher is better)
            candidates.sort(key=lambda x: x['rerank_score'], reverse=True)
            
            # print(f"✅ Re-ranking complete")
            # print("\nTop 5 after re-ranking:")
            for i, c in enumerate(candidates[:5], 1):
                header = c['metadata'].get('header_path', 'Unknown')
                node_type = c['metadata'].get('node_type', 'unknown')
                boost = c.get('keyword_boost', 0)
               # print(f"  {i}. {header[:60]}")
                #print(f"     Score: {c['rerank_score']:.3f} (keyword boost: +{boost:.1f}) | Type: {node_type}")
        
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
