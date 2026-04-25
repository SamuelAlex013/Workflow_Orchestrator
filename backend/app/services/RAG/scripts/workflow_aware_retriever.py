"""
Smart multi-concept workflow retrieval.
Detects when user needs multiple node types (trigger + action) and retrieves both.
"""

from .rag_retriever_reranked import RAGRetrieverWithReranking
from typing import List, Dict
import re


class WorkflowAwareRetriever(RAGRetrieverWithReranking):
    """
    Extension of re-ranking retriever that understands workflow patterns.
    Automatically detects multi-step workflows and retrieves appropriate node types.
    """
    
    def detect_workflow_intent(self, query: str) -> Dict[str, any]:
        """
        Analyze query to detect workflow structure.
        
        Returns:
            {
                'is_workflow': bool,
                'trigger_integration': str or None,
                'action_integration': str or None,
                'action_type': str or None
            }
        """
        query_lower = query.lower()
        
        # Trigger keywords
        trigger_keywords = {
            'receive', 'get', 'when', 'listen', 'watch', 'trigger',
            'incoming', 'new', 'from'
        }
        
        # Action keywords
        action_keywords = {
            'store', 'save', 'send', 'write', 'insert', 'create',
            'update', 'post', 'publish', 'to', 'in', 'into'
        }
        
        # Integration detection
        integrations = {
            'telegram': ['telegram'],
            'slack': ['slack'],
            'discord': ['discord'],
            'email': ['email', 'gmail', 'smtp'],
            'mongodb': ['mongodb', 'mongo'],
            'postgres': ['postgres', 'postgresql'],
            'mysql': ['mysql'],
            'database': ['database', 'db'],
            'airtable': ['airtable'],
            'google sheets': ['google sheets', 'sheets'],
        }
        
        has_trigger = any(kw in query_lower for kw in trigger_keywords)
        has_action = any(kw in query_lower for kw in action_keywords)
        
        detected_integrations = []
        for integration, keywords in integrations.items():
            if any(kw in query_lower for kw in keywords):
                detected_integrations.append(integration)
        
        # Workflow pattern detection
        is_workflow = has_trigger and has_action and len(detected_integrations) >= 2
        
        # Extract trigger and action integrations
        trigger_integration = None
        action_integration = None
        action_type = None
        
        if is_workflow:
            # Pattern: "from X" or "receive from X" = trigger
            # Pattern: "to Y" or "store in Y" = action
            
            for integration in detected_integrations:
                # Check if it's a trigger (messaging service)
                if integration in ['telegram', 'slack', 'discord', 'email']:
                    trigger_integration = integration
                
                # Check if it's an action (database/storage)
                if integration in ['mongodb', 'postgres', 'mysql', 'database', 'airtable', 'google sheets']:
                    action_integration = integration
                    action_type = 'database'
        
        return {
            'is_workflow': is_workflow,
            'trigger_integration': trigger_integration,
            'action_integration': action_integration,
            'action_type': action_type,
            'detected_integrations': detected_integrations
        }
    
    def retrieve_workflow_nodes(
        self,
        query: str,
        top_k: int = 5,
        use_reranking: bool = True
    ) -> List[Dict]:
        """
        Smart retrieval for workflow queries.
        Returns mix of trigger + action nodes if workflow pattern detected.
        
        Args:
            query: User query
            top_k: Total results to return
            use_reranking: Whether to use cross-encoder
        
        Returns:
            List of chunks with trigger nodes first, then action nodes
        """
        # Detect workflow intent
        intent = self.detect_workflow_intent(query)
        
        # print(f"\n🔍 Workflow Intent Analysis:")
        # print(f"   Is workflow: {intent['is_workflow']}")
        # print(f"   Trigger integration: {intent['trigger_integration']}")
        # print(f"   Action integration: {intent['action_integration']}")
        # print(f"   Detected integrations: {intent['detected_integrations']}")
        
        if not intent['is_workflow']:
            # Single-concept query - use normal retrieval
            return super().retrieve(query, top_k, expand_query=True, use_reranking=use_reranking)
        
        # Multi-concept workflow - retrieve trigger + action separately
        trigger_results = []
        action_results = []
        
        # Get trigger nodes
        if intent['trigger_integration']:
            print(f"\n🎯 Retrieving TRIGGER nodes for {intent['trigger_integration']}...")
            trigger_query = f"{intent['trigger_integration']} trigger receive message webhook"
            trigger_candidates = super().retrieve(
                trigger_query,
                top_k=30,
                expand_query=True,
                use_reranking=use_reranking,
                initial_candidates=50
            )
            
            # Filter for trigger nodes
            for candidate in trigger_candidates:
                node_type = candidate['metadata'].get('node_type', 'unknown')
                integrations = candidate['metadata'].get('integrations', [])
                
                if (node_type == 'trigger' or 'trigger' in candidate['metadata'].get('header_path', '').lower()) and \
                   intent['trigger_integration'] in integrations:
                    trigger_results.append(candidate)
                    if len(trigger_results) >= top_k // 2:
                        break
        
        # Get action nodes
        if intent['action_integration']:
            print(f"\n🎯 Retrieving ACTION nodes for {intent['action_integration']}...")
            action_query = f"{intent['action_integration']} insert save store write database"
            action_candidates = super().retrieve(
                action_query,
                top_k=30,
                expand_query=True,
                use_reranking=use_reranking,
                initial_candidates=50
            )
            
            # Filter for action nodes with database operations
            for candidate in action_candidates:
                node_type = candidate['metadata'].get('node_type', 'unknown')
                integrations = candidate['metadata'].get('integrations', [])
                header = candidate['metadata'].get('header_path', '').lower()
                
                # Look for database operations or specific integration
                is_database_action = any(keyword in header for keyword in ['operation', 'insert', 'write', 'create', 'save'])
                
                if node_type == 'action' and (is_database_action or intent['action_integration'] in integrations):
                    action_results.append(candidate)
                    if len(action_results) >= top_k // 2:
                        break
        
        # Combine results
        print(f"\n✅ Found {len(trigger_results)} trigger nodes + {len(action_results)} action nodes")
        combined = trigger_results + action_results
        
        # If we didn't find enough, add general results
        if len(combined) < top_k:
            print(f"⚠️  Adding general results to reach top_k={top_k}")
            general_results = super().retrieve(query, top_k=top_k - len(combined), expand_query=True, use_reranking=use_reranking)
            
            # Avoid duplicates
            existing_headers = {c['metadata'].get('header_path') for c in combined}
            for result in general_results:
                if result['metadata'].get('header_path') not in existing_headers:
                    combined.append(result)
                if len(combined) >= top_k:
                    break
        
        return combined[:top_k]


