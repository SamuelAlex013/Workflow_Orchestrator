"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { MessageBubble } from "./MessageBubble";
import { InputArea } from "./InputArea";
import { sendChatMessageStream, WorkflowApiError, type ChatMode, type StreamMetadata } from "@/lib/workflowApi";

type Mode = "general" | "workflow_planning" | "advanced_automation";

interface Message {
    id: string;
    sender: "user" | "assistant";
    content: string;
    createdAt: string;
    sources?: string[];
    confidence?: string;
    model?: string;
    isError?: boolean;
    isStreaming?: boolean;
}

interface ChatInterfaceProps {
    conversationId?: string;
    initialMessages?: Message[];
}

export function ChatInterface({
    conversationId,
    initialMessages = [],
}: ChatInterfaceProps) {
    const [messages, setMessages] = useState<Message[]>(initialMessages);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [streamingMessageId, setStreamingMessageId] = useState<string | null>(null);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    // Clear error after 5 seconds
    useEffect(() => {
        if (error) {
            const timer = setTimeout(() => setError(null), 5000);
            return () => clearTimeout(timer);
        }
    }, [error]);

    const handleSendMessage = useCallback(async (content: string, mode?: Mode) => {
        const userMessage: Message = {
            id: Date.now().toString(),
            sender: "user",
            content,
            createdAt: new Date().toISOString(),
        };

        const assistantMessageId = (Date.now() + 1).toString();
        
        // Create initial empty assistant message for streaming
        const assistantMessage: Message = {
            id: assistantMessageId,
            sender: "assistant",
            content: "",
            createdAt: new Date().toISOString(),
            isStreaming: true,
        };

        setMessages((prev) => [...prev, userMessage, assistantMessage]);
        setIsLoading(true);
        setStreamingMessageId(assistantMessageId);
        setError(null);

        try {
            // Map frontend mode to API mode
            const apiMode: ChatMode = mode === "workflow_planning" ? "workflow_planning" : "general";
            
            // Call the streaming API
            await sendChatMessageStream(content, apiMode, {
                onToken: (token: string) => {
                    setMessages((prev) => 
                        prev.map((msg) => 
                            msg.id === assistantMessageId 
                                ? { ...msg, content: msg.content + token }
                                : msg
                        )
                    );
                },
                onMetadata: (metadata: StreamMetadata) => {
                    setMessages((prev) => 
                        prev.map((msg) => 
                            msg.id === assistantMessageId 
                                ? { 
                                    ...msg, 
                                    sources: metadata.sources,
                                    confidence: metadata.confidence,
                                    model: metadata.model,
                                }
                                : msg
                        )
                    );
                },
                onError: (errorMsg: string) => {
                    setMessages((prev) => 
                        prev.map((msg) => 
                            msg.id === assistantMessageId 
                                ? { 
                                    ...msg, 
                                    content: `❌ **Error**\n\n${errorMsg}`,
                                    isError: true,
                                    isStreaming: false,
                                }
                                : msg
                        )
                    );
                    setError(errorMsg);
                },
                onDone: () => {
                    setMessages((prev) => 
                        prev.map((msg) => 
                            msg.id === assistantMessageId 
                                ? { ...msg, isStreaming: false }
                                : msg
                        )
                    );
                    setStreamingMessageId(null);
                },
            });
        } catch (err) {
            console.error("API Error:", err);
            
            let errorContent: string;
            
            if (err instanceof WorkflowApiError) {
                if (err.isServiceUnavailable) {
                    errorContent = "⚠️ **Service Unavailable**\n\nThe AI services are still initializing. Please wait a moment and try again.\n\nMake sure the backend server is running on port 8000.";
                } else if (err.isNotFound) {
                    errorContent = "🔍 **No Relevant Information Found**\n\nI couldn't find relevant documentation to answer your question. Try rephrasing or asking about a different n8n topic.";
                } else if (err.isValidationError) {
                    errorContent = "❌ **Invalid Request**\n\nYour message couldn't be processed. Please ensure your query is between 1-1000 characters.";
                } else {
                    errorContent = `❌ **Error**\n\n${err.message}`;
                }
            } else if (err instanceof TypeError && err.message.includes("fetch")) {
                errorContent = "🔌 **Connection Failed**\n\nCannot connect to the backend server.\n\nPlease ensure:\n1. The backend is running (`python run_server.py`)\n2. It's accessible at `http://localhost:8000`";
            } else {
                errorContent = "❌ **Unexpected Error**\n\nSomething went wrong. Please try again.";
            }

            setMessages((prev) => 
                prev.map((msg) => 
                    msg.id === assistantMessageId 
                        ? { 
                            ...msg, 
                            content: errorContent,
                            isError: true,
                            isStreaming: false,
                        }
                        : msg
                )
            );
            setError(err instanceof Error ? err.message : "Unknown error");
        } finally {
            setIsLoading(false);
            setStreamingMessageId(null);
        }
    }, []);

    return (
        <div className="flex flex-col h-full">
            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto bg-slate-50 dark:bg-[#0F172A]">
                <div className="max-w-4xl mx-auto px-6 py-8">
                    {messages.length === 0 ? (
                        <div className="text-center py-16">
                            <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-indigo-500 dark:bg-sky-500 mb-4 shadow-lg shadow-indigo-500/25 dark:shadow-sky-500/25">
                                <span className="text-3xl">🤖</span>
                            </div>
                            <h2 className="text-2xl font-semibold text-slate-900 dark:text-white mb-2">
                                Welcome to Workflow Orchestrator
                            </h2>
                            <p className="text-slate-600 dark:text-slate-400 max-w-md mx-auto">
                                Chat with your AI assistant to plan and create powerful workflow automations.
                                Type @ to switch modes or select a model above.
                            </p>
                            <div className="mt-6 flex flex-wrap justify-center gap-2">
                                <div className="px-3 py-1.5 rounded-lg bg-indigo-100 dark:bg-sky-900/30 text-indigo-700 dark:text-sky-300 text-sm font-medium">
                                    Workflow Planning
                                </div>
                                <div className="px-3 py-1.5 rounded-lg bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300 text-sm font-medium">
                                    n8n Integration
                                </div>
                                <div className="px-3 py-1.5 rounded-lg bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300 text-sm font-medium">
                                    Automation Guidance
                                </div>
                            </div>
                        </div>
                    ) : (
                        <>
                            {messages.map((message) => (
                                <MessageBubble key={message.id} message={message} />
                            ))}
                            {isLoading && !streamingMessageId && (
                                <div className="flex gap-4 mb-6 animate-in fade-in duration-300">
                                    <div className="flex-shrink-0 w-9 h-9 rounded-xl bg-indigo-500 dark:bg-sky-500 flex items-center justify-center shadow-md">
                                        <div className="w-2 h-2 bg-white rounded-full animate-pulse" />
                                    </div>
                                    <div className="bg-white dark:bg-[#1E293B] rounded-2xl rounded-tl-sm px-5 py-3 border border-slate-200 dark:border-slate-700/50">
                                        <div className="flex gap-1.5">
                                            <span className="w-2 h-2 bg-indigo-400 dark:bg-sky-400 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                            <span className="w-2 h-2 bg-indigo-400 dark:bg-sky-400 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                            <span className="w-2 h-2 bg-indigo-400 dark:bg-sky-400 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                                        </div>
                                    </div>
                                </div>
                            )}
                        </>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>

            <InputArea onSendMessage={handleSendMessage} disabled={isLoading} />
        </div>
    );
}
