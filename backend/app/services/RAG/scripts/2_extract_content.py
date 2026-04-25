import json
import hashlib
from pathlib import Path
import re
import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict, Tuple

BASE_DIR = Path(__file__).resolve().parent

# Preferred source docs locations (first existing file is used)
SOURCE_DOC_CANDIDATES = [
    # Workspace-level docs path used in this repository
    BASE_DIR.parents[4] / "data" / "docs" / "n8n_official_docs.md",
    # Legacy path (kept for backward compatibility)
    BASE_DIR.parent / "docs" / "n8n_official_docs.md",
]

OUTPUT_JSONL = Path(__file__).parent.parent / "data" / "chunks.jsonl"


CHUNK_SIZE = 1500
CHUNK_OVERLAP = 300

HEADERS_TO_SPLIT = [
    ("# ", "h1"),
    ("## ", "h2"),
    ("### ", "h3"),
    ("#### ", "h4"),
    ("##### ", "h5"),
    ("###### ", "h6")
]

def count_tokens(text: str) -> int:
    """Count the number of tokens in a given text using tiktoken."""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def generate_chunk_id(text: str, metadata: dict) -> str:
    """Generate SHA256 hash as chunk ID based on text content and metadata."""
    combined = f"{metadata.get('header_path', '')}{text}"
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()

def detect_code_blocks(text: str) -> bool:
    """Detect if the text contains code blocks."""
    return bool(re.search(r"```[\s\S]*?```", text))

def build_header_path(metadata: dict) -> str:
    """Build breadcrumb path from h1/h2/... headers in metadata."""
    path_parts = []
    for level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        if level in metadata and metadata[level]:
            path_parts.append(metadata[level])
    return " > ".join(path_parts) if path_parts else "root"

def detect_section_type(header_path: str, content: str) -> str:
    """Classify chunk by section type based on header path and content."""
    header_lower = header_path.lower()
    content_lower = content.lower()
    
    # Check for specific section types
    if any(keyword in header_lower for keyword in ["example", "template", "workflow"]):
        return "example"
    elif any(keyword in header_lower for keyword in ["install", "setup", "quickstart", "getting started"]):
        return "installation"
    elif any(keyword in header_lower for keyword in ["api", "credential", "authentication", "configuration"]):
        return "configuration"
    elif any(keyword in header_lower for keyword in ["faq", "troubleshoot", "common issues", "error"]):
        return "troubleshooting"
    elif any(keyword in header_lower for keyword in ["migration", "breaking change", "upgrade"]):
        return "migration"
    elif any(keyword in header_lower for keyword in ["reference", "parameter", "option"]):
        return "reference"
    else:
        return "documentation"

def detect_doc_category(header_path: str) -> str:
    """Detect document category for filtering and prioritization."""
    header_lower = header_path.lower()
    
    if any(keyword in header_lower for keyword in ["enterprise", "external secret", "sso", "ldap"]):
        return "enterprise_features"
    elif any(keyword in header_lower for keyword in ["ai", "agent", "langchain", "vector store"]):
        return "ai_features"
    elif any(keyword in header_lower for keyword in ["integration", "node", "app"]):
        return "integrations"
    elif any(keyword in header_lower for keyword in ["core", "workflow", "execution"]):
        return "core_concepts"
    else:
        return "general"

def detect_node_type(header_path: str, content: str) -> str:
    """Detect n8n node type from header and content."""
    header_lower = header_path.lower()
    content_lower = content.lower()
    
    # Trigger nodes
    if 'trigger' in header_lower or 'webhook' in header_lower:
        return 'trigger'
    # Action nodes (most common)
    elif any(keyword in header_lower for keyword in [' node', 'operations', 'credentials']):
        return 'action'
    # Core nodes
    elif any(keyword in header_lower for keyword in ['code', 'http request', 'set', 'if', 'switch', 'merge']):
        return 'core'
    # Sub-nodes
    elif any(keyword in header_lower for keyword in ['agent', 'tool', 'memory', 'retriever']):
        return 'ai_subnode'
    else:
        return 'unknown'

