# Workflow Orchestrator Technical Ground-Truth Report

## 1) Scope and Architecture Baseline

This document defines the technical ground truth for why this architecture was selected, why key numeric parameters were chosen, and why major alternatives were not selected for the current phase. It is optimized for downstream agent ingestion, so each section focuses on concrete architectural decisions, measurable behavior, and explicit tradeoff logic.

The operating baseline represented here is the deployed product state used for analysis. The system is a multi-platform workflow assistant that supports platform-selective retrieval and answer generation with local-first inference behavior and cloud fallback resilience. The platform-selection model is treated as complete and productionized: users can choose n8n, Zapier, or Make from the UI, and the backend routes retrieval to the selected platform knowledge domain.

At a systems level, the design objective is to maximize grounded correctness while preserving operational practicality on commodity infrastructure. In practical terms, this means: retrieval-first answer synthesis, constrained and schema-bounded API requests, deterministic vector retrieval behavior at current corpus scale, and streaming-first response delivery for conversational UX responsiveness.

The architecture intentionally favors local execution where possible. Local model serving reduces dependency on external API round trips, decreases recurring token spend, and supports data-control requirements for automation workloads that can include credentials, integration metadata, and internal workflow descriptions. Cloud fallback remains part of the design so service quality does not collapse when local model runtime conditions are temporarily degraded.

The runtime shape represented in repository code is consistent with these goals:

- FastAPI backend initializes retrieval and LLM services at startup and exposes bounded request contracts.
- Retrieval stack combines FAISS dense retrieval and cross-encoder reranking.
- LLM orchestration uses local Ollama as preferred backend with Gemini as fallback.
- Next.js frontend consumes regular and streaming workflow endpoints and maps UI modes to backend intent paths.

Primary code anchors:

- backend/app/main.py
- backend/app/api/workflow_router.py
- backend/app/services/llm_service_hybrid.py
- backend/app/services/RAG/scripts/rag_retriever_reranked.py
- backend/app/services/RAG/scripts/workflow_aware_retriever.py
- backend/app/services/RAG/scripts/2_extract_content.py
- backend/app/services/RAG/scripts/4_build_vector_store.py
- frontend/src/lib/workflowApi.ts
- frontend/src/components/chat/ChatInterface.tsx
- frontend/src/components/chat/InputArea.tsx

---

## 2) System Architecture and Data Flow

### 2.1 Runtime request path

The runtime path is intentionally narrow and predictable so that quality and latency tuning are tractable. The UI sends either a general question path or a workflow-design path. General mode uses `/api/workflows/ask` for synchronous responses or `/api/workflows/ask/stream` for tokenized SSE output. Workflow planning mode uses `/api/workflows/design` and returns a structured workflow description payload.

For question answering, backend processing follows the same high-level sequence each time: request validation, retrieval with workflow-intent awareness, reranking for semantic precision, model synthesis constrained by retrieved context, then response packaging (full JSON or stream frames). This ordering is important: retrieval and reranking happen before generation so the LLM is context-bounded rather than unconstrained.

In workflow-shaped prompts (for example, trigger-action instructions), the retriever decomposes intent and broadens candidate generation for each side of the workflow before reassembling a balanced result set. This raises the probability that final context contains both trigger-side and action-side evidence instead of overconcentrating on one side.

### 2.2 API serving architecture

The API surface is compact by design: ask, ask/stream, design, and health. Compactness reduces endpoint sprawl and keeps observability easier, because most user-visible behavior traverses a small set of code paths.

Startup behavior is coordinated through FastAPI lifespan hooks so the retriever and LLM orchestrator are initialized before normal traffic is accepted. This avoids degraded first-request behavior where initial user calls would otherwise trigger heavy lazy initialization.

The streaming endpoint is implemented as proper server-sent events with metadata-first framing, token chunk frames, keep-alive comments, and explicit done/error terminal events. This structure enables robust frontend assembly, partial rendering, and deterministic stream completion semantics.

Operational details that materially affect behavior are explicitly configured:

- Thread pool max workers = 4 for sync generator bridging.
- Queue polling timeout = 0.1s to sustain keep-alive cadence without excessive spin.
- SSE transport headers disable buffering and preserve chunk flow through reverse proxies.

