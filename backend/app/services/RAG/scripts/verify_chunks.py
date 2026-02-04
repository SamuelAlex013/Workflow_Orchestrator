import json
from pathlib import Path

CHUNKS_FILE = Path(__file__).parent.parent / "data" / "chunks.jsonl"

# Read first 10 chunks
chunks = []
with CHUNKS_FILE.open('r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i >= 10:
            break
        chunks.append(json.loads(line))

# Display sample chunks
print("\n" + "="*70)
print("📝 Sample Chunks Analysis")
print("="*70 + "\n")

for i, chunk in enumerate(chunks):
    meta = chunk['metadata']
    print(f"Chunk #{i+1}:")
    print(f"  Header Path: {meta['header_path']}")
    print(f"  Last Header: {meta['last_header']}")
    print(f"  Tokens: {meta['token_count']} | Chars: {meta['char_count']}")
    print(f"  Section Type: {meta['section_type']}")
    print(f"  Category: {meta['doc_category']}")
    print(f"  Contains Code: {meta['contains_code']}")
    print(f"  Text Preview: {chunk['text'][:120]}...")
    print()

# Check header path diversity
unique_paths = set(c['metadata']['header_path'] for c in chunks)
print(f"Unique header paths in sample: {len(unique_paths)}")
print("Header paths:")
for path in sorted(unique_paths):
    print(f"  - {path}")
