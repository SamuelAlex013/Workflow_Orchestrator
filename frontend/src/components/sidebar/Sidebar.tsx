"use client";

import { UserButton } from "@clerk/nextjs";
import { MessageSquarePlus, Settings } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

interface Conversation {
    id: string;
    title: string;
    mode: string;
    updatedAt: string;
}

interface SidebarProps {
    conversations: Conversation[];
}

export function Sidebar({ conversations }: SidebarProps) {
    const pathname = usePathname();

    return (
        <div className="w-64 h-screen bg-gray-50 dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col">
            {/* Header */}
            <div className="p-4 border-b border-gray-200 dark:border-gray-800">
                <h1 className="text-xl font-bold text-gray-900 dark:text-white">
                    Workflow Orchestrator
                </h1>
            </div>

            {/* New Chat Button */}
            <div className="p-3">
                <Link
                    href="/chat"
                    className="w-full flex items-center gap-2 px-4 py-3 rounded-lg bg-primary hover:bg-primary-hover text-white font-medium transition-all hover:scale-[1.02] active:scale-[0.98]"
                >
                    <MessageSquarePlus size={20} />
                    New Conversation
                </Link>
            </div>

            {/* Conversations List */}
            <div className="flex-1 overflow-y-auto px-3">
                <div className="space-y-1">
                    {conversations.map((conv) => {
                        const isActive = pathname.includes(conv.id);
                        return (
                            <Link
                                key={conv.id}
                                href={`/chat/${conv.id}`}
                                className={cn(
                                    "block px-4 py-3 rounded-lg transition-all hover:bg-gray-100 dark:hover:bg-gray-800",
                                    isActive && "bg-gray-200 dark:bg-gray-800"
                                )}
                            >
                                <div className="flex items-start justify-between">
                                    <div className="flex-1 min-w-0">
                                        <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                                            {conv.title || "Untitled Conversation"}
                                        </p>
                                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                                            {conv.mode === "workflow_planning" ? "Workflow Planning" : "General"}
                                        </p>
                                    </div>
                                </div>
                            </Link>
                        );
                    })}
                </div>
            </div>

            {/* User Profile */}
            <div className="p-4 border-t border-gray-200 dark:border-gray-800 flex items-center justify-between">
                <UserButton
                    appearance={{
                        elements: {
                            avatarBox: "w-10 h-10"
                        }
                    }}
                />
                <Link
                    href="/settings"
                    className="p-2 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors"
                >
                    <Settings size={20} className="text-gray-600 dark:text-gray-400" />
                </Link>
            </div>
        </div>
    );
}
