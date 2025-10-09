# ==============================================================================
# Step 3: Process and Chunk Data 
# ==============================================================================
#
#
# Description:
# This enhanced script processes raw data, applying a much richer metadata
# schema. It now parses YAML frontmatter, detects language, classifies content
# into semantic sections (e.g., configuration, examples), and identifies code
# snippets, creating a highly context-aware corpus for the RAG system.
#
# Output:
# A final `rag_corpus.jsonl` file with enriched, production-ready chunks.
# ==============================================================================

import os
import json
import re
import yaml
from langdetect import detect, lang_detect_exception

# --- CONFIGURATION ---
RAW_DATA_DIR = './raw_data/'
MANIFEST_FILE = './backend/app/services/RAG/docs/nodes_manifest.json'
OUTPUT_FILE = './backend/app/services/RAG/docs/rag_corpus.jsonl'
CHUNK_SIZE = 512 # Target character size, not token size

# --- ENHANCED PROCESSING LOGIC (from Analysis Report) ---

SECTION_KEYWORDS = {
    'installation': ['install', 'npm', 'package', 'prerequisite', 'setup'],
    'credentials': ['credential', 'authentication', 'oauth', 'api key', 'authenticate'],
    'configuration': ['configure', 'parameter', 'options', 'setting'],
    'examples': ['example', 'template', 'workflow', 'use case', 'how to'],
    'troubleshooting': ['issue', 'error', 'troubleshoot', 'problem', 'common issues'],
}

def extract_yaml_frontmatter(content):
    """Extracts metadata from YAML frontmatter in official docs."""
    try:
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            frontmatter = yaml.safe_load(match.group(1))
            # Remove the frontmatter from the main content
            content = content[match.end():]
            return frontmatter or {}, content
    except yaml.YAMLError:
        pass
    return {}, content

def detect_language(text):
    """Safely detects the language of a text chunk."""
    try:
        # Avoid errors on very short or non-alphabetic strings
        if len(re.findall(r'\w+', text)) < 5:
            return 'unknown'
        return detect(text)
    except lang_detect_exception.LangDetectException:
        return 'unknown'

def classify_section(text):
    """Classifies a chunk's content based on keywords."""
    text_lower = text.lower()
    scores = {section: sum(1 for kw in keywords if kw in text_lower) for section, keywords in SECTION_KEYWORDS.items()}
    if max(scores.values()) > 0:
        return max(scores, key=scores.get)
    return 'general'

def tag_code_examples(text):
    """Checks for code blocks and adds relevant metadata."""
    metadata = {'has_code_examples': False, 'code_languages': []}
    code_blocks = re.findall(r'```(\w+)?\n', text, re.DOTALL)
    if code_blocks:
        metadata['has_code_examples'] = True
        metadata['code_languages'] = list(set(lang for lang in code_blocks if lang))
    return metadata

def chunk_markdown(content, chunk_size):
    """Chunks Markdown content along semantic boundaries (headings)."""
    chunks = []
    current_chunk = ""
    # Split by headings (e.g., #, ##, ###) to keep sections together
    sections = re.split(r'(^#+\s.*)', content, flags=re.MULTILINE)
    
    # Handle the case where the first part of the content has no heading
    if sections[0]:
        current_chunk = sections[0]
    
    # Process pairs of (heading, content)
    for i in range(1, len(sections), 2):
        heading = sections[i]
        section_content = sections[i+1] if (i+1) < len(sections) else ""
        
        if len(current_chunk) + len(heading) + len(section_content) > chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = heading + section_content
        else:
            current_chunk += heading + section_content
            
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def process_files(directory, doc_type, manifest_map):
    """Processes all files, chunks them, and adds enriched metadata."""
    corpus = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        key = filename.replace('.md', '')
        base_metadata = manifest_map.get(key, {})
        base_metadata['doc_type'] = doc_type
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, content = extract_yaml_frontmatter(content)
        
        chunks = chunk_markdown(content, CHUNK_SIZE)
        
        for i, chunk_text in enumerate(chunks):
            if not chunk_text: continue

            chunk_metadata = base_metadata.copy()
            # Add metadata from analysis recommendations
            if doc_type == 'official_node':
                chunk_metadata['node_name'] = key.split('.')[0] # e.g., 'scheduletrigger' from 'n8n-nodes-base.scheduletrigger.md'
                chunk_metadata.update(frontmatter)

            chunk_metadata['chunk_id'] = f"{key}_{i}"
            chunk_metadata['language'] = detect_language(chunk_text)
            chunk_metadata['section'] = classify_section(chunk_text)
            chunk_metadata.update(tag_code_examples(chunk_text))
            
            corpus.append({
                'chunk_text': chunk_text,
                'metadata': chunk_metadata
            })
            
    return corpus

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    if not os.path.exists(RAW_DATA_DIR):
        print(f"FATAL: Raw data directory '{RAW_DATA_DIR}' not found. Please run 2_extract_content.py first.")
    elif not os.path.exists(MANIFEST_FILE):
        print(f"FATAL: Manifest file '{MANIFEST_FILE}' not found. Please run 1_discover_nodes.py first.")
    else:
        with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        official_map = {os.path.basename(node['markdownPath']): node for node in manifest['official_nodes']}
        community_map = {node['packageName']: node for node in manifest['community_nodes']}
        
        print("=============================================")
        print("  n8n Universal Data Processing & Chunking (v2)")
        print("=============================================")
        
        full_corpus = []
        
        official_dir = os.path.join(RAW_DATA_DIR, 'official')
        if os.path.exists(official_dir):
            print("\nProcessing official node documentation...")
            full_corpus.extend(process_files(official_dir, 'official_node', official_map))
            
        community_dir = os.path.join(RAW_DATA_DIR, 'community')
        if os.path.exists(community_dir):
            print("Processing community node documentation...")
            full_corpus.extend(process_files(community_dir, 'community_node', community_map))
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            for entry in full_corpus:
                f.write(json.dumps(entry) + '\n')
                
        print(f"\nProcessing complete. Enriched RAG corpus saved to '{OUTPUT_FILE}'.")
        print(f"Total chunks created: {len(full_corpus)}")

