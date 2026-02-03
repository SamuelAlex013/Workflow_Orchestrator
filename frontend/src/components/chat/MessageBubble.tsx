"use client";

import { cn } from "@/lib/utils";
import { Sparkles } from "lucide-react";
import { useUser } from "@clerk/nextjs";
import Image from "next/image";

interface Message {
    id: string;
    sender: "user" | "assistant";
    content: string;
    createdAt: string;
}

interface MessageBubbleProps {
    message: Message;
}

export function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.sender === "user";
    const { user } = useUser();

    return (
        <div className={cn("flex gap-4 mb-6 animate-in fade-in slide-in-from-bottom-4 duration-500", isUser && "justify-end")}>
            {!isUser && (
                <div className="flex-shrink-0 w-9 h-9 rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center shadow-md">
                    <Sparkles size={16} className="text-white" />
                </div>
            )}

            <div
                className={cn(
                    "max-w-[75%] rounded-2xl px-5 py-3.5 shadow-sm",
                    isUser
                        ? "bg-gradient-to-br from-purple-500 to-purple-600 text-white rounded-tr-sm"
                        : "bg-gray-100 dark:bg-gray-800/50 text-gray-900 dark:text-white rounded-tl-sm backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50"
                )}
            >
                <p className="text-[15px] leading-relaxed whitespace-pre-wrap">{message.content}</p>
                <div className="text-xs opacity-60 mt-2">{new Date(message.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
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
