# OpsKit for n8n

## Nodes
- **RateLimit Gate**: token-bucket limiter per policy key.
- **Semaphore**: named lock / bounded concurrency.
- **Circuit Breaker**: open/half/closed based on failure rate.
- **Idempotency**: drop duplicates using a TTL key.
- **Backoff Retry**: exponential backoff & jitter for retry loops.
- **Dead Letter**: push failed items to a DLQ.
- **DLQ Replayer**: pop items back for reprocessing.

## Install
1) Build: `pnpm i && pnpm build`
2) Copy `packages/n8n-nodes-opskit` into n8n’s custom nodes dir or publish as a package and add to n8n.
3) Configure **OpsKit Redis** credentials per environment. Use `ns=prod|stg|tenantA`.

## Patterns
### 1) Tame an external API
Webhook → **RateLimitGate**(policy: `openai:{{$json.orgId}}`, 60rpm) → Call API  
On error: **CircuitBreaker**(record failure) → **DeadLetter**  
On success: **CircuitBreaker**(record success)

### 2) Serialize chat updates
**Semaphore**(lock: `chat:{{$json.chat_id}}`) → Update → **Semaphore**(release)

### 3) Idempotent webhooks
Webhook → **Idempotency**(key: `{{$json.message_id}}`) → process…

### 4) Retry loop
**BackoffRetry** → HTTP (continue on fail) → IF failed → back to **BackoffRetry**

### 5) DLQ replay
Cron → **DLQReplayer**(topic: `waba-fails`, batch: 100) → process…
