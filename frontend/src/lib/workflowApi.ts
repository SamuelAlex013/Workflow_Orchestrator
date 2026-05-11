/**
 * Workflow Orchestrator API Service
 * 
 * Centralized API layer for communicating with the FastAPI backend.
 * Handles all HTTP requests, error handling, and response typing.
 */

// ============================================
// Configuration
// ============================================

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

// ============================================
// Type Definitions (matching backend schemas)
// ============================================

// Document Search Types
export interface ChunkMetadata {
    source: string;
    header_path: string;
    last_header: string;
    chunk_index: number;
    contains_code: boolean;
    token_count: number;
    section_type: string;
    doc_category: string;
    char_count: number;
    node_type?: string;
    integrations?: string[];
    workflow_patterns?: string[];
}

export interface DocumentChunk {
    text: string;
    metadata: ChunkMetadata;
    distance: number;
    relevance_score: number;
}

// Workflow Assistant Types
export interface WorkflowAskRequest {
    query: string;
    top_k?: number;
    temperature?: number;
    max_answer_tokens?: number;
    include_sources?: boolean;
    platform?: "n8n" | "zapier" | "make";
}

export interface WorkflowAskResponse {
    query: string;
    answer: string;
    sources: string[];
    confidence: "high" | "medium" | "low";
    model: string;
    retrieved_chunks: number;
    platform: "n8n" | "zapier" | "make";
}

export interface WorkflowDesignRequest {
    description: string;
    top_k?: number;
    platform?: "n8n" | "zapier" | "make";
}

export interface WorkflowDesignResponse {
    workflow_description: string;
    required_nodes: string[];
    suggested_structure: string;
    model: string;
    sources: string[];
    retrieved_chunks: number;
    platform: "n8n" | "zapier" | "make";
}

// Health Check Types
export interface WorkflowHealthResponse {
    status: "healthy" | "degraded";
    rag_retriever: boolean;
    llm_service: boolean;
    llm_backend: string | null;
}

// Error Types
export interface ApiError {
    detail: string | ValidationError[];
}

export interface ValidationError {
    type: string;
    loc: (string | number)[];
    msg: string;
    input: unknown;
    ctx?: Record<string, unknown>;
}

// ============================================
// Custom Error Class
// ============================================

export class WorkflowApiError extends Error {
    public status: number;
    public detail: string | ValidationError[];

    constructor(status: number, detail: string | ValidationError[]) {
        const message = typeof detail === "string" 
            ? detail 
            : "Validation error occurred";
        super(message);
        this.name = "WorkflowApiError";
        this.status = status;
        this.detail = detail;
    }

    get isValidationError(): boolean {
        return this.status === 422;
    }

    get isServiceUnavailable(): boolean {
        return this.status === 503;
    }

    get isNotFound(): boolean {
        return this.status === 404;
    }
}

// ============================================
// HTTP Client Utilities
// ============================================

async function handleResponse<T>(response: Response): Promise<T> {
    if (!response.ok) {
        let detail: string | ValidationError[];
        try {
            const errorData: ApiError = await response.json();
            detail = errorData.detail;
        } catch {
            detail = `HTTP ${response.status}: ${response.statusText}`;
        }
        throw new WorkflowApiError(response.status, detail);
    }
    return response.json();
}

async function apiGet<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    return handleResponse<T>(response);
}

async function apiPost<T, R>(endpoint: string, data: T): Promise<R> {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    return handleResponse<R>(response);
}

// ============================================
// API Service Functions
// ============================================

// ============================================
// Streaming Types
// ============================================

export interface StreamMetadata {
    sources: string[];
    confidence: string;
    model: string;
    retrieved_chunks: number;
    platform?: "n8n" | "zapier" | "make";
}

// ============================================
// SSE Helper Function
// ============================================

