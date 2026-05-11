"use client";

import { cn } from "@/lib/utils";
import { Sparkles, AlertTriangle, BookOpen, ChevronDown, ChevronUp } from "lucide-react";
import { useUser } from "@clerk/nextjs";
import Image from "next/image";
import { useState } from "react";
import ReactMarkdown from "react-markdown";

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

interface MessageBubbleProps {
    message: Message;
}

export function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.sender === "user";
    const { user } = useUser();
    const [showSources, setShowSources] = useState(false);
    const formattedTime = message.isStreaming
        ? "Generating..."
        : new Date(message.createdAt)
            .toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            .toUpperCase();

    return (
        <div className={cn("flex gap-4 mb-6 animate-in fade-in slide-in-from-bottom-4 duration-500", isUser && "justify-end")}>
            {!isUser && (
                <div className={cn(
                    "flex-shrink-0 w-9 h-9 rounded-xl flex items-center justify-center shadow-md",
                    message.isError 
                        ? "bg-rose-500" 
                        : "bg-indigo-500 dark:bg-sky-500"
                )}>
                    {message.isError ? (
                        <AlertTriangle size={16} className="text-white" />
                    ) : (
                        <Sparkles size={16} className="text-white" />
                    )}
                </div>
            )}

            <div className="max-w-[75%] flex flex-col gap-2">
                <div
                    className={cn(
                        "rounded-2xl px-5 py-3.5 shadow-sm",
                        isUser
                            ? "bg-indigo-500 dark:bg-sky-500 text-white rounded-tr-sm"
                            : message.isError
                                ? "bg-rose-50 dark:bg-rose-950/30 text-slate-900 dark:text-white rounded-tl-sm border border-rose-200 dark:border-rose-800/50"
                                : "bg-white dark:bg-[#1E293B] text-slate-900 dark:text-slate-100 rounded-tl-sm border border-slate-200 dark:border-slate-700/50"
                    )}
                >
                    {/* Markdown content rendering */}
                    <div className={cn(
                        "prose prose-sm max-w-none",
                        isUser 
                            ? "prose-invert prose-p:text-white prose-headings:text-white prose-strong:text-white prose-li:text-white" 
                            : "dark:prose-invert prose-p:text-gray-900 dark:prose-p:text-gray-100 prose-headings:text-gray-900 dark:prose-headings:text-white prose-strong:text-gray-900 dark:prose-strong:text-white prose-li:text-gray-800 dark:prose-li:text-gray-200",
                        "prose-p:my-1 prose-headings:my-2 prose-ul:my-1 prose-ol:my-1 prose-li:my-0.5",
                        "prose-h1:text-lg prose-h2:text-base prose-h3:text-sm prose-h4:text-sm",
                        "prose-code:bg-gray-200 dark:prose-code:bg-gray-700 prose-code:px-1 prose-code:py-0.5 prose-code:rounded prose-code:text-sm prose-code:before:content-none prose-code:after:content-none",
                        "prose-pre:bg-gray-900 dark:prose-pre:bg-gray-950 prose-pre:text-gray-100 prose-pre:rounded-lg prose-pre:p-3 prose-pre:my-2",
                        "prose-hr:my-3 prose-hr:border-gray-300 dark:prose-hr:border-gray-600"
                    )}>
                        <ReactMarkdown>
                            {message.content}
                        </ReactMarkdown>
                        {/* Streaming cursor */}
                        {message.isStreaming && (
                            <span className="inline-block w-2 h-4 ml-1 bg-indigo-500 dark:bg-sky-400 animate-pulse rounded-sm" />
                        )}
                    </div>
                    
                    {/* Metadata row - only show when not streaming or has content */}
                    {(!message.isStreaming || message.content) && (
                        <div className="flex items-center justify-between mt-2 pt-2 border-t border-gray-200/30 dark:border-gray-700/30">
                            <span className="text-xs opacity-60">
                                {formattedTime}
                            </span>
                        
                            {/* Confidence & Model indicator for assistant messages */}
                            {!isUser && message.confidence && !message.isError && !message.isStreaming && (
                                <div className="flex items-center gap-2">
                                    <span className={cn(
                                        "text-xs px-2 py-0.5 rounded-full font-medium",
                                        message.confidence === "high" && "bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400",
                                        message.confidence === "medium" && "bg-yellow-100 dark:bg-yellow-900/30 text-yellow-700 dark:text-yellow-400",
                                        message.confidence === "low" && "bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-400"
                                    )}>
                                        {message.confidence}
                                    </span>
                                    {message.model && (
                                        <span className="text-xs opacity-50">{message.model}</span>
                                    )}
                                </div>
                            )}
                        </div>
                    )}
                </div>

                {/* Sources accordion */}
                {!isUser && message.sources && message.sources.length > 0 && (
                    <div className="ml-1">
                        <button
                            onClick={() => setShowSources(!showSources)}
                            className="flex items-center gap-1.5 text-xs text-gray-500 dark:text-gray-400 hover:text-purple-600 dark:hover:text-purple-400 transition-colors"
                        >
                            <BookOpen size={12} />
                            <span>{message.sources.length} source{message.sources.length > 1 ? 's' : ''}</span>
                            {showSources ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
                        </button>
                        
                        {showSources && (
                            <div className="mt-2 p-3 bg-gray-50 dark:bg-gray-900/50 rounded-lg border border-gray-200 dark:border-gray-700/50 animate-in fade-in slide-in-from-top-2 duration-200">
                                <ul className="space-y-1">
                                    {message.sources.map((source, idx) => (
                                        <li key={idx} className="text-xs text-gray-600 dark:text-gray-400 flex items-start gap-2">
                                            <span className="text-purple-500 mt-0.5">•</span>
                                            <span>{source}</span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </div>
                )}
            </div>

            {isUser && (
                <div className="flex-shrink-0">
                    {user?.imageUrl ? (
                        <Image
                            src={user.imageUrl}
                            alt={user.fullName || "User"}
                            width={36}
                            height={36}
                            className="rounded-xl shadow-md"
                        />
                    ) : (
                        <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-gray-700 to-gray-800 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center shadow-md">
                            <span className="text-white font-medium text-sm">
                                {user?.firstName?.[0] || "U"}
                            </span>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}
