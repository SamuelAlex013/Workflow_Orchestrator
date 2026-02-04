"""
Enhanced LLM Service with multiple backend support.
Supports: Gemini API (cloud), Ollama/Llama 3.2 (local)
Automatically fallback between providers.
"""

import os
from typing import List, Dict, Optional
import requests


class LLMService:
    """Service for generating answers using multiple LLM backends."""
    
    def __init__(self, backend: str = "auto", api_key: Optional[str] = None, ollama_url: str = "http://localhost:11434"):
        """
        Initialize LLM service with auto-detection or specific backend.
        
        Args:
            backend: "auto" (try local first), "gemini", "ollama", or "llama"
            api_key: Google API key for Gemini (optional)
            ollama_url: URL for Ollama server (default: localhost:11434)
        """
        self.backend = backend
        self.ollama_url = ollama_url
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        
        # Try to initialize backends
        self._init_backends()
    
    def _init_backends(self):
        """Initialize available backends."""
        self.gemini_available = False
        self.ollama_available = False
        
        # Check Ollama
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            if response.status_code == 200:
                models = response.json().get("models", [])
                # Prefer smaller models that fit in memory
                # Priority: deepseek-r1:1.5b > phi3 > gemma3
                if any("llama3.2" in m.get("name", "") for m in models):
                    self.ollama_available = True
                    self.model = "deepseek-r1:1.5b"
                    print(f"✅ Ollama detected with DeepSeek-R1 1.5B (memory-efficient)")
                elif any("phi3" in m.get("name", "") for m in models):
                    self.ollama_available = True
                    self.model = "phi3"
                    print(f"✅ Ollama detected with Phi-3")
                elif any("gemma3:270m" in m.get("name", "") for m in models):
                    self.ollama_available = True
                    self.model = "gemma3:270m"
                    print(f"✅ Ollama detected with Gemma3 270M")
                elif any("llama3.2" in m.get("name", "") for m in models):
                    self.ollama_available = True
                    self.model = "llama3.2"
                    print(f"⚠️  Using Llama 3.2 (may require more RAM)")
        except Exception as e:
            print(f"⚠️  Ollama not available: {e}")
        
        # Check Gemini
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.genai = genai
                self.gemini_available = True
                self.gemini_model = "gemini-2.5-flash"
                print(f"✅ Gemini API available")
            except Exception as e:
                print(f"⚠️  Gemini not available: {e}")
        
        # Determine active backend
        if self.backend == "auto":
            if self.ollama_available:
                self.active_backend = "ollama"
                print("🎯 Using Ollama (local) as primary LLM")
            elif self.gemini_available:
                self.active_backend = "gemini"
                print("🎯 Using Gemini API as primary LLM")
            else:
                raise ValueError(
                    "No LLM backend available!\n"
                    "Install Ollama: https://ollama.com/download\n"
                    "Then run: ollama pull llama3.2\n"
                    "OR set GOOGLE_API_KEY environment variable"
                )
        elif self.backend == "ollama" or self.backend == "llama":
            if not self.ollama_available:
                raise ValueError("Ollama not available. Run: ollama pull llama3.2")
            self.active_backend = "ollama"
        elif self.backend == "gemini":
            if not self.gemini_available:
                raise ValueError("Gemini not available. Set GOOGLE_API_KEY")
            self.active_backend = "gemini"
    
    def _call_ollama(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float) -> str:
        """Call Ollama API."""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": f"{system_prompt}\n\n{prompt}",
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "num_predict": max_tokens
                    }
                },
                timeout=120  # Increase timeout for longer generations
            )
            
            if response.status_code != 200:
                error_detail = response.text
                print(f"❌ Ollama API error: {response.status_code}")
                print(f"   Error details: {error_detail}")
                raise ValueError(f"Ollama API returned {response.status_code}: {error_detail}")
            
            result = response.json()
            return result.get("response", "")
            
        except requests.exceptions.Timeout:
            raise ValueError("Ollama request timed out. The model may be overloaded or the query too complex.")
        except requests.exceptions.ConnectionError:
            raise ValueError("Cannot connect to Ollama. Make sure Ollama is running (ollama serve).")
        except Exception as e:
            print(f"❌ Unexpected error calling Ollama: {e}")
            raise
    
    def _call_gemini(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float) -> str:
        """Call Gemini API."""
        model = self.genai.GenerativeModel(
            model_name=self.gemini_model,
            generation_config=self.genai.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            ),
            system_instruction=system_prompt
        )
        response = model.generate_content(prompt)
        return response.text
    
    def synthesize_answer(
        self,
        query: str,
        context_chunks: List[Dict],
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> Dict[str, any]:
        """
        Synthesize an answer from RAG context using available LLM.
        
        Args:
            query: User's original question
            context_chunks: Retrieved chunks from RAG
            max_tokens: Maximum tokens in response
            temperature: Response randomness (0-1)
        
        Returns:
            {
                'answer': str,
                'sources': List[str],
                'confidence': str,
                'model': str,
                'backend': str
            }
        """
        # Build context
        context_parts = []
        sources = []
        
        for i, chunk in enumerate(context_chunks[:5], 1):
            metadata = chunk.get('metadata', {})
            text = chunk.get('text', '')
            header_path = metadata.get('header_path', 'Unknown')
            sources.append(header_path)
            context_parts.append(f"[Source {i}: {header_path}]\n{text}")
        
        context = "\n\n".join(context_parts)
        
        # Calculate confidence
        avg_distance = sum(c.get('distance', 1.0) for c in context_chunks[:5]) / min(5, len(context_chunks))
        confidence = "high" if avg_distance < 0.5 else ("medium" if avg_distance < 0.8 else "low")
        
        # Build prompts
        system_prompt = """You are an expert n8n workflow automation assistant. Your role is to help users understand how to build workflows in n8n by providing clear, accurate answers based on the official documentation.

Guidelines:
1. Answer the user's question using ONLY the provided documentation context
2. Be specific and actionable - include configuration steps, node names, and parameters
3. If the context contains code examples or templates, include them
4. If multiple approaches exist, mention all of them
5. If the context doesn't fully answer the question, acknowledge what's missing
6. For workflow-building questions, suggest a step-by-step approach
7. Always cite which documentation sections you're referencing"""

        user_prompt = f"""User Question: {query}

Documentation Context:
{context}

Please provide a comprehensive answer to the user's question based on the documentation above. If this is a workflow-building question (e.g., "I want to take messages from X and store in Y"), provide:
1. Required nodes and their configuration
2. Step-by-step workflow structure
3. Any authentication/credentials needed
4. Example configurations if available

Note: Do NOT make up information not present in the documentation context.
Also avoid using phrases like "from the documentation" in your answer.


Answer:"""

        # Call LLM
        try:
            if self.active_backend == "ollama":
                answer = self._call_ollama(user_prompt, system_prompt, max_tokens, temperature)
                model_name = f"llama3.2 (local)"
            else:  # gemini
                answer = self._call_gemini(user_prompt, system_prompt, max_tokens, temperature)
                model_name = self.gemini_model
            
            return {
                "answer": answer,
                "sources": sources,
                "confidence": confidence,
                "model": model_name,
                "backend": self.active_backend
            }
        
        except Exception as e:
            # Fallback to other backend if available
            if self.active_backend == "ollama" and self.gemini_available:
                print(f"⚠️  Ollama failed, falling back to Gemini: {e}")
                try:
                    answer = self._call_gemini(user_prompt, system_prompt, max_tokens, temperature)
                    return {
                        "answer": answer,
                        "sources": sources,
                        "confidence": confidence,
                        "model": f"{self.gemini_model} (fallback)",
                        "backend": "gemini"
                    }
                except Exception as e2:
                    return self._error_response(str(e2), sources)
            elif self.active_backend == "gemini" and self.ollama_available:
                print(f"⚠️  Gemini failed, falling back to Ollama: {e}")
                try:
                    answer = self._call_ollama(user_prompt, system_prompt, max_tokens, temperature)
                    return {
                        "answer": answer,
                        "sources": sources,
                        "confidence": confidence,
                        "model": "llama3.2 (fallback)",
                        "backend": "ollama"
                    }
                except Exception as e2:
                    return self._error_response(str(e2), sources)
            else:
                return self._error_response(str(e), sources)
    
    def _error_response(self, error: str, sources: List[str]) -> Dict:
        """Create error response."""
        return {
            "answer": f"Error calling LLM: {error}",
            "sources": sources,
            "confidence": "error",
            "model": self.active_backend if hasattr(self, 'active_backend') else "unknown",
            "backend": "error"
        }
    
    def synthesize_answer_stream(
        self,
        query: str,
        context_chunks: List[Dict],
        max_tokens: int = 1000,
        temperature: float = 0.7
    ):
        """
        Stream answer tokens from RAG context using available LLM.
        Yields tokens as they are generated.
        """
        # Build context
        context_parts = []
        for i, chunk in enumerate(context_chunks[:5], 1):
            metadata = chunk.get('metadata', {})
            text = chunk.get('text', '')
            header_path = metadata.get('header_path', 'Unknown')
            context_parts.append(f"[Source {i}: {header_path}]\n{text}")
        
        context = "\n\n".join(context_parts)
        
        # Build prompts
        system_prompt = """You are an expert n8n workflow automation assistant. Your role is to help users understand how to build workflows in n8n by providing clear, accurate answers based on the official documentation.

Guidelines:
1. Answer the user's question using ONLY the provided documentation context
2. Be specific and actionable - include configuration steps, node names, and parameters
3. If the context contains code examples or templates, include them
4. If multiple approaches exist, mention all of them
5. If the context doesn't fully answer the question, acknowledge what's missing
6. For workflow-building questions, suggest a step-by-step approach
7. Always cite which documentation sections you're referencing"""

        user_prompt = f"""User Question: {query}

Documentation Context:
{context}

Please provide a comprehensive answer to the user's question based on the documentation above. If this is a workflow-building question (e.g., "I want to take messages from X and store in Y"), provide:
1. Required nodes and their configuration
2. Step-by-step workflow structure
3. Any authentication/credentials needed
4. Example configurations if available

Note: Do NOT make up information not present in the documentation context.
Also avoid using phrases like "from the documentation" in your answer.


Answer:"""

        # Stream from appropriate backend
        if self.active_backend == "ollama":
            yield from self._stream_ollama(user_prompt, system_prompt, max_tokens, temperature)
        else:
            yield from self._stream_gemini(user_prompt, system_prompt, max_tokens, temperature)
    
    def _stream_ollama(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float):
        """Stream from Ollama API."""
        token_count = 0
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": f"{system_prompt}\n\n{prompt}",
                    "stream": True,
                    "options": {
                        "temperature": temperature,
                        "num_predict": max_tokens,
                        "num_ctx": 4096  # Increase context window
                    }
                },
                stream=True,
                timeout=(10, 600)  # (connect timeout, read timeout) - even longer for big responses
            )
            
            if response.status_code != 200:
                yield f"Error: Ollama API returned {response.status_code}"
                return
            
            import json
            # Use iter_lines with decode_unicode for better streaming
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        data = json.loads(line)
                        token = data.get("response", "")
                        if token:
                            token_count += 1
                            yield token
                        if data.get("done", False):
                            print(f"\n✅ Ollama stream completed: {token_count} tokens")
                            break
                    except json.JSONDecodeError:
                        continue
            
            # If we exit without 'done', log it
            print(f"\n⚠️ Ollama stream ended (total tokens: {token_count})")
                        
        except requests.exceptions.Timeout:
            yield "\n\n[Response timed out. Please try a shorter query.]"
        except requests.exceptions.ConnectionError:
            yield "\n\n[Connection lost to Ollama. Please check if Ollama is running.]"
        except Exception as e:
            yield f"\n\n[Error streaming from Ollama: {str(e)}]"
    
    def _stream_gemini(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float):
        """Stream from Gemini API."""
        try:
            model = self.genai.GenerativeModel(
                model_name=self.gemini_model,
                generation_config=self.genai.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                ),
                system_instruction=system_prompt
            )
            
            response = model.generate_content(prompt, stream=True)
            
            for chunk in response:
                try:
                    if chunk.text:
                        yield chunk.text
                except ValueError:
                    # Handle safety filter or other issues with individual chunks
                    continue
                    
        except Exception as e:
            yield f"\n\n[Error streaming from Gemini: {str(e)}]"

    def generate_workflow_description(
        self,
        query: str,
        context_chunks: List[Dict]
    ) -> Dict[str, any]:
        """Generate structured workflow description."""
        # Build context
        context_parts = []
        for chunk in context_chunks[:5]:
            text = chunk.get('text', '')
            metadata = chunk.get('metadata', {})
            integrations = metadata.get('integrations', [])
            node_type = metadata.get('node_type', 'unknown')
            context_parts.append(
                f"[Node Type: {node_type}, Integrations: {', '.join(integrations)}]\n{text[:500]}"
            )
        
        context = "\n\n".join(context_parts)
        
        system_prompt = """You are an n8n workflow architect. Design clear, actionable workflow structures.
Output must be structured with clear sections. Keep it concise."""

        user_prompt = f"""User Request: {query}

Relevant n8n Documentation:
{context}

Design a workflow with this EXACT format:

DESCRIPTION:
[1-2 sentences describing what this workflow does]

NODES:
- NodeName1: purpose
- NodeName2: purpose
- NodeName3: purpose

STEPS:
1. Step description with node config
2. Step description with node config
3. Step description with node config

Note: Do NOT make up information not present in the documentation context.
Also avoid using phrases like "from the documentation" in your answer.
"""

        try:
            if self.active_backend == "ollama":
                response_text = self._call_ollama(user_prompt, system_prompt, 800, 0.5)
                model_name = f"{self.model} (local)"
            else:
                response_text = self._call_gemini(user_prompt, system_prompt, 800, 0.5)
                model_name = self.gemini_model
            
            # Parse response into sections
            description = ""
            required_nodes = []
            structure = ""
            
            lines = response_text.split('\n')
            current_section = None
            
            for line in lines:
                line_stripped = line.strip()
                line_upper = line_stripped.upper()
                
                # Detect section headers
                if line_upper.startswith('DESCRIPTION:') or line_upper.startswith('**DESCRIPTION'):
                    current_section = 'description'
                    continue
                elif line_upper.startswith('NODES:') or line_upper.startswith('**NODES') or line_upper.startswith('**REQUIRED NODES'):
                    current_section = 'nodes'
                    continue
                elif line_upper.startswith('STEPS:') or line_upper.startswith('**STEPS') or line_upper.startswith('**WORKFLOW STRUCTURE'):
                    current_section = 'steps'
                    continue
                
                # Collect content based on section
                if current_section == 'description' and line_stripped:
                    description += line_stripped + " "
                elif current_section == 'nodes' and line_stripped:
                    # Extract node names from lines like "- NodeName: purpose" or "1. NodeName - purpose"
                    if line_stripped.startswith(('-', '*', '•')) or (line_stripped[0].isdigit() and '.' in line_stripped[:3]):
                        # Remove leading markers
                        node_line = line_stripped.lstrip('-*•0123456789. ')
                        # Extract node name (before : or -)
                        if ':' in node_line:
                            node_name = node_line.split(':')[0].strip()
                        elif ' - ' in node_line:
                            node_name = node_line.split(' - ')[0].strip()
                        else:
                            node_name = node_line.split()[0] if node_line.split() else ""
                        
                        if node_name and len(node_name) > 1:
                            required_nodes.append(node_name)
                elif current_section == 'steps' and line_stripped:
                    structure += line + "\n"
            
            # Fallback if parsing failed
            if not description:
                description = response_text[:200] + "..."
            if not structure:
                structure = response_text
            
            return {
                "workflow_description": description.strip(),
                "required_nodes": required_nodes[:10],  # Limit to 10 nodes
                "suggested_structure": structure.strip(),
                "model": model_name
            }
        
        except Exception as e:
            return {
                "workflow_description": f"Error: {str(e)}",
                "required_nodes": [],
                "suggested_structure": "",
                "model": self.active_backend if hasattr(self, 'active_backend') else "unknown"
            }