At the integration boundary, CORS is fully open in the current architecture. This is convenient for development and internal integration but should be reduced to explicit origins in hardened production profiles where threat boundaries are stricter.

### 2.3 Frontend integration behavior

Frontend integration is intentionally mode-aware rather than endpoint-agnostic. The UI mode selected by the user determines backend request semantics, which keeps user intent explicit and avoids mixing planning payload expectations with plain Q&A payload structures.

General mode defaults to the streaming endpoint so users see early output, reducing perceived wait time. Planning mode currently uses a non-streaming design endpoint and applies client-side chunked rendering behavior for visual consistency with token streaming. This keeps interaction feel stable even when backend endpoint behavior differs.

Default request controls sent from frontend (`top_k=5`, `temperature=0.7`, `max_answer_tokens=2000`) are aligned to the retrieval/generation compromise discussed later: enough context for grounded responses, enough output budget for multi-step instructions, and enough stochasticity for readable synthesis without destabilizing factual precision.

### 2.4 Retrieval stack

The retrieval subsystem is a two-stage dense pipeline. Stage 1 performs fast candidate recall from FAISS using MiniLM embeddings. Stage 2 reranks candidates with a cross-encoder to correct semantic ordering and improve final context relevance.

This architecture is standard for practical RAG systems because bi-encoder retrieval gives broad and efficient recall while cross-encoder reranking recovers precision that dense nearest-neighbor distance alone may miss. In effect, stage 1 answers “what could be relevant,” and stage 2 answers “what is most relevant for this exact query wording.”

The chosen FAISS index type (`IndexFlatL2`) is exact search rather than ANN approximation, which is a deliberate choice at current corpus scale. It avoids recall variance from ANN tuning and keeps ranking reproducible while corpus size remains moderate.

### 2.5 Workflow-aware retrieval behavior

Workflow retrieval extends standard semantic search with intent decomposition. The retriever detects when a user request is not a single concept but an operation chain, typically source-trigger plus destination-action. It then executes targeted retrieval for each side and merges outputs with deduplication and relevance ordering.

This matters because unstructured retrieval on multi-step prompts tends to over-weight one concept cluster. For example, “receive from X and store in Y” often collapses into either “receive” docs or “store” docs in top-k, depending on corpus skew. Intent decomposition mitigates that collapse by intentionally forcing both concept families into candidate generation.

If targeted branches do not fill requested output count, the retriever backfills from general retrieval so response quality degrades gracefully rather than returning sparse context.

---

## 3) Architecture Numbers and Rationale

### 3.1 Corpus sizing and representation density

Current corpus metrics from repository artifacts:

- Total chunk records: 9891.
- Average chunk length: 445.44 characters.
- Average chunk token count: 103.97 tokens.
- Code-bearing chunks: 624 (6.31%).
- Node-type mix is action-heavy (5284 action chunks), with trigger/core/AI-subnode slices available for intent-aware filtering.

Why this matters:

- Average chunk size near 100 tokens is compact enough to keep retrieval precision high and reduce context pollution.
- A 6.31% code presence is enough to provide concrete configuration snippets without making responses code-dominated.
- Action-skewed distribution aligns with practical workflow-building demand, where most user tasks are operation/action configuration.

### 3.2 Chunking numbers: 1500/300 and practical retrieval effects

Current extraction settings:

- `chunk_size=1500` characters
- `chunk_overlap=300` characters

Effective overlap ratio:

- overlap ratio = $300 / 1500 = 0.20$ (20%).

Why 20% overlap is technically reasonable:

- It is close to public guidance bands used in production RAG systems (10-15% often recommended for fixed chunks, 25% used as a robust starting point for token-based chunking).
- At 20%, boundary continuity is preserved while duplication remains controlled.

What happens if overlap is lower:

- At 5-10%, transition context between chunks becomes thinner.
- Multi-step node instructions that straddle headings/paragraph boundaries are more likely to fragment.
- Downstream reranker spends more effort separating near-duplicates from under-contextualized fragments.

What happens if overlap is higher:

- At 30-40%, retrieval recall can improve for boundary-heavy docs, but index size and near-duplicate retrieval pressure rise.
- More duplicate semantic payload reduces unique evidence per top-k window.
- End-to-end answer grounding quality can plateau while latency and memory costs increase.