def extract_integration_names(header_path: str, content: str) -> List[str]:
    """Extract integration/service names mentioned in the chunk."""
    integrations = []
    
    # Common integrations from header
    integration_keywords = [
        'telegram', 'slack', 'discord', 'google', 'aws', 'azure', 
        'github', 'gitlab', 'jira', 'notion', 'airtable', 'mongodb',
        'mysql', 'postgres', 'redis', 'kafka', 'rabbitmq', 'twilio',
        'sendgrid', 'mailgun', 'stripe', 'shopify', 'woocommerce',
        'hubspot', 'salesforce', 'zendesk', 'intercom', 'mailchimp',
        'trello', 'asana', 'clickup', 'monday', 'linear'
    ]
    
    text_combined = (header_path + " " + content).lower()
    
    for integration in integration_keywords:
        if integration in text_combined:
            integrations.append(integration)
    
    return list(set(integrations))  # Remove duplicates

def detect_workflow_patterns(header_path: str, content: str, integrations: List[str]) -> List[str]:
    """Detect workflow patterns this chunk describes."""
    patterns = []
    header_lower = header_path.lower()
    content_lower = content.lower()
    
    # Trigger to storage pattern
    if any(trigger in integrations for trigger in ['telegram', 'slack', 'discord', 'webhook']):
        if any(storage in integrations for storage in ['database', 'mongodb', 'mysql', 'postgres', 'airtable']):
            patterns.append('message_to_storage')
    
    # API to notification pattern
    if 'http' in content_lower or 'api' in content_lower:
        if any(notify in integrations for notify in ['slack', 'telegram', 'email', 'sms']):
            patterns.append('api_to_notification')
    
    # Data sync pattern
    if len(integrations) >= 2:
        if 'sync' in content_lower or 'transfer' in content_lower:
            patterns.append('data_sync')
    
    # Template/Example pattern
    if 'template' in header_lower or 'example' in header_lower or 'workflow' in header_lower:
        patterns.append('workflow_template')
    
    # Authentication/Setup pattern
    if any(keyword in header_lower for keyword in ['credential', 'oauth', 'api key', 'authentication']):
        patterns.append('authentication_setup')
    
    # Automation pattern
    if any(keyword in content_lower for keyword in ['schedule', 'cron', 'interval', 'watch', 'monitor']):
        patterns.append('scheduled_automation')
    
    return patterns

def parse_markdown_with_headers(content: str) -> List[Dict[str, any]]:
    """Manually parse markdown content preserving header hierarchy."""
    lines = content.split('\n')
    sections = []
    current_headers = {'h1': None, 'h2': None, 'h3': None, 'h4': None, 'h5': None, 'h6': None}
    current_content = []
    
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
    
    def save_section():
        """Save accumulated content as a section."""
        if current_content:
            text = '\n'.join(current_content).strip()
            if text:  # Only save non-empty sections
                sections.append({
                    'content': text,
                    'headers': current_headers.copy()
                })
            current_content.clear()
    
    for line in lines:
        match = header_pattern.match(line)
        if match:
            # Save previous section before starting new one
            save_section()
            
            # Update header hierarchy
            hashes = match.group(1)
            header_text = match.group(2).strip()
            level = len(hashes)
            header_key = f'h{level}'
            
            # Update current level and clear lower levels
            current_headers[header_key] = header_text
            for i in range(level + 1, 7):
                current_headers[f'h{i}'] = None
            
            # Add header to content
            current_content.append(line)
        else:
            current_content.append(line)
    
    # Save final section
    save_section()
    
    return sections