function processSSELine(
    line: string,
    onToken: (token: string) => void,
    onMetadata: (metadata: StreamMetadata) => void,
    onError: (error: string) => void,
    onDone: () => void
): void {
    // Skip empty lines and SSE comments (keep-alive signals)
    if (!line.trim() || line.startsWith(":")) return;
    
    // Handle "data: " prefix
    const dataPrefix = "data: ";
    const content = line.startsWith(dataPrefix) ? line.slice(dataPrefix.length) : line;
    
    if (!content.trim()) return;
    
    try {
        const data = JSON.parse(content);
        switch (data.type) {
            case "metadata":
                onMetadata({
                    sources: data.sources || [],
                    confidence: data.confidence || "medium",
                    model: data.model || "unknown",
                    retrieved_chunks: data.retrieved_chunks || 0,
                    platform: data.platform,
                });
                break;
            case "token":
                if (data.content) {
                    onToken(data.content);
                }
                break;
            case "error":
                onError(data.message || "Unknown error");
                break;
            case "done":
                onDone();
                break;
            default:
                // Log unknown event types for debugging
                console.warn("Unknown SSE event type:", data.type);
        }
    } catch (e) {
        // Log parse errors for debugging but don't break the stream
        console.warn("Failed to parse SSE data:", content, e);
    }
}

/**
 * Workflow Assistant API
 */
export const workflowService = {
    /**
     * Ask a question and get an AI-generated answer
     * This is the PRIMARY chat endpoint
     */
    async ask(request: WorkflowAskRequest): Promise<WorkflowAskResponse> {
        return apiPost("/api/workflows/ask", request);
    },

    /**
     * Ask a question with streaming response (SSE)
     */
    async askStream(
        request: WorkflowAskRequest,
        onToken: (token: string) => void,
        onMetadata: (metadata: StreamMetadata) => void,
        onError: (error: string) => void,
        onDone: () => void,
        abortController?: AbortController
    ): Promise<void> {
        const controller = abortController || new AbortController();
        
        const response = await fetch(`${API_BASE_URL}/api/workflows/ask/stream`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "text/event-stream",
            },
            body: JSON.stringify(request),
            signal: controller.signal,
        });

        if (!response.ok) {
            let detail: string;
            try {
                const errorData = await response.json();
                detail = errorData.detail || `HTTP ${response.status}`;
            } catch {
                detail = `HTTP ${response.status}: ${response.statusText}`;
            }
            throw new WorkflowApiError(response.status, detail);
        }

        const reader = response.body?.getReader();
        if (!reader) {
            throw new Error("No response body");
        }

        const decoder = new TextDecoder();
        let buffer = "";
        let doneReceived = false;
        
        // Wrapper to track done state
        const handleDone = () => {
            doneReceived = true;
            onDone();
        };

        try {
            while (true) {
                const { done, value } = await reader.read();
                
                if (done) {
                    // Process any remaining data in buffer
                    if (buffer.trim()) {
                        processSSELine(buffer, onToken, onMetadata, onError, handleDone);
                    }
                    break;
                }

                buffer += decoder.decode(value, { stream: true });
                
                // Process complete SSE messages (end with \n\n)
                let newlineIndex;
                while ((newlineIndex = buffer.indexOf("\n\n")) !== -1) {
                    const line = buffer.slice(0, newlineIndex);
                    buffer = buffer.slice(newlineIndex + 2);
                    
                    if (line.trim()) {
                        processSSELine(line, onToken, onMetadata, onError, handleDone);
                    }
                }
            }
        } catch (e) {
            // Handle abort/cancellation gracefully
            if (e instanceof Error && e.name === 'AbortError') {
                console.log("Stream aborted by user");
            } else {
                throw e;
            }
        } finally {
            reader.releaseLock();
            // Call onDone if backend didn't send explicit done signal
            if (!doneReceived) {
                onDone();
            }
        }
    },

    /**
     * Generate a structured workflow design from natural language
     */
    async design(request: WorkflowDesignRequest): Promise<WorkflowDesignResponse> {
        return apiPost("/api/workflows/design", request);
    },
};