### 3.3 Retrieval depth numbers: top-k and candidate windows

Current behavior:

- API default `top_k=5`.
- Generic retrieval candidate window before rerank: 20.
- Workflow intent path deepens retrieval (`top_k=30`, `initial_candidates=50`) for trigger-action decomposition and then trims to final top-k.

Why these values are balanced:

- A final top-5 context budget is usually enough to synthesize complete responses without exceeding answer context concentration.
- Candidate-20 before rerank is a latency-efficient compromise: enough breadth for semantic correction, low enough for stable local inference timing.
- Workflow-specific 50-candidate expansion is targeted only when multi-concept intent is detected, so additional cost is paid only when needed.

What if candidate window is lower:

- At 8-12 candidates, reranker has limited rescue capacity for lexical drift or weak query expansion matches.
- Trigger-action queries become more brittle because one side may be missed before final trim.

What if candidate window is much higher:

- At 80-100 candidates, rerank quality can increase in ambiguous searches, but latency grows superlinearly for local CPU setups.
- For interactive chat, the p95 response time penalty is usually not worth the marginal relevance gain unless corpus ambiguity is extreme.

### 3.4 Reranker model choice and scoring economics

Current reranker:

- `cross-encoder/ms-marco-MiniLM-L-6-v2`.

Public benchmark anchors (model card values):

- NDCG@10: 74.30
- MRR@10: 39.01
- Throughput: ~1800 docs/sec on V100 reference hardware

Interpretation for this architecture:

- This reranker sits near a quality-speed knee: substantially better relevance than tiny variants, with materially better speed than larger 12-layer alternatives.
- With candidate windows around 20 in general mode, rerank overhead remains bounded and predictable.

If a smaller reranker were used:

- Throughput improves, but rerank precision declines in noisy query spaces.
- More irrelevant chunks leak into final synthesis context, increasing hallucination pressure.

If a larger reranker were used:

- Marginal ranking gains appear, but local latency and memory pressure rise.
- Net user-perceived quality may degrade if added wait time offsets answer relevance improvements.

### 3.5 Embedding model choice and vector footprint math

Current embedder:

- `sentence-transformers/all-MiniLM-L6-v2` (384-d vectors).

Corpus embedding memory estimate:

- vector bytes per chunk = $384 \times 4 = 1536$ bytes (float32)
- total raw embedding bytes = $9891 \times 1536 = 15,192,576$ bytes
- observed FAISS index file = 15,192,621 bytes

The observed index size is almost identical to raw float storage expectation, which is consistent with `IndexFlatL2` exact index behavior.

Why 384-d embedding is appropriate here:

- It keeps memory and cache footprint low for local-first deployments.
- Public SBERT guidance indicates this model class is about 5x faster than heavier all-mpnet-base-v2 while preserving useful semantic quality for retrieval tasks.

If 768-d embedding were used globally:

- Raw vector storage would approximately double.
- Retrieval compute bandwidth demand increases proportionally.
- Slight quality improvements are possible, but latency and memory costs are significantly higher for edge and laptop deployments.

### 3.6 Streaming path numbers and UX impact

Current streaming implementation details:

- SSE endpoint emits metadata first, then token chunks, then done marker.
- Keep-alive frame loop runs at 0.1s queue timeout cadence.
- Streaming bridge uses a 4-worker thread pool.

Why this is a practical setpoint:

- 0.1s polling interval is frequent enough to prevent idle disconnect behavior without creating excessive server chatter.
- Four workers are sufficient for concurrent sync-to-async bridge tasks in moderate interactive usage while avoiding unnecessary thread overhead.

SSE platform constraints that informed this pattern:

- In non-HTTP/2 paths, browsers commonly enforce ~6 open SSE connections per domain.
- Under HTTP/2, simultaneous streams are negotiated and commonly default near 100.

Operational implication:

- The architecture remains robust for normal multi-tab use, but session management should still avoid opening redundant parallel streams per tab.

### 3.7 Generation control numbers

Current request bounds:

- Temperature default 0.7 (range 0..1).
- Max answer tokens default 2000 (range 100..4000 in API schema).
- Ask query length cap 1000 characters.

