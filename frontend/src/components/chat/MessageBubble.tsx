"use client";

import { cn } from "@/lib/utils";
import { User, Bot } from "lucide-react";

interface Message {
    id: string;
    sender: "user" | "assistant";
    content: string;
    createdAt: string;
}

interface MessageBubbleProps {
    message: Message;
    mode: "general" | "workflow_planning";
}

export function MessageBubble({ message, mode }: MessageBubbleProps) {
    const isUser = message.sender === "user";

    return (
        <div className={cn("flex gap-4 mb-6", isUser && "justify-end")}>
            {!isUser && (
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center">
                    <Bot size={18} className="text-white" />
                </div>
            )}

            <div
                className={cn(
                    "max-w-[70%] rounded-2xl px-4 py-3",
                    isUser
                        ? "bg-primary text-white rounded-tr-none"
                        : mode === "workflow_planning"
                            ? "bg-purple-50 dark:bg-purple-950 text-gray-900 dark:text-white rounded-tl-none"
                            : "bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white rounded-tl-none"
                )}
            >
                <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
            </div>

            {isUser && (
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-700 dark:bg-gray-600 flex items-center justify-center">
                    <User size={18} className="text-white" />
                </div>
            )}
        </div>
    );
}
