# Metrics Ledger

## Repository-derived metrics

- chunks.jsonl records: 9891
- average chunk characters: 445.44
- average chunk tokens: 103.97
- chunks containing code blocks: 624 (6.31%)
- node_type distribution:
  - action: 5284
  - unknown: 3422
  - trigger: 559
  - core: 429
  - ai_subnode: 197
- FAISS index size: 15,192,621 bytes
- metadata.pkl size: 7,738,382 bytes

## Runtime numeric defaults in code

- API request limits:
  - ask query max length: 1000
  - ask top_k range: 1..10 (default 5)
  - ask temperature range: 0..1 (default 0.7)
  - ask max_answer_tokens range: 100..4000 (default 2000)
  - design description max length: 500
- extraction:
  - chunk_size: 1500 chars
  - chunk_overlap: 300 chars
- retriever:
  - initial_candidates default: 20
  - workflow targeted retrieval candidate depth: top_k=30, initial_candidates=50
- streaming:
  - thread pool workers: 4
  - token queue timeout: 0.1 seconds

## External benchmark numbers to use in report

- all-MiniLM-L6-v2:
  - embedding dimension: 384
  - truncation behavior: >256 word pieces truncated
- all-mpnet-base-v2:
  - embedding dimension: 768
  - truncation behavior: >384 word pieces truncated
- SBERT guidance:
  - all-MiniLM-L6-v2 is around 5x faster than all-mpnet-base-v2
- ms-marco-MiniLM-L6-v2 cross-encoder benchmark (V100):
  - NDCG@10: 74.30
  - MRR@10: 39.01
  - docs/sec: 1800
- Retrieve-rerank guidance:
  - retrieve around top 100 candidates, rerank to smaller top set
- Azure chunking guidance:
  - suggested start point: 512 tokens with 25% overlap (128 tokens)
  - practical fixed-size guidance: 10-15% overlap often works
- SSE browser behavior:
  - non-HTTP/2 browser/domain cap commonly 6 open connections
  - HTTP/2 negotiated stream default often around 100
- pgvector reference:
  - vector storage: 4 * dimensions + 8 bytes
  - HNSW ef_search default: 40
  - IVFFlat probes default: 1
  - indexed vector dimension support up to 2000 for vector type
- FAISS (GPU paper):
  - reported 8.5x speedup over prior GPU state of the art in tested setup
  - 95M graph build in 35 minutes
  - 1B vector graph build in <12 hours on 4 Titan X GPUs