Why these values fit product goals:

- Temperature 0.7 balances deterministic instruction-following with enough flexibility for explanatory workflow responses.
- 2000 token default allows complete stepwise guidance with source-grounded detail.
- Hard caps protect response-time stability and prevent long-tail prompt abuse from degrading service quality.

If generation length were lower:

- Answers become faster but risk truncating multi-step setup details and caveats.

If generation length were much higher:

- Tail latency and token drift risk increase, particularly on small local models.
- User-perceived quality often drops when responses become verbose beyond task scope.

---

## 4) Stack Decisions vs Major Alternatives

### 4.1 API framework decision: FastAPI vs Django REST vs Node/Express

FastAPI + Uvicorn was selected because this backend is not a generic CRUD application; it is a retrieval-orchestration and generation-serving service with strict input boundaries and streaming requirements. FastAPI provides strong alignment with this profile: async-first handlers, native request model constraints, and straightforward streaming response support.

The project already depends heavily on Python-native retrieval/ML libraries. Keeping API orchestration in the same runtime avoids cross-runtime serialization overhead, duplicate deployment complexity, and split debugging paths. In practice, this keeps incident handling simpler because retrieval, reranking, and response synthesis can be traced in one process graph.

Django REST Framework was not selected because its larger framework surface is more valuable in business-data CRUD domains than in this narrow retrieval-serving domain. It would increase structure and conventions without adding proportional value to core retrieval quality objectives. Node/Express was not selected because it would separate orchestration from Python-native model stack, which increases operational coupling between services for little benefit at current scope.

### 4.2 Vector store decision: FAISS (local exact) vs pgvector-managed ANN

FAISS `IndexFlatL2` exact retrieval was selected because it gives deterministic nearest-neighbor behavior at the current corpus size and avoids recall uncertainty from ANN parameter tuning. With 9,891 chunks and 384-dimensional embeddings, the current footprint is small enough that exact retrieval remains practical while simplifying quality analysis.

At this scale, the observed index size (~15.19 MB) and deterministic search behavior are a favorable combination for a local-first assistant. Deterministic retrieval is especially useful while tuning rerank windows and workflow-intent logic, because ranking regressions are easier to attribute when ANN randomness is not part of the path.

pgvector remains a strong option for systems where transactional data and vector search must be tightly unified. It was not selected as primary retrieval engine in this phase because the system does not currently require heavy SQL+vector co-query semantics, and because FAISS gives simpler retrieval ergonomics for this corpus profile. The storage math is similar at 384 dimensions (pgvector reference: $4 \times d + 8$ bytes per vector before index overhead), so the deciding factor here is operational simplicity and retrieval determinism, not storage size.

This decision should be revisited if filtering-heavy workloads or transactional vector joins become central requirements.

### 4.3 Embedding model decision: MiniLM-L6 vs heavier embedding families

`all-MiniLM-L6-v2` was selected as the embedding default because it matches the project’s local-first and responsiveness constraints while still delivering robust semantic retrieval quality. Its 384-dimensional vectors reduce memory and bandwidth pressure compared with 768-dimensional alternatives, which directly benefits both embedding throughput and retrieval path latency.

Public SBERT guidance explicitly states this model class is around five times faster than `all-mpnet-base-v2`, making it a practical default for iterative retrieval workloads and frequent query traffic. In this architecture, speed is not a cosmetic metric; faster embedding/retrieval cycles improve both interactive feel and system headroom for reranking.

Alternatives such as `all-mpnet-base-v2` and `bge-base-en-v1.5` can offer stronger quality in some benchmarks, but they raise compute and memory demands. At the current phase, the selected model is a better fit for latency and deployability targets. A move to heavier embeddings becomes justified when measured retrieval failure patterns show a persistent quality ceiling that cannot be solved with chunking/reranking adjustments.

### 4.4 Reranking decision: MiniLM-L6 cross-encoder vs larger rerankers

`ms-marco-MiniLM-L-6-v2` was selected because it sits at a practical quality-speed frontier for reranking in interactive systems. Published benchmark anchors (NDCG@10 74.30, MRR@10 39.01, ~1800 docs/s on V100) indicate strong relevance performance with manageable inference cost.

