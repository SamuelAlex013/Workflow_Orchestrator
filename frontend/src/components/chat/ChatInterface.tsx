"use client";

import { useState, useEffect, useRef } from "react";
import { MessageBubble } from "./MessageBubble";
import { InputArea } from "./InputArea";
import { Header } from "../header/Header";
import { AlertCircle } from "lucide-react";

type Mode = "general" | "workflow_planning";

interface Message {
    id: string;
    sender: "user" | "assistant";
    content: string;
    createdAt: string;
}

interface ChatInterfaceProps {
    conversationId?: string;
    initialMessages?: Message[];
    initialMode?: Mode;
}

export function ChatInterface({
    conversationId,
    initialMessages = [],
    initialMode = "general",
}: ChatInterfaceProps) {
    const [messages, setMessages] = useState<Message[]>(initialMessages);
    const [mode, setMode] = useState<Mode>(initialMode);
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    const handleSendMessage = async (content: string) => {
        const userMessage: Message = {
            id: Date.now().toString(),
            sender: "user",
            content,
            createdAt: new Date().toISOString(),
        };

        setMessages((prev) => [...prev, userMessage]);
        setIsLoading(true);

        // Simulate AI response (replace with actual API call)
        setTimeout(() => {
            const assistantMessage: Message = {
                id: (Date.now() + 1).toString(),
                sender: "assistant",
                content:
                    mode === "workflow_planning"
                        ? `I'll help you plan this workflow. Here's a structured approach:\n\n1. Identify the trigger\n2. Define the data flow\n3. Map API endpoints\n4. Set up error handling\n\nLet me know which step you'd like to explore first!`
                        : `This is a simulated response. In production, this would connect to your AI backend to provide intelligent assistance with workflow automation and n8n concepts.`,
                createdAt: new Date().toISOString(),
            };
            setMessages((prev) => [...prev, assistantMessage]);
            setIsLoading(false);
        }, 1000);
    };

    const handleModeChange = (newMode: Mode) => {
        setMode(newMode);
    };

    return (
        <div className="flex flex-col h-screen">
            <Header mode={mode} onModeChange={handleModeChange} />

            {/* Mode Indicator */}
            {mode === "workflow_planning" && (
                <div className="bg-purple-100 dark:bg-purple-950 border-b border-purple-200 dark:border-purple-900 px-6 py-3">
                    <div className="max-w-4xl mx-auto flex items-center gap-2 text-sm text-purple-900 dark:text-purple-200">
                        <AlertCircle size={16} />
                        <span className="font-medium">Workflow Planning Mode</span>
                        <span className="text-purple-700 dark:text-purple-400">
                            - Structured planning for automation workflows
                        </span>
                    </div>
                </div>
            )}

            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto bg-white dark:bg-gray-950">
                <div className="max-w-4xl mx-auto px-6 py-8">
                    {messages.length === 0 ? (
                        <div className="text-center py-12">
                            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                                Welcome to Workflow Orchestrator
                            </h2>
                            <p className="text-gray-600 dark:text-gray-400">
                                {mode === "general"
                                    ? "Ask me anything about workflow automation and n8n"
                                    : "Let's plan your workflow step by step"}
                            </p>
                        </div>
                    ) : (
                        <>
                            {messages.map((message) => (
                                <MessageBubble key={message.id} message={message} mode={mode} />
                            ))}
                            {isLoading && (
                                <div className="flex gap-4 mb-6">
                                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                                        <div className="w-2 h-2 bg-white rounded-full animate-pulse" />
                                    </div>
                                    <div className="bg-gray-100 dark:bg-gray-800 rounded-2xl rounded-tl-none px-4 py-3">
                                        <div className="flex gap-1">
                                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
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