if __name__ == "__main__":
    print("=" * 80)
    print("Testing Workflow-Aware Retriever")
    print("=" * 80)
    print()
    
    # Initialize
    retriever = WorkflowAwareRetriever()
    print()
    
    # Test query
    query = "i want to take the message from telegram and store it at a database"
    
    print("=" * 80)
    print(f"Query: {query}")
    print("=" * 80)
    
    # Get results
    results = retriever.retrieve_workflow_nodes(query, top_k=5, use_reranking=True)
    
    print("\n" + "=" * 80)
    print("FINAL RESULTS (Workflow-Aware)")
    print("=" * 80)
    print()
    
    for i, result in enumerate(results, 1):
        header = result['metadata'].get('header_path', 'Unknown')
        node_type = result['metadata'].get('node_type', 'unknown')
        integrations = result['metadata'].get('integrations', [])
        distance = result['distance']
        rerank_score = result.get('rerank_score', 'N/A')
        
        print(f"{i}. {header}")
        print(f"   Node type: {node_type} | Integrations: {integrations}")
        print(f"   Distance: {distance:.3f} | Rerank: {rerank_score}")
        print()
    
    print("=" * 80)
    print("EVALUATION")
    print("=" * 80)
    print()
    print("✅ Check if results include:")
    print("   1. Telegram Trigger node (to receive messages)")
    print("   2. Database node with insert/write operations")
    print()
    
    has_telegram_trigger = any(
        c['metadata'].get('node_type') == 'trigger' and 'telegram' in c['metadata'].get('integrations', [])
        for c in results
    )
    has_database_action = any(
        c['metadata'].get('node_type') == 'action' and any(
            db in c['metadata'].get('integrations', [])
            for db in ['mongodb', 'postgres', 'mysql']
        )
        for c in results
    )
    
    print(f"   Telegram Trigger found: {'✅ YES' if has_telegram_trigger else '❌ NO'}")
    print(f"   Database action found: {'✅ YES' if has_database_action else '❌ NO'}")
    print()
    
    if has_telegram_trigger and has_database_action:
        print("🎉 SUCCESS! Retrieval now returns BOTH node types needed for the workflow!")
    else:
        print("⚠️  Partial success - some node types still missing")