# Singleton instance
_llm_service: Optional[LLMService] = None

def get_llm_service(backend: str = "auto", api_key: Optional[str] = None) -> LLMService:
    """Get or create LLM service singleton."""
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService(backend=backend, api_key=api_key)
    return _llm_service


if __name__ == "__main__":
    import sys
    
    # Test LLM service with auto-detection
    print("Testing LLM Service (auto-detection)...\n")
    
    try:
        llm = LLMService(backend="auto")
        
        # Mock context
        test_chunks = [
            {
                "text": "The Telegram Trigger node starts a workflow when a message is received...",
                "metadata": {
                    "header_path": "Telegram Trigger node",
                    "integrations": ["telegram"],
                    "node_type": "trigger"
                },
                "distance": 0.4
            },
            {
                "text": "The MongoDB node allows you to insert, update, and delete documents...",
                "metadata": {
                    "header_path": "MongoDB node > Operations",
                    "integrations": ["mongodb"],
                    "node_type": "action"
                },
                "distance": 0.5
            }
        ]
        
        print("Testing answer synthesis...")
        result = llm.synthesize_answer(
            query="How do I take Telegram messages and store them in MongoDB?",
            context_chunks=test_chunks
        )
        
        print(f"\n✅ Answer ({result['backend']}): {result['answer'][:200]}...")
        print(f"📚 Sources: {result['sources']}")
        print(f"🎯 Confidence: {result['confidence']}")
        print(f"🤖 Model: {result['model']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTo use this service:")
        print("1. Install Ollama: https://ollama.com/download")
        print("2. Run: ollama pull llama3.2")
        print("3. OR set GOOGLE_API_KEY environment variable")
        sys.exit(1)