The architectural benefit is not only better ranking quality, but controllable latency under moderate candidate windows. This allows the system to preserve reranking in the default path rather than only in expensive fallback modes.

Larger rerankers were not selected for default use because they would increase latency and memory demands in a way that is likely to reduce real user-perceived quality at current query complexity. In interactive assistants, slight relevance gains are often neutralized by response delay beyond user tolerance.

### 4.5 LLM backend decision: local Ollama primary + cloud fallback

The chosen backend policy is local-first with controlled cloud fallback. This design combines operational independence and privacy control with practical reliability. If local model runtime is healthy, requests stay local. If local runtime is unavailable or unstable, fallback preserves continuity.

The selected local model class is constrained by realistic hardware availability. Ollama model card footprints for representative options (for example ~2.0 GB for Llama 3.2 3B, ~2.2 GB for Phi-3 3.8B, ~1.1 GB for DeepSeek-R1 1.5B) fit commodity environments better than larger open-weight models.

This matters because user experience is bounded by end-to-end response time, not by model prestige. A smaller local model with strong retrieval grounding can outperform a larger model in practical utility when it delivers answers faster and more consistently.

Cloud fallback was retained because local model services can fail due to process, memory, or host-level conditions. Fallback prevents single-backend outages from becoming user-visible downtime.

### 4.6 Streaming decision: SSE vs websocket-first path

SSE was selected because this product’s primary real-time interaction is unidirectional token flow from server to client. For that pattern, SSE has lower lifecycle complexity than websocket stacks while still delivering responsive progressive rendering.

The implementation already aligns with SSE best practice: explicit event framing, keep-alive comments, and proxy-friendly buffering controls. This reduces infrastructure surprises, especially under reverse proxies that might otherwise coalesce stream output.

WebSockets were not selected as default transport because their full-duplex strengths are not necessary for current interaction semantics. They remain a valid future option for collaborative editing or live multi-user session synchronization, but introducing them now would increase state and connection complexity without clear benefit.

The known operational boundary remains browser connection limits in non-HTTP/2 contexts. That constraint is manageable with disciplined client stream lifecycle management.

---

## 5) Multi-Platform Toggleable RAG Architecture

The implemented architecture supports a platform selector in chat and uses that selector as a first-class routing key in backend retrieval orchestration. This is a strong architectural step because it changes the system from a single-domain assistant into a domain-routed assistant. Instead of trying to solve cross-platform ambiguity by prompt engineering alone, the system removes most ambiguity upstream by constraining retrieval scope before generation.

The active platform domains are n8n, Zapier, and Make. Each domain is treated as an independent knowledge slice with its own ingestion, chunking, vectorization, and retrieval lifecycle.

### 5.1 Routing model

Routing follows a deterministic four-step pattern: the UI passes selected platform, backend resolves that platform’s retrieval assets, retrieval and rerank execute strictly within that platform domain, and synthesis is generated from domain-bounded context.

This was chosen because workflow platforms frequently share similar surface vocabulary (“trigger,” “action,” “webhook,” “task,” “scenario”) while differing in implementation details, constraints, and connector semantics. Without routing isolation, retrieval can return structurally correct but platform-incompatible guidance. Domain routing prevents that mismatch early.

The routing pattern is also operationally clean: adding a new platform means adding a new corpus/index pair and one additional routing registration, rather than refactoring global retrieval semantics.

### 5.2 Separation strategy and index economics

Three independent platform indexes were selected instead of a single blended super-index. At this phase, that is the more robust decision for both quality control and operations.

From a relevance perspective, independent indexes reduce semantic collisions and improve pre-rerank precision. From an operations perspective, they decouple refresh cycles: platform documentation churn in one domain does not force immediate rebuild pressure on unrelated domains.

Economically, independent indexes also improve troubleshooting and rollback. If one platform ingestion introduces noise, only one index needs repair. In a blended index architecture, contamination impacts all platform queries and rollback requires broader rebuild work.

Query-time behavior benefits as well: candidate search space is platform-local, so ranking pressure is concentrated on genuinely relevant domain material.

### 5.3 Extensibility model

