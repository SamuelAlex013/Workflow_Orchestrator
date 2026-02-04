import json
from pathlib import Path
from typing import List, Dict
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Paths
CHUNKS_FILE = Path(__file__).parent.parent / "data" / "chunks.jsonl"
VECTOR_DB_PATH = Path(__file__).parent.parent / "data" / "vector_store"
INDEX_FILE = VECTOR_DB_PATH / "faiss.index"
METADATA_FILE = VECTOR_DB_PATH / "metadata.pkl"

# Embedding model configuration
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Batch size for embedding generation
BATCH_SIZE = 100


def load_chunks() -> List[Dict]:
    """Load chunks from JSONL file."""
    chunks = []
    with CHUNKS_FILE.open('r', encoding='utf-8') as f:
        for line in f:
            chunks.append(json.loads(line))
    return chunks


def build_vector_store(reset: bool = False):
    """Build FAISS vector store from chunks using local embeddings."""
    
    print("=" * 70)
    print("🏗️  Building Vector Store (FAISS)")
    print("=" * 70)
    
    # Load chunks
    print(f"\n📂 Loading chunks from {CHUNKS_FILE}...")
    chunks = load_chunks()
    print(f"✓ Loaded {len(chunks)} chunks")
    
    # Initialize embedding model
    print(f"\n🤖 Loading embedding model: {EMBEDDING_MODEL}...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    embedding_dim = model.get_sentence_embedding_dimension()
    print(f"✓ Model loaded (embedding dimension: {embedding_dim})")
    
    # Create FAISS index
    print(f"\n💾 Creating FAISS index...")
    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)
    
    # Use IndexFlatL2 for exact search (can upgrade to IndexIVFFlat for large datasets)
    index = faiss.IndexFlatL2(embedding_dim)
    
    # Store metadata separately
    metadata_list = []
    text_list = []
    
    # Process chunks in batches
    print(f"\n🔄 Generating embeddings and building index (batch size: {BATCH_SIZE})...")
    
    all_embeddings = []
    for i in tqdm(range(0, len(chunks), BATCH_SIZE), desc="Processing batches"):
        batch = chunks[i:i + BATCH_SIZE]
        
        # Extract data for batch
        texts = [chunk['text'] for chunk in batch]
        metadatas = [chunk['metadata'] for chunk in batch]
        
        # Generate embeddings
        embeddings = model.encode(texts, show_progress_bar=False)
        all_embeddings.append(embeddings)
        
        # Store metadata and texts
        metadata_list.extend(metadatas)
        text_list.extend(texts)
    
    # Combine all embeddings and add to index
    all_embeddings_array = np.vstack(all_embeddings).astype('float32')
    index.add(all_embeddings_array)
    
    # Save index and metadata
    print(f"\n💾 Saving index to {INDEX_FILE}...")
    faiss.write_index(index, str(INDEX_FILE))
    
    print(f"💾 Saving metadata to {METADATA_FILE}...")
    with METADATA_FILE.open('wb') as f:
        pickle.dump({'metadata': metadata_list, 'texts': text_list}, f)
    
    # Verify
    count = index.ntotal
    
    print("\n" + "=" * 70)
    print("✅ Vector Store Build Complete!")
    print("=" * 70)
    print(f"📊 Statistics:")
    print(f"   Total chunks: {len(chunks)}")
    print(f"   Vectors in index: {count}")
    print(f"   Embedding dimension: {embedding_dim}")
    print(f"   Index file: {INDEX_FILE}")
    print(f"   Metadata file: {METADATA_FILE}")
    print(f"   Model: {EMBEDDING_MODEL}")
    print("=" * 70)
    
    return index, metadata_list, text_list, model


def test_retrieval(index, metadata_list, text_list, model, query: str = "How do I send an SMS in n8n?", top_k: int = 3):
    """Test retrieval with a sample query."""
    print(f"\n🔍 Testing retrieval with query: '{query}'")
    print("-" * 70)
    
    # Generate query embedding
    query_embedding = model.encode([query])[0].astype('float32').reshape(1, -1)
    
    # Search in FAISS index
    distances, indices = index.search(query_embedding, top_k)
    
    # Display results
    for i, (idx, distance) in enumerate(zip(indices[0], distances[0])):
        if idx < len(text_list):
            metadata = metadata_list[idx]
            text = text_list[idx]
            
            print(f"\nResult #{i+1} (distance: {distance:.4f}):")
            print(f"  Header: {metadata['header_path']}")
            print(f"  Section: {metadata['section_type']}")
            print(f"  Category: {metadata['doc_category']}")
            print(f"  Preview: {text[:150]}...")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Build FAISS vector store from n8n documentation chunks")
    parser.add_argument("--reset", action="store_true", help="Reset existing index before building")
    parser.add_argument("--test", action="store_true", help="Run test query after building")
    parser.add_argument("--query", type=str, default="How do I send an SMS in n8n?", help="Test query string")
    
    args = parser.parse_args()
    
    # Build vector store
    index, metadata_list, text_list, model = build_vector_store(reset=args.reset)
    
    # Run test if requested
    if args.test:
        test_retrieval(index, metadata_list, text_list, model, query=args.query)
