"use client";

import { useState, useEffect, useRef } from "react";
import { MessageBubble } from "./MessageBubble";
import { InputArea } from "./InputArea";

type Mode = "general" | "workflow_planning" | "workflow_creation";

interface Message {
    id: string;
    sender: "user" | "assistant";
    content: string;
    createdAt: string;
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
    const messagesEndRef = useRef<HTMLDivElement>(null);

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    const handleSendMessage = async (content: string, mode?: Mode) => {
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
                        : `This is a simulated response in ${mode || 'general'} mode. In production, this would connect to your AI backend to provide intelligent assistance with workflow automation and n8n concepts.`,
                createdAt: new Date().toISOString(),
            };
            setMessages((prev) => [...prev, assistantMessage]);
            setIsLoading(false);
        }, 1000);
    };

    return (
        <div className="flex flex-col h-full">
            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto bg-gradient-to-b from-white to-gray-50/50 dark:from-gray-950 dark:to-gray-900/50">
                <div className="max-w-4xl mx-auto px-6 py-8">
                    {messages.length === 0 ? (
                        <div className="text-center py-16">
                            <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-purple-600 mb-4 shadow-lg shadow-purple-500/30">
                                <span className="text-3xl">🤖</span>
                            </div>
                            <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mb-2">
                                Welcome to Workflow Orchestrator
                            </h2>
                            <p className="text-gray-600 dark:text-gray-400 max-w-md mx-auto">
                                Chat with your AI assistant to plan and create powerful workflow automations.
                                Type @ to switch modes or select a model above.
                            </p>
                            <div className="mt-6 flex flex-wrap justify-center gap-2">
                                <div className="px-3 py-1.5 rounded-lg bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 text-sm font-medium">
                                    Workflow Planning
                                </div>
                                <div className="px-3 py-1.5 rounded-lg bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-sm font-medium">
                                    n8n Integration
                                </div>
                                <div className="px-3 py-1.5 rounded-lg bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 text-sm font-medium">
                                    Automation Guidance
                                </div>
                            </div>
                        </div>
                    ) : (
                        <>
                            {messages.map((message) => (
                                <MessageBubble key={message.id} message={message} />
                            ))}
                            {isLoading && (
                                <div className="flex gap-4 mb-6 animate-in fade-in duration-300">
                                    <div className="flex-shrink-0 w-9 h-9 rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center shadow-md">
                                        <div className="w-2 h-2 bg-white rounded-full animate-pulse" />
                                    </div>
                                    <div className="bg-gray-100 dark:bg-gray-800/50 rounded-2xl rounded-tl-sm px-5 py-3 backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50">
                                        <div className="flex gap-1.5">
                                            <span className="w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                            <span className="w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                            <span className="w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
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