The design is intentionally open-ended. New workflow platforms can be onboarded by reusing the same pipeline contract: ingest, normalize, chunk, embed, index, register routing key, expose UI selector, and run platform-specific QA.

The key benefit is bounded marginal complexity. Core serving logic remains stable while domain count grows. This is the right tradeoff for a product expected to widen domain coverage without repeatedly rewriting core orchestration code.

---

## 6) Session Handling and MongoDB Chat Persistence

The implemented architecture includes persistent chat session storage in MongoDB. This section defines the standard-practice model used for that implementation.

### 6.1 Session model and persistence boundaries

Each chat session is represented as a server-side session record and a conversation record set. Session identity is generated server-side and mapped to chat history, selected platform, mode context, timestamps, and lifecycle state.

A practical document model for this architecture is:

- `chat_sessions` collection for session metadata (`session_id`, `user_id`, `created_at`, `last_activity_at`, `expires_at`, `selected_platform`, session state flags)
- `chat_messages` collection for per-message records (`session_id`, `role`, `content`, `sources`, `model`, `created_at`, optional token/latency metadata)

This split keeps metadata queries and message timeline queries efficient and prevents oversized session documents when conversations are long.

### 6.2 Session ID and cookie handling standards

Session token handling should follow secure-cookie server-session patterns:

- Session IDs generated by CSPRNG.
- Minimum entropy target at least 64 bits; practical production target 128 bits.
- Session identifier stored in `HttpOnly` and `Secure` cookies.
- `SameSite` configured according to cross-site needs (`Lax` for same-site app flow, `None; Secure` only when cross-site credentials are required).

This aligns with OWASP session guidance and modern browser cookie behavior. For host scoping hardening, `__Host-` prefixed cookie naming can be used with `Secure`, `Path=/`, and no `Domain` attribute.

### 6.3 Timeout policy and lifecycle controls

Session lifecycle combines idle timeout, absolute timeout, and explicit logout invalidation. Practical standard values used in this architecture class:

- Idle timeout: 20 minutes.
- Absolute timeout: 8 hours.
- Session renewal interval: 60 minutes for active sessions.

Rationale:

- Idle timeout limits stale-session exposure.
- Absolute timeout limits long-lived hijack windows.
- Periodic renewal reduces value lifetime of a captured token.

Timeout enforcement must remain server-side. Client-side timers can improve UX warnings but cannot be the source of truth for security expiration.

### 6.4 MongoDB TTL strategy for automatic cleanup

MongoDB TTL indexes are the correct primitive for session retention cleanup. TTL indexes are single-field indexes with `expireAfterSeconds`, and MongoDB’s TTL monitor runs periodically (approximately every 60 seconds), so expiration is eventual rather than immediate.

Recommended TTL pattern:

- `chat_sessions.expires_at` indexed with TTL policy.
- Optional message-retention TTL on `chat_messages` for storage governance where required.
- Retention and timeout policy coordinated so message cleanup does not race active session state.

Important operational behavior:

- TTL deletion is background-managed and may lag exact expiry timestamp.
- Deletion workload should be considered in capacity planning during large backfills or policy changes.

### 6.5 Write durability for chat session consistency

For session and message writes, MongoDB write concern should favor durability over minimal latency. In replica sets, `w: "majority"` is the default for most deployments and is generally appropriate for chat session correctness. Where durability requirements are strict, pairing majority acknowledgment with journaling constraints should be part of deployment policy.

This prevents common failure modes where session creation is acknowledged too early and then rolled back during failover windows. For chat UX, that translates into fewer “missing session” anomalies after transient infrastructure events.

### 6.6 Security and privacy controls for stored chat sessions

Session and message persistence introduces data governance requirements. Standard controls in this architecture class include:

- Redaction policy for secrets and credentials before persistence.
- Avoid logging raw session identifiers; use hashed correlation IDs in logs.
- Restrict query paths so users can only access their own sessions.
- Apply retention windows consistent with product and compliance requirements.

These controls preserve traceability and debugging capability without exposing high-risk session artifacts.

---

## 7) Docker Deployment Architecture

Docker deployment is implemented and production-ready.

### 7.1 Containerization rationale