// ============================================
// Convenience Functions for Chat Integration
// ============================================

export type ChatMode = "general" | "workflow_planning" | "advanced_automation" | "workflow_creation";

function platformForMode(mode: ChatMode): "n8n" | "zapier" | "make" {
    switch (mode) {
        case "workflow_planning":
            return "zapier";
        case "advanced_automation":
            return "make";
        case "workflow_creation":
        case "general":
        default:
            return "n8n";
    }
}

/**
 * Send a chat message and get a response based on the selected mode (non-streaming)
 */
export async function sendChatMessage(
    message: string,
    mode: ChatMode = "general"
): Promise<{
    answer: string;
    sources: string[];
    confidence: string;
    model: string;
    metadata?: WorkflowDesignResponse;
}> {
    const platform = platformForMode(mode);

    switch (mode) {
        case "workflow_planning":
        case "workflow_creation": {
            // Use the design endpoint for workflow-specific queries
            const designResponse = await workflowService.design({
                description: message,
                top_k: 5,
                platform,
            });
            return {
                answer: formatWorkflowDesignResponse(designResponse),
                sources: designResponse.sources || [],
                confidence: "high",
                model: designResponse.model,
                metadata: designResponse,
            };
        }
        case "general":
        default: {
            // Use the ask endpoint for general questions
            const askResponse = await workflowService.ask({
                query: message,
                top_k: 5,
                temperature: 0.7,
                max_answer_tokens: 2000,
                include_sources: true,
                platform,
            });
            return {
                answer: askResponse.answer,
                sources: askResponse.sources,
                confidence: askResponse.confidence,
                model: askResponse.model,
            };
        }
    }
}

/**
 * Send a chat message with streaming response
 */
export async function sendChatMessageStream(
    message: string,
    mode: ChatMode = "general",
    callbacks: {
        onToken: (token: string) => void;
        onMetadata: (metadata: StreamMetadata) => void;
        onError: (error: string) => void;
        onDone: () => void;
    }
): Promise<void> {
    const platform = platformForMode(mode);

    if (mode === "workflow_planning" || mode === "workflow_creation") {
        // Design endpoint doesn't support streaming, fallback to regular call
        const response = await sendChatMessage(message, mode);
        callbacks.onMetadata({
            sources: response.sources,
            confidence: response.confidence,
            model: response.model,
            retrieved_chunks: 0,
        });
        // Simulate streaming by yielding chunks
        const words = response.answer.split(" ");
        for (const word of words) {
            callbacks.onToken(word + " ");
            await new Promise((r) => setTimeout(r, 20));
        }
        callbacks.onDone();
        return;
    }

    // Use streaming endpoint for general mode
    await workflowService.askStream(
        {
            query: message,
            top_k: 5,
            temperature: 0.7,
            max_answer_tokens: 2000,
            include_sources: true,
            platform,
        },
        callbacks.onToken,
        callbacks.onMetadata,
        callbacks.onError,
        callbacks.onDone
    );
}

/**
 * Format a workflow design response into a readable string
 */
function formatWorkflowDesignResponse(response: WorkflowDesignResponse): string {
    const parts: string[] = [];
    
    if (response.workflow_description) {
        parts.push(response.workflow_description);
    }
    
    if (response.required_nodes && response.required_nodes.length > 0) {
        parts.push(`\n**Required Nodes:**\n${response.required_nodes.map(n => `- ${n}`).join("\n")}`);
    }
    
    if (response.suggested_structure) {
        parts.push(`\n**Suggested Structure:**\n${response.suggested_structure}`);
    }
    
    return parts.join("\n");
}

// ============================================
// Default Export
// ============================================

const workflowApi = {
    workflows: workflowService,
    sendChatMessage,
};

export default workflowApi;
