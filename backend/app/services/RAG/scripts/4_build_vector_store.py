# ==============================================================================
# Step 4: Build the Vector Store
# ==============================================================================
#
#
# Description:
# This script reads the final, enriched corpus from `rag_corpus.jsonl`.
# It generates vector embeddings for each chunk and stores them along with
# their metadata in a persistent ChromaDB vector store. This is the final step
# in preparing the knowledge base.
#
# Output:
# A local ChromaDB database directory containing the indexed knowledge base,
# ready to be queried by the RAG system's AI service.
# ==============================================================================

import os
import json
import chromadb
from sentence_transformers import SentenceTransformer

# --- CONFIGURATION ---
CORPUS_FILE = './backend/app/services/RAG/docs/rag_corpus.jsonl'
CHROMA_DB_PATH = './backend/app/services/chroma_db'
COLLECTION_NAME = 'n8n_universal_knowledge'
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    if not os.path.exists(CORPUS_FILE):
        print(f"FATAL: Corpus file '{CORPUS_FILE}' not found. Please run the full pipeline (1-3) first.")
    else:
        print("=============================================")
        print("        n8n Universal Vector Store Build       ")
        print("=============================================")

        # 1. Load the processed corpus
        print(f"Loading corpus from '{CORPUS_FILE}'...")
        chunks = []
        with open(CORPUS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                chunks.append(json.loads(line))
        
        if not chunks:
            print("Corpus is empty. Aborting.")
        else:
            print(f"Loaded {len(chunks)} chunks to be indexed.")
            
            # 2. Initialize the embedding model
            print(f"Loading embedding model: '{EMBEDDING_MODEL}'...")
            model = SentenceTransformer(EMBEDDING_MODEL)

            # 3. Initialize ChromaDB client and create/get collection
            client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
            # Use get_or_create_collection to avoid errors on subsequent runs
            collection = client.get_or_create_collection(name=COLLECTION_NAME)
            print(f"ChromaDB collection '{COLLECTION_NAME}' is ready.")

            # 4. Prepare data for ChromaDB
            ids = [chunk['metadata']['chunk_id'] for chunk in chunks]
            documents = [chunk['chunk_text'] for chunk in chunks]
            metadatas = [chunk['metadata'] for chunk in chunks]

            # 5. Generate embeddings
            print("Generating embeddings (this may take a while for the full corpus)...")
            embeddings = model.encode(documents, show_progress_bar=True)

            # 6. Add to ChromaDB collection in batches for efficiency
            batch_size = 500
            print(f"Adding {len(ids)} documents to ChromaDB in batches of {batch_size}...")
            for i in range(0, len(ids), batch_size):
                end_index = i + batch_size
                print(f"  -> Adding batch {i//batch_size + 1} ({i+1}-{min(end_index, len(ids))}/{len(ids)})")
                collection.add(
                    ids=ids[i:end_index],
                    embeddings=embeddings[i:end_index].tolist(),
                    documents=documents[i:end_index],
                    metadatas=metadatas[i:end_index]
                )
            
            print("\n=============================================")
            print(" Vector Store build complete!")
            print(f" Database is stored at: '{CHROMA_DB_PATH}'")
            print("=============================================")