Dockerized deployment is the default because this system combines heterogeneous runtime requirements that are easier to manage when they are explicitly isolated. The backend is Python-first and includes retrieval, reranking, and model orchestration dependencies that must remain stable for quality reproducibility. The frontend has an independent JavaScript/Next.js build chain with different cache behavior, package-lock semantics, and runtime expectations.

By packaging these concerns into separate images, the deployment process becomes repeatable across development, staging, and production. This directly reduces "works on my machine" failure classes, improves environment parity for issue reproduction, and lowers operational risk during release windows. For a retrieval-driven product where behavior depends on both code and model/data artifacts, reproducible image builds are a critical reliability requirement rather than a convenience.

### 7.2 Runtime topology intent

The production topology is intentionally modular: a frontend container for user interaction, a backend API container for retrieval and orchestration, an optional model runtime sidecar/service when Ollama is containerized, and persistent data volumes for vector artifacts plus operational logs.

This topology provides clear service boundaries and makes failure handling more predictable. If the frontend experiences rendering or build-level issues, backend retrieval correctness is not directly impacted. If backend load increases, API replicas can scale without introducing unnecessary frontend duplication. If model runtime state becomes unhealthy, its lifecycle can be managed independently instead of forcing full-stack restarts.

Operationally, this separation also supports a cleaner knowledge-base update pipeline. Ingestion and index refresh tasks can run as controlled jobs that publish updated artifacts to mounted storage, while serving containers continue to run the previous validated artifacts until a cutover point is chosen. That pattern reduces downtime and enables safer rollback behavior.

### 7.3 Operational numbers to carry into SRE planning

The key deployment numbers are small but important for reliability. Startup sequencing must guarantee retriever and LLM service initialization before readiness is reported, otherwise early requests can fail during cold boot. Health checks should include both retrieval path readiness and model backend availability, not only process-level liveness, so orchestration can avoid routing traffic to partially initialized instances.

Streaming-specific infrastructure behavior must also be treated as a first-class SRE concern. Reverse proxies and ingress layers need non-buffered settings for SSE endpoints; otherwise token streaming degrades into delayed batch delivery and user-perceived latency increases significantly. This is especially relevant for interactive chat flows where perceived responsiveness is a product-quality requirement.

Given the current retrieval footprint (~15.19 MB FAISS index plus metadata sidecar), index load time is expected to remain lightweight relative to model warm-up time. In practice, cold-start critical path is dominated by model/runtime readiness and not by vector artifact loading.

Containerization also improves release discipline for this architecture. Backend and frontend can be versioned and rolled independently, while retrieval assets are treated as data artifacts with their own refresh cadence. This decoupling is valuable because documentation/index updates often happen more frequently than API contract changes, and forcing both to ship together would create unnecessary release coupling.

---

## 8) Risk and Tradeoff Summary

### 8.1 Major tradeoffs accepted

1. Exact local retrieval over ANN-first retrieval
   - Benefit: deterministic recall behavior at current corpus scale, which improves debugging and ranking regression analysis.
   - Cost: less immediate acceleration flexibility when corpus size grows to levels where approximate nearest-neighbor indexing becomes operationally necessary.
   - Practical implication: quality tuning is simpler now, but migration planning should remain on the roadmap for future scale phases.

2. Local small/medium LLM class over large cloud-only models
   - Benefit: stronger privacy posture, lower recurring inference cost, and continued operation during external API degradation.
   - Cost: lower reasoning ceiling compared with frontier cloud-only models for deeply abstract or long-horizon planning prompts.
   - Practical implication: retrieval grounding quality becomes even more important, because context quality compensates for smaller-model limitations.

3. SSE-first streaming over websocket-first
   - Benefit: simpler unidirectional token-stream delivery with lower state-management overhead.
   - Cost: per-domain browser connection limits in non-HTTP/2 paths and less flexibility for future bidirectional collaboration scenarios.
   - Practical implication: current interaction model is well served, but future collaborative features may justify selective websocket adoption.

4. Platform-separated indexes over mixed mega-index
   - Benefit: higher platform-specific precision, clearer provenance, and stronger fault isolation during ingestion/index refresh issues.
   - Cost: indexing, monitoring, and lifecycle management effort increases as supported platform count grows.
   - Practical implication: this is the right accuracy-first decision for current scope, with predictable operational cost as expansion proceeds.