def main():
    input_md = next((p for p in SOURCE_DOC_CANDIDATES if p.exists()), None)
    if input_md is None:
        searched = "\n".join(f"  - {p}" for p in SOURCE_DOC_CANDIDATES)
        raise FileNotFoundError(
            "Could not locate n8n_official_docs.md. Looked in:\n"
            f"{searched}\n\n"
            "Place the docs file in one of these locations and retry."
        )

    print(f"📘 Using source docs: {input_md}")
    content = input_md.read_text(encoding="utf-8")

    # Parse markdown with custom header-aware parser
    sections = parse_markdown_with_headers(content)
    
    print(f"📄 Parsed {len(sections)} sections from markdown")

    # Text splitter for large sections
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". "," ", ""]
    )

    final_chunks = []
    chunk_index = 0

    for section in sections:
        raw_metadata = section['headers']

        header_path = build_header_path(raw_metadata)
        last_header = raw_metadata.get('h6') or raw_metadata.get('h5') or \
                      raw_metadata.get('h4') or raw_metadata.get('h3') or \
                        raw_metadata.get('h2') or raw_metadata.get('h1') or "Unknown"

        # Split section content if too large
        splits = text_splitter.split_text(section['content'])

        for split_text in splits:
            # Skip empty chunks
            if not split_text.strip():
                continue
            
            # Extract workflow intelligence
            integrations = extract_integration_names(header_path, split_text)
            node_type = detect_node_type(header_path, split_text)
            workflow_patterns = detect_workflow_patterns(header_path, split_text, integrations)
                
            chunk_data = {
                "id": generate_chunk_id(split_text, {"header_path": header_path}),
                "text": split_text,
                "metadata": {
                    "source": "n8n_official_docs.md",
                    "header_path": header_path,
                    "last_header": last_header,
                    "chunk_index": chunk_index,
                    "contains_code": detect_code_blocks(split_text),
                    "token_count": count_tokens(split_text),
                    "section_type": detect_section_type(header_path, split_text),
                    "doc_category": detect_doc_category(header_path),
                    "char_count": len(split_text),
                    # New workflow-specific metadata
                    "node_type": node_type,
                    "integrations": integrations,
                    "workflow_patterns": workflow_patterns
                }
            }
            final_chunks.append(chunk_data)
            chunk_index += 1

    OUTPUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSONL.open("w", encoding="utf-8") as f:
        for chunk in final_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    
    # Calculate statistics
    total_tokens = sum(c['metadata']['token_count'] for c in final_chunks)
    avg_tokens = total_tokens / len(final_chunks) if final_chunks else 0
    chunks_with_code = sum(1 for c in final_chunks if c['metadata']['contains_code'])
    
    # Count by section type
    section_types = {}
    doc_categories = {}
    node_types = {}
    integration_counts = {}
    pattern_counts = {}
    
    for chunk in final_chunks:
        st = chunk['metadata']['section_type']
        dc = chunk['metadata']['doc_category']
        nt = chunk['metadata']['node_type']
        
        section_types[st] = section_types.get(st, 0) + 1
        doc_categories[dc] = doc_categories.get(dc, 0) + 1
        node_types[nt] = node_types.get(nt, 0) + 1
        
        # Count integrations
        for integration in chunk['metadata']['integrations']:
            integration_counts[integration] = integration_counts.get(integration, 0) + 1
        
        # Count workflow patterns
        for pattern in chunk['metadata']['workflow_patterns']:
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    
    print("=" * 70)
    print("📊 Extraction Statistics")
    print("=" * 70)
    print(f"✓ Total chunks extracted: {len(final_chunks)}")
    print(f"✓ Average tokens per chunk: {avg_tokens:.0f}")
    print(f"✓ Total tokens: {total_tokens:,}")
    print(f"✓ Chunks with code blocks: {chunks_with_code} ({chunks_with_code/len(final_chunks)*100:.1f}%)")
    print(f"\n📂 Section Types:")
    for st, count in sorted(section_types.items(), key=lambda x: x[1], reverse=True):
        print(f"   {st}: {count}")
    print(f"\n📁 Document Categories:")
    for dc, count in sorted(doc_categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   {dc}: {count}")
    print(f"\n🔧 Node Types:")
    for nt, count in sorted(node_types.items(), key=lambda x: x[1], reverse=True):
        print(f"   {nt}: {count}")
    print(f"\n🔗 Top Integrations:")
    for integration, count in sorted(integration_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"   {integration}: {count}")
    print(f"\n📋 Workflow Patterns:")
    for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {pattern}: {count}")
    print(f"\n💾 Output saved to: {OUTPUT_JSONL}")
    print("=" * 70)

if __name__ == "__main__":
    main()