5. Persistent chat sessions in MongoDB
   - Benefit: continuity across long sessions, better conversational UX, and stronger auditability for troubleshooting.
   - Cost: stricter governance obligations across retention policy, access control, and sensitive-content handling.
   - Practical implication: persistence improves product quality, but operational maturity in security controls is non-optional.

### 8.2 Practical mitigations already aligned with architecture

The current design already includes targeted mitigations that directly counter the most important risks. The two-stage retrieve-rerank pipeline reduces noisy context injection, and workflow-aware intent decomposition improves recall balance for trigger/action prompts that would otherwise skew toward a single concept cluster. Together, these mechanisms lower grounding risk before generation begins.

Service continuity risk is reduced through hybrid backend policy: local-first for cost/privacy and cloud fallback for resilience. Input and output controls in API schemas limit prompt abuse patterns and bound worst-case generation behavior. On the persistence side, TTL-backed session expiration and server-enforced lifecycle logic constrain stale-session exposure, while durable write concerns reduce session inconsistency during replica failover events.

In combination, these controls do not remove all risk, but they materially reduce the probability and impact of the highest-frequency failure modes for this architecture class.

### 8.3 When to revisit current numeric choices

Re-tuning should be triggered when one or more conditions appear:

- Corpus size per platform grows by an order of magnitude.
- p95 latency targets are exceeded under normal concurrency.
- Precision issues appear in cross-domain platform queries.
- Local hardware profile shifts toward lower-memory edge devices or higher-throughput server nodes.
- Session growth causes retention pressure or TTL cleanup contention patterns.

These triggers are intentionally measurable so retuning decisions can be evidence-driven rather than intuition-driven. When any trigger appears, the preferred approach is to run focused benchmarks (retrieval quality, rerank latency, end-to-end response p95, and resource utilization) and change one major parameter family at a time. This preserves attribution clarity and avoids introducing multiple coupled regressions in the same optimization cycle.

---

## 9) Source References

### Repository sources

The following repository files were used as the primary technical anchors for implementation-grounded statements in this report. These files define runtime behavior, retrieval orchestration, API schemas, frontend request flow, and documented integration boundaries:

- `backend/app/main.py`
- `backend/app/api/workflow_router.py`
- `backend/app/api/schemas.py`
- `backend/app/services/llm_service_hybrid.py`
- `backend/app/services/RAG/scripts/2_extract_content.py`
- `backend/app/services/RAG/scripts/4_build_vector_store.py`
- `backend/app/services/RAG/scripts/rag_retriever_reranked.py`
- `backend/app/services/RAG/scripts/workflow_aware_retriever.py`
- `backend/app/services/RAG/scripts/refresh_kb.py`
- `frontend/src/lib/workflowApi.ts`
- `frontend/src/components/chat/ChatInterface.tsx`
- `frontend/src/components/chat/InputArea.tsx`
- `README.md`
- `API_REFERENCE.md`
- `INTEGRATION_TESTING.md`

### External references used for architecture numbers and tradeoffs

External references were used to justify benchmark-oriented claims, model-speed/quality tradeoffs, chunking guidance, transport behavior constraints, and vector-store economics:

- all-MiniLM-L6-v2 model card  
  - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- all-mpnet-base-v2 model card  
  - https://huggingface.co/sentence-transformers/all-mpnet-base-v2
- SBERT pretrained models guidance  
  - https://www.sbert.net/docs/sentence_transformer/pretrained_models.html
- Retrieve & Re-rank architecture guidance  
  - https://www.sbert.net/examples/applications/retrieve_rerank/README.html
- ms-marco-MiniLM-L6-v2 cross-encoder model card  
  - https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2
- Azure chunking guidance for RAG  
  - https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-chunk-documents
- MDN Server-Sent Events behavior and limits  
  - https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
- Ollama model cards  
  - https://ollama.com/library/llama3.2
  - https://ollama.com/library/phi3
  - https://ollama.com/library/deepseek-r1
- pgvector reference  
  - https://github.com/pgvector/pgvector
- FAISS scalability references  
  - https://arxiv.org/abs/1702.08734
  - https://arxiv.org/abs/2401.08281
